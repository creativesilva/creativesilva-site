#!/usr/bin/env python3
# Digital Arts 1A - Motivational Athlete Poster (Photoshop). Converted from the MRC
# orange build to the PVHS teal angular framework. Overview + Step 01, bilingual.
import os, re
SITE="https://www.creativesilva.com"
ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
IMG=f"{SITE}/assets/images/digarts1/athlete-poster"
ATHLETE=f"{SITE}/assets/mrc/images/MRC_Athlete.png"   # existing embedded image, kept for now
NEWDOC=f"{IMG}/new-document.png"
NEWDOC_MOBILE=f"{IMG}/new-document-mobile.png"
FIX_RASTER=f"{IMG}/fix-rasterize.png"
FIX_SMVIEW=f"{IMG}/fix-select-mask-view.png"
FIX_OUTPUT=f"{IMG}/fix-output-to.png"
FIX_BLUR=f"{IMG}/fix-motion-blur.png"
REFLECT_EN=f"{SITE}/assets/course-documents/Athlete-Poster-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Athlete-Poster-Reflection-ES.docx"
TUT_WORK=f"{IMG}/tut-workspace.png"
TUT_SEL=f"{IMG}/tut-selections.png"
TUT_MASK=f"{IMG}/tut-layer-masks.png"
URL_WORK="https://www.adobe.com/learn/photoshop/in-app/introduction-to-the-workspace"
URL_SEL="https://www.adobe.com/learn/photoshop/in-app/introduction-to-selections"
URL_MASK="https://www.adobe.com/learn/photoshop/in-app/get-to-know-layer-masks"

OVER="digarts1-athlete-poster-overview.html"
S1="digarts1-athlete-poster-step01.html"
S2="digarts1-athlete-poster-step02.html"
S3="digarts1-athlete-poster-step03.html"

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

