#!/usr/bin/env python3
# Monochromatic Photography: a campus black-and-white PHOTO WALK (Module 12). Built for BOTH courses from
# one builder, differing only in image counts (Chris, 2026-11-03):
#   Photography 1A: capture at least 12 frames, cull/edit/deliver 4 black-and-white JPGs.
#   Photography 2A: capture at least 24 frames, cull/edit/deliver 8 black-and-white JPGs (double).
# Flow (4 steps, Overview = Step 01): Step 01 Overview + download, Step 02 Capture & Contact Sheet,
# Step 03 Cull/Edit/Deliver, Step 04 Reflection. SOLO work (no groups). School Canon EOS R50 kits,
# RAW capture, Picture Style set to Monochrome so the viewfinder previews black and white while the RAW
# keeps full color (verified on cam.start.canon + Canon KB: for RAW the Picture Style changes only the
# camera's LCD rendering; Lightroom may show color first, then you finish it in black and white).
# Camera-kit module, so NO own-device fresh-photos note. Bilingual, 5th-grade, locked dark angular style.
# The companion deck ("Seeing in Black and White") lives in the staff Slide Decks accordion, not here.
# Every example image is GATED OFF until Chris supplies art (no live placeholders).
import os
from silva_framework import *

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"

IMGDIR=f"{SITE}/assets/images/shared/monochromatic-photography"
HEADER=f"{IMGDIR}/header-v1.png"      # 21:9 title graphic, transparent PNG (keeps its soft alpha edges)
CAP_FLOAT=f"{IMGDIR}/capture-float-v1.jpg"
EDIT_FLOAT=f"{IMGDIR}/edit-float-v1.jpg"
HAVE_HEADER=True
HAVE_CAP_FLOAT=True
HAVE_EDIT_FLOAT=False

COURSES=[
  {"prefix":"photo1","title":"Photography 1A","nf":4,"nc":12,
   "refl":"Monochromatic-Photography-Reflection",
   "zip":f"{SITE}/assets/course-documents/Monochromatic-Photography-Project-Folder-Photo1.zip"},
  {"prefix":"photo2","title":"Photography 2A","nf":8,"nc":24,
   "refl":"Monochromatic-Photography-Photo2-Reflection",
   "zip":f"{SITE}/assets/course-documents/Monochromatic-Photography-Project-Folder-Photo2.zip"},
]

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

MONO_STANDARDS=[
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You use tonal value, contrast, line, and shape to build a strong black-and-white photo.",
   "es_desc":"Usas el valor tonal, el contraste, la l&iacute;nea y la forma para crear una foto fuerte en blanco y negro."},
  {"code":"SA.17.2","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Observation &amp; Seeing","es_title":"Observaci&oacute;n y Mirada",
   "en_desc":"You find strong compositions in ordinary campus subjects by seeing light and shadow, not color.",
   "es_desc":"Encuentras composiciones fuertes en temas comunes de la escuela al ver la luz y la sombra, no el color."},
  {"code":"SA.17.5","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Equipment &amp; Image Production","es_title":"Equipo y Producci&oacute;n de Imagen",
   "en_desc":"You set the camera to a Monochrome preview, capture in RAW, and expose for a full range of tones.",
   "es_desc":"Pones la c&aacute;mara en vista Monocromo, capturas en RAW y expones para un rango completo de tonos."},
  {"code":"SA.17.6","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Digital Editing &amp; Workflow","es_title":"Edici&oacute;n Digital y Flujo de Trabajo",
   "en_desc":"You import RAW files, build a contact sheet, edit in black and white in Lightroom Classic, and export clean JPGs.",
   "es_desc":"Importas archivos RAW, armas una hoja de contactos, editas en blanco y negro en Lightroom Classic y exportas JPG limpios."},
]

