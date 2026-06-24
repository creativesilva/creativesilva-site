#!/usr/bin/env python3
"""Generate the MRC Digital Arts 1A "Camera Modes: TV & AV" module (English),
locked Angular Gradient Framework (orange #c95201), lead Patricia Guererro.
Accurate to the Canon EOS R50 (Tv = Shutter Priority, Av = Aperture
Priority; ISO Auto; RF-S 18-45 kit, RF 50mm f/1.8, RF-S 55-210 telephoto).

  1 overview              tvav-overview.html
  2 step01 capture        tvav-step01-capture.html
  3 step02 cull & edit    tvav-step02-edit.html
  4 step03 reflection     tvav-step03-reflection.html

Project-folder and reflection buttons are placeholders with no link yet.
"""
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'curriculum', 'mrc')
RAWBASE = 'https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/'
ZIP_URL = RAWBASE + 'assets/mrc/handouts/TV-AV.zip'
DOCX_URL = RAWBASE + 'assets/mrc/study-guides/MRC_TV_AV_Reflection.docx'
IMG = RAWBASE + 'assets/mrc/images/'

FRAME ='border:2px solid transparent;border-image:linear-gradient(135deg,#c95201 0%,rgba(201,82,1,0.08) 100%) 1;'
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

def ph(desc):
    return ('<div style="background:linear-gradient(135deg,rgba(201,82,1,0.12) 0%,rgba(0,0,0,0.45) 100%);'
            'border:2px solid transparent;border-image:linear-gradient(135deg,#c95201 0%,rgba(201,82,1,0.08) 100%) 1;'
            'padding:26px 22px;text-align:center;float:right;width:42%;min-width:240px;margin:0 0 18px 26px;">'
            '<div style="font-size:10pt;letter-spacing:0.22em;text-transform:uppercase;color:#eda268;margin-bottom:10px;">'
            '<strong>Image Placeholder</strong></div>'
            '<div style="font-size:11.5pt;line-height:1.6;color:rgba(255,255,255,0.66);font-style:italic;">'
            + desc + '</div></div>')

def floatimg(src, alt):
    return ('<img src="%s" alt="%s" style="float:right;width:42%%;min-width:240px;margin:0 0 18px 26px;%s" />'
            % (src, alt, FRAME))

def headerimg(src, alt):
    return ('<img src="%s" alt="%s" style="width:100%%;display:block;margin-bottom:24px;%s" />'
            % (src, alt, FRAME))

def headerph(desc):
    return ('<div style="background:linear-gradient(135deg,rgba(201,82,1,0.12) 0%,rgba(0,0,0,0.45) 100%);'
            'border:2px solid transparent;border-image:linear-gradient(135deg,#c95201 0%,rgba(201,82,1,0.08) 100%) 1;'
            'padding:46px 30px;text-align:center;margin-bottom:24px;">'
            '<div style="font-size:10pt;letter-spacing:0.22em;text-transform:uppercase;color:#eda268;margin-bottom:10px;">'
            '<strong>Header Image Placeholder &bull; 16:6 Ultra-Wide</strong></div>'
            '<div style="font-size:12pt;line-height:1.6;color:rgba(255,255,255,0.66);font-style:italic;max-width:760px;margin:0 auto;">'
            + desc + '</div></div>')

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

