#!/usr/bin/env python3
# Build the MYSTERY ITEM module (Photo 1A = Module 13, Photo 2A = Module 13).
# Partners get a camera kit number that matches a numbered brown paper bag. They open the bag to
# find a surprise object, choose a photography approach that fits it, capture it in Manual mode
# (RAW), build a 12-up contact sheet of their full take in Lightroom Classic, cull and edit their
# best three in Lightroom Classic, build a 6-up contact sheet of the three edited images, and finish
# with a reflection. Same Lightroom Classic workflow as every other photo module (never Bridge).
# Two days: Day 1 capture + offload, Day 2 edit + reflect + submit.
# Pages: Step 01 Overview + Step 02 Capture & Contact + Step 03 Cull & Edit + Step 04 Reflection.
# Dark teal angular framework, bilingual EN/ES, 5th-grade. Portal-only (no public share copy).
import os, re
from silva_framework import *

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"
HERO=f"{SITE}/assets/images/mystery-item/mystery-item-hero-v1.jpg"

# Image + download slots. Hero is in; the three per-step student photos and the downloads (reflection
# doc + project folder zip) are gated OFF until the assets exist. A missing image renders nothing,
# never a placeholder box. Flip a flag and drop the file in when it is ready.
HAVE_HERO=True
HAVE_S2_FLOAT=True; HAVE_S3_FLOAT=False; HAVE_S4_FLOAT=False
HAVE_DOWNLOADS=True

COURSES=[
  {"prefix":"photo1","label":"Photography 1A","mod":"13",
   "reflect_en":f"{SITE}/assets/course-documents/Mystery-Item-Reflection-EN.docx",
   "reflect_es":f"{SITE}/assets/course-documents/Mystery-Item-Reflection-ES.docx",
   "zip":f"{SITE}/assets/templates/mystery-item/Mystery-Item-Project-Folder.zip"},
  {"prefix":"photo2","label":"Photography 2A","mod":"13",
   "reflect_en":f"{SITE}/assets/course-documents/Mystery-Item-Reflection-EN.docx",
   "reflect_es":f"{SITE}/assets/course-documents/Mystery-Item-Reflection-ES.docx",
   "zip":f"{SITE}/assets/templates/mystery-item/Mystery-Item-Project-Folder.zip"},
]

# Local ent: accents to entities AND en-dash to a plain hyphen (never emit &ndash;, per the dash ban).
def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

MYSTERY_STANDARDS=[
  {"code":"MA:Cr1.1","en_tier":"Media Arts","es_tier":"Artes Medi&aacute;ticas",
   "en_title":"Generate &amp; Conceptualize","es_title":"Genera y Conceptualiza",
   "en_desc":"You choose a photography approach that fits your mystery item and make an intentional creative decision.",
   "es_desc":"Eliges un enfoque de fotograf&iacute;a que va con tu objeto misterioso y tomas una decisi&oacute;n creativa a prop&oacute;sito."},
  {"code":"MA:Pr5.1","en_tier":"Media Arts","es_tier":"Artes Medi&aacute;ticas",
   "en_title":"Develop &amp; Refine Techniques","es_title":"Desarrolla y Refina T&eacute;cnicas",
   "en_desc":"You capture your item in Manual mode, controlling exposure, angle, and light on purpose.",
   "es_desc":"Capturas tu objeto en modo Manual, controlando la exposici&oacute;n, el &aacute;ngulo y la luz a prop&oacute;sito."},
  {"code":"MA:Cr3.1","en_tier":"Media Arts","es_tier":"Artes Medi&aacute;ticas",
   "en_title":"Refine &amp; Complete","es_title":"Refina y Completa",
   "en_desc":"You cull your take and edit your strongest three images in Lightroom Classic to finish clean, polished photos.",
   "es_desc":"Seleccionas de tu trabajo y editas tus tres im&aacute;genes m&aacute;s fuertes en Lightroom Classic para terminar fotos limpias y pulidas."},
  {"code":"AME.A4.0","en_tier":"CTE","es_tier":"CTE",
   "en_title":"Analyze &amp; Problem-Solve","es_title":"Analiza y Resuelve Problemas",
   "en_desc":"You solve a creative problem with a partner, planning and making decisions together to photograph a surprise object.",
   "es_desc":"Resuelves un problema creativo con un compa&ntilde;ero, planeando y tomando decisiones juntos para fotografiar un objeto sorpresa."},
]

# Suggested photography approaches (the creative-choice menu; same list EN/ES body text differs).
APPROACHES_EN=[
  ("Product photo","a clean, careful photo that shows your item clearly, with simple light and a simple background."),
  ("Black and white","drop the color and let shape, light, and texture carry the photo."),
  ("Photo story","a small set of photos that show your item from different angles or tell a tiny story."),
  ("Creative lighting","use an LED light or a window to make shadows, highlights, or a mood."),
  ("Panorama","get in close or frame it wide to make your small item feel big."),
  ("Your own idea","any thoughtful, on-purpose approach you can explain."),
]
APPROACHES_ES=[
  ("Foto de producto","una foto limpia y cuidada que muestra tu objeto con claridad, con luz simple y fondo simple."),
  ("Blanco y negro","quita el color y deja que la forma, la luz y la textura lleven la foto."),
  ("Historia en fotos","un grupo peque&ntilde;o de fotos que muestran tu objeto desde distintos &aacute;ngulos o cuentan una peque&ntilde;a historia."),
  ("Iluminaci&oacute;n creativa","usa una luz LED o una ventana para crear sombras, luces o un ambiente."),
  ("Panor&aacute;mica","ac&eacute;rcate mucho o toma amplio para que tu objeto peque&ntilde;o se sienta grande."),
  ("Tu propia idea","cualquier enfoque pensado y a prop&oacute;sito que puedas explicar."),
]