def mono_settings(es):
    # LOCKED camera-settings template (silva_framework.camera_settings_section): title spans the page,
    # the exposure grid (Shutter / Aperture / ISO / Light Meter / Image Quality) floats right, and
    # students balance the meter in MANUAL mode (Chris: we always capture manual). Recommended STARTING
    # values only; students fine-tune for the best exposure. The module's signature Monochrome Picture
    # Style + the RAW/JPG format + the Lightroom-shows-color note go in the `extra` block below the grid.
    if es:
        note=("Pon tu c&aacute;mara en <strong>Manual (M)</strong>. Estos son un <strong>punto de partida</strong>: "
              "deja la apertura y el ISO, y cambia la velocidad del obturador para equilibrar el expos&iacute;metro "
              "(m&aacute;s r&aacute;pida si est&aacute; muy brillante, m&aacute;s lenta si est&aacute; muy oscuro). "
              "Tambi&eacute;n puedes ajustar el ISO si te quedas sin rango.")
        extra=(para("<strong>Estilo de Imagen: Monocromo.</strong> En el men&uacute; de la c&aacute;mara, elige Picture Style y ponlo en <strong>Monocromo (Monochrome)</strong>, para que el visor se vea en blanco y negro mientras capturas.")
             + para("Captura en <strong>RAW</strong> para guardar el mayor detalle, o en <strong>JPG</strong> para una foto en blanco y negro directa de la c&aacute;mara. Tu maestro te dir&aacute; cu&aacute;l usar. En Lightroom tu RAW puede verse en color al principio: es normal, y terminas el blanco y negro al editar."))
        activity="esta caminata en blanco y negro"
    else:
        note=("Set your camera to <strong>Manual (M)</strong>. These are a <strong>starting point</strong>: "
              "keep the aperture and ISO, and change the shutter speed to balance the light meter "
              "(faster if it is too bright, slower if it is too dark). You can adjust the ISO too if you run out of room.")
        extra=(para("<strong>Picture Style: Monochrome.</strong> In the camera menu, choose Picture Style and set it to <strong>Monochrome</strong>, so your viewfinder previews in black and white while you capture.")
             + para("Capture in <strong>RAW</strong> to keep the most detail, or <strong>JPG</strong> for a black-and-white photo straight from the camera. Your teacher will tell you which to use. In Lightroom your RAW may show in color at first: that is normal, and you finish the black and white when you edit."))
        activity="this black-and-white photo walk"
    return camera_settings_section(es, quality="RAW", shutter="1/250", aperture="F8", iso="200",
                                   change_field="shutter", activity=activity, note=note, extra=extra)

def walk_safety(es):
    if es:
        return card("EN LA CAMINATA / SEGURIDAD Y RESPETO","Mant&eacute;n la Caminata Segura y Amable",
            bullets([
                ("Qu&eacute;date en las zonas permitidas:","tu maestro te dice a d&oacute;nde puedes ir. No salgas de esas zonas."),
                ("Fotos de lugares, no de personas:","este m&oacute;dulo es de lugares, superficies, luz y formas. No fotograf&iacute;es a tus compa&ntilde;eros ni a quien no quiera salir."),
                ("No molestes a las clases:","no entres a salones ni a espacios donde hay clase. Mant&eacute;n silencio cerca de las clases."),
                ("Cuida la vida y las cosas:","no molestes a los animales, no te subas a nada y no entres a zonas cerradas o peligrosas."),
                ("Mira por d&oacute;nde caminas:","trae la correa de la c&aacute;mara puesta y fíjate en escalones y bordes."),
            ]))
    return card("ON THE WALK / SAFETY &amp; RESPECT","Keep the Walk Safe and Kind",
        bullets([
            ("Stay in allowed areas:","your teacher tells you where you can go. Do not leave those areas."),
            ("Places, not people:","this module is about places, surfaces, light, and shapes. Do not photograph your classmates or anyone who does not want to be in a photo."),
            ("Do not disturb classes:","do not enter classrooms or spaces where a class is in session. Keep quiet near classes."),
            ("Care for life and property:","do not disturb animals, do not climb on anything, and do not enter closed or unsafe areas."),
            ("Watch where you walk:","keep your camera strap on and watch for steps and edges."),
        ]))