def vscroll(tiles, hint='&#8597; scroll for more &#8597;'):
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
triangle = [
    tile('Part 01', 'Aperture', 'How wide the lens opens to let light in. It also controls how much of the photo is in focus.'),
    tile('Part 02', 'Shutter Speed', 'How long the lens stays open. It controls whether motion looks frozen or blurry.'),
    tile('Part 03', 'ISO', 'How sensitive the camera is to light. Keep this on <strong>Auto</strong> and let the camera handle it.'),
]
mission = [
    tile('STEP 01', 'Capture', 'Shoot eight photos: four in AV and four in TV. Turn in a screenshot of your RAW folder.'),
    tile('STEP 02', 'Cull &amp; Edit', 'Pick and polish your best eight photos, then submit them as JPGs.'),
    tile('STEP 03', 'Reflect', 'Answer a few short questions about what you learned.'),
]
page(
    'tvav-overview.html',
    'Overview | Camera Modes TV &amp; AV | Digital Arts 1A | Mark Richardson Center',
    'Overview', [('tvav-step01-capture.html', 'Step 1 &#8594;')],
    'mrc-tvav-overview-canvas.html',
    'Digital Arts 1A &nbsp;&bull;&nbsp; Module', 'Camera Modes: TV &amp; AV',
    'Take control of motion and focus.',
    [
        headerimg(IMG + 'tvav-header.png', 'Patricia Guererro framing a shot with a Canon camera in front of the MRC campus at golden hour'),
        card('TWO CAMERA MODES / 01 / 05', 'Take the Wheel',
             para('Until now, you shot in <strong>Auto</strong> and the camera made every choice for you. Now you take the wheel with two new modes on your <strong>Canon EOS R50</strong>: <strong>TV</strong> and <strong>AV</strong>.')
             + para('These are <strong>semi-manual</strong> modes. You make one important choice, and the camera figures out the rest. They are the easiest way to start controlling how your photos look.')),
        card('THE EXPOSURE TRIANGLE / 02 / 05', 'Three Things Make a Photo Bright',
             para('Every photo gets its brightness from three things working together. Photographers call this the <strong>exposure triangle</strong>.')
             + scrollrow(triangle)
             + para('In TV and AV you control <strong>one</strong> of these, and the camera balances the other two. With ISO on <strong>Auto</strong>, you only think about one setting at a time.')),
        card('AV MODE / 03 / 05', 'AV: You Control Focus',
             para('<strong>AV</strong> means <strong>Aperture Priority</strong>. You pick the <strong>aperture</strong> (the f-number), and the camera picks the shutter speed for you.')
             + para('Aperture controls <strong>depth of field</strong>, how much of your photo is sharp. A <strong>low f-number</strong> like <strong>f/1.8</strong> blurs the background, perfect for a portrait. A <strong>high f-number</strong> like <strong>f/11</strong> keeps everything sharp, perfect for a wide scene.')
             + para('Use AV when <strong>focus</strong> matters most: portraits, close-up details, or scenes with lots of depth.')),
        card('TV MODE / 04 / 05', 'TV: You Control Motion',
             para('<strong>TV</strong> means <strong>Shutter Priority</strong>. You pick the <strong>shutter speed</strong>, and the camera picks the aperture for you.')
             + para('Shutter speed controls <strong>motion</strong>. A <strong>fast</strong> shutter like <strong>1/500</strong> freezes action razor sharp. A <strong>slow</strong> shutter like <strong>1/30</strong> lets moving things blur into streaks.')
             + para('Use TV when <strong>movement</strong> matters most: sports, running, bikes, flowing water, or anything in motion.')),
        card('YOUR MISSION / 05 / 05', 'What You Will Do',
             para('You will shoot, edit, and reflect, just like a real photographer. Three steps, three turn-ins.')
             + scrollrow(mission)
             + notecard('START HERE', 'Download Your Project Folder', 'Download the project folder below and move it into your <strong>OneDrive Digital Arts</strong> folder. Inside is a <strong>RAW Images</strong> folder for your photos and your reflection sheet.')
             + '<div style="margin-top:18px;">' + dlbutton(ZIP_URL, 'Download the Project Folder') + '</div>'),
    ],
)

