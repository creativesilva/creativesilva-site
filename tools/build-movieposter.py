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
ZIP_URL = RAWBASE + 'assets/mrc/handouts/Movie_Poster_Project.zip'

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

def refimg(src, alt):
    # small reference cover thumbnail inside a magazine tile
    return ('<img src="%s" alt="%s" style="display:block;width:150px;height:auto;margin:0 auto 12px;%s" />'
            % (src, alt, FRAME))

def videothumb(href, src, alt):
    # small clickable video thumbnail, floated right (Canvas-safe: anchor wraps an inline img)
    return ('<div style="float:right;width:34%%;min-width:200px;margin:0 0 14px 24px;text-align:center;">'
            '<a href="%s" target="_blank" rel="noopener"><img src="%s" alt="%s" '
            'style="display:block;width:100%%;%s" /></a>'
            '<div style="font-size:8.5pt;letter-spacing:0.16em;text-transform:uppercase;color:#eda268;'
            'margin-top:8px;font-family:Arial,sans-serif;"><strong>&#9658; Watch on YouTube</strong></div></div>'
            % (href, src, alt, FRAME))

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

def dlbutton(href, label):
    return ('<a href="%s" download="" style="background:rgba(255,255,255,0.92);color:#4a1e02;text-decoration:none;'
            'padding:7px 16px;display:inline-block;font-size:11pt;white-space:nowrap;border-top:2px solid #c95201;">'
            '<strong>%s</strong></a>' % (href, label))

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
concepts = [
    tile('Idea 01', 'The Herd', 'After dark, the cattle in the MRC pens stop acting like cattle. They stand in perfect rows, all facing the same way, watching the barn door. The night-feed student is not alone.<br /><strong>Tagline:</strong> &ldquo;The herd is watching.&rdquo;'),
    tile('Idea 02', 'The Pen', 'Something is wrong in the hog barn. The pigs go quiet, then they do not. Whatever has gotten into them has learned how to open the gate.<br /><strong>Tagline:</strong> &ldquo;The pen never goes quiet anymore.&rdquo;'),
    tile('Idea 03', 'Night Shift', 'A student locks up the ag-mechanics shop alone after dark. The machines power on by themselves, and a shadow moves in the sparks.<br /><strong>Tagline:</strong> &ldquo;Some machines never clock out.&rdquo;'),
]
vocab = [
    tile('Term 01', 'Title Treatment', 'The styled design of the movie&rsquo;s name. The font and look set the mood before you read a word.'),
    tile('Term 02', 'Tagline', 'One short, haunting line that hooks you, like &ldquo;You can&rsquo;t find your way out.&rdquo;'),
    tile('Term 03', 'Key Art', 'The main image of the poster, also called the hero image. It carries the whole feeling of the movie.'),
    tile('Term 04', 'Billing Block', 'The thin block of credits at the bottom: the cast, the director, and the studio.'),
    tile('Term 05', 'Mood and Tone', 'The feeling the poster gives, set with color, light, and shadow. Scary posters are dark and moody.'),
    tile('Term 06', 'Teaser vs Theatrical', 'A teaser poster shows just enough to spark curiosity. A theatrical poster shows more right before release.'),
]
required = [
    tile('Must-Have 01', 'A Clear Protagonist', 'Show the star, the hero we follow. We should know who to root for at a glance.'),
    tile('Must-Have 02', 'A Clear Antagonist', 'Show the villain or scary monster. The threat should be obvious and recognizable right away.'),
    tile('Must-Have 03', 'Title', 'The movie name, big and styled to match the scary mood.'),
    tile('Must-Have 04', 'Tagline', 'One short, creepy line that hooks the viewer.'),
    tile('Must-Have 05', 'Subtitle', 'A short second line that adds detail or sets up the story.'),
    tile('Must-Have 06', 'Production Logo', 'A production company or studio logo. Make one up for your film.'),
    tile('Must-Have 07', 'Actor Names', 'At least two or three actor names (your cast), placed with the credits.'),
    tile('Must-Have 08', 'Mood and Hierarchy', 'A dark, moody color grade, and clear type hierarchy so the eye knows what matters most.'),
]
mission = [
    tile('STEP 01', 'Plan', 'Pick a concept, research the genre, cast your hero and villain, and sketch your poster.'),
    tile('STEP 02', 'Capture', 'Shoot your moody hero image and supporting shots, then turn in a RAW folder screenshot.'),
    tile('STEP 03', 'Design', 'Build the poster with a title treatment, a tagline, and a billing block.'),
    tile('STEP 04', 'Reflect', 'Answer four questions about your poster and the choices you made.'),
]
page(
    'movieposter-overview.html',
    'Overview | Movie Poster | Digital Arts 1A | Mark Richardson Center',
    'Overview', [('movieposter-step01-plan.html', 'Step 1 &#8594;')],
    'mrc-movieposter-overview-canvas.html',
    'Digital Arts 1A &nbsp;&bull;&nbsp; Module', 'Movie Poster',
    'Sell the scare in one image.',
    [
        headerimg(IMG + 'movieposter-header.png', 'A nighttime movie poster shoot at the MRC: a student photographer captures an actor holding a flashlight in a foggy field'),
        card('WHAT IS A MOVIE POSTER / 01 / 08', 'One Image, One Scare',
             para('A movie poster is one image that makes you want to see the film. It uses <strong>one strong photo</strong>, a <strong>title</strong>, and a short <strong>tagline</strong> to sell the whole story in a single glance.')
             + para('A scary movie poster does it with <strong>mood</strong>: dark shadows, cold color, and a feeling that something is wrong.')
             + para('For this project you will design a real-looking <strong>movie poster</strong> for a PG-13 scary movie set at the Mark Richardson Center.')),
        card('MOVIE IDEAS / 02 / 08', 'Three Ideas to Get You Started',
             para('Need a starting point? Here are three scary movie <strong>ideas</strong> set right here at the MRC. Use one as it is, or let it spark something of your own.')
             + scrollrow(concepts)
             + para('<strong>Have a better idea? Pitch it.</strong> If you have your own creative concept, run it by <strong>Mr. Silva for approval</strong> first. As long as it stays PG-13 and school-appropriate, original ideas are encouraged.')),
        card('KEEP IT PG-13 / 03 / 08', 'Scary, Not Gross',
             para('Scary is great. <strong>Gross is not.</strong> Your movie must stay <strong>PG-13</strong> and school-appropriate. Build fear with <strong>mood, shadow, and suspense</strong>, not blood, gore, or weapons.')
             + para('Think about the scariest part of a movie, the part before anything even happens: the dark hallway, the sound behind you, the thing you cannot quite see. That is your goal.')
             + notecard('THE RULE', 'Get It Approved', 'Mr. Silva must approve your concept before you shoot. No blood, no gore, no weapons, nothing that breaks school rules. When in doubt, ask.')),
        card('WHAT YOUR POSTER MUST HAVE / 04 / 08', 'Set the Standard',
             para('Every finished poster must include all eight of these. This is the standard you are graded on. The protagonist and antagonist should be clear and recognizable at first glance.')
             + scrollrow(required)),
        card('WORK AS A TEAM / 05 / 08', 'Brainstorm Together, Build Your Own',
             para('You may work in a <strong>group</strong>. Slow down and brainstorm together: share concept ideas, act in each other&rsquo;s shoots, and trade photos so everyone has plenty to work with.')
             + para('But every student turns in their <strong>own unique poster</strong>. Same group and same shoot, different design. Your title, your mood, and your choices must be your own.')
             + notecard('TEAM RULE', 'Share Ideas, Not Posters', 'Help each other with ideas, acting, and photos. Then make a poster that is one hundred percent yours.')),
        card('LEARN THE LIGHTING / 06 / 08', 'Watch This Before We Shoot',
             videothumb('https://www.youtube.com/watch?v=fPJC1e_MmS0', IMG + 'movieposter-lighting-thumb.png', 'Watch the lighting tutorial on YouTube')
             + para('Most scary posters turn <strong>day into night</strong>, and the secret is <strong>lighting</strong>. We have a <strong>Godox AD200</strong> portable flash with a light stand and a trigger that connects to your <strong>Canon EOS R50</strong>.')
             + para('Watch this short tutorial to see how the lighting works (click the thumbnail). When we head out to shoot, Mr. Silva will coach you, but if you have studied this first it will all make sense fast and we can move quickly together.')),
        card('WORDS TO KNOW / 07 / 08', 'Movie Poster Vocabulary',
             para('Learn these six terms. You will use them all the way through the project.')
             + scrollrow(vocab)),
        card('YOUR MISSION / 08 / 08', 'What You Will Do',
             para('You will work like a real movie marketing artist in four steps: plan, capture, design, and reflect.')
             + scrollrow(mission)
             + '<div style="margin-top:18px;">' + dlbutton(ZIP_URL, 'Download the Project Folder') + '</div>'),
    ],
)

