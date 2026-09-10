#!/usr/bin/env python3
# Photography 1A - Module 04: Image Series Photo Walk.
# Intro to the workflow: capture a COHESIVE series with the classroom camera kit in RAW,
# offload to OneDrive, import into Lightroom Classic, build a 12-Up contact sheet; then cull
# to 6, do a light edit, and deliver a 6-Up contact sheet; then reflect.
# Dark teal angular framework. Overview + 3 steps, bilingual EN/ES, 5th-grade.
# Step 01 embeds the existing scrollable "Lightroom Import" slide deck (12 slides + PDF).
# HEADER is a PLACEHOLDER (Chris drops art in later).
import os, re
SITE="https://www.creativesilva.com"
ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
HEADER=f"{SITE}/assets/images/photo1/image-series/header-v1.png"   # overview header art
# shared with the Photo 2 Build-Your-Own-Preset module (same capture image, one hosted copy)
BEE=f"{SITE}/assets/images/photo2/build-your-own-preset/capture-float-v1.jpg"
EDIT_FLOAT=f"{SITE}/assets/images/photo1/image-series/edit-float-v1.jpg"  # step 2 editing image
LRC=f"{SITE}/assets/images/photo1/lrc-import"          # existing import slide deck images
SLIDE=LRC+"/lrc-slide-{:02d}.jpg"
SLIDE_PDF=f"{SITE}/assets/course-documents/Lightroom-Import-Guide.pdf"
CONTACT_ZIP=f"{SITE}/assets/PVHS_Contact_Sheet_Presets.zip"
REFLECT_EN=f"{SITE}/assets/course-documents/Image-Series-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Image-Series-Reflection-ES.docx"

OVER="photo1-image-series-overview.html"
S1="photo1-image-series-step01-capture-import.html"
S2="photo1-image-series-step02-cull-edit.html"
S3="photo1-image-series-step03-reflection.html"

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"&ndash;","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

def banner(label,title,subtitle,es_href,es_label):
    return ('<div style="background:linear-gradient(135deg,#000000 0%,#003838 40%,#007474 100%);padding:20px 28px 22px;margin:-28px -28px 24px -28px;">'
      '<div style="display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;gap:16px;">'
      f'<div style="justify-self:start;"><img src="{SITE}/assets/PV%20LOGO%20NEW.png" alt="Pioneer Valley High School Logo" style="width:min(90px,15vw);height:auto;display:block;" /></div>'
      '<div style="justify-self:center;text-align:center;">'
      f'<div style="margin-bottom:6px;"><span style="font-size:13pt;color:#80e0e0;"><strong>{label}</strong></span></div>'
      f'<div style="color:#ffffff;font-size:23pt;line-height:1.1;"><strong>{title}</strong></div>'
      f'<div style="color:rgba(255,255,255,0.82);margin-top:6px;"><span style="font-size:13pt;font-style:italic;"><strong>{subtitle}</strong></span></div></div>'
      f'<div style="justify-self:end;"><a href="{es_href}" style="background:rgba(255,255,255,0.92);color:#003838;text-decoration:none;padding:7px 16px;display:inline-block;font-size:11pt;white-space:nowrap;border-top:2px solid #ff6b1a;"><strong>{es_label}</strong></a></div>'
      '</div></div>')

def card(eyebrow,heading,inner):
    return ('<div style="background:linear-gradient(180deg,rgba(0,116,116,0.10) 0%,rgba(0,116,116,0.03) 100%);border:1px solid rgba(0,184,184,0.22);border-left:6px solid #00b8b8;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      '<div style="display:inline-block;background:rgba(0,0,0,0.40);border-left:3px solid #00b8b8;padding:5px 12px 5px 10px;font-family:Arial,sans-serif;font-size:10pt;letter-spacing:0.22em;color:#80e0e0;text-transform:uppercase;margin-bottom:12px;">'
      f'<strong>{eyebrow}</strong></div>'
      f'<div style="margin-bottom:8px;"><span style="font-size:20pt;color:#ffffff;"><strong>{heading}</strong></span></div>'
      '<div style="height:2px;background:#00b8b8;width:60px;margin-bottom:18px;"></div>'
      f'{inner}</div>')

def para(t):
    return f'<div style="margin-bottom:14px;line-height:1.72;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{t}</span></div>'

