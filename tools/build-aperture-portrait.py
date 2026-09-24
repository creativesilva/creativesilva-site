#!/usr/bin/env python3
# Photography 1A - Module 08: Aperture Portrait (partner photo walk).
# Explore APERTURE by capturing a partner portrait at f/8, f/4, and f/2. Manual mode,
# ISO 100 constant, adjust the shutter to balance the light meter. JPG capture, crop-only edit.
# Overview + 3 steps (Capture & Contact Sheet, Cull & Submit, Reflection), bilingual EN/ES, 5th-grade.
# Dark teal angular framework via silva_framework. Pages: Step 01 Overview (read + download) +
# Steps 02-04. Images are per-slot (HAVE_* flags): header, capture and reflection floats are LIVE;
# the cull float awaits art and renders NOTHING until placed. Camera-kit module: NO fresh-photos note.
import os, re
from silva_framework import *   # shared angular chrome: banner, cards, sections, vocab, deliverables, etc.

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"

# --- images (per-slot: header + reflection LIVE; step 1/2 floats await art, render nothing) ---
IMGDIR=f"{SITE}/assets/images/photo1/aperture-portrait"
HEADER=f"{IMGDIR}/header-v1.jpg"            # overview hero (LIVE)
S1_FLOAT=f"{IMGDIR}/capture-float-v2.jpg"   # step 2 capture image (LIVE)
S2_FLOAT=f"{IMGDIR}/cull-float-v1.jpg"      # step 2 cull/submit image (placeholder)
S3_FLOAT=f"{IMGDIR}/reflection-float-v1.jpg"# step 3 reflection image (LIVE)
HAVE_HEADER=True       # header art placed; overview hero renders
HAVE_S1_FLOAT=True     # capture float, Step 02 page (placed)
HAVE_S2_FLOAT=False    # cull float, Step 03 page (awaiting photo)
HAVE_S3_FLOAT=True     # reflection float, Step 04 page (placed)

# --- downloadable files ---
CONTACT_ZIP=f"{SITE}/assets/PVHS_Contact_Sheet_Presets.zip"   # 12-Up + 6-Up presets (installed earlier in Image Series)
REFLECT_EN=f"{SITE}/assets/course-documents/Aperture-Portrait-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Aperture-Portrait-Reflection-ES.docx"
EXPOSURE_FULL=f"{SITE}/assets/images/shared/exposure-basics-v1.jpg"     # exposure-basics poster (click to open full)
EXPOSURE_THUMB=f"{SITE}/assets/images/shared/exposure-basics-thumb-v1.jpg"

OVER="photo1-aperture-portrait-overview.html"
S1="photo1-aperture-portrait-step01-capture-contact.html"
S2="photo1-aperture-portrait-step02-cull-submit.html"
S3="photo1-aperture-portrait-step03-reflection.html"
MODNAME_EN="Aperture Portrait"; MODNAME_ES="Retrato de Apertura"

# Local ent: convert stray accents to entities AND map an en-dash to a plain hyphen (never emit
# &ndash;, per Chris's hard dash ban). silva_framework's ent maps en-dash to &ndash;, so we override.
def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

def float_ph(label):
    # Floated dashed placeholder that sits in the same right-hand thumbnail column a real
    # float_right image will use, so the layout is already correct. Swap to float_right(...) later.
    return '<!--FLOAT-->'+placeholder(label, minh=300)+'<!--/FLOAT-->'

def hero_ph(label):
    return placeholder(label, minh=300)

# ---- nav breadcrumb + progress dots ----
def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Aperture Portrait</a>\n'
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

