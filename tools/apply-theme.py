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
    # Mark Richardson Center: four-color system mapped to framework roles.
    # primary=orange #c95201, action=gold #e9b949, info=steel blue
    # #3a7ca5, rules=rust red #a4161a, support=grays + black.
    'hex': {
      '#00b8b8': '#c95201',  # primary/content accent (was teal)
      '#007474': '#c95201',  # banner accent
      '#003838': '#4a1e02',  # banner dark-mid (dark orange)
      '#80e0e0': '#eda268',  # light primary eyebrow (light orange)
      '#FF6B1A': '#e9b949',  # action/format (was orange) -> gold
      '#ff6b1a': '#e9b949',
      '#ffb27c': '#f6dd9d',  # light action (light gold)
      '#00c2ff': '#3a7ca5',  # info/study (was cyan) -> steel blue
      '#7dd3fc': '#9ecbe6',  # light info (light steel blue)
      '#E62429': '#a4161a',  # rules (was red) -> rust red
      '#ffb3b6': '#e09b9d',  # light rules (light rust)
    },
    'rgb': {
      '0,184,184': '201,82,1',    # teal -> orange
      '0,116,116': '201,82,1',    # dark teal tint -> orange
      '255,107,26': '233,185,73', # orange -> gold
      '0,194,255': '58,124,165',  # cyan -> steel blue
      '230,36,41': '164,22,26',   # red -> rust red
      '0,56,56': '40,20,2',       # page-background tint -> dark orange
    },
    # logo: text placeholder until the MRC logo file is added to assets
    'logo_text': 'MRC',
    'brand': [
      ('Pioneer Valley High School Logo', 'Mark Richardson Center'),
      ('Pioneer Valley High School', 'Mark Richardson Center'),
      ('DIGITAL ARTS / FINAL EXAM / STUDY GUIDE', 'MARK RICHARDSON CENTER / INTRO TO DIGITAL ARTS'),
      ('ARTES DIGITALES / EXAMEN FINAL / GU&Iacute;A DE ESTUDIO', 'CENTRO MARK RICHARDSON / INTRODUCCI&Oacute;N AL ARTE DIGITAL'),
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
