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
    # Canvas-safe responsive: a flex-wrap row (no CSS grid / @media, which Canvas strips), so on a
    # narrow view the pieces reflow onto their own centered lines instead of overlapping. The title
    # uses clamp() so it shrinks on small widths. The language toggle matches the site's glass style.
    hicon_img=(f'<img src="{hicon}" alt="" style="width:40px;height:40px;display:block;flex:0 0 auto;" />' if hicon else '')
    es_btn=(f'<a href="{es_href}" style="display:inline-flex;align-items:center;background:rgba(0,0,0,0.40);'
      'border:1px solid #00b8b8;color:#a9f2f2;text-decoration:none;padding:8px 16px;font-family:Arial,sans-serif;'
      'font-size:10pt;letter-spacing:0.09em;text-transform:uppercase;white-space:nowrap;">'
      f'<strong>{es_label}</strong></a>')
    return ('<div style="background:linear-gradient(135deg,#000000 0%,#003838 40%,#007474 100%);padding:20px 28px 22px;margin:-28px -28px 24px -28px;">'
      '<div style="display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:12px 18px;">'
      f'<img src="{SITE}/assets/PV%20LOGO%20NEW.png" alt="Pioneer Valley High School Logo" style="width:clamp(54px,12vw,84px);height:auto;display:block;flex:0 0 auto;" />'
      '<div style="flex:1 1 240px;min-width:200px;text-align:center;">'
      f'<div style="margin-bottom:6px;"><span style="font-size:13pt;color:#80e0e0;"><strong>{label}</strong></span></div>'
      f'<div style="color:#ffffff;font-size:clamp(17pt,4.5vw,23pt);line-height:1.1;"><strong>{title}</strong></div>'
      f'<div style="color:rgba(255,255,255,0.82);margin-top:6px;"><span style="font-size:12.5pt;font-style:italic;"><strong>{subtitle}</strong></span></div></div>'
      f'<div style="flex:0 0 auto;display:flex;align-items:center;gap:12px;">{hicon_img}{es_btn}</div>'
      '</div></div>')

# White header-crown icons (module-type identity in the banner). Rendered from the SVG masters.
HICON_PHOTO_WALK=f"{SITE}/assets/Icons/assignment/photo-walk-white-v1.png"
HICON_YOUR_DEVICE=f"{SITE}/assets/Icons/assignment/your-device-white-v1.png"

# Camera-settings panel (red camera-kit modules): the on-screen settings mimic + its teaching
# section. quality="RAW" or "JPG" swaps only the Image Quality badge. Canvas-safe fixed 3-col table:
# the box border/fill lives on each <td> so row-equalization makes the boxes equal height, and
# border-spacing gives an even margin around every box. Values from Chris's PSD: shutter 1/500 (the
# one students adjust), aperture F6.3, ISO 100, light meter balanced.
CAMSET_ICON=f"{SITE}/assets/Icons/assignment/camera-settings-v1.svg"
RAW_BADGE=f"{SITE}/assets/Icons/assignment/raw-v2.png"
JPG_BADGE=f"{SITE}/assets/Icons/assignment/jpg-v2.svg"

