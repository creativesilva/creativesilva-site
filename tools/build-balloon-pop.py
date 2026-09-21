#!/usr/bin/env python3
# Balloon Pop (Photography 1A Module 07 AND Photography 2A Module 06) - identical module, two courses.
# The capstone of the shutter-speed unit: students work in PAIRS outside with a school CAMERA KIT
# (18-45mm), set the camera by hand, and use a fast shutter + High-Speed Continuous to freeze a water
# balloon into a floating globe the instant it bursts. They share their best frames, do a light
# Lightroom crop (JPG), and submit their favorite 1 to 3 images (Step 01), then write a short
# reflection (Step 02). School-kit, so NO fresh-photos note. The last page foreshadows the next
# module: Aperture. Overview + 2 steps, bilingual EN/ES, 5th-grade. Uses the shared silva_framework.
import os
from silva_framework import *
import silva_framework as _sf
def banner(label,title,subtitle,es_href,es_label):
    # Camera-kit outdoor capture: crown the banner with the white photo-walk icon.
    return _sf.banner(label,title,subtitle,es_href,es_label,HICON_PHOTO_WALK)

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/photo1/balloon-pop"
HEADER=f"{IMG}/balloon-pop-header-v1.jpg"
STEP1_FLOAT=f"{IMG}/balloon-pop-step01-float-v1.jpg"
BTN=f"{IMG}/balloon-pop-drive-button-v1.jpg"
DOCS=f"{SITE}/assets/course-documents"
AREA="Photography Folder"

# Per-course config. Content is identical; only these fields change.
COURSES=[
  {"cn_en":"Photography 1A","cn_es":"Fotograf&iacute;a 1A","mod":"07",
   "over":"photo1-balloon-pop-overview.html",
   "s1":"photo1-balloon-pop-step01-capture.html",
   "s2":"photo1-balloon-pop-step02-reflection.html",
   "refl_en":f"{DOCS}/Balloon-Pop-Reflection-EN.docx",
   "refl_es":f"{DOCS}/Balloon-Pop-Reflection-ES.docx"},
  {"cn_en":"Photography 2A","cn_es":"Fotograf&iacute;a 2A","mod":"06",
   "over":"photo2-balloon-pop-overview.html",
   "s1":"photo2-balloon-pop-step01-capture.html",
   "s2":"photo2-balloon-pop-step02-reflection.html",
   "refl_en":f"{DOCS}/Balloon-Pop-Photo2-Reflection-EN.docx",
   "refl_es":f"{DOCS}/Balloon-Pop-Photo2-Reflection-ES.docx"},
]

def nxt_mod(C):
    return f"{int(C['mod'])+1:02d}"

# CTE Studio Arts standards (draft, same family as the other photo modules).
BP_STANDARDS=[
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You use shutter speed, timing, and exposure on purpose to freeze a fast-moving moment.",
   "es_desc":"Usas la velocidad del obturador, el momento justo y la exposici&oacute;n a prop&oacute;sito para congelar un momento r&aacute;pido."},
  {"code":"SA.17.2","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Visual Communication","es_title":"Comunicaci&oacute;n Visual",
   "en_desc":"You capture a split second the eye cannot catch and turn it into a striking image.",
   "es_desc":"Capturas una fracci&oacute;n de segundo que el ojo no alcanza a ver y la conviertes en una imagen impactante."},
  {"code":"SA.17.5","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Equipment &amp; Image Production","es_title":"Equipo y Producci&oacute;n de Imagen",
   "en_desc":"You set a camera kit by hand in Manual mode and use High-Speed Continuous to catch the burst.",
   "es_desc":"Configuras un kit de c&aacute;mara a mano en modo Manual y usas Alta Velocidad Continua para atrapar el estallido."},
  {"code":"SA.17.9","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Collaboration &amp; Critique","es_title":"Colaboraci&oacute;n y Cr&iacute;tica",
   "en_desc":"You work as a pair, share your best frames, and reflect on what worked and what to try next.",
   "es_desc":"Trabajas en pareja, compartes tus mejores tomas y reflexionas sobre qu&eacute; funcion&oacute; y qu&eacute; probar despu&eacute;s."},
]

