#!/usr/bin/env python3
"""Generate the MRC Digital Arts 1A "Magazine Cover" module (English).
Five Canvas pages on the locked Angular Gradient Framework (orange
#c95201), lead character Julian:

  1 overview               magcover-overview.html
  2 step01 plan            magcover-step01-plan.html
  3 step02 capture (RAW)   magcover-step02-capture.html
  4 step03 design (PS)     magcover-step03-design.html
  5 step04 reflection      magcover-step04-reflection.html

Students design a real-looking agriculture magazine cover (Successful
Farming, Progressive Farmer, or Farm Journal) featuring the MRC campus.
Project folder + logos are supplied by the teacher (button no-link for
now). Image slots are placeholders with hyper-real generation prompts.
"""
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'curriculum', 'mrc')
RAWBASE = 'https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/'
IMG = RAWBASE + 'assets/mrc/images/'

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

def ilink(href, label):
    return ('<a href="%s" style="color:#eda268;text-decoration:underline;"><strong>%s &rarr;</strong></a>'
            % (href, label))

def floatimg(src, alt):
    return ('<img src="%s" alt="%s" style="float:right;width:42%%;min-width:240px;margin:0 0 18px 26px;%s" />'
            % (src, alt, FRAME))

def imgfull(src, alt, caption):
    return ('<img src="%s" alt="%s" style="width:100%%;display:block;margin:6px 0 8px;%s" />'
            '<div style="font-size:9pt;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.55);'
            'text-align:center;margin-bottom:6px;font-family:Arial,sans-serif;"><strong>%s</strong></div>'
            % (src, alt, FRAME, caption))

def ph(desc):
    return ('<div style="background:linear-gradient(135deg,rgba(201,82,1,0.12) 0%,rgba(0,0,0,0.45) 100%);'
            'border:2px solid transparent;border-image:linear-gradient(135deg,#c95201 0%,rgba(201,82,1,0.08) 100%) 1;'
            'padding:26px 22px;text-align:center;float:right;width:42%;min-width:240px;margin:0 0 18px 26px;">'
            '<div style="font-size:10pt;letter-spacing:0.22em;text-transform:uppercase;color:#eda268;margin-bottom:10px;">'
            '<strong>Image Placeholder</strong></div>'
            '<div style="font-size:11.5pt;line-height:1.6;color:rgba(255,255,255,0.66);font-style:italic;">'
            + desc + '</div></div>')