def capture_panel(quality="RAW"):
    red="#f90101"
    boxtd=(f'border:2px solid {red};background:rgba(0,0,0,0.55);box-sizing:border-box;'
           'text-align:center;vertical-align:top;padding:14px 12px 16px;')
    def label(t):
        return (f'<div style="font-family:Arial,sans-serif;font-size:9.5pt;letter-spacing:0.14em;'
                f'text-transform:uppercase;color:{red};line-height:1.25;"><strong>{t}</strong></div>')
    def val(v):
        return (f'<div style="font-family:Arial,sans-serif;font-size:24pt;color:#ffffff;line-height:1.05;'
                f'margin-top:9px;"><strong>{v}</strong></div>')
    tag=(f'<div style="position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:{red};'
         'color:#ffffff;font-family:Arial,sans-serif;font-size:8pt;letter-spacing:0.1em;text-transform:uppercase;'
         'padding:3px 10px;white-space:nowrap;"><strong>Change this</strong></div>')
    sub=('<div style="font-family:Arial,sans-serif;font-size:10.5pt;color:#ffb0b0;margin-top:8px;'
         'line-height:1.3;">adjust to balance the light meter</div>')
    shutter=f'{tag}{label("Shutter")}{val("1/500")}{sub}'
    labels13=["-3","","-2","","-1","","0","","+1","","+2","","+3"]
    tickcols=""; numcols=""
    for i in range(13):
        tall=(i%2==0); h="17px" if tall else "9px"; c="#ffffff" if tall else "rgba(255,255,255,0.35)"
        tickcols+=(f'<div style="flex:1;text-align:center;"><span style="display:inline-block;width:2px;'
                   f'height:{h};background:{c};"></span></div>')
        n=labels13[i]; inner=(f'<strong>{n}</strong>' if n else '&nbsp;')
        numcols+=(f'<div style="flex:1;text-align:center;font-family:Arial,sans-serif;font-size:9pt;'
                  f'color:rgba(255,255,255,0.65);">{inner}</div>')
    meter=(f'{label("Light Meter")}'
      f'<div style="display:flex;align-items:flex-end;height:19px;margin-top:11px;">{tickcols}</div>'
      f'<div style="display:flex;margin-top:5px;">{numcols}</div>'
      '<div style="text-align:center;margin-top:9px;"><span style="display:inline-block;width:0;height:0;'
      'border-left:8px solid transparent;border-right:8px solid transparent;border-bottom:11px solid #26de78;"></span></div>'
      '<div style="text-align:center;margin-top:6px;font-family:Arial,sans-serif;font-size:9pt;'
      'letter-spacing:0.12em;text-transform:uppercase;color:#26de78;"><strong>Balanced (outdoors)</strong></div>')
    badge=RAW_BADGE if quality=="RAW" else JPG_BADGE
    qalt="RAW image-capture format" if quality=="RAW" else "JPG image-capture format"
    iq=(f'{label("Image Quality")}'
        f'<img src="{badge}" alt="{qalt}" style="height:68px;width:auto;display:block;margin:18px auto 0;" />')
    return (f'<div style="background:linear-gradient(180deg,#0c1010 0%,#050707 100%);border:1px solid rgba(249,1,1,0.35);'
      'padding:0;box-sizing:border-box;max-width:520px;margin:0 auto;">'
      '<table style="width:100%;border-collapse:separate;border-spacing:14px;table-layout:fixed;"><tbody>'
      f'<tr><td style="{boxtd}position:relative;">{shutter}</td><td style="{boxtd}">{label("Aperture")}{val("F6.3")}</td>'
      f'<td style="{boxtd}">{label("ISO")}{val("100")}</td></tr>'
      f'<tr><td colspan="2" style="{boxtd}">{meter}</td><td style="{boxtd}">{iq}</td></tr>'
      '</tbody></table></div>')

