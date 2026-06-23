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
DOCX_URL = 'https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/mrc/study-guides/MRC_Panorama_Reflection.docx'

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
        headerph('Over-the-shoulder rear view at a 45-degree angle of Renee Lopez (21, warm medium-brown skin, shoulder-length curly dark-brown hair, gold hoop earrings, gray MS monogram tee, light-blue flared jeans), framed from the knees up, standing at a DSLR camera on a tripod and aiming it toward the Mark Richardson Center campus far in the distance. Golden hour, long warm shadows. The campus is a futuristic agricultural trade school of brushed steel, glass, and sculptural structural panels with soft orange ambient glows. Mid-ground rows of crops and fenced-off corrals with livestock. Shallow depth of field on the campus, sharp on Renee and the tripod. Warm amber palette, gentle lens flare, photoreal.'),
        card('WHAT IS A PANORAMA / 01 / 04', 'One Photo, Wide as the World',
             para('A panorama is a very wide photo made by joining several photos into one. It captures far more than a single shot can: a whole landscape, a long hallway, or a city skyline.')
             + para('You take a row of photos that <strong>overlap</strong>, then the computer stitches them edge to edge into one wide image. The result tells a visual story across movement and space.')),
        card('THE TWO PARTS / 02 / 04', 'Capture, Then Merge',
             para('This is a two-part project. In <strong>Part A</strong> (Step 1) you photograph RAW images for two panoramas with a camera and tripod. In <strong>Part B</strong> (Step 2) you stitch and edit them in Photoshop. Then you finish with a short reflection.')
             + para('You will make at least <strong>two panoramas</strong>, each built from <strong>4 to 5 photos</strong>.')),
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
    tile('Shoot 03', 'Overlap Each Shot', 'Overlap each photo with the one before it by <strong>15 to 20 percent</strong> so the computer can match them up.'),
    tile('Shoot 04', 'Lock Focus (Optional)', 'For a blurry background, turn off autofocus after your first shot so focus stays the same. Turn autofocus back on when you finish, for the next student.'),
    tile('Shoot 05', 'Do It Again', 'Move to a different spot and shoot your second panorama the same way. Two panoramas total.'),
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
        card('CHOOSE TWO LOCATIONS / 01 / 05', 'Pick Two Scenes',
             para('Choose <strong>2 locations</strong>, indoors or outdoors. Look for interesting textures, structures, or open space. Pick scenes that are wide and tell a story across the frame.')
             + para('You will shoot two different panoramas, each <strong>4 to 5 photos</strong>.')),
        card('SET UP YOUR CAMERA / 02 / 05', 'Camera and Tripod Setup',
             para('Get your gear ready before you shoot. Scroll through each setup step.')
             + '<div style="clear:both;"></div>'
             + vscroll(setup),
             ph('FLOAT-RIGHT IMAGE: Ricardo Gomez (21, muscular athletic build, short dark textured hair, gray bomber jacket with red trim) leaning to a DSLR camera mounted on a tripod, checking the settings, outdoors at the MRC campus.')),
        card('SHOOT THE PANORAMA / 03 / 05', 'Pan Slow and Overlap',
             para('Now capture your photos. Move across the scene in even, overlapping steps.')
             + para('<strong>Focus pro tip:</strong> if the camera will not lock focus, flip the <strong>AF / MF</strong> switch to <strong>MF</strong> (manual focus). That turns on the focus ring on the lens so you can twist it to set focus by hand. Switch it back to <strong>AF</strong> when you finish, for the next student.')
             + '<div style="clear:both;"></div>'
             + vscroll(shoot),
             floatimg(RAW + 'pano-camera-mf.png', 'Canon camera back with the AF / MF button circled')),
        card('ORGANIZE YOUR FILES / 04 / 05', 'Keep It Organized',
             para('In your <strong>OneDrive Photography</strong> folder, make a <strong>Panorama</strong> folder with a <strong>RAW Images</strong> subfolder inside it.')
             + para('Offload all your <strong>.CR3</strong> RAW files into the <strong>RAW Images</strong> folder. Keep every part of this project organized here from start to finish.')),
        card('TURN IT IN / 05 / 05', 'Screenshot Your RAW Folder',
             para('Open <strong>Finder</strong> and switch to <strong>Icon view</strong> so you can see the photo thumbnails.')
             + para('Open your <strong>RAW Images</strong> folder. Make sure the window shows the folder name <strong>RAW Images</strong> at the top and your image thumbnails inside. No contact sheet, just the folder.')
             + para('Press the <strong>F15</strong> key to take the screenshot. On our Macs, F15 saves the screenshot straight to your <strong>Desktop</strong> as a PNG.')
             + para('Find it on the Desktop and rename it:')
             + fname('FirstName LastInitial - Panorama (PNG)')
             + imgfull(RAW + 'pano-raw-folder-screenshot.png', 'Example screenshot of a RAW Images folder in Finder Icon view', 'Your screenshot should look like this')
             + para('Upload the PNG screenshot to Step 1 in Canvas to finish Part A.')),
    ],
)

