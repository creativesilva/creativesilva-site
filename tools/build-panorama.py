#!/usr/bin/env python3
"""Generate the MRC Digital Arts 1A "Panorama Project" module (English).
Four Canvas pages on the locked Angular Gradient Framework (orange
#c95201), lead character Ricardo Gomez:

  1 overview                panorama-overview.html
  2 step01 capture (RAW)    panorama-step01-capture.html
  3 step02 merge (PS)       panorama-step02-merge.html
  4 step03 reflection       panorama-step03-reflection.html

Photoshop steps follow the 2026 Photomerge workflow. Reflection uses a
downloadable Word template (built by build-panorama-reflection.js).
"""
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'curriculum', 'mrc')
RAW = 'https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/mrc/images/'
ZIP_URL = 'https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/mrc/handouts/Panorama.zip'

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

def floatimg(src, alt):
    return ('<img src="%s" alt="%s" style="float:right;width:42%%;min-width:240px;margin:0 0 18px 26px;%s" />'
            % (src, alt, FRAME))

def ph(desc):
    return ('<div style="background:linear-gradient(135deg,rgba(201,82,1,0.12) 0%,rgba(0,0,0,0.45) 100%);'
            'border:2px solid transparent;border-image:linear-gradient(135deg,#c95201 0%,rgba(201,82,1,0.08) 100%) 1;'
            'padding:26px 22px;text-align:center;float:right;width:42%;min-width:240px;margin:0 0 18px 26px;">'
            '<div style="font-size:10pt;letter-spacing:0.22em;text-transform:uppercase;color:#eda268;margin-bottom:10px;">'
            '<strong>Image Placeholder</strong></div>'
            '<div style="font-size:11.5pt;line-height:1.6;color:rgba(255,255,255,0.66);font-style:italic;">'
            + desc + '</div></div>')

def headerph(desc):
    """Full-width ultra-wide header placeholder (16:6 hero image)."""
    return ('<div style="background:linear-gradient(135deg,rgba(201,82,1,0.12) 0%,rgba(0,0,0,0.45) 100%);'
            'border:2px solid transparent;border-image:linear-gradient(135deg,#c95201 0%,rgba(201,82,1,0.08) 100%) 1;'
            'padding:46px 30px;text-align:center;margin-bottom:24px;">'
            '<div style="font-size:10pt;letter-spacing:0.22em;text-transform:uppercase;color:#eda268;margin-bottom:10px;">'
            '<strong>Header Image Placeholder &bull; 16:6 Ultra-Wide</strong></div>'
            '<div style="font-size:12pt;line-height:1.6;color:rgba(255,255,255,0.66);font-style:italic;max-width:760px;margin:0 auto;">'
            + desc + '</div></div>')

def headerimg(src, alt):
    """Full-width ultra-wide header image (16:6 hero)."""
    return ('<img src="%s" alt="%s" style="width:100%%;display:block;margin-bottom:24px;%s" />'
            % (src, alt, FRAME))

def imgfull(src, alt, caption):
    """Full-width framed example image with a small caption."""
    return ('<img src="%s" alt="%s" style="width:100%%;display:block;margin:6px 0 8px;%s" />'
            '<div style="font-size:9pt;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.55);'
            'text-align:center;margin-bottom:6px;font-family:Arial,sans-serif;"><strong>%s</strong></div>'
            % (src, alt, FRAME, caption))

def card(label, title, body, floatel=''):
    return ('<div style="%s%spadding:30px;margin-bottom:24px;position:relative;overflow:hidden;">'
            '<div style="height:4px;background:#c95201;margin:-30px -30px 24px -30px;"></div>'
            '%s%s%s%s</div>' % (CARD_BG, FRAME, floatel, chip(label), tb(title), body))

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

