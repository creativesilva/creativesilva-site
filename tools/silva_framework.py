#!/usr/bin/env python3
# Silva Angular Framework - shared chrome for every Canvas module builder.
# One source of truth for the visual system so all modules stay identical:
# combined chip headers, four-color accent system (teal content / orange Downloads /
# purple Resources / gold Deliverables), section cohesion, step-check content icon,
# collapsible 2-column vocab, float-right images that top-align and drop below when narrow.
# Builders do `from silva_framework import *`, keep their own module constants, content
# functions, downloads_block (their files), nav breadcrumb, dots, and the build/ban-guard loop.
# See SILVA_ANGULAR_FRAMEWORK.md section 3.5.
import re

SITE="https://www.creativesilva.com"

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"&ndash;","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

def banner(label,title,subtitle,es_href,es_label,hicon=""):
    # hicon: optional WHITE module-type icon shown on the RIGHT, left of the language toggle.
    # Used on photo-walk modules (white photo-walk icon) and own-device modules (white your-device).
    hicon_img=(f'<img src="{hicon}" alt="" style="width:44px;height:44px;display:block;flex:0 0 auto;" />' if hicon else '')
    return ('<div style="background:linear-gradient(135deg,#000000 0%,#003838 40%,#007474 100%);padding:20px 28px 22px;margin:-28px -28px 24px -28px;">'
      '<div style="display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;gap:16px;">'
      f'<div style="justify-self:start;"><img src="{SITE}/assets/PV%20LOGO%20NEW.png" alt="Pioneer Valley High School Logo" style="width:min(90px,15vw);height:auto;display:block;" /></div>'
      '<div style="justify-self:center;text-align:center;">'
      f'<div style="margin-bottom:6px;"><span style="font-size:13pt;color:#80e0e0;"><strong>{label}</strong></span></div>'
      f'<div style="color:#ffffff;font-size:23pt;line-height:1.1;"><strong>{title}</strong></div>'
      f'<div style="color:rgba(255,255,255,0.82);margin-top:6px;"><span style="font-size:13pt;font-style:italic;"><strong>{subtitle}</strong></span></div></div>'
      f'<div style="justify-self:end;display:flex;align-items:center;gap:14px;">{hicon_img}<a href="{es_href}" style="background:rgba(255,255,255,0.92);color:#003838;text-decoration:none;padding:7px 16px;display:inline-block;font-size:11pt;white-space:nowrap;border-top:2px solid #00b8b8;"><strong>{es_label}</strong></a></div>'
      '</div></div>')

# White header-crown icons (module-type identity in the banner). Rendered from the SVG masters.
HICON_PHOTO_WALK=f"{SITE}/assets/Icons/assignment/photo-walk-white-v1.png"
HICON_YOUR_DEVICE=f"{SITE}/assets/Icons/assignment/your-device-white-v1.png"

SLIDE_PLACEHOLDER=f"{SITE}/assets/images/shared/slide-deck-placeholder-v1.jpg"
def slide_deck_thumb(pdf_url, es, thumb=None, cap=None):
    # Click-to-open PDF slide deck: a purple cover thumbnail linking to the hosted PDF, which opens
    # as a standalone page in a new tab (native browser PDF viewer handles reading + download).
    # Every module's slide deck uses this. thumb defaults to the shared placeholder until Chris
    # supplies a real cover thumbnail.
    thumb = thumb or SLIDE_PLACEHOLDER
    alt = ("Portada de la presentaci&oacute;n (PDF)" if es else "Slide deck cover (PDF)")
    cap = cap or ("Haz clic para abrir la presentaci&oacute;n. Se abre como PDF en una pesta&ntilde;a nueva, donde puedes verla en pantalla completa y descargarla." if es
                  else "Click to open the slide deck. It opens as a PDF in a new tab, where you can read it full screen and download it.")
    return purple_thumb(pdf_url, thumb, alt, cap)

CONTENT_ICON=f"{SITE}/assets/Icons/assignment/step-check-teal-v2.png"
TYPE_ICON={"overview":f"{SITE}/assets/Icons/assignment/overview-teal-v1.png",
  "photo-walk":f"{SITE}/assets/Icons/assignment/photo-walk-teal-v1.png",
  "edit":f"{SITE}/assets/Icons/assignment/edit-teal-v1.png",
  "reflection":f"{SITE}/assets/Icons/assignment/reflection-teal-v1.png"}