# ---------------- DRIVE MODE: HIGH-SPEED CONTINUOUS (separate red section) ----------------
# The camera-settings GRAPHIC is the LOCKED framework template (camera_settings_section): only the
# three values + the "CHANGE THIS" position change. This separate red section carries the manual-mode
# + High-Speed Continuous how-to and the drive-button close-up, which live OUTSIDE the locked graphic.
def high_speed_section(es):
    red="#f90101"
    if es:
        title="Modo de Disparo"
        intro=("Pon la c&aacute;mara en modo Manual (M). Luego pon el modo de disparo en Alta Velocidad Continua "
               "para que tome muchas fotos por segundo mientras mantienes el bot&oacute;n presionado. As&iacute; "
               "atrapas la fracci&oacute;n de segundo en que revienta el globo.")
        hs_steps=[
            ("Presiona el bot&oacute;n de disparo","en el lado derecho del disco trasero (marcado en rojo)."),
            ("Elige Alta Velocidad Continua","el &iacute;cono de cuadros apilados."),
            ("Mant&eacute;n presionado el disparador","mientras tu pareja revienta el globo, para capturar una r&aacute;faga r&aacute;pida."),
        ]
        btn_alt="Primer plano del bot&oacute;n de disparo en el disco trasero de la c&aacute;mara, marcado en rojo"
    else:
        title="Drive Mode"
        intro=("Set your camera to Manual (M). Then set the drive mode to High-Speed Continuous so it takes many "
               "photos per second while you hold the button down. That is how you catch the split second the "
               "balloon bursts.")
        hs_steps=[
            ("Press the drive button","on the right side of the back dial (circled in red)."),
            ("Choose High-Speed Continuous","the stacked-frames icon."),
            ("Hold the shutter button down","as your partner pops the balloon, to capture a fast burst."),
        ]
        btn_alt="Close-up of the camera&rsquo;s drive button on the back dial, circled in red"
    steps_html=""
    for n,(b,rest) in enumerate(hs_steps,1):
        steps_html+=(f'<div style="display:flex;gap:12px;align-items:flex-start;margin-top:10px;">'
          f'<span style="flex:0 0 auto;width:26px;height:26px;border-radius:50%;background:{red};color:#fff;'
          f'font-family:Arial,sans-serif;font-size:12pt;line-height:26px;text-align:center;"><strong>{n}</strong></span>'
          f'<span style="font-size:12.5pt;color:rgba(255,255,255,0.90);line-height:1.5;"><strong>{b}</strong> {rest}</span></div>')
    hs_img=(f'<div style="flex:0 0 auto;width:200px;max-width:42%;"><div style="border:2px solid {red};background:#000;">'
      f'<img src="{BTN}" alt="{btn_alt}" style="display:block;width:100%;height:auto;" /></div></div>')
    body=('<div style="display:flex;flex-wrap:wrap-reverse;gap:18px 26px;align-items:flex-start;">'
      + f'<div style="flex:1 1 320px;min-width:0;"><div style="font-size:13pt;color:rgba(255,255,255,0.88);line-height:1.6;margin-bottom:4px;">{intro}</div>{steps_html}</div>'
      + hs_img
      + '</div>')
    return (f'<div style="background:linear-gradient(180deg,rgba(249,1,1,0.06) 0%,rgba(249,1,1,0.02) 100%);border:1px solid rgba(249,1,1,0.26);border-left:6px solid {red};padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(CAMSET_ICON, title, "#f90101", "#ff8f8f")
      + body
      + '</div>')