def vscroll(tiles, hint='&#8597; scroll for more steps &#8597;'):
    inner = ''.join('<div style="margin-bottom:12px;">%s</div>' % t for t in tiles)
    return ('<div style="max-height:560px;overflow-y:auto;padding-right:8px;-webkit-overflow-scrolling:touch;">%s</div>'
            '<div style="text-align:center;font-size:8pt;color:rgba(201,82,1,0.65);letter-spacing:0.22em;'
            'text-transform:uppercase;margin-top:14px;font-family:Arial,sans-serif;"><strong>%s</strong></div>'
            % (inner, hint))

def fname(text):
    return ('<div style="font-size:14pt;color:#eda268;margin-bottom:14px;font-family:Arial,sans-serif;">'
            '<strong>%s</strong></div>' % text)

def dlbutton(href, label):
    return ('<a href="%s" download="" style="background:rgba(255,255,255,0.92);color:#4a1e02;text-decoration:none;'
            'padding:7px 16px;display:inline-block;font-size:11pt;white-space:nowrap;border-top:2px solid #c95201;">'
            '<strong>%s</strong></a>' % (href, label))

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

def stepnav(links):
    btns = ''.join('<a href="%s" class="silva-step-btn">%s</a>' % (href, lbl) for href, lbl in links)
    return '<div class="silva-step-nav">%s</div><div class="silva-nav-div"></div>' % btns

NAV = '''  <nav class="silva-nav" aria-label="Module navigation">
    <div class="silva-nav-inner">
      <div class="silva-breadcrumb">
        <a href="/curriculum.html">Curriculum</a>
        <span class="bc-sep">&rsaquo;</span>
        <a href="/curriculum.html#mrc-da1a" class="bc-hide-sm">Digital Arts 1A</a>
        <span class="bc-sep bc-hide-sm">&rsaquo;</span>
        <span class="bc-current">%(crumb)s</span>
      </div>
      <div class="silva-nav-spacer"></div>
      %(stepnav)s
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
      var a = document.createElement('a'); a.href = url; a.download = '%(dl)s';
      document.body.appendChild(a); a.click(); document.body.removeChild(a); URL.revokeObjectURL(url);
    }
  </script>
  <script src="/js/silva-nav.js"></script>'''

def page(filename, title_tag, crumb, links, dl, eyebrow, btitle, tagline, cards):
    body = ''.join(cards)
    html = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n'
            '  <meta charset="UTF-8" />\n'
            '  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
            '  <title>%s</title>\n' % title_tag +
            '  <link rel="icon" type="image/svg+xml" href="/logos/CS_Logo_Only.svg" />\n'
            '  <link rel="apple-touch-icon" href="/logos/CS_Logo_Only.svg" />\n'
            '  <style>:root { --course-accent: #c95201; }</style>\n'
            '  <link rel="stylesheet" href="/css/silva-module.css" />\n'
            '</head>\n<body>\n' +
            (NAV % {'crumb': crumb, 'stepnav': stepnav(links)}) + '\n'
            '  <div class="silva-page">\n  <div id="silva-module-content">\n'
            '  <div id="top" style="width:100%;margin:0 auto;font-family:Arial,sans-serif;color:#ffffff;'
            'background-color:#080808;background-image:linear-gradient(180deg,rgba(8,8,8,0.97) 0%,'
            'rgba(40,20,2,0.94) 50%,rgba(8,8,8,0.97) 100%);background-position:center center;'
            'background-repeat:no-repeat;background-attachment:fixed;overflow:hidden;">\n\n'
            '    <div style="padding:28px 28px 40px;">\n      ' +
            banner(eyebrow, btitle, tagline) + body +
            '\n    </div>\n\n  </div>\n  </div>\n  </div>\n' +
            (SCRIPTS % {'dl': dl}) + '\n</body>\n</html>\n')
    open(os.path.join(OUT, filename), 'w').write(html)
    print('  %s  divs=%s  em=%d' % (filename, 'OK' if html.count('<div') == html.count('</div>') else 'IMBALANCE',
                                    html.count('—') + html.count('&mdash;')))