# =========================================================================
# PAGE 3 — STEP 02 MERGE
# =========================================================================
merge = [
    tile('Merge 01', 'Keep Layout on Auto', 'In the Photomerge window, leave <strong>Layout</strong> set to <strong>Auto</strong>. It works best for most panoramas.'),
    tile('Merge 02', 'Browse and Select', 'Click <strong>Browse</strong>. Go to your <strong>RAW Images</strong> folder and select the 4 to 5 <strong>.CR3</strong> files for <strong>one</strong> panorama. Click OK.'),
    tile('Merge 03', 'Check the Boxes', 'Turn on <strong>Blend Images Together</strong>, <strong>Vignette Removal</strong>, and <strong>Geometric Distortion Correction</strong>.'),
    tile('Merge 04', 'Fill the Edges', 'Also check <strong>Content Aware Fill Transparent Areas</strong> to fill the empty edges for you. Then click <strong>OK</strong>.'),
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
             + para('You will run this once for each panorama, so you will do it twice.')),
        card('BUILD THE PANORAMA / 02 / 04', 'Choose and Blend',
             para('Set up the merge in the Photomerge window. Scroll through each step.')
             + '<div style="clear:both;"></div>'
             + vscroll(merge),
             ph('FLOAT-RIGHT IMAGE: Julian (21, lean, dark curly hair with a taper fade, red-and-black plaid flannel over a black tee, silver cross necklace) seen over the shoulder at an iMac in the MRC computer lab, a wide stitched panorama of the campus open on the Photoshop screen mid-merge, cool screen glow on his face and warm orange lab lighting.')),
        card('CLEAN IT UP / 03 / 04', 'Flatten, Crop, Adjust',
             para('Flatten the layers into one image: <strong>Layer &gt; Flatten Image</strong>.')
             + para('If you did not use Content Aware Fill, crop off the uneven transparent edges with the <strong>Crop tool</strong>.')
             + para('Adjust your photo with the <strong>Camera Raw Filter</strong> (<strong>Filter &gt; Camera Raw Filter</strong>) or adjustment layers. Fix the exposure, contrast, and color until it looks great.')
             + para('Now do this whole process again for your <strong>second</strong> panorama.')),
        card('SAVE AND SUBMIT / 04 / 04', 'Save Big, Submit Both',
             para('Save each panorama as a layered <strong>.PSD</strong> in your OneDrive Panorama folder so you keep your work.')
             + para('Then export each as a large <strong>JPG</strong>: <strong>File &gt; Save a Copy</strong>, choose JPG, full size. Name them:')
             + fname('FirstName LastInitial - Panorama 1.jpg &nbsp;and&nbsp; FirstName LastInitial - Panorama 2.jpg')
             + para('Submit <strong>both</strong> panorama JPGs to Step 2 in Canvas.')),
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
             para('A reflection helps you learn from your work. Download the reflection template below, answer all four questions in complete sentences, and turn it in.')
             + scrollrow(questions)),
        card('TURN IT IN / 02 / 02', 'Submit Your Reflection',
             para('Open the template, type your answers, and save it. Name your file:')
             + fname('FirstName LastInitial - Panorama Reflection.docx')
             + para('Upload your finished reflection to Step 3 in Canvas to complete the project.')
             + '<div style="margin-top:18px;">' + dlbutton(DOCX_URL, 'Download the Reflection Template') + '</div>'),
    ],
)

print('done')
