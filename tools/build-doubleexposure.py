#!/usr/bin/env python3
"""Generate the MRC Digital Arts 1A "Double Exposure" creative exercise
(English only) on the locked Angular Gradient Framework (orange #c95201).
One Canvas page: what a double exposure is, two clickable tutorial-video
buttons, how to blend with blending modes, and a turn-in section.
"""
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'curriculum', 'mrc')
IMG = 'https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/mrc/images/'
FRAME = 'border:2px solid transparent;border-image:linear-gradient(135deg,#c95201 0%,rgba(201,82,1,0.08) 100%) 1;'
CARD_BG = 'background:linear-gradient(180deg,rgba(201,82,1,0.10) 0%,rgba(201,82,1,0.03) 100%);'
WEDGE = 'background:linear-gradient(135deg,rgba(201,82,1,0.20) 0%,rgba(201,82,1,0.20) 8%,rgba(0,0,0,0.40) 8%,rgba(0,0,0,0.40) 100%);'

def chip(label):
    return ('<div style="display:inline-block;background:rgba(0,0,0,0.40);border-left:3px solid #c95201;'
            'padding:5px 12px 5px 10px;font-family:Arial,sans-serif;font-size:10pt;letter-spacing:0.22em;'
            'color:#eda268;text-transform:uppercase;margin-bottom:12px;"><strong>%s</strong></div>' % label)

def tb(title):
    return ('<div style="font-size:22pt;color:#ffffff;line-height:1.15;margin-bottom:10px;"><strong>%s</strong></div>'
            '<div style="height:2px;background:#c95201;width:60px;margin-bottom:20px;"></div>' % title)

def para(text):
    return ('<div style="font-size:14pt;line-height:1.78;color:rgba(255,255,255,0.88);margin-bottom:14px;">%s</div>'
            % text)

def headerph(desc):
    return ('<div style="%spadding:46px 30px;text-align:center;margin-bottom:24px;'
            'background:linear-gradient(135deg,rgba(201,82,1,0.12) 0%%,rgba(0,0,0,0.45) 100%%);">'
            '<div style="font-size:10pt;letter-spacing:0.22em;text-transform:uppercase;color:#eda268;margin-bottom:10px;">'
            '<strong>Header Image Placeholder &bull; 16:6 Ultra-Wide</strong></div>'
            '<div style="font-size:12pt;line-height:1.6;color:rgba(255,255,255,0.66);font-style:italic;max-width:780px;margin:0 auto;">'
            '%s</div></div>' % (FRAME, desc))

def videorow(videos):
    """Two clickable tutorial thumbnails (anchor wraps the inline img, Canvas-safe) with a caption bar."""
    cells = ''.join(
        '<div>'
        '<a href="%s" target="_blank" rel="noopener"><img src="%s" alt="%s" style="display:block;width:100%%;%s" /></a>'
        '<div style="background:rgba(255,255,255,0.92);color:#4a1e02;padding:9px 14px;text-align:center;font-size:10.5pt;'
        'border-top:2px solid #c95201;font-family:Arial,sans-serif;"><strong>&#9658; %s</strong></div>'
        '</div>' % (href, src, alt, FRAME, label)
        for (href, src, alt, label) in videos)
    return ('<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin:6px 0 4px;">%s</div>'
            % cells)

def tile(eyebrow, title, body):
    return ('<div style="%sborder:1px solid transparent;border-image:linear-gradient(135deg,#c95201 0%%,'
            'rgba(201,82,1,0.08) 100%%) 1;padding:20px 22px 24px;position:relative;overflow:hidden;">'
            '<div style="height:3px;background:#c95201;margin:-20px -22px 12px -22px;"></div>'
            '<div style="font-size:9pt;letter-spacing:0.22em;color:#eda268;text-transform:uppercase;margin-bottom:8px;">'
            '<strong>%s</strong></div>'
            '<div style="font-size:16pt;color:#ffffff;line-height:1.15;margin-bottom:8px;"><strong>%s</strong></div>'
            '<div style="height:2px;background:#c95201;width:32px;margin-bottom:10px;"></div>'
            '<div style="font-size:13pt;line-height:1.55;color:rgba(255,255,255,0.84);">%s</div></div>'
            % (WEDGE, eyebrow, title, body))

def notecard(eyebrow, title, body):
    return ('<div style="%sborder:1px solid transparent;border-image:linear-gradient(135deg,#c95201 0%%,'
            'rgba(201,82,1,0.08) 100%%) 1;padding:20px 22px 24px;position:relative;overflow:hidden;margin-top:4px;">'
            '<div style="height:3px;background:#c95201;margin:-20px -22px 12px -22px;"></div>'
            '<div style="font-size:9pt;letter-spacing:0.22em;color:#eda268;text-transform:uppercase;margin-bottom:8px;">'
            '<strong>%s</strong></div>'
            '<div style="font-size:16pt;color:#ffffff;line-height:1.15;margin-bottom:8px;"><strong>%s</strong></div>'
            '<div style="height:2px;background:#c95201;width:32px;margin-bottom:10px;"></div>'
            '<div style="font-size:13pt;line-height:1.55;color:rgba(255,255,255,0.84);">%s</div></div>'
            % (WEDGE, eyebrow, title, body))

