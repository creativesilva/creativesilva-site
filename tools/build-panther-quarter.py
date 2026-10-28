#!/usr/bin/env python3
# Photography 2A - Module 10: Panther of the Quarter Portrait Studio.
# A REAL-CLIENT group studio job: students photograph the Panther of the Quarter honorees for
# Mr. Movahedi (assistant principal). Groups of three run four roles (Greeter, Honoree Assistant,
# Lighting Assistant, Photographer). One photographer per group, but all three SHARE the take and
# each one edits + submits their OWN JPGs. Overview + 3 steps, bilingual, 5th-grade, camera-kit
# (studio) so NO own-device fresh-photos note. Capture is RAW only (Chris, 2026-10-28).
#   Step 01 Overview: read + download the project folder (POTQ_10-28-26 with RAW_Images/ + both
#     reflection docs inside, one zip).
#   Step 02 Capture & Contact: run the studio flow, share the files all three ways, import to
#     Lightroom, turn in a 12-Up contact sheet of the full take (high-res JPG).
#   Step 03 Cull, Edit & Deliver: best waist + best chest edited JPG per honoree.
#   Step 04 Reflection: the bilingual reflection .docx (inside the downloaded project folder).
# Hero = Chris's poster (2026-10-28_Panther_Quarter_Studio_Poster_v4.pdf) rasterized. Float slots
# are gated off (HAVE_*_FLOAT=False) and render NOTHING until photos arrive (no live placeholder).
import os, re
from silva_framework import *

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"

IMGDIR=f"{SITE}/assets/images/photo2/panther-quarter"
HEADER=f"{IMGDIR}/header-v1.jpg"          # the poster graphic
S1_FLOAT=f"{IMGDIR}/capture-float-v1.jpg"
S2_FLOAT=f"{IMGDIR}/edit-float-v1.jpg"
S3_FLOAT=f"{IMGDIR}/reflection-float-v1.jpg"
HAVE_HEADER=True
HAVE_S1_FLOAT=False
HAVE_S2_FLOAT=False
HAVE_S3_FLOAT=False

PROJECT_ZIP=f"{SITE}/assets/course-documents/Panther-of-the-Quarter-Project-Folder.zip"

OVER="photo2-panther-quarter-overview.html"
S1="photo2-panther-quarter-step01-capture-contact.html"
S2="photo2-panther-quarter-step02-cull-edit-deliver.html"
S3="photo2-panther-quarter-step03-reflection.html"

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Panther of the Quarter</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

DOTS_TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04")]
def dots_for(active_idx):
    hrefs=[OVER,S1,S2,S3]
    r=""
    for i,(lab,title) in enumerate(DOTS_TITLES):
        r+=dot("" if i==active_idx else hrefs[i], lab, title, i==active_idx, module=False)
    return r

PANTHER_STANDARDS=[
  {"code":"SA.17.5","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Equipment &amp; Image Production","es_title":"Equipo y Producci&oacute;n de Imagen",
   "en_desc":"You run a lit studio, set the camera to f/5.6, focus on the eyes, and capture in RAW.",
   "es_desc":"Manejas un estudio con luces, pones la c&aacute;mara en f/5.6, enfocas en los ojos y capturas en RAW."},
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You make even, flattering portraits with a steady backdrop and the same crops every time.",
   "es_desc":"Haces retratos parejos y favorecedores con un fondo estable y los mismos encuadres cada vez."},
  {"code":"SA.17.6","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Digital Editing &amp; Workflow","es_title":"Edici&oacute;n Digital y Flujo de Trabajo",
   "en_desc":"You import RAW files, build contact sheets, edit in Lightroom Classic, and export clean JPGs.",
   "es_desc":"Importas archivos RAW, creas hojas de contactos, editas en Lightroom Classic y exportas JPG limpios."},
  {"code":"SA.17.8","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Real Client Delivery","es_title":"Entrega a un Cliente Real",
   "en_desc":"You deliver named, correctly labeled portraits to a real client to a clear standard, on time.",
   "es_desc":"Entregas retratos con nombre y bien etiquetados a un cliente real, con un est&aacute;ndar claro y a tiempo."},
]

# --- module-local helpers ---

