#!/usr/bin/env python3
# Live Image Catalog generator (teacher-facing, Build Resources > Image Generation Tools).
# Scans every LIVE module's pages for the AI-generated HEADER (the hero on each overview) and the
# FLOAT-RIGHT content photos (images hoisted into the flex:1 1 44% column), labels each with its
# module + page/step, and writes them as character-sheet-style cards (Download / Copy / lightbox)
# between the LIVE_IMAGE_CATALOG markers in curriculum.html, grouped by course, in module order.
# Module order + membership come from curriculum.html's own MODULES array, so this AUTO-UPDATES:
# add a module there + build its pages, then re-run this. Excludes tutorial screen captures, example
# photos, slide panels, and resource thumbnails (they do not use the float column / overview hero).
import os, re, html as _html

ROOT=os.path.join(os.path.dirname(__file__),"..")
CAT=os.path.join(ROOT,"curriculum.html")
SHARED=os.path.join(ROOT,"curriculum/shared")
COURSE_NAME={"da1a":"Digital Arts 1A","photo1a":"Photography 1A","photo2a":"Photography 2A"}
COURSE_ORDER=["da1a","photo1a","photo2a"]

TEAL=r'linear-gradient\(135deg,#00b8b8 0%,rgba\(0,184,184,0\.08\)'
HERO_RE=re.compile(TEAL+r'[^>]*"><img src="https://www\.creativesilva\.com(/assets/images/[^"]+)"(?:[^>]*alt="([^"]*)")?')
FLOAT_RE=re.compile(r'flex:1 1 44%;min-width:300px;"><div style="[^"]*"><img src="https://www\.creativesilva\.com(/assets/images/[^"]+)"(?:[^>]*alt="([^"]*)")?')

def modules_from_catalog():
    src=open(CAT,encoding="utf-8").read()
    block=src[src.index("const MODULES = ["):src.index("const COURSES = [")]
    mods=[]
    for m in re.finditer(r'\{[^{}]*\}', block):
        b=m.group(0)
        c=re.search(r'course:\s*"([^"]+)"',b); n=re.search(r'name:\s*"([^"]+)"',b); u=re.search(r'url:\s*"([^"]+)"',b)
        st=re.search(r'status:\s*"([^"]+)"',b); inact='inactive: true' in b or 'inactive:true' in b
        if not (c and n and u): continue
        if not re.match(r'Module\s*\d',n.group(1)): continue           # module entries only
        if c.group(1) not in COURSE_NAME: continue                      # active teaching courses
        if inact or (st and st.group(1)!="published"): continue
        mods.append((c.group(1), n.group(1), u.group(1)))
    return mods

def step_pages(overview_url):
    stem=os.path.basename(overview_url)[:-len("-overview.html")]
    steps=sorted(g for g in os.listdir(SHARED) if re.match(re.escape(stem)+r'-step\d',g))
    return stem, [f"curriculum/shared/{s}" for s in steps]

def page_label(fn):
    if fn.endswith("-overview.html"): return "Overview"
    m=re.search(r'step0*(\d+)-?([a-z0-9-]*)\.html',fn)
    if not m: return fn
    rest=m.group(2).replace("-"," ").strip().title()
    return f"Step {int(m.group(1)):02d}"+(f" &middot; {rest}" if rest else "")

def card(path, module_title, page, role, alt, page_url):
    ext=path.rsplit(".",1)[-1].upper()
    name=f'{module_title} &rsaquo; {page}'
    alt=alt or f"{module_title} {re.sub('&[a-z]+;','',page)} {role.lower()}"
    return ('<div class="logo-card"><div class="logo-tile">'
      f'<img src="{path}" alt="{alt}" /></div>'
      f'<div class="logo-meta"><span class="logo-name">{name} '
      f'<span class="logo-fmt">{role} &middot; {ext}</span></span>'
      f'<a class="logo-view" href="{page_url}">View Page</a>'
      f'<a class="logo-dl" href="{path}" download>Download</a></div></div>')

def collect():
    mods=modules_from_catalog()
    seen=set(); bycourse={c:[] for c in COURSE_ORDER}
    for course,name,overview_url in mods:
        title=re.sub(r'^Module\s*\d+:\s*','',name)   # "Module 05: Live Stream Graphic" -> title
        stem,steps=step_pages(overview_url)
        overview=os.path.join(ROOT,overview_url)
        # header: first teal-framed content image on the overview
        if os.path.exists(overview):
            h=open(overview,encoding="utf-8").read()
            m=HERO_RE.search(h)
            if m and m.group(1) not in seen:
                seen.add(m.group(1)); bycourse[course].append(card(m.group(1),title,"Overview","Header",m.group(2),"/"+overview_url))
        # floats: images in the 44% float column, each step in order
        for sp in [overview_url]+steps:
            p=os.path.join(ROOT,sp)
            if not os.path.exists(p): continue
            h=open(p,encoding="utf-8").read(); fn=os.path.basename(sp)
            for m in FLOAT_RE.finditer(h):
                if m.group(1) in seen: continue
                seen.add(m.group(1)); bycourse[course].append(card(m.group(1),title,page_label(fn),"Float",m.group(2),"/"+sp))
    return bycourse

def render(bycourse):
    # each course is its own collapsible sub-accordion (nested cat-acc), collapsed by default
    out=[]
    for c in COURSE_ORDER:
        cards=bycourse[c]
        if not cards: continue
        out.append('<details class="cat-acc"><summary class="cat-head">'
          f'<span class="cat-name">{COURSE_NAME[c]} ({len(cards)})</span><span class="cat-chevron"></span></summary>'
          '<div class="cat-body"><div class="logo-grid">'+"".join(cards)+'</div></div></details>')
    return "\n                      ".join(out)

def main():
    bycourse=collect()
    inner=render(bycourse)
    src=open(CAT,encoding="utf-8").read()
    new=re.sub(r'(<!-- LIVE_IMAGE_CATALOG_START -->).*?(<!-- LIVE_IMAGE_CATALOG_END -->)',
               lambda m: m.group(1)+"\n                      "+inner+"\n                      "+m.group(2), src, flags=re.S)
    assert new!=src, "markers not found in curriculum.html"
    open(CAT,"w",encoding="utf-8").write(new)
    total=sum(len(v) for v in bycourse.values())
    print(f"Live Image Catalog: {total} images "+", ".join(f"{COURSE_NAME[c]}={len(bycourse[c])}" for c in COURSE_ORDER))

main()
