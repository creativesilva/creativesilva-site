#!/usr/bin/env python3
"""Generate the MRC Digital Arts 1A "Logo Redesign" module (English only).
Four Canvas pages built entirely from the locked Angular Gradient
Framework (orange #c95201). Structure, wedges, chips, buttons, and
numbering match the Pictographs module exactly. Only the copy changes.

Pages:
  1 overview              logo-redesign-overview.html
  2 step01 thumbnails     logo-redesign-step01-thumbnails.html
  3 step02 final sketch   logo-redesign-step02-final-sketch.html
  4 step03 digital        logo-redesign-step03-digital.html
"""
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'curriculum', 'mrc')

ACCENT = '#c95201'
RAW = 'https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/mrc/images/'
FRAME = 'border:2px solid transparent;border-image:linear-gradient(135deg,#c95201 0%,rgba(201,82,1,0.08) 100%) 1;'
CARD_BG = 'background:linear-gradient(180deg,rgba(201,82,1,0.10) 0%,rgba(201,82,1,0.03) 100%);'
WEDGE = 'background:linear-gradient(135deg,rgba(201,82,1,0.20) 0%,rgba(201,82,1,0.20) 8%,rgba(0,0,0,0.40) 8%,rgba(0,0,0,0.40) 100%);'

# ---- framework helpers (verbatim markup) ----

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
    """Image placeholder, float right (framework section 8.5)."""
    return ('<div style="background:linear-gradient(135deg,rgba(201,82,1,0.12) 0%,rgba(0,0,0,0.45) 100%);'
            'border:2px solid transparent;border-image:linear-gradient(135deg,#c95201 0%,rgba(201,82,1,0.08) 100%) 1;'
            'padding:26px 22px;text-align:center;float:right;width:42%;min-width:240px;margin:0 0 18px 26px;">'
            '<div style="font-size:10pt;letter-spacing:0.22em;text-transform:uppercase;color:#eda268;margin-bottom:10px;">'
            '<strong>Image Placeholder</strong></div>'
            '<div style="font-size:11.5pt;line-height:1.6;color:rgba(255,255,255,0.66);font-style:italic;">'
            + desc + '</div></div>')

def card(label, title, body, floatel=''):
    return ('<div style="%s%spadding:30px;margin-bottom:24px;position:relative;overflow:hidden;">'
            '<div style="height:4px;background:#c95201;margin:-30px -30px 24px -30px;"></div>'
            '%s%s%s%s</div>' % (CARD_BG, FRAME, chip(label), tb(title), floatel, body))

def tile(eyebrow, title, body):
    """Inner wedge tile (used in scroll rows and pointer lists)."""
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
    """Full-width wedge tile used as a standalone callout (checkpoint/turn-in)."""
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

def vscroll(tiles, hint='&#8597; scroll for more pointers &#8597;'):
    inner = ''.join('<div style="margin-bottom:12px;">%s</div>' % t for t in tiles)
    return ('<div style="max-height:560px;overflow-y:auto;padding-right:8px;-webkit-overflow-scrolling:touch;">%s</div>'
            '<div style="text-align:center;font-size:8pt;color:rgba(201,82,1,0.65);letter-spacing:0.22em;'
            'text-transform:uppercase;margin-top:14px;font-family:Arial,sans-serif;"><strong>%s</strong></div>'
            % (inner, hint))

def fname(text):
    """Highlighted filename line, matching the picto step3 treatment."""
    return ('<div style="font-size:14pt;color:#eda268;margin-bottom:14px;font-family:Arial,sans-serif;">'
            '<strong>%s</strong></div>' % text)

# ---- page shell ----

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
        <a href="/curriculum.html">Curriculum Catalog</a>
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
    path = os.path.join(OUT, filename)
    open(path, 'w').write(html)
    bal = html.count('<div') == html.count('</div>')
    print('  %s  divs=%s  em=%d' % (filename, 'OK' if bal else 'IMBALANCE',
                                    html.count('—') + html.count('&mdash;')))