# =========================================================================
# PAGE 2 — STEP 01 PLAN
# =========================================================================
research = [
    tile('Look At 01', 'Color Schemes', 'What colors set the mood? Notice the black, cold blue, deep red, or sickly green in horror posters.'),
    tile('Look At 02', 'Font Choices', 'Are the titles sharp, rough, hand-drawn, or clean? How does the lettering make you feel?'),
    tile('Look At 03', 'Layout', 'Where do the title, the faces, and the credits sit? How is the empty space used?'),
    tile('Look At 04', 'Hero and Villain', 'How do they show the good guy and the threat? The villain often looms large or hides in shadow.'),
    tile('Look At 05', 'Genre Trends', 'What do recent scary-movie posters have in common? Find ideas you can borrow.'),
]
decide = [
    tile('Decide 01', 'Protagonist', 'Who is the hero, the star we follow? Cast a friend to play them.'),
    tile('Decide 02', 'Antagonist', 'Who or what is the villain or monster? How will you show the threat?'),
    tile('Decide 03', 'Title', 'Name your movie. Short and creepy works best.'),
    tile('Decide 04', 'Tagline', 'Write one haunting line that hooks the viewer.'),
    tile('Decide 05', 'Subtitle', 'A short second line that adds detail or sets up the story.'),
    tile('Decide 06', 'Studio and Cast', 'Make up a production company name and pick two or three actor names for the credits.'),
    tile('Decide 07', 'Location and Mood', 'Pick a moody spot and your colors: cold blues, deep shadows, low fog.'),
]
page(
    'movieposter-step01-plan.html',
    'Step 1: Plan | Movie Poster | Digital Arts 1A | Mark Richardson Center',
    'Step 1',
    [('movieposter-overview.html', '&#8592; Overview'), ('movieposter-step02-capture.html', 'Step 2 &#8594;')],
    'mrc-movieposter-step01-plan-canvas.html',
    'Movie Poster &nbsp;&bull;&nbsp; Step 1', 'Plan Your Poster',
    'Pick your story and sketch the layout.',
    [
        card('PICK YOUR CONCEPT / 01 / 05', 'Choose or Pitch',
             para('Use one of the three ideas from the overview as a starting point, or pitch your own creative concept to <strong>Mr. Silva for approval</strong>. Then write your <strong>logline</strong>: one sentence that says who the story is about, where it happens, and what is wrong.')
             + notecard('KEEP IT PG-13', 'Get It Approved First', 'Your concept must be school-appropriate and approved by Mr. Silva before you shoot. Scary with mood and suspense, never with blood, gore, or weapons.')),
        card('RESEARCH THE GENRE / 02 / 05', 'Study Real Scary Posters',
             para('Before you design anything, study how real scary movie posters work. As a group, pull up posters from horror and thriller films and notice what they share. Spend real time on this, good research leads to good design.')
             + scrollrow(research)
             + notecard('TEAM RESEARCH', 'Decide Together', 'Talk through what you find and agree as a group on a <strong>color scheme</strong>, a <strong>font style</strong>, and a <strong>layout direction</strong> before you build. Then each of you makes your own poster from that shared plan.')),
        card('WRITE AND CAST / 03 / 05', 'Build Your Movie',
             para('Now decide the pieces of your movie. These choices give you the people, the words, and the look for your poster. Scroll through each one.')
             + scrollrow(decide)),
        card('SKETCH YOUR LAYOUT / 04 / 05', 'Plan the Poster',
             para('On paper, sketch a quick <strong>thumbnail</strong> of your poster. Use <strong>design hierarchy</strong>: plan where each piece goes and how big it is.')
             + para('Show your <strong>protagonist</strong> as the main focus and your <strong>antagonist</strong> (villain or monster) as a clear threat. Put the big <strong>title</strong> near the bottom, mark spots for the <strong>tagline</strong> and <strong>subtitle</strong>, the <strong>production logo</strong>, and the <strong>actor names</strong> and credits.')
             + para('Leave room for the text. Both characters and the title should read at a glance.'),
             floatimg(IMG + 'movieposter-plan-float.png', 'Ricardo Gomez sketching a movie poster layout in a sketchbook at the MRC studio')),
        card('GET IT CHECKED / 05 / 05', 'Get Approved',
             para('Before you shoot, show Mr. Silva your <strong>concept</strong>, your <strong>cast and location</strong>, and your <strong>layout sketch</strong>. This is a required checkpoint.')
             + notecard('CHECKPOINT', 'Approval First, Shoot Second', 'Your concept must be approved so it stays PG-13 and school-safe. Get the green light, then grab a camera for Step 2.')),
    ],
)

