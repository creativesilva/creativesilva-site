#!/usr/bin/env python3
# Photography 2A - Module 07: Aperture Portrait (partner photo walk, RAW + preset edit).
# Same aperture exercise as Photo 1A (f/8, f/4, f/2; Manual; ISO 100; balance with shutter), but
# students capture in RAW and do an EXTENSIVE edit: they run and refine the preset they built in
# Module 04 (Build Your Own Preset), or start a new one. A preset is not dialed in until it has been
# run across many sessions, so this is part of that refining. Overview + 3 steps, bilingual, 5th-grade.
# HEADER + step float images are PLACEHOLDERS. Camera-kit module: NO fresh-photos honesty note.
import os, re
from silva_framework import *

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"

IMGDIR=f"{SITE}/assets/images/photo2/aperture-portrait"
HEADER=f"{IMGDIR}/header-v1.jpg"
S1_FLOAT=f"{IMGDIR}/capture-float-v1.jpg"
S2_FLOAT=f"{IMGDIR}/edit-float-v1.jpg"
S3_FLOAT=f"{IMGDIR}/reflection-float-v1.jpg"
HAVE_HEADER=True       # header art placed; overview hero renders
HAVE_S1_FLOAT=False    # step 1 capture float (awaiting photo)
HAVE_S2_FLOAT=False    # step 2 edit float (awaiting photo)
HAVE_S3_FLOAT=True     # step 3 reflection float (placed)

CONTACT_ZIP=f"{SITE}/assets/PVHS_Contact_Sheet_Presets.zip"
REFLECT_EN=f"{SITE}/assets/course-documents/Aperture-Portrait-Photo2-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Aperture-Portrait-Photo2-Reflection-ES.docx"
EXPOSURE_FULL=f"{SITE}/assets/images/shared/exposure-basics-v1.jpg"     # exposure-basics poster (click to open full)
EXPOSURE_THUMB=f"{SITE}/assets/images/shared/exposure-basics-thumb-v1.jpg"
PRESET_MODULE="photo2-preset-overview.html"   # Module 04: Build Your Own Preset (the preset started earlier)

OVER="photo2-aperture-portrait-overview.html"
S1="photo2-aperture-portrait-step01-capture-contact.html"
S2="photo2-aperture-portrait-step02-edit-submit.html"
S3="photo2-aperture-portrait-step03-reflection.html"

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

def float_ph(label):
    return '<!--FLOAT-->'+placeholder(label, minh=300)+'<!--/FLOAT-->'
def hero_ph(label):
    return placeholder(label, minh=300)

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

DOTS_TITLES=[("M","Overview"),("1","Step 01"),("2","Step 02"),("3","Step 03")]
def dots_for(active_idx):
    hrefs=[OVER,S1,S2,S3]
    r=""
    for i,(lab,title) in enumerate(DOTS_TITLES):
        r+=dot("" if i==active_idx else hrefs[i], lab, title, i==active_idx, module=(i==0 and active_idx!=0))
    return r

def aperture_settings_section(es):
    red="#f90101"
    if es:
        title="Ajustes de C&aacute;mara"
        lead=("Trabaja en modo Manual (M). Mant&eacute;n tu ISO en 100 todo el tiempo. Debes capturar un buen retrato en las TRES aperturas: f/8, f/4 y f/2. "
              "Puedes empezar en f/8 o en f/2, pero pasa por las tres en orden. Cada vez que cambies la apertura, ajusta el obturador para equilibrar el expos&iacute;metro.")
        note_t=("Captura en <strong>RAW</strong> para tener el mayor detalle para editar. No es elegir una sola apertura: capturas las tres, en orden. Cuando est&eacute;s en f/8, hazla un paso m&aacute;s brillante (apunta a <strong>+1</strong> en el expos&iacute;metro). "
                "En f/4 y f/2, equilibra el expos&iacute;metro. Solo se mueven dos ajustes: la apertura (en orden) y el obturador (para equilibrar). El ISO se queda en 100.")
    else:
        title="Camera Settings"
        lead=("Work in Manual mode (M). Keep your ISO at 100 the whole time. You must capture a good portrait at ALL three apertures: f/8, f/4, and f/2. "
              "You can start at f/8 or at f/2, but go through all three in order. Every time you change the aperture, adjust the shutter to balance the light meter.")
        note_t=("Capture in <strong>RAW</strong> so you have the most detail to edit. This is not a free choice of one aperture: you capture all three, in order. When you are at f/8, make it one stop bright (aim for <strong>+1</strong> on the light meter). "
                "At f/4 and f/2, balance the meter. Only two settings move: the aperture (in order) and the shutter (to balance). ISO stays at 100.")
    lead_html=f'<div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{lead}</span></div>'
    note_box=(f'<div style="background:rgba(249,1,1,0.10);border:1px solid rgba(249,1,1,0.30);border-left:4px solid {red};padding:11px 14px;margin:0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.92);line-height:1.55;">{note_t}</div>')
    return (f'<div style="background:linear-gradient(180deg,rgba(249,1,1,0.06) 0%,rgba(249,1,1,0.02) 100%);border:1px solid rgba(249,1,1,0.26);border-left:6px solid {red};padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(CAMSET_ICON, title, "#f90101", "#ff8f8f")
      + f'<div class="silva-cfloat" style="float:right;width:50%;min-width:400px;margin:2px 0 16px 30px;">{capture_panel("RAW", "1/500", "F8", "100", "shutter")}</div>'
      + lead_html + note_box + '</div>')

