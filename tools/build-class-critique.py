#!/usr/bin/env python3
"""
build-class-critique.py  -  Build a PVHS critique gallery from Canvas photo exports.

Student photos + names are FERPA PII, so NOTHING here is ever committed or hosted on the public site.
This runs locally on Mr. Silva's Mac: it reads the roster (local, PII) and the Drive photo folders,
matches each photo to a student + period, makes lean projector-sized copies, packages one gallery as a
ZIP, and uploads it to the Command Center's authed /api/critique/upload route, where it lives on the
private disk behind Google sign-in (same protection as the roll sheet). curriculum.html links to the
viewer; critique.html (served by the Command Center) projects it.

Usage:
  python3 tools/build-class-critique.py \
      --title "Spooky Portraits" --slug spooky-portraits \
      --match Spooky_Portraits                 # finds every incoming folder with that in its name
  # or point at explicit folders with one or more --folder "<path>"
  # add --no-upload to only build the package locally (for preview); --out <dir> to keep it.

The Command Center API key (for upload) is read from, in order: --api-key, env CC_API_KEY,
~/.config/creativesilva/cc_api_key. With no key, the ZIP is written out and instructions printed.
"""
import argparse, glob, json, os, re, sys, tempfile, zipfile, time, shutil
from collections import defaultdict
from urllib import request as urlrequest

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow is required:  python3 -m pip install Pillow")

HOME = os.path.expanduser("~")
INCOMING = os.path.join(HOME, "Library/CloudStorage/GoogleDrive-creativesilva1@gmail.com/My Drive/creativesilva_incoming")
ROSTER_GLOB = os.path.join(HOME, "RIVA_CODE/01_TEACHING/Class Rosters & Seating Charts/2026-2027_Fall/data/*Roster_Data_v*.json")
CC_BASE = os.environ.get("CC_BASE", "https://command.creativesilva.com")
SUBTITLE = "Pioneer Valley High School"
PERIOD_ORDER = ["1", "2", "3", "4", "5", "6", "7"]
THUMB_EDGE, THUMB_Q = 640, 72
FULL_EDGE,  FULL_Q  = 1920, 82
IMG_EXT = (".jpg", ".jpeg", ".JPG", ".JPEG", ".png", ".PNG", ".heic", ".HEIC")
PH_EXT  = IMG_EXT + (".webp", ".WEBP")


# ----- roster matching (validated: matches names incl. compound surnames, pulls the period) -----
def norm(s):            return re.sub(r"[^a-z]", "", (s or "").lower())
def strip_init(fn):     return re.sub(r"\s+[A-Za-z]\.?$", "", (fn or "").strip())

def clean_name(call_name, first, last):
    """A tidy 'First Last' for display: prefer call name, drop (parentheticals), Liz/Lizzie -> Liz,
    and a trailing middle initial."""
    base = (call_name or "").strip() or (first or "").strip()
    base = re.sub(r"\([^)]*\)", "", base)          # drop "(Leo)"
    base = base.split("/")[0]                       # "Liz/Lizzie" -> "Liz"
    base = re.sub(r"\s+[A-Za-z]\.?$", "", base.strip())   # drop trailing middle initial
    base = re.sub(r"\s+", " ", base).strip()
    return f"{base} {str(last).strip()}".strip()

def load_roster():
    paths = sorted(glob.glob(ROSTER_GLOB), key=lambda p: int(re.search(r"_v(\d+)\.json$", p).group(1)))
    if not paths:
        sys.exit(f"No roster found at {ROSTER_GLOB}")
    path = paths[-1]
    raw = json.load(open(path))
    arr = raw.get("students") if isinstance(raw, dict) else raw
    if not arr:
        arr = next((v for v in raw.values() if isinstance(v, list) and v and isinstance(v[0], dict) and "last_name" in v[0]), None) if isinstance(raw, dict) else None
    if not arr:
        sys.exit(f"Could not find the student array in {path}")
    keymap = {}        # normalized name key -> record (for matching a photo filename to a student)
    rows = []          # one active roster row per enrollment (for missing-work detection)
    for s in arr:
        last  = str(s.get("last_name", "")).strip()
        first = str(s.get("first_name", "")).strip()
        call  = str(s.get("call_name", "")).strip()
        disp  = clean_name(call, first, last)
        period = str(s.get("period", "")).strip()
        course = str(s.get("course", "")).strip()
        key    = norm(last + (call.split("/")[0] if call else strip_init(first)))
        rec    = {"name": disp, "period": period, "course": course, "key": key}
        rows.append(rec)
        for cand in {key, norm(last + strip_init(first)), norm(last + first)}:
            keymap.setdefault(cand, rec)
    return keymap, rows, os.path.basename(path)


def find_folders(match, explicit):
    if explicit:
        return [os.path.abspath(f) for f in explicit]
    hits = sorted(d for d in glob.glob(os.path.join(INCOMING, "*")) if os.path.isdir(d) and match.lower() in os.path.basename(d).lower())
    if not hits:
        sys.exit(f"No incoming folders match '{match}' in {INCOMING}")
    return hits