# =========================================================================
# PAGE 1 — OVERVIEW
# =========================================================================
mission = [
    tile('STEP 01', 'Capture', 'Shoot RAW images for two panoramas with a camera and tripod, then turn in a screenshot of your RAW folder.'),
    tile('STEP 02', 'Merge & Edit', 'Stitch each set of photos into one wide panorama in Photoshop, then submit two finished JPGs.'),
    tile('STEP 03', 'Reflect', 'Answer four short questions about how your panorama project went.'),
]
page(
    'panorama-overview.html',
    'Overview | Panorama Project | Digital Arts 1A | Mark Richardson Center',
    'Overview', [('panorama-step01-capture.html', 'Step 1 &#8594;')],
    'mrc-panorama-overview-canvas.html',
    'Digital Arts 1A &nbsp;&bull;&nbsp; Module', 'Panorama Project',
    'Stitch many photos into one wide world.',
    [
        headerimg(RAW + 'pano-header.png', 'A photography student capturing a wide panorama of the futuristic MRC campus at golden hour, with crops and livestock corrals in the foreground'),
        card('WHAT IS A PANORAMA / 01 / 04', 'One Photo, Wide as the World',
             para('A panorama is a very wide photo made by joining several photos into one. It captures far more than a single shot can: a whole landscape, a long hallway, or a city skyline.')
             + para('You take a row of photos that <strong>overlap</strong>, then the computer stitches them edge to edge into one wide image. The result tells a visual story across movement and space.')),
        card('THE TWO PARTS / 02 / 04', 'Capture, Then Merge',
             para('This is a two-part project. In <strong>Part A</strong> (Step 1) you photograph RAW images for two panoramas with a camera and tripod. In <strong>Part B</strong> (Step 2) you stitch and edit them in Photoshop. Then you finish with a short reflection.')
             + para('You will make at least <strong>two panoramas</strong>, each built from <strong>4 to 5 photos</strong>.')
             + notecard('START HERE', 'Download Your Project Folder', 'Download the <strong>Panorama</strong> folder below and move it into your <strong>OneDrive Digital Arts</strong> folder. Inside you will find a <strong>RAW Images</strong> folder for your photos and your <strong>reflection</strong> sheet. Keep all of your project work in this one folder from start to finish.')
             + '<div style="margin-top:18px;">' + dlbutton(ZIP_URL, 'Download the Panorama Project Folder') + '</div>'),
        card('SHOOTING IN RAW / 03 / 04', 'Why RAW This Time',
             para('This time you shoot in <strong>RAW</strong>, not JPEG. A RAW file keeps all the data the camera sensor captured, so you can fix exposure and color later with no loss in quality. On our Canon cameras, RAW files end in <strong>.CR3</strong>.')
             + para('RAW files are larger and need editing software to open and merge. That is exactly what Photoshop is for in Part B.')),
        card('YOUR MISSION / 04 / 04', 'What You Will Do',
             para('You will work like a real photographer: capture, merge, and reflect. Three steps, three turn-ins.')
             + scrollrow(mission)),
    ],
)