def note_orange(t):
    return (f'<div style="background:rgba(255,107,26,0.10);border:1px solid rgba(255,107,26,0.30);border-left:4px solid #FF6B1A;padding:11px 14px;margin:8px 0;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def framed(src,alt,maxw=None):
    mw=f'max-width:{maxw};' if maxw else ''
    return f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;margin:6px 0 4px;{mw}"><img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'

STEPLBL="STEP"
def stepblock(n,title,body):
    return ('<div style="border-left:3px solid #00b8b8;padding:2px 0 2px 16px;margin:0 0 18px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.18em;text-transform:uppercase;color:#80e0e0;margin-bottom:4px;"><strong>{STEPLBL} {n}</strong></div>'
      f'<div style="font-size:15pt;color:#ffffff;margin-bottom:6px;"><strong>{title}</strong></div>'
      f'<div style="font-size:13.5pt;color:rgba(255,255,255,0.88);line-height:1.65;">{body}</div></div>')

def scrollbox(n, inner):
    hint=(f'Scroll inside the box to see all {n} steps' if STEPLBL=="STEP"
          else f'Despl&aacute;zate en el cuadro para ver los {n} pasos')
    return (f'<div style="font-size:11pt;color:#80e0e0;margin-bottom:8px;opacity:0.85;">&#8595; {hint}</div>'
      '<div class="silva-scroll" style="max-height:460px;overflow-y:auto;padding:14px 16px 20px;border:1px solid rgba(0,184,184,0.22);border-radius:14px;'
      'background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, rgba(0,0,0,0.14) 88%, rgba(0,184,184,0.16) 100%);">'
      f'{inner}</div>')

def support_tile(thumb,title,desc,url,openlabel):
    return ('<div style="flex:0 0 290px;width:290px;box-sizing:border-box;display:flex;flex-direction:column;background:linear-gradient(180deg,rgba(0,116,116,0.14) 0%,rgba(0,116,116,0.04) 100%);border:1px solid rgba(0,184,184,0.28);border-top:4px solid #00b8b8;">'
      f'<a href="{url}" target="_blank" rel="noopener" style="display:block;line-height:0;"><img src="{thumb}" alt="{title}" style="display:block;width:100%;height:163px;object-fit:cover;" /></a>'
      '<div style="padding:14px 16px 16px;display:flex;flex-direction:column;flex:1 1 auto;">'
      f'<div style="font-size:13.5pt;color:#ffffff;margin-bottom:6px;"><strong>{title}</strong></div>'
      f'<div style="font-size:11.5pt;color:rgba(255,255,255,0.82);line-height:1.55;flex:1 1 auto;margin-bottom:14px;">{desc}</div>'
      f'<div><a href="{url}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:9px 16px;border-top:2px solid #00b8b8;font-size:10.5pt;letter-spacing:0.04em;"><strong>{openlabel}</strong></a></div>'
      '</div></div>')

def dl_link(url,label):
    return (f'<div style="margin-top:6px;"><a href="{url}" download style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:10px 20px;border-top:2px solid #00b8b8;font-size:11pt;letter-spacing:0.04em;"><strong>{label}</strong></a></div>')

def support_tiles(items):
    tiles="".join(support_tile(*it) for it in items)
    return ('<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;padding-bottom:6px;">'
      f'<div style="display:flex;gap:16px;min-width:min-content;align-items:stretch;">{tiles}</div></div>'
      '<div style="font-size:10pt;color:rgba(255,255,255,0.5);margin-top:8px;letter-spacing:0.08em;">&laquo; swipe or scroll for more &raquo;</div>')

def deliverables_box(title,lead,items):
    lis=""
    for b,rest in items:
        lis+=('<div style="margin-bottom:6px;line-height:1.5;"><span style="color:#00b8b8;">&bull;</span> '
              f'<span style="font-size:13pt;color:rgba(255,255,255,0.90);"><strong>{b}</strong> {rest}</span></div>')
    return ('<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.35);border-left:5px solid #00b8b8;padding:16px 18px;margin:0 0 8px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:8px;"><strong>{title}</strong></div>'
      f'<div style="font-size:13pt;color:#ffffff;margin-bottom:8px;"><strong>{lead}</strong></div>{lis}</div>')

def vocab_grid(terms):
    rows=[terms[i:i+3] for i in range(0,len(terms),3)]
    body=""
    for row in rows:
        tds=""
        for term,d in row:
            tds+=('<td style="width:33.33%;vertical-align:top;padding:6px;">'
                  '<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;height:100%;box-sizing:border-box;">'
                  '<div style="background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:16px;height:100%;box-sizing:border-box;">'
                  f'<div style="font-size:12pt;color:#ffffff;margin-bottom:5px;"><strong>{term}</strong></div>'
                  f'<div style="font-size:10.5pt;line-height:1.5;color:rgba(255,255,255,0.80);">{d}</div></div></div></td>')
        body+=f'<tr>{tds}</tr>'
    return f'<table role="presentation" style="width:100%;border-collapse:collapse;table-layout:fixed;"><tbody>{body}</tbody></table>'

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
            f'        <a href="{OVER}" class="bc-hide-sm">Motivational Athlete Poster</a>\n'
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

VOCAB_EN=[
 ("Resolution (PPI)","Pixels per inch. More resolution means a sharper print. This poster needs 300."),
 ("Select and Mask","The Photoshop tool that cuts your athlete cleanly off their background."),
 ("Layer","A stacked level in Photoshop. Your athlete, logo, background, and text each live on their own layer."),
 ("Motion Blur","A filter that adds fast streaks, so the background looks full of speed and energy."),
 ("Layer Style","Effects you add to a layer, like Outer Glow or Drop Shadow, to make it pop."),
 ("Color Palette","The set of colors you use. Pull them from the photo so the whole poster matches."),
]
VOCAB_ES=[
 ("Resoluci&oacute;n (PPI)","P&iacute;xeles por pulgada. M&aacute;s resoluci&oacute;n significa una impresi&oacute;n m&aacute;s n&iacute;tida. Este p&oacute;ster necesita 300."),
 ("Seleccionar y Aplicar M&aacute;scara","La herramienta de Photoshop que recorta a tu atleta limpiamente de su fondo."),
 ("Capa","Un nivel apilado en Photoshop. Tu atleta, el logo, el fondo y el texto viven cada uno en su propia capa."),
 ("Desenfoque de Movimiento","Un filtro que agrega rayas r&aacute;pidas, para que el fondo se vea lleno de velocidad y energ&iacute;a."),
 ("Estilo de Capa","Efectos que agregas a una capa, como Resplandor Exterior o Sombra, para que resalte."),
 ("Paleta de Colores","El conjunto de colores que usas. S&aacute;calos de la foto para que todo el p&oacute;ster combine."),
]

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Digital Arts 1A &bull; Photoshop","Motivational Athlete Poster","Design a poster that hypes up your favorite athlete.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("THE PROJECT / OVERVIEW","What You Will Make",
        para("You will design a motivational poster of your favorite athlete in Photoshop. You will cut the athlete out of their background, add a bold motion-blurred background behind them, drop in their team logo with a glow, and finish with a real quote the athlete actually said, their name, and colors that all work together. The goal is a clean, hype-worthy poster you would be proud to print and hang up.")
        + framed(ATHLETE,"Example motivational athlete poster")
        + note_orange("Your quote must be a real quote your athlete actually said. Choose a font (typeface) for the words that fits the mood and style of your poster."))
    en+=card("QUICK SPECS","Set It Up Right",
        bullets([
            ("Artboard:","8.5 &times; 11 inches, portrait. This is print size."),
            ("Resolution:","300 pixels per inch (PPI), for print quality."),
            ("Color mode:","RGB. You set this when you create the file."),
            ("Submit:","one flattened JPG, the final file you turn in."),
        ])
        + note_orange("New to Photoshop? Step 01 walks you through every click, starting with opening the app and making your file."))
    en+=card("WORDS TO KNOW","Poster Vocabulary",
        note_orange("Heads up: these six key words may be on a quiz.")
        + vocab_grid(VOCAB_EN))
    en+=card("RESOURCES / SUPPORT","Tutorials to Help You",
        para("Three short Adobe guides for the trickiest parts. Tap a video to open it in a new tab. You can watch them again any time.")
        + support_tiles([
            (TUT_WORK,"Introduction to the Workspace","Get to know the Photoshop workspace: the panels, the tools, and where everything lives.",URL_WORK,"Watch: Workspace &rarr;"),
            (TUT_SEL,"Introduction to Selections","Learn how to select part of an image. This is the first step to cutting your athlete out.",URL_SEL,"Watch: Selections &rarr;"),
            (TUT_MASK,"Get to Know Layer Masks","Use layer masks to hide and show parts of a layer without erasing anything.",URL_MASK,"Watch: Layer Masks &rarr;"),
        ]))
    en+=card("REFLECTION / DOWNLOAD","Get the Reflection Document",
        para("Download the reflection here. Fill it out after your poster is done, then turn it in on Step 03.")
        + dl_link(REFLECT_EN,"Athlete Poster Reflection (Word)"))

    es=banner("Arte Digital 1A &bull; Photoshop","P&oacute;ster Motivacional de Atleta","Dise&ntilde;a un p&oacute;ster que anime a tu atleta favorito.","#top","Back to English")
    es+=card("EL PROYECTO / RESUMEN","Lo Que Vas a Crear",
        para("Vas a dise&ntilde;ar un p&oacute;ster motivacional de tu atleta favorito en Photoshop. Vas a recortar al atleta de su fondo, agregar un fondo con desenfoque de movimiento detr&aacute;s, colocar el logo de su equipo con un resplandor, y terminar con una frase real que el atleta haya dicho, su nombre y colores que combinen. La meta es un p&oacute;ster limpio y llamativo que te sientas orgulloso de imprimir y colgar.")
        + framed(ATHLETE,"Ejemplo de p&oacute;ster motivacional de atleta")
        + note_orange("Tu frase debe ser una frase real que tu atleta haya dicho. Elige un tipo de letra para las palabras que quede con el estilo y el ambiente de tu p&oacute;ster."))
    es+=card("DATOS R&Aacute;PIDOS","Config&uacute;ralo Bien",
        bullets([
            ("Lienzo:","8.5 &times; 11 pulgadas, vertical. Es tama&ntilde;o de impresi&oacute;n."),
            ("Resoluci&oacute;n:","300 p&iacute;xeles por pulgada (PPI), para calidad de impresi&oacute;n."),
            ("Modo de color:","RGB. Lo eliges al crear el archivo."),
            ("Entrega:","un JPG aplanado, el archivo final que entregas."),
        ])
        + note_orange("&iquest;Nuevo en Photoshop? El Paso 01 te gu&iacute;a en cada clic, empezando por abrir la app y crear tu archivo."))
    es+=card("PALABRAS CLAVE","Vocabulario del P&oacute;ster",
        note_orange("Atenci&oacute;n: estas seis palabras clave pueden estar en un examen.")
        + vocab_grid(VOCAB_ES))
    es+=card("RECURSOS / APOYO","Tutoriales Para Ayudarte",
        para("Tres gu&iacute;as cortas de Adobe para las partes m&aacute;s dif&iacute;ciles. Toca un video para abrirlo en una pesta&ntilde;a nueva. Puedes verlos las veces que necesites.")
        + support_tiles([
            (TUT_WORK,"Introducci&oacute;n al Espacio de Trabajo","Conoce el espacio de trabajo de Photoshop: los paneles, las herramientas y d&oacute;nde est&aacute; todo.",URL_WORK,"Ver: Espacio de Trabajo &rarr;"),
            (TUT_SEL,"Introducci&oacute;n a las Selecciones","Aprende a seleccionar parte de una imagen. Es el primer paso para recortar a tu atleta.",URL_SEL,"Ver: Selecciones &rarr;"),
            (TUT_MASK,"Conoce las M&aacute;scaras de Capa","Usa m&aacute;scaras de capa para ocultar y mostrar partes de una capa sin borrar nada.",URL_MASK,"Ver: M&aacute;scaras de Capa &rarr;"),
        ]))
    es+=card("REFLEXI&Oacute;N / DESCARGA","Descarga el Documento de Reflexi&oacute;n",
        para("Descarga la reflexi&oacute;n aqu&iacute;. Ll&eacute;nala cuando termines tu p&oacute;ster y entr&eacute;gala en el Paso 03.")
        + dl_link(REFLECT_ES,"Reflexi&oacute;n del P&oacute;ster (Word)"))

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Motivational Athlete Poster | Digital Arts 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    global STEPLBL
    STEPLBL="STEP"
    en=banner("Motivational Athlete Poster &bull; Step 1","Build the Poster","Set up OneDrive, open Photoshop, then build.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("BEFORE YOU START / ONEDRIVE","Check OneDrive and Make Your Folder",
        para("Do this first, every time. It keeps your work saving to the cloud so you never lose it.")
        + stepblock(1,"Check OneDrive Is Syncing","Look at the menu bar in the top-right corner of the screen, next to the date and time. Find the OneDrive cloud icon. A steady gray or blue cloud means it is syncing. If the cloud has a red X or a warning sign, click it and sign in with your school account to clear the error before you go on.")
        + stepblock(2,"Open Your Digital Arts Folder","Open a <strong>Finder</strong> window. In the sidebar, click <strong>OneDrive</strong>, then open your <strong>Digital Arts</strong> folder.")
        + stepblock(3,"Make Your Project Folder","Inside Digital Arts, make a new folder: go to <strong>File &gt; New Folder</strong> (or press <strong>Shift + Command + N</strong>). Name it <strong>Motivational Poster</strong>. Save all your work for this project inside it."))
    en+=card("START IN PHOTOSHOP","Open and Create Your Document",
        para("Never used Photoshop? No problem. Follow these steps exactly and your poster file will be ready to build.")
        + scrollbox(6,
          stepblock(4,"Open Photoshop","Click the Photoshop icon in the <strong>Dock</strong> at the bottom of the screen. If you do not see it, press <strong>Command + Spacebar</strong>, type &lsquo;Photoshop,&rsquo; and press <strong>Return</strong>.")
        + stepblock(5,"Start a New File","On the start screen, click <strong>New file</strong>. You can also go to <strong>File &gt; New</strong> at the top.")
        + stepblock(6,"Pick Print, Then Letter","At the top of the New Document window, click <strong>Print</strong>. Then click the <strong>Letter</strong> preset. It is already 8.5 &times; 11 inches at 300 PPI.")
        + stepblock(7,"Check Your Settings","On the right side, make sure Width is <strong>8.5 Inches</strong>, Height is <strong>11</strong>, Orientation is <strong>Portrait</strong> (the tall one), Resolution is <strong>300 Pixels/Inch</strong>, and Color Mode is <strong>RGB Color</strong>. Name it &lsquo;Motivational Poster.&rsquo;")
        + framed(NEWDOC,"Photoshop New Document window set to Letter, 8.5 by 11 inches, 300 PPI, RGB",maxw="640px")
        + stepblock(8,"Click Create","Click the blue <strong>Create</strong> button. Your blank poster opens, ready to work on.")
        + stepblock(9,"Save Into Your Folder","Go to <strong>File &gt; Save As</strong> and save it inside your <strong>Motivational Poster</strong> folder. Keep it as a Photoshop file (.psd) while you work, so you can keep editing your layers.")))
    en+=card("BUILD YOUR POSTER","Cut Out, Blur, Glow, Finish",
        para("Now build the poster. Work through the steps in order. Take your time.")
        + scrollbox(9,
          stepblock(10,"Find Your Athlete Photo","Go to Google Images and search your athlete&rsquo;s name. Click <strong>Tools</strong>, set <strong>Size</strong> to <strong>Large</strong>, and pick a sharp, high-resolution photo. Save it. High resolution matters because this is print size.")
        + stepblock(11,"Bring the Photo In, Then Rasterize","In Photoshop, go to <strong>File &gt; Place Embedded</strong>, pick your athlete photo, and press Return to drop it in. It arrives as a <strong>Smart Object</strong>, which blocks many edits. Right-click the new layer and choose <strong>Rasterize Layer</strong> so filters and Select and Mask will work.")
        + framed(FIX_RASTER,"Right-click the layer and choose Rasterize Layer",maxw="340px")
        + stepblock(12,"Recrop First, Then Cut Out","<strong>Important:</strong> recrop the photo first so Select Subject lines up. Pick the <strong>Rectangular Marquee tool (M)</strong>, press <strong>Command + A</strong> to Select All, then go to <strong>Image &gt; Crop</strong>. If you skip this, the mask will be off. Now click <strong>Select &gt; Subject</strong> to grab your athlete, then click <strong>Select and Mask</strong>. Press <strong>V</strong> to set the View to <strong>Overlay</strong>, the red view, so your selection is easy to see. Clean the edges with the brush. At the bottom, set <strong>Output To: New Layer</strong>.")
        + framed(FIX_SMVIEW,"Press V for the Overlay (red) view",maxw="290px")
        + framed(FIX_OUTPUT,"Set Output To: New Layer",maxw="360px")
        + stepblock(13,"Blur the Background","Turn the original photo layer back on, underneath your cut-out athlete, and click it. Go to <strong>Filter &gt; Blur &gt; Motion Blur</strong>. Choose <strong>Motion Blur</strong>, NOT Gaussian Blur. Set the Angle to <strong>0</strong> (straight across) and push the Distance high, so the streaks are bold behind your athlete.")
        + framed(FIX_BLUR,"Choose Motion Blur, not Gaussian Blur",maxw="400px")
        + stepblock(14,"Add the Team Logo","Find your athlete&rsquo;s team or organization logo online in high resolution. Remove its background. Place the logo on a layer between the athlete and the blurred background.")
        + stepblock(15,"Make the Logo Glow","Click the logo layer. Double-click it to open <strong>Layer Style</strong>. Turn on <strong>Outer Glow</strong> so the logo pops.")
        + stepblock(16,"Add Your Words","Pick the <strong>Type tool (T)</strong>. Add a <strong>real quote your athlete actually said</strong> and your athlete&rsquo;s name. Choose a <strong>font (typeface)</strong> that fits your poster&rsquo;s style, and keep the words big and easy to read.")
        + stepblock(17,"Match Your Colors","Use the <strong>Eyedropper tool (I)</strong> to pull colors from the photo. Use those colors for your text so the whole poster matches.")
        + stepblock(18,"Flatten and Export","When you are happy, go to <strong>Layer &gt; Flatten Image</strong>. Then <strong>File &gt; Export &gt; Export As</strong>, choose <strong>JPG</strong>, and save it into your Motivational Poster folder. That JPG is what you turn in.")))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 poster:","your final flattened poster, saved as a JPG, uploaded to this Canvas assignment.")])
    en+=note_orange("Your poster must be your own original work. Be honest and turn in your own design.")

    STEPLBL="PASO"
    es=banner("P&oacute;ster Motivacional de Atleta &bull; Paso 1","Construye el P&oacute;ster","Configura OneDrive, abre Photoshop y construye.","#top","Back to English")
    es+=card("ANTES DE EMPEZAR / ONEDRIVE","Revisa OneDrive y Crea Tu Carpeta",
        para("Haz esto primero, cada vez. Mantiene tu trabajo guard&aacute;ndose en la nube para que nunca lo pierdas.")
        + stepblock(1,"Revisa que OneDrive Est&eacute; Sincronizando","Mira la barra de men&uacute;s en la esquina superior derecha de la pantalla, junto a la fecha y la hora. Busca el &iacute;cono de nube de OneDrive. Una nube gris o azul fija significa que est&aacute; sincronizando. Si la nube tiene una X roja o un signo de advertencia, haz clic en ella e inicia sesi&oacute;n con tu cuenta escolar para quitar el error antes de seguir.")
        + stepblock(2,"Abre Tu Carpeta de Arte Digital","Abre una ventana de <strong>Finder</strong>. En la barra lateral, haz clic en <strong>OneDrive</strong>, luego abre tu carpeta <strong>Digital Arts</strong>.")
        + stepblock(3,"Crea Tu Carpeta del Proyecto","Dentro de Digital Arts, crea una carpeta nueva: ve a <strong>Archivo &gt; Nueva Carpeta</strong> (o presiona <strong>Shift + Command + N</strong>). Ll&aacute;mala <strong>Motivational Poster</strong>. Guarda todo tu trabajo de este proyecto dentro de ella."))
    es+=card("EMPIEZA EN PHOTOSHOP","Abre y Crea Tu Documento",
        para("&iquest;Nunca usaste Photoshop? No hay problema. Sigue estos pasos tal cual y tu archivo del p&oacute;ster quedar&aacute; listo para construir.")
        + scrollbox(6,
          stepblock(4,"Abre Photoshop","Haz clic en el &iacute;cono de Photoshop en el <strong>Dock</strong>, abajo en la pantalla. Si no lo ves, presiona <strong>Command + Barra espaciadora</strong>, escribe &lsquo;Photoshop&rsquo; y presiona <strong>Return</strong>.")
        + stepblock(5,"Crea un Archivo Nuevo","En la pantalla de inicio, haz clic en <strong>Nuevo archivo</strong>. Tambi&eacute;n puedes ir a <strong>Archivo &gt; Nuevo</strong> arriba.")
        + stepblock(6,"Elige Impresi&oacute;n y Luego Carta","Arriba en la ventana de Nuevo Documento, haz clic en <strong>Impresi&oacute;n</strong>. Luego haz clic en el ajuste <strong>Carta</strong> (Letter). Ya viene en 8.5 &times; 11 pulgadas a 300 PPI.")
        + stepblock(7,"Revisa Tus Ajustes","A la derecha, aseg&uacute;rate de que el Ancho sea <strong>8.5 Pulgadas</strong>, la Altura <strong>11</strong>, la Orientaci&oacute;n <strong>Vertical</strong> (la alta), la Resoluci&oacute;n <strong>300 P&iacute;xeles/Pulgada</strong> y el Modo de Color <strong>RGB</strong>. Ponle de nombre &lsquo;Motivational Poster.&rsquo;")
        + framed(NEWDOC,"Ventana de Nuevo Documento de Photoshop en Carta, 8.5 por 11 pulgadas, 300 PPI, RGB",maxw="640px")
        + stepblock(8,"Haz Clic en Crear","Haz clic en el bot&oacute;n azul <strong>Crear</strong>. Tu p&oacute;ster en blanco se abre, listo para trabajar.")
        + stepblock(9,"Guarda en Tu Carpeta","Ve a <strong>Archivo &gt; Guardar Como</strong> y gu&aacute;rdalo dentro de tu carpeta <strong>Motivational Poster</strong>. D&eacute;jalo como archivo de Photoshop (.psd) mientras trabajas, para que puedas seguir editando tus capas.")))
    es+=card("CONSTRUYE TU P&Oacute;STER","Recorta, Desenfoca, Resplandor, Termina",
        para("Ahora construye el p&oacute;ster. Ve paso a paso, en orden. T&oacute;mate tu tiempo.")
        + scrollbox(9,
          stepblock(10,"Busca la Foto de Tu Atleta","Ve a Google Im&aacute;genes y busca el nombre de tu atleta. Haz clic en <strong>Herramientas</strong>, pon <strong>Tama&ntilde;o</strong> en <strong>Grande</strong>, y elige una foto n&iacute;tida y de alta resoluci&oacute;n. Gu&aacute;rdala. La alta resoluci&oacute;n importa porque es tama&ntilde;o de impresi&oacute;n.")
        + stepblock(11,"Trae la Foto y Rasteriza","En Photoshop, ve a <strong>Archivo &gt; Colocar Incrustado</strong>, elige la foto de tu atleta y presiona Return para colocarla. Llega como <strong>Objeto Inteligente</strong>, que bloquea muchas ediciones. Haz clic derecho en la capa nueva y elige <strong>Rasterizar Capa</strong> para que funcionen los filtros y Seleccionar y Aplicar M&aacute;scara.")
        + framed(FIX_RASTER,"Haz clic derecho en la capa y elige Rasterizar Capa",maxw="340px")
        + stepblock(12,"Reencuadra Primero, Luego Recorta","<strong>Importante:</strong> reencuadra la foto primero para que Seleccionar Sujeto quede bien. Elige la <strong>herramienta Marco Rectangular (M)</strong>, presiona <strong>Command + A</strong> para Seleccionar Todo, luego ve a <strong>Imagen &gt; Recortar</strong>. Si te saltas esto, la m&aacute;scara quedar&aacute; mal. Ahora haz clic en <strong>Seleccionar &gt; Sujeto</strong> para tomar a tu atleta, luego haz clic en <strong>Seleccionar y Aplicar M&aacute;scara</strong>. Presiona <strong>V</strong> para poner la Vista en <strong>Superposici&oacute;n</strong>, la vista roja, para ver bien tu selecci&oacute;n. Limpia los bordes con el pincel. Abajo, pon <strong>Salida a: Nueva Capa</strong>.")
        + framed(FIX_SMVIEW,"Presiona V para la vista Superposici&oacute;n (roja)",maxw="290px")
        + framed(FIX_OUTPUT,"Pon Salida a: Nueva Capa",maxw="360px")
        + stepblock(13,"Desenfoca el Fondo","Vuelve a encender la capa original de la foto, debajo de tu atleta recortado, y haz clic en ella. Ve a <strong>Filtro &gt; Desenfocar &gt; Desenfoque de Movimiento</strong>. Elige <strong>Desenfoque de Movimiento</strong>, NO Desenfoque Gaussiano. Pon el &Aacute;ngulo en <strong>0</strong> (recto) y sube la Distancia alto, para que las rayas sean fuertes detr&aacute;s de tu atleta.")
        + framed(FIX_BLUR,"Elige Desenfoque de Movimiento, no Gaussiano",maxw="400px")
        + stepblock(14,"Agrega el Logo del Equipo","Busca el logo del equipo u organizaci&oacute;n de tu atleta en alta resoluci&oacute;n. Qu&iacute;tale el fondo. Coloca el logo en una capa entre el atleta y el fondo desenfocado.")
        + stepblock(15,"Haz que el Logo Brille","Haz clic en la capa del logo. Haz doble clic para abrir <strong>Estilo de Capa</strong>. Activa <strong>Resplandor Exterior</strong> para que el logo resalte.")
        + stepblock(16,"Agrega Tus Palabras","Elige la <strong>herramienta Texto (T)</strong>. Agrega una <strong>frase real que tu atleta haya dicho</strong> y el nombre de tu atleta. Elige un <strong>tipo de letra</strong> que quede con el estilo de tu p&oacute;ster, y mant&eacute;n las palabras grandes y f&aacute;ciles de leer.")
        + stepblock(17,"Combina Tus Colores","Usa la <strong>herramienta Cuentagotas (I)</strong> para sacar colores de la foto. Usa esos colores en tu texto para que todo el p&oacute;ster combine.")
        + stepblock(18,"Aplana y Exporta","Cuando est&eacute;s contento, ve a <strong>Capa &gt; Acoplar Imagen</strong>. Luego <strong>Archivo &gt; Exportar &gt; Exportar Como</strong>, elige <strong>JPG</strong> y gu&aacute;rdalo en tu carpeta Motivational Poster. Ese JPG es lo que entregas.")))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 p&oacute;ster:","tu p&oacute;ster final aplanado, guardado como JPG, subido a esta tarea de Canvas.")])
    es+=note_orange("Tu p&oacute;ster debe ser tu propio trabajo original. S&eacute; honesto y entrega tu propio dise&ntilde;o.")

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Build | Motivational Athlete Poster | Digital Arts 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 (MOBILE) ----------------
def step02():
    global STEPLBL
    STEPLBL="STEP"
    en=banner("Motivational Athlete Poster &bull; Step 2","Make the Mobile Version","Remake your poster to fit a phone screen.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("BEFORE YOU START / ONEDRIVE","Same Folder, New Size",
        para("You already made the print poster. Now make a second version, sized for a phone screen.")
        + stepblock(1,"Check OneDrive Is Syncing","Look at the OneDrive cloud icon in the top-right menu bar, next to the clock. If it shows a red X or a warning, click it and sign in with your school account to clear it.")
        + stepblock(2,"Open Your Project Folder","In Finder, open <strong>OneDrive &gt; Digital Arts &gt; Motivational Poster</strong>, the folder you made in Step 1. Save this phone version in there too."))
    en+=card("MAKE THE MOBILE FILE","Create a Phone-Size Document",
        scrollbox(3,
          stepblock(3,"Start a New File","Open Photoshop and click <strong>New file</strong> (or <strong>File &gt; New</strong>).")
        + stepblock(4,"Pick Mobile, Then iPhone","At the top of the New Document window, click the <strong>Mobile</strong> tab. Click the <strong>iPhone X</strong> preset: it is <strong>1125 &times; 2436 pixels at 72 PPI</strong>, Portrait. Make sure Color Mode is <strong>RGB</strong>. Name it &lsquo;Motivational Wallpaper&rsquo; and click <strong>Create</strong>.")
        + framed(NEWDOC_MOBILE,"Photoshop New Document window on the Mobile tab with the iPhone X preset",maxw="640px")
        + stepblock(5,"Save Into Your Folder","Go to <strong>File &gt; Save As</strong> and save it in your <strong>Motivational Poster</strong> folder as a Photoshop file (.psd).")))
    en+=card("REBUILD FOR THE PHONE","Same Steps, Tall Layout",
        para("You know the tools now. Build the same poster, but arrange it for a tall, narrow phone screen.")
        + scrollbox(5,
          stepblock(6,"Bring In and Rasterize","Go to <strong>File &gt; Place Embedded</strong> and drop in your athlete photo. Right-click the layer and choose <strong>Rasterize Layer</strong>, just like Step 1.")
        + stepblock(7,"Recrop, Then Cut Out","<strong>First recrop</strong> so Select Subject lines up: <strong>Rectangular Marquee (M)</strong>, <strong>Command + A</strong>, then <strong>Image &gt; Crop</strong> (skip it and the mask will be off). Then use <strong>Select &gt; Subject</strong> and <strong>Select and Mask</strong>. Press <strong>V</strong> for the red Overlay view, clean the edges, and set <strong>Output To: New Layer</strong>.")
        + stepblock(8,"Blur the Background","Behind your athlete, add <strong>Filter &gt; Blur &gt; Motion Blur</strong> (Motion Blur, not Gaussian). Angle 0, high Distance.")
        + stepblock(9,"Logo and Words","Add the team logo with an <strong>Outer Glow</strong>. Add your <strong>real quote</strong> and your athlete&rsquo;s name with the <strong>Type tool (T)</strong>, in a <strong>font</strong> that fits the style.")
        + stepblock(10,"Arrange It Tall","The phone screen is narrow and very tall. Stack your athlete and your words up and down and fill the whole screen. Leave a little space at the very top and bottom for the phone&rsquo;s clock and home bar.")))
    en+=card("TURN IT IN","Flatten and Export",
        stepblock(11,"Export as JPG","When you are happy, go to <strong>Layer &gt; Flatten Image</strong>, then <strong>File &gt; Export &gt; Export As</strong>, choose <strong>JPG</strong>, and save it into your Motivational Poster folder."))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 mobile poster:","your phone-size version, flattened and saved as a JPG, uploaded to this Canvas assignment.")])
    en+=note_orange("This is your own second version. Be honest and turn in your own design.")

    STEPLBL="PASO"
    es=banner("P&oacute;ster Motivacional de Atleta &bull; Paso 2","Haz la Versi&oacute;n M&oacute;vil","Rehaz tu p&oacute;ster para que quepa en la pantalla de un tel&eacute;fono.","#top","Back to English")
    es+=card("ANTES DE EMPEZAR / ONEDRIVE","Misma Carpeta, Nuevo Tama&ntilde;o",
        para("Ya hiciste el p&oacute;ster para imprimir. Ahora haz una segunda versi&oacute;n, del tama&ntilde;o de una pantalla de tel&eacute;fono.")
        + stepblock(1,"Revisa que OneDrive Est&eacute; Sincronizando","Mira el &iacute;cono de nube de OneDrive en la barra de men&uacute;s arriba a la derecha, junto al reloj. Si muestra una X roja o una advertencia, haz clic e inicia sesi&oacute;n con tu cuenta escolar para quitarla.")
        + stepblock(2,"Abre Tu Carpeta del Proyecto","En Finder, abre <strong>OneDrive &gt; Digital Arts &gt; Motivational Poster</strong>, la carpeta que hiciste en el Paso 1. Guarda esta versi&oacute;n de tel&eacute;fono ah&iacute; tambi&eacute;n."))
    es+=card("CREA EL ARCHIVO M&Oacute;VIL","Crea un Documento Tama&ntilde;o Tel&eacute;fono",
        scrollbox(3,
          stepblock(3,"Crea un Archivo Nuevo","Abre Photoshop y haz clic en <strong>Nuevo archivo</strong> (o <strong>Archivo &gt; Nuevo</strong>).")
        + stepblock(4,"Elige M&oacute;vil y Luego iPhone","Arriba en la ventana de Nuevo Documento, haz clic en la pesta&ntilde;a <strong>M&oacute;vil</strong>. Haz clic en el ajuste <strong>iPhone X</strong>: es <strong>1125 &times; 2436 p&iacute;xeles a 72 PPI</strong>, Vertical. Aseg&uacute;rate de que el Modo de Color sea <strong>RGB</strong>. Ll&aacute;malo &lsquo;Motivational Wallpaper&rsquo; y haz clic en <strong>Crear</strong>.")
        + framed(NEWDOC_MOBILE,"Ventana de Nuevo Documento de Photoshop en la pesta&ntilde;a M&oacute;vil con el ajuste iPhone X",maxw="640px")
        + stepblock(5,"Guarda en Tu Carpeta","Ve a <strong>Archivo &gt; Guardar Como</strong> y gu&aacute;rdalo en tu carpeta <strong>Motivational Poster</strong> como archivo de Photoshop (.psd).")))
    es+=card("RECONSTRUYE PARA EL TEL&Eacute;FONO","Mismos Pasos, Dise&ntilde;o Alto",
        para("Ya conoces las herramientas. Haz el mismo p&oacute;ster, pero acom&oacute;dalo para una pantalla de tel&eacute;fono alta y angosta.")
        + scrollbox(5,
          stepblock(6,"Trae y Rasteriza","Ve a <strong>Archivo &gt; Colocar Incrustado</strong> y coloca la foto de tu atleta. Haz clic derecho en la capa y elige <strong>Rasterizar Capa</strong>, igual que en el Paso 1.")
        + stepblock(7,"Reencuadra, Luego Recorta","<strong>Primero reencuadra</strong> para que Seleccionar Sujeto quede bien: <strong>Marco Rectangular (M)</strong>, <strong>Command + A</strong>, luego <strong>Imagen &gt; Recortar</strong> (si te lo saltas, la m&aacute;scara quedar&aacute; mal). Luego usa <strong>Seleccionar &gt; Sujeto</strong> y <strong>Seleccionar y Aplicar M&aacute;scara</strong>. Presiona <strong>V</strong> para la vista roja Superposici&oacute;n, limpia los bordes y pon <strong>Salida a: Nueva Capa</strong>.")
        + stepblock(8,"Desenfoca el Fondo","Detr&aacute;s de tu atleta, agrega <strong>Filtro &gt; Desenfocar &gt; Desenfoque de Movimiento</strong> (de Movimiento, no Gaussiano). &Aacute;ngulo 0, Distancia alta.")
        + stepblock(9,"Logo y Palabras","Agrega el logo del equipo con un <strong>Resplandor Exterior</strong>. Agrega tu <strong>frase real</strong> y el nombre de tu atleta con la <strong>herramienta Texto (T)</strong>, en un <strong>tipo de letra</strong> que quede con el estilo.")
        + stepblock(10,"Acom&oacute;dalo Alto","La pantalla del tel&eacute;fono es angosta y muy alta. Apila a tu atleta y tus palabras de arriba a abajo y llena toda la pantalla. Deja un poco de espacio arriba y abajo para el reloj y la barra de inicio del tel&eacute;fono.")))
    es+=card("ENTR&Eacute;GALO","Aplana y Exporta",
        stepblock(11,"Exporta como JPG","Cuando est&eacute;s contento, ve a <strong>Capa &gt; Acoplar Imagen</strong>, luego <strong>Archivo &gt; Exportar &gt; Exportar Como</strong>, elige <strong>JPG</strong> y gu&aacute;rdalo en tu carpeta Motivational Poster."))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 p&oacute;ster m&oacute;vil:","tu versi&oacute;n tama&ntilde;o tel&eacute;fono, aplanada y guardada como JPG, subida a esta tarea de Canvas.")])
    es+=note_orange("Esta es tu propia segunda versi&oacute;n. S&eacute; honesto y entrega tu propio dise&ntilde;o.")

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a><a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Mobile Version | Motivational Athlete Poster | Digital Arts 1A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 03 (REFLECTION) ----------------
def step03():
    global STEPLBL
    STEPLBL="STEP"
    en=banner("Motivational Athlete Poster &bull; Step 3","Turn In Your Reflection","Answer four quick questions about your poster.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("STEP 03 / REFLECT","Complete and Upload the Reflection",
        para("Finish the project with a short reflection. It asks who you chose, the font you picked, the hardest part, and what you enjoyed.")
        + note_orange("The reflection Word document is on the Overview page. Open the Overview to download it.")
        + bullets([
            ("Open it:","open the reflection Word document you downloaded from the Overview."),
            ("Answer all 4:","type your answers in the boxes, in full sentences."),
            ("Save and upload:","save the document and upload it to this Canvas assignment."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 reflection:","your completed reflection Word document, uploaded to this Canvas assignment.")])
    en+=note_orange("Answer honestly, in your own words.")

    STEPLBL="PASO"
    es=banner("P&oacute;ster Motivacional de Atleta &bull; Paso 3","Entrega Tu Reflexi&oacute;n","Contesta cuatro preguntas cortas sobre tu p&oacute;ster.","#top","Back to English")
    es+=card("PASO 03 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        para("Termina el proyecto con una reflexi&oacute;n corta. Pregunta a qui&eacute;n elegiste, el tipo de letra que usaste, la parte m&aacute;s dif&iacute;cil y qu&eacute; disfrutaste.")
        + note_orange("El documento de Word de la reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen. Abre el Resumen para descargarlo.")
        + bullets([
            ("&Aacute;brelo:","abre el documento de Word de la reflexi&oacute;n que descargaste del Resumen."),
            ("Contesta las 4:","escribe tus respuestas en los cuadros, en oraciones completas."),
            ("Guarda y sube:","guarda el documento y s&uacute;belo a esta tarea de Canvas."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 reflexi&oacute;n:","tu documento de Word de la reflexi&oacute;n completo, subido a esta tarea de Canvas.")])
    es+=note_orange("Contesta con honestidad, en tus propias palabras.")

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)+dot("",'3',"Step 03",True)
    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page("Step 3: Reflection | Motivational Athlete Poster | Digital Arts 1A | PVHS", nav("Step 03",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03)]:
    html=ent(gen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    low=html.lower()
    for w in ["shoot","shooting","shot","shots","screenshot"]:
        assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
