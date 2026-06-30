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
ZIP_URL = RAWBASE + 'assets/mrc/handouts/Magazine_Cover_Project.zip'

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

def videothumb(href, src, alt):
    # small clickable video thumbnail, floated right (Canvas-safe: anchor wraps an inline img)
    return ('<div style="float:right;width:34%%;min-width:200px;margin:0 0 14px 24px;text-align:center;">'
            '<a class="inline_disabled" href="%s" target="_blank" rel="noopener"><img src="%s" alt="%s" '
            'style="display:block;width:100%%;%s" /></a>'
            '<div style="font-size:8.5pt;letter-spacing:0.16em;text-transform:uppercase;color:#eda268;'
            'margin-top:8px;font-family:Arial,sans-serif;"><strong>&#9658; Watch on YouTube</strong></div></div>'
            % (href, src, alt, FRAME))

def refimg(src, alt):
    # small reference cover thumbnail inside a magazine tile
    return ('<img src="%s" alt="%s" style="display:block;width:150px;height:auto;margin:0 auto 12px;%s" />'
            % (src, alt, FRAME))

def floatimg(src, alt):
    return ('<img src="%s" alt="%s" style="float:right;width:42%%;min-width:240px;margin:0 0 18px 26px;%s" />'
            % (src, alt, FRAME))

def headerimg(src, alt):
    return ('<img src="%s" alt="%s" style="width:100%%;display:block;margin-bottom:24px;%s" />'
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
            '%s%s%s%s</div>' % (CARD_BG, FRAME, chip(label), tb(title), floatel, body))

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

def dlbutton(href, label):
    return ('<a href="%s" download style="background:rgba(255,255,255,0.92);color:#4a1e02;text-decoration:none;'
            'padding:7px 16px;display:inline-block;font-size:11pt;white-space:nowrap;border-top:2px solid #c95201;">'
            '<strong>&#11015; %s</strong></a>' % (href, label))

def bpara(text):
    return ('<div style="font-size:13.5pt;line-height:1.72;color:rgba(255,255,255,0.86);margin-bottom:12px;">%s</div>'
            % text)

def scrollbox(headline, accolade, body):
    # vertical scrolling brief, big headline on top for hierarchy (not cards)
    return ('<div style="font-size:30pt;color:#ffffff;line-height:1.05;margin-bottom:4px;"><strong>%s</strong></div>'
            '<div style="font-size:13pt;color:#eda268;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:14px;">'
            '<strong>%s</strong></div>'
            '<div class="silva-scroll" style="max-height:300px;overflow-y:auto;border:1px solid rgba(201,82,1,0.30);'
            'background:rgba(0,0,0,0.22);padding:18px 20px;">%s</div>'
            '<div style="text-align:center;font-size:8pt;color:rgba(201,82,1,0.65);letter-spacing:0.22em;'
            'text-transform:uppercase;margin-top:10px;font-family:Arial,sans-serif;"><strong>&#8597; scroll the brief &#8597;</strong></div>'
            % (headline, accolade, body))

TEDDY_BRIEF = (
    bpara('<strong>Teddy</strong> is the security officer at the Mark Richardson CTE Center and Ag Farm, but her real focus is people. She practices &ldquo;relational security&rdquo;: she learns every student&rsquo;s name, greets them by it, and makes the whole campus feel seen and safe. Students know her not just as an officer, but as a trusted mentor.')
    + bpara('She is also the <strong>campus photographer</strong>. Her photos of student grit and determination have appeared in school assemblies, school board reports, and local media, building real pride in the MRC.')
    + bpara('Teddy goes far beyond her job description. She checks on the animals daily, feeds livestock on weekends, helps the Robotics team prepare late into the night, waters the campus flowers, and pulls weeds, all because she cares. She even became <strong>forklift certified</strong> to keep students safe in an active CTE environment.')
    + bpara('Principal Dr. Paul Robinson calls her watchful and dedicated, and bus drivers, teachers, and students all trust her. She was named the <strong>2025/2026 Classified Employee of the Year</strong>, and as her nomination put it, Teddy proves that <strong>kindness and heart</strong> are the most powerful tools for building a strong school community.')
)

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
    open(os.path.join(OUT, filename), 'w').write(html)
    print('  %s  divs=%s  em=%d' % (filename, 'OK' if html.count('<div') == html.count('</div>') else 'IMBALANCE',
                                    html.count('—') + html.count('&mdash;')))