# =========================================================================
# PAGE 2 — STEP 01 CAPTURE
# =========================================================================
setup = [
    tile('Setup 01', 'Format the SD Card', 'Erase old photos first so you have room and start clean. Format the card in the camera menu.'),
    tile('Setup 02', 'Set Quality to RAW', 'In the menu, set image quality to <strong>RAW only</strong>, no JPEG. On our Canon cameras this makes .CR3 files.'),
    tile('Setup 03', 'Mount the Tripod', 'Put the camera on a tripod and level it. A steady, level camera is the key to a clean stitch.'),
    tile('Setup 04', 'Switch to AV Mode', 'Use <strong>AV</strong> (aperture priority). Pick your aperture: a low f-stop like <strong>f/4</strong> blurs the background; a high f-stop like <strong>f/11</strong> keeps more in focus.'),
    tile('Setup 05', 'Set Your Exposure', 'Check the light meter. The photo should not be too dark or too bright. Take a test shot and adjust.'),
]
shoot = [
    tile('Shoot 01', 'Take 4 to 5 Photos', 'Shoot 4 to 5 RAW photos for one panorama, moving across the scene from one side to the other.'),
    tile('Shoot 02', 'Pan Slow and Level', 'Turn slowly in a level, horizontal motion. Keep the camera flat the whole way across.'),
    tile('Shoot 03', 'Overlap Each Shot', 'Overlap each photo with the one before it by <strong>about a third</strong> so Photoshop can match them up. More on this rule next.'),
    tile('Shoot 04', 'Lock Focus (Optional)', 'For a blurry background, turn off autofocus after your first shot so focus stays the same. Turn autofocus back on when you finish, for the next student.'),
    tile('Shoot 05', 'Check Your Shots', 'Look at your photos on the back screen. If one is blurry or you missed the overlap, shoot the whole set again.'),
]
handheld = [
    tile('Tip 01', 'Use a Wide Lens', 'Zoom out wide if you can. A wide view is more forgiving and hides small wobbles between shots.'),
    tile('Tip 02', 'Brace Your Arms', 'Tuck your elbows tight against your sides and hold the camera with both hands. Your body becomes the tripod.'),
    tile('Tip 03', 'Turn at the Hips', 'Keep your feet planted and rotate your whole upper body from the hips. That makes a smooth, even sweep.'),
    tile('Tip 04', 'Try a Tabletop', 'No steady hands? Rest the camera on a flat surface like a table or a wall, and slide or turn it a little at a time in one direction.'),
    tile('Tip 05', 'Overlap Even More', 'Without a tripod your aim drifts, so overlap each shot by a third or more. Extra overlap saves a handheld stitch.'),
]
page(
    'panorama-step01-capture.html',
    'Step 1: Capture | Panorama Project | Digital Arts 1A | Mark Richardson Center',
    'Step 1',
    [('panorama-overview.html', '&#8592; Overview'), ('panorama-step02-merge.html', 'Step 2 &#8594;')],
    'mrc-panorama-step01-capture-canvas.html',
    'Panorama Project &nbsp;&bull;&nbsp; Step 1', 'Capture Your RAW Images',
    'Camera, tripod, and RAW files.',
    [
        card('YOUR TWO PANORAMAS / 01 / 07', 'One on Campus, One at Home',
             para('You will make <strong>two panoramas</strong> for this project. You shoot one here on campus in class, with the camera on a <strong>tripod</strong>. You shoot the other one at home for homework, holding the <strong>Canon R50</strong> in your hands.')
             + para('Each panorama is <strong>4 to 5 photos</strong> that overlap. Look for wide scenes with interesting textures, structures, or open space.')),
        card('SET UP YOUR CAMERA / 02 / 07', 'Camera and Tripod Setup',
             para('Get your gear ready before you shoot the campus panorama. Scroll through each setup step.')
             + '<div style="clear:both;"></div>'
             + vscroll(setup),
             floatimg(RAW + 'pano-capture-float.png', 'Ricardo Gomez setting up a DSLR camera on a tripod at the MRC campus')),
        card('SHOOT THE PANORAMA / 03 / 07', 'Pan Slow and Overlap',
             para('Now capture your photos. Move across the scene in even, overlapping steps.')
             + para('<strong>Focus pro tip:</strong> if the camera will not lock focus, flip the <strong>AF / MF</strong> switch to <strong>MF</strong> (manual focus). That turns on the focus ring on the lens so you can twist it to set focus by hand. Switch it back to <strong>AF</strong> when you finish, for the next student.')
             + '<div style="clear:both;"></div>'
             + vscroll(shoot),
             floatimg(RAW + 'pano-camera-mf.png', 'Canon camera back with the AF / MF button circled')),
        card('THE KEY RULE / 04 / 07', 'Overlap Is Everything',
             para('This is the most important rule in the whole project: your photos must <strong>overlap</strong>. Overlap means each photo shares part of the same view with the photo next to it.')
             + para('Photoshop builds your panorama by matching the parts that repeat. If two photos share enough of the same details, it lines them up and blends them into one smooth image. If they do not share enough, the stitch breaks, leaves gaps, or looks crooked.')
             + para('Overlap each photo with the one before it by <strong>about a third</strong> (30 to 40 percent). When you are not sure, <strong>overlap more, not less</strong>. Extra overlap is free insurance for a clean stitch.')
             + notecard('PRO TIP', 'Pick a Marker', 'Find an object near the right edge of your photo, like a post or a tree. Put that same object near the left edge of your next photo. That guarantees enough overlap every time.')),
        card('ORGANIZE YOUR FILES / 05 / 07', 'Keep It Organized',
             para('Use the <strong>Panorama</strong> folder you downloaded from the overview. If you have not yet, move it into your <strong>OneDrive Digital Arts</strong> folder.')
             + para('Offload all your <strong>.CR3</strong> RAW files into the <strong>RAW Images</strong> subfolder inside it. Keep every part of this project organized here from start to finish, including your reflection at the end.')),
        card('TURN IT IN / 06 / 07', 'Screenshot Your RAW Folder',
             para('Open <strong>Finder</strong> and switch to <strong>Icon view</strong> so you can see the photo thumbnails.')
             + para('Open your <strong>RAW Images</strong> folder. Make sure the window shows the folder name <strong>RAW Images</strong> at the top and your image thumbnails inside. No contact sheet, just the folder.')
             + para('Press the <strong>F15</strong> key to take the screenshot. On our Macs, F15 saves the screenshot straight to your <strong>Desktop</strong> as a PNG.')
             + para('Find it on the Desktop and rename it:')
             + fname('FirstName LastInitial - Panorama (PNG)')
             + imgfull(RAW + 'pano-raw-folder-screenshot.png', 'Example screenshot of a RAW Images folder in Finder Icon view', 'Your screenshot should look like this')
             + para('Upload the PNG screenshot of your <strong>campus</strong> photos to Step 1 in Canvas to finish Part A.')),
        card('TAKE IT HOME / 07 / 07', 'Shoot One Without a Tripod',
             para('For homework, take the <strong>Canon R50</strong> home and shoot your <strong>second panorama</strong> off campus, with no tripod. You will edit it next to your campus one in Step 2.')
             + para('No tripod is harder, but these tricks keep your photos steady and even. Same rules apply: pan slowly, keep the camera level, and overlap a lot.')
             + scrollrow(handheld)
             + notecard('REMEMBER', 'Same Direction, Even Steps', 'Move in one direction only, in small even steps. Do not skip ahead or jump back, and keep your overlap high.')),
    ],
)

