#!/usr/bin/env python3
"""Generate the MRC Digital Arts 1A "Photo Scavenger Hunt" overview page
(English only) on the locked Angular Gradient Framework (orange #c95201).
One Canvas page: the mission, how it works, camera basics, composition
basics, safety rules, and a turn-in section with a Download Shot List
(PDF) button. The actual hunt list is a printable PDF (built separately).
"""
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'curriculum', 'mrc')

RAW = 'https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/mrc/images/'
PDF_URL = 'https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/mrc/handouts/MRC_Photo_Scavenger_Hunt.pdf'
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

def thumb(src, alt):
    """Small framed product thumbnail (white fill), floated right."""
    return ('<div style="float:right;width:170px;background:#ffffff;%spadding:10px;margin:0 0 14px 22px;">'
            '<img src="%s" alt="%s" style="width:100%%;height:auto;display:block;" /></div>'
            % (FRAME, src, alt))

def ph(desc):
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

def ilink(href, label):
    return ('<a href="%s" target="_blank" rel="noopener" style="color:#eda268;text-decoration:underline;"><strong>%s</strong></a>'
            % (href, label))

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

# composition concept tiles (define every shot challenge on the paper list)
comp = [
    tile('Composition', 'Leading Lines', 'Use a road, fence, or row of crops to pull your eye into the photo.'),
    tile('Composition', 'Rule of Thirds', 'Put your subject off to one side, not dead center. It feels more natural.'),
    tile('Composition', 'Framing', 'Shoot through a gate, window, or branches to frame your subject.'),
    tile('Composition', 'Texture', 'Get close to a rough surface so the viewer can almost feel it.'),
    tile('Composition', 'Pattern', 'Find shapes that repeat, like fence posts or stacked pipes.'),
    tile('Composition', 'Fill the Frame', 'Get close so your subject fills the whole photo, with no empty space.'),
    tile('Composition', 'Low Angle', 'Crouch down low and shoot upward for a bold, powerful angle.'),
    tile('Composition', 'Negative Space', 'Leave lots of empty space around a small subject to make it pop.'),
]

# what the judges score every set on
judges = [
    tile('Judging', 'Accuracy', 'Your photo clearly shows the prompt. A texture shot is really about texture.'),
    tile('Judging', 'Composition', 'You used the technique and framed it with care, not just a quick snapshot.'),
    tile('Judging', 'Creativity', 'A fresh or clever take that stands out from everyone else.'),
    tile('Judging', 'Image Quality', 'Sharp focus, good light, and clean. Not blurry and not too dark.'),
]

vocab_scav = [
    tile('Vocabulary', 'Composition', 'How you arrange the things in your photo inside the frame.'),
    tile('Vocabulary', 'Leading Lines', 'Lines in a scene, like a road or fence, that pull the eye toward your subject.'),
    tile('Vocabulary', 'Rule of Thirds', 'Placing your subject off-center for a more natural, balanced shot.'),
    tile('Vocabulary', 'Framing', 'Shooting through something, like a gate or branches, to frame your subject.'),
    tile('Vocabulary', 'Fill the Frame', 'Getting close so your subject fills the photo, with no wasted empty space.'),
    tile('Vocabulary', 'Culling', 'Choosing your single best photo and dropping the rest.'),
]

