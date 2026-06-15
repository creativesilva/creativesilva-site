#!/usr/bin/env python3
"""Re-skin a framework page to a different course brand. ONLY colors,
logo, and brand text change. Structure, fonts, layout, numbering, and
the wedge geometry stay locked.

A theme is a color map (source hex + rgb-triple -> target) plus the
banner logo replacement and brand-text swaps. Apply a theme to any
existing framework page to get the same page in the new brand.

Usage: python3 tools/apply-theme.py <theme> <source.html> <target.html>
"""
import re, sys, os

THEMES = {
  'mrc': {
    # Marc Richardson Center: orange #c95201 + grays + black (monochrome).
    # teal/cyan/red roles all collapse onto orange + gray.
    'hex': {
      '#00b8b8': '#c95201',  # primary accent
      '#007474': '#c95201',  # banner accent
      '#003838': '#4a1e02',  # banner dark-mid (dark orange)
      '#80e0e0': '#eda268',  # light eyebrow (light orange)
      '#FF6B1A': '#c95201',  # action -> brand orange
      '#ff6b1a': '#c95201',
      '#ffb27c': '#eda268',  # light action
      '#00c2ff': '#a6a6a6',  # info -> light gray
      '#7dd3fc': '#c2c2c2',  # light info
      '#E62429': '#c95201',  # rules (no red in brand) -> orange
      '#ffb3b6': '#eda268',
      '#003838': '#4a1e02',
    },
    'rgb': {
      '0,184,184': '201,82,1',
      '0,116,116': '201,82,1',
      '255,107,26': '201,82,1',
      '0,194,255': '166,166,166',
      '230,36,41': '201,82,1',
      '0,56,56': '40,20,2',     # page-background tint
    },
    # logo: text placeholder until the real MRC logo is supplied
    'logo_text': 'MRC',
    'brand': [
      ('Pioneer Valley High School Logo', 'Marc Richardson Center'),
      ('Pioneer Valley High School', 'Marc Richardson Center'),
      ('DIGITAL ARTS / FINAL EXAM / STUDY GUIDE', 'MARC RICHARDSON CENTER / INTRO TO DIGITAL ARTS'),
      ('ARTES DIGITALES / EXAMEN FINAL / GU&Iacute;A DE ESTUDIO', 'CENTRO MARC RICHARDSON / INTRODUCCI&Oacute;N AL ARTE DIGITAL'),
    ],
  },
}

LOGO_IMG = re.compile(r'<img\b[^>]*alt="[^"]*(?:Pioneer Valley|Logo)[^"]*"[^>]*>')

def apply(theme_name, src, dst):
    t = THEMES[theme_name]
    html = open(src).read()
    # rgb triples first (so they are not disturbed by hex edits)
    for a,b in t['rgb'].items():
        html = html.replace(f'rgba({a},', f'rgba({b},')
        html = html.replace(f'rgb({a})', f'rgb({b})')
    # hex colors (case-insensitive)
    for a,b in t['hex'].items():
        html = re.sub(re.escape(a), b, html, flags=re.I)
    # logo -> text placeholder wordmark
    if t.get('logo_text'):
        wordmark = (f'<div style="font-size:20pt;color:#c95201;font-weight:700;'
                    f'letter-spacing:0.04em;"><strong>{t["logo_text"]}</strong></div>'
                    f'<!--LOGO PLACEHOLDER: swap for the MRC logo img-->')
        html = LOGO_IMG.sub(wordmark, html)
    # brand text swaps
    for a,b in t['brand']:
        html = html.replace(a, b)
    bal = html.count('<div')==html.count('</div>')
    if not bal:
        print(f'  CHECK {os.path.basename(dst)}: imbalance -- NOT WRITTEN'); return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst,'w').write(html)
    print(f'  OK wrote {dst}')

if __name__=='__main__':
    apply(sys.argv[1], sys.argv[2], sys.argv[3])