TEAL_BOX='<div style="background:linear-gradient(180deg,rgba(0,116,116,0.10) 0%,rgba(0,116,116,0.03) 100%);border:1px solid rgba(0,184,184,0.22);border-left:6px solid #00b8b8;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
RESICON=f"{SITE}/assets/Icons/assignment/resources-v1.png"
PURPLE_BOX='<div style="background:linear-gradient(180deg,rgba(139,92,246,0.10) 0%,rgba(139,92,246,0.03) 100%);border:1px solid rgba(139,92,246,0.28);border-left:6px solid #8b5cf6;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
DL_ICON=f"{SITE}/assets/Icons/assignment/downloads-v1.png"
DELIVER_ICON=f"{SITE}/assets/Icons/assignment/deliverables-v4.png"

def section_header(icon,title,accent,light):
    # COMBINED section header (LOCKED 2026-09-10): one dark rectangle holding the section icon
    # + one big color-coded title, then the short accent rule under it.
    return ('<div style="display:inline-flex;align-items:center;gap:12px;background:rgba(0,0,0,0.40);'
      f'border-left:5px solid {accent};padding:9px 18px 9px 12px;margin-bottom:12px;max-width:100%;box-sizing:border-box;">'
      f'<img src="{icon}" alt="" style="width:44px;height:44px;display:block;flex:0 0 auto;" />'
      f'<span style="font-family:Arial,sans-serif;font-size:17pt;color:{light};letter-spacing:0.01em;line-height:1.15;"><strong>{title}</strong></span></div>'
      f'<div style="height:2px;background:{accent};width:60px;margin-bottom:18px;"></div>')

FLOAT_RE=re.compile(r'<!--FLOAT-->(.*?)<!--/FLOAT-->', re.S)
def _hoist(inner):
    # pull any FLOAT-marked block out of inner so the card can place it in the thumbnail column
    floats="".join(FLOAT_RE.findall(inner))
    return floats, FLOAT_RE.sub("", inner)

def _lay(box_open, chip, inner, floatimg):
    # Card body layout. With a float image/thumbnail: a wrapping flex row of [text column: chip +
    # body] and [thumbnail column]. align-items:flex-start top-aligns the thumbnail with the title
    # chip; flex-wrap drops the thumbnail BELOW the text when the page is too narrow (never above).
    # Canvas preserves display:flex, so this survives paste. Without a float: chip then body.
    hf, inner = _hoist(inner)
    thumb = floatimg + hf
    if thumb:
        # A generated CONTENT photo (float_right, hoisted) is showcased at ~half the card width;
        # a resource THUMBNAIL (floatimg: slide deck / video) stays compact. Both drop below the
        # text when the page gets too narrow (flex-wrap).
        if hf:
            textcol='flex:1 1 44%;min-width:0;'; imgcol='flex:1 1 44%;min-width:300px;'
        else:
            textcol='flex:1 1 320px;min-width:0;'; imgcol='flex:0 1 360px;'
        return (box_open
          + '<div style="display:flex;flex-wrap:wrap;align-items:flex-start;gap:16px 30px;">'
          + f'<div style="{textcol}">{chip}{inner}</div>'
          + f'<div style="{imgcol}">{thumb}</div>'
          + '</div></div>')
    return box_open + chip + inner + '</div>'

def card(eyebrow,heading,inner,floatimg=""):
    return _lay(TEAL_BOX, section_header(CONTENT_ICON, heading, "#00b8b8", "#80e0e0"), inner, floatimg)

def type_card(kind,label,heading,inner,floatimg=""):
    # FIRST card of a page: teal chip [type icon + type label] then the card's own heading + content
    hd=(f'<div style="margin-bottom:14px;"><span style="font-size:18pt;color:#ffffff;"><strong>{heading}</strong></span></div>' if heading else '')
    return _lay(TEAL_BOX, section_header(TYPE_ICON[kind], label, "#00b8b8", "#80e0e0") + hd, inner, floatimg)

def resources_card(heading,inner,es=False,floatimg=""):
    # PURPLE Resources section: chip [gear icon + "Module Resource: <heading>"] + content.
    label=("Recurso del M&oacute;dulo: " if es else "Module Resource: ")+heading
    return _lay(PURPLE_BOX, section_header(RESICON, label, "#8b5cf6", "#c4b5fd"), inner, floatimg)

def para(t):
    return f'<div style="margin-bottom:14px;line-height:1.72;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{t}</span></div>'