def mystery_camera_settings(es):
    # Red camera-settings section for the Mystery Item product session: the LOCKED capture_panel graphic
    # with the STARTING-POINT values (50mm lens in the lead, f/2.8 / 1-125 / ISO 800 / RAW in the panel).
    # Custom lead/note (not the locked photo-walk "only change one setting" text): these are a start,
    # students adjust for mood + lighting. change_field="iso" tags ISO as the quick balance control.
    red="#f90101"
    if es:
        title="Ajustes de C&aacute;mara"
        lead=("Trabaja en modo Manual (M). Aqu&iacute; tienes un buen <strong>punto de partida</strong> para tu objeto misterioso: un <strong>lente de 50mm</strong> en <strong>f/2.8</strong>, obturador <strong>1/125</strong> e <strong>ISO 800</strong>, capturando en RAW.")
        note_t=("Esto es un punto de partida, no una regla. Cambia tus ajustes seg&uacute;n el <strong>ambiente</strong> que quieras y seg&uacute;n tu <strong>luz</strong>: la luz del sal&oacute;n, una ventana, y cualquier luz LED o reflector que agregues. Observa tu expos&iacute;metro y ajusta tu ISO (y lo dem&aacute;s) hasta que tu foto se vea bien.")
    else:
        title="Camera Settings"
        lead=("Work in Manual mode (M). Here is a good <strong>starting point</strong> for your mystery item: a <strong>50mm lens</strong> at <strong>f/2.8</strong>, shutter <strong>1/125</strong>, and <strong>ISO 800</strong>, captured in RAW.")
        note_t=("This is a starting point, not a rule. Change your settings for the <strong>mood</strong> you want and for your <strong>light</strong>: the room light, a window, and any LED light or reflector you add. Watch your light meter and adjust your ISO (and the rest) until your photo looks right.")
    lead_html=f'<div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{lead}</span></div>'
    note_box=(f'<div style="background:rgba(249,1,1,0.10);border:1px solid rgba(249,1,1,0.30);border-left:4px solid {red};padding:11px 14px;margin:0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.92);line-height:1.55;">{note_t}</div>')
    return (f'<div style="background:linear-gradient(180deg,rgba(249,1,1,0.06) 0%,rgba(249,1,1,0.02) 100%);border:1px solid rgba(249,1,1,0.26);border-left:6px solid {red};padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(CAMSET_ICON, title, "#f90101", "#ff8f8f")
      + f'<div class="silva-cfloat" style="float:right;width:50%;min-width:400px;margin:2px 0 16px 30px;">{capture_panel("RAW", "1/125", "f/2.8", "800", "iso")}</div>'
      + lead_html + note_box + '</div>')

