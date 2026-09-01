#!/usr/bin/env python3
# Digital Arts 1A - Motivational Athlete Poster (Photoshop). Converted from the MRC
# orange build to the PVHS teal angular framework. Overview + Step 01, bilingual.
import os, re
SITE="https://www.creativesilva.com"
ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
IMG=f"{SITE}/assets/images/digarts1/athlete-poster"
ATHLETE=f"{SITE}/assets/mrc/images/MRC_Athlete.png"   # existing embedded image, kept for now
NEWDOC=f"{IMG}/new-document.png"
TUT_WORK=f"{IMG}/tut-workspace.png"
TUT_SEL=f"{IMG}/tut-selections.png"
TUT_MASK=f"{IMG}/tut-layer-masks.png"
URL_WORK="https://www.adobe.com/learn/photoshop/in-app/introduction-to-the-workspace"
URL_SEL="https://www.adobe.com/learn/photoshop/in-app/introduction-to-selections"
URL_MASK="https://www.adobe.com/learn/photoshop/in-app/get-to-know-layer-masks"

OVER="digarts1-athlete-poster-overview.html"
S1="digarts1-athlete-poster-step01.html"

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

def support_tile(thumb,title,desc,url,openlabel):
    return ('<div style="flex:0 0 290px;width:290px;box-sizing:border-box;display:flex;flex-direction:column;background:linear-gradient(180deg,rgba(0,116,116,0.14) 0%,rgba(0,116,116,0.04) 100%);border:1px solid rgba(0,184,184,0.28);border-top:4px solid #00b8b8;">'
      f'<a href="{url}" target="_blank" rel="noopener" style="display:block;line-height:0;"><img src="{thumb}" alt="{title}" style="display:block;width:100%;height:163px;object-fit:cover;" /></a>'
      '<div style="padding:14px 16px 16px;display:flex;flex-direction:column;flex:1 1 auto;">'
      f'<div style="font-size:13.5pt;color:#ffffff;margin-bottom:6px;"><strong>{title}</strong></div>'
      f'<div style="font-size:11.5pt;color:rgba(255,255,255,0.82);line-height:1.55;flex:1 1 auto;margin-bottom:14px;">{desc}</div>'
      f'<div><a href="{url}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:9px 16px;border-top:2px solid #00b8b8;font-size:10.5pt;letter-spacing:0.04em;"><strong>{openlabel}</strong></a></div>'
      '</div></div>')

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
        para("You will design a motivational poster of your favorite athlete in Photoshop. You will cut the athlete out of their background, add a bold motion-blurred background behind them, drop in their team logo with a glow, and finish with a quote, their name, and colors that all work together. The goal is a clean, hype-worthy poster you would be proud to print and hang up.")
        + framed(ATHLETE,"Example motivational athlete poster"))
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

    es=banner("Arte Digital 1A &bull; Photoshop","P&oacute;ster Motivacional de Atleta","Dise&ntilde;a un p&oacute;ster que anime a tu atleta favorito.","#top","Back to English")
    es+=card("EL PROYECTO / RESUMEN","Lo Que Vas a Crear",
        para("Vas a dise&ntilde;ar un p&oacute;ster motivacional de tu atleta favorito en Photoshop. Vas a recortar al atleta de su fondo, agregar un fondo con desenfoque de movimiento detr&aacute;s, colocar el logo de su equipo con un resplandor, y terminar con una frase, su nombre y colores que combinen. La meta es un p&oacute;ster limpio y llamativo que te sientas orgulloso de imprimir y colgar.")
        + framed(ATHLETE,"Ejemplo de p&oacute;ster motivacional de atleta"))
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

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)
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
        + stepblock(4,"Open Photoshop","Click the Photoshop icon in the <strong>Dock</strong> at the bottom of the screen. If you do not see it, press <strong>Command + Spacebar</strong>, type &lsquo;Photoshop,&rsquo; and press <strong>Return</strong>.")
        + stepblock(5,"Start a New File","On the start screen, click <strong>New file</strong>. You can also go to <strong>File &gt; New</strong> at the top.")
        + stepblock(6,"Pick Print, Then Letter","At the top of the New Document window, click <strong>Print</strong>. Then click the <strong>Letter</strong> preset. It is already 8.5 &times; 11 inches at 300 PPI.")
        + stepblock(7,"Check Your Settings","On the right side, make sure Width is <strong>8.5 Inches</strong>, Height is <strong>11</strong>, Orientation is <strong>Portrait</strong> (the tall one), Resolution is <strong>300 Pixels/Inch</strong>, and Color Mode is <strong>RGB Color</strong>. Name it &lsquo;Motivational Poster.&rsquo;")
        + framed(NEWDOC,"Photoshop New Document window set to Letter, 8.5 by 11 inches, 300 PPI, RGB",maxw="640px")
        + stepblock(8,"Click Create","Click the blue <strong>Create</strong> button. Your blank poster opens, ready to work on.")
        + stepblock(9,"Save Into Your Folder","Go to <strong>File &gt; Save As</strong> and save it inside your <strong>Motivational Poster</strong> folder. Keep it as a Photoshop file (.psd) while you work, so you can keep editing your layers."))
    en+=card("BUILD YOUR POSTER","Cut Out, Blur, Glow, Finish",
        para("Now build the poster. Work through the steps in order. Take your time.")
        + stepblock(10,"Find Your Athlete Photo","Go to Google Images and search your athlete&rsquo;s name. Click <strong>Tools</strong>, set <strong>Size</strong> to <strong>Large</strong>, and pick a sharp, high-resolution photo. Save it. High resolution matters because this is print size.")
        + stepblock(11,"Bring the Photo In","In Photoshop, go to <strong>File &gt; Place Embedded</strong>, pick your athlete photo, and press Return to drop it in.")
        + stepblock(12,"Cut Out the Athlete","Click <strong>Select &gt; Subject</strong> to grab your athlete. Then click <strong>Select and Mask</strong>. Switch the View to <strong>Overlay</strong> (the red view) so you can see what is selected. Clean the edges with the brush. Set Output To: <strong>New Layer with Layer Mask</strong>.")
        + stepblock(13,"Blur the Background","Turn the original photo layer back on, underneath your cut-out athlete, and click it. Go to <strong>Filter &gt; Blur &gt; Motion Blur</strong>. Set the Angle to <strong>0</strong> (straight across) and push the Distance high, so the streaks are bold behind your athlete.")
        + stepblock(14,"Add the Team Logo","Find your athlete&rsquo;s team or organization logo online in high resolution. Remove its background. Place the logo on a layer between the athlete and the blurred background.")
        + stepblock(15,"Make the Logo Glow","Click the logo layer. Double-click it to open <strong>Layer Style</strong>. Turn on <strong>Outer Glow</strong> so the logo pops.")
        + stepblock(16,"Add Your Words","Pick the <strong>Type tool (T)</strong>. Add a short motivational quote and your athlete&rsquo;s name. Keep the words big and easy to read.")
        + stepblock(17,"Match Your Colors","Use the <strong>Eyedropper tool (I)</strong> to pull colors from the photo. Use those colors for your text so the whole poster matches.")
        + stepblock(18,"Flatten and Export","When you are happy, go to <strong>Layer &gt; Flatten Image</strong>. Then <strong>File &gt; Export &gt; Export As</strong>, choose <strong>JPG</strong>, and save it into your Motivational Poster folder. That JPG is what you turn in."))
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
        + stepblock(4,"Abre Photoshop","Haz clic en el &iacute;cono de Photoshop en el <strong>Dock</strong>, abajo en la pantalla. Si no lo ves, presiona <strong>Command + Barra espaciadora</strong>, escribe &lsquo;Photoshop&rsquo; y presiona <strong>Return</strong>.")
        + stepblock(5,"Crea un Archivo Nuevo","En la pantalla de inicio, haz clic en <strong>Nuevo archivo</strong>. Tambi&eacute;n puedes ir a <strong>Archivo &gt; Nuevo</strong> arriba.")
        + stepblock(6,"Elige Impresi&oacute;n y Luego Carta","Arriba en la ventana de Nuevo Documento, haz clic en <strong>Impresi&oacute;n</strong>. Luego haz clic en el ajuste <strong>Carta</strong> (Letter). Ya viene en 8.5 &times; 11 pulgadas a 300 PPI.")
        + stepblock(7,"Revisa Tus Ajustes","A la derecha, aseg&uacute;rate de que el Ancho sea <strong>8.5 Pulgadas</strong>, la Altura <strong>11</strong>, la Orientaci&oacute;n <strong>Vertical</strong> (la alta), la Resoluci&oacute;n <strong>300 P&iacute;xeles/Pulgada</strong> y el Modo de Color <strong>RGB</strong>. Ponle de nombre &lsquo;Motivational Poster.&rsquo;")
        + framed(NEWDOC,"Ventana de Nuevo Documento de Photoshop en Carta, 8.5 por 11 pulgadas, 300 PPI, RGB",maxw="640px")
        + stepblock(8,"Haz Clic en Crear","Haz clic en el bot&oacute;n azul <strong>Crear</strong>. Tu p&oacute;ster en blanco se abre, listo para trabajar.")
        + stepblock(9,"Guarda en Tu Carpeta","Ve a <strong>Archivo &gt; Guardar Como</strong> y gu&aacute;rdalo dentro de tu carpeta <strong>Motivational Poster</strong>. D&eacute;jalo como archivo de Photoshop (.psd) mientras trabajas, para que puedas seguir editando tus capas."))
    es+=card("CONSTRUYE TU P&Oacute;STER","Recorta, Desenfoca, Resplandor, Termina",
        para("Ahora construye el p&oacute;ster. Ve paso a paso, en orden. T&oacute;mate tu tiempo.")
        + stepblock(10,"Busca la Foto de Tu Atleta","Ve a Google Im&aacute;genes y busca el nombre de tu atleta. Haz clic en <strong>Herramientas</strong>, pon <strong>Tama&ntilde;o</strong> en <strong>Grande</strong>, y elige una foto n&iacute;tida y de alta resoluci&oacute;n. Gu&aacute;rdala. La alta resoluci&oacute;n importa porque es tama&ntilde;o de impresi&oacute;n.")
        + stepblock(11,"Trae la Foto","En Photoshop, ve a <strong>Archivo &gt; Colocar Incrustado</strong>, elige la foto de tu atleta y presiona Return para colocarla.")
        + stepblock(12,"Recorta al Atleta","Haz clic en <strong>Seleccionar &gt; Sujeto</strong> para tomar a tu atleta. Luego haz clic en <strong>Seleccionar y Aplicar M&aacute;scara</strong>. Cambia la Vista a <strong>Superposici&oacute;n</strong> (la vista roja) para ver qu&eacute; est&aacute; seleccionado. Limpia los bordes con el pincel. Salida a: <strong>Nueva Capa con M&aacute;scara</strong>.")
        + stepblock(13,"Desenfoca el Fondo","Vuelve a encender la capa original de la foto, debajo de tu atleta recortado, y haz clic en ella. Ve a <strong>Filtro &gt; Desenfocar &gt; Desenfoque de Movimiento</strong>. Pon el &Aacute;ngulo en <strong>0</strong> (recto) y sube la Distancia alto, para que las rayas sean fuertes detr&aacute;s de tu atleta.")
        + stepblock(14,"Agrega el Logo del Equipo","Busca el logo del equipo u organizaci&oacute;n de tu atleta en alta resoluci&oacute;n. Qu&iacute;tale el fondo. Coloca el logo en una capa entre el atleta y el fondo desenfocado.")
        + stepblock(15,"Haz que el Logo Brille","Haz clic en la capa del logo. Haz doble clic para abrir <strong>Estilo de Capa</strong>. Activa <strong>Resplandor Exterior</strong> para que el logo resalte.")
        + stepblock(16,"Agrega Tus Palabras","Elige la <strong>herramienta Texto (T)</strong>. Agrega una frase motivadora corta y el nombre de tu atleta. Mant&eacute;n las palabras grandes y f&aacute;ciles de leer.")
        + stepblock(17,"Combina Tus Colores","Usa la <strong>herramienta Cuentagotas (I)</strong> para sacar colores de la foto. Usa esos colores en tu texto para que todo el p&oacute;ster combine.")
        + stepblock(18,"Aplana y Exporta","Cuando est&eacute;s contento, ve a <strong>Capa &gt; Acoplar Imagen</strong>. Luego <strong>Archivo &gt; Exportar &gt; Exportar Como</strong>, elige <strong>JPG</strong> y gu&aacute;rdalo en tu carpeta Motivational Poster. Ese JPG es lo que entregas."))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 p&oacute;ster:","tu p&oacute;ster final aplanado, guardado como JPG, subido a esta tarea de Canvas.")])
    es+=note_orange("Tu p&oacute;ster debe ser tu propio trabajo original. S&eacute; honesto y entrega tu propio dise&ntilde;o.")

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><span></span></div>'
    return wrap_page("Step 1: Build | Motivational Athlete Poster | Digital Arts 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01)]:
    html=ent(gen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    low=html.lower()
    for w in ["shoot","shooting","shot","shots","screenshot"]:
        assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