def list_images(folder, exts=IMG_EXT):
    out = []
    for e in exts:
        out += glob.glob(os.path.join(folder, "*" + e))
    # de-dup case-insensitive globs on case-insensitive filesystems
    return sorted(set(out))

def find_placeholders(arg):
    if arg:
        folder = os.path.abspath(arg)
    else:
        hits = [d for d in glob.glob(os.path.join(INCOMING, "*")) if os.path.isdir(d)
                and ("missing" in os.path.basename(d).lower() or "place" in os.path.basename(d).lower())]
        folder = hits[0] if hits else None
    if not folder or not os.path.isdir(folder):
        return []
    return list_images(folder, PH_EXT)


def make_copy(src, dest, edge, quality):
    im = Image.open(src)
    im = ImageOps.exif_transpose(im)          # honor camera/phone rotation
    if im.mode not in ("RGB", "L"):
        im = im.convert("RGB")
    w, h = im.size
    scale = min(1.0, edge / float(max(w, h)))
    if scale < 1.0:
        w, h = max(1, round(w * scale)), max(1, round(h * scale))
        im = im.resize((w, h), Image.LANCZOS)
    im.save(dest, "JPEG", quality=quality, optimize=True, progressive=True)  # metadata stripped (no exif passed)
    return w, h


def build(args):
    keymap, roster_rows, roster_name = load_roster()
    folders = find_folders(args.match, args.folder)
    print(f"Roster:  {roster_name}")
    print(f"Folders: " + ", ".join(os.path.basename(f) for f in folders))

    # match every photo -> student + period
    period_students = defaultdict(lambda: defaultdict(list))   # period -> student name -> [src paths]
    period_course = {}
    submitted_keys = defaultdict(set)                          # period -> {normalized student keys}
    unmatched = []
    total = 0
    for folder in folders:
        for src in list_images(folder):
            total += 1
            tok = os.path.basename(src).split("_")[0]
            rec = keymap.get(norm(tok))
            if not rec or not rec["period"]:
                unmatched.append(os.path.basename(src)); continue
            period_students[rec["period"]][rec["name"]].append(src)
            period_course.setdefault(rec["period"], rec["course"])
            submitted_keys[rec["period"]].add(rec["key"])
    matched = total - len(unmatched)
    print(f"\n{matched}/{total} photos matched" + (f"  ({len(unmatched)} UNMATCHED)" if unmatched else "  (all matched)"))
    if unmatched:
        for u in unmatched[:20]:
            print(f"   unmatched: {u}")
        if not args.allow_unmatched:
            sys.exit("Refusing to build with unmatched photos. Fix names or pass --allow-unmatched to skip them.")

    # missing-work: roster students in a gallery period/course who did NOT submit
    placeholders = [] if args.no_missing else find_placeholders(args.placeholders)
    missing_by_period = defaultdict(list)   # period -> [display names], deduped
    if placeholders:
        for p in list(period_students):
            course = period_course.get(p, "")
            seen = set()
            for r in roster_rows:
                if r["period"] == p and r["course"] == course and r["key"] not in submitted_keys[p] and r["key"] not in seen:
                    seen.add(r["key"]); missing_by_period[p].append(r["name"])
            missing_by_period[p].sort(key=lambda n: n.lower())
    elif not args.no_missing:
        print("   (no placeholder images found; skipping missing-work entries)")

    # stage the package
    pkg = args.out or tempfile.mkdtemp(prefix="critique_pkg_")
    for sz in ("thumb", "full"):
        os.makedirs(os.path.join(pkg, sz), exist_ok=True)
    manifest = {"slug": args.slug, "title": args.title, "subtitle": args.subtitle,
                "updated": time.strftime("%Y-%m-%d %H:%M:%S"), "periods": []}

    # process the placeholder pool once (ph_001..), reused by missing students round-robin
    ph_ids = []; ph_dims = {}
    for i, src in enumerate(placeholders, 1):
        pid = f"ph_{i:03d}"
        try:
            make_copy(src, os.path.join(pkg, "thumb", pid + ".jpg"), THUMB_EDGE, THUMB_Q)
            fw, fh = make_copy(src, os.path.join(pkg, "full", pid + ".jpg"), FULL_EDGE, FULL_Q)
            ph_ids.append(pid); ph_dims[pid] = (fw, fh)
        except Exception as e:
            print(f"   skipped placeholder {os.path.basename(src)}: {e}")
    if ph_ids:
        print(f"   placeholders: {len(ph_ids)} silly images loaded for missing work")
    ph_rot = 0

    present = [p for p in PERIOD_ORDER if p in period_students] + \
              sorted(p for p in period_students if p not in PERIOD_ORDER)
    done = 0
    for p in present:
        pnode = {"key": p, "label": f"Period {p}", "course": period_course.get(p, ""),
                 "submitted": 0, "missing": 0, "photos": []}
        entries = []
        seq = 0
        for student in sorted(period_students[p], key=lambda n: n.lower()):
            for src in sorted(period_students[p][student], key=lambda s: os.path.basename(s).lower()):
                seq += 1
                pid = f"p{p}_{seq:03d}"
                make_copy(src, os.path.join(pkg, "thumb", pid + ".jpg"), THUMB_EDGE, THUMB_Q)
                fw, fh = make_copy(src, os.path.join(pkg, "full", pid + ".jpg"), FULL_EDGE, FULL_Q)
                entries.append({"id": pid, "student": student, "w": fw, "h": fh})
                pnode["submitted"] += 1
                done += 1
                if done % 25 == 0:
                    print(f"   processed {done}/{matched} photos...")
        # missing students: a rotating silly placeholder, MIXED into the gallery as if submitted
        if ph_ids:
            for name in missing_by_period.get(p, []):
                phid = ph_ids[ph_rot % len(ph_ids)]
                fw, fh = ph_dims.get(phid, (3, 4))
                entries.append({"id": phid, "student": name, "missing": True, "w": fw, "h": fh})
                pnode["missing"] += 1
                ph_rot += 1
        # interleave everyone alphabetically by student so placeholders sit in natural order
        entries.sort(key=lambda e: (e["student"].lower(), e["id"]))
        pnode["photos"] = entries
        manifest["periods"].append(pnode)
        print(f"   Period {p}: {pnode['submitted']} submitted + {pnode['missing']} missing placeholders, "
              f"mixed into {len(entries)} tiles ({pnode['course']})")
    json.dump(manifest, open(os.path.join(pkg, "manifest.json"), "w"), indent=0)
    tot_missing = sum(pn["missing"] for pn in manifest["periods"])
    print(f"\nBuilt package: {pkg}  ({done} real photos + {tot_missing} missing-work placeholders, "
          f"{len(manifest['periods'])} periods)")

    # zip it
    zip_path = (args.out + ".zip") if args.out else os.path.join(tempfile.gettempdir(), f"critique_{args.slug}.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_STORED) as zf:   # JPEGs already compressed
        zf.write(os.path.join(pkg, "manifest.json"), "manifest.json")
        for sz in ("thumb", "full"):
            for f in sorted(glob.glob(os.path.join(pkg, sz, "*.jpg"))):
                zf.write(f, f"{sz}/{os.path.basename(f)}")
    mb = os.path.getsize(zip_path) / 1e6
    print(f"Zipped: {zip_path}  ({mb:.1f} MB)")
    return zip_path, manifest


def api_key(args):
    if args.api_key:
        return args.api_key.strip()
    if os.environ.get("CC_API_KEY"):
        return os.environ["CC_API_KEY"].strip()
    kf = os.path.join(HOME, ".config/creativesilva/cc_api_key")
    if os.path.isfile(kf):
        return open(kf).read().strip()
    return None


def upload(zip_path, slug, key):
    url = f"{CC_BASE}/api/critique/upload?g={slug}"
    body = open(zip_path, "rb").read()
    req = urlrequest.Request(url, data=body, method="POST",
                             headers={"X-API-Key": key, "Content-Type": "application/zip"})
    print(f"\nUploading {len(body)/1e6:.1f} MB to {url} ...")
    with urlrequest.urlopen(req, timeout=300) as r:
        resp = json.load(r)
    print(f"Upload OK: {resp}")
    return resp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--slug", required=True, help="url-safe id, e.g. spooky-portraits")
    ap.add_argument("--subtitle", default=SUBTITLE)
    ap.add_argument("--match", default="", help="substring to find incoming folders by name")
    ap.add_argument("--folder", action="append", default=[], help="explicit folder path (repeatable)")
    ap.add_argument("--out", default="", help="keep the built package at this dir (also writes <out>.zip)")
    ap.add_argument("--no-upload", action="store_true")
    ap.add_argument("--allow-unmatched", action="store_true")
    ap.add_argument("--placeholders", default="", help="folder of silly placeholder images for missing work (auto-found by name if omitted)")
    ap.add_argument("--no-missing", action="store_true", help="do not add missing-work placeholder entries")
    ap.add_argument("--api-key", default="")
    args = ap.parse_args()
    if not re.match(r"^[a-z0-9][a-z0-9-]{0,63}$", args.slug):
        sys.exit("--slug must be lowercase letters, digits, hyphens")
    if not args.match and not args.folder:
        sys.exit("Pass --match <substring> or one or more --folder <path>")

    zip_path, manifest = build(args)
    if args.no_upload:
        print("\n--no-upload set. Package/zip left in place for preview.")
        return
    key = api_key(args)
    if not key:
        print(f"\nNo Command Center API key found. ZIP is ready at:\n   {zip_path}\n"
              f"Provide the key (env CC_API_KEY, ~/.config/creativesilva/cc_api_key, or --api-key) to upload,\n"
              f"or ask Chris for it once.")
        return
    upload(zip_path, args.slug, key)
    print(f"\nLive: {CC_BASE}/critique  (gallery '{args.title}')")


if __name__ == "__main__":
    main()
