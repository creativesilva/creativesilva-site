#!/usr/bin/env python3
# Digital Arts 1A - Module 05: Live Stream Graphic (Photoshop how-to).
# Guided, step-by-step: build the "History 301 Live Stream" promo in Photoshop.
# Stripped from Adobe CIB 2025 Lesson 1 to a 5th-grade reading level, production steps only
# (no work-area touring, no Generative Fill). NO reflection (it is a guided how-to).
# Overview + 1 step, bilingual EN/ES. End-example float image on the Overview; no header image;
# no image on Step 01 (the picture-by-picture guide is the Lesson Slides PDF, added later).
import os, re
SITE="https://www.creativesilva.com"
ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
END_IMG=f"{SITE}/assets/images/digarts1/live-stream-graphic/live-stream-end-example-v1.jpg"
ASSETS_ZIP=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Assets.zip"
SLIDES_PDF=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Slides.pdf"

OVER="digarts1-live-stream-graphic-overview.html"
S1="digarts1-live-stream-graphic-step01.html"

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

AREA="Digital Arts"   # OneDrive top folder for this course's project folders

def folder_note(es):
    # Every orange downloads block tells students to make a module project folder and move
    # their files from Downloads into OneDrive > Digital Arts > that folder, so work stays together.
    if es:
        return ('<div style="margin-top:16px;font-size:12pt;color:rgba(255,255,255,0.82);line-height:1.55;">'
          '<strong style="color:#ffb27c;">Mantente organizado:</strong> crea una carpeta nueva y ll&aacute;mala como este m&oacute;dulo. '
          'Cuando cada archivo termine de descargarse, mu&eacute;velo de tu carpeta de Descargas a '
          f'OneDrive &rarr; {AREA} &rarr; esa carpeta del proyecto para que todos tus archivos queden juntos.</div>')
    return ('<div style="margin-top:16px;font-size:12pt;color:rgba(255,255,255,0.82);line-height:1.55;">'
      '<strong style="color:#ffb27c;">Stay organized:</strong> make a new folder and name it after this module. '
      'As each file finishes downloading, move it out of your Downloads folder into '
      f'OneDrive &rarr; {AREA} &rarr; that project folder so all your files stay together.</div>')

def downloads_card(eyebrow,heading,inner):
    # CANONICAL orange downloads card (framework standard), placed right after the
    # intro/header card on the Overview so students grab files before starting.
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      '<div style="display:inline-block;background:rgba(0,0,0,0.40);border-left:3px solid #FF6B1A;padding:5px 12px 5px 10px;font-family:Arial,sans-serif;font-size:10pt;letter-spacing:0.22em;color:#ffb27c;text-transform:uppercase;margin-bottom:12px;">'
      f'<strong>{eyebrow}</strong></div>'
      f'<div style="margin-bottom:8px;"><span style="font-size:20pt;color:#ffffff;"><strong>{heading}</strong></span></div>'
      '<div style="height:2px;background:#FF6B1A;width:60px;margin-bottom:18px;"></div>'
      f'{inner}</div>')


RESICON=f"{SITE}/assets/Icons/assignment/resources-v1.png"
def resources_card(eyebrow,heading,inner):
    # PURPLE Resources section (LOCKED): in-depth how-to / reference. Distinct from teal content,
    # orange Downloads, gold Deliverables.
    return ('<div style="background:linear-gradient(180deg,rgba(139,92,246,0.10) 0%,rgba(139,92,246,0.03) 100%);border:1px solid rgba(139,92,246,0.28);border-left:6px solid #8b5cf6;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      '<div style="display:inline-block;background:rgba(0,0,0,0.40);border-left:3px solid #8b5cf6;padding:5px 12px 5px 10px;font-family:Arial,sans-serif;font-size:10pt;letter-spacing:0.22em;color:#c4b5fd;text-transform:uppercase;margin-bottom:12px;">'
      f'<strong>{eyebrow}</strong></div>'
      '<div style="display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:8px;">'
      f'<div style="font-size:20pt;color:#ffffff;"><strong>{heading}</strong></div>'
      f'<img src="{RESICON}" alt="Resource" style="width:44px;height:44px;flex:0 0 auto;display:block;" /></div>'
      '<div style="height:2px;background:#8b5cf6;width:60px;margin-bottom:18px;"></div>'
      f'{inner}</div>')