def headerph(desc):
    return ('<div style="background:linear-gradient(135deg,rgba(201,82,1,0.12) 0%,rgba(0,0,0,0.45) 100%);'
            'border:2px solid transparent;border-image:linear-gradient(135deg,#c95201 0%,rgba(201,82,1,0.08) 100%) 1;'
            'padding:46px 30px;text-align:center;margin-bottom:24px;">'
            '<div style="font-size:10pt;letter-spacing:0.22em;text-transform:uppercase;color:#eda268;margin-bottom:10px;">'
            '<strong>Header Image Placeholder &bull; 16:6 Ultra-Wide</strong></div>'
            '<div style="font-size:12pt;line-height:1.6;color:rgba(255,255,255,0.66);font-style:italic;max-width:780px;margin:0 auto;">'
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
            'rgba(201,82,1,0.08) 100%%) 1;padding:20px 22px 24px;position:relative;overflow:hidden;margin:4px 0 14px;">'
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

def pendingbutton(label):
    # framework button, link to be added once the teacher supplies the project folder
    return ('<a href="#" style="background:rgba(255,255,255,0.92);color:#4a1e02;text-decoration:none;'
            'padding:7px 16px;display:inline-block;font-size:11pt;white-space:nowrap;border-top:2px solid #c95201;">'
            '<strong>%s</strong></a>' % label)

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
mags = [
    tile('Option 01', 'Successful Farming',
         'A big, clean masthead with one bold livestock or crop photo. Published at agriculture.com.<br />'
         + ilink('https://www.agriculture.com', 'See real covers')),
    tile('Option 02', 'Progressive Farmer',
         'A modern look from DTN, often shot from above or on location in the field.<br />'
         + ilink('https://www.dtnpf.com/agriculture/web/ag/magazine', 'See real covers')),
    tile('Option 03', 'Farm Journal',
         'Classic, friendly covers that often feature a real farmer up close.<br />'
         + ilink('https://www.farmjournal.com', 'See real covers')),
]
vocab = [
    tile('Term 01', 'Masthead', 'The magazine&rsquo;s name and logo at the top of the cover. It is the brand, and usually the biggest text.'),
    tile('Term 02', 'Cover Image', 'The one big photo that fills the cover and grabs your eye. It is also called the hero image.'),
    tile('Term 03', 'Cover Lines', 'The short, bold headlines that tease the stories inside. They are also called coverlines.'),
    tile('Term 04', 'Type Hierarchy', 'Using big, bold type for the main story and smaller type for the rest, so the eye knows where to look first.'),
    tile('Term 05', 'Bleed', 'When the photo runs all the way to the edge of the page with no white border. Covers almost always bleed.'),
    tile('Term 06', 'Photojournalism', 'Telling a true story with photos taken on location, in real moments, not posed in a studio.'),
]
great = [
    tile('Tip 01', 'One Strong Subject', 'Pick one clear subject for your hero photo. A cover with one bold focal point beats a busy one.'),
    tile('Tip 02', 'Leave Room for Text', 'Frame your photo with empty space at the top and one side so the masthead and cover lines have a home.'),
    tile('Tip 03', 'Shoot Vertical', 'Magazine covers are tall (portrait). Turn the camera vertical when you shoot your hero image.'),
    tile('Tip 04', 'Keep It Real', 'This is photojournalism. Real people, real places, and real moments make the strongest covers.'),
    tile('Tip 05', 'Match the Style', 'Study your magazine&rsquo;s real covers and match their fonts, colors, and mood.'),
]
mission = [
    tile('STEP 01', 'Plan', 'Pick your magazine and your story, then sketch your cover layout.'),
    tile('STEP 02', 'Capture', 'Shoot your hero photo on location, then turn in a screenshot of your RAW folder.'),
    tile('STEP 03', 'Design', 'Build the cover in Photoshop with the real masthead and your cover lines.'),
    tile('STEP 04', 'Reflect', 'Answer four questions about your cover and the choices you made.'),
]
page(
    'magcover-overview.html',
    'Overview | Magazine Cover | Digital Arts 1A | Mark Richardson Center',
    'Overview', [('magcover-step01-plan.html', 'Step 1 &#8594;')],
    'mrc-magcover-overview-canvas.html',
    'Digital Arts 1A &nbsp;&bull;&nbsp; Module', 'Magazine Cover',
    'Tell the MRC story in one cover.',
    [
        headerph('Ultra-wide 16:6 hyper-realistic, behind-the-scenes photo of a magazine cover shoot on the Mark Richardson Center campus at golden hour. Julian (21, lean, dark curly hair with a taper fade, red-and-black plaid flannel over a black tee) crouches with a Canon DSLR, photographing his subject: a confident young MRC agriculture student in a work shirt standing beside a tractor and a fenced livestock corral, crop rows in the mid-ground. Warm low sun, gentle lens flare, shallow depth of field. Editorial photojournalism mood like the cover of a real farming magazine (Successful Farming / Progressive Farmer / Farm Journal). Photoreal, sharp detail, natural skin tones.'),
        card('WHAT IS A MAGAZINE COVER / 01 / 06', 'One Image, One Story',
             para('A magazine cover is the front page that makes you want to pick it up. It uses <strong>one strong photo</strong> and a few <strong>bold words</strong> to sell the whole magazine in a single glance.')
             + para('Look at a real cover: a big name at the top (the <strong>masthead</strong>), one powerful photo behind it, and short headlines that tease the stories inside.')
             + para('For this project you will design a real-looking <strong>agriculture magazine cover</strong> that puts the Mark Richardson Center in the spotlight.')),
        card('PICK YOUR MAGAZINE / 02 / 06', 'Choose One of Three',
             para('You will design your cover in the style of one real farming magazine. Pick <strong>one</strong> of these three. Click to study their real covers for ideas.')
             + scrollrow(mags)
             + para('You will get the real magazine logo from your <strong>project folder</strong> to make your cover look authentic.')),
        card('THE BRIEF / 03 / 06', 'Your Assignment from Admin',
             para('Here is your creative brief from the <strong>MRC administration</strong>:')
             + notecard('FROM MRC ADMIN', 'Show the Heart of Our Campus', 'We want a cover that makes people stop and look. Show what makes the Mark Richardson Center special: our people, our work, and our future.')
             + para('<strong>What you could highlight:</strong> the agriculture program, livestock and crops, the welding or automotive shops, new equipment, a campus event, or how the MRC grows and builds.')
             + para('<strong>Who you could highlight:</strong> a standout student, an instructor, a team, or someone hard at work.')
             + para('You have lots of <strong>creative freedom</strong>. Tell a true story. A studio is set up if you need it, but shots taken <strong>on location</strong> usually tell a stronger story.')),
        card('WORDS TO KNOW / 04 / 06', 'Magazine Vocabulary',
             para('Learn these six terms. You will use them all the way through the project.')
             + scrollrow(vocab)),
        card('WHAT MAKES A GREAT COVER / 05 / 06', 'Cover Design Tips',
             para('Keep these in mind from your first shot to your final design.')
             + scrollrow(great)),
        card('YOUR MISSION / 06 / 06', 'What You Will Do',
             para('You will work like a real photo editor in four steps: plan, capture, design, and reflect.')
             + scrollrow(mission)
             + '<div style="margin-top:18px;">' + pendingbutton('Download the Project Folder') + '</div>'),
    ],
)

# =========================================================================
# PAGE 2 — STEP 01 PLAN
# =========================================================================
page(
    'magcover-step01-plan.html',
    'Step 1: Plan | Magazine Cover | Digital Arts 1A | Mark Richardson Center',
    'Step 1',
    [('magcover-overview.html', '&#8592; Overview'), ('magcover-step02-capture.html', 'Step 2 &#8594;')],
    'mrc-magcover-step01-plan-canvas.html',
    'Magazine Cover &nbsp;&bull;&nbsp; Step 1', 'Plan Your Cover',
    'Pick your story and sketch the layout.',
    [
        card('PICK YOUR STORY / 01 / 03', 'Choose Your Subject',
             para('Read the brief again and choose <strong>one story</strong> to tell on your cover. Pick a real subject you can photograph: a person, an animal, a machine, or a place on campus.')
             + para('Choose your <strong>angle</strong> too. What is the headline? &ldquo;Future Farmers,&rdquo; &ldquo;Built at the MRC,&rdquo; &ldquo;Meet the Welder.&rdquo; Your photo and your words should tell the same story.')),
        card('SKETCH YOUR LAYOUT / 02 / 03', 'Plan the Cover',
             para('On paper, sketch a quick <strong>thumbnail</strong> of your cover. Plan where each piece goes:')
             + para('Put the <strong>masthead</strong> box at the top. Block out where your <strong>hero photo</strong> will sit. Mark where 3 or 4 <strong>cover lines</strong> will go down one side.')
             + para('Leave room for the text. Do not plan to cover your subject&rsquo;s face with the masthead or headlines.'),
             ph('Hyper-realistic photo of Julian (21, lean, dark curly hair with a taper fade, red-and-black plaid flannel over a black tee) at a desk in the MRC studio, sketching a magazine cover layout in a sketchbook: a rough thumbnail showing a masthead box at the top, a large hero-photo area, and a few cover-line bars down one side. Pencil in hand, real farming magazine covers pinned on the wall behind him. Warm light, photoreal, three-quarter view.')),
        card('GET IT CHECKED / 03 / 03', 'Bring It to Mr. Silva',
             para('Before you shoot, show Mr. Silva your <strong>subject idea</strong> and your <strong>layout sketch</strong>. This is a quick checkpoint, no upload needed.')
             + notecard('CHECKPOINT', 'Plan First, Shoot Second', 'A clear plan makes a stronger photo. Get the green light, then grab a camera for Step 2.')),
    ],
)

# =========================================================================
# PAGE 3 — STEP 02 CAPTURE
# =========================================================================
heroshot = [
    tile('Shot 01', 'Shoot Vertical', 'Turn the camera so the photo is tall (portrait). Covers are tall, so your hero photo should be too.'),
    tile('Shot 02', 'Fill the Frame', 'Get close and make your subject big and clear. A bold subject makes a bold cover.'),
    tile('Shot 03', 'Leave Text Room', 'Keep the top and one side a little open and simple, so the masthead and cover lines will fit later.'),
    tile('Shot 04', 'Find Good Light', 'Soft daylight or golden hour looks best. Keep the sun out of the lens and off harsh shadows.'),
    tile('Shot 05', 'Shoot a Lot', 'Take many photos and a few angles. You only need one great shot, but options give you choices.'),
]
page(
    'magcover-step02-capture.html',
    'Step 2: Capture | Magazine Cover | Digital Arts 1A | Mark Richardson Center',
    'Step 2',
    [('magcover-step01-plan.html', '&#8592; Step 1'), ('magcover-step03-design.html', 'Step 3 &#8594;')],
    'mrc-magcover-step02-capture-canvas.html',
    'Magazine Cover &nbsp;&bull;&nbsp; Step 2', 'Shoot Your Cover Photo',
    'Capture your hero image on location.',
    [
        card('SHOOT ON LOCATION / 01 / 04', 'Photojournalism Style',
             para('Go where the story is: the barn, the field, the shop, the field house. Shoot <strong>real moments</strong>, not stiff poses. This is <strong>photojournalism</strong>.')
             + para('A studio is set up if your story needs it, but on-location photos usually feel more real and tell a stronger story.'),
             ph('Hyper-realistic on-location photojournalism photo of Julian (21, lean, dark curly hair with a taper fade, red-and-black plaid flannel over a black tee) holding a Canon DSLR vertically (portrait orientation), photographing his cover subject: an MRC agriculture student kneeling beside livestock in a corral on the MRC campus at golden hour. Julian is focused and framing the shot, leaving open space at the top for a masthead. Documentary feel, warm light, photoreal, three-quarter rear view.')),
        card('MAKE A STRONG HERO SHOT / 02 / 04', 'Frame the Cover Image',
             para('Your hero image carries the whole cover. Scroll through each pointer as you shoot.')
             + scrollrow(heroshot)),
        card('ORGANIZE YOUR FILES / 03 / 04', 'Keep It Organized',
             para('Use the <strong>project folder</strong> you downloaded from the overview. If you have not yet, move it into your <strong>OneDrive Digital Arts</strong> folder.')
             + para('Offload all your <strong>RAW</strong> files into the <strong>RAW Images</strong> subfolder inside it. Keep every part of this project organized here.')),
        card('TURN IT IN / 04 / 04', 'Screenshot Your RAW Folder',
             para('Open <strong>Finder</strong> and switch to <strong>Icon view</strong> so you can see the photo thumbnails.')
             + para('Open your <strong>RAW Images</strong> folder so the window shows the folder name and your thumbnails inside. Press the <strong>F15</strong> key to take the screenshot. On our Macs, F15 saves it straight to your <strong>Desktop</strong> as a PNG.')
             + para('Find it on the Desktop and rename it:')
             + fname('FirstName LastInitial - Magazine Cover (PNG)')
             + imgfull(IMG + 'pano-raw-folder-screenshot.png', 'Example screenshot of a RAW Images folder in Finder Icon view', 'Your screenshot should look like this')
             + para('Upload the PNG screenshot to Step 2 in Canvas.')),
    ],
)

# =========================================================================
# PAGE 4 — STEP 03 DESIGN
# =========================================================================
coverlines = [
    tile('Line 01', 'Write a Main Headline', 'One big, bold cover line is the star. Make it short and exciting, like &ldquo;Built at the MRC&rdquo; or &ldquo;Future Farmers.&rdquo;'),
    tile('Line 02', 'Add Teasers', 'Add 2 or 3 smaller cover lines that hint at other stories. These are your teasers.'),
    tile('Line 03', 'Use Type Hierarchy', 'Make the main headline the biggest. Make the teasers smaller. Size shows the reader what matters most.'),
    tile('Line 04', 'Keep Text Off the Face', 'Place your words in the open space you left when you shot. Never cover your subject&rsquo;s face or eyes.'),
    tile('Line 05', 'Match the Magazine', 'Use fonts and colors close to your real magazine&rsquo;s style so your cover looks authentic.'),
]
page(
    'magcover-step03-design.html',
    'Step 3: Design | Magazine Cover | Digital Arts 1A | Mark Richardson Center',
    'Step 3',
    [('magcover-step02-capture.html', '&#8592; Step 2'), ('magcover-step04-reflection.html', 'Step 4 &#8594;')],
    'mrc-magcover-step03-design-canvas.html',
    'Magazine Cover &nbsp;&bull;&nbsp; Step 3', 'Build Your Cover',
    'Design it like the real thing.',
    [
        card('SET UP YOUR COVER / 01 / 04', 'Start a New File',
             para('Open Photoshop. Go to <strong>File &gt; New</strong> and make a tall (portrait) magazine page, about <strong>8.5 by 11 inches</strong>, RGB color, 300 ppi.')
             + para('Open your best hero photo through <strong>Camera Raw</strong>, place it on your page, and let it <strong>bleed</strong> all the way to the edges with no white border. Save your work as a <strong>.PSD</strong> in your project folder.'),
             ph('Hyper-realistic over-the-shoulder photo of Julian (21, lean, dark curly hair with a taper fade, red-and-black plaid flannel over a black tee) at an iMac in the MRC computer lab, designing a farming magazine cover in Photoshop: a bold vertical hero photo fills the screen with a large masthead at the top and stacked cover lines down one side, just like a real agriculture magazine. Cool screen glow on his face, warm orange lab lighting, photoreal.')),
        card('ADD THE MASTHEAD / 02 / 04', 'Place the Logo',
             para('Open the magazine <strong>logo</strong> from your project folder and place it at the <strong>top</strong> of your cover.')
             + para('Size it big and bold, like the real magazine. The masthead is the brand, so it should be one of the first things you see.')),
        card('WRITE YOUR COVER LINES / 03 / 04', 'Add Your Headlines',
             para('Use the <strong>Type tool</strong> to add your cover lines. Scroll through each pointer.')
             + scrollrow(coverlines)),
        card('SAVE AND SUBMIT / 04 / 04', 'Save as JPG and Submit',
             para('When your cover is done, flatten it with <strong>Layer &gt; Flatten Image</strong>. Keep a PSD only if you want one.')
             + para('Turn in a <strong>JPG</strong>, not a PSD. Use <strong>File &gt; Save a Copy</strong>, choose <strong>JPG</strong>, full size. Name it:')
             + fname('FirstName LastInitial - Magazine Cover.jpg')
             + para('Submit your finished cover JPG to Step 3 in Canvas.')),
    ],
)

# =========================================================================
# PAGE 5 — STEP 04 REFLECTION
# =========================================================================
questions = [
    tile('Question 01', 'Your Magazine', 'Which magazine did you design for, and why did it fit your story?'),
    tile('Question 02', 'Your Story', 'What story does your cover tell? Who or what did you highlight, and why?'),
    tile('Question 03', 'The Hard Part', 'What was harder for you, shooting or designing? How did you solve the problem?'),
    tile('Question 04', 'The Big Picture', 'If a real magazine printed your cover, what would people learn about the MRC?'),
]
page(
    'magcover-step04-reflection.html',
    'Step 4: Reflection | Magazine Cover | Digital Arts 1A | Mark Richardson Center',
    'Step 4',
    [('magcover-step03-design.html', '&#8592; Step 3')],
    'mrc-magcover-step04-reflection-canvas.html',
    'Magazine Cover &nbsp;&bull;&nbsp; Step 4', 'Reflection',
    'Look back at your cover.',
    [
        card('ANSWER FOUR QUESTIONS / 01 / 02', 'Reflect on Your Work',
             para('A reflection helps you learn from your work. Open the <strong>reflection document</strong> in your project folder and answer all four questions in complete sentences.')
             + scrollrow(questions)),
        card('TURN IT IN / 02 / 02', 'Submit Your Reflection',
             para('The reflection document is inside your <strong>project folder</strong>. Type your answers, save the document, and name it:')
             + fname('FirstName LastInitial - Magazine Cover Reflection.docx')
             + para('Upload your finished reflection to Step 4 in Canvas to complete the project.'),
             ph('Hyper-realistic photo of Julian (21, lean, dark curly hair with a taper fade, red-and-black plaid flannel over a black tee) sitting back at the MRC lab, holding a printed proof of his finished farming magazine cover and looking at it thoughtfully, his iMac showing the same cover behind him. Warm reflective mood, soft orange lab lighting, photoreal, over-the-shoulder view.')),
    ],
)

print('done')
