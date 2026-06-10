#!/usr/bin/env python3
"""Lock framework buttons to the bottom of their tile so a row of
resource cards has aligned buttons regardless of description length.

For every inner tile (1px gradient-frame) that contains a framework
button (gray base rgba(255,255,255,0.92)):
  - make the tile a flex column (display:flex;flex-direction:column)
  - give the button margin-top:auto so it sinks to the bottom
The enclosing scroll grid already stretches tiles to equal height
(grid default align-items:stretch), so every button lands on the same
baseline.

Usage: python3 tools/fix-button-align.py <file.html> [more...]
"""
import re, sys, os

TILE_OPEN = re.compile(r'<div style="([^"]*border:1px solid transparent;border-image:[^"]*)">')
BTN = re.compile(r'(<a\b[^>]*style="background:rgba\(255,255,255,0\.92\);)')

def process(html):
    out=[]; pos=0; n=0
    for m in TILE_OPEN.finditer(html):
        if m.start() < pos:
            continue
        out.append(html[pos:m.start()])
        style=m.group(1)
        # find matching close div
        depth=1; i=m.end(); close=-1
        while depth>0 and i<len(html):
            no=html.find('<div',i); nc=html.find('</div>',i)
            if nc==-1: break
            if no!=-1 and no<nc: depth+=1; i=no+4
            else:
                depth-=1
                if depth==0: close=nc; break
                i=nc+6
        if close==-1:
            out.append(m.group(0)); pos=m.end(); continue
        content=html[m.end():close]
        if 'background:rgba(255,255,255,0.92)' in content and 'display:flex' not in style:
            ns=style.rstrip(';')+';display:flex;flex-direction:column;'
            content=BTN.sub(r'\1margin-top:auto;', content)
            out.append(f'<div style="{ns}">'+content)
            n+=1; pos=close
        else:
            out.append(m.group(0)); pos=m.end()
    out.append(html[pos:])
    return ''.join(out), n

def main():
    for path in sys.argv[1:]:
        h=open(path).read()
        new,n=process(h)
        if n==0:
            continue
        bal=new.count('<div')==new.count('</div>')
        if not bal:
            print(f'  CHECK {os.path.basename(path)}: bal={bal} -- NOT WRITTEN'); continue
        open(path,'w').write(new)
        print(f'  OK {os.path.basename(path)}: {n} tile(s) bottom-locked')

if __name__=='__main__':
    main()