# =========================================================================
# PAGE 3 — STEP 02 CAPTURE
# =========================================================================
heroshot = [
    tile('Shot 01', 'Shoot Vertical', 'Turn the camera tall (portrait). Posters are tall, so your hero photo should be too.'),
    tile('Shot 02', 'Use Dramatic Light', 'Light from one side, from below, or with a flashlight. Hard shadows feel scary.'),
    tile('Shot 03', 'Strong Expression', 'Direct your character: a stare, a look back, fear in the eyes. Mood is everything.'),
    tile('Shot 04', 'Leave Title Room', 'Keep the top or bottom a little open so your title and tagline will fit later.'),
    tile('Shot 05', 'Shoot a Lot', 'Try many angles, low and high. Creepy angles make a creepy poster.'),
]
page(
    'movieposter-step02-capture.html',
    'Step 2: Capture | Movie Poster | Digital Arts 1A | Mark Richardson Center',
    'Step 2',
    [('movieposter-step01-plan.html', '&#8592; Step 1'), ('movieposter-step03-design.html', 'Step 3 &#8594;')],
    'mrc-movieposter-step02-capture-canvas.html',
    'Movie Poster &nbsp;&bull;&nbsp; Step 2', 'Shoot Your Scene',
    'Capture your moody hero image.',
    [
        card('SHOOT YOUR SCENE / 01 / 05', 'Shoot by Day, Go Dark Later',
             para('Take your actor to a moody spot: the field, the barn, or the shop. Build fear with <strong>shadow and angle</strong>, not action.')
             + para('We cannot be on campus at night, so you will shoot in the <strong>daytime</strong> and turn it into night later in Photoshop. A <strong>studio</strong> with a <strong>backdrop and constant lighting</strong> is also great, because you control every shadow.')
             + notecard('SHOOT FOR NIGHT', 'Make the Convert Easy', 'Shoot on an overcast day or in open shade so the light is soft and even. Keep some <strong>sky</strong> in your frame so you can replace it, and keep harsh sun off your subject. Soft daytime photos turn into night the cleanest.'),
             floatimg(IMG + 'movieposter-capture-float.png', 'Ricardo Gomez photographing his actor in a doorway in daylight at the MRC')),
        card('SHOOT YOUR PROTAGONIST / 02 / 05', 'Frame the Hero',
             para('Start with your <strong>protagonist</strong>, the star of the film. This hero shot carries the whole poster. Scroll through each pointer as you shoot.')
             + scrollrow(heroshot)),
        card('SHOOT YOUR ANTAGONIST / 03 / 05', 'Capture the Threat',
             para('Now capture your <strong>antagonist</strong>, the villain or scary monster, so it reads as a clear threat. Keep it PG-13: scary, not gross.')
             + para('Ideas: a second actor in deep <strong>shadow</strong>, a <strong>silhouette</strong> in a doorway, a figure in a mask, a pair of eyes, or a looming shape you will darken later. Often the villain looms large or hides in the dark.')
             + para('Also grab <strong>two or more atmosphere shots</strong>: fog, the empty location, a creepy detail, or a texture, to blend in when you design.')),
        card('ORGANIZE YOUR FILES / 04 / 05', 'Keep It Organized',
             para('Use the <strong>project folder</strong> you downloaded from the overview. If you have not yet, move it into your <strong>OneDrive Digital Arts</strong> folder.')
             + para('Offload all your <strong>RAW</strong> files into the <strong>RAW Images</strong> subfolder inside it. Keep every part of this project organized here.')),
        card('TURN IT IN / 05 / 05', 'Screenshot Your RAW Folder',
             para('Open <strong>Finder</strong> and switch to <strong>Icon view</strong> so you can see the photo thumbnails.')
             + para('Open your <strong>RAW Images</strong> folder so the window shows the folder name and your thumbnails inside. Press the <strong>F15</strong> key to take the screenshot. On our Macs, F15 saves it straight to your <strong>Desktop</strong> as a PNG.')
             + para('Find it on the Desktop and rename it:')
             + fname('FirstName LastInitial - Movie Poster (PNG)')
             + imgfull(IMG + 'pano-raw-folder-screenshot.png', 'Example screenshot of a RAW Images folder in Finder Icon view', 'Your screenshot should look like this')
             + para('Upload the PNG screenshot to Step 2 in Canvas.')),
    ],
)

