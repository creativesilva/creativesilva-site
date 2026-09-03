#!/usr/bin/env python3
# Photography 2A - Module 03: Studio Session (Panther of the Quarter portraits).
# Dark teal angular framework. Overview + 3 steps, bilingual EN/ES, 5th-grade.
import os, re
SITE="https://www.creativesilva.com"
ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
IMG=f"{SITE}/assets/images/photo2/studio-session"
HEADER=f"{IMG}/studio-header-v2.png"
EDIT_EXAMPLE=f"{IMG}/studio-header.jpg"
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

def float_right(src,alt,cap):
    return ('<div style="float:right;width:40%;min-width:230px;margin:0 0 14px 22px;">'
      f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;"><img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      f'<div style="font-size:10.5pt;color:#80e0e0;text-align:center;margin-top:6px;opacity:0.9;line-height:1.4;">{cap}</div></div>')

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
        + framed(HEADER,"A three-person student crew photographing a Panther of the Quarter honoree in the studio"))
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
    en+=card("GET YOUR FILES / RESOURCES","Your Raw Files",
        para("Download your group&rsquo;s raw files from the class Google Drive, then set up your folders and import into Lightroom Classic (full steps on Step 01). You should already have the Lightroom contact sheet presets installed; if not, they are on the Photography 2A course overview.")
        + '<div style="margin-top:6px;">'
        + dl_link(GDRIVE,"Google Drive: Raw Files",download=False)
        + '</div>')
    en+=card("REFLECTION / DOWNLOAD","Get the Reflection Document",
        para("Download the reflection here. Complete it after you finish editing, then turn it in on Step 03.")
        + '<div style="margin-top:6px;">' + dl_link(REFLECT_EN,"Studio Session Reflection (Word)") + '</div>')

    es=banner("Fotograf&iacute;a 2A &bull; Sesi&oacute;n de Estudio","Sesi&oacute;n de Estudio","Fotograf&iacute;a a los honorados Pantera del Trimestre.","#top","Back to English")
    es+=card("EL PROYECTO / RESUMEN","Retratos de la Pantera del Trimestre",
        para("Nuestro estudio recibe a los honorados de la Pantera del Trimestre (POTQ). Hay 20 honorados que fotografiar para el bolet&iacute;n de la escuela. Para cada honorado crear&aacute;s un retrato de cintura para arriba y un retrato de hombros para arriba (headshot) en nuestro estudio, y luego editar&aacute;s los resultados con un acabado profesional.")
        + framed(HEADER,"Un equipo de tres estudiantes fotografiando a un honorado de la Pantera del Trimestre en el estudio"))
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
    es+=card("OBT&Eacute;N TUS ARCHIVOS / RECURSOS","Tus Archivos Raw",
        para("Descarga los archivos raw de tu grupo del Google Drive de la clase, luego crea tus carpetas e imp&oacute;rtalos a Lightroom Classic (los pasos completos est&aacute;n en el Paso 01). Ya deber&iacute;as tener instalados los presets de hoja de contactos de Lightroom; si no, est&aacute;n en el resumen del curso de Fotograf&iacute;a 2A.")
        + '<div style="margin-top:6px;">'
        + dl_link(GDRIVE,"Google Drive: Archivos Raw",download=False)
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
          + stepblock(5,"Build a Full-Take Contact Sheet","Using your contact sheet preset (it is also on the Photography 2A course overview if you need it), build a contact sheet of your <strong>entire take</strong>: every image your group captured. Use more than one sheet if you have a lot of images.")
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
          + stepblock(5,"Arma una Hoja de Contactos de Toda la Toma","Con tu preset de hoja de contactos (tambi&eacute;n en el resumen del curso de Fotograf&iacute;a 2A si lo necesitas), arma una hoja de contactos de <strong>toda tu toma</strong>: cada imagen que captur&oacute; tu grupo. Usa m&aacute;s de una hoja si tienes muchas im&aacute;genes.")
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
    en=banner("Studio Session &bull; Step 2","Cull and Edit","Make four finals: two crops, in color and black and white.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("EDIT / LIGHTROOM CLASSIC","Cull, Edit, and Make 4 Finals",
        float_right(EDIT_EXAMPLE,"A raw studio portrait on the left next to the edited, retouched final on the right","Your editing goal: raw frame on the left, finished portrait on the right.")
        + para("Now you will edit in Lightroom Classic. For each honoree you will finish <strong>four</strong> images: two crops in color, and those same two crops in black and white. You know Lightroom a bit already; the new part here is duplicating a photo and converting the copy to black and white the right way. Work through the steps in order.")
        + note_orange("Keep your color version. You will DUPLICATE each edited photo and turn the copy black and white, so you end up with BOTH the color and the black-and-white version.")
        + '<div style="clear:both;"></div>'
        + scrollbox(7,
          stepblock(1,"Cull Your Best Frames","In the <strong>Library</strong> module, look through your whole take of your honoree. Pick the frames where they look their best: eyes open, natural expression, sharp focus. Press <strong>P</strong> to flag your favorites, then work from those.")
          + stepblock(2,"Make Your Two Crops","You need two different crops. Grab the <strong>Crop tool (R)</strong> and make a <strong>waist-up portrait</strong> (framed from about the waist up) and a <strong>headshot</strong> (cropped tighter, from the shoulders up). You can crop one strong frame two ways, or use two different frames. These are your two <strong>color</strong> images.")
          + stepblock(3,"Edit the Color Versions","Switch to the <strong>Develop</strong> module. Make each crop look its best: if the face is dark, raise <strong>Exposure</strong> or <strong>Shadows</strong>; balance the highlights; use the <strong>Healing tool</strong> to gently remove blemishes (keep skin natural). Try a <strong>portrait preset</strong> and fine-tune. When both crops look great, those are your two finished color photos.")
          + stepblock(4,"Duplicate: Create a Virtual Copy","Now keep the color AND make a black-and-white version without losing your color edit. <strong>Right-click</strong> the photo (in the Develop filmstrip or the Library grid) and choose <strong>Create Virtual Copy</strong> (shortcut <strong>Command + &#39;</strong>). Lightroom adds a second copy you can edit on its own. Do this for <strong>both</strong> crops, so you now have four photos: two color originals and two copies to convert.")
          + stepblock(5,"Convert the Copy to Black &amp; White with a Preset","Select a <strong>virtual copy</strong>. <strong>Do NOT just drag Saturation to &minus;100</strong>: that makes a flat, muddy gray. Use a real black-and-white conversion instead: open the <strong>Presets</strong> panel on the left and click a preset in the <strong>B&amp;W</strong> (Black &amp; White) group; or open the <strong>Profile Browser</strong> (next to &lsquo;Profile&rsquo; at the top of the Basic panel) and choose a <strong>Monochrome / B&amp;W</strong> profile. This gives a rich black and white with real contrast. Do this for both virtual copies.")
          + stepblock(6,"Fine-Tune the Black &amp; White","With the black-and-white photo selected, open the <strong>B&amp;W</strong> panel (the color mix). Each slider brightens or darkens what used to be a color: for example, lowering <strong>Red / Orange</strong> deepens skin tones and raising them lifts the face. Nudge the sliders and the <strong>Contrast</strong> until the portrait looks strong.")
          + stepblock(7,"Export All Four as JPG","Select all four photos (2 color + 2 black and white), go to <strong>File &gt; Export</strong>, and export as <strong>high-resolution JPG</strong>. Rename them clearly: <strong>waist_up_color</strong>, <strong>headshot_color</strong>, <strong>waist_up_bw</strong>, and <strong>headshot_bw</strong>.")))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("4 images (minimum):","for one honoree, upload all four as high-resolution JPGs: <strong>waist_up_color</strong>, <strong>headshot_color</strong>, <strong>waist_up_bw</strong>, and <strong>headshot_bw</strong>."),
         ("More than one honoree?","if your group photographed more than one honoree, upload four images for each. The minimum to complete this step is one honoree (four images).")])

    STEPLBL="PASO"
    es=banner("Sesi&oacute;n de Estudio &bull; Paso 2","Selecciona y Edita","Haz cuatro finales: dos recortes, en color y en blanco y negro.","#top","Back to English")
    es+=card("EDITA / LIGHTROOM CLASSIC","Selecciona, Edita y Haz 4 Finales",
        float_right(EDIT_EXAMPLE,"Un retrato de estudio sin editar a la izquierda junto al final editado y retocado a la derecha","Tu meta de edici&oacute;n: la toma sin editar a la izquierda, el retrato terminado a la derecha.")
        + para("Ahora editar&aacute;s en Lightroom Classic. Para cada honorado terminar&aacute;s <strong>cuatro</strong> im&aacute;genes: dos recortes en color y esos mismos dos recortes en blanco y negro. Ya conoces Lightroom un poco; lo nuevo aqu&iacute; es duplicar una foto y convertir la copia a blanco y negro de la forma correcta. Ve paso a paso, en orden.")
        + note_orange("Conserva tu versi&oacute;n en color. Vas a DUPLICAR cada foto editada y convertir la copia a blanco y negro, para que te queden LAS DOS: la de color y la de blanco y negro.")
        + '<div style="clear:both;"></div>'
        + scrollbox(7,
          stepblock(1,"Selecciona Tus Mejores Cuadros","En el m&oacute;dulo <strong>Biblioteca</strong>, revisa toda tu toma del honorado. Elige los cuadros donde se ve mejor: ojos abiertos, expresi&oacute;n natural, enfoque n&iacute;tido. Presiona <strong>P</strong> para marcar tus favoritos y trabaja desde ah&iacute;.")
          + stepblock(2,"Haz Tus Dos Recortes","Necesitas dos recortes diferentes. Toma la <strong>herramienta Recortar (R)</strong> y haz un <strong>retrato de cintura para arriba</strong> (encuadrado m&aacute;s o menos de la cintura para arriba) y un <strong>headshot</strong> (recortado m&aacute;s cerca, de los hombros para arriba). Puedes recortar un buen cuadro de dos formas, o usar dos cuadros distintos. Estas son tus dos im&aacute;genes en <strong>color</strong>.")
          + stepblock(3,"Edita las Versiones en Color","Cambia al m&oacute;dulo <strong>Revelar</strong>. Haz que cada recorte se vea de lo mejor: si la cara est&aacute; oscura, sube <strong>Exposici&oacute;n</strong> o <strong>Sombras</strong>; equilibra las luces; usa la <strong>herramienta Corrector</strong> para quitar imperfecciones con cuidado (mant&eacute;n la piel natural). Prueba un <strong>preset de retrato</strong> y aj&uacute;stalo. Cuando los dos recortes se vean muy bien, esas son tus dos fotos en color terminadas.")
          + stepblock(4,"Duplica: Crea una Copia Virtual","Ahora conserva el color Y haz una versi&oacute;n en blanco y negro sin perder tu edici&oacute;n en color. <strong>Haz clic derecho</strong> en la foto (en la tira de miniaturas de Revelar o en la cuadr&iacute;cula de Biblioteca) y elige <strong>Crear copia virtual</strong> (atajo <strong>Command + &#39;</strong>). Lightroom agrega una segunda copia que puedes editar por separado. Hazlo en <strong>ambos</strong> recortes, para que tengas cuatro fotos: dos originales en color y dos copias para convertir.")
          + stepblock(5,"Convierte la Copia a Blanco y Negro con un Preset","Selecciona una <strong>copia virtual</strong>. <strong>NO bajes la Saturaci&oacute;n a &minus;100</strong>: eso da un gris plano y sucio. Usa una conversi&oacute;n real a blanco y negro: abre el panel <strong>Presets (Ajustes preestablecidos)</strong> a la izquierda y haz clic en un preset del grupo <strong>B&amp;N</strong> (Blanco y Negro); o abre el <strong>Explorador de perfiles</strong> (junto a &lsquo;Perfil&rsquo; arriba del panel B&aacute;sico) y elige un perfil <strong>Monocromo / B&amp;N</strong>. Esto da un blanco y negro rico y con contraste. Hazlo en las dos copias virtuales.")
          + stepblock(6,"Ajusta el Blanco y Negro","Con la foto en blanco y negro seleccionada, abre el panel <strong>B&amp;N</strong> (la mezcla de color). Cada control aclara u oscurece lo que antes era un color: por ejemplo, bajar <strong>Rojo / Naranja</strong> hace m&aacute;s profundos los tonos de piel y subirlos aclara la cara. Mueve los controles y el <strong>Contraste</strong> hasta que el retrato se vea fuerte.")
          + stepblock(7,"Exporta las Cuatro como JPG","Selecciona las cuatro fotos (2 en color + 2 en blanco y negro), ve a <strong>Archivo &gt; Exportar</strong> y exporta como <strong>JPG de alta resoluci&oacute;n</strong>. Renombra con claridad: <strong>waist_up_color</strong>, <strong>headshot_color</strong>, <strong>waist_up_bw</strong> y <strong>headshot_bw</strong>.")))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("4 im&aacute;genes (m&iacute;nimo):","para un honorado, sube las cuatro como JPG de alta resoluci&oacute;n: <strong>waist_up_color</strong>, <strong>headshot_color</strong>, <strong>waist_up_bw</strong> y <strong>headshot_bw</strong>."),
         ("&iquest;M&aacute;s de un honorado?","si tu grupo fotografi&oacute; a m&aacute;s de un honorado, sube cuatro im&aacute;genes por cada uno. El m&iacute;nimo para completar este paso es un honorado (cuatro im&aacute;genes).")])

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