# ---- custom camera-settings section (aperture is the creative variable; shutter balances) ----
def aperture_settings_section(es, quality="JPG"):
    red="#f90101"
    if es:
        title="Ajustes de C&aacute;mara"
        lead=("Trabaja en modo Manual (M). Mant&eacute;n tu ISO en 100 todo el tiempo. Debes capturar un buen retrato en las TRES aperturas: f/8, f/4 y f/2. "
              "Puedes empezar en f/8 o en f/2, pero pasa por las tres en orden. Cada vez que cambies la apertura, ajusta el obturador para equilibrar el expos&iacute;metro.")
        note_t=("No es elegir una sola apertura: capturas las tres, en orden. Cuando est&eacute;s en f/8, hazla un paso m&aacute;s brillante (apunta a <strong>+1</strong> en el expos&iacute;metro). "
                "En f/4 y f/2, equilibra el expos&iacute;metro. Solo se mueven dos ajustes: la apertura (en orden) y el obturador (para equilibrar). El ISO se queda en 100.")
    else:
        title="Camera Settings"
        lead=("Work in Manual mode (M). Keep your ISO at 100 the whole time. You must capture a good portrait at ALL three apertures: f/8, f/4, and f/2. "
              "You can start at f/8 or at f/2, but go through all three in order. Every time you change the aperture, adjust the shutter to balance the light meter.")
        note_t=("This is not a free choice of one aperture: you capture all three, in order. When you are at f/8, make it one stop bright (aim for <strong>+1</strong> on the light meter). "
                "At f/4 and f/2, balance the meter. Only two settings move: the aperture (in order) and the shutter (to balance). ISO stays at 100.")
    lead_html=f'<div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{lead}</span></div>'
    note_box=(f'<div style="background:rgba(249,1,1,0.10);border:1px solid rgba(249,1,1,0.30);border-left:4px solid {red};padding:11px 14px;margin:0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.92);line-height:1.55;">{note_t}</div>')
    return (f'<div style="background:linear-gradient(180deg,rgba(249,1,1,0.06) 0%,rgba(249,1,1,0.02) 100%);border:1px solid rgba(249,1,1,0.26);border-left:6px solid {red};padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(CAMSET_ICON, title, "#f90101", "#ff8f8f")
      + f'<div class="silva-cfloat" style="float:right;width:50%;min-width:400px;margin:2px 0 16px 30px;">{capture_panel(quality, "1/500", "F8", "100", "shutter")}</div>'
      + lead_html + note_box + '</div>')

# ---- downloads (Overview) ----
def exposure_poster(es):
    # Purple RESOURCE: a clickable thumbnail of the Exposure Basics poster that opens the full
    # image in a new tab (so students can read the fine print large).
    if es:
        heading="P&oacute;ster de Conceptos de Exposici&oacute;n"
        body=para("Este p&oacute;ster repasa lo b&aacute;sico de la exposici&oacute;n: la apertura, la velocidad del obturador y el ISO, y c&oacute;mo cada n&uacute;mero cambia la luz, el movimiento, la profundidad de campo y el grano. &Uacute;salo como referencia mientras equilibras tu exposici&oacute;n.")
        alt="P&oacute;ster de Conceptos de Exposici&oacute;n: apertura, velocidad del obturador e ISO"
        cap="Toca para abrirlo en grande en una pesta&ntilde;a nueva."
    else:
        heading="Exposure Basics Poster"
        body=para("This poster covers the basics of exposure: aperture, shutter speed, and ISO, and how each number changes light, motion, depth of field, and grain. Use it as a reference while you balance your exposure.")
        alt="Exposure Basics poster: aperture, shutter speed, and ISO"
        cap="Tap to open it full size in a new tab."
    return resources_card(heading, body, es, floatimg=purple_thumb(EXPOSURE_FULL, EXPOSURE_THUMB, alt, cap))

def downloads_block(es):
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga el documento de reflexi&oacute;n de este m&oacute;dulo. Tus ajustes de hoja de contactos ya est&aacute;n instalados en Lightroom; si alguna vez los necesitas otra vez, est&aacute;n en la p&aacute;gina de Resumen del curso." if es
          else "Download this module&rsquo;s reflection document. Your contact sheet presets are already installed in Lightroom; if you ever need them again, they are on the Course Overview page.")
    reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
    ref=REFLECT_ES if es else REFLECT_EN
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ref,reflabel,row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

APERTURE_STANDARDS=[
  {"code":"SA.17.5","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Equipment &amp; Image Production","es_title":"Equipo y Producci&oacute;n de Imagen",
   "en_desc":"You use the class camera kit in Manual mode and control aperture, shutter, and ISO on purpose.",
   "es_desc":"Usas el kit de c&aacute;mara de la clase en modo Manual y controlas la apertura, el obturador y el ISO a prop&oacute;sito."},
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You use depth of field and background separation to make a strong portrait.",
   "es_desc":"Usas la profundidad de campo y la separaci&oacute;n del fondo para hacer un retrato fuerte."},
  {"code":"SA.17.2","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Visual Communication","es_title":"Comunicaci&oacute;n Visual",
   "en_desc":"You direct a partner and frame a portrait that communicates, not a stiff ID photo.",
   "es_desc":"Diriges a tu compa&ntilde;ero y encuadras un retrato que comunica, no una foto de identificaci&oacute;n r&iacute;gida."},
  {"code":"SA.17.8","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Documentation of Finished Work","es_title":"Documentaci&oacute;n del Trabajo Terminado",
   "en_desc":"You build contact sheets that present your take and your final selections clearly.",
   "es_desc":"Creas hojas de contactos que presentan tu trabajo y tus selecciones finales con claridad."},
]