def camera_settings_section(es, quality="RAW"):
    red="#f90101"
    if es:
        title="Ajustes de C&aacute;mara"; lead="Usa estos ajustes para esta caminata. El &uacute;nico ajuste que cambias es la velocidad del obturador, para equilibrar el expos&iacute;metro."
        note_t="Solo cambia el obturador. Si afuera est&aacute; muy brillante, sube la velocidad del obturador. Si est&aacute; muy oscuro, b&aacute;jala, hasta que el expos&iacute;metro quede equilibrado. Adentro, con estos ajustes, el expos&iacute;metro marcar&aacute; subexpuesto y la imagen se ver&aacute; negra: eso es normal. Afuera quedar&aacute; mucho m&aacute;s cerca."
    else:
        title="Camera Settings"; lead="Use these settings for this photo walk. The only setting you change is the shutter speed, to balance the light meter."
        note_t="Change only the shutter. If it is too bright outside, raise the shutter speed. If it is too dark, lower it, until the light meter is balanced. Indoors, with these settings, the light meter will read underexposed and the image will look black: that is expected. Outside it will be much closer."
    hdr=(f'<div style="display:inline-flex;align-items:center;gap:12px;background:rgba(0,0,0,0.40);border-left:5px solid {red};padding:9px 18px 9px 12px;margin-bottom:12px;max-width:100%;box-sizing:border-box;">'
      f'<img src="{CAMSET_ICON}" alt="" style="width:44px;height:44px;display:block;flex:0 0 auto;" />'
      f'<span style="font-family:Arial,sans-serif;font-size:17pt;color:#ff8f8f;letter-spacing:0.01em;line-height:1.15;"><strong>{title}</strong></span></div>'
      f'<div style="height:2px;background:{red};width:60px;margin-bottom:18px;"></div>')
    lead_html=f'<div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{lead}</span></div>'
    note_box=f'<div style="background:rgba(249,1,1,0.10);border:1px solid rgba(249,1,1,0.30);border-left:4px solid {red};padding:11px 14px;margin:14px 0 0;font-size:12pt;color:rgba(255,255,255,0.92);line-height:1.55;">{note_t}</div>'
    return (f'<div style="background:linear-gradient(180deg,rgba(249,1,1,0.06) 0%,rgba(249,1,1,0.02) 100%);border:1px solid rgba(249,1,1,0.26);border-left:6px solid {red};padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      '<div style="display:flex;flex-wrap:wrap;align-items:flex-start;gap:18px 30px;">'
      f'<div style="flex:1 1 300px;min-width:0;">{hdr}{lead_html}{note_box}</div>'
      f'<div style="flex:1 1 380px;min-width:300px;">{capture_panel(quality)}</div>'
      '</div></div>')

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
STANDARDS_ICON=f"{SITE}/assets/Icons/assignment/standards-v1.svg"
CAPFMT_ICON={"jpg":f"{SITE}/assets/Icons/assignment/jpg-v2.svg","raw":f"{SITE}/assets/Icons/assignment/raw-v2.png"}  # v2 = transparent interior
CAMSET_ICON=f"{SITE}/assets/Icons/assignment/camera-settings-v1.svg"  # red aperture = camera-settings family marker

def section_header(icon,title,accent,light):
    # COMBINED section header (LOCKED 2026-09-10): one dark rectangle holding the section icon
    # + one big color-coded title, then the short accent rule under it.
    return ('<div style="display:inline-flex;align-items:center;gap:12px;background:rgba(0,0,0,0.40);'
      f'border-left:5px solid {accent};padding:9px 18px 9px 12px;margin-bottom:12px;max-width:100%;box-sizing:border-box;">'
      f'<img src="{icon}" alt="" style="width:44px;height:44px;display:block;flex:0 0 auto;" />'
      f'<span style="font-family:Arial,sans-serif;font-size:17pt;color:{light};letter-spacing:0.01em;line-height:1.15;"><strong>{title}</strong></span></div>'
      f'<div style="height:2px;background:{accent};width:60px;margin-bottom:18px;"></div>')

def capture_format(fmt, es=False):
    # Capture-format classifier: the JPG or RAW badge + "Image Capture" label, so students know which
    # format to capture in for this assignment. Section-header-style chip, goes right after the banner
    # on the capture step. Red left-border (#E62429) matches the badge; the icon is a wide format badge.
    icon=CAPFMT_ICON[fmt]
    label="Captura de Imagen" if es else "Image Capture"
    return ('<div style="display:inline-flex;align-items:center;gap:13px;background:rgba(0,0,0,0.40);border-left:5px solid #E62429;padding:8px 18px 8px 12px;margin-bottom:20px;max-width:100%;box-sizing:border-box;">'
      f'<img src="{icon}" alt="{fmt.upper()} image-capture format" style="height:40px;width:auto;display:block;flex:0 0 auto;" />'
      f'<span style="font-family:Arial,sans-serif;font-size:11pt;letter-spacing:0.14em;text-transform:uppercase;color:#ffffff;line-height:1.2;"><strong>{label}</strong></span></div>')

def capture_note(fmt, text, es=False):
    # RED camera-settings callout, highlighted like note() but RED (red = camera settings, LOCKED
    # 2026-09-16). Carries the JPG/RAW capture-format icon inline and lives INSIDE the content section
    # that talks about capturing (not a standalone chip at the top). Use it for a single setting like
    # "capture in JPG"; when a module needs many camera settings, break them into their own section.
    label="Captura de Imagen" if es else "Image Capture"
    # Inline format badge: put a {fmt} token in `text` where the JPG/RAW badge should sit.
    badge=(f'<img src="{CAPFMT_ICON[fmt]}" alt="{fmt.upper()}" '
      'style="height:1.87em;width:auto;vertical-align:middle;margin:0 3px;display:inline-block;" />')
    body=text.replace("{fmt}", badge)
    return ('<div style="display:flex;align-items:center;gap:13px;background:rgba(230,36,41,0.10);'
      'border:1px solid rgba(230,36,41,0.34);border-left:4px solid #E62429;padding:10px 14px;margin:12px 0;">'
      f'<img src="{CAMSET_ICON}" alt="Camera settings" style="height:34px;width:34px;display:block;flex:0 0 auto;" />'
      f'<span style="font-size:12pt;color:rgba(255,255,255,0.92);line-height:1.5;">'
      f'<strong style="letter-spacing:0.05em;text-transform:uppercase;">{label}:</strong> {body}</span></div>')