def downloads_block(es, C):
    # Orange Downloads section (Overview only). Balloon Pop holds the reflection doc (per course).
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga aqu&iacute; todo lo que necesitas para este m&oacute;dulo. Consigue tus archivos antes de empezar." if es
          else "Download everything you need for this module here. Get your files before you start.")
    reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
    ref=C["refl_es"] if es else C["refl_en"]
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ref,reflabel,row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

def nav(current,dots,stepnav,C):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{C["over"]}" class="bc-hide-sm">Balloon Pop</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

# ---------------- OVERVIEW ----------------
def overview(C):
    OVER,S1,S2=C["over"],C["s1"],C["s2"]
    en=banner(f'{C["cn_en"]}',f'Module {C["mod"]}: Balloon Pop',"Freeze a water balloon into a globe the instant it bursts.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Balloon Pop",
        para("This is our big finish for shutter speed. You and a partner will pop water balloons outside and use a fast shutter to freeze the water in mid-air. For one split second, right after the balloon breaks, the water still holds a round shape like a little globe. Your job is to catch that exact moment.")
        + framed(HEADER,"Two Pioneer Valley students outside by the panther statue: one aims a camera while the other pops a water balloon, the water frozen in mid-air as a clear globe")
        + para("You will use a school camera kit with the 18-45mm lens, set the camera by hand, and take a fast burst of photos as the balloon pops. Then you and your partner share your best frames, do a light crop, and each turn in your favorite 1 to 3 images."))
    en+=standards_box(False, BP_STANDARDS)
    en+=downloads_block(False, C)
    en+=card("HOW TO NAIL IT","Tips for a Clean Freeze",
        para("A great freeze comes from being ready before the pop and getting close. Set up, focus, and start your burst a moment early so you never miss the globe.")
        + bullets([
            ("Fill the frame:","get close enough that the balloon and the water are the star, not the background."),
            ("Focus early:","pre-focus on your partner&rsquo;s hand so the burst lands sharp."),
            ("Start before the pop:","hold the button down just before the balloon breaks so the burst is already going."),
            ("Use good light:","face the sun or work in open shade so the fast shutter still gets a bright photo."),
            ("Take turns:","one person holds and pops, one captures, then switch so you both get a turn."),
        ]))
    en+=resources_card("Key Words", vocab_grid("On the Quiz",
        "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
        [("Shutter Speed","How long the camera&rsquo;s shutter stays open for one photo. A fast shutter, like 1/1600, is open for only a tiny sliver of time, so it can freeze fast action."),
         ("Freeze Motion","Using a fast shutter speed to catch a moving thing so sharp that it looks frozen, like water hanging in the air instead of a blur."),
         ("High-Speed Continuous","A drive mode that takes many photos per second while you hold the button down. It gives you a burst of frames so one of them catches the perfect moment."),
         ("Manual Mode (M)","A camera mode where you set the shutter, aperture, and ISO yourself. The camera keeps them locked, so every frame comes out the same."),
         ("ISO","How sensitive the camera is to light. A higher ISO, like 800, makes the photo brighter, which helps when you are using a very fast shutter."),
         ("Aperture","How wide the lens opens, shown as an f-number like F8.0. It controls how much light comes in and how much of the photo is in focus. It is the focus of our next module.")]), False)
    en+=next_up("UP NEXT &middot; STEP 01 - Capture, Crop &amp; Submit","Grab your camera kit and a partner. Next you&rsquo;ll head outside and freeze the balloon pop.")

    es=banner(f'{C["cn_es"]}',f'M&oacute;dulo {C["mod"]}: Globo de Agua',"Congela un globo de agua en una esfera en el instante en que revienta.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","Globo de Agua",
        para("Este es nuestro gran cierre de la velocidad del obturador. T&uacute; y tu pareja van a reventar globos de agua afuera y usar un obturador r&aacute;pido para congelar el agua en el aire. Por una fracci&oacute;n de segundo, justo despu&eacute;s de que el globo se rompe, el agua a&uacute;n mantiene una forma redonda como una peque&ntilde;a esfera. Tu trabajo es atrapar ese momento exacto.")
        + framed(HEADER,"Dos estudiantes de Pioneer Valley afuera junto a la estatua de la pantera: uno apunta una c&aacute;mara mientras la otra revienta un globo de agua, con el agua congelada en el aire como una esfera")
        + para("Vas a usar un kit de c&aacute;mara de la escuela con el lente 18-45mm, configurar la c&aacute;mara a mano y tomar una r&aacute;faga r&aacute;pida de fotos cuando el globo revienta. Luego t&uacute; y tu pareja comparten sus mejores tomas, hacen un recorte ligero y cada uno entrega sus 1 a 3 im&aacute;genes favoritas."))
    es+=standards_box(True, BP_STANDARDS)
    es+=downloads_block(True, C)
    es+=card("C&Oacute;MO LOGRARLO","Consejos Para un Buen Congelado",
        para("Un buen congelado sale de estar listo antes del estallido y de acercarte. Prep&aacute;rate, enfoca y empieza tu r&aacute;faga un momento antes para nunca perder la esfera.")
        + bullets([
            ("Llena el encuadre:","ac&eacute;rcate para que el globo y el agua sean la estrella, no el fondo."),
            ("Enfoca antes:","pre-enfoca en la mano de tu pareja para que el estallido salga n&iacute;tido."),
            ("Empieza antes del estallido:","mant&eacute;n el bot&oacute;n presionado justo antes de que el globo se rompa, para que la r&aacute;faga ya est&eacute; corriendo."),
            ("Usa buena luz:","ponte de frente al sol o trabaja en sombra abierta para que el obturador r&aacute;pido a&uacute;n consiga una foto con luz."),
            ("T&oacute;mense turnos:","una persona sostiene y revienta, otra captura, y luego cambian para que ambos tengan su turno."),
        ]))
    es+=resources_card("Palabras Clave", vocab_grid("En el Examen",
        "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el de mitad de semestre y el del final. Apr&eacute;ndelas ahora, no la noche anterior.",
        [("Velocidad del Obturador","Cu&aacute;nto tiempo el obturador de la c&aacute;mara queda abierto para una foto. Un obturador r&aacute;pido, como 1/1600, se abre solo una fracci&oacute;n de tiempo, as&iacute; que congela la acci&oacute;n r&aacute;pida."),
         ("Congelar Movimiento","Usar un obturador r&aacute;pido para atrapar algo en movimiento tan n&iacute;tido que se ve congelado, como el agua flotando en el aire en vez de borrosa."),
         ("Alta Velocidad Continua","Un modo de disparo que toma muchas fotos por segundo mientras mantienes el bot&oacute;n presionado. Te da una r&aacute;faga de tomas para que una atrape el momento perfecto."),
         ("Modo Manual (M)","Un modo de c&aacute;mara donde t&uacute; pones el obturador, la apertura y el ISO. La c&aacute;mara los deja fijos, as&iacute; que cada toma sale igual."),
         ("ISO","Qu&eacute; tan sensible es la c&aacute;mara a la luz. Un ISO m&aacute;s alto, como 800, hace la foto m&aacute;s brillante, lo que ayuda cuando usas un obturador muy r&aacute;pido."),
         ("Apertura","Qu&eacute; tan ancho se abre el lente, mostrado como un n&uacute;mero f como F8.0. Controla cu&aacute;nta luz entra y cu&aacute;nto de la foto queda en foco. Es el tema de nuestro pr&oacute;ximo m&oacute;dulo.")]), True)
    es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 01 - Captura, Recorta y Entrega","Toma tu kit de c&aacute;mara y una pareja. Ahora vas a salir y congelar el globo de agua.")

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page(f'Balloon Pop | {C["cn_en"]} | PVHS', nav("Overview",dots,stepnav,C), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01(C):
    OVER,S1,S2=C["over"],C["s1"],C["s2"]
    en=banner(f'Module {C["mod"]} &bull; Step 01',"Capture, Crop &amp; Submit","Work in pairs. Pop, freeze, and capture the burst.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("STEP 01 / CAPTURE","Pop, Freeze, and Capture",
        float_right(STEP1_FLOAT,"Close-up of a water balloon at the instant it pops: the water holds a round globe shape in mid-air as a pin breaks the balloon","The exact moment to catch: the water still holds a globe shape the instant the balloon breaks.")
        + para("Head outside with your partner and your camera kit. One person holds and pops the water balloon. The other person captures a fast burst of photos at the exact moment it bursts. Then trade places so you both get a turn.")
        + para("You may not both get a perfect frame, and that is okay. Work as a team: share your best images with each other so you both have great photos to pick from.")
        + bullets([
            ("Take turns:","one person pops, one captures, then switch."),
            ("Aim for the globe:","the best frame is the split second the water still holds a round shape."),
            ("Start early:","hold the button down just before the pop so the burst is already going."),
            ("Share your best:","give your partner your best frames, and use theirs too."),
        ])
        + note("Water and cameras do not mix. Keep the camera back from the splash zone and dry your hands before you touch the gear."))
    en+=camera_settings_section(False, quality="JPG", shutter="1/1600", aperture="F8.0", iso="800", change_field="shutter", activity="Balloon Pop")
    en+=high_speed_section(False)
    en+=deliverables_box(False,
        [("1 to 3 favorite images (JPG),","your best frozen-globe photos, lightly cropped and uploaded to this Canvas assignment.")])
    en+=card("CROP &amp; SUBMIT","A Light Crop, Then Turn It In",
        para("Bring your favorite photos into Lightroom and do a light edit. Since these are JPG files, keep it simple: mostly just crop to frame the water globe and straighten it if needed. You do not need heavy edits.")
        + para("Export your best 1 to 3 images as high-quality JPGs and upload them to Canvas. Then go to Step 02 for the reflection."))
    en+=next_up("UP NEXT &middot; STEP 02 - Reflection","With your favorites turned in, you&rsquo;ll write a short reflection and pitch another outdoor photo activity.")

    es=banner(f'M&oacute;dulo {C["mod"]} &bull; Paso 01',"Captura, Recorta y Entrega","Trabajen en parejas. Revienta, congela y captura el estallido.","#top","Back to English")
    es+=card("PASO 01 / CAPTURA","Revienta, Congela y Captura",
        float_right(STEP1_FLOAT,"Primer plano de un globo de agua en el instante en que revienta: el agua mantiene una forma redonda en el aire mientras un alfiler rompe el globo","El momento exacto que hay que atrapar: el agua a&uacute;n mantiene una forma de esfera en el instante en que el globo se rompe.")
        + para("Sal afuera con tu pareja y tu kit de c&aacute;mara. Una persona sostiene y revienta el globo de agua. La otra persona captura una r&aacute;faga r&aacute;pida de fotos en el momento exacto en que revienta. Luego cambien de lugar para que ambos tengan su turno.")
        + para("Puede que no ambos consigan una toma perfecta, y est&aacute; bien. Trabajen en equipo: compartan sus mejores im&aacute;genes para que ambos tengan buenas fotos para elegir.")
        + bullets([
            ("T&oacute;mense turnos:","una persona revienta, otra captura, y luego cambian."),
            ("Busca la esfera:","la mejor toma es la fracci&oacute;n de segundo en que el agua a&uacute;n mantiene una forma redonda."),
            ("Empieza antes:","mant&eacute;n el bot&oacute;n presionado justo antes del estallido para que la r&aacute;faga ya est&eacute; corriendo."),
            ("Comparte lo mejor:","dale a tu pareja tus mejores tomas y usa las de ella tambi&eacute;n."),
        ])
        + note("El agua y las c&aacute;maras no se llevan bien. Mant&eacute;n la c&aacute;mara lejos de la zona de salpicaduras y s&eacute;cate las manos antes de tocar el equipo."))
    es+=camera_settings_section(True, quality="JPG", shutter="1/1600", aperture="F8.0", iso="800", change_field="shutter", activity="el Globo de Agua")
    es+=high_speed_section(True)
    es+=deliverables_box(True,
        [("1 a 3 im&aacute;genes favoritas (JPG),","tus mejores fotos de la esfera congelada, con un recorte ligero y subidas a esta tarea de Canvas.")])
    es+=card("RECORTA Y ENTREGA","Un Recorte Ligero, Luego Entrega",
        para("Lleva tus fotos favoritas a Lightroom y haz una edici&oacute;n ligera. Como son archivos JPG, mantenlo simple: sobre todo recorta para encuadrar la esfera de agua y enderezarla si hace falta. No necesitas ediciones fuertes.")
        + para("Exporta tus mejores 1 a 3 im&aacute;genes como JPG de alta calidad y s&uacute;belas a Canvas. Luego ve al Paso 02 para la reflexi&oacute;n."))
    es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 02 - Reflexi&oacute;n","Con tus favoritas entregadas, vas a escribir una reflexi&oacute;n corta y proponer otra actividad de fotos al aire libre.")

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page(f'Balloon Pop: Capture | {C["cn_en"]} | PVHS', nav("Step 01",dots,stepnav,C), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02(C):
    OVER,S1,S2=C["over"],C["s1"],C["s2"]
    NX=nxt_mod(C)
    en=banner(f'Module {C["mod"]} &bull; Step 02',"Reflection","What worked, what didn&rsquo;t, and what&rsquo;s next.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("STEP 02 / REFLECTION","Reflect on the Balloon Pop",
        para("Finish with a short and simple reflection. Tell what worked, what did not work, and what you would do better next time. Then share any feedback or an idea for another outdoor photography activity we could try as a class.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + para("Type your answers in the document, save it, and upload it to Canvas."))
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to Canvas.")])
    en+=next_up(f"UP NEXT &middot; MODULE {NX} - Aperture","That wraps up shutter speed. Next module we switch to aperture: the f-number that controls how much of your photo is in focus, from a soft, blurry background to sharp from front to back.")

    es=banner(f'M&oacute;dulo {C["mod"]} &bull; Paso 02',"Reflexi&oacute;n","Qu&eacute; funcion&oacute;, qu&eacute; no, y qu&eacute; sigue.","#top","Back to English")
    es+=card("PASO 02 / REFLEXI&Oacute;N","Reflexiona Sobre el Globo de Agua",
        para("Termina con una reflexi&oacute;n corta y simple. Di qu&eacute; funcion&oacute;, qu&eacute; no funcion&oacute; y qu&eacute; har&iacute;as mejor la pr&oacute;xima vez. Luego comparte cualquier idea o comentario para otra actividad de fotograf&iacute;a al aire libre que podamos probar como clase.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y consíguelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + para("Escribe tus respuestas en el documento, gu&aacute;rdalo y s&uacute;belo a Canvas."))
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word de reflexi&oacute;n completo (.docx), subido a Canvas.")])
    es+=next_up(f"A CONTINUACI&Oacute;N &middot; M&Oacute;DULO {NX} - Apertura","Con esto cerramos la velocidad del obturador. El pr&oacute;ximo m&oacute;dulo pasamos a la apertura: el n&uacute;mero f que controla cu&aacute;nto de tu foto queda en foco, desde un fondo suave y borroso hasta n&iacute;tido de adelante hacia atr&aacute;s.")

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
    return wrap_page(f'Balloon Pop: Reflection | {C["cn_en"]} | PVHS', nav("Step 02",dots,stepnav,C), top_wrap(en,es), bottom)

for C in COURSES:
    for fname,gen in [(C["over"],overview),(C["s1"],step01),(C["s2"],step02)]:
        html=ent(gen(C))
        ban_check(html, fname)
        open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
        print("wrote", fname, len(html), "bytes")