def placeholder(label, minh=240):
    return (f'<div style="min-height:{minh}px;border:2px dashed rgba(0,184,184,0.45);background:rgba(0,184,184,0.06);'
      'display:flex;align-items:center;justify-content:center;text-align:center;padding:18px;margin:6px 0 4px;box-sizing:border-box;">'
      f'<span style="font-size:11pt;letter-spacing:0.16em;text-transform:uppercase;color:#80e0e0;line-height:1.5;">{label}</span></div>')

def folder_note(es, area):
    # Every orange downloads block tells students to make a module project folder and move their
    # files from Downloads into OneDrive > {area} > that folder. area = "Photography Folder" (Photo)
    # or "Digital Arts Folder" (Digital Arts).
    if es:
        return ('<div style="margin-top:16px;font-size:12pt;color:rgba(255,255,255,0.82);line-height:1.55;">'
          '<strong style="color:#ffb27c;">Mantente organizado:</strong> crea una carpeta nueva y ll&aacute;mala como este m&oacute;dulo. '
          'Cuando cada archivo termine de descargarse, mu&eacute;velo de tu carpeta de Descargas a '
          f'OneDrive &rarr; {area} &rarr; esa carpeta del proyecto para que todos tus archivos queden juntos.</div>')
    return ('<div style="margin-top:16px;font-size:12pt;color:rgba(255,255,255,0.82);line-height:1.55;">'
      '<strong style="color:#ffb27c;">Stay organized:</strong> make a new folder and name it after this module. '
      'As each file finishes downloading, move it out of your Downloads folder into '
      f'OneDrive &rarr; {area} &rarr; that project folder so all your files stay together.</div>')

def bullets(items):
    r=""
    for b,rest in items:
        inner=(f'<strong>{b}</strong> {rest}' if b else rest)
        r+=('<div style="margin-bottom:8px;line-height:1.55;"><span style="color:#00b8b8;">&bull;</span> '
            f'<span style="font-size:13.5pt;color:rgba(255,255,255,0.88);">{inner}</span></div>')
    return f'<div style="margin-bottom:6px;">{r}</div>'

def steps(items, accent="#00b8b8"):
    # Numbered how-to list. Badge inherits the parent section's accent (teal by default).
    r=""
    for i,(b,rest) in enumerate(items,1):
        body=(f'<strong>{b}</strong> {rest}' if b else rest)
        r+=('<div style="display:flex;align-items:flex-start;gap:12px;margin-bottom:12px;">'
            f'<span style="flex:0 0 auto;width:26px;height:26px;border-radius:50%;background:{accent};color:#ffffff;font-size:12pt;line-height:26px;text-align:center;"><strong>{i}</strong></span>'
            f'<span style="font-size:13.5pt;color:rgba(255,255,255,0.88);line-height:1.5;">{body}</span></div>')
    return f'<div style="margin:4px 0 6px;">{r}</div>'