# =========================================================================
# PAGE 4 — STEP 03 DESIGN
# =========================================================================
words = [
    tile('Words 01', 'Tagline and Subtitle', 'Add your one creepy <strong>tagline</strong> and a short <strong>subtitle</strong> near the title. Keep both short and easy to read.'),
    tile('Words 02', 'Actor Names', 'Add 2 to 3 <strong>actor names</strong>. The biggest names often go across the top; the rest sit in the credits block at the bottom.'),
    tile('Words 03', 'Production Logo', 'Add your made-up <strong>production company</strong> logo or name. It usually sits small near the top or in the bottom credits.'),
    tile('Words 04', 'Billing and Rating', 'Add a thin <strong>billing block</strong> at the bottom (cast, director, studio) plus the PG-13 rating and a release line.'),
    tile('Words 05', 'Use Type Hierarchy', 'Make the title the biggest, the names and tagline medium, and the credits smallest. Size tells the eye what matters most.'),
    tile('Words 06', 'Keep It Readable', 'Dark posters can hide text. Add a soft glow or shadow so every word still pops.'),
]
dafont_steps = [
    tile('daFont 01', 'Browse and Download', 'Go to <strong>dafont.com</strong>, find a font you like (try the Horror or Gothic categories), and click <strong>Download</strong>. A .zip saves to your Downloads.'),
    tile('daFont 02', 'Unzip the File', 'In Finder, open <strong>Downloads</strong> and double-click the .zip to unzip it. Inside is a font file that ends in <strong>.ttf</strong> or <strong>.otf</strong>.'),
    tile('daFont 03', 'Install the Font', 'Double-click the font file. <strong>Font Book</strong> opens with a preview. Click <strong>Install Font</strong>. The font is now on the Mac.'),
    tile('daFont 04', 'Use It in Photoshop', 'If Photoshop was open, quit and reopen it so it sees the new font. Pick the <strong>Type tool</strong> and find your font in the font menu.'),
]
adobe_steps = [
    tile('Adobe 01', 'Open Adobe Fonts', 'Go to <strong>fonts.adobe.com</strong> and sign in with your school Adobe account, the same one you use for Photoshop.'),
    tile('Adobe 02', 'Find a Font', 'Browse or search for a font that fits your scary mood. Use the filters for a bold or display style.'),
    tile('Adobe 03', 'Activate It', 'Open the font family and turn on the <strong>Add font</strong> toggle. Adobe installs it for you, with no download.'),
    tile('Adobe 04', 'Use It in Photoshop', 'Back in Photoshop, pick the <strong>Type tool</strong> and find your activated font in the font menu. It shows a small cloud icon.'),
]
page(
    'movieposter-step03-design.html',
    'Step 3: Design | Movie Poster | Digital Arts 1A | Mark Richardson Center',
    'Step 3',
    [('movieposter-step02-capture.html', '&#8592; Step 2'), ('movieposter-step04-reflection.html', 'Step 4 &#8594;')],
    'mrc-movieposter-step03-design-canvas.html',
    'Movie Poster &nbsp;&bull;&nbsp; Step 3', 'Build Your Poster',
    'Design it like the real thing.',
    [
        card('SET UP YOUR POSTER / 01 / 06', 'Start a New File',
             para('Open Photoshop. Go to <strong>File &gt; New</strong> and make a tall (portrait) poster, about <strong>11 by 17 inches</strong>, RGB color, 300 ppi.')
             + para('Place your <strong>protagonist</strong> as the main image and let it <strong>bleed</strong> to the edges. Bring in your <strong>antagonist</strong> (villain or monster) too, looming or in shadow, so both are clear at a glance. Darken the background so it feels moody, and save as a <strong>.PSD</strong> in your project folder.'),
             floatimg(IMG + 'movieposter-design-float.png', 'Ricardo Gomez designing a dark, moody movie poster in Photoshop at an iMac in the MRC lab')),
        card('GET YOUR FONTS / 02 / 06', 'Find and Install a Font',
             para('Your title needs the right font. You have two places to get one: '
                  '<a href="https://www.dafont.com" style="color:#eda268;text-decoration:underline;"><strong>dafont.com</strong></a> (free downloads) and '
                  '<a href="https://fonts.adobe.com" style="color:#eda268;text-decoration:underline;"><strong>Adobe Fonts</strong></a> (built into your Adobe account). Here is how to use each.')
             + para('<strong>Option A: dafont.com</strong>, download and install:')
             + scrollrow(dafont_steps)
             + para('<strong>Option B: Adobe Fonts</strong>, activate with no download:')
             + scrollrow(adobe_steps)
             + notecard('TIP', 'Match the Mood', 'Scary movies love rough, sharp, or hand-drawn fonts. Pick one that feels like your story, then make it big in the next step.')),
        card('DESIGN THE TITLE TREATMENT / 03 / 06', 'Make the Title',
             para('Your movie title is the star. Using the font you just installed, make it big and bold, usually near the <strong>bottom</strong> of the poster.')
             + para('Add a soft glow, a rough edge, or a shadow so the title stands out against the dark image.')),
        card('ADD YOUR WORDS / 04 / 06', 'Tagline, Credits, and Rating',
             para('Use the <strong>Type tool</strong> to add the rest of the words. Scroll through each pointer.')
             + scrollrow(words)),
        card('SET THE MOOD / 05 / 06', 'Turn Day into Night',
             para('You shot in the daytime, so now make it <strong>night</strong>. First swap the bright sky: go to <strong>Edit &gt; Sky Replacement</strong> and pick a dark, stormy, or night sky. This is the biggest step from day to night.')
             + para('Then grade the whole poster with the <strong>Camera Raw Filter</strong> (<strong>Filter &gt; Camera Raw Filter</strong>): lower the brightness, cool the colors toward blue, deepen the shadows, and add a <strong>vignette</strong> around the edges.')
             + para('Blend in your <strong>supporting images</strong> for fog or texture. The whole poster should feel cold and tense, like a real horror one-sheet.')),
        card('SAVE AND SUBMIT / 06 / 06', 'Save as JPG and Submit',
             para('When your poster is done, flatten it with <strong>Layer &gt; Flatten Image</strong>. Keep a PSD only if you want one.')
             + para('Turn in a <strong>JPG</strong>, not a PSD. Use <strong>File &gt; Save a Copy</strong>, choose <strong>JPG</strong>, full size. Name it:')
             + fname('FirstName LastInitial - Movie Poster.jpg')
             + para('Submit your finished poster JPG to Step 3 in Canvas.')),
    ],
)