def scrollrow(tiles, hint='&laquo; drag or swipe for more &raquo;'):
    inner = ''.join(tiles)
    return ('<div style="display:grid;grid-auto-flow:column;grid-auto-columns:minmax(255px,1fr);overflow-x:auto;'
            'gap:14px;padding-bottom:8px;-webkit-overflow-scrolling:touch;">%s</div>'
            '<div style="text-align:center;font-size:8pt;color:rgba(201,82,1,0.65);letter-spacing:0.22em;'
            'text-transform:uppercase;margin-top:14px;font-family:Arial,sans-serif;"><strong>%s</strong></div>'
            % (inner, hint))

def card(label, title, body):
    return ('<div style="%s%spadding:30px;margin-bottom:24px;position:relative;overflow:hidden;">'
            '<div style="height:4px;background:#c95201;margin:-30px -30px 24px -30px;"></div>'
            '%s%s%s</div>' % (CARD_BG, FRAME, chip(label), tb(title), body))

def banner(eyebrow, title, tagline):
    return ('<div style="background:linear-gradient(135deg,#000000 0%%,#4a1e02 40%%,#c95201 100%%);'
            'padding:20px 28px 22px;margin:-28px -28px 24px -28px;border-bottom:3px solid #c95201;">'
            '<div style="display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;gap:16px;">'
            '<div style="justify-self:start;"><img src="https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/mrc/MRC_Logo.png" alt="Mark Richardson Center" style="width:min(90px,15vw);height:auto;display:block;" /></div>'
            '<div style="justify-self:center;text-align:center;">'
            '<div style="margin-bottom:6px;"><span style="font-size:14pt;color:#eda268;"><strong>%s</strong></span></div>'
            '<div style="color:#ffffff;font-size:24pt;font-weight:700;line-height:1.1;"><strong>%s</strong></div>'
            '<div style="color:rgba(255,255,255,0.82);margin-top:6px;"><span style="font-size:13pt;font-style:italic;"><strong>%s</strong></span></div>'
            '</div>'
            '<div style="justify-self:end;"></div>'
            '</div></div>' % (eyebrow, title, tagline))

NAV = '''  <nav class="silva-nav" aria-label="Module navigation">
    <div class="silva-nav-inner">
      <div class="silva-breadcrumb">
        <a href="/curriculum.html">Curriculum</a>
        <span class="bc-sep">&rsaquo;</span>
        <a href="/curriculum.html#mrc-da1a" class="bc-hide-sm">Digital Arts 1A</a>
        <span class="bc-sep bc-hide-sm">&rsaquo;</span>
        <span class="bc-current">Double Exposure</span>
      </div>
      <div class="silva-nav-spacer"></div>
      <button class="silva-copy-btn" onclick="silvaCopyHTML()" aria-label="Copy Canvas HTML to clipboard">&#128203; Copy Canvas HTML</button>
      <button class="silva-download-btn" onclick="silvaDownloadHTML()" aria-label="Download Canvas HTML as file">&#128229; Download HTML</button>
    </div>
  </nav>'''

SCRIPTS = '''  <script>
    function silvaCopyHTML() {
      const el = document.getElementById('top'); const html = el.outerHTML;
      navigator.clipboard.writeText(html).then(function() {
        var btn = document.querySelector('.silva-copy-btn');
        btn.textContent = '\\u2713 Copied to clipboard!'; btn.classList.add('copied');
        setTimeout(function() { btn.innerHTML = '&#128203; Copy Canvas HTML'; btn.classList.remove('copied'); }, 2500);
      }).catch(function() { alert('Copy failed. Try selecting the page source manually.'); });
    }
    function silvaDownloadHTML() {
      var el = document.getElementById('top'); var html = el.outerHTML;
      var blob = new Blob([html], { type: 'text/html' }); var url = URL.createObjectURL(blob);
      var a = document.createElement('a'); a.href = url; a.download = 'mrc-double-exposure-canvas.html';
      document.body.appendChild(a); a.click(); document.body.removeChild(a); URL.revokeObjectURL(url);
    }
  </script>
  <script src="/js/silva-nav.js"></script>'''

videos = [
    ('https://www.youtube.com/watch?v=h8Rjpae_NwE', IMG + 'doubleexposure-tutorial-01.png',
     'Double Exposure tutorial one, Photoshop', 'Watch Tutorial 1'),
    ('https://www.youtube.com/watch?v=d-lhr83hEhk', IMG + 'doubleexposure-tutorial-02.png',
     'Double Exposure tutorial two, Photoshop', 'Watch Tutorial 2'),
]