# =========================================================================
# PAGE 1 — OVERVIEW
# =========================================================================
principles = [
    tile('Principle 01', 'Simple', 'Few shapes, few colors. If you can draw it from memory, it is working.'),
    tile('Principle 02', 'Memorable', 'One strong idea that sticks in your head after a single look.'),
    tile('Principle 03', 'Scalable', 'Looks sharp tiny on a phone or huge on a billboard, on screen or on a shirt.'),
    tile('Principle 04', 'Timeless', 'Avoids trendy tricks that will look old and dated in a year.'),
    tile('Principle 05', 'One Color', 'A great logo still reads clearly in plain black or plain white.'),
]
def ilink(href, label):
    return ('<a href="%s" target="_blank" rel="noopener" style="color:#eda268;text-decoration:underline;"><strong>%s</strong></a>'
            % (href, label))

vocab_logo = [
    tile('Vocabulary', 'Logo', 'A simple, memorable mark that stands for a whole brand: its products, style, and promise.'),
    tile('Vocabulary', 'Rebrand', 'Updating a logo to feel modern while keeping what makes it recognizable.'),
    tile('Vocabulary', 'Simplify', 'Removing detail so a logo works tiny, huge, and in one color. The core of this project.'),
    tile('Vocabulary', 'Negative Space', 'The empty area around and inside a logo. Good designers shape it on purpose.'),
    tile('Vocabulary', 'Typography', 'The style and spacing of the lettering in a logo.'),
    tile('Vocabulary', 'Wordmark', 'A logo made from the brand&rsquo;s name in a custom typeface, like Coca-Cola.'),
]

res_logo = [
    tile('Resource', 'Adobe: Design a Logo', 'Logo design fundamentals from Adobe: shapes, type, and color. ' + ilink('https://www.adobe.com/learn/illustrator/web/logo-design', 'Open &rarr;')),
    tile('Resource', 'Beginner Logo Tutorial', 'A free step-by-step walkthrough of designing a logo from scratch. ' + ilink('https://logosbynick.com/beginner-logo-tutorial-for-adobe-illustrator/', 'Open &rarr;')),
]

mission = [
    tile('STEP 01', 'Thumbnails', 'Sketch three quick redesign ideas for a famous logo, then bring them to Mr. Silva for a check.'),
    tile('STEP 02', 'Final Sketch', 'Use the feedback to draw one polished final sketch, photograph your work, and turn it in.'),
    tile('STEP 03', 'Digital Redesign', 'Rebuild your new logo in Photoshop at 2000 x 2000 pixels and turn in the final JPG.'),
]
page(
    'logo-redesign-overview.html',
    'Overview | Logo Redesign | Digital Arts 1A | Mark Richardson Center',
    'Overview',
    [('logo-redesign-step01-thumbnails.html', 'Step 1 &#8594;')],
    'mrc-logo-redesign-overview-canvas.html',
    'Digital Arts 1A &nbsp;&bull;&nbsp; Module', 'Logo Redesign',
    'The best logos say the most with the least.',
    [
        card('WHY LOGOS MATTER / 01 / 06', 'A Logo Is a Brand&rsquo;s Face',
             para('A logo is the face of a brand. It is one small mark that stands for a whole company: its products, its style, and its promise to you.')
             + para('You already recognize hundreds of logos in a split second, even with no name attached. A checkmark. A bitten apple. A pair of golden arches. That fast recognition is the whole job of a logo.')
             + para('The best logos are simple enough to draw from memory. That is not an accident. It is the result of careful design.'),
             floatimg(RAW + 'logo-overview-float.jpg', 'The Starbucks logo evolution from 1971 to today, getting simpler at each step')),
        card('SIMPLE WINS / 02 / 06', 'The More Successful, the Simpler',
             para('Look at how the Starbucks logo changed over time. The first version in 1971 had a detailed siren, a brown color, and the words &ldquo;Starbucks Coffee&rdquo; wrapped around a ring. Each redesign removed something: the outer text, then the ring, until only a clean green siren was left.')
             + para('This happens to almost every big brand. As a company grows, its logo gets <strong>simpler, not fancier</strong>. Nike dropped its name and kept the swoosh. Apple dropped the rainbow stripes and the word &ldquo;Apple.&rdquo; Shell, McDonald&rsquo;s, and Mastercard all did the same.')
             + para('Why? A simple logo works everywhere: tiny on a phone screen, huge on a billboard, stamped on a cup, or stitched on a shirt. It is easy to remember and hard to mess up. Simple is not lazy. Simple is powerful.')),
        card('THE BIG IDEA / 03 / 06', 'Less, but Better',
             para('Great designers follow a few rules to keep a logo strong. Keep these in mind for your own redesign.')
             + scrollrow(principles)),
        card('WORDS TO KNOW / 04 / 06', 'Logo Vocabulary',
             para('Learn these six terms. You will use them through the whole project.')
             + scrollrow(vocab_logo)),
        card('RESOURCES / 05 / 06', 'Watch and Learn',
             para('Want a deeper look at logo design? These cover the fundamentals. Click to open in a new tab.')
             + scrollrow(res_logo)),
        card('YOUR MISSION / 06 / 06', 'What You Will Do',
             para('You will take a famous logo you already know and reimagine it. You will work like a real designer: sketch first, get feedback, then build a polished digital version. Three steps, three turn-ins.')
             + scrollrow(mission)),
    ],
)

