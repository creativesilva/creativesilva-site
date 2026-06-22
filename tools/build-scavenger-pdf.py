#!/usr/bin/env python3
"""Build the printable Photo Scavenger Hunt handout HTML (light, one page,
MRC-branded). Convert to PDF with Chrome headless:

  python3 tools/build-scavenger-pdf.py
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \\
    --headless --disable-gpu --no-pdf-header-footer \\
    --print-to-pdf=assets/mrc/handouts/MRC_Photo_Scavenger_Hunt.pdf \\
    tools/scavenger-list-print.html
"""
import os, base64

ROOT = os.path.join(os.path.dirname(__file__), '..')
logo = open(os.path.join(ROOT, 'assets/mrc/MRC_Logo.png'), 'rb').read()
LOGO = 'data:image/png;base64,' + base64.b64encode(logo).decode()

FIND = [
    'An American flag',
    'A tractor or heavy machine',
    'An animal (livestock)',
    'A crop or plant growing',
    'Rusty or weathered metal',
    'A tool (hand or shop)',
    'The MRC logo or a campus sign',
]
SHOTS = [
    ('Leading lines', 'a line that pulls your eye in'),
    ('Rule of thirds', 'put the subject off to one side'),
    ('Framing', 'shoot through a gate, window, or branches'),
    ('Texture', 'fill the frame with a rough surface'),
    ('Pattern', 'shapes that repeat'),
    ('Fill the frame', 'get close, no empty space'),
    ('Low angle', 'shoot from down low, looking up'),
    ('Negative space', 'small subject, lots of empty space'),
]

def find_item(n, label):
    return ('<div class="item"><span class="box"></span>'
            '<span class="num">%d</span>'
            '<span class="label">%s</span></div>' % (n, label))

def shot_item(n, label, hint):
    return ('<div class="item"><span class="box"></span>'
            '<span class="num">%d</span>'
            '<span class="label"><b>%s</b><span class="hint">%s</span></span></div>'
            % (n, label, hint))

find_html = ''.join(find_item(i + 1, t) for i, t in enumerate(FIND))
shot_html = ''.join(shot_item(i + 1, t, h) for i, (t, h) in enumerate(SHOTS))

html = '''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8" />
<style>
  @page { size: Letter; margin: 0.45in; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  html, body { background: #ffffff; }
  body { font-family: Arial, Helvetica, sans-serif; color: #1a1a1a; margin: 0; }
  .header { display: flex; align-items: center; gap: 16px; border-bottom: 3px solid #c95201; padding-bottom: 12px; }
  .header img { height: 60px; width: auto; }
  .htext h1 { font-size: 23pt; margin: 0; color: #c95201; letter-spacing: 0.01em; }
  .htext .sub { font-size: 10.5pt; color: #555; margin-top: 3px; letter-spacing: 0.04em; text-transform: uppercase; }
  .intro { font-size: 10.5pt; line-height: 1.45; margin: 13px 0 11px; }
  .intro b { color: #c95201; }
  .fields { font-size: 10.5pt; margin-bottom: 16px; }
  .fields .f { display: inline-block; margin-right: 26px; }
  .fields .line { display: inline-block; border-bottom: 1px solid #888; width: 150px; }
  .fields .line.sm { width: 70px; }
  .cols { display: flex; gap: 30px; }
  .col { flex: 1; }
  .sec-title { background: #c95201; color: #fff; font-size: 11pt; font-weight: bold; padding: 6px 11px;
    text-transform: uppercase; letter-spacing: 0.09em; margin-bottom: 6px; }
  .item { display: flex; align-items: flex-start; gap: 9px; padding: 6px 2px; border-bottom: 1px dotted #cfcfcf; }
  .box { width: 15px; height: 15px; border: 2px solid #c95201; flex: none; margin-top: 1px; }
  .num { font-size: 9.5pt; font-weight: bold; color: #c95201; flex: none; width: 15px; text-align: right; margin-top: 1px; }
  .label { font-size: 11pt; line-height: 1.25; }
  .hint { display: block; font-size: 8.5pt; color: #6b6b6b; font-style: italic; margin-top: 1px; }
  .footer { margin-top: 16px; padding-top: 9px; border-top: 1px solid #e0e0e0; text-align: center;
    font-size: 8.5pt; color: #888; }
  .footer b { color: #c95201; }
</style></head>
<body>
  <div class="header">
    <img src="%(logo)s" alt="Mark Richardson Center" />
    <div class="htext">
      <h1>Photo Scavenger Hunt</h1>
      <div class="sub">Digital Arts 1A &bull; Mark Richardson Center</div>
    </div>
  </div>

  <div class="intro">
    Everyone shoots the <b>same 15 shots</b>. Shoot in <b>AUTO</b> and put all your focus on <b>framing</b>.
    Take lots of photos, then turn in your single best <b>JPG</b> for each of the 15 on Canvas.
    Best set wins a <b>$20 Chick-fil-A gift card</b>.
  </div>

  <div class="fields">
    <span class="f">Name: <span class="line"></span></span>
    <span class="f">Period: <span class="line sm"></span></span>
    <span class="f">Date: <span class="line sm"></span></span>
  </div>

  <div class="cols">
    <div class="col">
      <div class="sec-title">Find These Things</div>
      %(find)s
    </div>
    <div class="col">
      <div class="sec-title">Capture These Shots</div>
      %(shots)s
    </div>
  </div>

  <div class="footer">
    Judged on <b>accuracy, composition, creativity, and image quality</b>. &nbsp; Stay safe: keep your distance from livestock and machinery, and stay with your group.
  </div>
</body></html>
''' % {'logo': LOGO, 'find': find_html, 'shots': shot_html}

out = os.path.join(os.path.dirname(__file__), 'scavenger-list-print.html')
open(out, 'w').write(html)
print('wrote', out, '(%d KB)' % (len(html) // 1024))
