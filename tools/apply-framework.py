#!/usr/bin/env python3
"""Apply the locked Angular Gradient Framework to a hand-authored
curriculum page (Sauce Baby, Jimenez, Cereal Box, Branding, Revisit,
course homes). Preserves brand colors, header, logo, hero images,
content, and bilingual structure.

Three passes, in order:
  1. angular   : strip all border-radius; convert border-left accent
                 cards/tiles to a 2px/1px gradient border-image frame +
                 solid top-stripe child in the brand color; convert
                 pill/brand buttons to the framework button rule.
  2. parity    : section eyebrow labels -> numbered framework chips
                 (LABEL / NN), accent taken from the card's own top
                 stripe; hairline divider under each section title.
  3. wedge     : plain inner tiles -> 135deg corner wedge accent + 1px
                 gradient frame + 3px top stripe + hairline, using the
                 enclosing section's accent.

Usage: python3 tools/apply-framework.py <file.html> [<file2.html> ...]
Idempotent-ish: skips a file that already has border-image frames.
"""
import re, sys, os

# ---------- helpers ----------
def hex_to_rgba(hex_color, alpha):
    h = hex_color.lstrip('#')
    if len(h) == 3:
        h = ''.join(c*2 for c in h)
    r = int(h[0:2],16); g = int(h[2:4],16); b = int(h[4:6],16)
    return f'rgba({r},{g},{b},{alpha})'

def parse_padding(pad):
    parts = [int(p) for p in pad.replace('px','').split()]
    if len(parts)==1: return parts[0],parts[0],parts[0],parts[0]
    if len(parts)==2: return parts[0],parts[1],parts[0],parts[1]
    if len(parts)==3: return parts[0],parts[1],parts[2],parts[1]
    return parts[0],parts[1],parts[2],parts[3]

# ---------- pass 1: angular ----------
OPEN_DIV = re.compile(r'<div style="([^"]*)">')

def pass_angular(html):
    out = []; pos = 0; ns = nt = 0
    for m in OPEN_DIV.finditer(html):
        style = m.group(1)
        out.append(html[pos:m.start()]); pos = m.end()
        bl = re.search(r'border-left:\s*(\d+)px solid (#[0-9a-fA-F]{3,6})', style)
        pad_m = re.search(r'padding:\s*([0-9px ]+?);', style)
        if not bl or not pad_m:
            out.append(m.group(0)); continue
        width = int(bl.group(1)); color = bl.group(2)
        pt,pr,pb,pl = parse_padding(pad_m.group(1).strip())
        is_section = width >= 5 and pt >= 22
        s = style
        s = re.sub(r'border:\s*[^;]*;', '', s)
        s = re.sub(r'border-left:\s*\d+px solid #[0-9a-fA-F]{3,6};?', '', s)
        s = re.sub(r'border-radius:\s*[^;]*;?', '', s)
        s = s.strip(';') + ';'
        fw = 2 if is_section else 1
        sh = 4 if is_section else 3
        dim = hex_to_rgba(color, '0.08')
        s += (f'border:{fw}px solid transparent;'
              f'border-image:linear-gradient(135deg,{color} 0%,{dim} 100%) 1;')
        if 'position:relative' not in s: s += 'position:relative;'
        if 'overflow:hidden' not in s: s += 'overflow:hidden;'
        gap = max(pt - (6 if is_section else 8), 10)
        stripe = (f'<div style="height:{sh}px;background:{color};'
                  f'margin:-{pt}px -{pr}px {gap}px -{pl}px;"></div>')
        out.append(f'<div style="{s}">{stripe}')
        ns += is_section; nt += (not is_section)
    out.append(html[pos:])
    return ''.join(out), ns, nt

BTN = re.compile(r'(<a\b[^>]*?style=")([^"]*border-radius:999px[^"]*)(")', re.S)
def pass_buttons(html):
    def repl(mm):
        style = mm.group(2)
        accent = '#ff6b1a'
        col = re.search(r'background:(#[0-9a-fA-F]{3,6})', style)
        if col: accent = col.group(1)
        new = (f'background:rgba(255,255,255,0.92);color:#003838;'
               f'text-decoration:none;padding:7px 16px;display:inline-block;'
               f'font-size:11pt;white-space:nowrap;border-top:2px solid {accent};')
        return mm.group(1) + new + mm.group(3)
    html, n = BTN.subn(repl, html)
    return html, n

def strip_radius(html):
    return re.sub(r'border-radius:[^;"]*;?', '', html)

# ---------- pass 2: parity (numbered chips + hairlines) ----------
# Anchor on the TITLE that follows each eyebrow (robust across markup
# variants): an eyebrow is a leaf <div> immediately followed by a title
# div whose text is sized 18-24pt. Title comes in two conventions:
#   A) <div style="font-size:18pt..."><strong>Title</strong></div>
#   B) <div style="..."><span style="font-size:18pt..."><strong>Title</strong></span></div>
STRIPE = re.compile(r'height:[34]px;background:(#[0-9a-fA-F]{3,6});margin:-')
LEAF = r'<div style="[^"]*">(?:(?!</?div).)*?</div>'
TITLE = (r'<div style="font-size:(?:18|19|20|22|24)pt[^"]*"><strong>(?:(?!</?div).)*?</strong></div>'
         r'|<div style="[^"]*"><span style="font-size:(?:18|19|20|22|24)pt[^"]*"><strong>(?:(?!</?div).)*?</strong></span></div>')
PAIR = re.compile(r'(' + LEAF + r')\s*(' + TITLE + r')', re.S)
TAGS = re.compile(r'<[^>]+>')