def build_course(c):
    prefix=c["prefix"]; CT=c["title"]; ZIP=c["zip"]; NF=c["nf"]; NC=c["nc"]; REFL=c["refl"]
    OVER=f"{prefix}-monochromatic-photography-overview.html"
    S1=f"{prefix}-monochromatic-photography-step01-capture-contact.html"
    S2=f"{prefix}-monochromatic-photography-step02-cull-edit-deliver.html"
    S3=f"{prefix}-monochromatic-photography-step03-reflection.html"

    def nav(current,dots,stepnav):
        return ('      <div class="silva-breadcrumb">\n'
                '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
                '        <span class="bc-sep">&rsaquo;</span>\n'
                f'        <a href="{OVER}" class="bc-hide-sm">Monochromatic Photography</a>\n'
                '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
                f'        <span class="bc-current">{current}</span>\n'
                '      </div>\n'
                '      <div class="silva-nav-spacer"></div>\n'
                f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
                f'      <div class="silva-step-nav">{stepnav}</div>')
    DT=[("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04")]
    def dots_for(active):
        hrefs=[OVER,S1,S2,S3]; r=""
        for i,(lab,title) in enumerate(DT):
            r+=dot("" if i==active else hrefs[i], lab, title, i==active, module=False)
        return r

    def project_downloads(es):
        if es:
            heading="Descarga Tu Carpeta del Proyecto"
            lead=("Descarga tu carpeta del proyecto. Es un archivo .zip. Al abrirlo tendr&aacute;s la carpeta "
                  "<strong>Monochromatic_Photography</strong>, y adentro hay una carpeta <strong>RAW_Images</strong> "
                  "para tus fotos RAW y tu documento de reflexi&oacute;n (en ingl&eacute;s y en espa&ntilde;ol).")
            label="Carpeta del Proyecto (.zip)"
            note_t=("<strong style=\"color:#ffb27c;\">Mantente organizado:</strong> cuando el .zip termine de descargarse, "
                    "&aacute;brelo y mueve la carpeta <strong>Monochromatic_Photography</strong> a "
                    f"OneDrive &rarr; {AREA}. Guarda tus fotos RAW dentro de <strong>RAW_Images</strong>.")
        else:
            heading="Download Your Project Folder"
            lead=("Download your project folder. It is a .zip file. When you open it you get the "
                  "<strong>Monochromatic_Photography</strong> folder, and inside it is a <strong>RAW_Images</strong> "
                  "folder for your RAW photos and your reflection document (English and Spanish).")
            label="Project Folder (.zip)"
            note_t=("<strong style=\"color:#ffb27c;\">Stay organized:</strong> when the .zip finishes downloading, "
                    "open it and move the <strong>Monochromatic_Photography</strong> folder into "
                    f"OneDrive &rarr; {AREA}. Keep your RAW photos inside <strong>RAW_Images</strong>.")
        return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
          + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
          + para(lead)
          + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
          + dl_link(ZIP, label, row=True)
          + '</div>'
          + f'<div style="margin-top:16px;font-size:12pt;color:rgba(255,255,255,0.82);line-height:1.55;">{note_t}</div>'
          + '</div>')

    def look_for_card(es):
        if es:
            return card("EN LA CAMINATA / QU&Eacute; BUSCAR","Cinco Formas de Ver en Blanco y Negro",
                para("Sin color, lo que manda es la luz, la sombra, el tono, la l&iacute;nea, la forma y la textura. Busca estas cinco cosas en la escuela.")
                + bullets([
                    ("Luz y sombra:","luz del sol de lado, sombras marcadas, mucho contraste. B&uacute;scalas en paredes, escaleras, barandales y sombras sobre los edificios."),
                    ("L&iacute;neas y formas:","l&iacute;neas gu&iacute;a, simetr&iacute;a, diagonales, ventanas o rejas repetidas. B&uacute;scalas en pasillos, andadores y fachadas."),
                    ("Textura:","acerca la c&aacute;mara a la corteza de un &aacute;rbol, el concreto, la grava o las hojas."),
                    ("Espacio negativo:","un solo tema contra un fondo simple: una rama, una pared vac&iacute;a o una sola sombra."),
                    ("Rango tonal:","separa los negros, los grises y los blancos para que tu tema resalte."),
                ], accent="#00b8b8"))
        return card("ON THE WALK / WHAT TO LOOK FOR","Five Ways to See in Black and White",
            para("Without color, what matters is light, shadow, tone, line, shape, and texture. Look for these five things on campus.")
            + bullets([
                ("Light and shadow:","side sunlight, hard cast shadows, strong contrast. Look on walls, stairs, railings, and shadows across buildings."),
                ("Lines and shapes:","leading lines, symmetry, diagonals, repeated windows or fences. Look in corridors, walkways, and building fronts."),
                ("Texture:","move in close on tree bark, concrete, gravel, or leaves."),
                ("Negative space:","one subject against a simple background: a single branch, an empty wall, or one shadow."),
                ("Tonal range:","separate the blacks, grays, and whites so your subject stands out."),
            ], accent="#00b8b8"))

    def masters_card(es):
        if es:
            return resources_card("Aprende de los Maestros",
                para("Estos fot&oacute;grafos hicieron un gran trabajo en blanco y negro. Fíjate en lo que buscaban y encu&eacute;ntralo en la escuela.")
                + bullets([
                    ("Ansel Adams:","rango tonal profundo y texturas naturales. Ll&eacute;valo a los &aacute;rboles, la corteza y la separaci&oacute;n de luz y sombra."),
                    ("Fan Ho:","geometr&iacute;a y sombras largas. Ll&eacute;valo a las paredes, los pasillos y la luz del sol de lado."),
                    ("Aaron Siskind:","superficies abstractas y encuadres cerrados. Ll&eacute;valo al concreto, las grietas y las rejas."),
                    ("Michael Kenna:","im&aacute;genes m&iacute;nimas y tranquilas con espacio negativo. Ll&eacute;valo a un &aacute;rbol solo y a fondos simples."),
                ], accent="#8b5cf6"), True)
        return resources_card("Learn from the Masters",
            para("These photographers did great black-and-white work. Notice what they looked for, then find it on campus.")
            + bullets([
                ("Ansel Adams:","deep tonal range and natural textures. Take it to campus trees, bark, and the split of light and shadow."),
                ("Fan Ho:","geometry and long shadows. Take it to walls, corridors, and side sunlight."),
                ("Aaron Siskind:","abstract surfaces and close framing. Take it to concrete, cracks, and fences."),
                ("Michael Kenna:","quiet, minimal images with negative space. Take it to a single tree and simple backgrounds."),
            ], accent="#8b5cf6"), False)

    def vocab_block(es):
        if es:
            return resources_card("Palabras Clave",
                vocab_grid("En el Examen",
                  "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
                  [("Tonal Value (Valor Tonal)","Qu&eacute; tan claro u oscuro es algo, del negro al blanco pasando por los grises."),
                   ("Contrast (Contraste)","La diferencia entre las partes claras y las oscuras de una foto. Mucho contraste es fuerte; poco es suave."),
                   ("Negative Space (Espacio Negativo)","El &aacute;rea vac&iacute;a o simple alrededor de tu tema. Ayuda a que el tema resalte."),
                   ("Texture (Textura)","C&oacute;mo se ver&iacute;a o se sentir&iacute;a una superficie: &aacute;spera, lisa, agrietada o rugosa."),
                   ("Leading Lines (L&iacute;neas Gu&iacute;a)","L&iacute;neas en la foto que llevan tus ojos hacia el tema, como un pasillo o un barandal."),
                   ("Silhouette (Silueta)","La forma oscura de un tema contra un fondo m&aacute;s claro, sin detalle adentro.")]), True)
        return resources_card("Key Words",
            vocab_grid("On the Quiz",
              "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
              [("Tonal Value","How light or dark something is, from black to white through the grays."),
               ("Contrast","The difference between the light parts and the dark parts of a photo. High contrast is bold; low is soft."),
               ("Negative Space","The empty or simple area around your subject. It helps the subject stand out."),
               ("Texture","How a surface would look or feel: rough, smooth, cracked, or bumpy."),
               ("Leading Lines","Lines in the photo that lead your eyes to the subject, like a hallway or a railing."),
               ("Silhouette","The dark shape of a subject against a lighter background, with no detail inside.")]))

    # ---------- STEP 01: OVERVIEW ----------
    def overview():
        sub_en="See the campus in black and white. Walk, capture, edit, and deliver your best monochrome photos."
        sub_es="Mira la escuela en blanco y negro. Camina, captura, edita y entrega tus mejores fotos monocromas."
        en=banner("Module 12 &bull; Step 01","Monochromatic Photography: Start Here", sub_en,"#espanol","Clic para Espa&ntilde;ol")
        en+=type_card("overview","Step 01 &middot; Overview &amp; Download","See a Different Way, Then Capture It",
            para("Today you look at our campus in <strong>black and white</strong>. The goal is not to find something beautiful. It is to make an ordinary subject strong through composition.")
            + para("Do not look for interesting things to photograph. Look for interesting ways to photograph ordinary things. A wall, a shadow, a tree, or a staircase can become powerful when you stop using color and start seeing light.")
            + (framed(HEADER,"A student on campus capturing black-and-white photos with a camera, the PV Academy of Arts building and a dove behind them") if HAVE_HEADER else ""))
        en+=standards_box(False, MONO_STANDARDS)
        en+=project_downloads(False)
        en+=card("THE BIG IDEA / HOW TO SEE","Monochrome Is a Way of Seeing",
            para("Black and white is not just removing color. It is a different way of seeing. When the color is gone, you start to notice <strong>light, shadow, tonal value, line, shape, texture, and negative space</strong>.")
            + bullets([
                ("Look for light:","where does the light come from, and what shadows does it make?"),
                ("Look for shape and line:","what lines, edges, and simple shapes hold the photo together?"),
                ("Look for tone:","where are the darkest darks, the brightest brights, and the grays between?"),
            ])
            + note("The challenge is to make an ordinary subject visually powerful through composition, not color."))
        en+=look_for_card(False)
        en+=masters_card(False)
        en+=card("HOW IT WORKS / YOUR PLAN","Your Next Three Steps",
            para("You are on Step 01 now: read this page and download your project folder above. Here are the three steps that follow.")
            + bullets([
                ("Step 02 &middot; Capture &amp; Contact Sheet:",f"set your camera to a Monochrome preview and RAW, then walk the campus and capture at least {NC} deliberate photos. Import them and build a contact sheet of your full take."),
                ("Step 03 &middot; Cull, Edit &amp; Deliver:",f"choose your best {NF} photos, finish them in black and white in Lightroom, and export your {NF} JPGs."),
                ("Step 04 &middot; Reflection:","tell what you looked for, how black and white changed what you saw, and which photo is your best."),
            ])
            + note("Slow down. Look first, then capture. One strong photo beats ten quick ones."))
        en+=vocab_block(False)
        en+=next_up("UP NEXT &middot; STEP 02 - Capture &amp; Contact Sheet","Set the Monochrome preview, walk the campus, capture your take, and build a contact sheet.")

        es=banner("M&oacute;dulo 12 &bull; Paso 01","Fotograf&iacute;a Monocrom&aacute;tica: Empieza Aqu&iacute;", sub_es,"#top","Back to English")
        es+=type_card("overview","Paso 01 &middot; Resumen y Descarga","Mira de Otra Forma, Luego Captura",
            para("Hoy miras nuestra escuela en <strong>blanco y negro</strong>. La meta no es encontrar algo bonito. Es hacer que un tema com&uacute;n sea fuerte por su composici&oacute;n.")
            + para("No busques cosas interesantes para fotografiar. Busca formas interesantes de fotografiar cosas comunes. Una pared, una sombra, un &aacute;rbol o una escalera pueden volverse poderosos cuando dejas el color y empiezas a ver la luz.")
            + (framed(HEADER,"Un estudiante en la escuela capturando fotos en blanco y negro con una c&aacute;mara, con el edificio PV Academy of Arts y una paloma detr&aacute;s") if HAVE_HEADER else ""))
        es+=standards_box(True, MONO_STANDARDS)
        es+=project_downloads(True)
        es+=card("LA GRAN IDEA / C&Oacute;MO VER","El Monocromo Es una Forma de Ver",
            para("El blanco y negro no es solo quitar el color. Es una forma distinta de ver. Cuando el color se va, empiezas a notar la <strong>luz, la sombra, el valor tonal, la l&iacute;nea, la forma, la textura y el espacio negativo</strong>.")
            + bullets([
                ("Busca la luz:","&iquest;de d&oacute;nde viene la luz y qu&eacute; sombras hace?"),
                ("Busca forma y l&iacute;nea:","&iquest;qu&eacute; l&iacute;neas, bordes y formas simples sostienen la foto?"),
                ("Busca el tono:","&iquest;d&oacute;nde est&aacute;n los m&aacute;s oscuros, los m&aacute;s claros y los grises de en medio?"),
            ])
            + note("El reto es hacer que un tema com&uacute;n sea visualmente poderoso por la composici&oacute;n, no por el color."))
        es+=look_for_card(True)
        es+=masters_card(True)
        es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Siguientes Tres Pasos",
            para("Est&aacute;s en el Paso 01: lee esta p&aacute;gina y descarga tu carpeta del proyecto arriba. Estos son los tres pasos que siguen.")
            + bullets([
                ("Paso 02 &middot; Captura y Hoja de Contactos:",f"pon tu c&aacute;mara en vista Monocromo y RAW, luego camina por la escuela y captura al menos {NC} fotos pensadas. Imp&oacute;rtalas y arma una hoja de contactos de todo tu trabajo."),
                ("Paso 03 &middot; Selecciona, Edita y Entrega:",f"elige tus mejores {NF} fotos, term&iacute;nalas en blanco y negro en Lightroom y exporta tus {NF} JPG."),
                ("Paso 04 &middot; Reflexi&oacute;n:","cuenta qu&eacute; buscaste, c&oacute;mo el blanco y negro cambi&oacute; lo que ve&iacute;as y cu&aacute;l foto es tu mejor."),
            ])
            + note("Ve despacio. Mira primero, luego captura. Una foto fuerte vale m&aacute;s que diez r&aacute;pidas."))
        es+=vocab_block(True)
        es+=next_up("SIGUIENTE &middot; PASO 02 - Captura y Hoja de Contactos","Pon la vista Monocromo, camina por la escuela, captura tu trabajo y arma una hoja de contactos.")

        stepnav=f'<a href="{S1}" class="silva-step-btn">Step 02 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
        return wrap_page(f"Monochromatic Photography | {CT} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

    # ---------- STEP 02: CAPTURE & CONTACT SHEET ----------
    def capture_contact():
        en=banner("Module 12 &bull; Step 02","Capture &amp; Contact Sheet",
            "Set the Monochrome preview, walk the campus, capture your take, and build a contact sheet.","#espanol","Clic para Espa&ntilde;ol")
        en+=card("ON THE WALK / WHAT YOU DO","Walk, Look, and Capture on Purpose",
            para(f"Set your camera to a Monochrome preview and RAW, then walk the campus. Look for light, shadow, lines, texture, and simple shapes. Capture at least <strong>{NC} photos</strong> on purpose, not random photos.")
            + (float_right(CAP_FLOAT,"A black-and-white photo of a dove resting on a concrete campus ledge, side light showing the feather texture","An ordinary campus subject made strong: feather texture, a clear tonal range, and a simple background.") if HAVE_CAP_FLOAT else "")
            + bullets([
                ("Look first:","before each photo, ask: what is my subject, and what makes it strong without color?"),
                ("Try more than one view:","move closer, change your height, and simplify the background. Make more than one view of the same subject and compare them."),
                (f"Capture at least {NC}:",f"you need a full take to choose from. You will cull it down to your best {NF} in the next step."),
            ]))
        en+=deliverables_box(False,
            [("Contact sheet (JPG):","1 contact sheet of your full take, built in Lightroom Classic and turned in as a high-resolution JPG.")])
        en+=mono_settings(False)
        en+=walk_safety(False)
        en+=card("BACK INSIDE / BUILD YOUR CONTACT SHEET","Import, Then Make Your Contact Sheet",
            steps([
                ("Import to Lightroom:","move your RAW files into your RAW_Images folder and import them into Lightroom Classic on the Mac."),
                ("See it in black and white:","your RAW may show in color at first. That is normal. You will finish the black and white in the next step."),
                ("Build the contact sheet:","in the Print module, use the contact-sheet template with your full take loaded."),
                ("Print to JPG:","use Print to File so it saves as a high-resolution JPG, then upload it here."),
            ])
            + note("Contact sheets are always turned in as a high-resolution JPG."))
        en+=next_up("UP NEXT &middot; STEP 03 - Cull, Edit &amp; Deliver",f"Choose your best {NF} photos, finish them in black and white, and export your {NF} JPGs.")

        es=banner("M&oacute;dulo 12 &bull; Paso 02","Captura y Hoja de Contactos",
            "Pon la vista Monocromo, camina por la escuela, captura tu trabajo y arma una hoja de contactos.","#top","Back to English")
        es+=card("EN LA CAMINATA / QU&Eacute; HACES","Camina, Mira y Captura con Intenci&oacute;n",
            para(f"Pon tu c&aacute;mara en vista Monocromo y RAW, luego camina por la escuela. Busca luz, sombra, l&iacute;neas, textura y formas simples. Captura al menos <strong>{NC} fotos</strong> pensadas, no fotos al azar.")
            + (float_right(CAP_FLOAT,"Una foto en blanco y negro de una paloma sobre una repisa de concreto en la escuela, con luz de lado que muestra la textura de las plumas","Un tema com&uacute;n de la escuela hecho fuerte: la textura de las plumas, un buen rango tonal y un fondo simple.") if HAVE_CAP_FLOAT else "")
            + bullets([
                ("Mira primero:","antes de cada foto, preg&uacute;ntate: &iquest;cu&aacute;l es mi tema y qu&eacute; lo hace fuerte sin color?"),
                ("Prueba m&aacute;s de una vista:","ac&eacute;rcate, cambia tu altura y simplifica el fondo. Haz m&aacute;s de una vista del mismo tema y compara."),
                (f"Captura al menos {NC}:",f"necesitas un buen conjunto para elegir. Lo reducir&aacute;s a tus mejores {NF} en el siguiente paso."),
            ]))
        es+=deliverables_box(True,
            [("Hoja de contactos (JPG):","1 hoja de contactos de todo tu trabajo, armada en Lightroom Classic y entregada como un JPG de alta resoluci&oacute;n.")])
        es+=mono_settings(True)
        es+=walk_safety(True)
        es+=card("DE REGRESO / ARMA TU HOJA DE CONTACTOS","Importa, Luego Arma Tu Hoja de Contactos",
            steps([
                ("Importa a Lightroom:","mueve tus archivos RAW a tu carpeta RAW_Images e imp&oacute;rtalos a Lightroom Classic en la Mac."),
                ("Ve en blanco y negro:","tu RAW puede verse en color al principio. Es normal. Terminar&aacute;s el blanco y negro en el siguiente paso."),
                ("Arma la hoja de contactos:","en el m&oacute;dulo Print, usa la plantilla de hoja de contactos con todo tu trabajo cargado."),
                ("Imprime a JPG:","usa Print to File para que se guarde como un JPG de alta resoluci&oacute;n, luego s&uacute;belo aqu&iacute;."),
            ])
            + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n."))
        es+=next_up("SIGUIENTE &middot; PASO 03 - Selecciona, Edita y Entrega",f"Elige tus mejores {NF} fotos, term&iacute;nalas en blanco y negro y exporta tus {NF} JPG.")

        stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S2}" class="silva-step-btn">Step 03 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S2}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
        return wrap_page(f"Step 2: Capture and Contact Sheet | Monochromatic Photography | {CT} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

    # ---------- STEP 03: CULL, EDIT & DELIVER ----------
    def cull_deliver():
        en=banner("Module 12 &bull; Step 03","Cull, Edit &amp; Deliver",
            f"Choose your best {NF} photos, finish them in black and white, and export your {NF} JPGs.","#espanol","Clic para Espa&ntilde;ol")
        en+=card("CULL / CHOOSE YOUR BEST","Pick Your Strongest Photos",
            para(f"Open your take in Lightroom Classic. Go through your full take and choose your best <strong>{NF} photos</strong>, the ones that are strong in black and white.")
            + (float_right(EDIT_FLOAT,"A before-and-after of one campus photo: a flat color RAW on the left, a finished high-contrast black-and-white edit on the right","Before and after: a flat color RAW, then a finished black-and-white edit with a full tonal range.") if HAVE_EDIT_FLOAT else "")
            + bullets([
                ("Strong tones:","keep the photos with a full range: real blacks, clean whites, and grays between."),
                ("Clear subject:","keep the photos where the subject stands out, helped by light, line, or negative space."),
                ("Sharp where it counts:","keep the sharp frames. Skip the soft ones."),
            ])
            + note(f"Call these your selections, not &ldquo;picks.&rdquo; You end with {NF}: your strongest black-and-white photos."))
        en+=deliverables_box(False,
            [(f"Your {NF} edited photos (JPGs):",f"your best {NF} photos from the walk, finished in black and white and exported as full-resolution JPGs, uploaded to this Canvas assignment.")])
        en+=card("EDIT / FINISH IN BLACK AND WHITE","Make Each Photo Its Best",
            para("These are RAW files, so you have room to edit. Finish each photo in black and white on the Mac in Lightroom Classic.")
            + steps([
                ("Set it to black and white:","in the Develop module, set the photo to a black-and-white profile or treatment."),
                ("Set your black and white points:","set the darkest part to a true black and the brightest to a clean white for a full tonal range."),
                ("Shape the contrast:","adjust contrast, highlights, and shadows so the photo has depth. Keep detail in the darks and brights."),
                ("Guide the eye:","dodge (lighten) and burn (darken) small areas to lead the eye to your subject."),
            ])
            + note("Not every black-and-white photo needs maximum contrast. Soft midtones can carry a quiet photo. You decide."))
        en+=card("DELIVER / NAME AND UPLOAD",f"Export Your {NF} JPGs",
            steps([
                ("Export full-resolution JPGs:",f"go to File &rsaquo; Export and export your {NF} edited photos as full-resolution JPGs into your project folder."),
                ("Name each file:","use your last name and first name plus the photo number, like <strong>Lee_Mia_Mono1.jpg</strong>."),
                ("Upload here:",f"turn in your {NF} edited black-and-white JPGs to this Canvas assignment."),
            ]))
        en+=next_up("UP NEXT &middot; STEP 04 - Reflection","Tell what you looked for, how black and white changed what you saw, and which photo is your best.")

        es=banner("M&oacute;dulo 12 &bull; Paso 03","Selecciona, Edita y Entrega",
            f"Elige tus mejores {NF} fotos, term&iacute;nalas en blanco y negro y exporta tus {NF} JPG.","#top","Back to English")
        es+=card("SELECCIONA / ELIGE LAS MEJORES","Elige Tus Fotos M&aacute;s Fuertes",
            para(f"Abre tu trabajo en Lightroom Classic. Revisa todo tu trabajo y elige tus mejores <strong>{NF} fotos</strong>, las que son fuertes en blanco y negro.")
            + (float_right(EDIT_FLOAT,"Un antes y despu&eacute;s de una foto de la escuela: un RAW plano a color a la izquierda, una edici&oacute;n terminada en blanco y negro con mucho contraste a la derecha","Antes y despu&eacute;s: un RAW plano a color, luego una edici&oacute;n terminada en blanco y negro con un rango tonal completo.") if HAVE_EDIT_FLOAT else "")
            + bullets([
                ("Tonos fuertes:","guarda las fotos con un rango completo: negros reales, blancos limpios y grises en medio."),
                ("Tema claro:","guarda las fotos donde el tema resalta, con ayuda de la luz, la l&iacute;nea o el espacio negativo."),
                ("N&iacute;tidas donde importa:","guarda las im&aacute;genes n&iacute;tidas. Descarta las borrosas."),
            ])
            + note(f"Llama a estas tus selecciones. Terminas con {NF}: tus fotos m&aacute;s fuertes en blanco y negro."))
        es+=deliverables_box(True,
            [(f"Tus {NF} fotos editadas (JPG):",f"tus mejores {NF} fotos de la caminata, terminadas en blanco y negro y exportadas como JPG a resoluci&oacute;n completa, subidas a esta tarea de Canvas.")])
        es+=card("EDITA / TERMINA EN BLANCO Y NEGRO","Haz Que Cada Foto Sea la Mejor",
            para("Estos son archivos RAW, as&iacute; que tienes espacio para editar. Termina cada foto en blanco y negro en la Mac en Lightroom Classic.")
            + steps([
                ("Ponla en blanco y negro:","en el m&oacute;dulo Develop, pon la foto en un perfil o tratamiento en blanco y negro."),
                ("Pon tus puntos de negro y blanco:","pon la parte m&aacute;s oscura en un negro real y la m&aacute;s clara en un blanco limpio para un rango tonal completo."),
                ("Forma el contraste:","ajusta el contraste, las luces altas y las sombras para que la foto tenga profundidad. Guarda detalle en los oscuros y los claros."),
                ("Gu&iacute;a la mirada:","aclara (dodge) y oscurece (burn) zonas peque&ntilde;as para llevar la mirada a tu tema."),
            ])
            + note("No toda foto en blanco y negro necesita el m&aacute;ximo contraste. Los grises suaves pueden cargar una foto tranquila. T&uacute; decides."))
        es+=card("ENTREGA / NOMBRA Y SUBE",f"Exporta Tus {NF} JPG",
            steps([
                ("Exporta JPG a resoluci&oacute;n completa:",f"ve a File &rsaquo; Export y exporta tus {NF} fotos editadas como JPG a resoluci&oacute;n completa a la carpeta de tu proyecto."),
                ("Nombra cada archivo:","usa tu apellido y tu nombre m&aacute;s el n&uacute;mero de la foto, como <strong>Lee_Mia_Mono1.jpg</strong>."),
                ("Sube aqu&iacute;:",f"entrega tus {NF} JPG editados en blanco y negro a esta tarea de Canvas."),
            ]))
        es+=next_up("SIGUIENTE &middot; PASO 04 - Reflexi&oacute;n","Cuenta qu&eacute; buscaste, c&oacute;mo el blanco y negro cambi&oacute; lo que ve&iacute;as y cu&aacute;l foto es tu mejor.")

        stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S3}" class="silva-step-btn">Step 04 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S3}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
        return wrap_page(f"Step 3: Cull, Edit and Deliver | Monochromatic Photography | {CT} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

    # ---------- STEP 04: REFLECTION ----------
    def reflection():
        en=banner("Module 12 &bull; Step 04","Reflection",
            "Tell what you looked for, how black and white changed what you saw, and which photo is your best.","#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
        en+=card("STEP 04 / REFLECT","Complete and Upload the Reflection",
            para("Finish with a short reflection about your walk, your choices, and your best photo.")
            + note(f"The reflection document is inside the project folder you downloaded on Step 01, the Overview. Open the <strong>Monochromatic_Photography</strong> folder and find <strong>{REFL}</strong> (English or Spanish). Type right in the document.")
            + bullets([
                ("What you looked for:","what did you look for on your walk: light, shadow, line, texture, or negative space?"),
                ("Seeing without color:","how did black and white change what you saw? What did you notice that color would have hidden?"),
                ("Your best photo:","which photo is your strongest, and why? Talk about its tonal range and composition."),
                ("What you would change:","what would you do differently on your next black-and-white walk?"),
            ])
            + note("Answer honestly, in your own words, in full sentences."))
        en+=deliverables_box(False,
            [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
        en+=next_up("MODULE COMPLETE","Great work. You stopped seeing color and started seeing light, and you made ordinary campus subjects strong.")

        es=banner("M&oacute;dulo 12 &bull; Paso 04","Reflexi&oacute;n",
            "Cuenta qu&eacute; buscaste, c&oacute;mo el blanco y negro cambi&oacute; lo que ve&iacute;as y cu&aacute;l foto es tu mejor.","#top","Back to English", HICON_REFLECT)
        es+=card("PASO 04 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
            para("Termina con una reflexi&oacute;n corta sobre tu caminata, tus decisiones y tu mejor foto.")
            + note(f"El documento de reflexi&oacute;n est&aacute; dentro de la carpeta del proyecto que descargaste en el Paso 01, el Resumen. Abre la carpeta <strong>Monochromatic_Photography</strong> y busca <strong>{REFL}</strong> (en ingl&eacute;s o en espa&ntilde;ol). Escribe directamente en el documento.")
            + bullets([
                ("Qu&eacute; buscaste:","&iquest;qu&eacute; buscaste en tu caminata: luz, sombra, l&iacute;nea, textura o espacio negativo?"),
                ("Ver sin color:","&iquest;c&oacute;mo cambi&oacute; el blanco y negro lo que ve&iacute;as? &iquest;Qu&eacute; notaste que el color habr&iacute;a escondido?"),
                ("Tu mejor foto:","&iquest;cu&aacute;l foto es tu m&aacute;s fuerte y por qu&eacute;? Habla de su rango tonal y su composici&oacute;n."),
                ("Qu&eacute; cambiar&iacute;as:","&iquest;qu&eacute; har&iacute;as diferente en tu pr&oacute;xima caminata en blanco y negro?"),
            ])
            + note("Contesta con honestidad, en tus propias palabras, en oraciones completas."))
        es+=deliverables_box(True,
            [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completado, subido a esta tarea de Canvas.")])
        es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Dejaste de ver el color y empezaste a ver la luz, y volviste fuertes temas comunes de la escuela.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 03</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 03</a><span></span></div>'
        return wrap_page(f"Step 4: Reflection | Monochromatic Photography | {CT} | PVHS", nav("Step 04",dots_for(3),stepnav), top_wrap(en,es), bottom)

    return [(OVER,overview),(S1,capture_contact),(S2,cull_deliver),(S3,reflection)]

# ================= BUILD =================
for c in COURSES:
    for fname,gen in build_course(c):
        html=ent(gen())
        assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
        assert "–" not in html and "&ndash;" not in html, "en dash in "+fname
        ban_check(html, fname)
        open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
        print("wrote", fname, len(html), "bytes")