FLOAT_RE=re.compile(r'<!--FLOAT-->(.*?)<!--/FLOAT-->', re.S)
def _hoist(inner):
    # pull any FLOAT-marked block out of inner so the card can place it in the thumbnail column
    floats="".join(FLOAT_RE.findall(inner))
    return floats, FLOAT_RE.sub("", inner)

def _lay(box_open, chip, inner, floatimg):
    # Card body layout.
    #  - A CONTENT photo (float_right, hoisted) becomes a TRUE right-floated block at ~half card
    #    width: the title chip and body text wrap beside it AND then fill the full width once past
    #    the image bottom (magazine wrap), instead of being trapped in a narrow left column.
    #    `.silva-cfloat` (silva-module.css) drops it to full width under 640px. Bordered callouts
    #    (note/note_orange) carry overflow:hidden so they form a BFC and never slide under the float.
    #  - A resource THUMBNAIL (floatimg: slide deck cover / install video) keeps the compact
    #    two-column flex row, which drops below the text when the page gets narrow (flex-wrap).
    hf, inner = _hoist(inner)
    if hf:
        return (box_open
          + f'<div class="silva-cfloat">{hf}</div>'
          + chip + inner + '</div>')
    if floatimg:
        return (box_open
          + '<div style="display:flex;flex-wrap:wrap;align-items:flex-start;gap:16px 30px;">'
          + f'<div style="flex:1 1 320px;min-width:0;">{chip}{inner}</div>'
          + f'<div style="flex:0 1 360px;">{floatimg}</div>'
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
            f'<span style="flex:0 0 auto;width:26px;height:26px;background:{accent};color:#ffffff;font-size:12pt;line-height:26px;text-align:center;"><strong>{i}</strong></span>'
            f'<span style="font-size:13.5pt;color:rgba(255,255,255,0.88);line-height:1.5;">{body}</span></div>')
    return f'<div style="margin:4px 0 6px;">{r}</div>'

