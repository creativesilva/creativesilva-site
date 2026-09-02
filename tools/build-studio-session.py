#!/usr/bin/env python3
# Photography 2A - Module 03: Studio Session (Panther of the Quarter portraits).
# Dark teal angular framework. Overview + 3 steps, bilingual EN/ES, 5th-grade.
import os, re
SITE="https://www.creativesilva.com"
ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
IMG=f"{SITE}/assets/images/photo2/studio-session"
HEADER=f"{IMG}/studio-header.jpg"
GDRIVE="https://drive.google.com/drive/folders/1sqOMXOYG0FhDJ3519k2DaXWQsawsvIqO?usp=sharing"
PRESETS=f"{SITE}/assets/PVHS_Contact_Sheet_Presets.zip"
REFLECT_EN=f"{SITE}/assets/course-documents/Studio-Session-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Studio-Session-Reflection-ES.docx"

OVER="photo2-studio-session-overview.html"
S1="photo2-studio-session-step01-capture.html"
S2="photo2-studio-session-step02-cull-edit.html"
S3="photo2-studio-session-step03-reflection.html"

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

def dl_link(url,label,download=True):
    dl='download ' if download else ''
    tgt='' if download else 'target="_blank" rel="noopener" '
    return (f'<a href="{url}" {dl}{tgt}style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:10px 20px;border-top:2px solid #00b8b8;font-size:11pt;letter-spacing:0.04em;margin:0 10px 10px 0;"><strong>{label}</strong></a>')

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
            f'        <a href="{OVER}" class="bc-hide-sm">Studio Session</a>\n'
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

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 2A &bull; Studio Session","Studio Session","Photograph the Panther of the Quarter honorees.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("THE PROJECT / OVERVIEW","Panther of the Quarter Portraits",
        para("Our studio is hosting the Panther of the Quarter (POTQ) honorees. There are 20 honorees to photograph for the school newsletter. For each honoree you will create a waist-up portrait and a shoulder-up headshot in our studio, then edit the results to a professional finish.")
        + framed(HEADER,"A raw studio portrait next to the edited, retouched version"))
    en+=card("YOUR CREW / THREE ROLES","Work as a Team of Three",
        para("You will work in groups of three and rotate through three professional roles. Each group photographs one or two of the 20 honorees, and then each person edits the images their group captured.")
        + bullets([
            ("Photographer:","runs the camera. Owns the camera settings and the framing for every frame."),
            ("Art Director:","handles the talent. Greets the honoree, asks their name and which side they favor, poses them, loosens them up, and checks their posture and hair before each frame."),
            ("Lighting Assistant:","owns the light. Sets and adjusts the placement and height of the Westcott Eyelighter reflector."),
        ]))
    en+=card("FRAMING / WHAT TO CAPTURE","Two Frames per Honoree",
        bullets([
            ("Waist-up portrait:","framed from about the waist up."),
            ("Headshot:","framed from the shoulders up."),
        ]))
    en+=card("GET YOUR FILES / RESOURCES","Raw Files and Presets",
        para("Download your group&rsquo;s raw files from the class Google Drive, then set up your folders and import into Lightroom Classic (full steps on Step 01). The Lightroom contact sheet presets are here too.")
        + '<div style="margin-top:6px;">'
        + dl_link(GDRIVE,"Google Drive: Raw Files",download=False)
        + dl_link(PRESETS,"Contact Sheet Presets (ZIP)")
        + '</div>')
    en+=card("REFLECTION / DOWNLOAD","Get the Reflection Document",
        para("Download the reflection here. Complete it after you finish editing, then turn it in on Step 03.")
        + '<div style="margin-top:6px;">' + dl_link(REFLECT_EN,"Studio Session Reflection (Word)") + '</div>')

    es=banner("Fotograf&iacute;a 2A &bull; Sesi&oacute;n de Estudio","Sesi&oacute;n de Estudio","Fotograf&iacute;a a los honorados Pantera del Trimestre.","#top","Back to English")
    es+=card("EL PROYECTO / RESUMEN","Retratos de la Pantera del Trimestre",
        para("Nuestro estudio recibe a los honorados de la Pantera del Trimestre (POTQ). Hay 20 honorados que fotografiar para el bolet&iacute;n de la escuela. Para cada honorado crear&aacute;s un retrato de cintura para arriba y un retrato de hombros para arriba (headshot) en nuestro estudio, y luego editar&aacute;s los resultados con un acabado profesional.")
        + framed(HEADER,"Un retrato de estudio sin editar junto a la versi&oacute;n editada y retocada"))
    es+=card("TU EQUIPO / TRES ROLES","Trabaja en Equipo de Tres",
        para("Trabajar&aacute;s en grupos de tres y rotar&aacute;n por tres roles profesionales. Cada grupo fotograf&iacute;a a uno o dos de los 20 honorados, y luego cada persona edita las im&aacute;genes que captur&oacute; su grupo.")
        + bullets([
            ("Fot&oacute;grafo:","maneja la c&aacute;mara. Es responsable de los ajustes de la c&aacute;mara y del encuadre en cada toma."),
            ("Director de Arte:","atiende al talento. Saluda al honorado, le pregunta su nombre y qu&eacute; lado prefiere, lo posa, lo relaja y revisa su postura y su cabello antes de cada toma."),
            ("Asistente de Iluminaci&oacute;n:","maneja la luz. Coloca y ajusta la posici&oacute;n y la altura del reflector Westcott Eyelighter."),
        ]))
    es+=card("ENCUADRE / QU&Eacute; CAPTURAR","Dos Tomas por Honorado",
        bullets([
            ("Retrato de cintura para arriba:","encuadrado m&aacute;s o menos de la cintura para arriba."),
            ("Headshot:","encuadrado de los hombros para arriba."),
        ]))
    es+=card("OBT&Eacute;N TUS ARCHIVOS / RECURSOS","Archivos Raw y Presets",
        para("Descarga los archivos raw de tu grupo del Google Drive de la clase, luego crea tus carpetas e imp&oacute;rtalos a Lightroom Classic (los pasos completos est&aacute;n en el Paso 01). Los presets de hoja de contactos de Lightroom tambi&eacute;n est&aacute;n aqu&iacute;.")
        + '<div style="margin-top:6px;">'
        + dl_link(GDRIVE,"Google Drive: Archivos Raw",download=False)
        + dl_link(PRESETS,"Presets de Hoja de Contactos (ZIP)")
        + '</div>')
    es+=card("REFLEXI&Oacute;N / DESCARGA","Descarga el Documento de Reflexi&oacute;n",
        para("Descarga la reflexi&oacute;n aqu&iacute;. Compl&eacute;tala cuando termines de editar y entr&eacute;gala en el Paso 03.")
        + '<div style="margin-top:6px;">' + dl_link(REFLECT_ES,"Reflexi&oacute;n de la Sesi&oacute;n (Word)") + '</div>')

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Studio Session | Photography 2A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    global STEPLBL
    STEPLBL="STEP"
    en=banner("Studio Session &bull; Step 1","Capture and Import","Photograph in the studio, then import your take.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("BEFORE YOU START / ONEDRIVE","Set Up Your Folders",
        para("Do this first so your files stay safe in the cloud.")
        + stepblock(1,"Check OneDrive Is Syncing","Look at the OneDrive cloud icon in the top-right menu bar, next to the clock. If it shows a red X or a warning, click it and sign in with your school account to clear it.")
        + stepblock(2,"Make Your Folders","In Finder, open <strong>OneDrive &gt; Photography</strong>. Make a folder called <strong>POTQ</strong>, and inside it make a folder called <strong>Raw</strong> (so the path is OneDrive &gt; Photography &gt; POTQ &gt; Raw).")
        + stepblock(3,"Download Your Raw Files","Open the class <strong>Google Drive</strong> (link on the Overview), find your group&rsquo;s honoree files, and download them into your <strong>Raw</strong> folder."))
    en+=card("IN THE STUDIO / THE SESSION","Photograph Your Honorees",
        para("In your group, rotate through the three roles and photograph your assigned honoree or honorees. Capture two frames of each: a waist-up portrait and a headshot.")
        + bullets([
            ("Photographer:","dial in the camera settings and frame each photo: waist-up, then shoulders-up."),
            ("Art Director:","greet the honoree, learn their name and favored side, pose them, and keep them relaxed. Check posture and hair before each frame."),
            ("Lighting Assistant:","set the height and angle of the Westcott Eyelighter reflector so the light is even and flattering."),
        ]))
    en+=card("IMPORT / LIGHTROOM CLASSIC","Import and Contact Sheet",
        scrollbox(3,
          stepblock(4,"Import Your Take","Open <strong>Lightroom Classic</strong>. Click <strong>Import</strong>, point to your <strong>Raw</strong> folder, select all your group&rsquo;s images, and import them.")
          + stepblock(5,"Build a Full-Take Contact Sheet","Using the contact sheet preset (on the Overview), build a contact sheet of your <strong>entire take</strong>: every image your group captured. Use more than one sheet if you have a lot of images.")
          + stepblock(6,"Export the Contact Sheet","Export the contact sheet as a PDF or JPG so you can turn it in.")))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 contact sheet:","a contact sheet of your entire take, uploaded to this Canvas assignment.")])

    STEPLBL="PASO"
    es=banner("Sesi&oacute;n de Estudio &bull; Paso 1","Captura e Importa","Fotograf&iacute;a en el estudio, luego importa tu toma.","#top","Back to English")
    es+=card("ANTES DE EMPEZAR / ONEDRIVE","Crea Tus Carpetas",
        para("Haz esto primero para que tus archivos queden seguros en la nube.")
        + stepblock(1,"Revisa que OneDrive Est&eacute; Sincronizando","Mira el &iacute;cono de nube de OneDrive en la barra de men&uacute;s arriba a la derecha, junto al reloj. Si muestra una X roja o una advertencia, haz clic e inicia sesi&oacute;n con tu cuenta escolar para quitarla.")
        + stepblock(2,"Crea Tus Carpetas","En Finder, abre <strong>OneDrive &gt; Photography</strong>. Crea una carpeta llamada <strong>POTQ</strong> y dentro de ella una carpeta llamada <strong>Raw</strong> (la ruta queda OneDrive &gt; Photography &gt; POTQ &gt; Raw).")
        + stepblock(3,"Descarga Tus Archivos Raw","Abre el <strong>Google Drive</strong> de la clase (el enlace est&aacute; en el Resumen), busca los archivos del honorado de tu grupo y desc&aacute;rgalos en tu carpeta <strong>Raw</strong>."))
    es+=card("EN EL ESTUDIO / LA SESI&Oacute;N","Fotograf&iacute;a a Tus Honorados",
        para("En tu grupo, roten por los tres roles y fotograf&iacute;en a su honorado o honorados. Captura dos tomas de cada uno: un retrato de cintura para arriba y un headshot.")
        + bullets([
            ("Fot&oacute;grafo:","ajusta la c&aacute;mara y encuadra cada toma: cintura para arriba, luego hombros para arriba."),
            ("Director de Arte:","saluda al honorado, aprende su nombre y su lado preferido, p&oacute;salo y mantenlo relajado. Revisa la postura y el cabello antes de cada toma."),
            ("Asistente de Iluminaci&oacute;n:","ajusta la altura y el &aacute;ngulo del reflector Westcott Eyelighter para que la luz sea pareja y favorecedora."),
        ]))
    es+=card("IMPORTA / LIGHTROOM CLASSIC","Importa y Hoja de Contactos",
        scrollbox(3,
          stepblock(4,"Importa Tu Toma","Abre <strong>Lightroom Classic</strong>. Haz clic en <strong>Importar</strong>, apunta a tu carpeta <strong>Raw</strong>, selecciona todas las im&aacute;genes de tu grupo e imp&oacute;rtalas.")
          + stepblock(5,"Arma una Hoja de Contactos de Toda la Toma","Con el preset de hoja de contactos (en el Resumen), arma una hoja de contactos de <strong>toda tu toma</strong>: cada imagen que captur&oacute; tu grupo. Usa m&aacute;s de una hoja si tienes muchas im&aacute;genes.")
          + stepblock(6,"Exporta la Hoja de Contactos","Exporta la hoja de contactos como PDF o JPG para poder entregarla.")))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 hoja de contactos:","una hoja de contactos de toda tu toma, subida a esta tarea de Canvas.")])

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Capture and Import | Studio Session | Photography 2A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    global STEPLBL
    STEPLBL="STEP"
    en=banner("Studio Session &bull; Step 2","Cull and Edit","Pick your best, edit, and export four finals.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("EDIT / LIGHTROOM CLASSIC","Cull, Edit, and Export",
        para("Now edit the images your group captured. Work in Lightroom Classic.")
        + scrollbox(7,
          stepblock(1,"Cull Your Best","Look through your take and pick your strongest <strong>waist-up portrait</strong> and your strongest <strong>headshot</strong>.")
          + stepblock(2,"Crop and Frame","Crop each image to a clean, well-balanced frame: waist-up for the portrait, shoulders-up for the headshot.")
          + stepblock(3,"Retouch the Skin","Use the <strong>Healing tool</strong> to remove skin blemishes. Keep it natural, do not over-smooth.")
          + stepblock(4,"Fix the Light","If the face is too dark, raise the <strong>Shadows</strong> slider. Balance highlights and exposure so the honoree looks their best.")
          + stepblock(5,"Try Portrait Presets","Experiment with the <strong>portrait presets</strong> in Lightroom Classic. Pick one that flatters your honoree, then fine-tune.")
          + stepblock(6,"Make Color and Black &amp; White","You need four finals: <strong>waist-up in color</strong>, <strong>headshot in color</strong>, <strong>waist-up in black and white</strong>, and <strong>headshot in black and white</strong>. For the black-and-white versions, make a copy of each and apply a <strong>Black &amp; White</strong> treatment.")
          + stepblock(7,"Export and Rename","Export each of the four as a <strong>high-resolution JPG</strong>. Rename the files clearly: <strong>waist_up_color</strong>, <strong>headshot_color</strong>, <strong>waist_up_bw</strong>, and <strong>headshot_bw</strong>.")))
    en+=card("CONTACT SHEET / SIX-UP","Show Your Four Finals",
        para("Build a <strong>6-Up contact sheet</strong> of your four final images using the contact sheet preset (on the Overview), and export it."))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own): 5 files",
        [("1 contact sheet:","a 6-Up contact sheet of your four final images."),
         ("4 images:","your four finals as high-resolution JPGs, named waist_up_color, headshot_color, waist_up_bw, and headshot_bw.")])

    STEPLBL="PASO"
    es=banner("Sesi&oacute;n de Estudio &bull; Paso 2","Selecciona y Edita","Elige tus mejores, edita y exporta cuatro finales.","#top","Back to English")
    es+=card("EDITA / LIGHTROOM CLASSIC","Selecciona, Edita y Exporta",
        para("Ahora edita las im&aacute;genes que captur&oacute; tu grupo. Trabaja en Lightroom Classic.")
        + scrollbox(7,
          stepblock(1,"Selecciona Tus Mejores","Revisa tu toma y elige tu mejor <strong>retrato de cintura para arriba</strong> y tu mejor <strong>headshot</strong>.")
          + stepblock(2,"Recorta y Encuadra","Recorta cada imagen a un encuadre limpio y equilibrado: cintura para arriba en el retrato, hombros para arriba en el headshot.")
          + stepblock(3,"Retoca la Piel","Usa la <strong>herramienta Corrector</strong> para quitar imperfecciones de la piel. Mant&eacute;nlo natural, no suavices de m&aacute;s.")
          + stepblock(4,"Arregla la Luz","Si la cara est&aacute; muy oscura, sube el control de <strong>Sombras</strong>. Equilibra las luces y la exposici&oacute;n para que el honorado se vea de lo mejor.")
          + stepblock(5,"Prueba Presets de Retrato","Experimenta con los <strong>presets de retrato</strong> en Lightroom Classic. Elige uno que favorezca a tu honorado y luego aj&uacute;stalo.")
          + stepblock(6,"Haz Color y Blanco y Negro","Necesitas cuatro finales: <strong>cintura para arriba en color</strong>, <strong>headshot en color</strong>, <strong>cintura para arriba en blanco y negro</strong> y <strong>headshot en blanco y negro</strong>. Para las versiones en blanco y negro, haz una copia de cada una y aplica un tratamiento <strong>Blanco y Negro</strong>.")
          + stepblock(7,"Exporta y Renombra","Exporta cada uno de los cuatro como <strong>JPG de alta resoluci&oacute;n</strong>. Renombra los archivos con claridad: <strong>waist_up_color</strong>, <strong>headshot_color</strong>, <strong>waist_up_bw</strong> y <strong>headshot_bw</strong>.")))
    es+=card("HOJA DE CONTACTOS / 6-UP","Muestra Tus Cuatro Finales",
        para("Arma una <strong>hoja de contactos 6-Up</strong> de tus cuatro im&aacute;genes finales con el preset de hoja de contactos (en el Resumen), y exp&oacute;rtala."))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta): 5 archivos",
        [("1 hoja de contactos:","una hoja de contactos 6-Up de tus cuatro im&aacute;genes finales."),
         ("4 im&aacute;genes:","tus cuatro finales como JPG de alta resoluci&oacute;n, con los nombres waist_up_color, headshot_color, waist_up_bw y headshot_bw.")])

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a><a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Cull and Edit | Studio Session | Photography 2A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 03 ----------------
def step03():
    global STEPLBL
    STEPLBL="STEP"
    en=banner("Studio Session &bull; Step 3","Turn In Your Reflection","Reflect on the process, your role, and your edits.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("STEP 03 / REFLECT","Complete and Upload the Reflection",
        para("Finish the project with a short reflection. It asks about your group and roles, the whole studio process, what you enjoyed and found hardest, and how you made your editing choices.")
        + note_orange("The reflection Word document is on the Overview page. Open the Overview to download it.")
        + bullets([
            ("Open it:","open the reflection Word document you downloaded from the Overview."),
            ("Answer every question:","type your answers in the boxes, in full sentences."),
            ("Save and upload:","save the document and upload it to this Canvas assignment."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 reflection:","your completed reflection Word document, uploaded to this Canvas assignment.")])
    en+=note_orange("Answer honestly, in your own words.")

    STEPLBL="PASO"
    es=banner("Sesi&oacute;n de Estudio &bull; Paso 3","Entrega Tu Reflexi&oacute;n","Reflexiona sobre el proceso, tu rol y tus ediciones.","#top","Back to English")
    es+=card("PASO 03 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        para("Termina el proyecto con una reflexi&oacute;n corta. Pregunta sobre tu grupo y los roles, todo el proceso del estudio, qu&eacute; disfrutaste y qu&eacute; fue lo m&aacute;s dif&iacute;cil, y c&oacute;mo tomaste tus decisiones de edici&oacute;n.")
        + note_orange("El documento de Word de la reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen. Abre el Resumen para descargarlo.")
        + bullets([
            ("&Aacute;brelo:","abre el documento de Word de la reflexi&oacute;n que descargaste del Resumen."),
            ("Contesta cada pregunta:","escribe tus respuestas en los cuadros, en oraciones completas."),
            ("Guarda y sube:","guarda el documento y s&uacute;belo a esta tarea de Canvas."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 reflexi&oacute;n:","tu documento de Word de la reflexi&oacute;n completo, subido a esta tarea de Canvas.")])
    es+=note_orange("Contesta con honestidad, en tus propias palabras.")

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)+dot("",'3',"Step 03",True)
    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page("Step 3: Reflection | Studio Session | Photography 2A | PVHS", nav("Step 03",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03)]:
    html=ent(gen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    low=html.lower()
    for w in ["shoot","shooting","shot","shots","screenshot"]:
        assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