def build_course(C):
    OVER=f"{C['prefix']}-mystery-item-overview.html"
    S2=f"{C['prefix']}-mystery-item-step02-capture-contact.html"
    S3=f"{C['prefix']}-mystery-item-step03-cull-edit.html"
    S4=f"{C['prefix']}-mystery-item-step04-reflection.html"
    MOD=C['mod']; LABEL=C['label']

    def nav(current,dots,stepnav):
        return ('      <div class="silva-breadcrumb">\n'
                '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
                '        <span class="bc-sep">&rsaquo;</span>\n'
                f'        <a href="{OVER}" class="bc-hide-sm">Mystery Item</a>\n'
                '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
                f'        <span class="bc-current">{current}</span>\n'
                '      </div>\n'
                '      <div class="silva-nav-spacer"></div>\n'
                f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
                f'      <div class="silva-step-nav">{stepnav}</div>')
    DOTS_TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04")]
    def dots_for(active_idx):
        hrefs=[OVER,S2,S3,S4]; r=""
        for i,(lab,title) in enumerate(DOTS_TITLES):
            r+=dot("" if i==active_idx else hrefs[i], lab, title, i==active_idx, module=False)
        return r

    def approaches_card(es):
        data=APPROACHES_ES if es else APPROACHES_EN
        eyebrow="ELIGE TU ENFOQUE / DECISI&Oacute;N CREATIVA" if es else "CHOOSE YOUR APPROACH / YOUR CREATIVE CALL"
        head="Pick a Style That Fits Your Item" if not es else "Elige un Estilo que Vaya con Tu Objeto"
        lead=("Antes de capturar, habla con tu compa&ntilde;ero y elige un enfoque. Piensa en proyectos pasados. No hay una respuesta correcta: elige a prop&oacute;sito."
              if es else "Before you capture, talk with your partner and choose an approach. Think back to past projects. There is no one right answer: choose on purpose.")
        return card(eyebrow, head, para(lead)+bullets(data))

    def downloads_block(es):
        heading="Descarga Tus Archivos" if es else "Download Your Files"
        lead=("Descarga la carpeta del proyecto Mystery Item. Adentro tienes una carpeta <strong>Inspo Images</strong> para tu inspiraci&oacute;n, una carpeta <strong>RAW Images</strong> para tus fotos, y el documento de <strong>reflexi&oacute;n</strong> que llenas al final."
              if es else "Download the Mystery Item project folder. Inside you have an <strong>Inspo Images</strong> folder for your inspiration, a <strong>RAW Images</strong> folder for your photos, and the <strong>reflection</strong> document you fill out at the end.")
        ziplabel="Carpeta del Proyecto Mystery Item (ZIP)" if es else "Mystery Item Project Folder (ZIP)"
        return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
          + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
          + para(lead)
          + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
          + dl_link(C['zip'],ziplabel,row=True)
          + '</div>'
          + folder_note(es, AREA) + '</div>')

    # ================= OVERVIEW (Step 01) =================
    def overview():
        en=banner(f"Module {MOD} &bull; Step 01","Mystery Item: Start Here","Open your mystery bag with your partner, choose a photography approach, and capture your surprise object. Read this page, then go to Step 02.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
        en+=type_card("overview","Step 01 &middot; Overview","A Surprise in the Bag",
            para("You and a partner get a <strong>camera kit number</strong> that matches a <strong>numbered brown paper bag</strong>. Inside the bag is a surprise object. You do not know what it is until you open it. Your job: open the bag, decide how to photograph your item, and make the strongest photo you can.")
            + para("This project is about <strong>creativity, problem-solving, and teamwork</strong>. You and your partner plan together, you both take photos, and then each of you edits and turns in your <strong>own</strong> work.")
            + (framed(HERO,"Two students at a table with numbered brown paper bags, choosing their mystery item") if HAVE_HERO else ""))
        en+=standards_box(False, MYSTERY_STANDARDS)
        if HAVE_DOWNLOADS: en+=downloads_block(False)
        en+=approaches_card(False)
        en+=card("HOW THIS WORKS / YOUR PLAN","From the Bag to Your Finished Photo",
            para("You are on Step 01 now: read this page so you understand the project. This module runs over <strong>two days</strong>. Here is the path.")
            + bullets([
                ("Step 02 &middot; Capture &amp; Contact:","open your bag, pick an approach, and photograph your item in Manual mode. Then build a 12-up contact sheet of your full take in Lightroom Classic."),
                ("Step 03 &middot; Cull &amp; Edit:","cull to your best three, edit them in Lightroom Classic, export your three final JPEGs, and build a 6-up contact sheet of your edited images."),
                ("Step 04 &middot; Reflection:","tell your idea, how you photographed your item, and what worked and what was hard."),
            ])
            + note("Day 1 is capture and offload. Day 2 is edit, reflect, and submit. You work with a partner, but each of you turns in your own photos and your own reflection."))
        en+=resources_card("Key Words",
            vocab_grid("On the Quiz",
              "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
              [("Manual Mode","You set the aperture, shutter speed, and ISO yourself, so you control the whole exposure."),
               ("Composition","How you arrange your item in the frame: your angle, your distance, and what you include or leave out."),
               ("Raw File","A large photo file that keeps all the camera&rsquo;s data, so you have the most room to edit later."),
               ("Contact Sheet","One image that shows all your photos in a grid, so you and your teacher can see your whole take at once."),
               ("Culling","Looking through all your photos and choosing your strongest one or ones, letting the rest go."),
               ("Lightroom Classic","The Adobe app where you import, cull, and edit your photos and build your contact sheets.")]))
        en+=next_up("UP NEXT &middot; STEP 02 - Capture &amp; Contact","Open your bag, choose an approach, photograph your item, and build a 12-up contact sheet of your full take in Lightroom Classic.")

        es=banner(f"M&oacute;dulo {MOD} &bull; Paso 01","Objeto Misterioso: Empieza Aqu&iacute;","Abre tu bolsa misteriosa con tu compa&ntilde;ero, elige un enfoque de fotograf&iacute;a y captura tu objeto sorpresa. Lee esta p&aacute;gina y ve al Paso 02.","#top","Back to English", HICON_PHOTO_WALK)
        es+=type_card("overview","Paso 01 &middot; Resumen","Una Sorpresa en la Bolsa",
            para("T&uacute; y un compa&ntilde;ero reciben un <strong>n&uacute;mero de kit de c&aacute;mara</strong> que coincide con una <strong>bolsa de papel caf&eacute; numerada</strong>. Dentro de la bolsa hay un objeto sorpresa. No sabes qu&eacute; es hasta que la abres. Tu trabajo: abre la bolsa, decide c&oacute;mo fotografiar tu objeto y haz la foto m&aacute;s fuerte que puedas.")
            + para("Este proyecto trata de <strong>creatividad, resoluci&oacute;n de problemas y trabajo en equipo</strong>. T&uacute; y tu compa&ntilde;ero planean juntos, los dos toman fotos, y luego cada uno edita y entrega su <strong>propio</strong> trabajo.")
            + (framed(HERO,"Dos estudiantes en una mesa con bolsas de papel numeradas, eligiendo su objeto misterioso") if HAVE_HERO else ""))
        es+=standards_box(True, MYSTERY_STANDARDS)
        if HAVE_DOWNLOADS: es+=downloads_block(True)
        es+=approaches_card(True)
        es+=card("C&Oacute;MO FUNCIONA / TU PLAN","De la Bolsa a Tu Foto Terminada",
            para("Ahora est&aacute;s en el Paso 01: lee esta p&aacute;gina para entender el proyecto. Este m&oacute;dulo dura <strong>dos d&iacute;as</strong>. Este es el camino.")
            + bullets([
                ("Paso 02 &middot; Captura y Contacto:","abre tu bolsa, elige un enfoque y fotograf&iacute;a tu objeto en modo Manual. Luego arma una hoja de contactos 12-up de toda tu toma en Lightroom Classic."),
                ("Paso 03 &middot; Selecci&oacute;n y Edici&oacute;n:","selecciona tus tres mejores, ed&iacute;talas en Lightroom Classic, exporta tus tres JPEG finales y arma una hoja de contactos 6-up de tus im&aacute;genes editadas."),
                ("Paso 04 &middot; Reflexi&oacute;n:","cuenta tu idea, c&oacute;mo fotografiaste tu objeto, y qu&eacute; funcion&oacute; y qu&eacute; fue dif&iacute;cil."),
            ])
            + note("El D&iacute;a 1 es capturar y descargar. El D&iacute;a 2 es editar, reflexionar y entregar. Trabajas con un compa&ntilde;ero, pero cada uno entrega sus propias fotos y su propia reflexi&oacute;n."))
        es+=resources_card("Palabras Clave",
            vocab_grid("En el Examen",
              "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el de mitad de semestre y el del final. Apr&eacute;ndelas ahora, no la noche anterior.",
              [("Manual Mode (Modo Manual)","T&uacute; ajustas la apertura, la velocidad del obturador y el ISO, as&iacute; que controlas toda la exposici&oacute;n."),
               ("Composition (Composici&oacute;n)","C&oacute;mo acomodas tu objeto en el encuadre: tu &aacute;ngulo, tu distancia y qu&eacute; incluyes o dejas fuera."),
               ("Raw File (Archivo RAW)","Un archivo de foto grande que guarda todos los datos de la c&aacute;mara, as&iacute; tienes el mayor espacio para editar despu&eacute;s."),
               ("Contact Sheet (Hoja de Contactos)","Una sola imagen que muestra todas tus fotos en una cuadr&iacute;cula, para que t&uacute; y tu maestro vean todo tu trabajo de una vez."),
               ("Culling (Selecci&oacute;n)","Revisar todas tus fotos y elegir tu m&aacute;s fuerte o fuertes, dejando ir el resto."),
               ("Lightroom Classic","La app de Adobe donde importas, seleccionas y editas tus fotos y armas tus hojas de contactos.")]))
        es+=next_up("SIGUIENTE &middot; PASO 02 - Captura y Contacto","Abre tu bolsa, elige un enfoque, fotograf&iacute;a tu objeto y arma una hoja de contactos 12-up de toda tu toma en Lightroom Classic.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
        return wrap_page(f"Mystery Item: Start Here | {LABEL} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 02: Capture & Contact =================
    def step_capture():
        float2_en=float_right(f"{SITE}/assets/images/mystery-item/capture-float-v3.jpg","A student photographing a mystery item with the camera kit","Try different angles, distances, and lighting.") if HAVE_S2_FLOAT else ""
        float2_es=float_right(f"{SITE}/assets/images/mystery-item/capture-float-v3.jpg","Un estudiante fotografiando un objeto misterioso con el kit de c&aacute;mara","Prueba distintos &aacute;ngulos, distancias e iluminaci&oacute;n.") if HAVE_S2_FLOAT else ""
        en=banner(f"Module {MOD} &bull; Step 02","Capture &amp; Contact","Open your bag, choose an approach, photograph your item in Manual mode, and build a 12-up contact sheet in Lightroom Classic.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
        en+=type_card("photo-walk","Step 02 &middot; Capture","Open Your Bag and Make a Plan",
            float2_en
            + para("Match your <strong>camera kit number</strong> to the <strong>brown paper bag</strong> with the same number. Only use the item from your matching bag. Open it with your partner and see your mystery item for the first time.")
            + para("Talk together: what kind of photo fits this item? Look back at the approaches on Step 01, then pick one. You can ask Mr. Silva for an <strong>LED light or a reflector</strong> if you want to try creative lighting.")
            + para("Before you capture, get inspired: look up a few photos of products or objects in the style you picked. Save <strong>2 or 3</strong> into the <strong>Inspo Images</strong> folder in your project folder, and use them as a guide for your angles, your light, and your background.")
            + note("Both partners take photos. You plan together, but each of you ends up with your own set of images to edit."))
        en+=deliverables_box(False,
            [("1 contact sheet (12-up):","a 12-up contact sheet of your full take, unedited, printed to a high-resolution JPG. Name it <strong>12 Up Mystery Item</strong> plus your name, like <strong>12 Up Mystery Item Maria G</strong>. Each partner turns in their own, even though you worked together.")])
        en+=mystery_camera_settings(False)
        en+=card("PHOTOGRAPH YOUR ITEM / WORK THE ANGLES","Take Lots of Photos, On Purpose",
            para("Photograph your item today. You can work in the classroom or just outside. Take <strong>many photos</strong> and try different ideas, so you have strong options to choose from later.")
            + steps([
                ("Set Manual mode:","turn the Mode dial to <strong>M</strong>. Balance your exposure so the photo is not too dark or too bright."),
                ("Try different angles:","photograph from above, from the side, and up close. Move around your item."),
                ("Try different light:","turn toward a window, or add an LED light or reflector to shape the light."),
                ("Fill the frame:","get close so your item is the clear subject. Watch your background and your edges."),
                ("Take a full take:","capture many photos, not just two or three. Both partners participate."),
            ])
            + note("Capture a lot now. In Step 03 you cull down to your strongest image, so give yourself plenty to choose from."))
        en+=card("SHARE THE CAMERA / KEEP YOUR OWN PHOTOS","Both of You, One Camera",
            para("This is a <strong>group project with a partner</strong>, and the two of you share <strong>one camera</strong>. So you have to be careful to keep your own photos separate from your partner&rsquo;s. Here is the plan.")
            + steps([
                ("Take turns on every setup.","set up your item, then <strong>you</strong> take your photos of it. Next, <strong>your partner</strong> takes their photos of the same setup. Trade off like this each time you change the setup."),
                ("Import ALL the photos to your own computer.","when you offload, copy <strong>every</strong> photo from the camera into your <strong>Photography folder on OneDrive</strong>. The camera holds both of your photos, so you will see yours and your partner&rsquo;s together."),
                ("Keep only YOUR photos.","look through them and keep the ones <strong>you</strong> took. <strong>Delete your partner&rsquo;s</strong> from your folder, so your folder has only your own work."),
                ("Edit and turn in your own.","each of you edits your own photos and turns in your own. You never turn in your partner&rsquo;s work."),
            ])
            + note("Share the camera, but keep your files your own: your folder, your photos, your grade."))
        en+=card("BUILD / 12-UP CONTACT SHEET","Make Your 12-Up Contact Sheet",
            para("Now that <strong>your own photos</strong> are in your project folder, make one <strong>12-up contact sheet</strong> that shows your whole take as small thumbnails on one page. Make it <strong>before you edit</strong>: this is your <strong>unedited</strong> full take, and it shows your camera settings. You build it in <strong>Lightroom Classic</strong>, the same as every other photo project.")
            + steps([
                ("Import your photos into Lightroom Classic.","open Lightroom Classic, click <strong>Import</strong>, and bring in your own raw images from your project folder."),
                ("Open the Print module and pick the 12-Up Contact Sheet preset.","select your images, go to the <strong>Print</strong> module, and choose the <strong>12-Up Contact Sheet</strong> preset from your User Templates. If you do not see it, install it from the Course Overview."),
                ("Print to a high-resolution JPG.","set <strong>Print To: JPEG File</strong>, then click <strong>Print to File</strong>. The preset already saves a high-resolution JPG for you."),
                ("Name it and upload.","name it <strong>12 Up Mystery Item</strong> plus your name, like <strong>12 Up Mystery Item Maria G</strong>. Then upload the JPG to this Canvas assignment."),
            ])
            + note("The number is a maximum, not a minimum: a 12-up with 8 photos or with extra pages is fine. Contact sheets are always turned in as a high-resolution JPG. Do not edit your photos yet, that happens in Step 03."))
        en+=next_up("UP NEXT &middot; STEP 03 - Cull &amp; Edit","Cull to your strongest three, edit them in Lightroom Classic, export your three final JPEGs, and build a 6-up contact sheet.")

        es=banner(f"M&oacute;dulo {MOD} &bull; Paso 02","Captura y Contacto","Abre tu bolsa, elige un enfoque, fotograf&iacute;a tu objeto en modo Manual y arma una hoja de contactos 12-up en Lightroom Classic.","#top","Back to English", HICON_PHOTO_WALK)
        es+=type_card("photo-walk","Paso 02 &middot; Captura","Abre Tu Bolsa y Haz un Plan",
            float2_es
            + para("Haz coincidir tu <strong>n&uacute;mero de kit de c&aacute;mara</strong> con la <strong>bolsa de papel caf&eacute;</strong> del mismo n&uacute;mero. Usa solo el objeto de tu bolsa. &Aacute;brela con tu compa&ntilde;ero y ve tu objeto misterioso por primera vez.")
            + para("Hablen juntos: &iquest;qu&eacute; tipo de foto va con este objeto? Mira los enfoques del Paso 01 y luego elige uno. Puedes pedirle a Mr. Silva una <strong>luz LED o un reflector</strong> si quieres probar iluminaci&oacute;n creativa.")
            + para("Antes de capturar, b&uacute;scate ideas: busca unas fotos de productos u objetos en el estilo que elegiste. Guarda <strong>2 o 3</strong> en la carpeta <strong>Inspo Images</strong> de tu carpeta del proyecto, y &uacute;salas como gu&iacute;a para tus &aacute;ngulos, tu luz y tu fondo.")
            + note("Los dos compa&ntilde;eros toman fotos. Planean juntos, pero cada uno termina con su propio grupo de im&aacute;genes para editar."))
        es+=deliverables_box(True,
            [("1 hoja de contactos (12-up):","una hoja de contactos 12-up de toda tu toma, sin editar, impresa como un JPG de alta resoluci&oacute;n. N&oacute;mbrala <strong>12 Up Mystery Item</strong> y tu nombre, como <strong>12 Up Mystery Item Maria G</strong>. Cada compa&ntilde;ero entrega la suya, aunque trabajaron juntos.")])
        es+=mystery_camera_settings(True)
        es+=card("FOTOGRAF&Iacute;A TU OBJETO / TRABAJA LOS &Aacute;NGULOS","Toma Muchas Fotos, a Prop&oacute;sito",
            para("Fotograf&iacute;a tu objeto hoy. Puedes trabajar en el sal&oacute;n o justo afuera. Toma <strong>muchas fotos</strong> y prueba distintas ideas, para tener buenas opciones despu&eacute;s.")
            + steps([
                ("Pon el modo Manual:","gira el dial de modo a <strong>M</strong>. Equilibra tu exposici&oacute;n para que la foto no quede muy oscura ni muy brillante."),
                ("Prueba distintos &aacute;ngulos:","fotograf&iacute;a desde arriba, desde el lado y bien de cerca. Mu&eacute;vete alrededor de tu objeto."),
                ("Prueba distinta luz:","gira hacia una ventana, o agrega una luz LED o un reflector para dar forma a la luz."),
                ("Llena el encuadre:","ac&eacute;rcate para que tu objeto sea el sujeto claro. Cuida tu fondo y tus bordes."),
                ("Haz una toma completa:","captura muchas fotos, no solo dos o tres. Los dos compa&ntilde;eros participan."),
            ])
            + note("Captura bastante ahora. En el Paso 03 seleccionas tu imagen m&aacute;s fuerte, as&iacute; que date muchas opciones."))
        es+=card("COMPARTAN LA C&Aacute;MARA / GUARDA TUS PROPIAS FOTOS","Los Dos, Una C&aacute;mara",
            para("Este es un <strong>proyecto en grupo con un compa&ntilde;ero</strong>, y los dos comparten <strong>una c&aacute;mara</strong>. Por eso tienes que tener cuidado de mantener tus propias fotos separadas de las de tu compa&ntilde;ero. Este es el plan.")
            + steps([
                ("Tomen turnos en cada arreglo.","acomoda tu objeto, luego <strong>t&uacute;</strong> tomas tus fotos. Despu&eacute;s, <strong>tu compa&ntilde;ero</strong> toma sus fotos del mismo arreglo. Tur&uacute;nense as&iacute; cada vez que cambien el arreglo."),
                ("Importa TODAS las fotos a tu propia computadora.","cuando descargues, copia <strong>todas</strong> las fotos de la c&aacute;mara a tu <strong>carpeta de Fotograf&iacute;a en OneDrive</strong>. La c&aacute;mara tiene las fotos de los dos, as&iacute; que ver&aacute;s las tuyas y las de tu compa&ntilde;ero juntas."),
                ("Guarda solo TUS fotos.","rev&iacute;salas y guarda las que <strong>t&uacute;</strong> tomaste. <strong>Borra las de tu compa&ntilde;ero</strong> de tu carpeta, para que tu carpeta tenga solo tu propio trabajo."),
                ("Edita y entrega lo tuyo.","cada uno edita sus propias fotos y entrega las suyas. Nunca entregues el trabajo de tu compa&ntilde;ero."),
            ])
            + note("Compartan la c&aacute;mara, pero mant&eacute;n tus archivos propios: tu carpeta, tus fotos, tu calificaci&oacute;n."))
        es+=card("ARMA / HOJA DE CONTACTOS 12-UP","Arma Tu Hoja de Contactos 12-Up",
            para("Ahora que <strong>tus propias fotos</strong> est&aacute;n en la carpeta de tu proyecto, arma una <strong>hoja de contactos 12-up</strong> que muestre todo tu trabajo como miniaturas en una p&aacute;gina. Arma esto <strong>antes de editar</strong>: esta es tu toma completa <strong>sin editar</strong>, y muestra tus ajustes de c&aacute;mara. La armas en <strong>Lightroom Classic</strong>, igual que en todos los dem&aacute;s proyectos de foto.")
            + steps([
                ("Importa tus fotos a Lightroom Classic.","abre Lightroom Classic, haz clic en <strong>Import</strong> (Importar) y trae tus propias im&aacute;genes RAW desde la carpeta de tu proyecto."),
                ("Abre el m&oacute;dulo Print y elige el ajuste 12-Up Contact Sheet.","selecciona tus im&aacute;genes, ve al m&oacute;dulo <strong>Print</strong> y elige el ajuste <strong>12-Up Contact Sheet</strong> de tus User Templates. Si no lo ves, inst&aacute;lalo desde el Resumen del Curso."),
                ("Imprime a un JPG de alta resoluci&oacute;n.","pon <strong>Print To: JPEG File</strong>, luego haz clic en <strong>Print to File</strong>. El ajuste ya guarda un JPG de alta resoluci&oacute;n por ti."),
                ("N&oacute;mbrala y s&uacute;bela.","n&oacute;mbrala <strong>12 Up Mystery Item</strong> y tu nombre, como <strong>12 Up Mystery Item Maria G</strong>. Luego sube el JPG a esta tarea de Canvas."),
            ])
            + note("El n&uacute;mero es un m&aacute;ximo, no un m&iacute;nimo: una 12-up con 8 fotos o con p&aacute;ginas de m&aacute;s est&aacute; bien. Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n. No edites tus fotos todav&iacute;a, eso es en el Paso 03."))
        es+=next_up("SIGUIENTE &middot; PASO 03 - Selecci&oacute;n y Edici&oacute;n","Selecciona tus tres mejores, ed&iacute;talas en Lightroom Classic, exporta tus tres JPEG finales y arma una hoja de contactos 6-up.")

        stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
        return wrap_page(f"Step 2: Capture and Contact | Mystery Item | {LABEL} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 03: Cull & Edit =================
    def step_edit():
        float3_en=float_right(f"{SITE}/assets/images/mystery-item/edit-float-v1.jpg","A student editing a mystery item photo in Lightroom Classic","Cull first, then edit your strongest three.") if HAVE_S3_FLOAT else ""
        float3_es=float_right(f"{SITE}/assets/images/mystery-item/edit-float-v1.jpg","Un estudiante editando una foto del objeto misterioso en Lightroom Classic","Selecciona primero, luego edita tus tres m&aacute;s fuertes.") if HAVE_S3_FLOAT else ""
        en=banner(f"Module {MOD} &bull; Step 03","Cull &amp; Edit","Cull to your strongest three, edit them in Lightroom Classic, export your three final JPEGs, and build a 6-up contact sheet.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
        en+=type_card("edit","Step 03 &middot; Cull","Choose Your Strongest Three",
            float3_en
            + para("Open your raw images in <strong>Lightroom Classic</strong> and look through your whole take. <strong>Cull</strong> means you choose your strongest work and let the rest go. Rate your best with stars and reject the ones you will not use.")
            + bullets([
                ("Open in Lightroom Classic:","load your raw files from your OneDrive project folder into Lightroom Classic."),
                ("Cull your take:","give your strongest images stars; reject the weak or blurry ones."),
                ("Pick your best three:","choose the three strongest images that show your idea the best."),
            ])
            + note("Call these your selections, not &ldquo;picks.&rdquo; Choose on purpose, based on your idea."))
        en+=deliverables_box(False,
            [("1 contact sheet (6-up):","a 6-up contact sheet with your 3 best edited images on it (3 empty spots is fine), printed to a high-resolution JPG. Name it <strong>6 Up Mystery Item</strong> plus your name."),
             ("3 final edited images (JPG):","each of your 3 finished edited images, exported as high-resolution JPGs. Name each file with your <strong>first name and last initial</strong>."),
             ("Turn in your own:","each partner edits and submits their own 4 files, even though you worked together.")], files=4)
        en+=card("EDIT THEM / LIGHTROOM CLASSIC","Make Your Three Images Their Best",
            para("Edit your three selections in <strong>Lightroom Classic</strong>. Your edits should support your idea, not fight it.")
            + steps([
                ("Set your exposure and color:","adjust exposure, contrast, highlights, shadows, and white balance until the light looks right."),
                ("Add clarity and crop:","sharpen or add clarity if it helps, then crop to clean your composition and edges."),
                ("Remove distractions:","use the Healing tool in Lightroom Classic to take out things that pull the eye away (a stray object, debris, a mark) if it makes the photo stronger."),
                ("Keep it honest:","edit to make your item look its best. Do not change it into something it is not."),
            ]))
        en+=card("EXPORT / SAVE YOUR 3 FINAL JPEGS","Name Them and Save Them Right",
            steps([
                ("Export as JPEGs:","in Lightroom Classic, export your <strong>three</strong> final edited images as high-resolution <strong>JPEGs</strong>."),
                ("Name your files:","start each file name with your <strong>first name and last initial</strong> (like <strong>MariaG</strong>)."),
                ("Save in your folder:","save them in your Mystery Item project folder on OneDrive, then upload all three to this Canvas assignment."),
            ])
            + note("Turn in your three final JPEGs, your best edited work."))
        en+=card("BUILD / 6-UP CONTACT SHEET","Make Your 6-Up Contact Sheet",
            para("Last, make a <strong>6-up contact sheet</strong> with your <strong>3 edited images</strong> on it. The number is a <strong>maximum, not a minimum</strong>: three images with three empty spots is completely fine. You build it in <strong>Lightroom Classic</strong>, the same as the 12-up.")
            + steps([
                ("Load your 3 edited images.","in Lightroom Classic, select your three final edited photos in the Library."),
                ("Open the Print module and pick the 6-Up Contact Sheet preset.","choose it from your User Templates. If you do not see it, install it from the Course Overview."),
                ("Print to file as a JPG.","click <strong>Print to File</strong>. The preset already saves a high-resolution JPG, so you never choose the format."),
                ("Name it and upload.","name it <strong>6 Up Mystery Item</strong> plus your name, like <strong>6 Up Mystery Item Maria G</strong>. Then upload the JPG to this Canvas assignment."),
            ])
            + note("Contact sheets are always turned in as a high-resolution JPG."))
        en+=next_up("UP NEXT &middot; STEP 04 - Reflection","Tell your idea, how you photographed your item, and what worked and what was hard.")

        es=banner(f"M&oacute;dulo {MOD} &bull; Paso 03","Selecci&oacute;n y Edici&oacute;n","Selecciona tus tres mejores, ed&iacute;talas en Lightroom Classic, exporta tus tres JPEG finales y arma una hoja de contactos 6-up.","#top","Back to English", HICON_DESIGN)
        es+=type_card("edit","Paso 03 &middot; Selecci&oacute;n","Elige Tus Tres M&aacute;s Fuertes",
            float3_es
            + para("Abre tus im&aacute;genes RAW en <strong>Lightroom Classic</strong> y revisa todo tu trabajo. <strong>Seleccionar</strong> significa elegir tu trabajo m&aacute;s fuerte y dejar ir el resto. Marca tus mejores con estrellas y rechaza las que no vas a usar.")
            + bullets([
                ("Abre en Lightroom Classic:","carga tus archivos RAW desde tu carpeta de proyecto en OneDrive a Lightroom Classic."),
                ("Selecciona de tu trabajo:","dale estrellas a tus im&aacute;genes m&aacute;s fuertes; rechaza las d&eacute;biles o borrosas."),
                ("Elige tus tres mejores:","elige las tres im&aacute;genes m&aacute;s fuertes que muestran mejor tu idea."),
            ])
            + note("Llama a estas tus selecciones. Elige a prop&oacute;sito, seg&uacute;n tu idea."))
        es+=deliverables_box(True,
            [("1 hoja de contactos (6-up):","una hoja de contactos 6-up con tus 3 mejores im&aacute;genes editadas (3 espacios vac&iacute;os est&aacute; bien), impresa como un JPG de alta resoluci&oacute;n. N&oacute;mbrala <strong>6 Up Mystery Item</strong> y tu nombre."),
             ("3 im&aacute;genes finales editadas (JPG):","cada una de tus 3 im&aacute;genes editadas terminadas, exportadas como JPG de alta resoluci&oacute;n. Nombra cada archivo con tu <strong>primer nombre e inicial del apellido</strong>."),
             ("Entrega lo tuyo:","cada compa&ntilde;ero edita y entrega sus propios 4 archivos, aunque trabajaron juntos.")], files=4)
        es+=card("ED&Iacute;TALAS / LIGHTROOM CLASSIC","Haz que Tus Tres Im&aacute;genes se Vean lo Mejor",
            para("Edita tus tres selecciones en <strong>Lightroom Classic</strong>. Tus ediciones deben apoyar tu idea, no pelear con ella.")
            + steps([
                ("Ajusta exposici&oacute;n y color:","ajusta la exposici&oacute;n, el contraste, las luces, las sombras y el balance de blancos hasta que la luz se vea bien."),
                ("Agrega claridad y recorta:","aumenta la nitidez o la claridad si ayuda, luego recorta para limpiar tu composici&oacute;n y tus bordes."),
                ("Quita distracciones:","usa la herramienta Healing (Correcci&oacute;n) en Lightroom Classic para quitar lo que jala la mirada (un objeto perdido, basura, una marca) si hace m&aacute;s fuerte la foto."),
                ("Mant&eacute;nla honesta:","edita para que tu objeto se vea lo mejor. No lo cambies en algo que no es."),
            ]))
        es+=card("EXPORTA / GUARDA TUS 3 JPEG FINALES","Nombr&aacute;los y Gu&aacute;rdalos Bien",
            steps([
                ("Exporta como JPEG:","en Lightroom Classic, exporta tus <strong>tres</strong> im&aacute;genes finales editadas como <strong>JPEG</strong> de alta resoluci&oacute;n."),
                ("Nombra tus archivos:","empieza cada nombre de archivo con tu <strong>primer nombre e inicial del apellido</strong> (como <strong>MariaG</strong>)."),
                ("Gu&aacute;rdalos en tu carpeta:","gu&aacute;rdalos en tu carpeta del proyecto Mystery Item en OneDrive, luego sube los tres a esta tarea de Canvas."),
            ])
            + note("Entrega tus tres JPEG finales, tu mejor trabajo editado."))
        es+=card("ARMA / HOJA DE CONTACTOS 6-UP","Arma Tu Hoja de Contactos 6-Up",
            para("Por &uacute;ltimo, arma una <strong>hoja de contactos 6-up</strong> con tus <strong>3 im&aacute;genes editadas</strong>. El n&uacute;mero es un <strong>m&aacute;ximo, no un m&iacute;nimo</strong>: tres im&aacute;genes con tres espacios vac&iacute;os est&aacute; perfecto. La armas en <strong>Lightroom Classic</strong>, igual que la 12-up.")
            + steps([
                ("Carga tus 3 im&aacute;genes editadas.","en Lightroom Classic, selecciona tus tres fotos finales editadas en la Biblioteca."),
                ("Abre el m&oacute;dulo Print y elige el ajuste 6-Up Contact Sheet.","el&iacute;gelo de tus User Templates. Si no lo ves, inst&aacute;lalo desde el Resumen del Curso."),
                ("Imprime a archivo como JPG.","haz clic en <strong>Print to File</strong> (Imprimir a archivo). El ajuste ya guarda un JPG de alta resoluci&oacute;n, as&iacute; que nunca eliges el formato."),
                ("N&oacute;mbrala y s&uacute;bela.","n&oacute;mbrala <strong>6 Up Mystery Item</strong> y tu nombre, como <strong>6 Up Mystery Item Maria G</strong>. Luego sube el JPG a esta tarea de Canvas."),
            ])
            + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n."))
        es+=next_up("SIGUIENTE &middot; PASO 04 - Reflexi&oacute;n","Cuenta tu idea, c&oacute;mo fotografiaste tu objeto, y qu&eacute; funcion&oacute; y qu&eacute; fue dif&iacute;cil.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S4}" class="silva-step-btn">Step 04 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S4}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
        return wrap_page(f"Step 3: Cull and Edit | Mystery Item | {LABEL} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 04: Reflection =================
    def step_reflect():
        ref_note_en=("Open the reflection document inside your Mystery Item project folder. It is already in the folder you downloaded on Step 01, the Overview."
                     if HAVE_DOWNLOADS else "Your teacher will give you the reflection Word document to fill out. Save it in your Mystery Item project folder before you start.")
        ref_note_es=("Abre el documento de reflexi&oacute;n que est&aacute; dentro de tu carpeta del proyecto Mystery Item. Ya viene en la carpeta que descargaste en el Paso 01, el Resumen."
                     if HAVE_DOWNLOADS else "Tu maestro te dar&aacute; el documento de reflexi&oacute;n de Word para llenar. Gu&aacute;rdalo en tu carpeta del proyecto Mystery Item antes de empezar.")
        en=banner(f"Module {MOD} &bull; Step 04","Reflection","Tell your idea, how you photographed your mystery item, and what worked and what was hard.","#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
        en+=card("STEP 04 / REFLECT","Complete and Upload the Reflection",
            para("Finish with a short written reflection. Each of you writes your own, even though you worked with a partner. Be thoughtful and honest, and write in full sentences.")
            + note(ref_note_en)
            + bullets([
                ("Your idea:","what approach did you choose for your mystery item, and why did it fit?"),
                ("Your process:","how did you photograph your item? Talk about your angles, your light, and your Manual settings."),
                ("What worked and what was hard:","what are you proud of, and what was the biggest challenge working with a surprise object and a partner?"),
            ]))
        en+=deliverables_box(False,
            [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
        en+=next_up("MODULE COMPLETE","Great work. You opened a mystery, made a plan with your partner, and turned a surprise object into a strong, finished photo.")

        es=banner(f"M&oacute;dulo {MOD} &bull; Paso 04","Reflexi&oacute;n","Cuenta tu idea, c&oacute;mo fotografiaste tu objeto misterioso, y qu&eacute; funcion&oacute; y qu&eacute; fue dif&iacute;cil.","#top","Back to English", HICON_REFLECT)
        es+=card("PASO 04 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
            para("Termina con una reflexi&oacute;n corta por escrito. Cada uno escribe la suya, aunque trabajaron con un compa&ntilde;ero. S&eacute; reflexivo y honesto, y escribe en oraciones completas.")
            + note(ref_note_es)
            + bullets([
                ("Tu idea:","&iquest;qu&eacute; enfoque elegiste para tu objeto misterioso y por qu&eacute; va bien?"),
                ("Tu proceso:","&iquest;c&oacute;mo fotografiaste tu objeto? Habla de tus &aacute;ngulos, tu luz y tus ajustes en Manual."),
                ("Qu&eacute; funcion&oacute; y qu&eacute; fue dif&iacute;cil:","&iquest;de qu&eacute; est&aacute;s orgulloso y cu&aacute;l fue el reto m&aacute;s grande al trabajar con un objeto sorpresa y un compa&ntilde;ero?"),
            ]))
        es+=deliverables_box(True,
            [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completado, subido a esta tarea de Canvas.")])
        es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Abriste un misterio, hiciste un plan con tu compa&ntilde;ero y convertiste un objeto sorpresa en una foto fuerte y terminada.")

        stepnav=f'<a href="{S3}" class="silva-step-btn">&#8592; Step 03</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S3}" class="silva-bottom-btn">&#8592; Step 03</a><span></span></div>'
        return wrap_page(f"Step 4: Reflection | Mystery Item | {LABEL} | PVHS", nav("Step 04",dots_for(3),stepnav), top_wrap(en,es), bottom)

    for fname,gen in [(OVER,overview),(S2,step_capture),(S3,step_edit),(S4,step_reflect)]:
        html=ent(gen())
        assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
        assert "–" not in html and "&ndash;" not in html, "en dash in "+fname
        low=html.lower()
        for allow in ["shooting tab","shooting menu"]:
            low=low.replace(allow,"")
        for w in ["shoot","shooting","shot","shots","shoots","screenshot"]:
            assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
        open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
        print("wrote", fname, len(html), "bytes")

for C in COURSES:
    build_course(C)