def note_orange(t):
    # ORANGE alert box. Reserve for the own-device fresh-photos integrity notice.
    # overflow:hidden = its own BFC, so it never slides under a right-floated content photo.
    return (f'<div style="background:rgba(255,107,26,0.10);border:1px solid rgba(255,107,26,0.30);border-left:4px solid #FF6B1A;padding:11px 14px;margin:8px 0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def note(t):
    # TEAL note: a callout INSIDE a teal content card, so it matches the section color (cohesion).
    # overflow:hidden = its own BFC, so it never slides under a right-floated content photo.
    return (f'<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.30);border-left:4px solid #00b8b8;padding:11px 14px;margin:8px 0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def framed(src,alt):
    return (f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;margin:6px 0 4px;">'
      f'<img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>')

def float_right(src,alt,cap=""):
    # Teal-framed content photo. FLOAT-marked so a card hoists it into the thumbnail column
    # (top-aligned with the title chip, drops below when narrow). Caption is optional: with an
    # empty caption no caption line is emitted (no stray empty div under the image).
    capdiv=(f'<div style="font-size:10.5pt;color:#80e0e0;text-align:center;margin-top:6px;opacity:0.9;line-height:1.4;">{cap}</div>' if cap else '')
    return ('<!--FLOAT-->'
      f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;"><img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      + capdiv
      + '<!--/FLOAT-->')

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

def standards_box(es, aligns):
    # GREEN CTE-standards alignment. A collapsible bar (native <details>, like vocab_grid) that
    # expands to the CDE Model Curriculum Standards this module builds. Green #26de78 + the award
    # icon. Works on the linked/standalone module view; Canvas's paste sanitizer strips <details>,
    # same caveat as vocab. `aligns` = list of dicts: code, en_title/es_title, en_desc/es_desc,
    # en_tier/es_tier (optional). Green is the 5th accent (teal/orange/purple/gold/green-standards).
    title = "EST&Aacute;NDARES CTE" if es else "CTE STANDARDS"
    lead  = ("Toca para ver los est&aacute;ndares que construyes en este m&oacute;dulo." if es
             else "Tap to see the standards this module builds.")
    rows=""
    for a in aligns:
        t=a.get("es_title") if es else a.get("en_title")
        d=a.get("es_desc") if es else a.get("en_desc")
        tier=(a.get("es_tier") if es else a.get("en_tier")) or ""
        tiertag=(f'<span style="font-size:9pt;letter-spacing:0.1em;text-transform:uppercase;color:#7bf0a8;">{tier}</span>' if tier else "")
        rows+=('<div style="margin-bottom:12px;line-height:1.5;">'
          '<div style="display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;">'
          f'<span style="display:inline-block;background:#26de78;color:#04160c;font-size:9.5pt;font-weight:bold;letter-spacing:0.04em;padding:2px 8px;white-space:nowrap;">{a["code"]}</span>'
          f'<span style="font-size:12.5pt;color:#ffffff;"><strong>{t}</strong></span>{tiertag}</div>'
          f'<div style="font-size:11pt;color:rgba(255,255,255,0.82);margin-top:3px;">{d}</div></div>')
    # Summary is NOT display:flex, so the browser renders its OWN disclosure triangle on the LEFT,
    # pointing right when closed and rotating down when open, exactly like the vocab words. The
    # triangle inherits the summary's green color. Icon + label sit inline after it.
    # The title box is wrapped in an inline-flex COLUMN so the short accent rule sits directly
    # under it (identical to section_header, which every other section title box uses). The lead
    # ("Tap to see...") stays inline to the right. The <details>/<summary> disclosure behavior is
    # unchanged: the browser still draws its own triangle on the left of the summary.
    return ('<details class="silva-standards" style="background:linear-gradient(180deg,rgba(38,222,120,0.12) 0%,rgba(38,222,120,0.03) 100%);border:1px solid rgba(38,222,120,0.35);border-left:6px solid #26de78;margin-bottom:24px;overflow:hidden;">'
      '<summary style="padding:14px 18px;cursor:pointer;color:#26de78;line-height:1.2;">'
      '<span style="display:inline-flex;flex-direction:column;align-items:flex-start;vertical-align:middle;">'
      '<span style="display:inline-flex;align-items:center;gap:12px;background:rgba(0,0,0,0.40);border-left:5px solid #26de78;padding:9px 18px 9px 12px;max-width:100%;box-sizing:border-box;">'
      f'<img src="{STANDARDS_ICON}" alt="" style="width:44px;height:44px;display:block;flex:0 0 auto;" />'
      f'<span style="font-family:Arial,sans-serif;font-size:17pt;color:#7bf0a8;letter-spacing:0.01em;line-height:1.15;"><strong>{title}</strong></span></span>'
      '<span style="display:block;height:2px;background:#26de78;width:60px;margin-top:12px;"></span>'
      '</span>'
      f'<span style="vertical-align:middle;font-size:12.5pt;color:rgba(255,255,255,0.92);margin-left:14px;">{lead}</span>'
      '</summary>'
      f'<div style="padding:8px 22px 22px;">{rows}</div></details>')

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
      <button class="silva-copy-btn silva-url-btn" onclick="silvaCopyURL()" aria-label="Copy this page URL to clipboard">&#128203; Copy URL</button>
      <button class="silva-copy-btn" onclick="silvaCopyHTML()" aria-label="Copy Canvas HTML to clipboard">&#128203; Copy Canvas HTML</button>
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
    function silvaCopyURL() {{ navigator.clipboard.writeText(location.href).then(function(){{var b=document.querySelector('.silva-url-btn');b.textContent='\\u2713 Copied!';b.classList.add('copied');setTimeout(function(){{b.innerHTML='&#128203; Copy URL';b.classList.remove('copied');}},2500);}}).catch(function(){{alert('Copy failed. Copy the address bar manually.');}}); }}
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