def exposure_poster(es):
    # Purple RESOURCE: clickable Exposure Basics poster thumbnail; opens the full image in a new tab.
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
   "en_desc":"You use the class camera kit in Manual mode, capture in RAW, and control aperture, shutter, and ISO on purpose.",
   "es_desc":"Usas el kit de c&aacute;mara en modo Manual, capturas en RAW y controlas la apertura, el obturador y el ISO a prop&oacute;sito."},
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You use depth of field and background separation to make a strong portrait.",
   "es_desc":"Usas la profundidad de campo y la separaci&oacute;n del fondo para hacer un retrato fuerte."},
  {"code":"SA.17.6","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Digital Editing &amp; Workflow","es_title":"Edici&oacute;n Digital y Flujo de Trabajo",
   "en_desc":"You edit RAW files in Lightroom Classic and refine your own preset across a real session.",
   "es_desc":"Editas archivos RAW en Lightroom Classic y refinas tu propio preset en una sesi&oacute;n real."},
  {"code":"SA.17.8","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Documentation of Finished Work","es_title":"Documentaci&oacute;n del Trabajo Terminado",
   "en_desc":"You build contact sheets that present your take and your final edited selections clearly.",
   "es_desc":"Creas hojas de contactos que presentan tu trabajo y tus selecciones finales editadas con claridad."},
]

def preset_resource(es):
    if es:
        body=(para("En el M&oacute;dulo 04 construiste tu propio preset. Un preset no queda perfecto de una vez: se afina despu&eacute;s de correrlo en muchas sesiones. Esta sesi&oacute;n es parte de ese proceso: corre tu preset, ve qu&eacute; funciona y aj&uacute;stalo. Si no est&aacute; funcionando, puedes empezar un preset nuevo.")
          + '<div style="margin-top:6px;">'+reslink(PRESET_MODULE,"Ir a: Construye Tu Preset")+'</div>')
        return resources_card("Tu Preset (del M&oacute;dulo 04)", body, True)
    body=(para("In Module 04 you built your own preset. A preset is not perfect the first time: it gets dialed in after you run it across many sessions. This session is part of that: run your preset, see what works, and adjust it. If it is not working, you can start a fresh preset build.")
      + '<div style="margin-top:6px;">'+reslink(PRESET_MODULE,"Go to: Build Your Own Preset")+'</div>')
    return resources_card("Your Preset (from Module 04)", body, False)