def note_orange(t):
    # ORANGE alert box. Reserve for the own-device fresh-photos integrity notice.
    return (f'<div style="background:rgba(255,107,26,0.10);border:1px solid rgba(255,107,26,0.30);border-left:4px solid #FF6B1A;padding:11px 14px;margin:8px 0;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def note(t):
    # TEAL note: a callout INSIDE a teal content card, so it matches the section color (cohesion).
    return (f'<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.30);border-left:4px solid #00b8b8;padding:11px 14px;margin:8px 0;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def framed(src,alt):
    return (f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;margin:6px 0 4px;">'
      f'<img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>')

def float_right(src,alt,cap):
    # Teal-framed content photo. FLOAT-marked so a card hoists it into the thumbnail column
    # (top-aligned with the title chip, drops below when narrow).
    return ('<!--FLOAT-->'
      f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;"><img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      f'<div style="font-size:10.5pt;color:#80e0e0;text-align:center;margin-top:6px;opacity:0.9;line-height:1.4;">{cap}</div>'
      '<!--/FLOAT-->')

def purple_thumb(href,src,alt,cap):
    # Purple-framed clickable thumbnail for a Resources card (slide deck, install video); new tab.
    return (f'<a href="{href}" target="_blank" rel="noopener" style="display:block;background:linear-gradient(135deg,#8b5cf6 0%,rgba(139,92,246,0.08) 100%);padding:2px;">'
      f'<img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></a>'
      f'<div style="font-size:10.5pt;color:#c4b5fd;text-align:center;margin-top:6px;opacity:0.9;line-height:1.4;">{cap}</div>')

def dl_link(url,label,download=True,row=False):
    if download:
        mgn='margin:0;' if row else 'margin:0 10px 8px 0;'
        return (f'<a href="{url}" download style="display:inline-block;text-decoration:none;background:#FF6B1A;color:#ffffff;padding:11px 22px;border-top:2px solid #ffb27c;font-size:11pt;letter-spacing:0.04em;{mgn}"><strong>{label}</strong></a>')
    return (f'<a href="{url}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:10px 20px;border-top:2px solid #00b8b8;font-size:11pt;letter-spacing:0.04em;margin:0 10px 10px 0;"><strong>{label}</strong></a>')

def reslink(url,label):
    # External reference / read link, styled for a PURPLE Resources card (cream button, purple top
    # accent). Batch several under one resources_card when they belong to the same step.
    return (f'<a href="{url}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#2a1a4a;padding:10px 20px;border-top:2px solid #8b5cf6;font-size:11pt;letter-spacing:0.04em;margin:0 10px 10px 0;"><strong>{label}</strong></a>')

def dl_row(url,label):
    return ('<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:8px;">'
      f'<img src="{DL_ICON}" alt="" style="width:42px;height:42px;flex:0 0 auto;display:block;" />'
      + dl_link(url,label,row=True) + '</div>')

def vocab_grid(quiz_label, quiz_body, terms):
    # Key Words is a PURPLE Resource (vocab is technically a resource). Collapsible accordion: each
    # term is a native <details> the student taps to reveal the definition. TWO columns (flex-wrap)
    # on iPad/desktop, one column when narrow. Native <details>, no JS: works on the linked page
    # view. NOTE: Canvas's paste sanitizer strips <details>, so use it on LINKED modules.
    es = "Examen" in quiz_label
    hint = "Toca una palabra para abrir su significado." if es else "Tap a word to open its meaning."
    note_box=('<div style="background:rgba(139,92,246,0.10);border:1px solid rgba(139,92,246,0.30);border-left:4px solid #8b5cf6;padding:12px 16px;margin-bottom:14px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#c4b5fd;margin-bottom:5px;"><strong>{quiz_label}</strong></div>'
      f'<div style="font-size:12pt;color:rgba(255,255,255,0.90);line-height:1.5;">{quiz_body}</div></div>')
    hintline=f'<div style="font-size:10.5pt;color:#c4b5fd;margin-bottom:12px;opacity:0.9;">&#9662; {hint}</div>'
    items=""
    for n,(term,defn) in enumerate(terms,1):
        items+=('<details style="flex:1 1 45%;min-width:260px;background:linear-gradient(135deg,#8b5cf6 0%,rgba(139,92,246,0.08) 100%);padding:2px;">'
          '<summary style="background:linear-gradient(135deg,#241d3a 0,#241d3a 30px,#140f24 30px,#140f24 100%);padding:12px 14px;cursor:pointer;">'
          f'<span style="font-size:12pt;color:#c4b5fd;"><strong>{n:02d}</strong></span> '
          f'<span style="font-size:12.5pt;color:#ffffff;"><strong>{term}</strong></span></summary>'
          f'<div style="padding:12px 14px 8px;font-size:11pt;line-height:1.55;color:rgba(255,255,255,0.85);">{defn}</div>'
          '</details>')
    return note_box+hintline+f'<div style="display:flex;flex-wrap:wrap;gap:10px;align-items:flex-start;">{items}</div>'

def deliverables_box(es,items):
    # GOLD deliverables section, chip header (icon LEFT), at the TOP of the step. Opens with a
    # forecast, then the turn-in bullets.
    title="ENTREGABLES &middot; ENTR&Eacute;GALO" if es else "DELIVERABLES &middot; TURN IT IN"
    lead=("Trabaja cada tarea de esta p&aacute;gina para terminar bien este paso. Cada paso de este m&oacute;dulo tiene su propia calificaci&oacute;n, as&iacute; que entrega lo siguiente:" if es
          else "Work through every task on this page to finish this step the right way. Each step in this module gets its own grade, so turn in the work below:")
    lis=""
    for b,rest in items:
        lis+=('<div style="margin-bottom:6px;line-height:1.5;"><span style="color:#f5b301;">&bull;</span> '
              f'<span style="font-size:13pt;color:rgba(255,255,255,0.90);"><strong>{b}</strong> {rest}</span></div>')
    return ('<div style="background:linear-gradient(180deg,rgba(245,179,1,0.12) 0%,rgba(245,179,1,0.03) 100%);border:1px solid rgba(245,179,1,0.35);border-left:6px solid #f5b301;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DELIVER_ICON, title, "#f5b301", "#ffd166")
      + f'<div style="font-size:13pt;color:#ffffff;margin-bottom:10px;line-height:1.5;">{lead}</div>'
      + f'{lis}</div>')

def top_wrap(en,es):
    return ('<div id="top" style="width:100%;margin:0 auto;font-family:Arial,sans-serif;color:#ffffff;background-color:#080808;'
      "background-image:linear-gradient(180deg,rgba(8,8,8,0.97) 0%,rgba(0,56,56,0.94) 50%,rgba(8,8,8,0.97) 100%),"
      f"url('{SITE}/assets/PV_Panther_Watermark.png');"
      'background-position:center center,center center;background-repeat:no-repeat,no-repeat;background-attachment:fixed,fixed;overflow:hidden;">'
      '<div style="padding:28px 28px 40px;">'+en+'</div>'
      '<div id="espanol" style="border-top:2px solid rgba(255,255,255,0.10);"><div style="padding:28px 28px 40px;">'+es+'</div></div>'
      '</div>')

def dot(href,label,title,active,module=False):
    if active: return f'<span class="sdot sdot-active" title="{title}">{label}</span>'
    cls="sdot sdot-link sdot-module" if module else "sdot sdot-link"
    return f'<a href="{href}" class="{cls}" title="{title}">{label}</a>'

def wrap_page(title,nav_inner,top_html,bottom):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="icon" type="image/svg+xml" href="https://www.creativesilva.com/logos/CS_Logo_Only.svg" />
  <style>:root {{ --course-accent: #007474; }}</style>
  <link rel="stylesheet" href="/css/silva-module.css" />
</head>
<body>
  <nav class="silva-nav" aria-label="Module navigation">
    <div class="silva-nav-inner">
{nav_inner}
      <div class="silva-nav-div"></div>
      <button class="silva-copy-btn" onclick="silvaCopyHTML()" aria-label="Copy Canvas HTML to clipboard">&#128203; Copy Canvas HTML</button>
      <button class="silva-copy-btn silva-url-btn" onclick="silvaCopyURL()" aria-label="Copy this page URL to clipboard">&#128279; Copy URL</button>
      <button class="silva-download-btn" onclick="silvaDownloadHTML()" aria-label="Download Canvas HTML as file">&#128229; Download HTML</button>
    </div>
  </nav>
  <div class="silva-page">
  <div id="silva-module-content">
  {top_html}
  </div>
  {bottom}
  </div>
  <script>
    function silvaCopyHTML() {{ var el=document.getElementById('top'); navigator.clipboard.writeText(el.outerHTML).then(function(){{var b=document.querySelector('.silva-copy-btn');b.textContent='\\u2713 Copied!';b.classList.add('copied');setTimeout(function(){{b.innerHTML='&#128203; Copy Canvas HTML';b.classList.remove('copied');}},2500);}}).catch(function(){{alert('Copy failed. Select the source manually.');}}); }}
    function silvaDownloadHTML() {{ var el=document.getElementById('top'); var blob=new Blob([el.outerHTML],{{type:'text/html'}}); var url=URL.createObjectURL(blob); var a=document.createElement('a'); a.href=url; a.download=location.pathname.split('/').pop().replace('.html','')+'-canvas.html'; document.body.appendChild(a); a.click(); document.body.removeChild(a); URL.revokeObjectURL(url); }}
    function silvaCopyURL() {{ navigator.clipboard.writeText(location.href).then(function(){{var b=document.querySelector('.silva-url-btn');b.textContent='\\u2713 Copied!';b.classList.add('copied');setTimeout(function(){{b.innerHTML='&#128279; Copy URL';b.classList.remove('copied');}},2500);}}).catch(function(){{alert('Copy failed. Copy the address bar manually.');}}); }}
  </script>
  <script src="/js/silva-nav.js"></script>
</body>
</html>
'''

def ban_check(html, fname):
    # Shared guard: no em dashes, no violence words (manufacturer menu names like Canon's
    # "Shooting" menu are allowlisted). Call from each builder's write loop.
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    low=html.lower()
    for allow in ["shooting tab","shooting menu"]:
        low=low.replace(allow,"")
    for w in ["shoot","shooting","shot","shots","shoots","screenshot"]:
        assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
