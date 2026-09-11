#!/usr/bin/env python3
# Photography 2A - Module 03: Studio Session (Panther of the Quarter portraits).
# School studio + camera kit (not own device), so NO fresh-photos integrity note.
# Chip-header framework via silva_framework. Overview + 3 steps, bilingual EN/ES, 5th-grade.
import os, re
from silva_framework import *

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/photo2/studio-session"
HEADER=f"{IMG}/studio-header-v4.jpg"
EDIT_EXAMPLE=f"{IMG}/studio-header.jpg"
GDRIVE="https://drive.google.com/drive/folders/1sqOMXOYG0FhDJ3519k2DaXWQsawsvIqO?usp=sharing"
PRESETS=f"{SITE}/assets/PVHS_Contact_Sheet_Presets.zip"
REFLECT_EN=f"{SITE}/assets/course-documents/Studio-Session-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Studio-Session-Reflection-ES.docx"
AREA="Photography Folder"

OVER="photo2-studio-session-overview.html"
S1="photo2-studio-session-step01-capture.html"
S2="photo2-studio-session-step02-cull-edit.html"
S3="photo2-studio-session-step03-reflection.html"

def downloads_block(es):
    # Orange Downloads section (Overview only). Studio holds the Google Drive raw files (read link)
    # and the reflection doc. Same files as before; chip-header chrome.
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga aqu&iacute; todo lo que necesitas para este m&oacute;dulo. Consigue tus archivos antes de empezar." if es
          else "Download everything you need for this module here. Get your files before you start.")
    rawpara=("<strong>Archivos raw:</strong> descarga los archivos raw de tu grupo del Google Drive de la clase, luego crea tus carpetas e imp&oacute;rtalos a Lightroom Classic (los pasos completos est&aacute;n en el Paso 01). Ya deber&iacute;as tener instalados los presets de hoja de contactos de Lightroom; si no, est&aacute;n en el resumen del curso de Fotograf&iacute;a 2A." if es
             else "<strong>Raw files:</strong> download your group&rsquo;s raw files from the class Google Drive, then set up your folders and import into Lightroom Classic (full steps on Step 01). You should already have the Lightroom contact sheet presets installed; if not, they are on the Photography 2A course overview.")
    gdlabel="Google Drive: Archivos Raw" if es else "Google Drive: Raw Files"
    reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
    ref=REFLECT_ES if es else REFLECT_EN
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + para(rawpara)
      + '<div style="margin:2px 0 14px;">' + dl_link(GDRIVE, gdlabel, download=False) + '</div>'
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ref, reflabel, row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

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

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 2A &bull; Studio Session","Studio Session","Photograph the Panther of the Quarter honorees.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Panther of the Quarter Portraits",
        para("Our studio is hosting the Panther of the Quarter (POTQ) honorees. There are 20 honorees to photograph for the school newsletter. For each honoree you will create a waist-up portrait and a shoulder-up headshot in our studio, then edit the results to a professional finish.")
        + framed(HEADER,"The three-person studio crew at work, labeled Art Director, Photographer, and Lighting Assistant, with the Talent posing on the backdrop"))
    en+=downloads_block(False)
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

    es=banner("Fotograf&iacute;a 2A &bull; Sesi&oacute;n de Estudio","Sesi&oacute;n de Estudio","Fotograf&iacute;a a los honorados Pantera del Trimestre.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","Retratos de la Pantera del Trimestre",
        para("Nuestro estudio recibe a los honorados de la Pantera del Trimestre (POTQ). Hay 20 honorados que fotografiar para el bolet&iacute;n de la escuela. Para cada honorado crear&aacute;s un retrato de cintura para arriba y un retrato de hombros para arriba (headshot) en nuestro estudio, y luego editar&aacute;s los resultados con un acabado profesional.")
        + framed(HEADER,"El equipo de estudio de tres personas trabajando, con las etiquetas Director de Arte, Fot&oacute;grafo y Asistente de Iluminaci&oacute;n, y el Talento posando frente al fondo"))
    es+=downloads_block(True)
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

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Studio Session | Photography 2A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Studio Session &bull; Step 1","Capture and Import","Photograph in the studio, then import your take.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 contact sheet:","a contact sheet of your entire take (high-resolution JPG), uploaded to this Canvas assignment.")])
    en+=card("BEFORE YOU START / ONEDRIVE","Set Up Your Folders",
        para("Do this first so your files stay safe in the cloud.")
        + steps([
            ("Check OneDrive Is Syncing","Look at the OneDrive cloud icon in the top-right menu bar, next to the clock. If it shows a red X or a warning, click it and sign in with your school account to clear it."),
            ("Make Your Folders","In Finder, open <strong>OneDrive &gt; Photography</strong>. Make a folder called <strong>POTQ</strong>, and inside it make a folder called <strong>Raw</strong> (so the path is OneDrive &gt; Photography &gt; POTQ &gt; Raw)."),
            ("Download Your Raw Files","Open the class <strong>Google Drive</strong> (link on this module&rsquo;s Overview page, marked M at the top), find your group&rsquo;s honoree files, and download them into your <strong>Raw</strong> folder."),
        ]))
    en+=card("IN THE STUDIO / THE SESSION","Photograph Your Honorees",
        para("In your group, rotate through the three roles and photograph your assigned honoree or honorees. Capture two frames of each: a waist-up portrait and a headshot.")
        + bullets([
            ("Photographer:","dial in the camera settings and frame each photo: waist-up, then shoulders-up."),
            ("Art Director:","greet the honoree, learn their name and favored side, pose them, and keep them relaxed. Check posture and hair before each frame."),
            ("Lighting Assistant:","set the height and angle of the Westcott Eyelighter reflector so the light is even and flattering."),
        ]))
    en+=card("IMPORT / LIGHTROOM CLASSIC","Import and Contact Sheet",
        steps([
            ("Import Your Take","Open <strong>Lightroom Classic</strong>. Click <strong>Import</strong>, point to your <strong>Raw</strong> folder, select all your group&rsquo;s images, and import them."),
            ("Build a Full-Take Contact Sheet","Using your contact sheet preset (it is also on the Photography 2A course overview if you need it), build a contact sheet of your <strong>entire take</strong>: every image your group captured. Use more than one sheet if you have a lot of images."),
            ("Export the Contact Sheet","Export the contact sheet as a high-resolution JPG so you can turn it in."),
        ]))

    es=banner("Sesi&oacute;n de Estudio &bull; Paso 1","Captura e Importa","Fotograf&iacute;a en el estudio, luego importa tu toma.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 hoja de contactos:","una hoja de contactos de toda tu toma (JPG de alta resoluci&oacute;n), subida a esta tarea de Canvas.")])
    es+=card("ANTES DE EMPEZAR / ONEDRIVE","Crea Tus Carpetas",
        para("Haz esto primero para que tus archivos queden seguros en la nube.")
        + steps([
            ("Revisa que OneDrive Est&eacute; Sincronizando","Mira el &iacute;cono de nube de OneDrive en la barra de men&uacute;s arriba a la derecha, junto al reloj. Si muestra una X roja o una advertencia, haz clic e inicia sesi&oacute;n con tu cuenta escolar para quitarla."),
            ("Crea Tus Carpetas","En Finder, abre <strong>OneDrive &gt; Photography</strong>. Crea una carpeta llamada <strong>POTQ</strong> y dentro de ella una carpeta llamada <strong>Raw</strong> (la ruta queda OneDrive &gt; Photography &gt; POTQ &gt; Raw)."),
            ("Descarga Tus Archivos Raw","Abre el <strong>Google Drive</strong> de la clase (el enlace est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, marcada con M arriba), busca los archivos del honorado de tu grupo y desc&aacute;rgalos en tu carpeta <strong>Raw</strong>."),
        ]))
    es+=card("EN EL ESTUDIO / LA SESI&Oacute;N","Fotograf&iacute;a a Tus Honorados",
        para("En tu grupo, roten por los tres roles y fotograf&iacute;en a su honorado o honorados. Captura dos tomas de cada uno: un retrato de cintura para arriba y un headshot.")
        + bullets([
            ("Fot&oacute;grafo:","ajusta la c&aacute;mara y encuadra cada toma: cintura para arriba, luego hombros para arriba."),
            ("Director de Arte:","saluda al honorado, aprende su nombre y su lado preferido, p&oacute;salo y mantenlo relajado. Revisa la postura y el cabello antes de cada toma."),
            ("Asistente de Iluminaci&oacute;n:","ajusta la altura y el &aacute;ngulo del reflector Westcott Eyelighter para que la luz sea pareja y favorecedora."),
        ]))
    es+=card("IMPORTA / LIGHTROOM CLASSIC","Importa y Hoja de Contactos",
        steps([
            ("Importa Tu Toma","Abre <strong>Lightroom Classic</strong>. Haz clic en <strong>Importar</strong>, apunta a tu carpeta <strong>Raw</strong>, selecciona todas las im&aacute;genes de tu grupo e imp&oacute;rtalas."),
            ("Arma una Hoja de Contactos de Toda la Toma","Con tu preset de hoja de contactos (tambi&eacute;n en el resumen del curso de Fotograf&iacute;a 2A si lo necesitas), arma una hoja de contactos de <strong>toda tu toma</strong>: cada imagen que captur&oacute; tu grupo. Usa m&aacute;s de una hoja si tienes muchas im&aacute;genes."),
            ("Exporta la Hoja de Contactos","Exporta la hoja de contactos como JPG de alta resoluci&oacute;n para poder entregarla."),
        ]))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Capture and Import | Studio Session | Photography 2A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Studio Session &bull; Step 2","Cull and Edit","Make four finals: two crops, in color and black and white.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 contact sheet:","a contact sheet of your four final images, exported as a high-resolution JPG."),
         ("4 images:","your four finals as high-resolution JPGs: <strong>waist_up_color</strong>, <strong>headshot_color</strong>, <strong>waist_up_bw</strong>, and <strong>headshot_bw</strong>."),
         ("More than one honoree?","if your group photographed more than one honoree, upload a contact sheet plus four images for each. The minimum to complete this step is one honoree (contact sheet + 4 images).")])
    en+=card("EDIT / LIGHTROOM CLASSIC","Cull, Edit, and Make 4 Finals",
        float_right(EDIT_EXAMPLE,"A raw studio portrait on the left next to the edited, retouched final on the right","Your editing goal: raw frame on the left, finished portrait on the right.")
        + para("Now you will edit in Lightroom Classic. For each honoree you will finish <strong>four</strong> images: two crops in color, and those same two crops in black and white. You know Lightroom a bit already; the new part here is duplicating a photo and converting the copy to black and white the right way. Work through the steps in order.")
        + note("Keep your color version. You will DUPLICATE each edited photo and turn the copy black and white, so you end up with BOTH the color and the black-and-white version.")
        + steps([
            ("Cull Your Best Frames","In the <strong>Library</strong> module, look through your whole take of your honoree. Select the frames where they look their best: eyes open, natural expression, sharp focus. Press <strong>P</strong> to flag your favorites, then work from those."),
            ("Make Your Two Crops","You need two different crops. Grab the <strong>Crop tool (R)</strong> and make a <strong>waist-up portrait</strong> (framed from about the waist up) and a <strong>headshot</strong> (cropped tighter, from the shoulders up). You can crop one strong frame two ways, or use two different frames. These are your two <strong>color</strong> images."),
            ("Edit the Color Versions","Switch to the <strong>Develop</strong> module. Make each crop look its best: if the face is dark, raise <strong>Exposure</strong> or <strong>Shadows</strong>; balance the highlights; use the <strong>Healing tool</strong> to gently remove blemishes (keep skin natural). Try a <strong>portrait preset</strong> and fine-tune. When both crops look great, those are your two finished color photos."),
            ("Duplicate: Create a Virtual Copy","Now keep the color AND make a black-and-white version without losing your color edit. <strong>Right-click</strong> the photo (in the Develop filmstrip or the Library grid) and choose <strong>Create Virtual Copy</strong> (shortcut <strong>Command + &#39;</strong>). Lightroom adds a second copy you can edit on its own. Do this for <strong>both</strong> crops, so you now have four photos: two color originals and two copies to convert."),
            ("Convert the Copy to Black &amp; White with a Preset","Select a <strong>virtual copy</strong>. <strong>Do NOT just drag Saturation to &minus;100</strong>: that makes a flat, muddy gray. Use a real black-and-white conversion instead: open the <strong>Presets</strong> panel on the left and click a preset in the <strong>B&amp;W</strong> (Black &amp; White) group; or open the <strong>Profile Browser</strong> (next to &lsquo;Profile&rsquo; at the top of the Basic panel) and choose a <strong>Monochrome / B&amp;W</strong> profile. This gives a rich black and white with real contrast. Do this for both virtual copies."),
            ("Fine-Tune the Black &amp; White","With the black-and-white photo selected, open the <strong>B&amp;W</strong> panel (the color mix). Each slider brightens or darkens what used to be a color: for example, lowering <strong>Red / Orange</strong> deepens skin tones and raising them lifts the face. Nudge the sliders and the <strong>Contrast</strong> until the portrait looks strong."),
            ("Export All Four as JPG","Select all four photos (2 color + 2 black and white), go to <strong>File &gt; Export</strong>, and export as <strong>high-resolution JPG</strong>. Rename them clearly: <strong>waist_up_color</strong>, <strong>headshot_color</strong>, <strong>waist_up_bw</strong>, and <strong>headshot_bw</strong>."),
        ]))
    en+=card("CONTACT SHEET / SHOW YOUR FOUR","Build a Contact Sheet of Your 4 Finals",
        para("After your four images are done, build a <strong>contact sheet</strong> of them using your contact sheet preset (it is also on the Photography 2A course overview if you need it), and export it as a high-resolution JPG. This puts all four finals on one sheet."))

    es=banner("Sesi&oacute;n de Estudio &bull; Paso 2","Selecciona y Edita","Haz cuatro finales: dos recortes, en color y en blanco y negro.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 hoja de contactos:","una hoja de contactos de tus cuatro im&aacute;genes finales, exportada como JPG de alta resoluci&oacute;n."),
         ("4 im&aacute;genes:","tus cuatro finales como JPG de alta resoluci&oacute;n: <strong>waist_up_color</strong>, <strong>headshot_color</strong>, <strong>waist_up_bw</strong> y <strong>headshot_bw</strong>."),
         ("&iquest;M&aacute;s de un honorado?","si tu grupo fotografi&oacute; a m&aacute;s de un honorado, sube una hoja de contactos m&aacute;s cuatro im&aacute;genes por cada uno. El m&iacute;nimo para completar este paso es un honorado (hoja de contactos + 4 im&aacute;genes).")])
    es+=card("EDITA / LIGHTROOM CLASSIC","Selecciona, Edita y Haz 4 Finales",
        float_right(EDIT_EXAMPLE,"Un retrato de estudio sin editar a la izquierda junto al final editado y retocado a la derecha","Tu meta de edici&oacute;n: la toma sin editar a la izquierda, el retrato terminado a la derecha.")
        + para("Ahora editar&aacute;s en Lightroom Classic. Para cada honorado terminar&aacute;s <strong>cuatro</strong> im&aacute;genes: dos recortes en color y esos mismos dos recortes en blanco y negro. Ya conoces Lightroom un poco; lo nuevo aqu&iacute; es duplicar una foto y convertir la copia a blanco y negro de la forma correcta. Ve paso a paso, en orden.")
        + note("Conserva tu versi&oacute;n en color. Vas a DUPLICAR cada foto editada y convertir la copia a blanco y negro, para que te queden LAS DOS: la de color y la de blanco y negro.")
        + steps([
            ("Selecciona Tus Mejores Cuadros","En el m&oacute;dulo <strong>Biblioteca</strong>, revisa toda tu toma del honorado. Elige los cuadros donde se ve mejor: ojos abiertos, expresi&oacute;n natural, enfoque n&iacute;tido. Presiona <strong>P</strong> para marcar tus favoritos y trabaja desde ah&iacute;."),
            ("Haz Tus Dos Recortes","Necesitas dos recortes diferentes. Toma la <strong>herramienta Recortar (R)</strong> y haz un <strong>retrato de cintura para arriba</strong> (encuadrado m&aacute;s o menos de la cintura para arriba) y un <strong>headshot</strong> (recortado m&aacute;s cerca, de los hombros para arriba). Puedes recortar un buen cuadro de dos formas, o usar dos cuadros distintos. Estas son tus dos im&aacute;genes en <strong>color</strong>."),
            ("Edita las Versiones en Color","Cambia al m&oacute;dulo <strong>Revelar</strong>. Haz que cada recorte se vea de lo mejor: si la cara est&aacute; oscura, sube <strong>Exposici&oacute;n</strong> o <strong>Sombras</strong>; equilibra las luces; usa la <strong>herramienta Corrector</strong> para quitar imperfecciones con cuidado (mant&eacute;n la piel natural). Prueba un <strong>preset de retrato</strong> y aj&uacute;stalo. Cuando los dos recortes se vean muy bien, esas son tus dos fotos en color terminadas."),
            ("Duplica: Crea una Copia Virtual","Ahora conserva el color Y haz una versi&oacute;n en blanco y negro sin perder tu edici&oacute;n en color. <strong>Haz clic derecho</strong> en la foto (en la tira de miniaturas de Revelar o en la cuadr&iacute;cula de Biblioteca) y elige <strong>Crear copia virtual</strong> (atajo <strong>Command + &#39;</strong>). Lightroom agrega una segunda copia que puedes editar por separado. Hazlo en <strong>ambos</strong> recortes, para que tengas cuatro fotos: dos originales en color y dos copias para convertir."),
            ("Convierte la Copia a Blanco y Negro con un Preset","Selecciona una <strong>copia virtual</strong>. <strong>NO bajes la Saturaci&oacute;n a &minus;100</strong>: eso da un gris plano y sucio. Usa una conversi&oacute;n real a blanco y negro: abre el panel <strong>Presets (Ajustes preestablecidos)</strong> a la izquierda y haz clic en un preset del grupo <strong>B&amp;N</strong> (Blanco y Negro); o abre el <strong>Explorador de perfiles</strong> (junto a &lsquo;Perfil&rsquo; arriba del panel B&aacute;sico) y elige un perfil <strong>Monocromo / B&amp;N</strong>. Esto da un blanco y negro rico y con contraste. Hazlo en las dos copias virtuales."),
            ("Ajusta el Blanco y Negro","Con la foto en blanco y negro seleccionada, abre el panel <strong>B&amp;N</strong> (la mezcla de color). Cada control aclara u oscurece lo que antes era un color: por ejemplo, bajar <strong>Rojo / Naranja</strong> hace m&aacute;s profundos los tonos de piel y subirlos aclara la cara. Mueve los controles y el <strong>Contraste</strong> hasta que el retrato se vea fuerte."),
            ("Exporta las Cuatro como JPG","Selecciona las cuatro fotos (2 en color + 2 en blanco y negro), ve a <strong>Archivo &gt; Exportar</strong> y exporta como <strong>JPG de alta resoluci&oacute;n</strong>. Renombra con claridad: <strong>waist_up_color</strong>, <strong>headshot_color</strong>, <strong>waist_up_bw</strong> y <strong>headshot_bw</strong>."),
        ]))
    es+=card("HOJA DE CONTACTOS / MUESTRA TUS CUATRO","Arma una Hoja de Contactos de Tus 4 Finales",
        para("Cuando tus cuatro im&aacute;genes est&eacute;n listas, arma una <strong>hoja de contactos</strong> de ellas con tu preset de hoja de contactos (tambi&eacute;n est&aacute; en el resumen del curso de Fotograf&iacute;a 2A si lo necesitas), y exp&oacute;rtala como JPG de alta resoluci&oacute;n. As&iacute; quedan las cuatro finales en una sola hoja."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a><a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Cull and Edit | Studio Session | Photography 2A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 03 ----------------
def step03():
    en=banner("Studio Session &bull; Step 3","Turn In Your Reflection","Reflect on the process, your role, and your edits.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
    en+=card("STEP 03 / REFLECT","Complete and Upload the Reflection",
        para("Finish the project with a short reflection. It asks about your group and roles, the whole studio process, what you enjoyed and found hardest, and how you made your editing choices.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + bullets([
            ("Open it:","open the reflection Word document (.docx) from your project folder."),
            ("Answer every question:","type your answers in the boxes, in full sentences."),
            ("Save and upload:","save the document and upload it to this Canvas assignment."),
        ])
        + note("Answer honestly, in your own words."))

    es=banner("Sesi&oacute;n de Estudio &bull; Paso 3","Entrega Tu Reflexi&oacute;n","Reflexiona sobre el proceso, tu rol y tus ediciones.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completo, subido a esta tarea de Canvas.")])
    es+=card("PASO 03 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        para("Termina el proyecto con una reflexi&oacute;n corta. Pregunta sobre tu grupo y los roles, todo el proceso del estudio, qu&eacute; disfrutaste y qu&eacute; fue lo m&aacute;s dif&iacute;cil, y c&oacute;mo tomaste tus decisiones de edici&oacute;n.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + bullets([
            ("&Aacute;brelo:","abre el documento de Word (.docx) de la reflexi&oacute;n desde tu carpeta del proyecto."),
            ("Contesta cada pregunta:","escribe tus respuestas en los cuadros, en oraciones completas."),
            ("Guarda y sube:","guarda el documento y s&uacute;belo a esta tarea de Canvas."),
        ])
        + note("Contesta con honestidad, en tus propias palabras."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)+dot("",'3',"Step 03",True)
    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page("Step 3: Reflection | Studio Session | Photography 2A | PVHS", nav("Step 03",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
