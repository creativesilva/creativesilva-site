#!/usr/bin/env python3
"""Build the MODULE_DOCS map for the curriculum catalog's "Module Documents" accordion.

Associates each live module (from curriculum.html MODULES) with its downloadable documents
in assets/course-documents/ (capture lists, reflections, project folders, worksheets, guides,
assets) BY the canonical doc prefix. The prefix is the module's overview-filename slug, with an
alias table for the handful whose slug != doc prefix. Course-aware: photo2 modules get the
Photo2 reflection / Photo2 project folder when present.

Slides (-Slides-), syllabi, and lab agreements are intentionally excluded (they live in the
Slide Decks accordion and the course-level Course Documents row).

Writes window.MODULE_DOCS = {...} between the MODULE_DOCS markers in curriculum.html.

Usage: python3 tools/build-module-docs.py [--write]   (default: dry-run, prints the mapping)
"""
import os, re, sys, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUR = os.path.join(ROOT, "curriculum.html")
DOCDIR = os.path.join(ROOT, "assets", "course-documents")
SITE = "https://www.creativesilva.com"
WRITE = "--write" in sys.argv

# Overview slug -> canonical doc prefix, for modules whose slug does not match the doc filename.
ALIAS = {
    "ocf": "Off-Camera-Flash",
    "composition": "Composition-Photo-Walk",      # photo2 Composition Photo Walk
    "composition-concepts": "Composition-Concepts",
    "preset": "Build-Your-Own-Preset",
    "character-form-color": "Character-Design-Form-Color",
    "panther-quarter": "Panther-of-the-Quarter",
    "get-to-know-illustrator": None,              # no docs yet
    "make-your-mark": "Design-A-Sticker",         # URL slug stays make-your-mark; docs use the display name
}

def norm(u):
    return (u or "").lstrip("/")

def slug_of(url):
    # curriculum/shared/photo1-monochromatic-photography-overview.html -> monochromatic-photography
    base = os.path.basename(url).replace("-overview.html", "")
    base = re.sub(r"^(photo1|photo2|da1|da2|digarts1|digarts2|yearbook)-", "", base)
    return base

def title_hyphen(slug):
    # monochromatic-photography -> Monochromatic-Photography (preserve known lowercase joiners)
    small = {"of", "the", "your", "own", "and"}
    parts = slug.split("-")
    return "-".join(p if p in small else (p[:1].upper() + p[1:]) for p in parts)

# ---- index the doc directory (match filenames case-insensitively, keep real casing for the URL) ----
docs = [os.path.basename(p) for p in glob.glob(os.path.join(DOCDIR, "*")) if os.path.isfile(p)]
EXCLUDE = re.compile(r"-Slides-|Syllabus|Lab-and-Equipment|Syllabus-and-Lab", re.I)
docs = [d for d in docs if not EXCLUDE.search(d)]
DOCS_CI = {d.lower(): d for d in docs}

def resolve(name):
    return DOCS_CI.get(name.lower())

def has(name):
    return name.lower() in DOCS_CI

# Odd-named docs that do not follow <Prefix>-Type, keyed by overview slug -> [(label, exact filename)]
EXTRA = {
    "color-theory": [("Worksheet &middot; English", "Color-Analysis-Worksheet-EN.docx"),
                     ("Worksheet &middot; Spanish", "Color-Analysis-Worksheet-ES.docx")],
    "lightroom-editing": [("Import Guide (PDF)", "Lightroom-Import-Guide.pdf")],
}