# =========================================================================
# PAGE 2 — STEP 01 THUMBNAILS
# =========================================================================
directions = [
    tile('Direction 01', 'Simplify', 'Remove every part the logo does not need. How few shapes can still say the brand? Strip it down.'),
    tile('Direction 02', 'Modernize', 'Keep the main idea but make it feel fresh and current. New look, same brand.'),
    tile('Direction 03', 'Go Bold', 'Push it further. Try a new angle, a new shape, or your own twist. Make it yours.'),
]
page(
    'logo-redesign-step01-thumbnails.html',
    'Step 1: Thumbnails | Logo Redesign | Digital Arts 1A | Mark Richardson Center',
    'Step 1',
    [('logo-redesign-overview.html', '&#8592; Overview'),
     ('logo-redesign-step02-final-sketch.html', 'Step 2 &#8594;')],
    'mrc-logo-redesign-step01-thumbnails-canvas.html',
    'Logo Redesign &nbsp;&bull;&nbsp; Step 1', 'Three Thumbnail Sketches',
    'Explore three quick redesign ideas.',
    [
        card('PICK YOUR LOGO / 01 / 03', 'Choose a Famous Logo',
             para('Pick one logo from a brand you already know well: a shoe brand, a game studio, a car, a restaurant, a team, or a phone. Choose one you find interesting and would enjoy redrawing.')
             + para('Pick a logo that has a clear shape or symbol, not just plain text. You want something you can simplify and make your own.')
             + para('Pull up a clear picture of the real logo on your screen, or print it. You will use it as your reference for the whole project.')
             + notecard('NOT SURE WHAT TO PICK?', 'Ask Mr. Silva', 'Bring two or three brands you like and Mr. Silva will help you choose the one with the most room to redesign.')),
        card('SKETCH THREE THUMBNAILS / 02 / 03', 'Three Quick Ideas',
             para('A thumbnail is a small, quick sketch, about the size of a business card. The small size keeps you fast and loose, so you try real ideas instead of fussing over details.')
             + para('Draw <strong>three different thumbnails</strong> of your logo. Make each one a different idea, not the same drawing three times. Try these three directions:')
             + '<div style="clear:both;"></div>'
             + scrollrow(directions)
             + para('Keep them rough. Thumbnails are about ideas, not clean lines. You will polish your best one later.'),
             floatimg(RAW + 'logo-thumbnails-float.png', 'Renee Lopez sketching three logo thumbnails in a sketchbook')),
        card('GET A CHECK / 03 / 03', 'Bring Them to Mr. Silva',
             para('Before you go any further, bring your three thumbnails to Mr. Silva for a quick visual check. This is a required checkpoint.')
             + para('Mr. Silva will look at your ideas and give you insight: which direction is strongest, what to push, and what to simplify even more.')
             + para('Take notes on the feedback. You will use it in Step 2 to choose and polish your best idea.')
             + notecard('CHECKPOINT', 'Raise Your Hand', 'When your three thumbnails are done, raise your hand for a check. Do not start your final sketch until you get the green light.')),
    ],
)

