#!/usr/bin/env python3
"""Repair two misses on already-built framework pages:
  1. Chip entity bug: chip labels were uppercased including HTML
     entities, so &eacute; became the broken &EACUTE;. Lowercase any
     all-caps entity inside a chip's <strong>LABEL / NN</strong> back
     to a valid entity.
  2. Unframed images: give every content image (width:100%) the 2px
     gradient frame, colored by the nearest section stripe (falls back
     to the page's first stripe, then teal). The small PV logo is
     width:min(90px,..) so it is excluded automatically.

Refuses to write a div-imbalanced result. Idempotent: an image that
already has a border-image is left alone.

Usage: python3 tools/fix-images-chips.py <file.html> [more...]
"""
import re, sys, os

def hex_rgba(h, a):
    h=h.lstrip('#'); r=int(h[0:2],16); g=int(h[2:4],16); b=int(h[4:6],16)
    return f'rgba({r},{g},{b},{a})'

STRIPE = re.compile(r'height:[1-9]px;background:(#[0-9a-fA-F]{6});margin:-')
IMG = re.compile(r'<img\b[^>]*?\bstyle="([^"]*width:100%[^"]*)"')
CHIP = re.compile(r'<strong>([^<]*?/ \d\d)</strong>')
ACCENT_UP = {'aacute':'Aacute','eacute':'Eacute','iacute':'Iacute','oacute':'Oacute',
             'uacute':'Uacute','ntilde':'Ntilde','uuml':'Uuml','auml':'Auml','ouml':'Ouml','iuml':'Iuml'}

def fix_chip_entities(html):
    """A broken all-caps entity inside a chip becomes a valid one:
    an accented letter takes its uppercase form (&EACUTE; -> &Eacute;),
    anything else just lowercases (&AMP; -> &amp;)."""
    def fix_ent(e):
        name=e.group(1)
        low=name.lower()
        return f'&{ACCENT_UP[low]};' if low in ACCENT_UP else f'&{low};'
    def repl(m):
        return f'<strong>{re.sub(r"&([A-Z]{2,});", fix_ent, m.group(1))}</strong>'
    return CHIP.sub(repl, html)

def frame_images(html):
    # Use the page's DOMINANT accent (most common stripe color) so every
    # image on a page gets the same frame, matching that page's brand
    # identity (teal for DA/Photo, blue for Jimenez, etc.), not whatever
    # section happens to sit nearest a top- or bottom-of-page hero.
    from collections import Counter
    colors=[m.group(1) for m in STRIPE.finditer(html)]
    page_accent = Counter(colors).most_common(1)[0][0] if colors else '#00b8b8'
    out=[]; pos=0; n=0
    for m in IMG.finditer(html):
        out.append(html[pos:m.start()]); pos=m.end()
        style=m.group(1)
        if 'border-image' in style:
            out.append(m.group(0)); continue
        color=page_accent; dim=hex_rgba(color,'0.08')
        ns=style.rstrip(';')+f';border:2px solid transparent;border-image:linear-gradient(135deg,{color} 0%,{dim} 100%) 1;'
        prefix=m.group(0)[:-(len(style)+1)]   # everything up to style="
        out.append(prefix+ns+'"')
        n+=1
    out.append(html[pos:])
    return ''.join(out), n

def main():
    for path in sys.argv[1:]:
        h=open(path).read()
        h2=fix_chip_entities(h)
        h2,n=frame_images(h2)
        bal=h2.count('<div')==h2.count('</div>')
        em=h2.count('—')
        if not bal or em:
            print(f'  CHECK {os.path.basename(path)}: bal={bal} em={em} -- NOT WRITTEN'); continue
        if h2==h:
            continue
        open(path,'w').write(h2)
        print(f'  OK {os.path.basename(path)}: {n} image(s) framed')

if __name__=='__main__':
    main()
