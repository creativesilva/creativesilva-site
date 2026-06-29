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

def floatimg(src, alt):
    return ('<img src="%s" alt="%s" style="float:right;width:42%%;min-width:240px;margin:0 0 18px 26px;%s" />'
            % (src, alt, FRAME))

def headerimg(src, alt):
    return ('<div style="margin-bottom:24px;"><img src="%s" alt="%s" style="width:100%%;height:auto;display:block;%s" /></div>'
            % (src, alt, FRAME))

def ilink(href, label):
    return ('<a href="%s" target="_blank" rel="noopener" style="color:#eda268;text-decoration:underline;"><strong>%s</strong></a>'
            % (href, label))

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

mask_steps = [
    tile('Cut Out 01', 'Open Select and Mask', 'With your portrait layer active, go to <strong>Select &gt; Select and Mask</strong> to open the workspace.'),
    tile('Cut Out 02', 'Click Select Subject', 'At the top, click <strong>Select Subject</strong>. Photoshop finds the person automatically.'),
    tile('Cut Out 03', 'Refine the Edges', 'Run the <strong>Refine Edge</strong> brush along the hair and edges to clean up the selection.'),
    tile('Cut Out 04', 'Output to Layer Mask', 'Set <strong>Output To: Layer Mask</strong> and click OK. Your subject is cut out and the background is gone.'),
    tile('Cut Out 05', 'Why a Simple Background', 'This is why you shoot against a <strong>plain, solid background</strong>: the subject separates cleanly and masks in seconds.'),
]

blend_steps = [
    tile('Blend 01', 'Find the Menu', 'In the <strong>Layers</strong> panel, click the dropdown that says <strong>Normal</strong> at the top. That is the blend mode menu for the selected layer.'),
    tile('Blend 02', 'What It Does', 'A blend mode changes how the top layer mixes with the layer below it, based on the light and dark pixels.'),
    tile('Blend 03', 'Screen', '<strong>Screen</strong> drops the dark areas and keeps the bright ones. Great for a light texture over a darker portrait.'),
    tile('Blend 04', 'Lighten', '<strong>Lighten</strong> keeps whichever pixels are brighter. Similar to Screen, a little punchier.'),
    tile('Blend 05', 'Multiply', '<strong>Multiply</strong> drops the bright areas and keeps the dark ones. Great for dark trees over a lighter portrait.'),
    tile('Blend 06', 'Cycle and Compare', 'Move down the list and watch the live preview. Pick the mode that fuses your two images best.'),
]

raw_steps = [
    tile('RAW 01', 'Shoot in RAW', 'Set your camera to <strong>RAW</strong>. Your Canon saves a <strong>.CR3</strong> file that holds far more detail than a JPG, so you can push the edit further without it falling apart.'),
    tile('RAW 02', 'Open It in Photoshop', 'In Photoshop, go to <strong>File &gt; Open</strong> (or press <strong>Command + O</strong>) and choose your <strong>.CR3</strong> file.'),
    tile('RAW 03', 'Camera Raw Opens', 'Because it is a RAW file, the <strong>Camera Raw</strong> window opens automatically. This is where you set your look before the photo ever reaches Photoshop.'),
    tile('RAW 04', 'Lock In Your Aesthetic', 'Adjust <strong>exposure, contrast, white balance, and color</strong> until the portrait has the mood you want. These are the same sliders as the Camera Raw Filter. Set your aesthetic here.'),
    tile('RAW 05', 'Open Onto the Artboard', 'Click <strong>Open</strong> (or Open Image) to drop the processed photo onto a Photoshop <strong>artboard</strong>, ready to cut out and blend.'),
]

vocab = [
    tile('Vocabulary', 'Double Exposure', 'Two images blended into one. The look comes from old film cameras exposing a single frame twice.'),
    tile('Vocabulary', 'Blending Mode', 'A layer setting that controls how a layer mixes with the one below it.'),
    tile('Vocabulary', 'Layer Mask', 'A black-and-white attachment that hides or shows parts of a layer. Black hides, white shows.'),
    tile('Vocabulary', 'Select and Mask', 'The Photoshop workspace for making and refining a selection, especially around hair and edges.'),
    tile('Vocabulary', 'Opacity', 'How see-through a layer is, from 0% (invisible) to 100% (solid).'),
    tile('Vocabulary', 'Silhouette', 'A subject shown as a solid dark shape against a lighter background.'),
    tile('Vocabulary', 'RAW (CR3)', 'An unprocessed image straight off the camera sensor. Canon&rsquo;s version is the .CR3. It holds far more editing data than a JPG.'),
    tile('Vocabulary', 'Camera Raw', 'The window that opens when you open a RAW file, where you set exposure, color, and contrast before Photoshop.'),
]