def placeholder(label, minh=240):
    # dashed hero placeholder; swap to framed(HEADER,...) when the art is dropped in
    return (f'<div style="min-height:{minh}px;border:2px dashed rgba(0,184,184,0.45);background:rgba(0,184,184,0.06);'
      'display:flex;align-items:center;justify-content:center;text-align:center;padding:18px;margin:6px 0 4px;box-sizing:border-box;">'
      f'<span style="font-size:11pt;letter-spacing:0.16em;text-transform:uppercase;color:#80e0e0;line-height:1.5;">{label}</span></div>')

def downloads_block(es):
    # CANONICAL orange downloads section, right after the intro/header card. This module
    # holds the reflection AND the contact sheet templates (first module to introduce them).
    eyebrow="DESCARGAS" if es else "DOWNLOADS"
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga aqu&iacute; todo lo que necesitas para este m&oacute;dulo. Consigue tus archivos antes de empezar." if es
          else "Download everything you need for this module here. Get your files before you start.")
    reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
    cslabel=("Plantillas de Hoja de Contactos (12 y 6, ZIP)" if es else "Contact Sheet Templates (12-Up &amp; 6-Up, ZIP)")
    ref=REFLECT_ES if es else REFLECT_EN
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      '<div style="display:inline-block;background:rgba(0,0,0,0.40);border-left:3px solid #FF6B1A;padding:5px 12px 5px 10px;font-family:Arial,sans-serif;font-size:10pt;letter-spacing:0.22em;color:#ffb27c;text-transform:uppercase;margin-bottom:12px;">'
      f'<strong>{eyebrow}</strong></div>'
      f'<div style="margin-bottom:8px;"><span style="font-size:20pt;color:#ffffff;"><strong>{heading}</strong></span></div>'
      '<div style="height:2px;background:#FF6B1A;width:60px;margin-bottom:18px;"></div>'
      f'{para(lead)}{dl_row(ref,reflabel)}'
      f'<div style="margin-top:10px;">{dl_row(CONTACT_ZIP,cslabel)}</div></div>')

def bullets(items):
    r=""
    for b,rest in items:
        inner=(f'<strong>{b}</strong> {rest}' if b else rest)
        r+=('<div style="margin-bottom:8px;line-height:1.55;"><span style="color:#00b8b8;">&bull;</span> '
            f'<span style="font-size:13.5pt;color:rgba(255,255,255,0.88);">{inner}</span></div>')
    return f'<div style="margin-bottom:6px;">{r}</div>'

def steps(items):
    r=""
    for i,(b,rest) in enumerate(items,1):
        r+=('<div style="display:flex;align-items:flex-start;gap:12px;margin-bottom:12px;">'
            f'<span style="flex:0 0 auto;width:26px;height:26px;border-radius:50%;background:#FF6B1A;color:#ffffff;font-size:12pt;line-height:26px;text-align:center;"><strong>{i}</strong></span>'
            f'<span style="font-size:13.5pt;color:rgba(255,255,255,0.88);line-height:1.5;"><strong>{b}</strong> {rest}</span></div>')
    return f'<div style="margin:4px 0 6px;">{r}</div>'