def project_downloads(es):
    # ORANGE downloads: the ready-made project folder zip (RAW_Images/ + both reflection docs inside).
    if es:
        heading="Descarga Tu Carpeta del Proyecto"
        lead=("Descarga tu carpeta del proyecto. Es un archivo .zip. Al abrirlo tendr&aacute;s la carpeta "
              "<strong>POTQ_10-28-26</strong>, y adentro hay una carpeta <strong>RAW_Images</strong> para tus fotos RAW "
              "y tu documento de reflexi&oacute;n (en ingl&eacute;s y en espa&ntilde;ol). Todo tu proyecto vive aqu&iacute;.")
        label="Carpeta del Proyecto (.zip)"
        note_t=("<strong style=\"color:#ffb27c;\">Mantente organizado:</strong> cuando el .zip termine de descargarse, "
                "&aacute;brelo y mueve la carpeta <strong>POTQ_10-28-26</strong> a "
                f"OneDrive &rarr; {AREA}. Guarda tus fotos RAW dentro de <strong>RAW_Images</strong>, "
                "y deja tu documento de reflexi&oacute;n en la carpeta.")
    else:
        heading="Download Your Project Folder"
        lead=("Download your project folder. It is a .zip file. When you open it you get the "
              "<strong>POTQ_10-28-26</strong> folder, and inside it is a <strong>RAW_Images</strong> folder for your RAW "
              "photos and your reflection document (English and Spanish). Your whole project lives here.")
        label="Project Folder (.zip)"
        note_t=("<strong style=\"color:#ffb27c;\">Stay organized:</strong> when the .zip finishes downloading, "
                "open it and move the <strong>POTQ_10-28-26</strong> folder into "
                f"OneDrive &rarr; {AREA}. Keep your RAW photos inside <strong>RAW_Images</strong>, "
                "and leave your reflection document in the folder.")
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(PROJECT_ZIP, label, row=True)
      + '</div>'
      + f'<div style="margin-top:16px;font-size:12pt;color:rgba(255,255,255,0.82);line-height:1.55;">{note_t}</div>'
      + '</div>')

def studio_settings(es):
    # RED camera + lighting settings. Preset studio: students only confirm f/5.6, focus eyes, RAW.
    red="#f90101"
    raw_badge=f'<img src="{RAW_BADGE}" alt="RAW" style="height:1.5em;width:auto;vertical-align:middle;margin:0 3px;display:inline-block;" />'
    if es:
        title="Ajustes de C&aacute;mara e Iluminaci&oacute;n"
        lead=("El estudio ya est&aacute; listo. Las luces y la l&iacute;nea de cinta est&aacute;n fijas: no las muevas. "
               "Lo &uacute;nico que cambia es el reflector, para la altura de cada homenajeado.")
        items=[
            ("Formato:",f"captura en RAW {raw_badge} para tener el mayor detalle al editar."),
            ("Apertura:","f/5.6, para retratos n&iacute;tidos y claros."),
            ("Enfoque:","en los ojos, siempre."),
            ("Luces:","luz trasera teal y luz de d&iacute;a como luz principal, ambas fijas."),
            ("Reflector:","el Asistente de Iluminaci&oacute;n sube o baja el Westcott Eyelighter para la altura del homenajeado."),
        ]
        note_t="Pon f/5.6, enfoca en los ojos y captura en RAW. No cambies las luces ni la l&iacute;nea de cinta."
    else:
        title="Camera &amp; Lighting Settings"
        lead=("The studio is already set up. The lights and the tape line are preset: do not move them. "
               "The only thing that changes is the reflector, for each honoree&rsquo;s height.")
        items=[
            ("Format:",f"capture in RAW {raw_badge} so you have the most detail to edit."),
            ("Aperture:","f/5.6, for sharp, clear portraits."),
            ("Focus:","on the eyes, every time."),
            ("Lights:","a teal backlight and a daylight key light, both preset."),
            ("Reflector:","the Lighting Assistant raises or lowers the Westcott Eyelighter for the honoree&rsquo;s height."),
        ]
        note_t="Set f/5.6, focus on the eyes, and capture in RAW. Do not change the lights or the tape line."
    lead_html=f'<div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{lead}</span></div>'
    note_box=f'<div style="background:rgba(249,1,1,0.10);border:1px solid rgba(249,1,1,0.30);border-left:4px solid {red};padding:11px 14px;margin:8px 0 0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.92);line-height:1.55;"><strong>{note_t}</strong></div>'
    return (f'<div style="background:linear-gradient(180deg,rgba(249,1,1,0.06) 0%,rgba(249,1,1,0.02) 100%);border:1px solid rgba(249,1,1,0.26);border-left:6px solid {red};padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(CAMSET_ICON, title, "#f90101", "#ff8f8f")
      + lead_html + bullets(items, accent=red) + note_box + '</div>')