# =========================================================================
# PAGE 3 — STEP 02 FINAL SKETCH
# =========================================================================
page(
    'logo-redesign-step02-final-sketch.html',
    'Step 2: Final Sketch | Logo Redesign | Digital Arts 1A | Mark Richardson Center',
    'Step 2',
    [('logo-redesign-step01-thumbnails.html', '&#8592; Step 1'),
     ('logo-redesign-step03-digital.html', 'Step 3 &#8594;')],
    'mrc-logo-redesign-step02-final-sketch-canvas.html',
    'Logo Redesign &nbsp;&bull;&nbsp; Step 2', 'Your Final Sketch',
    'Polish your best idea and turn it in.',
    [
        card('CHOOSE YOUR BEST / 01 / 03', 'Pick the Winning Idea',
             para('Look back at your three thumbnails and the feedback from Mr. Silva. Choose the one idea that is the strongest and most exciting to build.')
             + para('You can also combine the best parts of two thumbnails into one stronger idea. Designers do this all the time.')),
        card('DRAW IT CLEAN / 02 / 03', 'One Polished Final Sketch',
             para('Now draw your chosen idea one more time, larger and cleaner. This is your <strong>final sketch</strong>, the plan you will follow in Photoshop.')
             + para('Make it neat: clean lines, clear shapes, and the colors you plan to use. Add notes about your fonts or colors off to the side if it helps.')
             + para('This sketch does not need to be perfect art. It needs to be a clear map of your new logo.')),
        card('PHOTOGRAPH AND TURN IN / 03 / 03', 'Snap It and Submit',
             para('Lay all of your sketches flat in good light. Use your phone to take clear, sharp photos of your three thumbnails and your final sketch.')
             + para('Tips for a good photo: fill the frame with the paper, hold the phone straight above the page, and keep your hand&rsquo;s shadow off the drawing.')
             + para('Turn your photos in to Step 2 in Canvas. Name your file:')
             + fname('FirstName LastInitial - Logo Sketch')
             + notecard('TURN IN', 'What to Submit', 'Clear photos of all three thumbnails plus your one polished final sketch.'),
             floatimg(RAW + 'logo-sketch-float.png', 'Renee Lopez photographing her logo sketches with a smartphone')),
    ],
)

# =========================================================================
# PAGE 4 — STEP 03 DIGITAL REDESIGN
# =========================================================================
tools = [
    tile('Pen Tool (Use This)', 'Pen Tool First', 'The <strong>Pen tool</strong> makes clean, sharp paths you fully control. Click to drop anchor points and drag to make curves. It is the pro way to build a logo and it stays crisp at any size. Use it as much as you can.'),
    tile('Shape Tools', 'Build With Shapes', 'The <strong>Rectangle, Ellipse, Polygon, and Line</strong> tools make crisp shapes fast. Hold <strong>Shift</strong> while you drag to keep them even, like a perfect circle or square.'),
    tile('Layers', 'Work in Layers', 'Put each part of your logo on its own <strong>layer</strong> and name it. You can hide, move, recolor, or restack a part without touching the rest.'),
    tile('Selections', 'Make Selections', 'Use the <strong>Marquee</strong> (boxes and ovals), the <strong>Lasso</strong> (freehand), or <strong>Object Selection</strong> to grab an area, then fill it, move it, or delete it.'),
    tile('Color', 'Fill With Color', 'Set your <strong>foreground color</strong>, then fill a shape or selection with <strong>Edit &gt; Fill</strong> or the <strong>Paint Bucket</strong>. Keep to two or three strong colors.'),
    tile('Eyedropper', 'Grab Colors', 'Click the <strong>Eyedropper</strong>, then click a color in your reference to pick it up. This keeps your colors consistent and on theme.'),
    tile('Align', 'Center It Up', 'Use the <strong>Move tool</strong> and the <strong>Align</strong> buttons to center your logo on the artboard so it looks balanced and clean.'),
    tile('Keep It Simple', 'Simple and Bold', 'Strong shapes, few colors, high contrast. Your logo should read in one second, even when it is shrunk down small.'),
]
def ilink(href, label):
    """Inline hyperlink that survives the Canvas sanitizer (no block wrapper)."""
    return ('<a href="%s" style="color:#eda268;text-decoration:underline;"><strong>%s &rarr;</strong></a>'
            % (href, label))