steps = [
    tile('Step 01', 'Open Your Base', 'Open your first photo. A <strong>portrait</strong> or a clean <strong>silhouette</strong> works best. This is your bottom layer.'),
    tile('Step 02', 'Add a Second Image', 'Place a second photo on top as a new layer: a <strong>landscape</strong>, a sky, trees, or a texture.'),
    tile('Step 03', 'Change the Blend Mode', 'In the Layers panel, change the top layer&rsquo;s blend mode. Try <strong>Screen</strong> or <strong>Lighten</strong> to drop the dark areas, or <strong>Multiply</strong> to drop the light.'),
    tile('Step 04', 'Mask and Move', 'Add a <strong>layer mask</strong> and paint with black to hide parts you do not want. Move and resize the top image until it sits right.'),
    tile('Step 05', 'Adjust to Finish', 'Tweak <strong>brightness, contrast, and color</strong> so the two photos read as one image.'),
]

body = ''.join([
    headerph('A wide hero image for the Double Exposure exercise: a portrait or silhouette fused with a landscape or texture, MRC orange accents.'),
    card('WHAT IS A DOUBLE EXPOSURE / 01 / 04', 'Two Photos, One Image',
         para('A <strong>double exposure</strong> blends two photos into a single image. The classic look is a <strong>portrait or silhouette</strong> filled with a second picture: a forest, a city, clouds, or water. It is one of the fastest ways to make something that looks like real art.')
         + para('The secret is <strong>blending modes</strong>: a Photoshop setting that changes how one layer mixes with the layer underneath it. Today you will stack two images and use blending modes to fuse them.')),
    card('WATCH THE TUTORIALS / 02 / 04', 'See It Done First',
         para('Watch both short tutorials before you start. They walk through the exact steps in Photoshop. <strong>Click a thumbnail</strong> to open it on YouTube.')
         + videorow(videos)),
    card('HOW TO BLEND / 03 / 04', 'Make Your Own',
         para('Here is the quick version. Follow the videos for the full details, then build your own.')
         + scrollrow(steps)
         + notecard('BLENDING MODES', 'Screen, Lighten, Multiply', 'Blending modes control how layers mix. <strong>Screen</strong> and <strong>Lighten</strong> keep the bright parts of the top layer; <strong>Multiply</strong> keeps the dark parts. Cycle through them and watch what happens, there is no wrong answer.')),
    card('TURN IT IN / 04 / 04', 'Export and Submit',
         para('When your double exposure looks good, flatten it with <strong>Layer &gt; Flatten Image</strong>, then export a <strong>JPG</strong> with <strong>File &gt; Save a Copy</strong>.')
         + para('Submit your JPG to this assignment in Canvas. Name it: <strong>FirstName LastInitial - Double Exposure.jpg</strong>')
         + para('Experiment and have fun. There is no single right look, so try a few image combinations and pick your favorite.')),
])

html = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '  <meta charset="UTF-8" />\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
        '  <title>Double Exposure | Digital Arts 1A | Mark Richardson Center</title>\n'
        '  <link rel="icon" type="image/svg+xml" href="/logos/CS_Logo_Only.svg" />\n'
        '  <link rel="apple-touch-icon" href="/logos/CS_Logo_Only.svg" />\n'
        '  <style>:root { --course-accent: #c95201; }</style>\n'
        '  <link rel="stylesheet" href="/css/silva-module.css" />\n'
        '</head>\n<body>\n' + NAV + '\n'
        '  <div class="silva-page">\n  <div id="silva-module-content">\n'
        '  <div id="top" style="width:100%;margin:0 auto;font-family:Arial,sans-serif;color:#ffffff;'
        'background-color:#080808;background-image:linear-gradient(180deg,rgba(8,8,8,0.97) 0%,'
        'rgba(40,20,2,0.94) 50%,rgba(8,8,8,0.97) 100%);background-position:center center;'
        'background-repeat:no-repeat;background-attachment:fixed;overflow:hidden;">\n\n'
        '    <div style="padding:28px 28px 40px;">\n      '
        + banner('Digital Arts 1A &nbsp;&bull;&nbsp; Creative Exercise', 'Double Exposure',
                 'Blend two photos into one with blending modes.')
        + body +
        '\n    </div>\n\n  </div>\n  </div>\n  </div>\n' + SCRIPTS + '\n</body>\n</html>\n')

path = os.path.join(OUT, 'double-exposure.html')
open(path, 'w').write(html)
print('double-exposure.html  divs=%s  em=%d'
      % ('OK' if html.count('<div') == html.count('</div>') else 'IMBALANCE',
         html.count('—') + html.count('&mdash;')))