def para(t):
    return f'<div style="margin-bottom:14px;line-height:1.72;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{t}</span></div>'

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
        lead=(f'<strong>{b}</strong> ' if b else '')
        r+=('<div style="display:flex;align-items:flex-start;gap:12px;margin-bottom:12px;">'
            f'<span style="flex:0 0 auto;width:26px;height:26px;border-radius:50%;background:#FF6B1A;color:#ffffff;font-size:12pt;line-height:26px;text-align:center;"><strong>{i}</strong></span>'
            f'<span style="font-size:13.5pt;color:rgba(255,255,255,0.88);line-height:1.5;">{lead}{rest}</span></div>')
    return f'<div style="margin:4px 0 6px;">{r}</div>'

def note_orange(t):
    return (f'<div style="background:rgba(255,107,26,0.10);border:1px solid rgba(255,107,26,0.30);border-left:4px solid #FF6B1A;padding:11px 14px;margin:8px 0;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def scrollbox(es, inner):
    # long step sequences go in a contained scroll panel so the page looks less intimidating
    hint=('Scroll inside the box to see all 13 steps' if not es else 'Despl&aacute;zate en el cuadro para ver los 13 pasos')
    return (f'<div style="font-size:11pt;color:#80e0e0;margin-bottom:8px;opacity:0.85;">&#8595; {hint}</div>'
      '<div class="silva-scroll" style="max-height:520px;overflow-y:auto;padding:16px 18px 20px;border:1px solid rgba(0,184,184,0.22);border-radius:14px;'
      'background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, rgba(0,0,0,0.14) 88%, rgba(0,184,184,0.16) 100%);">'
      f'{inner}</div>')

def phase(title, items, intro=''):
    introhtml=(f'<div style="margin-bottom:10px;line-height:1.6;"><span style="font-size:13pt;color:rgba(255,255,255,0.86);">{intro}</span></div>' if intro else '')
    return ('<div style="border-left:3px solid #00b8b8;padding:2px 0 2px 16px;margin:0 0 22px;">'
      f'<div style="font-size:15pt;color:#ffffff;margin-bottom:8px;"><strong>{title}</strong></div>'
      f'{introhtml}{steps(items)}</div>')

def float_right(src,alt,cap):
    return ('<div style="float:right;width:44%;min-width:250px;margin:0 0 14px 22px;">'
      f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;"><img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      f'<div style="font-size:10.5pt;color:#80e0e0;text-align:center;margin-top:6px;opacity:0.9;line-height:1.4;">{cap}</div></div>')

DL_ICON=f"{SITE}/assets/Icons/assignment/downloads-v1.png"

def dl_link(url,label,row=False):
    mgn='margin:0;' if row else 'margin:0 10px 8px 0;'
    return (f'<a href="{url}" download style="display:inline-block;text-decoration:none;background:#FF6B1A;color:#ffffff;padding:11px 22px;border-top:2px solid #ffb27c;font-size:11pt;letter-spacing:0.04em;{mgn}"><strong>{label}</strong></a>')

def dl_row(url,label):
    return ('<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:8px;">'
      f'<img src="{DL_ICON}" alt="" style="width:42px;height:42px;flex:0 0 auto;display:block;" />'
      + dl_link(url,label,row=True) + '</div>')

def pdf_placeholder(label):
    # dashed placeholder for the Lesson Slides PDF link (Chris adds the deck + link later)
    return ('<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:8px;">'
      f'<img src="{DL_ICON}" alt="" style="width:42px;height:42px;flex:0 0 auto;opacity:0.45;display:block;" />'
      '<div style="flex:1 1 auto;min-width:230px;border:2px dashed rgba(0,184,184,0.45);background:rgba(0,184,184,0.06);'
      'padding:11px 16px;box-sizing:border-box;font-size:11pt;letter-spacing:0.06em;text-transform:uppercase;color:#80e0e0;">'
      f'<strong>{label}</strong></div></div>')

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
        lis+=('<div style="margin-bottom:6px;line-height:1.5;"><span style="color:#f5b301;">&bull;</span> '
              f'<span style="font-size:13pt;color:rgba(255,255,255,0.90);"><strong>{b}</strong> {rest}</span></div>')
    return ('<div style="background:rgba(245,179,1,0.12);border:1px solid rgba(245,179,1,0.35);border-left:5px solid #f5b301;padding:16px 18px;margin:0 0 8px;">'
      '<div style="display:flex;align-items:flex-start;gap:12px;">'
      '<div style="flex:1 1 auto;min-width:0;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#ffd166;margin-bottom:8px;"><strong>{title}</strong></div>'
      f'<div style="font-size:13pt;color:#ffffff;margin-bottom:8px;"><strong>{lead}</strong></div></div>'
      f'<img src="{SITE}/assets/Icons/assignment/deliverables-v3.png" alt="Deliverables" style="width:44px;height:44px;flex:0 0 auto;display:block;" /></div>'
      f'{lis}</div>')

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
            f'        <a href="{OVER}" class="bc-hide-sm">Live Stream Graphic</a>\n'
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

def dots_for(active_idx):
    hrefs=[OVER,S1]; titles=[("M","Overview"),("1","Step 01")]
    r=""
    for i,(lab,title) in enumerate(titles):
        r+=dot("" if i==active_idx else hrefs[i], lab, title, i==active_idx, module=(i==0 and active_idx!=0))
    return r

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Digital Arts 1A &bull; Module 05","Live Stream Graphic","Follow the steps to build a live stream promo image in Photoshop.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("THE PROJECT / OVERVIEW","Build a Live Stream Graphic",
        float_right(END_IMG,"Finished History 301 Live Stream graphic: an arch photo with an orange bar on the left, a blue bar on the right, a green wash, and the words HISTORY 301 and LIVE STREAM in white","What your finished graphic will look like.")
        + para("In this project you follow clear steps in Adobe Photoshop to build a live stream promo graphic. Everyone starts from the same photo and follows the same steps, so all your graphics will come out looking alike.")
        + para("You will make a new Photoshop file, add a photo, add two colored bars, add the words &ldquo;History 301&rdquo; and &ldquo;Live Stream,&rdquo; add a green color wash, paint a blue spatter, move the photo and use Generative Fill to fill the gap, and export your finished image to turn in.")
        + '<div style="clear:both;"></div>'
        + note_orange("This is a follow-along how-to, not a free-choice project. Do the steps in order so your result matches the example."))
    en+=downloads_card("DOWNLOADS / GET YOUR FILES","Download Your Files",
        para("Grab the project files here before you start. The Lesson Slides show a picture for every step.")
        + dl_row(ASSETS_ZIP,"Project Files (ZIP)")
        + '<div style="margin-top:10px;">' + dl_row(SLIDES_PDF,"Lesson Slides (PDF)") + '</div>'
        + folder_note(False))
    en+=card("SKILLS / WHAT YOU WILL LEARN","New Photoshop Skills",
        para("This project teaches you the basics you will use in every Photoshop project after this one:")
        + bullets([
            ("Start a file:","make a new Photoshop document the right size."),
            ("Add a photo:","place a photo into your design and size it."),
            ("Select and fill:","use the Rectangular Marquee to make a box and fill it with color."),
            ("Add type:","add and style words (text) on your image."),
            ("Layers and blending:","stack layers and use a blending mode to mix colors."),
            ("Adjustment layers and AI:","add a solid color layer, and use Generative Fill to extend the photo."),
            ("Export:","save a finished copy to hand in."),
        ]))
    en+=card("VOCABULARY / 6 TERMS","Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Layer","One level of your image. Layers stack on top of each other, and you can edit one without changing the others."),
           ("Selection","The part of the image you mark off to work on. A moving dashed line shows the edge."),
           ("Fill","To pour a color into a selection or a layer."),
           ("Type","Words (text) you add to your image. Type sits on its own layer."),
           ("Blending Mode","A setting that changes how a layer&rsquo;s colors mix with the layers under it."),
           ("Export","To save a finished copy of your work as a JPG or PNG to share or hand in.")]))

    es=banner("Arte Digital 1A &bull; M&oacute;dulo 05","Gr&aacute;fico de Live Stream","Sigue los pasos para crear una imagen promocional de live stream en Photoshop.","#top","Back to English")
    es+=card("EL PROYECTO / RESUMEN","Crea un Gr&aacute;fico de Live Stream",
        float_right(END_IMG,"Gr&aacute;fico terminado de History 301 Live Stream: una foto de un arco con una barra naranja a la izquierda, una barra azul a la derecha, un ba&ntilde;o verde y las palabras HISTORY 301 y LIVE STREAM en blanco","As&iacute; se ver&aacute; tu gr&aacute;fico terminado.")
        + para("En este proyecto sigues pasos claros en Adobe Photoshop para crear un gr&aacute;fico promocional de live stream. Todos empiezan con la misma foto y siguen los mismos pasos, as&iacute; que todos los gr&aacute;ficos quedar&aacute;n parecidos.")
        + para("Vas a crear un archivo nuevo de Photoshop, agregar una foto, agregar dos barras de color, agregar las palabras &ldquo;History 301&rdquo; y &ldquo;Live Stream,&rdquo; agregar un ba&ntilde;o de color verde, pintar un salpicado azul, mover la foto y usar Relleno Generativo para llenar el hueco, y exportar tu imagen terminada para entregar.")
        + '<div style="clear:both;"></div>'
        + note_orange("Esto es un instructivo para seguir paso a paso, no un proyecto de elecci&oacute;n libre. Haz los pasos en orden para que tu resultado se parezca al ejemplo."))
    es+=downloads_card("DESCARGAS / OBT&Eacute;N TUS ARCHIVOS","Descarga Tus Archivos",
        para("Consigue aqu&iacute; los archivos del proyecto antes de empezar. Las Diapositivas de la Lecci&oacute;n muestran una imagen de cada paso.")
        + dl_row(ASSETS_ZIP,"Archivos del Proyecto (ZIP)")
        + '<div style="margin-top:10px;">' + dl_row(SLIDES_PDF,"Diapositivas de la Lecci&oacute;n (PDF)") + '</div>'
        + folder_note(True))
    es+=card("HABILIDADES / LO QUE APRENDER&Aacute;S","Nuevas Habilidades de Photoshop",
        para("Este proyecto te ense&ntilde;a lo b&aacute;sico que usar&aacute;s en cada proyecto de Photoshop despu&eacute;s de este:")
        + bullets([
            ("Crear un archivo:","haz un documento nuevo de Photoshop del tama&ntilde;o correcto."),
            ("Agregar una foto:","coloca una foto en tu dise&ntilde;o y ajusta su tama&ntilde;o."),
            ("Seleccionar y rellenar:","usa el Marco Rectangular para hacer una caja y rellenarla con color."),
            ("Agregar texto:","agrega y da estilo a las palabras (texto) en tu imagen."),
            ("Capas y mezcla:","apila capas y usa un modo de fusi&oacute;n para mezclar colores."),
            ("Capas de ajuste e IA:","agrega una capa de color s&oacute;lido y usa Relleno Generativo para extender la foto."),
            ("Exportar:","guarda una copia terminada para entregar."),
        ]))
    es+=card("VOCABULARIO / 6 T&Eacute;RMINOS","Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Layer (Capa)","Un nivel de tu imagen. Las capas se apilan una sobre otra y puedes editar una sin cambiar las dem&aacute;s."),
           ("Selection (Selecci&oacute;n)","La parte de la imagen que marcas para trabajar. Una l&iacute;nea punteada en movimiento muestra el borde."),
           ("Fill (Rellenar)","Poner un color dentro de una selecci&oacute;n o una capa."),
           ("Type (Texto)","Las palabras que agregas a tu imagen. El texto va en su propia capa."),
           ("Blending Mode (Modo de Fusi&oacute;n)","Un ajuste que cambia c&oacute;mo se mezclan los colores de una capa con las capas de abajo."),
           ("Export (Exportar)","Guardar una copia terminada de tu trabajo como JPG o PNG para compartir o entregar.")]))

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Live Stream Graphic | Digital Arts 1A | PVHS", nav("Overview",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Live Stream Graphic &bull; Step 1","Build It in Photoshop","Follow the steps in order to build your graphic.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 image:","your finished Live Stream graphic (01Working.jpg), uploaded to this Canvas assignment.")])
    en+=card("BEFORE YOU START / THE SLIDES","Follow Along With the Slides",
        para("Do these steps in Adobe Photoshop, in order. The Lesson Slides show a picture for each step, so open them next to Photoshop as you work.")
        + dl_row(SLIDES_PDF,"Lesson Slides (PDF)")
        + note_orange("Use color codes exactly as written (like ff7f00) so your colors match the example."))
    en+=resources_card("RESOURCE / STEP-BY-STEP GUIDE","Build Your Graphic",
        para("Do these steps in Adobe Photoshop, in order. Scroll through the box below, and open the Lesson Slides to see a picture for each step.")
        + scrollbox(False,
            phase("Step 1 &middot; New Document",[
                ("Open Photoshop.",""),
                ("Make a new file:","choose File &gt; New. Click the Film &amp; Video tab, then click the HDTV 1080p preset (1920 by 1080). Click Create."),
                ("Save it:","choose File &gt; Save As, name it 01Working, and click Save. Click OK if a box pops up."),
            ])
            + phase("Step 2 &middot; Place the Photo",[
                ("Place the photo:","choose File &gt; Place Embedded. Find Arch.jpg in your project files, and click Place."),
                ("Fill the width:","drag a corner handle out so the photo covers the whole width of the canvas."),
                ("Lock it in:","click the checkmark in the top bar, or press Enter (Windows) or Return (Mac)."),
            ],intro="Do not center the building yet. You move it near the end.")
            + phase("Step 3 &middot; Set Units to Pixels",[
                ("Open the setting:","choose Edit &gt; Preferences &gt; Units &amp; Rulers (Windows) or Photoshop &gt; Settings &gt; Units &amp; Rulers (Mac)."),
                ("Choose pixels:","set Rulers to Pixels, and click OK. You only do this once."),
            ])
            + phase("Step 4 &middot; New Layer",[
                ("Pick the layer:","in the Layers panel, click the Arch layer."),
                ("Add a layer:","click the Create a New Layer button at the bottom of the Layers panel."),
                ("Name it:","double-click the new layer&rsquo;s name, type Rectangles, and press Enter or Return."),
            ])
            + phase("Step 5 &middot; Orange Bar",[
                ("Get ready:","make sure the Rectangles layer is selected. Pick the Rectangular Marquee tool (press M)."),
                ("Draw the box:","start just outside the top-left corner and drag down and right. Release when the info reads W 96px and H 1080px."),
                ("Fill it orange:","in the Contextual Task Bar, click Fill Selection, then Fill Color. Type ff7f00 in the # field, click OK, then OK again."),
                ("Clear it:","choose Select &gt; Deselect."),
            ])
            + phase("Step 6 &middot; Blue Bar",[
                ("Draw the box:","with the Rectangular Marquee tool, start just outside the top-right corner and drag down and left. Release when the info reads W 660px and H 1080px."),
                ("Fill it blue:","choose Edit &gt; Fill. Set Contents to Color, type 0053b2, and click OK, then OK again."),
                ("Clear it:","choose Select &gt; Deselect."),
            ])
            + phase("Step 7 &middot; Color Blend Mode",[
                ("Blend the bars:","in the Layers panel, click the blend mode menu (it says Normal) at the top-left, and choose Color. Now the photo shows through both bars."),
                ("Save:","choose File &gt; Save."),
            ])
            + phase("Step 8 &middot; Title Text",[
                ("Set up type:","pick the Horizontal Type tool (press T). In the top bar, choose a bold serif font (the deck uses Abril Fatface), set the size to 210 pt, click Center, and set the color to white (ffffff)."),
                ("Turn on All Caps:","in the Properties panel, click the All Caps (TT) button."),
                ("Type the title:","click near the lower-center of the canvas and type History 301. It shows as HISTORY 301."),
                ("Finish:","click the checkmark, or press Ctrl+Enter (Windows) or Cmd+Return (Mac). Do not press plain Enter."),
                ("Center it:","pick the Move tool (press V) and drag the words to center them."),
            ])
            + phase("Step 9 &middot; Subtitle Text",[
                ("Start a new line:","choose Select &gt; Deselect Layers so Photoshop makes a new type layer."),
                ("Change the type:","with the Type tool, change the font to a condensed bold italic (the deck uses Acumin Pro Condensed Black Italic), set the size to 165 pt, and click Right align."),
                ("Type it:","click near the right side, about two-thirds down the canvas, and type Live Stream. It shows as LIVE STREAM."),
                ("Finish:","click the checkmark to commit."),
            ])
            + phase("Step 10 &middot; Solid Color Layer",[
                ("Pick the layer:","in the Layers panel, click the Arch layer."),
                ("Add a solid color:","click the Create New Fill or Adjustment Layer button (the half-filled circle) at the bottom of the Layers panel, and choose Solid Color."),
                ("Choose dark green:","type 0c3303, and click OK."),
                ("Blend it in:","set this layer&rsquo;s blend mode to Hard Light, then change its Opacity to 90%."),
                ("Hide the guides:","choose View &gt; Show &gt; Guides to turn off the cyan guides."),
            ],intro="This dark green layer makes the white text easier to read.")
            + phase("Step 11 &middot; Sample and Paint",[
                ("Sample a blue:","pick the Eyedropper tool (press I) and click a lighter blue area on the right side to load that color."),
                ("Brighten it:","choose Window &gt; Color. From the panel menu, choose Web Color Sliders, type 4099ff, and press Enter."),
                ("Make a paint layer:","in the Layers panel, click the Rectangles layer. Hold Alt (Windows) or Option (Mac) and click the Create a New Layer button. Name it Paint, and click OK."),
                ("Pick a spatter brush:","pick the Brush tool (press B). Choose Window &gt; Brushes, open the Special Effects Brushes group, and pick Kyle&rsquo;s Spatter Brushes - Spatter Bot Tilt. Set the brush Size to 80px."),
                ("Paint it:","with the Paint layer selected, drag in small circles over the word LIVE to build up a blue spatter. Choose File &gt; Save."),
            ])
            + phase("Step 12 &middot; Move and Generative Fill",[
                ("Set up the Move tool:","pick the Move tool (press V). In the top bar, uncheck Auto-Select."),
                ("Center the building:","in the Layers panel, click the Arch layer. Drag the photo on the canvas until the building is centered in the green area. A gap shows on the left."),
                ("See the gap:","hold Alt (Windows) or Option (Mac) and click the eye icon on the Arch layer to hide the other layers."),
                ("Select the gap:","pick the Rectangular Marquee tool (press M) and drag to select the empty left gap. Overlap the photo edge a little."),
                ("Fill it with AI:","click the Arch layer in the Layers panel. In the Contextual Task Bar, click Generative Fill, leave the box blank, and click Generate. Click Agree if asked."),
                ("Select the best:","in the Properties panel, click each Variation and choose the one that looks most natural."),
                ("Show everything:","right-click (Windows) or Control-click (Mac) the eye icon on the Generative Fill layer, and choose Show/Hide All Other Layers. Choose File &gt; Save."),
            ])
            + phase("Step 13 &middot; Export",[
                ("Open Export As:","choose File &gt; Export &gt; Export As."),
                ("Set the file type:","set Format to JPG and Quality to 6."),
                ("Set the size:","set Width to 1280 and press Tab. The Height becomes 720."),
                ("Match the colors:","make sure Convert to sRGB and Embed Color Profile are on."),
                ("Save the copy:","click Export, name it 01Working, and click Save."),
            ])
        ))

    es=banner("Gr&aacute;fico de Live Stream &bull; Paso 1","Cr&eacute;alo en Photoshop","Sigue los pasos en orden para crear tu gr&aacute;fico.","#top","Back to English")
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 imagen:","tu gr&aacute;fico de Live Stream terminado (01Working.jpg), subido a esta tarea de Canvas.")])
    es+=card("ANTES DE EMPEZAR / LAS DIAPOSITIVAS","Sigue las Diapositivas",
        para("Haz estos pasos en Adobe Photoshop, en orden. Las Diapositivas de la Lecci&oacute;n muestran una imagen de cada paso, as&iacute; que &aacute;brelas junto a Photoshop mientras trabajas.")
        + dl_row(SLIDES_PDF,"Diapositivas de la Lecci&oacute;n (PDF)")
        + note_orange("Usa los c&oacute;digos de color tal como est&aacute;n escritos (como ff7f00) para que tus colores coincidan con el ejemplo."))
    es+=resources_card("RECURSO / GU&Iacute;A PASO A PASO","Crea Tu Gr&aacute;fico",
        para("Haz estos pasos en Adobe Photoshop, en orden. Despl&aacute;zate por el cuadro de abajo y abre las Diapositivas de la Lecci&oacute;n para ver una imagen de cada paso.")
        + scrollbox(True,
            phase("Paso 1 &middot; Documento Nuevo",[
                ("Abre Photoshop.",""),
                ("Crea un archivo nuevo:","elige Archivo &gt; Nuevo. Haz clic en la pesta&ntilde;a Cine y Video, luego en el ajuste HDTV 1080p (1920 por 1080). Haz clic en Crear."),
                ("Gu&aacute;rdalo:","elige Archivo &gt; Guardar Como, nombra el archivo 01Working y haz clic en Guardar. Haz clic en OK si aparece un cuadro."),
            ])
            + phase("Paso 2 &middot; Coloca la Foto",[
                ("Coloca la foto:","elige Archivo &gt; Colocar Incrustado. Busca Arch.jpg en tus archivos del proyecto y haz clic en Colocar."),
                ("Llena el ancho:","arrastra una esquina hacia afuera para que la foto cubra todo el ancho del lienzo."),
                ("F&iacute;jala:","haz clic en la palomita de la barra de arriba, o presiona Enter (Windows) o Return (Mac)."),
            ],intro="No centres el edificio todav&iacute;a. Lo mueves casi al final.")
            + phase("Paso 3 &middot; Pon las Unidades en P&iacute;xeles",[
                ("Abre el ajuste:","elige Edici&oacute;n &gt; Preferencias &gt; Unidades y Reglas (Windows) o Photoshop &gt; Ajustes &gt; Unidades y Reglas (Mac)."),
                ("Elige p&iacute;xeles:","pon Reglas en P&iacute;xeles y haz clic en OK. Solo lo haces una vez."),
            ])
            + phase("Paso 4 &middot; Capa Nueva",[
                ("Elige la capa:","en el panel Capas, haz clic en la capa Arch."),
                ("Agrega una capa:","haz clic en el bot&oacute;n Crear una Capa Nueva abajo del panel Capas."),
                ("N&oacute;mbrala:","haz doble clic en el nombre de la capa nueva, escribe Rectangles y presiona Enter o Return."),
            ])
            + phase("Paso 5 &middot; Barra Naranja",[
                ("Prep&aacute;rate:","aseg&uacute;rate de que la capa Rectangles est&eacute; seleccionada. Elige la herramienta Marco Rectangular (presiona M)."),
                ("Dibuja la caja:","empieza justo afuera de la esquina superior izquierda y arrastra hacia abajo y a la derecha. Suelta cuando la info diga W 96px y H 1080px."),
                ("Rell&eacute;nala de naranja:","en la Barra de Tareas Contextual, haz clic en Rellenar Selecci&oacute;n, luego en Rellenar con Color. Escribe ff7f00 en el campo #, haz clic en OK y OK otra vez."),
                ("Qu&iacute;tala:","elige Selecci&oacute;n &gt; Deseleccionar."),
            ])
            + phase("Paso 6 &middot; Barra Azul",[
                ("Dibuja la caja:","con la herramienta Marco Rectangular, empieza justo afuera de la esquina superior derecha y arrastra hacia abajo y a la izquierda. Suelta cuando la info diga W 660px y H 1080px."),
                ("Rell&eacute;nala de azul:","elige Edici&oacute;n &gt; Rellenar. Pon Contenido en Color, escribe 0053b2 y haz clic en OK, luego OK otra vez."),
                ("Qu&iacute;tala:","elige Selecci&oacute;n &gt; Deseleccionar."),
            ])
            + phase("Paso 7 &middot; Modo de Fusi&oacute;n Color",[
                ("Mezcla las barras:","en el panel Capas, haz clic en el men&uacute; de modo de fusi&oacute;n (dice Normal) arriba a la izquierda y elige Color. Ahora la foto se ve a trav&eacute;s de las dos barras."),
                ("Guarda:","elige Archivo &gt; Guardar."),
            ])
            + phase("Paso 8 &middot; Texto del T&iacute;tulo",[
                ("Prepara el texto:","elige la herramienta Texto Horizontal (presiona T). En la barra de arriba, elige una fuente serif en negrita (el deck usa Abril Fatface), pon el tama&ntilde;o en 210 pt, haz clic en Centrar y pon el color en blanco (ffffff)."),
                ("Activa May&uacute;sculas:","en el panel Propiedades, haz clic en el bot&oacute;n May&uacute;sculas (TT)."),
                ("Escribe el t&iacute;tulo:","haz clic cerca del centro-inferior del lienzo y escribe History 301. Se ve como HISTORY 301."),
                ("Termina:","haz clic en la palomita, o presiona Ctrl+Enter (Windows) o Cmd+Return (Mac). No presiones solo Enter."),
                ("Cent&eacute;ralo:","elige la herramienta Mover (presiona V) y arrastra las palabras para centrarlas."),
            ])
            + phase("Paso 9 &middot; Texto del Subt&iacute;tulo",[
                ("Empieza una l&iacute;nea nueva:","elige Selecci&oacute;n &gt; Deseleccionar Capas para que Photoshop haga una capa de texto nueva."),
                ("Cambia el texto:","con la herramienta Texto, cambia la fuente a una condensada en negrita cursiva (el deck usa Acumin Pro Condensed Black Italic), pon el tama&ntilde;o en 165 pt y haz clic en Alinear a la derecha."),
                ("Escr&iacute;belo:","haz clic cerca del lado derecho, como a dos tercios hacia abajo, y escribe Live Stream. Se ve como LIVE STREAM."),
                ("Termina:","haz clic en la palomita para confirmar."),
            ])
            + phase("Paso 10 &middot; Capa de Color S&oacute;lido",[
                ("Elige la capa:","en el panel Capas, haz clic en la capa Arch."),
                ("Agrega un color s&oacute;lido:","haz clic en el bot&oacute;n Crear Nueva Capa de Relleno o Ajuste (el c&iacute;rculo medio lleno) abajo del panel Capas y elige Color S&oacute;lido."),
                ("Elige verde oscuro:","escribe 0c3303 y haz clic en OK."),
                ("M&eacute;zclalo:","pon el modo de fusi&oacute;n de esta capa en Luz Fuerte, luego cambia su Opacidad a 90%."),
                ("Oculta las gu&iacute;as:","elige Vista &gt; Mostrar &gt; Gu&iacute;as para apagar las gu&iacute;as cian."),
            ],intro="Esta capa verde oscuro hace que el texto blanco se lea mejor.")
            + phase("Paso 11 &middot; Muestrea y Pinta",[
                ("Muestrea un azul:","elige la herramienta Cuentagotas (presiona I) y haz clic en una zona azul m&aacute;s clara del lado derecho para cargar ese color."),
                ("Acl&aacute;ralo:","elige Ventana &gt; Color. Del men&uacute; del panel, elige Deslizadores de Color Web, escribe 4099ff y presiona Enter."),
                ("Crea una capa para pintar:","en el panel Capas, haz clic en la capa Rectangles. Mant&eacute;n Alt (Windows) u Option (Mac) y haz clic en el bot&oacute;n Crear una Capa Nueva. N&oacute;mbrala Paint y haz clic en OK."),
                ("Elige un pincel de salpicado:","elige la herramienta Pincel (presiona B). Elige Ventana &gt; Pinceles, abre el grupo Pinceles de Efectos Especiales y elige Kyle&rsquo;s Spatter Brushes - Spatter Bot Tilt. Pon el Tama&ntilde;o del pincel en 80px."),
                ("Pinta:","con la capa Paint seleccionada, arrastra en c&iacute;rculos peque&ntilde;os sobre la palabra LIVE para crear un salpicado azul. Elige Archivo &gt; Guardar."),
            ])
            + phase("Paso 12 &middot; Mueve y Relleno Generativo",[
                ("Prepara la herramienta Mover:","elige la herramienta Mover (presiona V). En la barra de arriba, desmarca Selecci&oacute;n Autom&aacute;tica (Auto-Select)."),
                ("Centra el edificio:","en el panel Capas, haz clic en la capa Arch. Arrastra la foto en el lienzo hasta que el edificio quede centrado en la zona verde. Aparece un hueco a la izquierda."),
                ("Ve el hueco:","mant&eacute;n Alt (Windows) u Option (Mac) y haz clic en el &iacute;cono de ojo de la capa Arch para ocultar las dem&aacute;s capas."),
                ("Selecciona el hueco:","elige la herramienta Marco Rectangular (presiona M) y arrastra para seleccionar el hueco vac&iacute;o de la izquierda. Traslapa un poco el borde de la foto."),
                ("Rell&eacute;nalo con IA:","haz clic en la capa Arch en el panel Capas. En la Barra de Tareas Contextual, haz clic en Relleno Generativo, deja el cuadro en blanco y haz clic en Generar. Haz clic en Aceptar si te lo pide."),
                ("Elige la mejor:","en el panel Propiedades, haz clic en cada Variaci&oacute;n y elige la que se vea m&aacute;s natural."),
                ("Muestra todo:","haz clic derecho (Windows) o Control-clic (Mac) en el &iacute;cono de ojo de la capa Relleno Generativo y elige Mostrar/Ocultar Todas las Dem&aacute;s Capas. Elige Archivo &gt; Guardar."),
            ])
            + phase("Paso 13 &middot; Exporta",[
                ("Abre Exportar Como:","elige Archivo &gt; Exportar &gt; Exportar Como."),
                ("Elige el tipo de archivo:","pon Formato en JPG y Calidad en 6."),
                ("Pon el tama&ntilde;o:","pon el Ancho en 1280 y presiona Tab. El Alto se vuelve 720."),
                ("Iguala los colores:","aseg&uacute;rate de que Convertir a sRGB e Incrustar Perfil de Color est&eacute;n activados."),
                ("Guarda la copia:","haz clic en Exportar, nombra el archivo 01Working y haz clic en Guardar."),
            ])
        ))

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><span></span></div>'
    return wrap_page("Step 1: Build It in Photoshop | Live Stream Graphic | Digital Arts 1A | PVHS", nav("Step 01",dots_for(1),stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01)]:
    html=ent(gen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    low=html.lower()
    for w in ["shoot","shooting","shot","shots","shoots","screenshot"]:
        assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
