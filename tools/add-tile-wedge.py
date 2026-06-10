#!/usr/bin/env python3
"""Give every small inner card the diagonal corner-wedge accent (the
"shadow triangle") so all tiles inside sections match the stat/term
tiles. Outer section cards (2px frame) are left flat on purpose.

For each inner tile (1px gradient frame), the background is replaced
with a 135deg wedge in the tile's own accent color: a small bright
corner triangle, then a dark fill.

Refuses to write a div-imbalanced result. Idempotent: a tile already
carrying the exact wedge is left unchanged.

Usage: python3 tools/add-tile-wedge.py <file.html> [more...]
"""
import re, sys, os

def hex_rgba(h, a):
    h=h.lstrip('#'); r=int(h[0:2],16); g=int(h[2:4],16); b=int(h[4:6],16)
    return f'rgba({r},{g},{b},{a})'

# inner tile opener: background:<bg>; ...(padding/margin)... then the
# 1px transparent border + 135deg border-image. The accent hex lives in
# the border-image. Non-greedy middle so it stays in one style attr.
TILE = re.compile(
    r'(<div style="background:)([^;]+)(;[^"]*?border:1px solid transparent;'
    r'border-image:linear-gradient\(135deg,(#[0-9a-fA-F]{6})[^"]*">)'
)

def wedge(accent):
    bright = hex_rgba(accent, '0.16')
    dark = 'rgba(0,0,0,0.34)'
    return (f'linear-gradient(135deg,{bright} 0%,{bright} 10%,'
            f'{dark} 10%,{dark} 100%)')

def process(html):
    n=[0]
    def repl(m):
        accent=m.group(4)
        w=wedge(accent)
        if m.group(2)==w:
            return m.group(0)
        n[0]+=1
        return m.group(1)+w+m.group(3)
    return TILE.sub(repl, html), n[0]

def main():
    for path in sys.argv[1:]:
        h=open(path).read()
        new,n=process(h)
        if n==0:
            continue
        if new.count('<div')!=new.count('</div>'):
            print(f'  CHECK {os.path.basename(path)}: imbalance -- NOT WRITTEN'); continue
        open(path,'w').write(new)
        print(f'  OK {os.path.basename(path)}: {n} tile(s) wedged')

if __name__=='__main__':
    main()