# =========================================================================
# PAGE 3 — STEP 02 MERGE
# =========================================================================
merge = [
    tile('Merge 01', 'Keep Layout on Auto', 'In the Photomerge window, leave <strong>Layout</strong> set to <strong>Auto</strong>. It works best for most panoramas.'),
    tile('Merge 02', 'Browse and Select', 'Click <strong>Browse</strong>. Go to your <strong>RAW Images</strong> folder and select the 4 to 5 <strong>.CR3</strong> files for <strong>one</strong> panorama. Click OK.'),
    tile('Merge 03', 'Check the Boxes', 'Turn on <strong>Blend Images Together</strong>, <strong>Vignette Removal</strong>, and <strong>Geometric Distortion Correction</strong>.'),
    tile('Merge 04', 'Fill the Edges', 'Also check <strong>Content Aware Fill Transparent Areas</strong> to fill the empty edges for you, then click <strong>OK</strong>. <strong>Watch out:</strong> if the fill looks fake or messy, you can crop those edges off later, or run Photomerge again with this box unchecked.'),
    tile('Merge 05', 'Let It Build', 'Photoshop opens each RAW file through Camera Raw, lines them up, and blends them into one layered panorama. Give it a minute.'),
]
page(
    'panorama-step02-merge.html',
    'Step 2: Merge | Panorama Project | Digital Arts 1A | Mark Richardson Center',
    'Step 2',
    [('panorama-step01-capture.html', '&#8592; Step 1'), ('panorama-step03-reflection.html', 'Step 3 &#8594;')],
    'mrc-panorama-step02-merge-canvas.html',
    'Panorama Project &nbsp;&bull;&nbsp; Step 2', 'Merge in Photoshop',
    'Stitch your photos into one wide image.',
    [
        card('OPEN PHOTOMERGE / 01 / 04', 'Start Photomerge',
             para('Open Photoshop. Go to <strong>File &gt; Automate &gt; Photomerge</strong>. This is the tool that stitches your photos into one panorama.')
             + para('You will run it <strong>twice</strong>: once for your <strong>campus</strong> photos and once for your <strong>home</strong> photos.')),
        card('BUILD THE PANORAMA / 02 / 04', 'Choose and Blend',
             para('Set up the merge in the Photomerge window. Scroll through each step.')
             + '<div style="clear:both;"></div>'
             + vscroll(merge),
             floatimg(RAW + 'pano-merge-float.png', 'Julian merging a panorama in Photoshop at an iMac in the MRC computer lab')),
        card('CLEAN IT UP / 03 / 04', 'Flatten, Crop, Adjust',
             para('Flatten the layers into one image: <strong>Layer &gt; Flatten Image</strong>.')
             + para('Crop off any uneven or fake-looking edges with the <strong>Crop tool</strong>. If you left Content Aware Fill on and it looks great, you may not need to crop much at all.')
             + para('Adjust your photo with the <strong>Camera Raw Filter</strong> (<strong>Filter &gt; Camera Raw Filter</strong>) or adjustment layers. Fix the exposure, contrast, and color until it looks great.')
             + para('Now do this whole process again for your <strong>other</strong> panorama (your home one).')),
        card('SAVE AND SUBMIT / 04 / 04', 'Save Big, Submit Both',
             para('Save each panorama as a layered <strong>.PSD</strong> in your <strong>Panorama</strong> folder so you keep your work.')
             + para('Then export each as a large <strong>JPG</strong>: <strong>File &gt; Save a Copy</strong>, choose JPG, full size. Name them:')
             + fname('FirstName LastInitial - Panorama Campus.jpg &nbsp;and&nbsp; FirstName LastInitial - Panorama Home.jpg')
             + para('Submit <strong>both</strong> finished panorama JPGs, your campus one and your home one, to Step 2 in Canvas.')),
    ],
)