# =========================================================================
# PAGE 1 — OVERVIEW
# =========================================================================
mags = [
    tile('Option 01', 'Successful Farming',
         refimg(IMG + 'magcover-ref-successful.webp', 'Successful Farming magazine cover, for reference')
         + 'A big, clean masthead with one bold livestock or crop photo. Published at agriculture.com.<br />'
         + ilink('https://www.agriculture.com', 'Visit the site')),
    tile('Option 02', 'Progressive Farmer',
         refimg(IMG + 'magcover-ref-progressive.webp', 'Progressive Farmer magazine cover, for reference')
         + 'A modern look from DTN, often shot from above or on location in the field.<br />'
         + ilink('https://www.dtnpf.com/agriculture/web/ag/magazine', 'Visit the site')),
    tile('Option 03', 'Farm Journal',
         refimg(IMG + 'magcover-ref-farmjournal.png', 'Farm Journal magazine cover, for reference')
         + 'Classic, friendly covers that often feature a real farmer up close.<br />'
         + ilink('https://www.farmjournal.com', 'Visit the site')),
]
vocab = [
    tile('Term 01', 'Masthead', 'The magazine&rsquo;s name and logo at the top of the cover. It is the brand, and usually the biggest text.'),
    tile('Term 02', 'Cover Image', 'The one big photo that fills the cover and grabs your eye. It is also called the hero image.'),
    tile('Term 03', 'Cover Lines', 'The short, bold headlines that tease the stories inside. They are also called coverlines.'),
    tile('Term 04', 'Type Hierarchy', 'Using big, bold type for the main story and smaller type for the rest, so the eye knows where to look first.'),
    tile('Term 05', 'Bleed', 'When the photo runs all the way to the edge of the page with no white border. Covers almost always bleed.'),
    tile('Term 06', 'Photojournalism', 'Telling a true story with photos taken on location, in real moments, not posed in a studio.'),
]
required = [
    tile('Must-Have 01', 'Masthead', 'The real magazine logo, big and bold at the top.'),
    tile('Must-Have 02', 'Hero Image', 'One strong photo of <strong>Teddy</strong> that bleeds to the edges.'),
    tile('Must-Have 03', 'Main Title', 'A bold headline about Teddy and her honor, the biggest text on the cover.'),
    tile('Must-Have 04', 'Subtitle', 'A short line under the title that adds detail. This is the deck.'),
    tile('Must-Have 05', 'Breakout Points', 'At least three smaller cover lines that tease other MRC stories.'),
    tile('Must-Have 06', 'Two Breakout Boxes', 'Two small boxes, each with its own photo and a few words, for extra stories.'),
]
mission = [
    tile('STEP 01', 'Plan', 'Read Teddy&rsquo;s brief, plan your shots, and sketch your cover layout.'),
    tile('STEP 02', 'Capture', 'Shoot your hero photo and two breakout photos, then turn in a RAW folder screenshot.'),
    tile('STEP 03', 'Design', 'Build the cover in Photoshop with the masthead, your words, and two breakout boxes.'),
    tile('STEP 04', 'Reflect', 'Answer four questions about your cover and the choices you made.'),
]
brief_pull = [
    tile('Pull 01', 'Your Main Title', 'The biggest headline. Make it about Teddy and her honor, like &ldquo;The Heartbeat of MRC.&rdquo;'),
    tile('Pull 02', 'Your Subtitle', 'One short line under the title that adds a detail from her story, like relational security or campus photographer.'),
    tile('Pull 03', 'A Strong Quote or Fact', 'Something specific from the brief, like forklift certified or feeds livestock on weekends. Great for a breakout point.'),
    tile('Pull 04', 'Other Campus Stories', 'Two or three other things happening on campus to tease in your smaller boxes: the Ag Farm, Robotics, student projects.'),
]
scout = [
    tile('Scout 01', 'Walk the Spot', 'Visit your location ahead of time with just a camera. No tripod and no flash, travel light.'),
    tile('Scout 02', 'Shoot References', 'Take quick reference photos of a few spots and angles. These are notes, not your final shots.'),
    tile('Scout 03', 'Read the Light', 'Notice where the light falls and how the background looks. Look for the cleanest, strongest angle.'),
    tile('Scout 04', 'Decide on a Computer', 'Back in the lab, study your reference photos on the big screen and pick your best spot and angle.'),
    tile('Scout 05', 'Plan the Setup', 'Decide where you, your subject, and your flash will go before you haul all the gear out.'),
]
page(
    'magcover-overview.html',
    'Overview | Magazine Cover | Digital Arts 1A | Mark Richardson Center',
    'Overview', [('magcover-step01-plan.html', 'Step 1 &#8594;')],
    'mrc-magcover-overview-canvas.html',
    'Digital Arts 1A &nbsp;&bull;&nbsp; Module', 'Magazine Cover',
    'Tell the MRC story in one cover.',
    [
        headerimg(IMG + 'magcover-header.png', 'Julian photographing an MRC agriculture student by a tractor for a magazine cover shoot at golden hour'),
        card('WHAT IS A MAGAZINE COVER / 01 / 07', 'One Image, One Story',
             para('A magazine cover is the front page that makes you want to pick it up. It uses <strong>one strong photo</strong> and a few <strong>bold words</strong> to sell the whole magazine in a single glance.')
             + para('Look at a real cover: a big name at the top (the <strong>masthead</strong>), one powerful photo behind it, and short headlines that tease the stories inside.')
             + para('For this project you will design a real-looking <strong>agriculture magazine cover</strong> featuring <strong>Teddy</strong>, the MRC security officer and campus photographer named the <strong>2025/2026 Classified Employee of the Year</strong>. She is your cover star.')),
        card('PICK YOUR MAGAZINE / 02 / 07', 'Choose One of Three',
             para('You will design your cover in the style of one real farming magazine. Pick <strong>one</strong> of these three. Click to study each one and learn its tone and the kind of images it uses.')
             + scrollrow(mags)
             + para('All three magazine logos are <strong>already in your template</strong> as layers. When you design, just turn on the layer for the magazine you chose. No need to find or place a logo yourself.')),
        card('YOUR ASSIGNMENT / 03 / 07', 'You Are Shooting Teddy',
             para('You have been <strong>contracted</strong> to shoot the cover featuring <strong>Teddy</strong>. Her photo is your <strong>hero image</strong>, and the <strong>biggest headline</strong> on the cover is about her and her honor.')
             + para('Read her brief below. Pull your main <strong>title</strong> and <strong>subtitle</strong> from it. Your smaller <strong>cover lines</strong> and <strong>breakout boxes</strong> can tease other things happening on campus: the Ag Farm, the livestock, the Robotics team, student projects.')
             + scrollbox('Teddy', 'Winner, 2025/2026 Classified Employee of the Year', TEDDY_BRIEF)
             + notecard('THE FOCUS', 'Teddy Is the Star', 'Your cover can mention other campus stories in the smaller boxes, but the <strong>name, the cover photo, and the largest text</strong> must all be about Teddy and her honor.')),
        card('WHAT YOUR COVER MUST HAVE / 04 / 07', 'Set the Standard',
             para('Every finished cover must include all six of these. This is the standard you are graded on.')
             + scrollrow(required)),
        card('WORK AS A TEAM / 05 / 07', 'Brainstorm Together, Build Your Own',
             para('You may work in a <strong>group</strong>. Slow down and brainstorm together: share ideas, plan your shots, and trade photos and content so everyone has plenty to work with.')
             + para('But every student turns in their <strong>own unique cover</strong>. Same group and same shoot, different design. Your layout, your title, and your choices must be your own.')
             + notecard('TEAM RULE', 'Share Ideas, Not Covers', 'Help each other with ideas, planning, and photos. Then make a cover that is one hundred percent yours.')),
        card('WORDS TO KNOW / 06 / 07', 'Magazine Vocabulary',
             para('Learn these six terms. You will use them all the way through the project.')
             + scrollrow(vocab)),
        card('YOUR MISSION / 07 / 07', 'What You Will Do',
             para('You will work like a real photo editor in four steps: plan, capture, design, and reflect.')
             + scrollrow(mission)
             + '<div style="margin-top:18px;">' + dlbutton(ZIP_URL, 'Download the Project Folder') + '</div>'),
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
        card('YOUR COVER STAR / 01 / 05', 'The Cover Is About Teddy',
             para('Your subject is <strong>Teddy</strong>, the MRC security officer and campus photographer named the <strong>2025/2026 Classified Employee of the Year</strong>. You will photograph her and build the whole cover around her.')
             + para('Her <strong>brief</strong> is your source, like a press kit a real photo editor is handed. Read it closely, then turn her story into one strong cover.')
             + notecard('TEAM TIME', 'Brainstorm Together', 'Work with your group to plan your shots and pick which other campus stories to tease in the breakout boxes. Then each of you builds your own unique cover.')),
        card('READ THE BRIEF / 02 / 05', 'Pull Your Words From Teddy&rsquo;s Story',
             para('Read Teddy&rsquo;s brief and pull out the words for your cover. Your <strong>main title</strong> comes from her honor and her story, your <strong>subtitle</strong> adds one detail, and your <strong>breakout points</strong> tease other campus stories.')
             + scrollbox('Teddy', 'Winner, 2025/2026 Classified Employee of the Year', TEDDY_BRIEF)
             + scrollrow(brief_pull)),
        card('SKETCH YOUR LAYOUT / 03 / 05', 'Plan the Cover',
             para('On paper, sketch a quick <strong>thumbnail</strong> of your cover. Plan where each piece goes:')
             + para('Put the <strong>masthead</strong> at the top, block out your <strong>hero photo of Teddy</strong>, mark where your <strong>main title</strong> (the biggest text, about her) and your smaller <strong>breakout points</strong> go down one side, and box out spots for your <strong>two breakout images</strong>.')
             + para('Leave room for the text. Do not plan to cover <strong>Teddy&rsquo;s face</strong> with the masthead or headlines.'),
             floatimg(IMG + 'magcover-plan-float.png', 'Julian sketching a magazine cover layout in a sketchbook at the MRC studio')),
        card('SCOUT YOUR LOCATION / 04 / 05', 'Scout Before You Shoot',
             para('Real photographers <strong>scout</strong> a location before the real shoot. Scouting means visiting a spot early to study the light, the angles, and the background, so shoot day runs smoothly.')
             + para('Go out with <strong>just your camera</strong>, no flash or tripod yet, and take reference photos. You are not making finals, you are gathering notes to choose the best spot.')
             + scrollrow(scout)
             + notecard('WHY SCOUT', 'A Scouted Shoot Is a Fast Shoot', 'When you already know your spot and your setup, shoot day is spent making great photos instead of figuring out where to stand. Then you bring out the flash and gear.')),
        card('GET IT CHECKED / 05 / 05', 'Bring It to Mr. Silva',
             para('Before you shoot, show Mr. Silva your <strong>plan</strong>, your <strong>scouting photos</strong>, and your <strong>layout sketch</strong>. This is a quick checkpoint, no upload needed.')
             + notecard('CHECKPOINT', 'Plan First, Shoot Second', 'A clear plan and strong photos make a stronger cover. Get the green light, then bring out the camera and flash for Step 2.')),
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
        card('LEARN THE LIGHTING / 01 / 06', 'Watch This Before You Shoot',
             videothumb('https://www.youtube.com/watch?v=eBcTFRFcZWU&amp;t=38s', IMG + 'magcover-lighting-thumb.png', 'Watch the magazine lighting tutorial on YouTube')
             + para('A great cover photo uses great <strong>lighting</strong>. For this shoot you must light Teddy with an <strong>off-camera flash</strong>: we have a <strong>Godox AD200</strong> with a light stand and a trigger that connects to your <strong>Canon EOS R50</strong>.')
             + para('Watch this short tutorial (click the thumbnail) to see how it works. Mr. Silva will coach you on the shoot, but study it first so we move quickly together.')),
        card('SHOOT ON LOCATION / 02 / 06', 'Photojournalism Style',
             para('Photograph <strong>Teddy</strong> where she works: greeting students, out at the Ag Farm, with the animals, or around campus. Shoot <strong>real moments</strong>, not stiff poses. This is <strong>photojournalism</strong>.')
             + notecard('SHOOT VERTICAL', 'Hold the Camera Tall (Portrait)', 'Your cover is a <strong>tall, vertical</strong> shape, so every photo must be shot in <strong>portrait orientation</strong>. Turn the camera <strong>sideways so the frame is taller than it is wide</strong>. A wide (landscape) photo will not fill the cover and leaves empty gaps. If your shot is wider than it is tall, turn the camera and take it again.')
             + notecard('REQUIRED', 'Light It With the Off-Camera Flash', 'You must light your subject with the <strong>off-camera flash</strong> (the Godox AD200 on a stand, triggered from your Canon R50), not just natural light. A flash lets you control the look and mood and make your subject pop, like a real magazine portrait. Watch the lighting tutorial at the top of this page first.')
             + para('A <strong>studio</strong> with a backdrop is also set up if your story needs it.'),
             floatimg(IMG + 'magcover-capture-float.png', 'Julian photographing his cover subject kneeling beside cattle at the MRC campus at golden hour')),
        card('MAKE A STRONG HERO SHOT / 03 / 06', 'Frame the Cover Image',
             para('Your hero image carries the whole cover. Scroll through each pointer as you shoot.')
             + scrollrow(heroshot)),
        card('SHOOT YOUR BREAKOUT IMAGES / 04 / 06', 'Two More Photos',
             para('Your cover also needs <strong>two breakout boxes</strong>, each with its own small photo. While you are on location, shoot at least <strong>two more images</strong> for them.')
             + para('Good breakout shots tease <strong>other campus stories</strong>: the livestock, a Robotics build, a tool or crop, a wide shot of the Ag Farm, or a second angle of Teddy. Shoot extra so you have choices when you design.')),
        card('ORGANIZE YOUR FILES / 05 / 06', 'Keep It Organized',
             para('Use the <strong>project folder</strong> you downloaded from the overview. If you have not yet, move it into your <strong>OneDrive Digital Arts</strong> folder.')
             + para('Offload all your <strong>RAW</strong> files into the <strong>RAW Images</strong> subfolder inside it. Keep every part of this project organized here.')),
        card('TURN IT IN / 06 / 06', 'Screenshot Your RAW Folder',
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
    tile('Words 01', 'Main Title', 'One big, bold headline about <strong>Teddy</strong> is the star, and the <strong>largest text</strong> on the cover. Pull it from her brief, short and powerful, like &ldquo;The Heartbeat of MRC.&rdquo;'),
    tile('Words 02', 'Subtitle', 'Add a short line under the title (the deck) that gives one more detail about Teddy and her honor.'),
    tile('Words 03', 'Breakout Points', 'Add at least three smaller cover lines that tease <strong>other campus stories</strong> (the Ag Farm, livestock, Robotics), using facts from the brief or what you saw on campus.'),
    tile('Words 04', 'Use Type Hierarchy', 'Make Teddy&rsquo;s title the biggest, the subtitle smaller, and the breakout points smaller still. Size shows what matters most.'),
    tile('Words 05', 'Keep Text Off the Face', 'Place your words in the open space you left when you shot. Never cover Teddy&rsquo;s face or eyes.'),
    tile('Words 06', 'Match the Magazine', 'Use fonts and colors close to your real magazine&rsquo;s style so your cover looks authentic.'),
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
        card('SET UP YOUR COVER / 01 / 05', 'Open the Template',
             para('Open the <strong>Magazine Cover template</strong> from your project folder with <strong>File &gt; Open</strong>. It is already built for you: tall (portrait), <strong>8.5 by 11 inches</strong>, RGB color, 300 ppi. You do not need to make your own.')
             + para('You will see <strong>cyan guide lines</strong> a little in from each edge. These lines <strong>do not print</strong>. They mark the <strong>text-safe area</strong>: keep your <strong>masthead, headlines, cover lines, and anything important</strong> inside the lines so nothing gets trimmed off.')
             + para('Your <strong>cover photo must full bleed</strong>. Open your best hero photo of <strong>Teddy</strong> through <strong>Camera Raw</strong>, place it, and extend it <strong>past the cyan lines all the way to the edges</strong> of the page, with no white border. Covers are cut at the edge, so the photo has to run right off the page.')
             + notecard('LOCK THEM', 'Lock Your Guides', 'So you do not move the guides by accident, go to <strong>View &gt; Lock Guides</strong>. They will stay put while you work.')
             + para('Save your work as a <strong>.PSD</strong> in your project folder.'),
             floatimg(IMG + 'magcover-template-guides.png', 'The magazine cover template open in Photoshop, showing the cyan text-safe guide lines and the magazine logo layers')),
        card('ADD THE MASTHEAD / 02 / 05', 'Turn On Your Logo Layer',
             para('All three magazine logos are <strong>already in the template</strong> as layers. In the <strong>Layers</strong> panel, find the logo for the magazine you chose and <strong>turn its layer on</strong> (click the eye icon). Hide the other two.')
             + para('The masthead is the brand, so it sits big and bold at the <strong>top</strong> of your cover. Keep it inside the cyan guides.')),
        card('ADD YOUR WORDS / 03 / 05', 'Title, Subtitle, and Breakout Points',
             para('Use the <strong>Type tool</strong> to add all the words from the brief. Scroll through each pointer.')
             + scrollrow(coverlines)),
        card('ADD TWO BREAKOUT BOXES / 04 / 05', 'Feature Two More Stories',
             para('Add your <strong>two breakout boxes</strong>. Each one is a small box with one of your <strong>breakout photos</strong> inside and a few words next to it, like a mini cover line.')
             + para('Keep them the same size and lined up neatly so they look clean and on purpose, just like the breakout boxes on a real cover.')),
        card('SAVE AND SUBMIT / 05 / 05', 'Save as JPG and Submit',
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
    tile('Question 01', 'Your Magazine', 'Which magazine did you design for, and why did it fit Teddy&rsquo;s story?'),
    tile('Question 02', 'Your Headline', 'What did you choose for your main title about Teddy, and why does it capture her?'),
    tile('Question 03', 'The Hard Part', 'What was hardest for you: the shoot, the layout, or the design? How did you solve it?'),
    tile('Question 04', 'The Big Picture', 'If a real magazine printed your cover, what would people learn about Teddy and the MRC?'),
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
             floatimg(IMG + 'magcover-reflection-float.png', 'Julian holding a printed proof of his finished farming magazine cover at the MRC lab')),
    ],
)

print('done')