# ================= OVERVIEW =================
def overview():
    en=banner("Module 08 &bull; Step 01","Aperture Portrait: Start Here","Read this page and download your files, then go to Step 02 to capture. This is a partner photo walk about aperture.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
    en+=type_card("overview","Step 01 &middot; Read &amp; Download","One Partner, Three Apertures",
        para("This is a partner photo walk about <strong>aperture</strong>. You and a partner take turns: one of you is the <strong>photographer</strong> and the other is the <strong>subject</strong> (the person being photographed). Then you switch, so each of you photographs and each of you gets photographed.")
        + para("You work in Manual mode with the Canon R50 and the RF 50mm f/1.8 lens. ISO stays at 100. You capture the same portrait at three apertures: <strong>f/8</strong>, then <strong>f/4</strong>, then <strong>f/2</strong>, adjusting the shutter each time to balance the light. Then you build a contact sheet, pick your best three, and reflect.")
        + (framed(HEADER,"Aperture Portrait module header") if HAVE_HEADER else hero_ph("HEADER IMAGE PLACEHOLDER &middot; Aperture Portrait overview hero (16:9). Swap in when ready.")))
    en+=standards_box(False, APERTURE_STANDARDS)
    en+=downloads_block(False)
    en+=card("THE CONCEPT / WHAT APERTURE DOES","Aperture and Depth of Field",
        para("Aperture is how wide the lens opens. It is written as an f-stop, like f/8 or f/2. Aperture changes two things at once: how much light comes in, and how much of your photo is in focus (this is called <strong>depth of field</strong>).")
        + bullets([
            ("f/8 (smaller opening):","more of the photo is sharp, from your subject to the background. A deeper focus."),
            ("f/2 (wider opening):","only your subject is sharp and the background goes soft and blurry. This makes your subject pop and separate from the background."),
            ("f/4 (in between):","a middle look, between the two."),
        ])
        + note("Because a wider aperture also lets in more light, you change your shutter each time to keep the light balanced. Same photo, three apertures, three looks."))
    en+=card("MAKE IT A PORTRAIT / NOT A FLAT PHOTO","Frame, Light, and Depth",
        para("A portrait is framed from the <strong>waist up, or closer</strong>. Turn the camera on its side so it is <strong>tall (portrait orientation)</strong>, not wide. Most people forget and leave the camera sideways, so check every time.")
        + bullets([
            ("Find soft light:","you are photographing in bright sun. Move into open shade so the light is soft and flattering, not harsh."),
            ("Step off the wall:","do not stand your partner right against a wall. Have them take a few steps forward. This is not a stiff ID photo, it is a portrait, so build some depth and separate them from the background."),
            ("Fill the frame:","waist up or closer, with the eyes near the top third."),
        ]))
    en+=card("HOW IT WORKS / YOUR PLAN","Your Next Three Steps",
        para("You are on Step 01 now: read this page and download your files below. Here are the three steps that follow.")
        + bullets([
            ("Step 02 &middot; Capture &amp; Contact Sheet:","in Manual mode, capture your partner at f/8, f/4, and f/2 (then switch roles). Build and turn in a 12-Up contact sheet of your whole take."),
            ("Step 03 &middot; Cull &amp; Submit:","pick your best three, one at each f-stop, crop them, and turn in a 6-Up contact sheet plus the three final JPGs."),
            ("Step 04 &middot; Reflection:","tell what you learned about balancing your exposure."),
        ])
        + note("This is a JPG capture. Get your exposure right in the camera so it looks good straight out of the camera. The only edit you need is a crop."))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Aperture","How wide the lens opens, written as an f-stop like f/8 or f/2."),
           ("F-stop","The number for the aperture. A small number (f/2) is a wide opening; a big number (f/8) is a smaller opening."),
           ("Depth of Field","How much of the photo is in focus, from near to far. Wide aperture = shallow (blurry background); small aperture = deep (more in focus)."),
           ("Exposure","How bright or dark the photo is. You balance it with your settings."),
           ("Light Meter","The scale in the camera that shows if your photo is too dark, too bright, or balanced."),
           ("Portrait Orientation","Holding the camera tall (on its side) so the photo is taller than it is wide.")]))
    en+=next_up("UP NEXT &middot; STEP 02 - Capture &amp; Contact Sheet","Set Manual mode, capture at f/8, f/4, and f/2, then build your 12-Up contact sheet.")

    es=banner("M&oacute;dulo 08 &bull; Paso 01","Retrato de Apertura: Empieza Aqu&iacute;","Lee esta p&aacute;gina y descarga tus archivos, luego ve al Paso 02 para capturar. Esta es una caminata en pareja sobre la apertura.","#top","Back to English", HICON_PHOTO_WALK)
    es+=type_card("overview","Paso 01 &middot; Lee y Descarga","Una Pareja, Tres Aperturas",
        para("Esta es una caminata fotogr&aacute;fica en pareja sobre la <strong>apertura</strong>. T&uacute; y tu compa&ntilde;ero se turnan: uno es el <strong>fot&oacute;grafo</strong> y el otro es el <strong>sujeto</strong> (la persona fotografiada). Luego cambian, para que cada uno fotograf&iacute;e y cada uno sea fotografiado.")
        + para("Trabajas en modo Manual con la Canon R50 y el lente RF 50mm f/1.8. El ISO se queda en 100. Capturas el mismo retrato en tres aperturas: <strong>f/8</strong>, luego <strong>f/4</strong>, luego <strong>f/2</strong>, ajustando el obturador cada vez para equilibrar la luz. Despu&eacute;s armas una hoja de contactos, eliges tus tres mejores y reflexionas.")
        + (framed(HEADER,"Encabezado del m&oacute;dulo Retrato de Apertura") if HAVE_HEADER else hero_ph("IMAGEN DE ENCABEZADO (PLACEHOLDER) &middot; se cambia despu&eacute;s")))
    es+=standards_box(True, APERTURE_STANDARDS)
    es+=downloads_block(True)
    es+=card("EL CONCEPTO / QU&Eacute; HACE LA APERTURA","Apertura y Profundidad de Campo",
        para("La apertura es qu&eacute; tan abierto est&aacute; el lente. Se escribe como un n&uacute;mero f, como f/8 o f/2. La apertura cambia dos cosas a la vez: cu&aacute;nta luz entra y cu&aacute;nto de tu foto est&aacute; enfocado (esto se llama <strong>profundidad de campo</strong>).")
        + bullets([
            ("f/8 (abertura m&aacute;s peque&ntilde;a):","m&aacute;s de la foto est&aacute; n&iacute;tida, desde tu sujeto hasta el fondo. Un enfoque m&aacute;s profundo."),
            ("f/2 (abertura m&aacute;s amplia):","solo tu sujeto est&aacute; n&iacute;tido y el fondo se pone suave y borroso. Esto hace que tu sujeto resalte y se separe del fondo."),
            ("f/4 (en medio):","un look intermedio entre los dos."),
        ])
        + note("Como una apertura m&aacute;s amplia tambi&eacute;n deja entrar m&aacute;s luz, cambias el obturador cada vez para mantener la luz equilibrada. La misma foto, tres aperturas, tres estilos."))
    es+=card("HAZLO UN RETRATO / NO UNA FOTO PLANA","Encuadre, Luz y Profundidad",
        para("Un retrato se encuadra de la <strong>cintura para arriba, o m&aacute;s cerca</strong>. Voltea la c&aacute;mara de lado para que quede <strong>vertical (orientaci&oacute;n de retrato)</strong>, no horizontal. Muchos olvidan y dejan la c&aacute;mara acostada, as&iacute; que revisa cada vez.")
        + bullets([
            ("Busca luz suave:","est&aacute;s fotografiando con sol fuerte. Mu&eacute;vete a una sombra abierta para que la luz sea suave y favorecedora, no dura."),
            ("Sep&aacute;rate de la pared:","no pongas a tu compa&ntilde;ero pegado a una pared. Que d&eacute; unos pasos hacia adelante. Esto no es una foto de identificaci&oacute;n r&iacute;gida, es un retrato, as&iacute; que crea profundidad y sep&aacute;ralo del fondo."),
            ("Llena el cuadro:","de la cintura para arriba o m&aacute;s cerca, con los ojos cerca del tercio superior."),
        ]))
    es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Siguientes Tres Pasos",
        para("Est&aacute;s en el Paso 01: lee esta p&aacute;gina y descarga tus archivos abajo. Estos son los tres pasos que siguen.")
        + bullets([
            ("Paso 02 &middot; Captura y Hoja de Contactos:","en modo Manual, captura a tu compa&ntilde;ero en f/8, f/4 y f/2 (luego cambien de rol). Arma y entrega una hoja de contactos de 12 im&aacute;genes de todo tu trabajo."),
            ("Paso 03 &middot; Selecciona y Entrega:","elige tus tres mejores, una en cada n&uacute;mero f, rec&oacute;rtalas y entrega una hoja de contactos de 6 im&aacute;genes m&aacute;s las tres im&aacute;genes finales en JPG."),
            ("Paso 04 &middot; Reflexi&oacute;n:","cuenta qu&eacute; aprendiste sobre equilibrar tu exposici&oacute;n."),
        ])
        + note("Esta es una captura en JPG. Deja bien tu exposici&oacute;n en la c&aacute;mara para que se vea bien tal como sale. La &uacute;nica edici&oacute;n que necesitas es un recorte."))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Aperture (Apertura)","Qu&eacute; tan abierto est&aacute; el lente, escrito como un n&uacute;mero f, como f/8 o f/2."),
           ("F-stop (N&uacute;mero f)","El n&uacute;mero de la apertura. Un n&uacute;mero peque&ntilde;o (f/2) es una abertura amplia; uno grande (f/8) es una abertura m&aacute;s peque&ntilde;a."),
           ("Depth of Field (Profundidad de Campo)","Cu&aacute;nto de la foto est&aacute; enfocado, de cerca a lejos. Apertura amplia = poca (fondo borroso); apertura peque&ntilde;a = mucha (m&aacute;s enfocado)."),
           ("Exposure (Exposici&oacute;n)","Qu&eacute; tan brillante u oscura es la foto. La equilibras con tus ajustes."),
           ("Light Meter (Expos&iacute;metro)","La escala en la c&aacute;mara que muestra si tu foto est&aacute; muy oscura, muy brillante o equilibrada."),
           ("Portrait Orientation (Orientaci&oacute;n de Retrato)","Sostener la c&aacute;mara vertical (de lado) para que la foto sea m&aacute;s alta que ancha.")]), True)
    es+=next_up("SIGUIENTE &middot; PASO 02 - Captura y Hoja de Contactos","Pon el modo Manual, captura en f/8, f/4 y f/2, y arma tu hoja de contactos de 12.")

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
    return wrap_page("Aperture Portrait | Photography 1A | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ================= STEP 02 =================
def step01():
    en=banner("Module 08 &bull; Step 02","Capture &amp; Contact Sheet","Capture your partner at f/8, f/4, and f/2, then build a 12-Up contact sheet.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
    en+=type_card("photo-walk","Step 02 &middot; On the Photo Walk","Take Turns: Photographer and Subject",
        para("Head out with your partner and the camera kit. One of you is the <strong>photographer</strong> and the other is the <strong>subject</strong>. Photograph your full set, then trade roles so you both get portraits and you both practice the camera.")
        + (float_right(S1_FLOAT,"A Pioneer Valley student photographing a partner in open shade with the Canon R50 held in portrait orientation","Camera on its side, one elbow up: that is portrait orientation.") if HAVE_S1_FLOAT else "")
        + bullets([
            ("Hold it tall:","turn the camera on its side with one elbow up in the air. This gives you portrait (tall) orientation. Do not leave it wide."),
            ("Frame waist up or closer:","fill the frame with your partner, eyes near the top third."),
            ("Open shade:","move out of the harsh sun into soft, even shade."),
            ("Step off the wall:","have your partner take a few steps forward from the background for depth and separation."),
        ]))
    en+=deliverables_box(False,
        [("1 contact sheet:","a 12-Up contact sheet of your entire take, turned in as a high-resolution JPG.")])
    en+=aperture_settings_section(False, "JPG")
    en+=exposure_poster(False)
    en+=card("YOUR THREE APERTURES / SET THE CAMERA","f/8, f/4, and f/2, in order",
        para("You must capture a good portrait at all three apertures, in order. You can start at f/8 or at f/2, then work through all three. Keep ISO at 100 and balance the light with your shutter at each one.")
        + steps([
            ("Set Manual mode:","turn the Mode dial to <strong>M</strong>."),
            ("Set ISO 100:","press the <strong>ISO button</strong>, then turn the dial to 100."),
            ("Set your aperture:","press the <strong>up arrow (Up key)</strong>, then turn the <strong>Main Dial</strong> to your f-stop."),
            ("Balance with the shutter:","turn the <strong>Main Dial</strong> to set the shutter speed until the light meter is balanced."),
            ("f/8 first:","set f/8 and make it one stop bright (aim for +1 on the meter). Capture a good portrait."),
            ("f/4 next:","set f/4, balance the shutter again, and capture."),
            ("f/2 last:","set f/2, balance the shutter again, and capture."),
        ], accent="#f90101")
        + note("At f/2 the background goes soft and your partner pops. At f/8 more of the scene stays sharp. Same portrait, three looks."))
    en+=card("BUILD IT / CONTACT SHEET","Turn In a 12-Up Contact Sheet",
        para("Bring your JPGs into Lightroom Classic and build a 12-Up contact sheet of your whole take, then print it to a high-resolution JPG.")
        + steps([
            ("Import your JPGs:","offload from the camera kit to OneDrive, then import into Lightroom Classic."),
            ("Use the 12-Up preset:","in the Print module, choose the 12-Up contact sheet preset (you installed it in Image Series)."),
            ("Print to JPG:","use Print to File so it saves as a high-resolution JPG, then upload it here."),
        ])
        + note("Contact sheets are always turned in as a high-resolution JPG."))
    en+=next_up("UP NEXT &middot; STEP 03 - Cull &amp; Submit","Pick your best three (one per f-stop), crop, and turn in a 6-Up plus the three final JPGs.")

    es=banner("M&oacute;dulo 08 &bull; Paso 02","Captura y Hoja de Contactos","Captura a tu compa&ntilde;ero en f/8, f/4 y f/2, y arma una hoja de contactos de 12.","#top","Back to English", HICON_PHOTO_WALK)
    es+=type_card("photo-walk","Paso 02 &middot; En la Caminata","Tomen Turnos: Fot&oacute;grafo y Sujeto",
        para("Salgan con tu compa&ntilde;ero y el kit de c&aacute;mara. Uno es el <strong>fot&oacute;grafo</strong> y el otro es el <strong>sujeto</strong>. Captura tu serie completa, luego cambien de rol para que ambos tengan retratos y ambos practiquen la c&aacute;mara.")
        + (float_right(S1_FLOAT,"Un estudiante de Pioneer Valley fotografiando a su compa&ntilde;ero en sombra abierta con la Canon R50 en orientaci&oacute;n vertical","C&aacute;mara de lado, un codo arriba: eso es orientaci&oacute;n de retrato.") if HAVE_S1_FLOAT else "")
        + bullets([
            ("Sost&eacute;nla vertical:","voltea la c&aacute;mara de lado con un codo arriba. Esto te da orientaci&oacute;n vertical (de retrato). No la dejes horizontal."),
            ("Encuadra de la cintura para arriba:","llena el cuadro con tu compa&ntilde;ero, los ojos cerca del tercio superior."),
            ("Sombra abierta:","sal del sol fuerte a una sombra suave y pareja."),
            ("Sep&aacute;rate de la pared:","que tu compa&ntilde;ero d&eacute; unos pasos hacia adelante para crear profundidad y separaci&oacute;n."),
        ]))
    es+=deliverables_box(True,
        [("1 hoja de contactos:","una hoja de contactos de 12 im&aacute;genes de todo tu trabajo, entregada como un JPG de alta resoluci&oacute;n.")])
    es+=aperture_settings_section(True, "JPG")
    es+=exposure_poster(True)
    es+=card("TUS TRES APERTURAS / AJUSTA LA C&Aacute;MARA","f/8, f/4 y f/2, en orden",
        para("Debes capturar un buen retrato en las tres aperturas, en orden. Puedes empezar en f/8 o en f/2, luego pasa por las tres. Mant&eacute;n el ISO en 100 y equilibra la luz con tu obturador en cada una.")
        + steps([
            ("Pon el modo Manual:","gira el dial de modo a <strong>M</strong>."),
            ("Pon ISO 100:","presiona el <strong>bot&oacute;n ISO</strong>, luego gira el dial a 100."),
            ("Pon tu apertura:","presiona la <strong>flecha hacia arriba</strong>, luego gira el <strong>dial principal</strong> a tu n&uacute;mero f."),
            ("Equilibra con el obturador:","gira el <strong>dial principal</strong> para ajustar la velocidad del obturador hasta que el expos&iacute;metro quede equilibrado."),
            ("f/8 primero:","pon f/8 y hazla un paso m&aacute;s brillante (apunta a +1 en el expos&iacute;metro). Captura un buen retrato."),
            ("f/4 despu&eacute;s:","pon f/4, equilibra el obturador otra vez y captura."),
            ("f/2 al final:","pon f/2, equilibra el obturador otra vez y captura."),
        ], accent="#f90101")
        + note("En f/2 el fondo se pone suave y tu compa&ntilde;ero resalta. En f/8 m&aacute;s de la escena queda n&iacute;tida. El mismo retrato, tres estilos."))
    es+=card("&Aacute;RMALA / HOJA DE CONTACTOS","Entrega una Hoja de Contactos de 12",
        para("Lleva tus JPG a Lightroom Classic y arma una hoja de contactos de 12 im&aacute;genes de todo tu trabajo, luego impr&iacute;mela como un JPG de alta resoluci&oacute;n.")
        + steps([
            ("Importa tus JPG:","descarga del kit de c&aacute;mara a OneDrive, luego importa a Lightroom Classic."),
            ("Usa el ajuste de 12:","en el m&oacute;dulo Print, elige el ajuste de hoja de contactos de 12 (lo instalaste en Serie de Im&aacute;genes)."),
            ("Imprime a JPG:","usa Print to File para que se guarde como un JPG de alta resoluci&oacute;n, luego s&uacute;belo aqu&iacute;."),
        ])
        + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n."))
    es+=next_up("SIGUIENTE &middot; PASO 03 - Selecciona y Entrega","Elige tus tres mejores (una por n&uacute;mero f), recorta y entrega una hoja de 6 m&aacute;s las tres im&aacute;genes finales.")

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S2}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S2}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Capture and Contact Sheet | Aperture Portrait | Photography 1A | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

# ================= STEP 03 =================
def step02():
    en=banner("Module 08 &bull; Step 03","Cull &amp; Submit","Pick your best three (one per f-stop), crop, and turn in a 6-Up plus three final JPGs.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
    en+=type_card("edit","Step 03 &middot; Cull","Choose Your Three Best",
        para("Look through your take and choose your three strongest portraits: <strong>one at f/8, one at f/4, and one at f/2</strong>. Keeping one at each f-stop shows the range of the aperture and sets up your reflection.")
        + (float_right(S2_FLOAT,"A Pioneer Valley student culling portraits in Lightroom Classic on an iMac in the lab","Compare your f/8, f/4, and f/2 portraits and keep the best of each.") if HAVE_S2_FLOAT else "")
        + bullets([
            ("One per f-stop:","your best f/8, your best f/4, and your best f/2."),
            ("Sharp eyes:","the eyes should be in focus. Skip any selections that are soft or squinting."),
            ("Good exposure:","keep the ones that are balanced and flattering."),
        ])
        + note("Call these your final selections, not &ldquo;picks.&rdquo; Choose on purpose."))
    en+=deliverables_box(False,
        [("1 contact sheet:","a 6-Up contact sheet with your three final images loaded, as a high-resolution JPG."),
         ("3 final photos:","your three polished portraits exported individually as high-resolution JPGs."),
         ("4 files total:","the 6-Up contact sheet plus the three final JPGs.")])
    en+=card("LIGHT EDIT / CROP ONLY","Get It Right in Camera, Then Crop",
        para("This is a JPG capture, so you got your exposure right in the camera. The only edit you need is a <strong>crop</strong>: tidy the framing so it reads as a clean portrait.")
        + bullets([
            ("Crop for the portrait:","waist up or closer, eyes near the top third, subject off-center if it looks better."),
            ("Do not over-edit:","no heavy color or filters. The photo should already look good out of the camera."),
        ]))
    en+=card("BUILD IT / CONTACT SHEET + EXPORTS","Turn In a 6-Up Plus Three JPGs",
        steps([
            ("Load your 3 finals:","in Lightroom Classic, select your three final portraits."),
            ("Build the 6-Up:","in the Print module, use the 6-Up contact sheet preset with your three finals loaded, and print it to a high-resolution JPG."),
            ("Export the 3 JPGs:","go to File &rsaquo; Export and export your three final portraits as high-resolution JPGs into your project folder."),
            ("Upload 4 files:","turn in the 6-Up contact sheet plus the three final JPGs."),
        ])
        + note("Contact sheets are always turned in as a high-resolution JPG."))
    en+=next_up("UP NEXT &middot; STEP 04 - Reflection","Tell what you learned about balancing your exposure and which f-stop you liked best.")

    es=banner("M&oacute;dulo 08 &bull; Paso 03","Selecciona y Entrega","Elige tus tres mejores (una por n&uacute;mero f), recorta y entrega una hoja de 6 m&aacute;s tres JPG finales.","#top","Back to English", HICON_PHOTO_WALK)
    es+=type_card("edit","Paso 03 &middot; Selecciona","Elige Tus Tres Mejores",
        para("Revisa tu trabajo y elige tus tres retratos m&aacute;s fuertes: <strong>uno en f/8, uno en f/4 y uno en f/2</strong>. Guardar uno en cada n&uacute;mero f muestra el rango de la apertura y prepara tu reflexi&oacute;n.")
        + (float_right(S2_FLOAT,"Un estudiante de Pioneer Valley seleccionando retratos en Lightroom Classic en una iMac en el laboratorio","Compara tus retratos de f/8, f/4 y f/2 y guarda el mejor de cada uno.") if HAVE_S2_FLOAT else "")
        + bullets([
            ("Uno por n&uacute;mero f:","tu mejor f/8, tu mejor f/4 y tu mejor f/2."),
            ("Ojos n&iacute;tidos:","los ojos deben estar enfocados. Descarta las selecciones borrosas o con los ojos entrecerrados."),
            ("Buena exposici&oacute;n:","guarda las que est&eacute;n equilibradas y favorecedoras."),
        ])
        + note("Llama a estas tus selecciones finales. Elige a prop&oacute;sito."))
    es+=deliverables_box(True,
        [("1 hoja de contactos:","una hoja de contactos de 6 con tus tres im&aacute;genes finales cargadas, como un JPG de alta resoluci&oacute;n."),
         ("3 fotos finales:","tus tres retratos pulidos exportados por separado como JPG de alta resoluci&oacute;n."),
         ("4 archivos en total:","la hoja de contactos de 6 m&aacute;s las tres im&aacute;genes finales en JPG.")])
    es+=card("EDICI&Oacute;N LIGERA / SOLO RECORTE","Deja Bien la C&aacute;mara, Luego Recorta",
        para("Esta es una captura en JPG, as&iacute; que dejaste bien tu exposici&oacute;n en la c&aacute;mara. La &uacute;nica edici&oacute;n que necesitas es un <strong>recorte</strong>: ordena el encuadre para que se vea como un retrato limpio.")
        + bullets([
            ("Recorta para el retrato:","de la cintura para arriba o m&aacute;s cerca, los ojos cerca del tercio superior, el sujeto descentrado si se ve mejor."),
            ("No edites de m&aacute;s:","sin color pesado ni filtros. La foto ya debe verse bien tal como sale de la c&aacute;mara."),
        ]))
    es+=card("&Aacute;RMALA / HOJA DE CONTACTOS + EXPORTES","Entrega una Hoja de 6 M&aacute;s Tres JPG",
        steps([
            ("Carga tus 3 finales:","en Lightroom Classic, selecciona tus tres retratos finales."),
            ("Arma la hoja de 6:","en el m&oacute;dulo Print, usa el ajuste de hoja de contactos de 6 con tus tres finales cargadas, e impr&iacute;mela como un JPG de alta resoluci&oacute;n."),
            ("Exporta los 3 JPG:","ve a File &rsaquo; Export y exporta tus tres retratos finales como JPG de alta resoluci&oacute;n a la carpeta de tu proyecto."),
            ("Sube 4 archivos:","entrega la hoja de contactos de 6 m&aacute;s los tres JPG finales."),
        ])
        + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n."))
    es+=next_up("SIGUIENTE &middot; PASO 04 - Reflexi&oacute;n","Cuenta qu&eacute; aprendiste sobre equilibrar tu exposici&oacute;n y qu&eacute; n&uacute;mero f te gust&oacute; m&aacute;s.")

    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S3}" class="silva-step-btn">Step 04 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S3}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
    return wrap_page("Step 3: Cull and Submit | Aperture Portrait | Photography 1A | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

# ================= STEP 04 =================
def step03():
    en=banner("Module 08 &bull; Step 04","Reflection","Tell what you learned about balancing your exposure.","#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
    en+=card("STEP 04 / REFLECT","Complete and Upload the Reflection",
        (float_right(S3_FLOAT,"A Pioneer Valley student typing the Aperture Portrait reflection in the Word document on an iMac in the lab","Type your answers right in the reflection document.") if HAVE_S3_FLOAT else "")
        + para("Finish with a short reflection. It asks how you balanced your exposure, what was hardest about it, and which aperture you liked best.")
        + note("The reflection document is on Step 01 (the Overview), the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + bullets([
            ("Balancing your exposure:","tell how you used the shutter to balance the light meter at each f-stop."),
            ("The hardest part:","what was the hardest part of balancing your exposure?"),
            ("Your favorite f-stop:","which did you like best, f/8, f/4, or f/2, and why?"),
        ])
        + note("Answer honestly, in your own words, in full sentences."))
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
    en+=next_up("MODULE COMPLETE","Great work. You explored aperture, directed a partner, and balanced your own exposure.")

    es=banner("M&oacute;dulo 08 &bull; Paso 04","Reflexi&oacute;n","Cuenta qu&eacute; aprendiste sobre equilibrar tu exposici&oacute;n.","#top","Back to English", HICON_REFLECT)
    es+=card("PASO 04 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        (float_right(S3_FLOAT,"Un estudiante de Pioneer Valley escribiendo la reflexi&oacute;n de Retrato de Apertura en el documento de Word en una iMac en el laboratorio","Escribe tus respuestas directamente en el documento de reflexi&oacute;n.") if HAVE_S3_FLOAT else "")
        + para("Termina con una reflexi&oacute;n corta. Te pregunta c&oacute;mo equilibraste tu exposici&oacute;n, qu&eacute; fue lo m&aacute;s dif&iacute;cil y qu&eacute; apertura te gust&oacute; m&aacute;s.")
        + note("El documento de reflexi&oacute;n est&aacute; en el Paso 01 (el Resumen), la primera pen la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;ginaaacute;gina. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + bullets([
            ("Equilibrar tu exposici&oacute;n:","cuenta c&oacute;mo usaste el obturador para equilibrar el expos&iacute;metro en cada n&uacute;mero f."),
            ("Lo m&aacute;s dif&iacute;cil:","&iquest;qu&eacute; fue lo m&aacute;s dif&iacute;cil de equilibrar tu exposici&oacute;n?"),
            ("Tu apertura favorita:","&iquest;cu&aacute;l te gust&oacute; m&aacute;s, f/8, f/4 o f/2, y por qu&eacute;?"),
        ])
        + note("Contesta con honestidad, en tus propias palabras, en oraciones completas."))
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completado, subido a esta tarea de Canvas.")])
    es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Exploraste la apertura, dirigiste a un compa&ntilde;ero y equilibraste tu propia exposici&oacute;n.")

    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 03</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 03</a><span></span></div>'
    return wrap_page("Step 4: Reflection | Aperture Portrait | Photography 1A | PVHS", nav("Step 04",dots_for(3),stepnav), top_wrap(en,es), bottom)

# ================= BUILD =================
for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03)]:
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