# =========================================================================
# PAGE 2 — STEP 01 CAPTURE
# =========================================================================
setup = [
    tile('Setup 01', 'Shoot RAW', 'Set image quality to <strong>RAW</strong> so you have room to edit later. On the R50 these are <strong>.CR3</strong> files.'),
    tile('Setup 02', 'ISO on Auto', 'Set <strong>ISO</strong> to <strong>Auto</strong> in the menu and leave it there. The camera handles brightness for you.'),
    tile('Setup 03', 'Pick Your Lens', 'For AV depth-of-field shots use the <strong>50mm</strong> lens. For TV motion shots the <strong>18-45mm kit</strong> lens is easiest, but the 50mm or the <strong>55-210mm</strong> telephoto work too.'),
    tile('Setup 04', 'Turn the Dial', 'Turn the mode dial to <strong>AV</strong> or <strong>TV</strong>. The screen shows the setting you control. Spin the top dial to change its number.'),
]
av_shots = [
    tile('AV: Shallow', 'Blurry Background (take 2)', 'Use a <strong>low f-number</strong> (f/1.8 to f/4). Get close to your subject so the background melts into a soft blur. Try a portrait or a close-up detail.'),
    tile('AV: Deep', 'All in Focus (take 2)', 'Use a <strong>high f-number</strong> (f/11 or more). Find a scene with depth and layers so the front and the back are both sharp.'),
]
tv_shots = [
    tile('TV: Freeze', 'Freeze the Action (take 2)', 'Use a <strong>fast shutter</strong> (1/500 or faster). Catch something quick: a jump, a run, a kick. The motion looks frozen and sharp.'),
    tile('TV: Blur', 'Blur the Motion (take 2)', 'Use a <strong>slow shutter</strong> (1/30 or slower). Hold steady and let a moving subject streak: a walking student, a bike, a waving flag.'),
]
page(
    'tvav-step01-capture.html',
    'Step 1: Capture | Camera Modes TV &amp; AV | Digital Arts 1A | Mark Richardson Center',
    'Step 1',
    [('tvav-overview.html', '&#8592; Overview'), ('tvav-step02-edit.html', 'Step 2 &#8594;')],
    'mrc-tvav-step01-capture-canvas.html',
    'Camera Modes &nbsp;&bull;&nbsp; Step 1', 'Capture Eight Photos',
    'Four in AV, four in TV.',
    [
        card('YOUR EIGHT SHOTS / 01 / 05', 'What to Capture',
             para('You and your partner will capture <strong>eight photos</strong> around the MRC campus: <strong>four in AV mode</strong> and <strong>four in TV mode</strong>.')
             + para('Keep your <strong>ISO on Auto</strong> the whole time. That lets the camera handle brightness while you focus on your one setting.'),
             floatimg(IMG + 'tvav-capture-float.png', 'Patricia Guererro photographing a jumping subject to capture motion at the MRC campus')),
        card('SET UP THE CAMERA / 02 / 05', 'Before You Shoot',
             para('Get the camera ready before each set of shots. Scroll through each setting.')
             + '<div style="clear:both;"></div>'
             + vscroll(setup)),
        card('AV SHOTS / 03 / 05', 'Control Your Focus',
             para('Put on the <strong>50mm</strong> lens and turn the dial to <strong>AV</strong>. Spin the top dial to change the f-number. Take <strong>four AV photos</strong>: two with a blurry background and two with everything sharp.')
             + scrollrow(av_shots)),
        card('TV SHOTS / 04 / 05', 'Control the Motion',
             para('Turn the dial to <strong>TV</strong>. The <strong>18-45mm kit</strong> lens is easiest here, but the 50mm or the <strong>55-210mm</strong> telephoto work too. Take <strong>four TV photos</strong>: two that freeze motion and two that blur it.')
             + scrollrow(tv_shots)),
        card('TURN IT IN / 05 / 05', 'Screenshot Your RAW Folder',
             para('Use the <strong>project folder</strong> you downloaded from the overview, inside your <strong>OneDrive Digital Arts</strong> folder. Offload all your <strong>.CR3</strong> files into the <strong>RAW Images</strong> subfolder.')
             + para('Open the <strong>RAW Images</strong> folder in Finder <strong>Icon view</strong> so the thumbnails show. Press the <strong>F15</strong> key to take a screenshot, it saves to your <strong>Desktop</strong> as a PNG. Rename it:')
             + fname('FirstName LastInitial - TV and AV (PNG)')
             + para('Upload the PNG screenshot to Step 1 in Canvas.')),
    ],
)