print('Photo Scavenger Hunt (2-page module):')
page(
    'scavenger-hunt-overview.html',
    'Photo Scavenger Hunt | Digital Arts 1A | Mark Richardson Center',
    'Photo Scavenger Hunt',
    [('scavenger-hunt-step01-hunt.html', 'Step 1 &#8594;')],
    'mrc-scavenger-hunt-overview-canvas.html',
    'Digital Arts 1A &nbsp;&bull;&nbsp; Module', 'Photo Scavenger Hunt',
    'Fifteen shots. Best set wins the prize.',
    [
        card('THE MISSION / 01 / 05', 'Your First Photo Hunt',
             para('Today you grab a real camera and go hunting, not for animals, but for great shots. The Mark Richardson Center is full of them: livestock and crops, big machines, rusted metal, rough wood, and an American flag.')
             + para('Here is the twist: this is a <strong>contest</strong>. Everyone shoots the same 15 shots, and the best set wins a prize. You do not need to know every button. You just need to look closely and frame each shot with care. This is how every photographer starts: by learning to <strong>see</strong>.'),
             floatimg(RAW + 'scavenger-mission-float.png', 'Patricia Guererro photographing an orange MRC tractor at golden hour outside the Mark Richardson Center')),
        card('THE PRIZE / 02 / 05', 'Win a $20 Chick-fil-A Gift Card',
             thumb(RAW + 'chick-fil-a-meal.png', 'A Chick-fil-A meal: chicken sandwich, waffle fries, and a drink')
             + para('The student with the best set of 15 photos wins a <strong>$20 Chick-fil-A gift card</strong>. One winner, chosen by Mr. Silva.')
             + para('Every shot counts, so give each one your best effort. A strong, complete set beats a few lucky photos.')
             + notecard('THE PRIZE', '$20 Chick-fil-A Gift Card', 'The best full set of 15 photos takes it home. Make every shot count.')),
        card('HOW IT WORKS / 03 / 05', 'The Same 15 Shots for Everyone',
             para('You get a paper shot list with <strong>15 shots</strong>. Everyone shoots the same list, so it is a fair contest. Some are <strong>things to find</strong>, like an American flag or a tractor. Some are <strong>shot challenges</strong>, like leading lines or texture.')
             + para('Take lots of photos as you go. Shoot each item more than once to get it right. Later you will pick your single best photo for each of the 15.')
             + notecard('THE GOAL', 'Quality Over Speed', 'It is not a race. One well-framed photo beats five quick snapshots. Slow down and look before you press the shutter.'),
             floatimg(RAW + 'scavenger-list-float.png', 'Julian reading the printed photo scavenger hunt shot list outside the MRC at golden hour, a Canon camera around his neck')),
        card('WORDS TO KNOW / 04 / 05', 'Photo Vocabulary',
             para('Learn these six terms. You will use them all over the hunt.')
             + scrollrow(vocab_scav)),
        card('RESOURCES / 05 / 05', 'Get the List and Learn',
             para('Download the shot list before you head out, and brush up on composition. Click to open in a new tab.')
             + scrollrow([
                 tile('Resource', 'The 15-Shot List', 'Everyone hunts the same 15 shots. Download the printable list below, print it, and check off each one as you go.'),
                 tile('Resource', 'Composition Basics', 'A beginner guide to rule of thirds, leading lines, and framing. ' + ilink('https://tamron-americas.com/blog/photo-composition-beginners-guide/', 'Open &rarr;')),
             ])
             + '<div style="margin-top:18px;">' + dlbutton(PDF_URL, 'Download the Shot List (PDF)') + '</div>'),
    ],
)

page(
    'scavenger-hunt-step01-hunt.html',
    'Step 1: The Hunt | Photo Scavenger Hunt | Digital Arts 1A | Mark Richardson Center',
    'Step 1',
    [('scavenger-hunt-overview.html', '&#8592; Overview')],
    'mrc-scavenger-hunt-step01-canvas.html',
    'Photo Scavenger Hunt &nbsp;&bull;&nbsp; Step 1', 'Shoot the Hunt',
    'Camera ready. Go find your shots.',
    [
        card('YOUR CAMERA, MADE EASY / 01 / 05', 'Let the Camera Do the Work',
             para('Set the dial to <strong>AUTO</strong>. In auto mode the camera handles the focus, the light, and the color for you. Your only job is <strong>what to point it at</strong> and <strong>how to frame it</strong>.')
             + para('Hold the camera with both hands and tuck your elbows into your body to stay steady. Press the shutter button <strong>halfway</strong> to lock focus, wait for the beep or the green box, then press the rest of the way to take the shot.')
             + para('Blurry photo? Hold still, press halfway again, and let it focus before you shoot.')),
        card('COMPOSITION BASICS / 02 / 05', 'How to Frame a Great Shot',
             para('Composition means how you arrange what is in your photo. These are the shot challenges on your list. Learn them here, then go find them out there.')
             + scrollrow(comp)),
        card('HOW YOU WIN / 03 / 05', 'What the Judges Look For',
             para('Mr. Silva will score every set on four things. Keep them in mind for every single shot.')
             + scrollrow(judges)),
        card('RULES OF THE HUNT / 04 / 05', 'Stay Safe, Shoot Smart',
             para('You will be outdoors around animals and heavy equipment. Safety comes first, every time.')
             + para('<strong>Keep your distance</strong> from livestock and machinery. Never climb on or reach into equipment, and never enter a pen or a gated area. Watch your footing on uneven ground.')
             + para('Stay with your group and your teacher. Respect the campus and the animals. Photograph the work, but do not touch tools or machines that are not yours.')),
        card('TURN IT IN / 05 / 05', 'Cull Your Best and Submit',
             para('Back in class, look through everything you shot. For each of the 15 prompts, pick your <strong>single best photo</strong>. Choosing your strongest shot and dropping the rest is called <strong>culling</strong>.')
             + para('Submit all <strong>15 photos as JPG files</strong> to this assignment in Canvas, one for each prompt. Tip: name each file with its number, like <strong>01 American Flag</strong>, so they stay in order.')),
    ],
)