# ================= OVERVIEW (Step 01) =================
def overview():
    en=banner("Module 10 &bull; Step 01","Panther of the Quarter: Start Here",
        "Read this page and download your project folder. This is a real portrait job for a real client.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","Step 01 &middot; Overview &amp; Download","A Real Portrait Job for Mr. Movahedi",
        para("This is a real job for a real client. <strong>Mr. Movahedi</strong>, our assistant principal, needs clean portraits of every <strong>Panther of the Quarter</strong> honoree. Your class is the studio that makes them.")
        + para("You work in small groups with <strong>four roles</strong>. Honorees come to the studio one at a time. Each honoree gets <strong>7 frames</strong>: 1 name board photo, then 6 portraits (3 positions, each at waist level and chest level).")
        + para("Every honoree gets the same quality: <strong>sharp eyes, even light, the same backdrop, the same crops,</strong> and the right name on every file.")
        + (framed(HEADER,"Panther of the Quarter Portrait Studio poster: the four roles and the name-board-first, six-frame sequence") if HAVE_HEADER else ""))
    en+=standards_box(False, PANTHER_STANDARDS)
    en+=project_downloads(False)
    en+=card("CLIENT / REAL-WORLD READINESS","Treat Mr. Movahedi Like a Real Client",
        para("Mr. Movahedi is counting on us. This is about <strong>discipline, effort, ownership,</strong> and real-world readiness: the way real photographers work for a real client.")
        + bullets([
            ("The product:","edited portraits of each honoree."),
            ("The standard:","sharp, evenly lit, same backdrop, same crops, correct names."),
            ("Due:","Friday, or sooner, as soon as your edits are done."),
        ])
        + note("Say it out loud with your group: every honoree gets the same quality and the right name on every file."))
    en+=card("YOUR GROUP / FOUR ROLES, ONE FLOW","Four Roles",
        para("Your group runs four roles. See the poster above for what each role does, step by step.")
        + bullets([
            ("1. Greeter:","welcomes each honoree, brings them to the green room, then to the tape line when the studio is open."),
            ("2. Honoree Assistant:","asks the name, writes it on the board, and helps the honoree pose."),
            ("3. Lighting Assistant:","moves the reflector up or down for the honoree&rsquo;s height. Does not move the lights."),
            ("4. Photographer:","captures the name board first, then waist and chest at each position. Checks that the eyes are sharp."),
        ])
        + note("Groups rotate roles after each honoree, so everyone photographs, guides, and lights."))
    en+=card("EVERY HONOREE / THE FRAME SEQUENCE","Name Board First, Then 6 Portraits",
        para("The order is the same for every honoree: the name board first, then three positions, and each position gets a waist crop and a chest crop.")
        + bullets([
            ("Name board:","1 photo of the whiteboard with the honoree&rsquo;s name. This is a reference, not delivered."),
            ("Position 1, favored shoulder:","waist level, then chest level."),
            ("Position 2, straight on:","waist level, then chest level."),
            ("Position 3, opposite shoulder:","waist level, then chest level."),
        ])
        + note("Waist level is framed at the waist. Chest level is a tighter crop, from the chest up. That is 6 portraits plus the name board, 7 frames in all."))
    en+=card("HOW IT WORKS / YOUR PLAN","Your Next Three Steps",
        para("You are on Step 01 now: read this page and download your project folder above. Here are the three steps that follow.")
        + bullets([
            ("Step 02 &middot; Capture &amp; Contact Sheet:","run the studio flow and capture your honorees in RAW. Share the files so all three of you have them, then turn in a 12-Up contact sheet of your full take."),
            ("Step 03 &middot; Cull, Edit &amp; Deliver:","choose your best waist and best chest for each honoree, edit to the client standard, and turn in your edited JPGs."),
            ("Step 04 &middot; Reflection:","tell how your group worked and how you made your editing choices."),
        ])
        + note("One person photographs, but all three of you edit and submit your own work."))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Honoree","A person chosen as Panther of the Quarter. The person you photograph."),
           ("Reflector","A panel that bounces light back onto the face to fill shadows. Here it is the Westcott Eyelighter."),
           ("Catchlight","The small bright spot of light you see in the eyes. It makes the eyes look alive."),
           ("Crop","How tightly you frame the photo. Here you make a waist-level crop and a tighter chest-level crop."),
           ("Contact Sheet","One page that shows all your frames as small thumbnails, so you can compare them."),
           ("Cull","To look through all your frames and keep only the best ones.")]))
    en+=next_up("UP NEXT &middot; STEP 02 - Capture &amp; Contact Sheet","Run the studio flow, capture in RAW, share the files, and build a 12-Up contact sheet of your full take.")

    es=banner("M&oacute;dulo 10 &bull; Paso 01","Panther of the Quarter: Empieza Aqu&iacute;",
        "Lee esta p&aacute;gina y descarga tu carpeta del proyecto. Este es un trabajo de retratos real para un cliente real.","#top","Back to English")
    es+=type_card("overview","Paso 01 &middot; Resumen y Descarga","Un Trabajo de Retratos Real para el Sr. Movahedi",
        para("Este es un trabajo real para un cliente real. El <strong>Sr. Movahedi</strong>, nuestro subdirector, necesita retratos limpios de cada homenajeado de <strong>Panther of the Quarter</strong>. Tu clase es el estudio que los hace.")
        + para("Trabajas en grupos peque&ntilde;os con <strong>cuatro roles</strong>. Los homenajeados llegan al estudio uno a la vez. Cada homenajeado recibe <strong>7 im&aacute;genes</strong>: 1 foto de la pizarra con el nombre, y luego 6 retratos (3 posiciones, cada una a nivel de cintura y a nivel de pecho).")
        + para("Cada homenajeado recibe la misma calidad: <strong>ojos n&iacute;tidos, luz pareja, el mismo fondo, los mismos encuadres,</strong> y el nombre correcto en cada archivo.")
        + (framed(HEADER,"P&oacute;ster del estudio de retratos Panther of the Quarter: los cuatro roles y la secuencia de la pizarra del nombre primero y seis im&aacute;genes") if HAVE_HEADER else ""))
    es+=standards_box(True, PANTHER_STANDARDS)
    es+=project_downloads(True)
    es+=card("CLIENTE / PREPARACI&Oacute;N PARA EL MUNDO REAL","Trata al Sr. Movahedi Como un Cliente Real",
        para("El Sr. Movahedi cuenta con nosotros. Esto es sobre <strong>disciplina, esfuerzo, responsabilidad</strong> y preparaci&oacute;n para el mundo real: la forma en que un fot&oacute;grafo real trabaja para un cliente real.")
        + bullets([
            ("El producto:","retratos editados de cada homenajeado."),
            ("El est&aacute;ndar:","n&iacute;tidos, bien iluminados, el mismo fondo, los mismos encuadres, nombres correctos."),
            ("Entrega:","el viernes, o antes, en cuanto terminen tus ediciones."),
        ])
        + note("D&iacute;ganlo en voz alta en tu grupo: cada homenajeado recibe la misma calidad y el nombre correcto en cada archivo."))
    es+=card("TU GRUPO / CUATRO ROLES, UN FLUJO","Cuatro Roles",
        para("Tu grupo maneja cuatro roles. Mira el p&oacute;ster de arriba para ver qu&eacute; hace cada rol, paso por paso.")
        + bullets([
            ("1. Recepcionista:","recibe a cada homenajeado, lo lleva al green room y luego a la l&iacute;nea de cinta cuando el estudio est&aacute; libre."),
            ("2. Asistente del Homenajeado:","pregunta el nombre, lo escribe en la pizarra y ayuda al homenajeado a posar."),
            ("3. Asistente de Iluminaci&oacute;n:","sube o baja el reflector para la altura del homenajeado. No mueve las luces."),
            ("4. Fot&oacute;grafo:","captura la pizarra del nombre primero, luego cintura y pecho en cada posici&oacute;n. Revisa que los ojos est&eacute;n n&iacute;tidos."),
        ])
        + note("Los grupos rotan los roles despu&eacute;s de cada homenajeado, para que todos fotograf&iacute;en, gu&iacute;en e iluminen."))
    es+=card("CADA HOMENAJEADO / LA SECUENCIA","La Pizarra del Nombre Primero, Luego 6 Retratos",
        para("El orden es el mismo para cada homenajeado: la pizarra del nombre primero, luego tres posiciones, y cada posici&oacute;n recibe un encuadre de cintura y uno de pecho.")
        + bullets([
            ("Pizarra del nombre:","1 foto de la pizarra con el nombre del homenajeado. Es una referencia, no se entrega."),
            ("Posici&oacute;n 1, hombro favorito:","nivel de cintura, luego nivel de pecho."),
            ("Posici&oacute;n 2, de frente:","nivel de cintura, luego nivel de pecho."),
            ("Posici&oacute;n 3, hombro opuesto:","nivel de cintura, luego nivel de pecho."),
        ])
        + note("Nivel de cintura se encuadra en la cintura. Nivel de pecho es un encuadre m&aacute;s cerrado, del pecho hacia arriba. Son 6 retratos m&aacute;s la pizarra del nombre, 7 im&aacute;genes en total."))
    es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Siguientes Tres Pasos",
        para("Est&aacute;s en el Paso 01: lee esta p&aacute;gina y descarga tu carpeta del proyecto arriba. Estos son los tres pasos que siguen.")
        + bullets([
            ("Paso 02 &middot; Captura y Hoja de Contactos:","maneja el flujo del estudio y captura a tus homenajeados en RAW. Comparte los archivos para que los tres los tengan, luego entrega una hoja de contactos de 12 de todo tu trabajo."),
            ("Paso 03 &middot; Selecciona, Edita y Entrega:","elige tu mejor cintura y tu mejor pecho de cada homenajeado, edita al est&aacute;ndar del cliente y entrega tus JPG editados."),
            ("Paso 04 &middot; Reflexi&oacute;n:","cuenta c&oacute;mo trabaj&oacute; tu grupo y c&oacute;mo tomaste tus decisiones de edici&oacute;n."),
        ])
        + note("Una persona fotograf&iacute;a, pero los tres editan y entregan su propio trabajo."))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Honoree (Homenajeado)","Una persona elegida como Panther of the Quarter. La persona que fotograf&iacute;as."),
           ("Reflector (Reflector)","Un panel que rebota la luz hacia la cara para rellenar las sombras. Aqu&iacute; es el Westcott Eyelighter."),
           ("Catchlight (Brillo en los Ojos)","El peque&ntilde;o punto de luz que ves en los ojos. Hace que los ojos se vean vivos."),
           ("Crop (Encuadre)","Qu&eacute; tan cerrado encuadras la foto. Aqu&iacute; haces un encuadre de cintura y uno m&aacute;s cerrado de pecho."),
           ("Contact Sheet (Hoja de Contactos)","Una p&aacute;gina que muestra todas tus im&aacute;genes como miniaturas, para compararlas."),
           ("Cull (Seleccionar)","Revisar todas tus im&aacute;genes y guardar solo las mejores.")]), True)
    es+=next_up("SIGUIENTE &middot; PASO 02 - Captura y Hoja de Contactos","Maneja el flujo del estudio, captura en RAW, comparte los archivos y arma una hoja de contactos de 12 de todo tu trabajo.")

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
    return wrap_page("Panther of the Quarter | Photography 2A | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ================= STEP 02: Capture & Contact =================
def step01():
    en=banner("Module 10 &bull; Step 02","Capture &amp; Contact Sheet",
        "Run the studio flow, capture in RAW, share the files, and turn in a 12-Up contact sheet of your full take.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("IN THE STUDIO / TAKE TURNS","Your Group Runs the Flow",
        para("Honorees arrive during the period. Your group runs the four-role flow for each one: the Greeter brings them in, the Honoree Assistant poses them, the Lighting Assistant sets the reflector, and the Photographer captures the 7 frames.")
        + (float_right(S1_FLOAT,"Pioneer Valley students running the Panther of the Quarter studio flow with a honoree on the tape line") if HAVE_S1_FLOAT else "")
        + bullets([
            ("One group at a time:","there is one set of lights and one tape line. Only the working group stands near the studio."),
            ("Rotate roles:","switch roles after each honoree, so everyone photographs, guides, and lights."),
            ("Be kind:","be warm and professional with every honoree. Keep the line moving so no one waits long."),
        ]))
    en+=deliverables_box(False,
        [("1 contact sheet:","your full take, every frame your group captured, built with the 12-Up contact sheet template and turned in as a high-resolution JPG. If your take fills more than one page, turn in each page.")])
    en+=studio_settings(False)
    en+=card("CAPTURE / EVERY HONOREE, 7 FRAMES","The Photographer&rsquo;s Order",
        para("Set f/5.6, focus on the eyes, and capture in RAW. Follow the same order for every honoree.")
        + steps([
            ("Name board first:","photograph the whiteboard with the honoree&rsquo;s name. This is your reference for who is who."),
            ("Position 1, favored shoulder:","capture waist level, then chest level."),
            ("Position 2, straight on:","capture waist level, then chest level."),
            ("Position 3, opposite shoulder:","capture waist level, then chest level."),
            ("Check the eyes:","look at the screen. Make sure the eyes are sharp before you release the honoree."),
            ("Call it out:","say &ldquo;Ready&rdquo; before each frame and &ldquo;Done&rdquo; after frame 6."),
        ])
        + note("That is 7 frames per honoree: the name board plus 6 portraits."))
    en+=card("SHARE / ALL THREE NEED THE FILES","Share Your Take with Your Group",
        para("One person photographs, but all three of you edit and turn in your own work. So everyone needs the same files. Share them one of these two ways.")
        + bullets([
            ("Share the memory card:","copy the RAW files off the card so all three group members get a copy."),
            ("Or use OneDrive:","put the RAW files in a shared OneDrive folder, then each person downloads them."),
            ("Then import:","each person moves the RAW files into their RAW_Images folder and imports them into Lightroom Classic."),
        ])
        + note("Do this before you leave. You cannot edit or turn in a contact sheet without the files."))
    en+=card("BUILD IT / CONTACT SHEET","Turn In a 12-Up Contact Sheet",
        steps([
            ("Import your RAW files:","in Lightroom Classic, import the full take from your RAW_Images folder."),
            ("Use the 12-Up template:","in the Print module, choose the 12-Up contact sheet template with your full take loaded."),
            ("Print to JPG:","use Print to File so it saves as a high-resolution JPG, then upload it here."),
        ])
        + note("Contact sheets are always turned in as a high-resolution JPG. Turn in your full take, every frame your group captured."))
    en+=next_up("UP NEXT &middot; STEP 03 - Cull, Edit &amp; Deliver","Choose your best waist and best chest for each honoree, edit to the client standard, and export your JPGs.")

    es=banner("M&oacute;dulo 10 &bull; Paso 02","Captura y Hoja de Contactos",
        "Maneja el flujo del estudio, captura en RAW, comparte los archivos y entrega una hoja de contactos de 12 de todo tu trabajo.","#top","Back to English")
    es+=card("EN EL ESTUDIO / TOMEN TURNOS","Tu Grupo Maneja el Flujo",
        para("Los homenajeados llegan durante el periodo. Tu grupo maneja el flujo de cuatro roles con cada uno: el Recepcionista lo trae, el Asistente del Homenajeado lo posa, el Asistente de Iluminaci&oacute;n ajusta el reflector y el Fot&oacute;grafo captura las 7 im&aacute;genes.")
        + (float_right(S1_FLOAT,"Estudiantes de Pioneer Valley manejando el flujo del estudio Panther of the Quarter con un homenajeado en la l&iacute;nea de cinta") if HAVE_S1_FLOAT else "")
        + bullets([
            ("Un grupo a la vez:","hay un solo juego de luces y una sola l&iacute;nea de cinta. Solo el grupo que trabaja se para cerca del estudio."),
            ("Roten los roles:","cambien de rol despu&eacute;s de cada homenajeado, para que todos fotograf&iacute;en, gu&iacute;en e iluminen."),
            ("S&eacute; amable:","s&eacute; c&aacute;lido y profesional con cada homenajeado. Mant&eacute;n la fila moviendo para que nadie espere mucho."),
        ]))
    es+=deliverables_box(True,
        [("1 hoja de contactos:","todo tu trabajo, cada imagen que tu grupo captur&oacute;, armada con la plantilla de hoja de contactos de 12 y entregada como un JPG de alta resoluci&oacute;n. Si tu trabajo llena m&aacute;s de una p&aacute;gina, entrega cada p&aacute;gina.")])
    es+=studio_settings(True)
    es+=card("CAPTURA / CADA HOMENAJEADO, 7 IM&Aacute;GENES","El Orden del Fot&oacute;grafo",
        para("Pon f/5.6, enfoca en los ojos y captura en RAW. Sigue el mismo orden con cada homenajeado.")
        + steps([
            ("La pizarra del nombre primero:","fotograf&iacute;a la pizarra con el nombre del homenajeado. Es tu referencia de qui&eacute;n es qui&eacute;n."),
            ("Posici&oacute;n 1, hombro favorito:","captura nivel de cintura, luego nivel de pecho."),
            ("Posici&oacute;n 2, de frente:","captura nivel de cintura, luego nivel de pecho."),
            ("Posici&oacute;n 3, hombro opuesto:","captura nivel de cintura, luego nivel de pecho."),
            ("Revisa los ojos:","mira la pantalla. Aseg&uacute;rate de que los ojos est&eacute;n n&iacute;tidos antes de soltar al homenajeado."),
            ("D&iacute;lo en voz alta:","di &ldquo;Ready&rdquo; antes de cada imagen y &ldquo;Done&rdquo; despu&eacute;s de la imagen 6."),
        ])
        + note("Son 7 im&aacute;genes por homenajeado: la pizarra del nombre m&aacute;s 6 retratos."))
    es+=card("COMPARTE / LOS TRES NECESITAN LOS ARCHIVOS","Comparte Tu Trabajo con Tu Grupo",
        para("Una persona fotograf&iacute;a, pero los tres editan y entregan su propio trabajo. As&iacute; que todos necesitan los mismos archivos. Comp&aacute;rtelos de una de estas dos formas.")
        + bullets([
            ("Comparte la tarjeta de memoria:","copia los archivos RAW de la tarjeta para que los tres del grupo tengan una copia."),
            ("O usa OneDrive:","pon los archivos RAW en una carpeta compartida de OneDrive, y cada persona los descarga."),
            ("Luego importa:","cada persona mueve los archivos RAW a su carpeta RAW_Images y los importa a Lightroom Classic."),
        ])
        + note("Haz esto antes de salir. No puedes editar ni entregar una hoja de contactos sin los archivos."))
    es+=card("&Aacute;RMALA / HOJA DE CONTACTOS","Entrega una Hoja de Contactos de 12",
        steps([
            ("Importa tus archivos RAW:","en Lightroom Classic, importa todo tu trabajo desde tu carpeta RAW_Images."),
            ("Usa la plantilla de 12:","en el m&oacute;dulo Print, elige la plantilla de hoja de contactos de 12 con todo tu trabajo cargado."),
            ("Imprime a JPG:","usa Print to File para que se guarde como un JPG de alta resoluci&oacute;n, luego s&uacute;belo aqu&iacute;."),
        ])
        + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n. Entrega todo tu trabajo, cada imagen que tu grupo captur&oacute;."))
    es+=next_up("SIGUIENTE &middot; PASO 03 - Selecciona, Edita y Entrega","Elige tu mejor cintura y tu mejor pecho de cada homenajeado, edita al est&aacute;ndar del cliente y exporta tus JPG.")

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S2}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S2}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Capture and Contact Sheet | Panther of the Quarter | Photography 2A | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