# ================= OVERVIEW =================
def overview():
    en=banner("Photography 2A","Module 07: Aperture Portrait","Explore aperture on a partner photo walk, capture in RAW, then run and refine your preset.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
    en+=type_card("overview","The Module Overview","One Partner, Three Apertures, Your Preset",
        para("This is a partner photo walk about <strong>aperture</strong>. You and a partner take turns: one is the <strong>photographer</strong> and the other is the <strong>subject</strong> (the person being photographed). Then you switch, so each of you photographs and each of you gets photographed.")
        + para("You work in Manual mode with the Canon R50 and the RF 50mm f/1.8 lens. ISO stays at 100. You capture the same portrait at three apertures, <strong>f/8</strong>, <strong>f/4</strong>, and <strong>f/2</strong>, balancing the shutter each time. This time you capture in <strong>RAW</strong> and do a full edit: you run the preset you built in Module 04 and refine it for these portraits.")
        + (framed(HEADER,"Aperture Portrait module header") if HAVE_HEADER else hero_ph("HEADER IMAGE PLACEHOLDER &middot; Aperture Portrait overview hero (16:9). Swap in when ready.")))
    en+=standards_box(False, APERTURE_STANDARDS)
    en+=downloads_block(False)
    en+=card("THE CONCEPT / WHAT APERTURE DOES","Aperture and Depth of Field",
        para("Aperture is how wide the lens opens. It is written as an f-stop, like f/8 or f/2. Aperture changes two things at once: how much light comes in, and how much of your photo is in focus (this is called <strong>depth of field</strong>).")
        + bullets([
            ("f/8 (smaller opening):","more of the photo is sharp, from your subject to the background. A deeper focus."),
            ("f/2 (wider opening):","only your subject is sharp and the background goes soft and blurry. Your subject pops and separates from the background."),
            ("f/4 (in between):","a middle look, between the two."),
        ])
        + note("A wider aperture also lets in more light, so you change your shutter each time to keep the light balanced. Same photo, three apertures, three looks."))
    en+=preset_resource(False)
    en+=card("MAKE IT A PORTRAIT / NOT A FLAT PHOTO","Frame, Light, and Depth",
        para("A portrait is framed from the <strong>waist up, or closer</strong>. Turn the camera on its side so it is <strong>tall (portrait orientation)</strong>, not wide. Most people forget and leave the camera sideways, so check every time.")
        + bullets([
            ("Find soft light:","you are photographing in bright sun. Move into open shade so the light is soft and flattering, not harsh."),
            ("Step off the wall:","do not stand your partner right against a wall. Have them take a few steps forward. This is not a stiff ID photo, it is a portrait, so build depth and separate them from the background."),
            ("Fill the frame:","waist up or closer, with the eyes near the top third."),
        ]))
    en+=card("HOW IT WORKS / YOUR PLAN","Your Three Steps",
        steps([
            ("Capture &amp; Contact Sheet:","in Manual mode, capture your partner in RAW at f/8, f/4, and f/2 (then switch roles). Build and turn in a 12-Up contact sheet of your whole take."),
            ("Cull, Edit &amp; Submit:","pick your best three (one per f-stop), run and refine your preset, and turn in a 6-Up contact sheet plus your three polished portraits."),
            ("Reflection:","tell whether your preset held up this session, and what you changed."),
        ])
        + note("Capture in RAW so you have room to edit. Your preset is a starting point, not the finish line."))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Aperture","How wide the lens opens, written as an f-stop like f/8 or f/2."),
           ("Depth of Field","How much of the photo is in focus. Wide aperture = shallow (blurry background); small aperture = deep (more in focus)."),
           ("RAW","A high-quality photo file that keeps the most detail, so you have room to edit."),
           ("Preset","A saved set of edits you can apply to a photo in one click, then fine-tune."),
           ("White Balance","The setting that makes colors look warm, cool, or true to life. Shade can push colors cool."),
           ("Portrait Orientation","Holding the camera tall (on its side) so the photo is taller than it is wide.")]))
    en+=next_up("UP NEXT &middot; STEP 01 - Capture &amp; Contact Sheet","Set Manual mode, capture in RAW at f/8, f/4, and f/2, then build your 12-Up contact sheet.")

    es=banner("Fotograf&iacute;a 2A","M&oacute;dulo 07: Retrato de Apertura","Explora la apertura en una caminata en pareja, captura en RAW, y corre y refina tu preset.","#top","Back to English", HICON_PHOTO_WALK)
    es+=type_card("overview","El Resumen del M&oacute;dulo","Una Pareja, Tres Aperturas, Tu Preset",
        para("Esta es una caminata fotogr&aacute;fica en pareja sobre la <strong>apertura</strong>. T&uacute; y tu compa&ntilde;ero se turnan: uno es el <strong>fot&oacute;grafo</strong> y el otro es el <strong>sujeto</strong> (la persona fotografiada). Luego cambian, para que cada uno fotograf&iacute;e y cada uno sea fotografiado.")
        + para("Trabajas en modo Manual con la Canon R50 y el lente RF 50mm f/1.8. El ISO se queda en 100. Capturas el mismo retrato en tres aperturas, <strong>f/8</strong>, <strong>f/4</strong> y <strong>f/2</strong>, equilibrando el obturador cada vez. Esta vez capturas en <strong>RAW</strong> y haces una edici&oacute;n completa: corres el preset que construiste en el M&oacute;dulo 04 y lo refinas para estos retratos.")
        + (framed(HEADER,"Encabezado del m&oacute;dulo Retrato de Apertura") if HAVE_HEADER else hero_ph("IMAGEN DE ENCABEZADO (PLACEHOLDER) &middot; se cambia despu&eacute;s")))
    es+=standards_box(True, APERTURE_STANDARDS)
    es+=downloads_block(True)
    es+=card("EL CONCEPTO / QU&Eacute; HACE LA APERTURA","Apertura y Profundidad de Campo",
        para("La apertura es qu&eacute; tan abierto est&aacute; el lente. Se escribe como un n&uacute;mero f, como f/8 o f/2. Cambia dos cosas a la vez: cu&aacute;nta luz entra y cu&aacute;nto de tu foto est&aacute; enfocado (esto se llama <strong>profundidad de campo</strong>).")
        + bullets([
            ("f/8 (abertura m&aacute;s peque&ntilde;a):","m&aacute;s de la foto est&aacute; n&iacute;tida, desde tu sujeto hasta el fondo."),
            ("f/2 (abertura m&aacute;s amplia):","solo tu sujeto est&aacute; n&iacute;tido y el fondo se pone borroso. Tu sujeto resalta y se separa del fondo."),
            ("f/4 (en medio):","un look intermedio entre los dos."),
        ])
        + note("Una apertura m&aacute;s amplia deja entrar m&aacute;s luz, as&iacute; que cambias el obturador cada vez para mantener la luz equilibrada."))
    es+=preset_resource(True)
    es+=card("HAZLO UN RETRATO / NO UNA FOTO PLANA","Encuadre, Luz y Profundidad",
        para("Un retrato se encuadra de la <strong>cintura para arriba, o m&aacute;s cerca</strong>. Voltea la c&aacute;mara de lado para que quede <strong>vertical (orientaci&oacute;n de retrato)</strong>, no horizontal. Revisa cada vez.")
        + bullets([
            ("Busca luz suave:","mu&eacute;vete a una sombra abierta para que la luz sea suave y favorecedora, no dura."),
            ("Sep&aacute;rate de la pared:","que tu compa&ntilde;ero d&eacute; unos pasos hacia adelante. No es una foto de identificaci&oacute;n r&iacute;gida, es un retrato: crea profundidad y separaci&oacute;n."),
            ("Llena el cuadro:","de la cintura para arriba o m&aacute;s cerca, con los ojos cerca del tercio superior."),
        ]))
    es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Tres Pasos",
        steps([
            ("Captura y Hoja de Contactos:","en modo Manual, captura a tu compa&ntilde;ero en RAW en f/8, f/4 y f/2 (luego cambien de rol). Arma y entrega una hoja de contactos de 12 im&aacute;genes."),
            ("Selecciona, Edita y Entrega:","elige tus tres mejores (una por n&uacute;mero f), corre y refina tu preset, y entrega una hoja de 6 m&aacute;s tus tres retratos pulidos."),
            ("Reflexi&oacute;n:","cuenta si tu preset funcion&oacute; esta sesi&oacute;n y qu&eacute; cambiaste."),
        ])
        + note("Captura en RAW para tener espacio para editar. Tu preset es un punto de partida, no la meta final."))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Aperture (Apertura)","Qu&eacute; tan abierto est&aacute; el lente, escrito como un n&uacute;mero f, como f/8 o f/2."),
           ("Depth of Field (Profundidad de Campo)","Cu&aacute;nto de la foto est&aacute; enfocado. Apertura amplia = poca (fondo borroso); apertura peque&ntilde;a = mucha."),
           ("RAW","Un archivo de foto de alta calidad que guarda el mayor detalle, para tener espacio para editar."),
           ("Preset","Un conjunto guardado de ediciones que aplicas a una foto con un clic, y luego ajustas."),
           ("White Balance (Balance de Blancos)","El ajuste que hace que los colores se vean c&aacute;lidos, fr&iacute;os o reales. La sombra puede enfriar los colores."),
           ("Portrait Orientation (Orientaci&oacute;n de Retrato)","Sostener la c&aacute;mara vertical (de lado) para que la foto sea m&aacute;s alta que ancha.")]), True)
    es+=next_up("SIGUIENTE &middot; PASO 01 - Captura y Hoja de Contactos","Pon el modo Manual, captura en RAW en f/8, f/4 y f/2, y arma tu hoja de contactos de 12.")

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Aperture Portrait | Photography 2A | PVHS", nav("Overview",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ================= STEP 01 =================
def step01():
    en=banner("Module 07 &bull; Step 01","Capture &amp; Contact Sheet","Capture your partner in RAW at f/8, f/4, and f/2, then build a 12-Up contact sheet.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
    en+=type_card("photo-walk","Step 01 &middot; On the Photo Walk","Take Turns: Photographer and Subject",
        para("Head out with your partner and the camera kit. One of you is the <strong>photographer</strong> and the other is the <strong>subject</strong>. Photograph your full set, then trade roles so you both get portraits and you both practice the camera.")
        + (float_right(S1_FLOAT,"A Pioneer Valley student photographing a partner in open shade with the Canon R50 held in portrait orientation","Camera on its side, one elbow up: that is portrait orientation.") if HAVE_S1_FLOAT else float_ph("FLOAT-RIGHT PLACEHOLDER &middot; Step 1 capture photo. Swap in when ready."))
        + bullets([
            ("Hold it tall:","turn the camera on its side with one elbow up in the air for portrait (tall) orientation. Do not leave it wide."),
            ("Frame waist up or closer:","fill the frame with your partner, eyes near the top third."),
            ("Open shade:","move out of the harsh sun into soft, even shade."),
            ("Step off the wall:","have your partner take a few steps forward from the background for depth and separation."),
        ]))
    en+=deliverables_box(False,
        [("1 contact sheet:","a 12-Up contact sheet of your entire take, turned in as a high-resolution JPG.")])
    en+=aperture_settings_section(False)
    en+=exposure_poster(False)
    en+=card("YOUR THREE APERTURES / SET THE CAMERA","f/8, f/4, and f/2, in order",
        para("You must capture a good portrait at all three apertures, in order, in RAW. You can start at f/8 or at f/2, then work through all three. Keep ISO at 100 and balance the light with your shutter at each one.")
        + steps([
            ("Set Manual mode:","turn the Mode dial to <strong>M</strong>."),
            ("Set ISO 100:","press the <strong>ISO button</strong>, then turn the dial to 100."),
            ("Set your aperture:","press the <strong>up arrow (Up key)</strong>, then turn the <strong>Main Dial</strong> to your f-stop."),
            ("Balance with the shutter:","turn the <strong>Main Dial</strong> to set the shutter speed until the light meter is balanced."),
            ("f/8 first:","set f/8 and make it one stop bright (aim for +1). Capture a good portrait."),
            ("f/4 next:","set f/4, balance the shutter again, and capture."),
            ("f/2 last:","set f/2, balance the shutter again, and capture."),
        ], accent="#f90101")
        + note("Capturing in RAW gives you room to push white balance and tone when you run your preset in Step 02."))
    en+=card("BUILD IT / CONTACT SHEET","Turn In a 12-Up Contact Sheet",
        steps([
            ("Import your RAW files:","offload from the camera kit to OneDrive, then import into Lightroom Classic."),
            ("Use the 12-Up preset:","in the Print module, choose the 12-Up contact sheet preset."),
            ("Print to JPG:","use Print to File so it saves as a high-resolution JPG, then upload it here."),
        ])
        + note("Contact sheets are always turned in as a high-resolution JPG."))
    en+=next_up("UP NEXT &middot; STEP 02 - Cull, Edit &amp; Submit","Pick your best three, run and refine your preset, and turn in a 6-Up plus three polished portraits.")

    es=banner("M&oacute;dulo 07 &bull; Paso 01","Captura y Hoja de Contactos","Captura a tu compa&ntilde;ero en RAW en f/8, f/4 y f/2, y arma una hoja de contactos de 12.","#top","Back to English", HICON_PHOTO_WALK)
    es+=type_card("photo-walk","Paso 01 &middot; En la Caminata","Tomen Turnos: Fot&oacute;grafo y Sujeto",
        para("Salgan con tu compa&ntilde;ero y el kit de c&aacute;mara. Uno es el <strong>fot&oacute;grafo</strong> y el otro es el <strong>sujeto</strong>. Captura tu serie completa, luego cambien de rol.")
        + (float_right(S1_FLOAT,"Un estudiante de Pioneer Valley fotografiando a su compa&ntilde;ero en sombra abierta con la Canon R50 en orientaci&oacute;n vertical","C&aacute;mara de lado, un codo arriba: eso es orientaci&oacute;n de retrato.") if HAVE_S1_FLOAT else float_ph("PLACEHOLDER FLOTANTE &middot; foto del Paso 1"))
        + bullets([
            ("Sost&eacute;nla vertical:","voltea la c&aacute;mara de lado con un codo arriba para orientaci&oacute;n vertical. No la dejes horizontal."),
            ("Encuadra de la cintura para arriba:","llena el cuadro con tu compa&ntilde;ero, los ojos cerca del tercio superior."),
            ("Sombra abierta:","sal del sol fuerte a una sombra suave y pareja."),
            ("Sep&aacute;rate de la pared:","que tu compa&ntilde;ero d&eacute; unos pasos hacia adelante para crear profundidad y separaci&oacute;n."),
        ]))
    es+=deliverables_box(True,
        [("1 hoja de contactos:","una hoja de contactos de 12 im&aacute;genes de todo tu trabajo, entregada como un JPG de alta resoluci&oacute;n.")])
    es+=aperture_settings_section(True)
    es+=exposure_poster(True)
    es+=card("TUS TRES APERTURAS / AJUSTA LA C&Aacute;MARA","f/8, f/4 y f/2, en orden",
        para("Debes capturar un buen retrato en las tres aperturas, en orden, en RAW. Puedes empezar en f/8 o en f/2, luego pasa por las tres. Mant&eacute;n el ISO en 100 y equilibra la luz con tu obturador en cada una.")
        + steps([
            ("Pon el modo Manual:","gira el dial de modo a <strong>M</strong>."),
            ("Pon ISO 100:","presiona el <strong>bot&oacute;n ISO</strong>, luego gira el dial a 100."),
            ("Pon tu apertura:","presiona la <strong>flecha hacia arriba</strong>, luego gira el <strong>dial principal</strong> a tu n&uacute;mero f."),
            ("Equilibra con el obturador:","gira el <strong>dial principal</strong> para ajustar el obturador hasta que el expos&iacute;metro quede equilibrado."),
            ("f/8 primero:","pon f/8 y hazla un paso m&aacute;s brillante (apunta a +1). Captura un buen retrato."),
            ("f/4 despu&eacute;s:","pon f/4, equilibra el obturador otra vez y captura."),
            ("f/2 al final:","pon f/2, equilibra el obturador otra vez y captura."),
        ], accent="#f90101")
        + note("Capturar en RAW te da espacio para ajustar el balance de blancos y el tono cuando corras tu preset en el Paso 02."))
    es+=card("&Aacute;RMALA / HOJA DE CONTACTOS","Entrega una Hoja de Contactos de 12",
        steps([
            ("Importa tus archivos RAW:","descarga del kit de c&aacute;mara a OneDrive, luego importa a Lightroom Classic."),
            ("Usa el ajuste de 12:","en el m&oacute;dulo Print, elige el ajuste de hoja de contactos de 12."),
            ("Imprime a JPG:","usa Print to File para que se guarde como un JPG de alta resoluci&oacute;n, luego s&uacute;belo aqu&iacute;."),
        ])
        + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n."))
    es+=next_up("SIGUIENTE &middot; PASO 02 - Selecciona, Edita y Entrega","Elige tus tres mejores, corre y refina tu preset, y entrega una hoja de 6 m&aacute;s tres retratos pulidos.")

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a> <a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Capture and Contact Sheet | Aperture Portrait | Photography 2A | PVHS", nav("Step 01",dots_for(1),stepnav), top_wrap(en,es), bottom)

# ================= STEP 02 =================
def step02():
    en=banner("Module 07 &bull; Step 02","Cull, Edit &amp; Submit","Pick your best three, run and refine your preset, and turn in a 6-Up plus three polished portraits.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
    en+=type_card("edit","Step 02 &middot; Cull","Choose Your Three Best",
        para("Look through your take and choose your three strongest portraits: <strong>one at f/8, one at f/4, and one at f/2</strong>. Keeping one at each f-stop shows the range of the aperture and sets up your reflection.")
        + (float_right(S2_FLOAT,"A Pioneer Valley student editing a RAW portrait in Lightroom Classic on an iMac in the lab","Run your preset, then fine-tune it for these portraits.") if HAVE_S2_FLOAT else float_ph("FLOAT-RIGHT PLACEHOLDER &middot; Step 2 edit photo. Swap in when ready."))
        + bullets([
            ("One per f-stop:","your best f/8, your best f/4, and your best f/2."),
            ("Sharp eyes:","the eyes should be in focus. Skip any selections that are soft."),
            ("Good base exposure:","keep the ones you can edit into a strong, flattering portrait."),
        ])
        + note("Call these your final selections, not &ldquo;picks.&rdquo; Choose on purpose."))
    en+=deliverables_box(False,
        [("1 contact sheet:","a 6-Up contact sheet with your three final edited images loaded, as a high-resolution JPG."),
         ("3 final photos:","your three polished, edited portraits exported individually as high-resolution JPGs."),
         ("4 files total:","the 6-Up contact sheet plus the three polished JPGs.")])
    en+=card("EDIT / RUN AND REFINE YOUR PRESET","Make Your Preset Work Here",
        para("These are RAW files, so you have room to edit. Start from the preset you built in Module 04, then refine it for these portraits and this light.")
        + steps([
            ("Apply your preset:","in the Develop module, click your preset to apply it to a portrait."),
            ("Check the light:","open shade can push colors cool. Fix the <strong>white balance</strong> so skin looks natural."),
            ("Refine the look:","adjust exposure, contrast, highlights, shadows, and tone until the portrait looks its best."),
            ("Update or restart:","if the preset works, update it with your changes. If it fights you this session, it is fine to start a new preset build."),
            ("Match all three:","sync your look across your f/8, f/4, and f/2 portraits so they feel like a set."),
        ], accent="#8b5cf6")
        + note("A preset is not dialed in until you have run it across many sessions. This session is part of dialing it in."))
    en+=card("BUILD IT / CONTACT SHEET + EXPORTS","Turn In a 6-Up Plus Three JPGs",
        steps([
            ("Load your 3 edited finals:","in Lightroom Classic, select your three edited portraits."),
            ("Build the 6-Up:","in the Print module, use the 6-Up contact sheet preset with your three finals loaded, and print it to a high-resolution JPG."),
            ("Export the 3 JPGs:","go to File &rsaquo; Export and export your three polished portraits as high-resolution JPGs into your project folder."),
            ("Upload 4 files:","turn in the 6-Up contact sheet plus the three polished JPGs."),
        ])
        + note("Contact sheets are always turned in as a high-resolution JPG."))
    en+=next_up("UP NEXT &middot; STEP 03 - Reflection","Tell whether your preset held up this session and what you changed.")

    es=banner("M&oacute;dulo 07 &bull; Paso 02","Selecciona, Edita y Entrega","Elige tus tres mejores, corre y refina tu preset, y entrega una hoja de 6 m&aacute;s tres retratos pulidos.","#top","Back to English", HICON_PHOTO_WALK)
    es+=type_card("edit","Paso 02 &middot; Selecciona","Elige Tus Tres Mejores",
        para("Revisa tu trabajo y elige tus tres retratos m&aacute;s fuertes: <strong>uno en f/8, uno en f/4 y uno en f/2</strong>. Guardar uno en cada n&uacute;mero f muestra el rango de la apertura y prepara tu reflexi&oacute;n.")
        + (float_right(S2_FLOAT,"Un estudiante de Pioneer Valley editando un retrato RAW en Lightroom Classic en una iMac en el laboratorio","Corre tu preset, luego aj&uacute;stalo para estos retratos.") if HAVE_S2_FLOAT else float_ph("PLACEHOLDER FLOTANTE &middot; foto del Paso 2"))
        + bullets([
            ("Uno por n&uacute;mero f:","tu mejor f/8, tu mejor f/4 y tu mejor f/2."),
            ("Ojos n&iacute;tidos:","los ojos deben estar enfocados. Descarta las borrosas."),
            ("Buena base de exposici&oacute;n:","guarda las que puedas editar en un retrato fuerte y favorecedor."),
        ])
        + note("Llama a estas tus selecciones finales. Elige a prop&oacute;sito."))
    es+=deliverables_box(True,
        [("1 hoja de contactos:","una hoja de contactos de 6 con tus tres im&aacute;genes finales editadas cargadas, como un JPG de alta resoluci&oacute;n."),
         ("3 fotos finales:","tus tres retratos pulidos y editados exportados por separado como JPG de alta resoluci&oacute;n."),
         ("4 archivos en total:","la hoja de contactos de 6 m&aacute;s los tres JPG pulidos.")])
    es+=card("EDITA / CORRE Y REFINA TU PRESET","Haz Que Tu Preset Funcione Aqu&iacute;",
        para("Estos son archivos RAW, as&iacute; que tienes espacio para editar. Empieza con el preset que construiste en el M&oacute;dulo 04, luego aj&uacute;stalo para estos retratos y esta luz.")
        + steps([
            ("Aplica tu preset:","en el m&oacute;dulo Develop, haz clic en tu preset para aplicarlo a un retrato."),
            ("Revisa la luz:","la sombra abierta puede enfriar los colores. Corrige el <strong>balance de blancos</strong> para que la piel se vea natural."),
            ("Refina el look:","ajusta exposici&oacute;n, contraste, luces, sombras y tono hasta que el retrato se vea lo mejor posible."),
            ("Actualiza o reinicia:","si el preset funciona, actual&iacute;zalo con tus cambios. Si esta sesi&oacute;n te pelea, est&aacute; bien empezar un preset nuevo."),
            ("Iguala las tres:","sincroniza tu look en tus retratos de f/8, f/4 y f/2 para que se sientan como un conjunto."),
        ], accent="#8b5cf6")
        + note("Un preset no queda perfecto hasta que lo corres en muchas sesiones. Esta sesi&oacute;n es parte de afinarlo."))
    es+=card("&Aacute;RMALA / HOJA DE CONTACTOS + EXPORTES","Entrega una Hoja de 6 M&aacute;s Tres JPG",
        steps([
            ("Carga tus 3 finales editadas:","en Lightroom Classic, selecciona tus tres retratos editados."),
            ("Arma la hoja de 6:","en el m&oacute;dulo Print, usa el ajuste de hoja de contactos de 6 con tus tres finales cargadas, e impr&iacute;mela como un JPG de alta resoluci&oacute;n."),
            ("Exporta los 3 JPG:","ve a File &rsaquo; Export y exporta tus tres retratos pulidos como JPG de alta resoluci&oacute;n a la carpeta de tu proyecto."),
            ("Sube 4 archivos:","entrega la hoja de contactos de 6 m&aacute;s los tres JPG pulidos."),
        ])
        + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n."))
    es+=next_up("SIGUIENTE &middot; PASO 03 - Reflexi&oacute;n","Cuenta si tu preset funcion&oacute; esta sesi&oacute;n y qu&eacute; cambiaste.")

    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Cull, Edit and Submit | Aperture Portrait | Photography 2A | PVHS", nav("Step 02",dots_for(2),stepnav), top_wrap(en,es), bottom)

# ================= STEP 03 =================
def step03():
    en=banner("Module 07 &bull; Step 03","Reflection","Tell whether your preset held up this session and what you changed.","#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
    en+=card("STEP 03 / REFLECT","Complete and Upload the Reflection",
        (float_right(S3_FLOAT,"A Pioneer Valley student typing the Aperture Portrait reflection in the Word document on an iMac in the lab","Type your answers right in the reflection document.") if HAVE_S3_FLOAT else float_ph("FLOAT-RIGHT PLACEHOLDER &middot; Step 3 reflection photo. Swap in when ready."))
        + para("Finish with a short reflection about your preset and this session.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + bullets([
            ("Did your preset work?","did the preset you built earlier work for this session? Yes or no?"),
            ("If not, why?","if it did not work, why not? Was the lighting scenario too different from where you first built it?"),
            ("What you changed:","what did you refine, or did you start a new preset? What is better now?"),
            ("Your favorite f-stop:","which did you like best, f/8, f/4, or f/2, and why?"),
        ])
        + note("Answer honestly, in your own words, in full sentences."))
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
    en+=next_up("MODULE COMPLETE","Great work. You captured in RAW, explored aperture, and pushed your preset one session closer to dialed in.")

    es=banner("M&oacute;dulo 07 &bull; Paso 03","Reflexi&oacute;n","Cuenta si tu preset funcion&oacute; esta sesi&oacute;n y qu&eacute; cambiaste.","#top","Back to English", HICON_REFLECT)
    es+=card("PASO 03 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        (float_right(S3_FLOAT,"Un estudiante de Pioneer Valley escribiendo la reflexi&oacute;n de Retrato de Apertura en el documento de Word en una iMac en el laboratorio","Escribe tus respuestas directamente en el documento de reflexi&oacute;n.") if HAVE_S3_FLOAT else float_ph("PLACEHOLDER FLOTANTE &middot; foto del Paso 3"))
        + para("Termina con una reflexi&oacute;n corta sobre tu preset y esta sesi&oacute;n.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + bullets([
            ("&iquest;Funcion&oacute; tu preset?","&iquest;el preset que construiste antes funcion&oacute; para esta sesi&oacute;n? &iquest;S&iacute; o no?"),
            ("Si no, &iquest;por qu&eacute;?","si no funcion&oacute;, &iquest;por qu&eacute;? &iquest;La luz era muy diferente de donde lo construiste al principio?"),
            ("Qu&eacute; cambiaste:","&iquest;qu&eacute; refinaste, o empezaste un preset nuevo? &iquest;Qu&eacute; est&aacute; mejor ahora?"),
            ("Tu apertura favorita:","&iquest;cu&aacute;l te gust&oacute; m&aacute;s, f/8, f/4 o f/2, y por qu&eacute;?"),
        ])
        + note("Contesta con honestidad, en tus propias palabras, en oraciones completas."))
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completado, subido a esta tarea de Canvas.")])
    es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Capturaste en RAW, exploraste la apertura y acercaste tu preset una sesi&oacute;n m&aacute;s a estar afinado.")

    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page("Step 3: Reflection | Aperture Portrait | Photography 2A | PVHS", nav("Step 03",dots_for(3),stepnav), top_wrap(en,es), bottom)

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