# =========================================================================
# PAGE 4 — STEP 03 REFLECTION
# =========================================================================
questions = [
    tile('Question 01', 'What Worked', 'What worked well in your panoramas? What are you proud of?'),
    tile('Question 02', 'What Did Not', 'What did not work, or what was tricky during shooting or merging?'),
    tile('Question 03', 'Do Differently', 'What would you do differently next time to make a better panorama?'),
    tile('Question 04', 'Favorite and Dream', 'What did you like most about this project? And if you could shoot a panorama of anywhere in the world, where would it be and why?'),
]
page(
    'panorama-step03-reflection.html',
    'Step 3: Reflection | Panorama Project | Digital Arts 1A | Mark Richardson Center',
    'Step 3',
    [('panorama-step02-merge.html', '&#8592; Step 2')],
    'mrc-panorama-step03-reflection-canvas.html',
    'Panorama Project &nbsp;&bull;&nbsp; Step 3', 'Reflection',
    'Look back at what you made.',
    [
        card('HOW IT WORKS / 01 / 02', 'Answer Four Questions',
             para('A reflection helps you learn from your work. Open the <strong>reflection document</strong> inside your <strong>Panorama project folder</strong> (the one you downloaded at the start). Answer all four questions in complete sentences.')
             + '<div style="clear:both;"></div>'
             + scrollrow(questions),
             floatimg(RAW + 'pano-reflection-float.png', 'Renee Lopez typing her panorama reflection at an iMac in the MRC computer lab')),
        card('TURN IT IN / 02 / 02', 'Submit Your Reflection',
             para('Type your answers into the reflection document and save it. Name your file:')
             + fname('FirstName LastInitial - Panorama Reflection.docx')
             + para('Upload your finished reflection to Step 3 in Canvas to complete the project.')),
    ],
)

print('done')