body = ''.join([
    headerimg(IMG + 'doubleexposure-header.png', 'An MRC student photographing a classmate for a portrait against a plain wall at the Santa Maria Academy of Arts'),
    card('WHAT IS A DOUBLE EXPOSURE / 01 / 08', 'Two Photos, One Image',
         floatimg(IMG + 'doubleexposure-example.png', 'A finished double exposure: a profile portrait blended with a mountain landscape')
         + para('A <strong>double exposure</strong> blends two photos into a single image. The classic look is a <strong>portrait or silhouette</strong> filled with a second picture: a forest, a city, clouds, or water. It is one of the fastest ways to make something that looks like real art.')
         + para('The secret is <strong>blending modes</strong>: a Photoshop setting that changes how one layer mixes with the layer underneath it. Today you will photograph a portrait in RAW, process it in Camera Raw, cut out your subject, and fuse it with a second image.')),
    card('WATCH THE TUTORIALS / 02 / 08', 'See It Done First',
         para('Watch both short tutorials before you start. They walk through the exact steps in Photoshop. <strong>Click a thumbnail</strong> to open it on YouTube.')
         + videorow(videos)),
    card('GET YOUR TWO IMAGES / 03 / 08', 'Shoot One, Source One',
         para('You need <strong>two images</strong>. The first one you must <strong>photograph yourself</strong>.')
         + para('<strong>Image 1, the portrait:</strong> Photograph a <strong>portrait or headshot</strong> of a person. Shoot them against a <strong>solid, simple background</strong> like a plain wall, so you can cut them out cleanly later.')
         + para('<strong>Image 2, the blend image:</strong> This is the picture that fills your subject. You can <strong>photograph it</strong> too, or download one free from <strong>Unsplash</strong>. Good choices: trees, mountains, a city skyline, fog, smoke, or water.')
         + notecard('FREE IMAGES', 'Find One That Is Free', 'Search for a blend image on ' + ilink('https://unsplash.com', 'unsplash.com &rarr;') + ' or the web, like &ldquo;forest&rdquo; or &ldquo;mountains.&rdquo; Heads up: <strong>not every image is free to download</strong>. Some need an <strong>account</strong> or a paid plan, and search results often link to <strong>paid stock sites</strong> like Shutterstock or iStock. <strong>Search for free images</strong>, then browse and pick one that is <strong>entirely free</strong> and also works for your photo. On Unsplash, open the photo and click <strong>Download free</strong>, then bring it into Photoshop.')),
    card('OPEN YOUR RAW FILE / 04 / 08', 'Process the RAW First',
         para('You are shooting your portrait in <strong>RAW</strong>, a Canon <strong>.CR3</strong> file. Before you blend anything, open it and lock in your look in <strong>Camera Raw</strong>.')
         + scrollrow(raw_steps)
         + notecard('WHY RAW', 'More Room to Edit', 'A RAW file keeps all the data straight off the sensor, so you can fix exposure and color with no quality loss. Set your aesthetic in Camera Raw first, then click Open to keep building in Photoshop.')),
    card('CUT OUT YOUR SUBJECT / 05 / 08', 'Mask With Select and Mask',
         para('To blend cleanly, separate your subject from their background. You know this workflow: <strong>Select &gt; Select and Mask &gt; Select Subject</strong>. Here is the quick refresher.')
         + scrollrow(mask_steps)),
    card('BLEND WITH BLENDING MODES / 06 / 08', 'Fuse the Two Images',
         para('Place your <strong>blend image</strong> on top of your cut-out portrait, then change its <strong>blend mode</strong> to fuse them. Here is where to find blend modes and what the main ones do.')
         + scrollrow(blend_steps)
         + notecard('EXPERIMENT', 'There Is No Wrong Answer', 'Cycle through the blend modes and watch the preview. Move and resize your blend image, lower the <strong>opacity</strong>, and add a <strong>layer mask</strong> to hide parts you do not want. Keep going until the two photos feel like one.')),
    card('WORDS TO KNOW / 07 / 08', 'Double Exposure Vocabulary',
         para('Learn these eight terms. You will use them through the whole exercise.')
         + scrollrow(vocab)),
    card('TURN IT IN / 08 / 08', 'Export and Submit',
         para('Make <strong>two or three different double exposures</strong> using different blend images or different blend modes. Experimenting is the point, so do not stop at one.')
         + para('For each one, flatten it with <strong>Layer &gt; Flatten Image</strong> and export a <strong>JPG</strong> with <strong>File &gt; Save a Copy</strong>.')
         + para('Submit your <strong>2 to 3 final JPG files</strong> to this assignment in Canvas. Name them: <strong>FirstName LastInitial - Double Exposure 1.jpg</strong>, and so on.')),
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