def note_orange(t):
    return (f'<div style="background:rgba(255,107,26,0.10);border:1px solid rgba(255,107,26,0.30);border-left:4px solid #FF6B1A;padding:11px 14px;margin:8px 0;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def framed(src,alt):
    return (f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;margin:6px 0 4px;">'
      f'<img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>')

def float_right(src,alt,cap):
    return ('<div style="float:right;width:40%;min-width:230px;margin:0 0 14px 22px;">'
      f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;"><img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      f'<div style="font-size:10.5pt;color:#80e0e0;text-align:center;margin-top:6px;opacity:0.9;line-height:1.4;">{cap}</div></div>')

DL_ICON=f"{SITE}/assets/Icons/assignment/downloads-v1.png"

def dl_link(url,label,download=True,row=False):
    if download:
        mgn='margin:0;' if row else 'margin:0 10px 8px 0;'
        return (f'<a href="{url}" download style="display:inline-block;text-decoration:none;background:#FF6B1A;color:#ffffff;padding:11px 22px;border-top:2px solid #ffb27c;font-size:11pt;letter-spacing:0.04em;{mgn}"><strong>{label}</strong></a>')
    return (f'<a href="{url}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:10px 20px;border-top:2px solid #00b8b8;font-size:11pt;letter-spacing:0.04em;margin:0 10px 10px 0;"><strong>{label}</strong></a>')

def dl_row(url,label):
    return ('<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:8px;">'
      f'<img src="{DL_ICON}" alt="" style="width:42px;height:42px;flex:0 0 auto;display:block;" />'
      + dl_link(url,label,row=True) + '</div>')

def slide_deck(es):
    hint=('Scroll inside the window to see all 12 slides' if not es
          else 'Despl&aacute;zate en la ventana para ver las 12 diapositivas')
    pdf_lbl=('Download the Slides (PDF)' if not es else 'Descarga las Diapositivas (PDF)')
    alt_lbl=('Lightroom import, slide {} of 12' if not es
             else 'Importar a Lightroom, diapositiva {} de 12')
    imgs=""
    for i in range(1,13):
        imgs+=('<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;margin:0 0 12px;">'
               f'<img src="{SLIDE.format(i)}" alt="{alt_lbl.format(i)}" style="display:block;width:100%;height:auto;" /></div>')
    return ('<div style="margin-bottom:12px;">'
      f'<a href="{SLIDE_PDF}" download style="display:inline-block;background:#FF6B1A;color:#ffffff;text-decoration:none;padding:11px 22px;border-top:2px solid #ffb27c;font-size:11pt;letter-spacing:0.04em;"><strong>&#128229; {pdf_lbl}</strong></a></div>'
      f'<div style="font-size:11pt;color:#80e0e0;margin-bottom:8px;opacity:0.9;">&#8595; {hint}</div>'
      '<div class="silva-scroll" style="aspect-ratio:16/11;max-height:82vh;overflow-y:auto;-webkit-overflow-scrolling:touch;border:1px solid rgba(0,184,184,0.22);background:rgba(0,0,0,0.22);padding:8px;box-sizing:border-box;">'
      + imgs + '</div>')

def vocab_grid(quiz_label, quiz_body, terms):
    note=('<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.30);border-left:4px solid #00b8b8;padding:12px 16px;margin-bottom:18px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:5px;"><strong>{quiz_label}</strong></div>'
      f'<div style="font-size:12pt;color:rgba(255,255,255,0.90);line-height:1.5;">{quiz_body}</div></div>')
    cell=('<td style="width:33.33%;vertical-align:top;padding:6px;">'
      '<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;height:100%;box-sizing:border-box;">'
      '<div style="background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:16px;min-height:132px;height:100%;box-sizing:border-box;">'
      '<div style="font-size:12pt;color:#ffffff;margin-bottom:5px;"><strong>{term}</strong></div>'
      '<div style="font-size:10.5pt;line-height:1.5;color:rgba(255,255,255,0.80);">{defn}</div></div></div></td>')
    rows=""
    for i in range(0,len(terms),3):
        rows+='<tr>'+''.join(cell.format(term=t,defn=d) for t,d in terms[i:i+3])+'</tr>'
    return note+f'<table role="presentation" style="width:100%;border-collapse:collapse;table-layout:fixed;"><tbody>{rows}</tbody></table>'

def deliverables_box(title,lead,items):
    lis=""
    for b,rest in items:
        lis+=('<div style="margin-bottom:6px;line-height:1.5;"><span style="color:#FF6B1A;">&bull;</span> '
              f'<span style="font-size:13pt;color:rgba(255,255,255,0.90);"><strong>{b}</strong> {rest}</span></div>')
    return ('<div style="background:rgba(255,107,26,0.12);border:1px solid rgba(255,107,26,0.35);border-left:5px solid #FF6B1A;padding:16px 18px;margin:0 0 8px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#ffb27c;margin-bottom:8px;"><strong>{title}</strong></div>'
      f'<div style="font-size:13pt;color:#ffffff;margin-bottom:8px;"><strong>{lead}</strong></div>{lis}</div>')

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

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Image Series Photo Walk</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

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
  </script>
  <script src="/js/silva-nav.js"></script>
</body>
</html>
'''

DOTS_TITLES=[("M","Overview"),("1","Step 01"),("2","Step 02"),("3","Step 03")]
def dots_for(active_idx):
    hrefs=[OVER,S1,S2,S3]
    r=""
    for i,(lab,title) in enumerate(DOTS_TITLES):
        r+=dot("" if i==active_idx else hrefs[i], lab, title, i==active_idx, module=(i==0 and active_idx!=0))
    return r

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 1A &bull; Module 04","Image Series Photo Walk","Capture a cohesive series with the camera kit, offload, import, and edit.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("THE PROJECT / OVERVIEW","Capture a Series That Belongs Together",
        para("On this photo walk you use a classroom camera kit to capture a cohesive series: a group of photos that feel linked, like a family of images. Your series can be circles, shapes, colors, textures, reflections, or your own idea. What matters is that the photos clearly go together.")
        + para("You capture in RAW, offload your photos to OneDrive, and import them into Lightroom Classic. You build your first contact sheet, then cull to your best 6, do a light edit, and turn in a final contact sheet.")
        + framed(HEADER,"Image Series Photo Walk header: a row of linked photos that form one cohesive series"))
    en+=downloads_block(False)
    en+=card("THE CONCEPT / WHAT MAKES A SERIES","A Family of Images",
        float_right(BEE,"A Pioneer Valley student kneeling to photograph a pink flower with a bee, using a Canon camera in golden light in front of the PV campus","Capturing a natural-light series on campus.")
        + para("A series is more than a pile of photos. The images share something: the same subject, the same shapes, the same colors, or the same feeling. When someone looks at all of them together, they can tell the photos belong to each other.")
        + bullets([
            ("Pick one idea:","circles, shapes, colors, textures, reflections, or your own theme."),
            ("Keep it consistent:","repeat that idea across every photo so they feel linked."),
            ("Think like a set:","each photo is part of a group, not a one-off."),
        ]))
    en+=card("HOW IT WORKS / YOUR PLAN","Your Three Steps",
        steps([
            ("Capture &amp; Import:","set the camera to RAW, capture your cohesive series, offload to OneDrive, import into Lightroom Classic, and turn in a 12-image contact sheet."),
            ("Cull &amp; Edit:","pick your best 6, do a light edit (exposure, highlights, shadows, color temperature), and turn in a 6-image contact sheet."),
            ("Reflection:","tell the story of your series."),
        ])
        + note_orange("Capture in RAW, not JPG. Set your Canon EOS R50 to RAW before you start. Step 01 shows you how.")
        + note_orange("Capture your photos on purpose for this project. They must be new images you take on this walk, not pictures already in your camera roll from before."))
    en+=card("VOCABULARY / 6 TERMS","Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Series / Cohesive","A group of photos that belong together and feel like one family of images."),
           ("RAW","A high-quality photo file the camera saves with the most detail for editing."),
           ("OneDrive","The cloud storage where you offload and keep your photos safe."),
           ("Import","Bringing your photos into Lightroom Classic to organize and edit."),
           ("Contact Sheet","One page that shows all your photos as small thumbnails."),
           ("White Balance","The setting that makes colors look warm, cool, or true to life.")]))

    es=banner("Fotograf&iacute;a 1A &bull; M&oacute;dulo 04","Caminata de Serie de Im&aacute;genes","Captura una serie cohesiva con el kit de c&aacute;mara, desc&aacute;rgala, imp&oacute;rtala y edita.","#top","Back to English")
    es+=card("EL PROYECTO / RESUMEN","Captura una Serie Que Va Junta",
        para("En esta caminata fotogr&aacute;fica usas un kit de c&aacute;mara de la clase para capturar una serie cohesiva: un grupo de fotos que se sienten unidas, como una familia de im&aacute;genes. Tu serie puede ser de c&iacute;rculos, formas, colores, texturas, reflejos o tu propia idea. Lo importante es que las fotos claramente van juntas.")
        + para("Capturas en RAW, descargas tus fotos a OneDrive y las importas a Lightroom Classic. Creas tu primera hoja de contactos, luego eliges tus mejores 6, haces una edici&oacute;n ligera y entregas una hoja de contactos final.")
        + framed(HEADER,"Encabezado de la Caminata de Serie de Im&aacute;genes: una fila de fotos unidas que forman una serie cohesiva"))
    es+=downloads_block(True)
    es+=card("EL CONCEPTO / QU&Eacute; HACE UNA SERIE","Una Familia de Im&aacute;genes",
        float_right(BEE,"Una estudiante de Pioneer Valley arrodillada fotografiando una flor rosa con una abeja, con una c&aacute;mara Canon en luz dorada frente al campus de PV","Capturando una serie con luz natural en el campus.")
        + para("Una serie es m&aacute;s que un mont&oacute;n de fotos. Las im&aacute;genes comparten algo: el mismo tema, las mismas formas, los mismos colores o la misma sensaci&oacute;n. Cuando alguien las ve todas juntas, puede notar que las fotos van una con otra.")
        + bullets([
            ("Elige una idea:","c&iacute;rculos, formas, colores, texturas, reflejos o tu propio tema."),
            ("Mant&eacute;nla consistente:","repite esa idea en cada foto para que se sientan unidas."),
            ("Piensa como un grupo:","cada foto es parte de un conjunto, no una foto suelta."),
        ]))
    es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Tres Pasos",
        steps([
            ("Captura e Importa:","pon la c&aacute;mara en RAW, captura tu serie cohesiva, desc&aacute;rgala a OneDrive, imp&oacute;rtala a Lightroom Classic y entrega una hoja de contactos de 12 im&aacute;genes."),
            ("Selecciona y Edita:","elige tus mejores 6, haz una edici&oacute;n ligera (exposici&oacute;n, luces, sombras, temperatura de color) y entrega una hoja de contactos de 6 im&aacute;genes."),
            ("Reflexi&oacute;n:","cuenta la historia de tu serie."),
        ])
        + note_orange("Captura en RAW, no en JPG. Pon tu Canon EOS R50 en RAW antes de empezar. El Paso 01 te ense&ntilde;a c&oacute;mo.")
        + note_orange("Captura tus fotos a prop&oacute;sito para este proyecto. Deben ser im&aacute;genes nuevas que tomes en esta caminata, no fotos que ya ten&iacute;as en tu galer&iacute;a de antes."))
    es+=card("VOCABULARIO / 6 T&Eacute;RMINOS","Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Series / Cohesive (Serie / Cohesiva)","Un grupo de fotos que van juntas y se sienten como una familia de im&aacute;genes."),
           ("RAW","Un archivo de foto de alta calidad que la c&aacute;mara guarda con el mayor detalle para editar."),
           ("OneDrive","El almacenamiento en la nube donde descargas y guardas tus fotos a salvo."),
           ("Import (Importar)","Llevar tus fotos a Lightroom Classic para organizarlas y editarlas."),
           ("Contact Sheet (Hoja de Contactos)","Una p&aacute;gina que muestra todas tus fotos como miniaturas."),
           ("White Balance (Balance de Blancos)","El ajuste que hace que los colores se vean c&aacute;lidos, fr&iacute;os o reales.")]))

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Image Series Photo Walk | Photography 1A | PVHS", nav("Overview",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Image Series Photo Walk &bull; Step 1","Capture &amp; Import","Set RAW, capture your series, offload to OneDrive, and import.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("CAMERA SETUP / SET TO RAW","Set Your Camera to RAW First",
        para("This project must be captured in RAW, not JPG. RAW keeps the most detail so your edits look clean. Set your Canon EOS R50 to RAW before you take any photos.")
        + steps([
            ("Press MENU:","press the MENU button on the back of the camera."),
            ("Open the red Camera menu:","go to the red Camera tab (the camera icon) and choose Image quality."),
            ("Choose RAW:","set the image type to RAW."),
            ("Turn JPEG off:","set the JPEG option to the dash (&ndash;) so the camera saves RAW only, no JPG."),
            ("Save:","press SET to save, then tap the shutter halfway to close the menu."),
        ])
        + note_orange("If you are not sure, ask Mr. Silva to check your setting before you start."))
    en+=card("CAPTURE / ON THE WALK","Capture Your Cohesive Series",
        para("Now go capture your series with the camera kit. Pick one idea and repeat it so the photos feel like a family. Take at least 12 images so you have strong ones to choose from.")
        + bullets([
            ("Pick your idea:","circles, shapes, colors, textures, reflections, or your own theme."),
            ("At least 12 images:","capture more than you need for the series."),
            ("Keep it cohesive:","repeat your idea so every photo clearly belongs to the set."),
            ("Watch your framing:","fill the frame and keep your subject sharp."),
        ])
        + note_orange("Capture your photos on purpose for this project. They must be new images from this walk, not pictures already in your camera roll from before."))
    en+=card("OFFLOAD / SAVE TO ONEDRIVE","Offload Your Photos to OneDrive",
        para("When you finish, offload your RAW photos to OneDrive so they are safe and ready to import.")
        + steps([
            ("Put the card in the computer:","take the SD card out of the camera and put it in the computer&rsquo;s card reader. Ask Mr. Silva if you need the reader."),
            ("Make a project folder:","in your OneDrive, make a new folder for this project."),
            ("Copy your RAW files:","copy all your RAW photos from the card into that OneDrive folder."),
            ("Let it sync:","wait for OneDrive to finish syncing. The cloud icon turns to a check when it is done."),
        ]))
    en+=card("IMPORT / INTO LIGHTROOM","Import Into Lightroom Classic",
        para("Now import your series into Lightroom Classic. The slide deck below walks you through every click. Scroll through all 12 slides, and download the PDF if you want it open while you work.")
        + slide_deck(False))
    en+=card("CONTACT SHEET / SHOW YOUR SERIES","Make Your 12-Image Contact Sheet",
        para("A contact sheet is one page that shows all your photos as small thumbnails. Make yours with the 12-Up contact sheet layout in the Lightroom Classic Print module, then save it as a high-resolution JPG. The template is on this module&rsquo;s Overview page (marked M at the top).")
        + bullets([
            ("Select your images:","pick the photos from your imported series."),
            ("Use the 12-Up layout:","in the Print module, choose the 12-Up contact sheet."),
            ("Save the page:","export the contact sheet as a high-resolution JPG to turn in."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 contact sheet:","your 12-image contact sheet (high-resolution JPG), showing your imported series, uploaded to this Canvas assignment.")])

    es=banner("Caminata de Serie de Im&aacute;genes &bull; Paso 1","Captura e Importa","Pon RAW, captura tu serie, desc&aacute;rgala a OneDrive e imp&oacute;rtala.","#top","Back to English")
    es+=card("AJUSTE DE C&Aacute;MARA / PON RAW","Primero Pon Tu C&aacute;mara en RAW",
        para("Este proyecto debe capturarse en RAW, no en JPG. RAW guarda el mayor detalle para que tus ediciones se vean limpias. Pon tu Canon EOS R50 en RAW antes de tomar cualquier foto.")
        + steps([
            ("Presiona MENU:","presiona el bot&oacute;n MENU en la parte de atr&aacute;s de la c&aacute;mara."),
            ("Abre el men&uacute; rojo de C&aacute;mara:","ve a la pesta&ntilde;a roja de C&aacute;mara (Captura) y elige Calidad de imagen."),
            ("Elige RAW:","pon el tipo de imagen en RAW."),
            ("Apaga el JPEG:","pon la opci&oacute;n JPEG en el gui&oacute;n (&ndash;) para que la c&aacute;mara guarde solo RAW, sin JPG."),
            ("Guarda:","presiona SET para guardar, luego toca el disparador a la mitad para cerrar el men&uacute;."),
        ])
        + note_orange("Si no est&aacute;s seguro, pide al Sr. Silva que revise tu ajuste antes de empezar."))
    es+=card("CAPTURA / EN LA CAMINATA","Captura Tu Serie Cohesiva",
        para("Ahora ve a capturar tu serie con el kit de c&aacute;mara. Elige una idea y rep&iacute;tela para que las fotos se sientan como una familia. Toma al menos 12 im&aacute;genes para tener buenas opciones.")
        + bullets([
            ("Elige tu idea:","c&iacute;rculos, formas, colores, texturas, reflejos o tu propio tema."),
            ("Al menos 12 im&aacute;genes:","captura m&aacute;s de las que necesitas para la serie."),
            ("Mant&eacute;nla cohesiva:","repite tu idea para que cada foto claramente pertenezca al grupo."),
            ("Cuida el encuadre:","llena el cuadro y mant&eacute;n tu sujeto n&iacute;tido."),
        ])
        + note_orange("Captura tus fotos a prop&oacute;sito para este proyecto. Deben ser im&aacute;genes nuevas de esta caminata, no fotos que ya ten&iacute;as en tu galer&iacute;a de antes."))
    es+=card("DESCARGA / GUARDA EN ONEDRIVE","Descarga Tus Fotos a OneDrive",
        para("Cuando termines, descarga tus fotos RAW a OneDrive para que est&eacute;n a salvo y listas para importar.")
        + steps([
            ("Pon la tarjeta en la computadora:","saca la tarjeta SD de la c&aacute;mara y ponla en el lector de la computadora. Pide el lector al Sr. Silva si lo necesitas."),
            ("Crea una carpeta del proyecto:","en tu OneDrive, crea una carpeta nueva para este proyecto."),
            ("Copia tus archivos RAW:","copia todas tus fotos RAW de la tarjeta a esa carpeta de OneDrive."),
            ("Deja que sincronice:","espera a que OneDrive termine de sincronizar. El &iacute;cono de nube cambia a una palomita cuando termina."),
        ]))
    es+=card("IMPORTA / A LIGHTROOM","Importa a Lightroom Classic",
        para("Ahora importa tu serie a Lightroom Classic. Las diapositivas de abajo te gu&iacute;an en cada clic. Despl&aacute;zate por las 12 diapositivas y descarga el PDF si quieres tenerlo abierto mientras trabajas.")
        + slide_deck(True))
    es+=card("HOJA DE CONTACTOS / MUESTRA TU SERIE","Crea Tu Hoja de Contactos de 12 Im&aacute;genes",
        para("Una hoja de contactos es una p&aacute;gina que muestra todas tus fotos como miniaturas. Crea la tuya con el dise&ntilde;o de hoja de contactos de 12 en el m&oacute;dulo Imprimir de Lightroom Classic, y gu&aacute;rdala como JPG de alta resoluci&oacute;n. La plantilla est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba).")
        + bullets([
            ("Selecciona tus im&aacute;genes:","elige las fotos de tu serie importada."),
            ("Usa el dise&ntilde;o de 12:","en el m&oacute;dulo Imprimir, elige la hoja de contactos de 12."),
            ("Guarda la p&aacute;gina:","exporta la hoja de contactos como JPG de alta resoluci&oacute;n para entregar."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 hoja de contactos:","tu hoja de contactos de 12 im&aacute;genes (JPG de alta resoluci&oacute;n), que muestra tu serie importada, subida a esta tarea de Canvas.")])

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Capture and Import | Image Series Photo Walk | Photography 1A | PVHS", nav("Step 01",dots_for(1),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Image Series Photo Walk &bull; Step 2","Cull &amp; Edit","Pick your best 6, do a light edit, and turn in a 6-image contact sheet.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("CULL / KEEP THE STRONG ONES","Cull to Your Best 6",
        para("Culling means looking through your photos and keeping only the strongest. Pick the 6 images that best show your series. Drop the blurry, the too-dark, and the repeats.")
        + bullets([
            ("Look for your best:","pick the 6 photos that are sharp, well-framed, and clearly part of your series."),
            ("Keep it cohesive:","choose 6 that feel like they belong together."),
            ("Flag your picks:","in Lightroom, mark your 6 so they are easy to find."),
        ]))
    en+=card("EDIT / A LIGHT TOUCH","Give Each Photo a Light Edit",
        float_right(EDIT_FLOAT,"A Pioneer Valley student editing her photos on an iMac in the lab, with her Canon EOS R5 on the desk","Editing your series in Lightroom Classic.")
        + para("Now do a light edit on your 6 in the Develop module. Small changes only: the goal is clean, natural photos that still feel like one series.")
        + bullets([
            ("Exposure:","make the photo brighter or darker until it looks right."),
            ("Highlights:","pull back the brightest areas so they are not blown out."),
            ("Shadows:","lift the darkest areas so you can see detail."),
            ("Color temperature (White Balance):","warm it up or cool it down so the colors look true and match across your series."),
        ])
        + note_orange("Keep your edits consistent across all 6 so the series still feels like one family of images."))
    en+=card("CONTACT SHEET / YOUR BEST SIX","Make Your 6-Image Contact Sheet",
        para("Now make a 6-image contact sheet of your edited picks. Use the 6-Up contact sheet layout in the Print module, then save it as a high-resolution JPG. The template is on this module&rsquo;s Overview page (marked M at the top).")
        + bullets([
            ("Select your 6:","pick your 6 edited images."),
            ("Use the 6-Up layout:","in the Print module, choose the 6-Up contact sheet."),
            ("Save the page:","export the contact sheet as a high-resolution JPG to turn in."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 contact sheet:","your 6-image contact sheet (high-resolution JPG), showing your 6 edited picks, uploaded to this Canvas assignment.")])

    es=banner("Caminata de Serie de Im&aacute;genes &bull; Paso 2","Selecciona y Edita","Elige tus mejores 6, haz una edici&oacute;n ligera y entrega una hoja de contactos de 6.","#top","Back to English")
    es+=card("SELECCIONA / QU&Eacute;DATE CON LAS FUERTES","Selecciona (Cull) Tus Mejores 6",
        para("Seleccionar (cull) significa revisar tus fotos y quedarte solo con las m&aacute;s fuertes. Elige las 6 im&aacute;genes que mejor muestran tu serie. Descarta las borrosas, las muy oscuras y las repetidas.")
        + bullets([
            ("Busca tus mejores:","elige las 6 fotos n&iacute;tidas, bien encuadradas y claramente parte de tu serie."),
            ("Mant&eacute;nla cohesiva:","elige 6 que se sientan que van juntas."),
            ("Marca tus elegidas:","en Lightroom, marca tus 6 para encontrarlas f&aacute;cil."),
        ]))
    es+=card("EDITA / UN TOQUE LIGERO","Dale a Cada Foto una Edici&oacute;n Ligera",
        float_right(EDIT_FLOAT,"Una estudiante de Pioneer Valley editando sus fotos en una iMac en el laboratorio, con su Canon EOS R5 sobre el escritorio","Editando tu serie en Lightroom Classic.")
        + para("Ahora haz una edici&oacute;n ligera de tus 6 en el m&oacute;dulo Revelar. Solo cambios peque&ntilde;os: la meta es fotos limpias y naturales que sigan sinti&eacute;ndose como una sola serie.")
        + bullets([
            ("Exposici&oacute;n:","haz la foto m&aacute;s clara o m&aacute;s oscura hasta que se vea bien."),
            ("Luces (Highlights):","baja las zonas m&aacute;s brillantes para que no se quemen."),
            ("Sombras (Shadows):","sube las zonas m&aacute;s oscuras para ver el detalle."),
            ("Temperatura de color (Balance de Blancos):","cali&eacute;ntala o enfr&iacute;ala para que los colores se vean reales y combinen en tu serie."),
        ])
        + note_orange("Mant&eacute;n tus ediciones consistentes en las 6 para que la serie siga sinti&eacute;ndose como una familia de im&aacute;genes."))
    es+=card("HOJA DE CONTACTOS / TUS MEJORES SEIS","Crea Tu Hoja de Contactos de 6 Im&aacute;genes",
        para("Ahora crea una hoja de contactos de 6 im&aacute;genes con tus elegidas editadas. Usa el dise&ntilde;o de hoja de contactos de 6 en el m&oacute;dulo Imprimir, y gu&aacute;rdala como JPG de alta resoluci&oacute;n. La plantilla est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba).")
        + bullets([
            ("Selecciona tus 6:","elige tus 6 im&aacute;genes editadas."),
            ("Usa el dise&ntilde;o de 6:","en el m&oacute;dulo Imprimir, elige la hoja de contactos de 6."),
            ("Guarda la p&aacute;gina:","exporta la hoja de contactos como JPG de alta resoluci&oacute;n para entregar."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 hoja de contactos:","tu hoja de contactos de 6 im&aacute;genes (JPG de alta resoluci&oacute;n), que muestra tus 6 elegidas editadas, subida a esta tarea de Canvas.")])

    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a><a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Cull and Edit | Image Series Photo Walk | Photography 1A | PVHS", nav("Step 02",dots_for(2),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 03 ----------------
def step03():
    en=banner("Image Series Photo Walk &bull; Step 3","Reflection","Tell the story of your series.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("STEP 03 / REFLECT","Complete and Upload the Reflection",
        para("Finish with a short reflection. It asks about the series you chose, how you offloaded and imported your photos, the 6 you kept, and the edits you made.")
        + note_orange("The reflection is on this module&rsquo;s Overview page: the first page of this module, marked M in the steps at the top. Open it to download the reflection.")
        + bullets([
            ("Open it:","open the reflection Word document (.docx) from this module&rsquo;s Overview page (marked M at the top)."),
            ("Answer every question:","type your answers in the boxes, in full sentences."),
            ("Save and upload:","save the document and upload it to this Canvas assignment."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
    en+=note_orange("Answer honestly, in your own words.")

    es=banner("Caminata de Serie de Im&aacute;genes &bull; Paso 3","Reflexi&oacute;n","Cuenta la historia de tu serie.","#top","Back to English")
    es+=card("PASO 03 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        para("Termina con una reflexi&oacute;n corta. Te pregunta sobre la serie que elegiste, c&oacute;mo descargaste e importaste tus fotos, las 6 que guardaste y las ediciones que hiciste.")
        + note_orange("La reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo: la primera p&aacute;gina de este m&oacute;dulo, marcada con M en los pasos de arriba. &Aacute;brela para descargar la reflexi&oacute;n.")
        + bullets([
            ("&Aacute;brelo:","abre el documento de Word (.docx) de la reflexi&oacute;n desde la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba)."),
            ("Contesta cada pregunta:","escribe tus respuestas en los cuadros, en oraciones completas."),
            ("Guarda y sube:","guarda el documento y s&uacute;belo a esta tarea de Canvas."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completado, subido a esta tarea de Canvas.")])
    es+=note_orange("Contesta con honestidad, en tus propias palabras.")

    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page("Step 3: Reflection | Image Series Photo Walk | Photography 1A | PVHS", nav("Step 03",dots_for(3),stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03)]:
    html=ent(gen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    low=html.lower()
    for w in ["shoot","shooting","shot","shots","shoots","screenshot"]:
        assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