ACCENT_UP = {'aacute':'Aacute','eacute':'Eacute','iacute':'Iacute','oacute':'Oacute',
             'uacute':'Uacute','ntilde':'Ntilde','uuml':'Uuml','auml':'Auml','ouml':'Ouml','iuml':'Iuml'}

def smart_upper(t):
    """Uppercase label text. HTML entities are not naively uppercased
    (which would break them); accented-letter entities are swapped for
    their uppercase form (&eacute; -> &Eacute;) so a chip like
    'DE QUE TRATA' shows a real uppercase accent. Other entities
    (&amp;, &bull;, ...) are left as-is."""
    def conv(p):
        if p.startswith('&') and p.endswith(';'):
            name = p[1:-1]
            return f'&{ACCENT_UP[name.lower()]};' if name.lower() in ACCENT_UP else p
        return p.upper()
    return ''.join(conv(p) for p in re.split(r'(&[a-zA-Z]+;)', t))

def pass_parity(html):
    stripes = [(m.start(), m.group(1)) for m in STRIPE.finditer(html)]
    def accent_at(pos):
        acc = '#ff6b1a'
        for idx,a in stripes:
            if idx <= pos: acc = a
            else: break
        return acc
    # eyebrow text color: pull the first color: in the eyebrow div, else neutral
    def eyebrow_color(div):
        m = re.search(r'color:(#[0-9a-fA-F]{3,6})', div)
        return m.group(1) if m else 'rgba(255,255,255,0.75)'
    counter = {'n': 0}
    def repl(m):
        eyebrow_div, title_div = m.group(1), m.group(2)
        text = TAGS.sub('', eyebrow_div).strip()
        # skip if the "eyebrow" is actually long body text, empty, or a
        # top-stripe child (height:Npx;background:...). Note: must NOT trip
        # on line-height, which also contains "height:".
        if not text or len(text) > 42 or re.search(r'height:\d+px;background:', eyebrow_div):
            return m.group(0)
        counter['n'] += 1
        accent = accent_at(m.start())
        eb = eyebrow_color(eyebrow_div)
        nn = f'{counter["n"]:02d}'
        chip = (
            f'<div style="display:inline-block;background:rgba(0,0,0,0.40);'
            f'border-left:3px solid {accent};padding:5px 12px 5px 10px;'
            f'font-family:Arial,sans-serif;font-size:10pt;letter-spacing:0.22em;'
            f'color:{eb};text-transform:uppercase;margin-bottom:12px;">'
            f'<strong>{smart_upper(text)} / {nn}</strong></div>'
        )
        hair = f'<div style="height:2px;background:{accent};width:60px;margin-bottom:18px;"></div>'
        return chip + title_div + hair
    return PAIR.sub(repl, html)

# ---------- pass 3: tile wedge ----------
CHIP = re.compile(r'border-left:3px solid (#[0-9a-fA-F]{3,6});padding:5px 12px 5px 10px')
PLAIN_TILE = re.compile(
    r'<div style="background:rgba\(0,0,0,0\.\d+\);'
    r'border:1px solid rgba\(255,255,255,0\.\d+\);padding:16px;">'
    r'(\s*<div style="font-size:14pt;color:#ffffff;margin-bottom:5px;"><strong>[^<]*</strong></div>)'
)
def pass_wedge(html):
    chips = [(m.start(), m.group(1)) for m in CHIP.finditer(html)]
    def accent_at(pos):
        acc = '#ff6b1a'
        for idx,a in chips:
            if idx <= pos: acc = a
            else: break
        return acc
    out = []; last = 0; n = 0
    for m in PLAIN_TILE.finditer(html):
        acc = accent_at(m.start())
        dim14 = hex_to_rgba(acc, '0.14'); dim8 = hex_to_rgba(acc, '0.08')
        wedge = (f'linear-gradient(135deg,{dim14} 0%,{dim14} 10%,'
                 f'rgba(0,0,0,0.32) 10%,rgba(0,0,0,0.32) 100%)')
        out.append(html[last:m.start()])
        title_div = m.group(1).strip()
        out.append(
            f'<div style="background:{wedge};border:1px solid transparent;'
            f'border-image:linear-gradient(135deg,{acc} 0%,{dim8} 100%) 1;'
            f'padding:16px;position:relative;overflow:hidden;">'
            f'<div style="height:3px;background:{acc};margin:-16px -16px 10px -16px;"></div>'
            f'{title_div}'
            f'<div style="height:2px;background:{acc};width:28px;margin-bottom:8px;"></div>')
        last = m.end(); n += 1
    out.append(html[last:])
    return ''.join(out), n

# ---------- driver ----------
def apply(path):
    with open(path) as f: html = f.read()
    if 'border-image:linear-gradient(135deg' in html:
        print(f'  SKIP {os.path.basename(path)} (already has framework frames)')
        return
    html, ns, nt = pass_angular(html)
    html, nb = pass_buttons(html)
    html = strip_radius(html)
    html = pass_parity(html)
    html, nw = pass_wedge(html)
    bal = html.count('<div') == html.count('</div>')
    radius_left = html.count('border-radius')
    em = html.count('—')
    status = 'OK' if (bal and radius_left == 0 and em == 0) else 'CHECK'
    if not bal or radius_left or em:
        print(f'  {status} {os.path.basename(path)}: sec={ns} tile={nt} btn={nb} '
              f'wedge={nw} balanced={bal} radius_left={radius_left} em={em} '
              f'-- NOT WRITTEN')
        return
    with open(path,'w') as f: f.write(html)
    print(f'  {status} {os.path.basename(path)}: sec={ns} tile={nt} btn={nb} wedge={nw}')

if __name__ == '__main__':
    for p in sys.argv[1:]:
        apply(p)