# =========================================================================
# PAGE 3 — STEP 02 CULL & EDIT
# =========================================================================
page(
    'tvav-step02-edit.html',
    'Step 2: Cull and Edit | Camera Modes TV &amp; AV | Digital Arts 1A | Mark Richardson Center',
    'Step 2',
    [('tvav-step01-capture.html', '&#8592; Step 1'), ('tvav-step03-reflection.html', 'Step 3 &#8594;')],
    'mrc-tvav-step02-edit-canvas.html',
    'Camera Modes &nbsp;&bull;&nbsp; Step 2', 'Cull and Edit',
    'Pick and polish your best eight.',
    [
        card('CULL YOUR BEST / 01 / 03', 'Pick the Best Eight',
             para('Look through everything you shot. Pick your <strong>best eight</strong>: two shallow and two deep from <strong>AV</strong>, and two freeze and two blur from <strong>TV</strong>.')
             + para('Choosing your strongest shots and dropping the rest is called <strong>culling</strong>. Keep the photos that show each effect the clearest.'),
             floatimg(IMG + 'tvav-edit-float.jpg', 'Patricia Guererro editing her photos in Adobe Camera Raw at an iMac in the MRC computer lab')),
        card('EDIT YOUR PHOTOS / 02 / 03', 'Make Them Pop',
             para('Open your eight photos in <strong>Photoshop</strong> or <strong>Adobe Camera Raw</strong>. Because they are RAW files, you have lots of room to fix them.')
             + para('Adjust the <strong>exposure, contrast, and color</strong>, and crop for a stronger frame. Keep it looking natural and real, do not overdo it.')),
        card('SAVE AND SUBMIT / 03 / 03', 'Submit Eight JPGs',
             para('Save each photo as a <strong>JPG</strong>: <strong>File &gt; Save a Copy</strong>, choose JPG, full size. Name them so your AV and TV shots are clear, like:')
             + fname('FirstName LastInitial - AV Shallow 1.jpg')
             + para('Submit all <strong>eight</strong> JPGs to Step 2 in Canvas: four AV and four TV.')),
    ],
)

# =========================================================================
# PAGE 4 — STEP 03 REFLECTION
# =========================================================================
questions = [
    tile('Question 01', 'TV or AV?', 'Which mode did you like better, TV or AV, and why?'),
    tile('Question 02', 'Hardest Shot', 'Which photo was the hardest to get? What did you change to make it work?'),
    tile('Question 03', 'Your Best', 'Pick your favorite photo. What mode and setting did you use, and why did it work?'),
    tile('Question 04', 'In Real Life', 'Where could you use TV or AV mode in real life? What would you shoot?'),
]
page(
    'tvav-step03-reflection.html',
    'Step 3: Reflection | Camera Modes TV &amp; AV | Digital Arts 1A | Mark Richardson Center',
    'Step 3',
    [('tvav-step02-edit.html', '&#8592; Step 2')],
    'mrc-tvav-step03-reflection-canvas.html',
    'Camera Modes &nbsp;&bull;&nbsp; Step 3', 'Reflection',
    'Look back at your shots.',
    [
        card('ANSWER FOUR QUESTIONS / 01 / 02', 'Reflect on Your Work',
             para('A reflection helps you learn from your work. Open the <strong>reflection document</strong> in your project folder and answer all four questions in complete sentences.')
             + scrollrow(questions),
             floatimg(IMG + 'tvav-reflection-float.png', 'Patricia Guererro reviewing her edited photos at an iMac in the MRC computer lab')),
        card('TURN IT IN / 02 / 02', 'Submit Your Reflection',
             para('The reflection document is already inside your <strong>project folder</strong> (the one you downloaded at the start). Type your answers, save the document, and name it:')
             + fname('FirstName LastInitial - TV and AV Reflection.docx')
             + para('Upload your finished reflection to Step 3 in Canvas to complete the project.')),
    ],
)

print('done')