def doc_entry(prefix, isP2):
    """Return the ordered [ {label, file} ] for a module with this prefix + course."""
    out = []
    enc = lambda f: SITE + "/assets/course-documents/" + f.replace(" ", "%20")
    def add(label, fname):
        actual = resolve(fname)
        if actual:
            out.append({"label": label, "file": enc(actual)})
            return True
        return False
    # 1) Capture list (shared EN/ES) -- Chris's priority, listed first
    add("Capture List &middot; English", f"{prefix}-Capture-List-EN.docx")
    add("Capture List &middot; Spanish", f"{prefix}-Capture-List-ES.docx")
    # 2) Reflection (course-aware: photo2 uses -Photo2- when present)
    if isP2 and has(f"{prefix}-Photo2-Reflection-EN.docx"):
        add("Reflection &middot; English", f"{prefix}-Photo2-Reflection-EN.docx")
        add("Reflection &middot; Spanish", f"{prefix}-Photo2-Reflection-ES.docx")
    else:
        add("Reflection &middot; English", f"{prefix}-Reflection-EN.docx")
        add("Reflection &middot; Spanish", f"{prefix}-Reflection-ES.docx")
    # 3) Worksheet (shared EN/ES)
    add("Worksheet &middot; English", f"{prefix}-Worksheet-EN.docx")
    add("Worksheet &middot; Spanish", f"{prefix}-Worksheet-ES.docx")
    # 4) Guide (PDF)
    add("Guide (PDF)", f"{prefix}-Guide.pdf")
    # 5) Project folder (course-aware)
    if isP2:
        if not add("Project Folder (ZIP)", f"{prefix}-Project-Folder-Photo2.zip"):
            add("Project Folder (ZIP)", f"{prefix}-Project-Folder.zip")
    else:
        if not add("Project Folder (ZIP)", f"{prefix}-Project-Folder-Photo1.zip"):
            add("Project Folder (ZIP)", f"{prefix}-Project-Folder.zip")
    # 6) Assets bundle
    add("Assets (ZIP)", f"{prefix}-Assets.zip")
    return out

# ---- parse MODULES entries from curriculum.html ----
html = open(CUR, encoding="utf-8").read()
# object literals inside the MODULES array; capture course, name, url
entries = re.findall(r"\{\s*course:\s*\"([^\"]+)\"[^}]*?name:\s*\"([^\"]+)\"[^}]*?url:\s*\"([^\"]+)\"[^}]*\}", html)

MODULE_DOCS = {}
report = []
used = set()
for course, name, url in entries:
    if "/mrc/" in url or course.startswith("mrc"):
        continue
    if not re.match(r"^(Module|Project)\s*\d", name):
        continue
    slug = slug_of(url)
    if slug in ALIAS:
        prefix = ALIAS[slug]
    else:
        prefix = title_hyphen(slug)
    if prefix is None:
        report.append(("--  no docs", name, url, "(alias=None)"))
        continue
    isP2 = course.startswith("photo2") or os.path.basename(url).startswith("photo2-")
    ent = doc_entry(prefix, isP2)
    for label, fname in EXTRA.get(slug, []):
        actual = resolve(fname)
        if actual and not any(e["file"].endswith(actual.replace(" ", "%20")) for e in ent):
            ent.append({"label": label, "file": SITE + "/assets/course-documents/" + actual.replace(" ", "%20")})
    if ent:
        MODULE_DOCS[norm(url)] = ent
        for e in ent:
            used.add(e["file"].split("/")[-1].replace("%20", " "))
        report.append((f"{len(ent):2d} docs", name, prefix, ", ".join(e["label"].replace("&middot;","·").replace("&amp;","&") for e in ent)))
    else:
        report.append(("00  MISSING", name, prefix, "(no matching docs found)"))

# ---- report ----
print("=== module -> docs mapping ===")
for r in sorted(report):
    print(f"[{r[0]}] {r[1]:48} <{r[2]}>")
    if len(r) > 3 and r[3] and not r[3].startswith("("):
        print(f"        {r[3]}")
    elif len(r) > 3:
        print(f"        {r[3]}")
print(f"\n{len(MODULE_DOCS)} modules with docs.")
# unused module-type docs (reflection/capture/project/worksheet/guide not matched to any module)
modish = [d for d in docs if re.search(r"-(Reflection|Capture-List|Project-Folder|Worksheet|Guide|Assets)", d) and "Syllabus" not in d]
unused = sorted(set(modish) - used)
print(f"\n=== module-type docs NOT matched to any module ({len(unused)}) ===")
for u in unused:
    print("  " + u)

if WRITE:
    block = "var MODULE_DOCS = " + json.dumps(MODULE_DOCS, ensure_ascii=False, indent=0).replace("\n", "") + ";"
    START, END = "/* MODULE_DOCS_START */", "/* MODULE_DOCS_END */"
    assert START in html and END in html, "MODULE_DOCS markers not found in curriculum.html"
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), START + "\n    " + block + "\n    " + END, html, flags=re.S)
    open(CUR, "w", encoding="utf-8").write(new)
    print(f"\nWROTE MODULE_DOCS ({len(MODULE_DOCS)} modules) into curriculum.html")
else:
    print("\n(dry run; pass --write to update curriculum.html)")