fonts = [
    tile('Source 01', 'dafont.com', 'A huge library of <strong>free</strong> fonts you can download. Browse by style, then download the font file to the computer.<br />' + ilink('https://www.dafont.com', 'Open dafont.com')),
    tile('Source 02', 'Adobe Fonts', 'Hundreds of quality fonts built right into your Adobe account. Turn one on and it shows up in Photoshop, no download needed.<br />' + ilink('https://fonts.adobe.com', 'Open Adobe Fonts')),
]
page(
    'logo-redesign-step03-digital.html',
    'Step 3: Digital Redesign | Logo Redesign | Digital Arts 1A | Mark Richardson Center',
    'Step 3',
    [('logo-redesign-step02-final-sketch.html', '&#8592; Step 2')],
    'mrc-logo-redesign-step03-digital-canvas.html',
    'Logo Redesign &nbsp;&bull;&nbsp; Step 3', 'Rebuild It in Photoshop',
    'Turn your sketch into a clean digital logo.',
    [
        card('SET UP YOUR DOCUMENT / 01 / 04', 'Start a New File',
             para('Open Photoshop. Go to <strong>File &gt; New</strong>. Make a square artboard, <strong>2000 &times; 2000 pixels</strong>, RGB color. In the <strong>Name</strong> box, name it <strong>FirstName LastInitial - Logo Redesign</strong>, then click Create.')
             + para('Save right away. Go to <strong>File &gt; Save As</strong> and save the layered <strong>.PSD</strong> file into your <strong>OneDrive Digital Arts</strong> folder. Save often as you work.')),
        card('BUILD YOUR LOGO / 02 / 04', 'Tools to Use',
             para('Rebuild your final sketch as a clean digital logo. Lead with the Pen tool, then use whatever else you need. Scroll for pointers on each tool.')
             + '<div style="clear:both;"></div>'
             + vscroll(tools),
             floatimg(RAW + 'logo-digital-float.png', 'Renee Lopez rebuilding the redesigned logo in Photoshop')),
        card('ADD TYPE AND FONTS / 03 / 04', 'Find the Right Font',
             para('Many logos include the brand name or a few letters. Choose a font that matches your new style: bold and clean, fun, sharp, or retro. Use one or two fonts at most.')
             + para('You can get fonts from two places. Pick one and add the font you like.')
             + scrollrow(fonts)
             + para('A downloaded font has to be <strong>installed</strong> on the computer before Photoshop can use it. Mr. Silva will demo how to install a font in class.')
             + para('Use the <strong>Type tool</strong> to add your text. Keep it readable and let it match the shapes in your logo.')),
        card('SAVE AND SUBMIT / 04 / 04', 'Save Twice, Submit the JPG',
             para('Save your layered Photoshop file (<strong>.PSD</strong>) one more time to your <strong>OneDrive Digital Arts</strong> folder so you keep all your layers.')
             + para('Then make a flat image to turn in. Use <strong>File &gt; Save a Copy</strong> and choose <strong>JPG</strong>. Name the JPG:')
             + fname('FirstName LastInitial - Logo Redesign.jpg')
             + para('Submit the JPG to Step 3 in Canvas. That is your finished, reimagined logo.')),
    ],
)

print('done')
