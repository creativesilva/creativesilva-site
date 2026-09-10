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
        lis+=('<div style="margin-bottom:6px;line-height:1.5;"><span style="color:#00b8b8;">&bull;</span> '
              f'<span style="font-size:13pt;color:rgba(255,255,255,0.90);"><strong>{b}</strong> {rest}</span></div>')
    return ('<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.35);border-left:5px solid #00b8b8;padding:16px 18px;margin:0 0 8px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:8px;"><strong>{title}</strong></div>'
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
        + para("You will make a new Photoshop file, add a photo, add two colored bars, add a green color wash, add the words &ldquo;History 301&rdquo; and &ldquo;Live Stream,&rdquo; add a blue spatter, and export your finished image to turn in.")
        + '<div style="clear:both;"></div>'
        + note_orange("This is a follow-along how-to, not a free-choice project. Do the steps in order so your result matches the example."))
    en+=card("SKILLS / WHAT YOU WILL LEARN","New Photoshop Skills",
        para("This project teaches you the basics you will use in every Photoshop project after this one:")
        + bullets([
            ("Start a file:","make a new Photoshop document the right size."),
            ("Add a photo:","place a photo into your design and size it."),
            ("Select and fill:","make a box selection and fill it with a color."),
            ("Add type:","add and style words (text) on your image."),
            ("Layers and blending:","stack layers and use a blending mode to mix colors."),
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
    en+=card("DOWNLOADS / GET YOUR FILES","Download Your Files",
        para("Grab the project files here. The Lesson Slides show a picture for every step.")
        + dl_row(ASSETS_ZIP,"Project Files (ZIP)")
        + '<div style="margin-top:10px;">' + pdf_placeholder("Lesson Slides (PDF) &middot; link coming soon") + '</div>')

    es=banner("Arte Digital 1A &bull; M&oacute;dulo 05","Gr&aacute;fico de Live Stream","Sigue los pasos para crear una imagen promocional de live stream en Photoshop.","#top","Back to English")
    es+=card("EL PROYECTO / RESUMEN","Crea un Gr&aacute;fico de Live Stream",
        float_right(END_IMG,"Gr&aacute;fico terminado de History 301 Live Stream: una foto de un arco con una barra naranja a la izquierda, una barra azul a la derecha, un ba&ntilde;o verde y las palabras HISTORY 301 y LIVE STREAM en blanco","As&iacute; se ver&aacute; tu gr&aacute;fico terminado.")
        + para("En este proyecto sigues pasos claros en Adobe Photoshop para crear un gr&aacute;fico promocional de live stream. Todos empiezan con la misma foto y siguen los mismos pasos, as&iacute; que todos los gr&aacute;ficos quedar&aacute;n parecidos.")
        + para("Vas a crear un archivo nuevo de Photoshop, agregar una foto, agregar dos barras de color, agregar un ba&ntilde;o de color verde, agregar las palabras &ldquo;History 301&rdquo; y &ldquo;Live Stream,&rdquo; agregar un salpicado azul y exportar tu imagen terminada para entregar.")
        + '<div style="clear:both;"></div>'
        + note_orange("Esto es un instructivo para seguir paso a paso, no un proyecto de elecci&oacute;n libre. Haz los pasos en orden para que tu resultado se parezca al ejemplo."))
    es+=card("HABILIDADES / LO QUE APRENDER&Aacute;S","Nuevas Habilidades de Photoshop",
        para("Este proyecto te ense&ntilde;a lo b&aacute;sico que usar&aacute;s en cada proyecto de Photoshop despu&eacute;s de este:")
        + bullets([
            ("Crear un archivo:","haz un documento nuevo de Photoshop del tama&ntilde;o correcto."),
            ("Agregar una foto:","coloca una foto en tu dise&ntilde;o y ajusta su tama&ntilde;o."),
            ("Seleccionar y rellenar:","haz una selecci&oacute;n de caja y rell&eacute;nala con un color."),
            ("Agregar texto:","agrega y da estilo a las palabras (texto) en tu imagen."),
            ("Capas y mezcla:","apila capas y usa un modo de fusi&oacute;n para mezclar colores."),
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
    es+=card("DESCARGAS / OBT&Eacute;N TUS ARCHIVOS","Descarga Tus Archivos",
        para("Consigue aqu&iacute; los archivos del proyecto. Las Diapositivas de la Lecci&oacute;n muestran una imagen de cada paso.")
        + dl_row(ASSETS_ZIP,"Archivos del Proyecto (ZIP)")
        + '<div style="margin-top:10px;">' + pdf_placeholder("Diapositivas de la Lecci&oacute;n (PDF) &middot; enlace pronto") + '</div>')

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Live Stream Graphic | Digital Arts 1A | PVHS", nav("Overview",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Live Stream Graphic &bull; Step 1","Build It in Photoshop","Follow the steps in order to build your graphic.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("BEFORE YOU START / THE SLIDES","Follow Along With the Slides",
        para("Do these steps in Adobe Photoshop, in order. The Lesson Slides show a picture for each step, so open them next to Photoshop as you work.")
        + pdf_placeholder("Lesson Slides (PDF) &middot; link coming soon")
        + note_orange("Use color codes exactly as written (like ff7f00) so your colors match the example."))
    en+=card("STEP 1 / NEW FILE","Start a New File",
        steps([
            ("Open Photoshop.",""),
            ("Make a new file:","choose File &gt; New. Click Film &amp; Video, then click HDTV 1080p (1920 by 1080). Click Create."),
            ("Save it:","choose File &gt; Save As, name it 01Working, and click Save. Click OK if a box pops up."),
        ]))
    en+=card("STEP 2 / ADD THE PHOTO","Place the Arch Photo",
        steps([
            ("Place the photo:","choose File &gt; Place Embedded. Find Arch.jpg in your project files, and click Place."),
            ("Fill the canvas:","drag a corner of the photo so it covers the whole canvas. Drag the middle to center the building."),
            ("Lock it in:","press Enter (Windows) or Return (Mac)."),
        ]))
    en+=card("STEP 3 / TWO COLOR BARS","Add an Orange Bar and a Blue Bar",
        para("You will add two colored bars on their own layer, so you do not change the photo.")
        + steps([
            ("Make a new layer:","in the Layers panel, click the Arch layer. Click the Create a New Layer button. Double-click the new layer&rsquo;s name and change it to Rectangles."),
            ("Set units to pixels:","choose Edit &gt; Preferences &gt; Units &amp; Rulers (Windows) or Photoshop &gt; Settings &gt; Units &amp; Rulers (Mac). Set Rulers to Pixels, and click OK."),
            ("Draw the orange box:","pick the Rectangular Marquee tool. Start at the top-left corner and drag right and down to make a thin, tall box, about 96 wide and 1080 tall."),
            ("Fill it orange:","choose Edit &gt; Fill. Set Contents to Color, type the code ff7f00, and click OK. Click OK again."),
            ("Clear the selection:","choose Select &gt; Deselect."),
            ("Draw the blue box:","with the Rectangular Marquee tool, start at the top-right corner and drag left and down to make a wider box, about 660 wide and 1080 tall."),
            ("Fill it blue:","choose Edit &gt; Fill. Set Contents to Color, type the code 0053b2, and click OK. Click OK again."),
            ("Clear the selection:","choose Select &gt; Deselect."),
            ("Let the photo show through:","in the Layers panel, click the mode menu that says Normal, and choose Color."),
        ]))
    en+=card("STEP 4 / GREEN WASH","Add a Green Color Layer",
        steps([
            ("Pick the layer:","in the Layers panel, click the Arch layer."),
            ("Add a solid color:","click the Create New Fill or Adjustment Layer button (the half-filled circle) at the bottom of the Layers panel, and choose Solid Color."),
            ("Choose dark green:","type the code 0c3303, and click OK."),
            ("Blend it in:","set this new layer&rsquo;s mode menu (Normal) to Hard Light. Then change its Opacity to 90%."),
            ("Hide the guides:","choose View &gt; Show &gt; Guides to turn them off."),
        ]))
    en+=card("STEP 5 / ADD THE WORDS","Add the Type",
        steps([
            ("Pick the Type tool:","pick the Horizontal Type tool (the T). In the bar at the top, choose a bold font, set the size to 210 pt, click Center, and set the color to white."),
            ("Type the title:","click near the middle of the canvas and type HISTORY 301 in capital letters. Click the checkmark to finish."),
            ("Center it:","pick the Move tool and drag the words to center them."),
            ("Add the second line:","pick the Horizontal Type tool again. Set the size to 165 pt and click Right align. Click near the lower-right and type LIVE STREAM. Click the checkmark."),
        ]))
    en+=card("STEP 6 / BLUE SPATTER","Paint a Blue Spatter Behind &ldquo;Live&rdquo;",
        steps([
            ("Make a paint layer:","in the Layers panel, click the Rectangles layer. Hold Alt (Windows) or Option (Mac) and click the Create a New Layer button. Name it Paint, and click OK."),
            ("Set the color:","click the foreground color box at the bottom of the Tools panel. Type the code 4099ff, and click OK."),
            ("Pick a spatter brush:","pick the Brush tool. Choose Window &gt; Brushes, open the Special Effects Brushes group, and pick a spatter brush. Set the brush Size to about 80."),
            ("Paint it:","with the Paint layer selected, drag over the word LIVE to build up a blue spatter behind it."),
            ("Save:","choose File &gt; Save."),
        ]))
    en+=card("STEP 7 / EXPORT","Export Your Finished Image",
        steps([
            ("Open Export As:","choose File &gt; Export &gt; Export As."),
            ("Set the file type:","set Format to JPG and Quality to 6."),
            ("Set the size:","set Width to 1280. The Height changes to 720 on its own."),
            ("Match the colors:","turn on Convert to sRGB."),
            ("Save the copy:","click Export, name it 01Working, and click Save."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 image:","your finished Live Stream graphic (01Working.jpg), uploaded to this Canvas assignment.")])

    es=banner("Gr&aacute;fico de Live Stream &bull; Paso 1","Cr&eacute;alo en Photoshop","Sigue los pasos en orden para crear tu gr&aacute;fico.","#top","Back to English")
    es+=card("ANTES DE EMPEZAR / LAS DIAPOSITIVAS","Sigue las Diapositivas",
        para("Haz estos pasos en Adobe Photoshop, en orden. Las Diapositivas de la Lecci&oacute;n muestran una imagen de cada paso, as&iacute; que &aacute;brelas junto a Photoshop mientras trabajas.")
        + pdf_placeholder("Diapositivas de la Lecci&oacute;n (PDF) &middot; enlace pronto")
        + note_orange("Usa los c&oacute;digos de color tal como est&aacute;n escritos (como ff7f00) para que tus colores coincidan con el ejemplo."))
    es+=card("PASO 1 / ARCHIVO NUEVO","Crea un Archivo Nuevo",
        steps([
            ("Abre Photoshop.",""),
            ("Crea un archivo nuevo:","elige Archivo &gt; Nuevo. Haz clic en Cine y Video, luego en HDTV 1080p (1920 por 1080). Haz clic en Crear."),
            ("Gu&aacute;rdalo:","elige Archivo &gt; Guardar Como, nombra el archivo 01Working y haz clic en Guardar. Haz clic en OK si aparece un cuadro."),
        ]))
    es+=card("PASO 2 / AGREGA LA FOTO","Coloca la Foto del Arco",
        steps([
            ("Coloca la foto:","elige Archivo &gt; Colocar Incrustado. Busca Arch.jpg en tus archivos del proyecto y haz clic en Colocar."),
            ("Llena el lienzo:","arrastra una esquina de la foto para que cubra todo el lienzo. Arrastra el centro para centrar el edificio."),
            ("Fija la foto:","presiona Enter (Windows) o Return (Mac)."),
        ]))
    es+=card("PASO 3 / DOS BARRAS DE COLOR","Agrega una Barra Naranja y una Azul",
        para("Vas a agregar dos barras de color en su propia capa, para no cambiar la foto.")
        + steps([
            ("Crea una capa nueva:","en el panel Capas, haz clic en la capa Arch. Haz clic en el bot&oacute;n Crear una Capa Nueva. Haz doble clic en el nombre de la capa nueva y c&aacute;mbialo a Rectangles."),
            ("Pon las unidades en p&iacute;xeles:","elige Edici&oacute;n &gt; Preferencias &gt; Unidades y Reglas (Windows) o Photoshop &gt; Ajustes &gt; Unidades y Reglas (Mac). Pon Reglas en P&iacute;xeles y haz clic en OK."),
            ("Dibuja la caja naranja:","elige la herramienta Marco Rectangular. Empieza en la esquina superior izquierda y arrastra a la derecha y hacia abajo para hacer una caja delgada y alta, de m&aacute;s o menos 96 de ancho y 1080 de alto."),
            ("Rell&eacute;nala de naranja:","elige Edici&oacute;n &gt; Rellenar. Pon Contenido en Color, escribe el c&oacute;digo ff7f00 y haz clic en OK. Haz clic en OK otra vez."),
            ("Quita la selecci&oacute;n:","elige Selecci&oacute;n &gt; Deseleccionar."),
            ("Dibuja la caja azul:","con la herramienta Marco Rectangular, empieza en la esquina superior derecha y arrastra a la izquierda y hacia abajo para hacer una caja m&aacute;s ancha, de m&aacute;s o menos 660 de ancho y 1080 de alto."),
            ("Rell&eacute;nala de azul:","elige Edici&oacute;n &gt; Rellenar. Pon Contenido en Color, escribe el c&oacute;digo 0053b2 y haz clic en OK. Haz clic en OK otra vez."),
            ("Quita la selecci&oacute;n:","elige Selecci&oacute;n &gt; Deseleccionar."),
            ("Deja ver la foto:","en el panel Capas, haz clic en el men&uacute; de modo que dice Normal y elige Color."),
        ]))
    es+=card("PASO 4 / BA&Ntilde;O VERDE","Agrega una Capa de Color Verde",
        steps([
            ("Elige la capa:","en el panel Capas, haz clic en la capa Arch."),
            ("Agrega un color s&oacute;lido:","haz clic en el bot&oacute;n Crear Nueva Capa de Relleno o Ajuste (el c&iacute;rculo medio lleno) abajo del panel Capas y elige Color S&oacute;lido."),
            ("Elige verde oscuro:","escribe el c&oacute;digo 0c3303 y haz clic en OK."),
            ("M&eacute;zclalo:","pon el men&uacute; de modo (Normal) de esta capa nueva en Luz Fuerte. Luego cambia su Opacidad a 90%."),
            ("Oculta las gu&iacute;as:","elige Vista &gt; Mostrar &gt; Gu&iacute;as para apagarlas."),
        ]))
    es+=card("PASO 5 / AGREGA LAS PALABRAS","Agrega el Texto",
        steps([
            ("Elige la herramienta Texto:","elige la herramienta Texto Horizontal (la T). En la barra de arriba, elige una fuente en negrita, pon el tama&ntilde;o en 210 pt, haz clic en Centrar y pon el color en blanco."),
            ("Escribe el t&iacute;tulo:","haz clic cerca del centro del lienzo y escribe HISTORY 301 en letras may&uacute;sculas. Haz clic en la palomita para terminar."),
            ("Cent&eacute;ralo:","elige la herramienta Mover y arrastra las palabras para centrarlas."),
            ("Agrega la segunda l&iacute;nea:","elige otra vez la herramienta Texto Horizontal. Pon el tama&ntilde;o en 165 pt y haz clic en Alinear a la derecha. Haz clic cerca de la esquina inferior derecha y escribe LIVE STREAM. Haz clic en la palomita."),
        ]))
    es+=card("PASO 6 / SALPICADO AZUL","Pinta un Salpicado Azul Detr&aacute;s de &ldquo;Live&rdquo;",
        steps([
            ("Crea una capa para pintar:","en el panel Capas, haz clic en la capa Rectangles. Mant&eacute;n Alt (Windows) u Option (Mac) y haz clic en el bot&oacute;n Crear una Capa Nueva. Nombra la capa Paint y haz clic en OK."),
            ("Pon el color:","haz clic en la caja de color frontal abajo del panel de Herramientas. Escribe el c&oacute;digo 4099ff y haz clic en OK."),
            ("Elige un pincel de salpicado:","elige la herramienta Pincel. Elige Ventana &gt; Pinceles, abre el grupo Pinceles de Efectos Especiales y elige un pincel de salpicado. Pon el Tama&ntilde;o del pincel en m&aacute;s o menos 80."),
            ("Pinta:","con la capa Paint seleccionada, arrastra sobre la palabra LIVE para crear un salpicado azul detr&aacute;s de ella."),
            ("Guarda:","elige Archivo &gt; Guardar."),
        ]))
    es+=card("PASO 7 / EXPORTA","Exporta Tu Imagen Terminada",
        steps([
            ("Abre Exportar Como:","elige Archivo &gt; Exportar &gt; Exportar Como."),
            ("Elige el tipo de archivo:","pon Formato en JPG y Calidad en 6."),
            ("Pon el tama&ntilde;o:","pon el Ancho en 1280. El Alto cambia a 720 solo."),
            ("Iguala los colores:","activa Convertir a sRGB."),
            ("Guarda la copia:","haz clic en Exportar, nombra el archivo 01Working y haz clic en Guardar."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 imagen:","tu gr&aacute;fico de Live Stream terminado (01Working.jpg), subido a esta tarea de Canvas.")])

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