# =========================================================================
# PAGE 5 — STEP 04 REFLECTION
# =========================================================================
questions = [
    tile('Question 01', 'Your Concept', 'Which concept did you choose or pitch, and what makes it scary?'),
    tile('Question 02', 'Working Together', 'This was your first project with a partner. How did teaming up on the concept help you, and what was tricky about working together?'),
    tile('Question 03', 'Off-Camera Light', 'This was your first time using an off-camera flash to light a shot. How did the flash change your photo, and what did you learn about lighting?'),
    tile('Question 04', 'Day to Night', 'How did you turn your daytime photo into a scary night scene? What did you change in Photoshop?'),
    tile('Question 05', 'The Trailer', 'If your movie were real, what would the trailer show? Would you watch it?'),
]
page(
    'movieposter-step04-reflection.html',
    'Step 4: Reflection | Movie Poster | Digital Arts 1A | Mark Richardson Center',
    'Step 4',
    [('movieposter-step03-design.html', '&#8592; Step 3')],
    'mrc-movieposter-step04-reflection-canvas.html',
    'Movie Poster &nbsp;&bull;&nbsp; Step 4', 'Reflection',
    'Look back at your poster.',
    [
        card('ANSWER FIVE QUESTIONS / 01 / 02', 'Reflect on Your Work',
             para('A reflection helps you learn from your work. Open the <strong>reflection document</strong> in your project folder and answer all five questions in complete sentences.')
             + scrollrow(questions)),
        card('TURN IT IN / 02 / 02', 'Submit Your Reflection',
             para('The reflection document is inside your <strong>project folder</strong>. Type your answers, save the document, and name it:')
             + fname('FirstName LastInitial - Movie Poster Reflection.docx')
             + para('Upload your finished reflection to Step 4 in Canvas to complete the project.'),
             floatimg(IMG + 'movieposter-reflection-float.png', 'Ricardo Gomez holding a printed proof of his finished movie poster at the MRC lab')),
    ],
)

print('done')