# ================= STEP 03: Cull, Edit & Deliver =================
def step02():
    en=banner("Module 10 &bull; Step 03","Cull, Edit &amp; Deliver",
        "Choose your best waist and best chest for each honoree, edit to the client standard, and turn in your JPGs.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("CULL / CHOOSE YOUR BEST","Best Waist, Best Chest, Per Honoree",
        para("Go through your take, honoree by honoree. For each honoree your group photographed, choose your <strong>best waist-level frame</strong> and your <strong>best chest-level frame</strong>.")
        + (float_right(S2_FLOAT,"A Pioneer Valley student culling and editing honoree portraits in Lightroom Classic on an iMac in the lab") if HAVE_S2_FLOAT else "")
        + bullets([
            ("Sharp eyes:","keep the frames where the eyes are in focus. Skip any that are soft."),
            ("No blinks:","make sure your keeper has open eyes and a natural look."),
            ("Even light:","keep the frame where the face is evenly lit, with a catchlight in the eyes."),
        ])
        + note("Call these your selections, not &ldquo;picks.&rdquo; You turn in two edited JPGs for every honoree your group photographed, so a two-honoree group turns in four files."))
    en+=deliverables_box(False,
        [("Per honoree, best waist-level JPG:","your strongest waist-level frame for the honoree, edited and exported at full resolution."),
         ("Per honoree, best chest-level JPG:","your strongest chest-level frame for that honoree, edited and exported at full resolution.")],
        files=2)
    en+=card("EDIT / MATCH THE CLIENT STANDARD","Make Every Honoree Consistent",
        para("Every honoree should look like part of the same set. Edit your RAW files in Lightroom Classic so they match.")
        + steps([
            ("Fix the white balance:","the teal backlight can push color. Set the white balance so skin looks natural."),
            ("Match the crops:","crop every waist-level the same way, and every chest-level the same way."),
            ("Even exposure:","keep the face bright and clear. Match the look across all your honorees."),
            ("Light retouch only:","small, natural cleanups are fine. No heavy skin smoothing."),
            ("Check the eyes:","the eyes should be sharp, with the catchlight showing."),
        ])
        + note("Consistent is the goal: same crops, same look, every honoree."))
    en+=card("DELIVER / NAME AND UPLOAD","Export, Name, and Turn In",
        steps([
            ("Export full-resolution JPGs:","go to File &rsaquo; Export and export your edited selections as full-resolution JPGs into your project folder."),
            ("Name each file:","use the honoree&rsquo;s last name and first name plus the crop, like <strong>Smith_John_Waist.jpg</strong> and <strong>Smith_John_Chest.jpg</strong>."),
            ("Upload here:","turn in your edited JPGs to this Canvas assignment: a waist and a chest for every honoree your group photographed."),
        ])
        + note("Mr. Silva checks every honoree and sends the final portraits to Mr. Movahedi. You turn in your own edits here."))
    en+=next_up("UP NEXT &middot; STEP 04 - Reflection","Tell how your group worked together and how you made your editing choices.")

    es=banner("M&oacute;dulo 10 &bull; Paso 03","Selecciona, Edita y Entrega",
        "Elige tu mejor cintura y tu mejor pecho de cada homenajeado, edita al est&aacute;ndar del cliente y entrega tus JPG.","#top","Back to English")
    es+=card("SELECCIONA / ELIGE LAS MEJORES","Mejor Cintura, Mejor Pecho, Por Homenajeado",
        para("Revisa tu trabajo, homenajeado por homenajeado. Para cada homenajeado que fotografi&oacute; tu grupo, elige tu <strong>mejor imagen de cintura</strong> y tu <strong>mejor imagen de pecho</strong>.")
        + (float_right(S2_FLOAT,"Un estudiante de Pioneer Valley seleccionando y editando retratos de homenajeados en Lightroom Classic en una iMac en el laboratorio") if HAVE_S2_FLOAT else "")
        + bullets([
            ("Ojos n&iacute;tidos:","guarda las im&aacute;genes donde los ojos est&aacute;n enfocados. Descarta las borrosas."),
            ("Sin parpadeos:","aseg&uacute;rate de que tu imagen tenga los ojos abiertos y se vea natural."),
            ("Luz pareja:","guarda la imagen donde la cara est&aacute; bien iluminada, con un brillo en los ojos."),
        ])
        + note("Llama a estas tus selecciones. Entregas dos JPG editados por cada homenajeado que fotografi&oacute; tu grupo, as&iacute; que un grupo de dos homenajeados entrega cuatro archivos."))
    es+=deliverables_box(True,
        [("Por homenajeado, mejor JPG de cintura:","tu mejor imagen de cintura del homenajeado, editada y exportada a resoluci&oacute;n completa."),
         ("Por homenajeado, mejor JPG de pecho:","tu mejor imagen de pecho de ese homenajeado, editada y exportada a resoluci&oacute;n completa.")],
        files=2)
    es+=card("EDITA / IGUALA EL EST&Aacute;NDAR DEL CLIENTE","Haz a Cada Homenajeado Consistente",
        para("Cada homenajeado debe verse como parte del mismo conjunto. Edita tus archivos RAW en Lightroom Classic para que coincidan.")
        + steps([
            ("Corrige el balance de blancos:","la luz trasera teal puede empujar el color. Ajusta el balance de blancos para que la piel se vea natural."),
            ("Iguala los encuadres:","recorta cada imagen de cintura igual, y cada imagen de pecho igual."),
            ("Exposici&oacute;n pareja:","mant&eacute;n la cara brillante y clara. Iguala el look en todos tus homenajeados."),
            ("Retoque ligero:","peque&ntilde;os arreglos naturales est&aacute;n bien. Nada de suavizar mucho la piel."),
            ("Revisa los ojos:","los ojos deben estar n&iacute;tidos, con el brillo visible."),
        ])
        + note("La meta es ser consistente: los mismos encuadres, el mismo look, cada homenajeado."))
    es+=card("ENTREGA / NOMBRA Y SUBE","Exporta, Nombra y Entrega",
        steps([
            ("Exporta JPG a resoluci&oacute;n completa:","ve a File &rsaquo; Export y exporta tus selecciones editadas como JPG a resoluci&oacute;n completa a la carpeta de tu proyecto."),
            ("Nombra cada archivo:","usa el apellido y el nombre del homenajeado m&aacute;s el encuadre, como <strong>Smith_John_Waist.jpg</strong> y <strong>Smith_John_Chest.jpg</strong>."),
            ("Sube aqu&iacute;:","entrega tus JPG editados a esta tarea de Canvas: una cintura y un pecho por cada homenajeado que fotografi&oacute; tu grupo."),
        ])
        + note("El Sr. Silva revisa cada homenajeado y env&iacute;a los retratos finales al Sr. Movahedi. T&uacute; entregas tus propias ediciones aqu&iacute;."))
    es+=next_up("SIGUIENTE &middot; PASO 04 - Reflexi&oacute;n","Cuenta c&oacute;mo trabaj&oacute; tu grupo y c&oacute;mo tomaste tus decisiones de edici&oacute;n.")

    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S3}" class="silva-step-btn">Step 04 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S3}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
    return wrap_page("Step 3: Cull, Edit and Deliver | Panther of the Quarter | Photography 2A | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

# ================= STEP 04: Reflection =================
def step03():
    en=banner("Module 10 &bull; Step 04","Reflection",
        "Tell how your group worked together and how you made your editing choices.","#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
    en+=card("STEP 04 / REFLECT","Complete and Upload the Reflection",
        (float_right(S3_FLOAT,"A Pioneer Valley student typing the Panther of the Quarter reflection in the Word document on an iMac in the lab") if HAVE_S3_FLOAT else "")
        + para("Finish with a short reflection about your group, your role, and your editing choices.")
        + note("The reflection document is inside the project folder you downloaded on Step 01, the Overview. Open the <strong>POTQ_10-28-26</strong> folder and find <strong>Panther-of-the-Quarter-Reflection</strong> (English or Spanish). Type right in the document.")
        + bullets([
            ("Your group and role:","who was in your group, and what role did each person play?"),
            ("A real client:","how did working for a real client, Mr. Movahedi, change the way you worked?"),
            ("Your editing choices:","what did you change so every honoree looked sharp, evenly lit, and consistent?"),
            ("Sharing the files:","how did your group share the images so each of you could edit your own?"),
        ])
        + note("Answer honestly, in your own words, in full sentences."))
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
    en+=next_up("MODULE COMPLETE","Great work. You ran a real studio for a real client, and every honoree got sharp, even, consistent portraits.")

    es=banner("M&oacute;dulo 10 &bull; Paso 04","Reflexi&oacute;n",
        "Cuenta c&oacute;mo trabaj&oacute; tu grupo y c&oacute;mo tomaste tus decisiones de edici&oacute;n.","#top","Back to English", HICON_REFLECT)
    es+=card("PASO 04 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        (float_right(S3_FLOAT,"Un estudiante de Pioneer Valley escribiendo la reflexi&oacute;n de Panther of the Quarter en el documento de Word en una iMac en el laboratorio") if HAVE_S3_FLOAT else "")
        + para("Termina con una reflexi&oacute;n corta sobre tu grupo, tu rol y tus decisiones de edici&oacute;n.")
        + note("El documento de reflexi&oacute;n est&aacute; dentro de la carpeta del proyecto que descargaste en el Paso 01, el Resumen. Abre la carpeta <strong>POTQ_10-28-26</strong> y busca <strong>Panther-of-the-Quarter-Reflection</strong> (en ingl&eacute;s o en espa&ntilde;ol). Escribe directamente en el documento.")
        + bullets([
            ("Tu grupo y tu rol:","&iquest;qui&eacute;nes estaban en tu grupo, y qu&eacute; rol tuvo cada uno?"),
            ("Un cliente real:","&iquest;c&oacute;mo cambi&oacute; tu forma de trabajar el hacerlo para un cliente real, el Sr. Movahedi?"),
            ("Tus decisiones de edici&oacute;n:","&iquest;qu&eacute; cambiaste para que cada homenajeado se viera n&iacute;tido, bien iluminado y consistente?"),
            ("Compartir los archivos:","&iquest;c&oacute;mo comparti&oacute; tu grupo las im&aacute;genes para que cada uno editara las suyas?"),
        ])
        + note("Contesta con honestidad, en tus propias palabras, en oraciones completas."))
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completado, subido a esta tarea de Canvas.")])
    es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Manejaste un estudio real para un cliente real, y cada homenajeado recibi&oacute; retratos n&iacute;tidos, parejos y consistentes.")

    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 03</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 03</a><span></span></div>'
    return wrap_page("Step 4: Reflection | Panther of the Quarter | Photography 2A | PVHS", nav("Step 04",dots_for(3),stepnav), top_wrap(en,es), bottom)

# ================= BUILD =================
for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03)]:
    html=ent(gen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    assert "–" not in html and "&ndash;" not in html, "en dash in "+fname
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
