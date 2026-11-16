#!/usr/bin/env python3
# Build the MYSTERY ITEM module (Photo 1A = Module 13, Photo 2A = Module 13).
# Partners get a camera kit number that matches a numbered brown paper bag. They open the bag to
# find a surprise object, choose a photography approach that fits it, capture it in Manual mode
# (RAW), build a contact sheet, cull and edit their strongest image in Adobe Camera Raw + Photoshop,
# and finish with a reflection. Two days: Day 1 capture + offload, Day 2 edit + reflect + submit.
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
HAVE_DOWNLOADS=False

COURSES=[
  {"prefix":"photo1","label":"Photography 1A","mod":"13",
   "reflect_en":f"{SITE}/assets/course-documents/Mystery-Item-Reflection-EN.docx",
   "reflect_es":f"{SITE}/assets/course-documents/Mystery-Item-Reflection-ES.docx",
   "zip":f"{SITE}/assets/templates/mystery-item/Mystery-Item-Project-Folder.zip"},
  {"prefix":"photo2","label":"Photography 2A","mod":"13",
   "reflect_en":f"{SITE}/assets/course-documents/Mystery-Item-Photo2-Reflection-EN.docx",
   "reflect_es":f"{SITE}/assets/course-documents/Mystery-Item-Photo2-Reflection-ES.docx",
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
   "en_desc":"You cull your take and edit your strongest image in Adobe Camera Raw and Photoshop to finish a clean, polished photo.",
   "es_desc":"Seleccionas de tu trabajo y editas tu imagen m&aacute;s fuerte en Adobe Camera Raw y Photoshop para terminar una foto limpia y pulida."},
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
        lead=("Descarga la carpeta del proyecto del M&oacute;dulo Mystery Item. Trae el documento de reflexi&oacute;n en Word que llenar&aacute;s al final."
              if es else "Download the Mystery Item project folder. It holds the Word reflection document you will fill out at the end.")
        ziplabel="Carpeta del Proyecto Mystery Item (ZIP)" if es else "Mystery Item Project Folder (ZIP)"
        reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
        ref=C['reflect_es'] if es else C['reflect_en']
        return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
          + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
          + para(lead)
          + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
          + dl_link(C['zip'],ziplabel,row=True) + dl_link(ref,reflabel,row=True)
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
                ("Step 02 &middot; Capture &amp; Contact:","open your bag, pick an approach, and photograph your item in Manual mode. Then build a contact sheet of your raw images."),
                ("Step 03 &middot; Cull &amp; Edit:","choose your strongest image, edit it in Adobe Camera Raw and Photoshop, and export your final JPEG."),
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
               ("Adobe Camera Raw","The Adobe tool where you open and edit raw photos: exposure, contrast, color, and cropping.")]))
        en+=next_up("UP NEXT &middot; STEP 02 - Capture &amp; Contact","Open your bag, choose an approach, photograph your item, and build a contact sheet of your raw images.")

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
                ("Paso 02 &middot; Captura y Contacto:","abre tu bolsa, elige un enfoque y fotograf&iacute;a tu objeto en modo Manual. Luego arma una hoja de contactos de tus im&aacute;genes RAW."),
                ("Paso 03 &middot; Selecci&oacute;n y Edici&oacute;n:","elige tu imagen m&aacute;s fuerte, ed&iacute;tala en Adobe Camera Raw y Photoshop, y exporta tu JPEG final."),
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
               ("Adobe Camera Raw","La herramienta de Adobe donde abres y editas fotos RAW: exposici&oacute;n, contraste, color y recorte.")]))
        es+=next_up("SIGUIENTE &middot; PASO 02 - Captura y Contacto","Abre tu bolsa, elige un enfoque, fotograf&iacute;a tu objeto y arma una hoja de contactos de tus im&aacute;genes RAW.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
        return wrap_page(f"Mystery Item: Start Here | {LABEL} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 02: Capture & Contact =================
    def step_capture():
        float2_en=float_right(f"{SITE}/assets/images/mystery-item/capture-float-v3.jpg","A student photographing a mystery item with the camera kit","Try different angles, distances, and lighting.") if HAVE_S2_FLOAT else ""
        float2_es=float_right(f"{SITE}/assets/images/mystery-item/capture-float-v3.jpg","Un estudiante fotografiando un objeto misterioso con el kit de c&aacute;mara","Prueba distintos &aacute;ngulos, distancias e iluminaci&oacute;n.") if HAVE_S2_FLOAT else ""
        en=banner(f"Module {MOD} &bull; Step 02","Capture &amp; Contact","Open your bag, choose an approach, photograph your item in Manual mode, and build a contact sheet.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
        en+=type_card("photo-walk","Step 02 &middot; Capture","Open Your Bag and Make a Plan",
            float2_en
            + para("Match your <strong>camera kit number</strong> to the <strong>brown paper bag</strong> with the same number. Only use the item from your matching bag. Open it with your partner and see your mystery item for the first time.")
            + para("Talk together: what kind of photo fits this item? Look back at the approaches on Step 01, then pick one. You can ask Mr. Silva for an <strong>LED light or a reflector</strong> if you want to try creative lighting.")
            + note("Both partners take photos. You plan together, but each of you ends up with your own set of images to edit."))
        en+=deliverables_box(False,
            [("1 contact sheet:","a contact sheet of your raw images, turned in as a high-resolution JPG. Each partner turns in their own, even though you worked together.")])
        en+=capture_note("raw","Work in Manual mode (M) with a balanced exposure: watch your light meter and keep it near the middle. Capture in {fmt} so you keep all the camera&rsquo;s data and have the most room to edit.", False)
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
        en+=card("OFFLOAD &amp; BUILD / CONTACT SHEET","Offload, Then Make Your Contact Sheet",
            para("Move your photos to your computer, then make one <strong>contact sheet</strong> that shows your whole take in a grid. On a Mac, Adobe Bridge builds it for you.")
            + steps([
                ("Offload your photos:","copy your raw files from the camera kit into your <strong>Photography folder on OneDrive</strong>. Each partner keeps their own copy."),
                ("Open Adobe Bridge:","open Bridge and go to your project folder. Select all of your raw images for this project."),
                ("Make the contact sheet:","go to <strong>Tools &rsaquo; Photoshop &rsaquo; Contact Sheet II</strong>. Let it build one sheet of all your images in Photoshop."),
                ("Save as a JPG:","in Photoshop, go to <strong>File &rsaquo; Export &rsaquo; Save a Copy</strong> and save your contact sheet as a high-resolution JPG, then upload it here."),
            ])
            + note("Contact sheets are always turned in as a high-resolution JPG. Do not edit your photos yet, that happens in Step 03."))
        en+=next_up("UP NEXT &middot; STEP 03 - Cull &amp; Edit","Choose your strongest image, edit it in Adobe Camera Raw and Photoshop, and export your final JPEG.")

        es=banner(f"M&oacute;dulo {MOD} &bull; Paso 02","Captura y Contacto","Abre tu bolsa, elige un enfoque, fotograf&iacute;a tu objeto en modo Manual y arma una hoja de contactos.","#top","Back to English", HICON_PHOTO_WALK)
        es+=type_card("photo-walk","Paso 02 &middot; Captura","Abre Tu Bolsa y Haz un Plan",
            float2_es
            + para("Haz coincidir tu <strong>n&uacute;mero de kit de c&aacute;mara</strong> con la <strong>bolsa de papel caf&eacute;</strong> del mismo n&uacute;mero. Usa solo el objeto de tu bolsa. &Aacute;brela con tu compa&ntilde;ero y ve tu objeto misterioso por primera vez.")
            + para("Hablen juntos: &iquest;qu&eacute; tipo de foto va con este objeto? Mira los enfoques del Paso 01 y luego elige uno. Puedes pedirle a Mr. Silva una <strong>luz LED o un reflector</strong> si quieres probar iluminaci&oacute;n creativa.")
            + note("Los dos compa&ntilde;eros toman fotos. Planean juntos, pero cada uno termina con su propio grupo de im&aacute;genes para editar."))
        es+=deliverables_box(True,
            [("1 hoja de contactos:","una hoja de contactos de tus im&aacute;genes RAW, entregada como un JPG de alta resoluci&oacute;n. Cada compa&ntilde;ero entrega la suya, aunque trabajaron juntos.")])
        es+=capture_note("raw","Trabaja en modo Manual (M) con una exposici&oacute;n equilibrada: observa tu expos&iacute;metro y mant&eacute;nlo cerca del centro. Captura en {fmt} para guardar todos los datos de la c&aacute;mara y tener el mayor espacio para editar.", True)
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
        es+=card("DESCARGA Y ARMA / HOJA DE CONTACTOS","Descarga, Luego Arma Tu Hoja de Contactos",
            para("Pasa tus fotos a tu computadora, luego arma una <strong>hoja de contactos</strong> que muestre todo tu trabajo en una cuadr&iacute;cula. En una Mac, Adobe Bridge la arma por ti.")
            + steps([
                ("Descarga tus fotos:","copia tus archivos RAW del kit de c&aacute;mara a tu <strong>carpeta de Fotograf&iacute;a en OneDrive</strong>. Cada compa&ntilde;ero guarda su propia copia."),
                ("Abre Adobe Bridge:","abre Bridge y ve a la carpeta de tu proyecto. Selecciona todas tus im&aacute;genes RAW de este proyecto."),
                ("Arma la hoja de contactos:","ve a <strong>Tools &rsaquo; Photoshop &rsaquo; Contact Sheet II</strong>. Deja que arme una hoja con todas tus im&aacute;genes en Photoshop."),
                ("Guarda como JPG:","en Photoshop, ve a <strong>File &rsaquo; Export &rsaquo; Save a Copy</strong> y guarda tu hoja de contactos como un JPG de alta resoluci&oacute;n, luego s&uacute;bela aqu&iacute;."),
            ])
            + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n. No edites tus fotos todav&iacute;a, eso es en el Paso 03."))
        es+=next_up("SIGUIENTE &middot; PASO 03 - Selecci&oacute;n y Edici&oacute;n","Elige tu imagen m&aacute;s fuerte, ed&iacute;tala en Adobe Camera Raw y Photoshop, y exporta tu JPEG final.")

        stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
        return wrap_page(f"Step 2: Capture and Contact | Mystery Item | {LABEL} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 03: Cull & Edit =================
    def step_edit():
        float3_en=float_right(f"{SITE}/assets/images/mystery-item/edit-float-v1.jpg","A student editing a mystery item photo in Adobe Camera Raw","Cull first, then edit your strongest image.") if HAVE_S3_FLOAT else ""
        float3_es=float_right(f"{SITE}/assets/images/mystery-item/edit-float-v1.jpg","Un estudiante editando una foto del objeto misterioso en Adobe Camera Raw","Selecciona primero, luego edita tu imagen m&aacute;s fuerte.") if HAVE_S3_FLOAT else ""
        en=banner(f"Module {MOD} &bull; Step 03","Cull &amp; Edit","Choose your strongest image, edit it in Adobe Camera Raw and Photoshop, and export your final JPEG.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
        en+=type_card("edit","Step 03 &middot; Cull","Choose Your Strongest Image",
            float3_en
            + para("Open your raw images in <strong>Adobe Camera Raw</strong> and look through your whole take. <strong>Cull</strong> means you choose your strongest work and let the rest go. Rate your best with stars and reject the ones you will not use.")
            + bullets([
                ("Open in Camera Raw:","load your raw files from your OneDrive project folder into Adobe Camera Raw."),
                ("Cull your take:","give your strongest images stars; reject the weak or blurry ones."),
                ("Pick one, or a small set:","choose your single strongest image, or a few if your idea works better as a short series."),
            ])
            + note("Call these your selections, not &ldquo;picks.&rdquo; Choose on purpose, based on your idea."))
        en+=deliverables_box(False,
            [("Your final photo(s):","your strongest edited image, exported as a high-resolution JPG. If your idea is a short series, export each final image. Name each file with your <strong>first name and last initial</strong>."),
             ("Turn in your own:","each partner edits and submits their own final image(s), even though you worked together.")])
        en+=card("EDIT IT / CAMERA RAW + PHOTOSHOP","Make Your Image Its Best",
            para("Edit your selection in <strong>Adobe Camera Raw</strong> and <strong>Adobe Photoshop</strong>. Your edits should support your idea, not fight it.")
            + steps([
                ("Set your exposure and color:","adjust exposure, contrast, highlights, shadows, and white balance until the light looks right."),
                ("Add clarity and crop:","sharpen or add clarity if it helps, then crop to clean your composition and edges."),
                ("Remove distractions:","in Photoshop, remove things that pull the eye away (a stray object, debris, a mark) if it makes the photo stronger."),
                ("Keep it honest:","edit to make your item look its best. Do not change it into something it is not."),
            ]))
        en+=card("EXPORT / SAVE YOUR FINAL JPEG","Name It and Save It Right",
            steps([
                ("Export as JPEG:","in Camera Raw or Photoshop, save or export your final image as a high-resolution <strong>JPEG</strong>."),
                ("Name your file:","start the file name with your <strong>first name and last initial</strong> (like <strong>MariaG</strong>)."),
                ("Save in your folder:","save it in your Mystery Item project folder on OneDrive, then upload it to this Canvas assignment."),
            ])
            + note("Turn in your final JPEG(s) only, your best edited work."))
        en+=next_up("UP NEXT &middot; STEP 04 - Reflection","Tell your idea, how you photographed your item, and what worked and what was hard.")

        es=banner(f"M&oacute;dulo {MOD} &bull; Paso 03","Selecci&oacute;n y Edici&oacute;n","Elige tu imagen m&aacute;s fuerte, ed&iacute;tala en Adobe Camera Raw y Photoshop, y exporta tu JPEG final.","#top","Back to English", HICON_DESIGN)
        es+=type_card("edit","Paso 03 &middot; Selecci&oacute;n","Elige Tu Imagen M&aacute;s Fuerte",
            float3_es
            + para("Abre tus im&aacute;genes RAW en <strong>Adobe Camera Raw</strong> y revisa todo tu trabajo. <strong>Seleccionar</strong> significa elegir tu trabajo m&aacute;s fuerte y dejar ir el resto. Marca tus mejores con estrellas y rechaza las que no vas a usar.")
            + bullets([
                ("Abre en Camera Raw:","carga tus archivos RAW desde tu carpeta de proyecto en OneDrive a Adobe Camera Raw."),
                ("Selecciona de tu trabajo:","dale estrellas a tus im&aacute;genes m&aacute;s fuertes; rechaza las d&eacute;biles o borrosas."),
                ("Elige una, o un grupo peque&ntilde;o:","elige tu imagen m&aacute;s fuerte, o unas pocas si tu idea funciona mejor como una serie corta."),
            ])
            + note("Llama a estas tus selecciones. Elige a prop&oacute;sito, seg&uacute;n tu idea."))
        es+=deliverables_box(True,
            [("Tu foto(s) final(es):","tu imagen editada m&aacute;s fuerte, exportada como un JPG de alta resoluci&oacute;n. Si tu idea es una serie corta, exporta cada imagen final. Nombra cada archivo con tu <strong>primer nombre e inicial del apellido</strong>."),
             ("Entrega lo tuyo:","cada compa&ntilde;ero edita y entrega sus propias im&aacute;genes finales, aunque trabajaron juntos.")])
        es+=card("ED&Iacute;TALA / CAMERA RAW + PHOTOSHOP","Haz que Tu Imagen se Vea lo Mejor",
            para("Edita tu selecci&oacute;n en <strong>Adobe Camera Raw</strong> y <strong>Adobe Photoshop</strong>. Tus ediciones deben apoyar tu idea, no pelear con ella.")
            + steps([
                ("Ajusta exposici&oacute;n y color:","ajusta la exposici&oacute;n, el contraste, las luces, las sombras y el balance de blancos hasta que la luz se vea bien."),
                ("Agrega claridad y recorta:","aumenta la nitidez o la claridad si ayuda, luego recorta para limpiar tu composici&oacute;n y tus bordes."),
                ("Quita distracciones:","en Photoshop, quita lo que jala la mirada (un objeto perdido, basura, una marca) si hace m&aacute;s fuerte la foto."),
                ("Mant&eacute;nla honesta:","edita para que tu objeto se vea lo mejor. No lo cambies en algo que no es."),
            ]))
        es+=card("EXPORTA / GUARDA TU JPEG FINAL","Nombr&aacute;lo y Gu&aacute;rdalo Bien",
            steps([
                ("Exporta como JPEG:","en Camera Raw o Photoshop, guarda o exporta tu imagen final como un <strong>JPEG</strong> de alta resoluci&oacute;n."),
                ("Nombra tu archivo:","empieza el nombre del archivo con tu <strong>primer nombre e inicial del apellido</strong> (como <strong>MariaG</strong>)."),
                ("Gu&aacute;rdalo en tu carpeta:","gu&aacute;rdalo en tu carpeta del proyecto Mystery Item en OneDrive, luego s&uacute;belo a esta tarea de Canvas."),
            ])
            + note("Entrega solo tu JPEG final, tu mejor trabajo editado."))
        es+=next_up("SIGUIENTE &middot; PASO 04 - Reflexi&oacute;n","Cuenta tu idea, c&oacute;mo fotografiaste tu objeto, y qu&eacute; funcion&oacute; y qu&eacute; fue dif&iacute;cil.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S4}" class="silva-step-btn">Step 04 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S4}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
        return wrap_page(f"Step 3: Cull and Edit | Mystery Item | {LABEL} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 04: Reflection =================
    def step_reflect():
        ref_note_en=("Open the reflection document from your project folder (Step 01, the Overview). Before you open it, move it from your Downloads folder into your project folder."
                     if HAVE_DOWNLOADS else "Your teacher will give you the reflection Word document to fill out. Save it in your Mystery Item project folder before you start.")
        ref_note_es=("Abre el documento de reflexi&oacute;n de tu carpeta del proyecto (Paso 01, el Resumen). Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto."
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
