#!/usr/bin/env python3
# Photography 1A - Module: Self-Portrait.
# Own-device capture module: students make one creative self-portrait on their own phone or a
# school iPad, cull to the single best, save as JPG, then reflect. Because it is OWN-DEVICE,
# the banner is crowned with the WHITE your-device icon on every page and the orange fresh-photos
# integrity note rides on the capture step AND the Overview. Chip-header framework via
# silva_framework. Overview + 2 steps, bilingual EN/ES, 5th-grade. Regenerates the three
# hand-authored pages 1:1 in copy; re-chromes only. See SILVA_ANGULAR_FRAMEWORK.md section 3.5.
import os
from silva_framework import *
import silva_framework as _sf

def banner(label,title,subtitle,es_href,es_label):
    # Self-Portrait is an own-device module: crown the banner with the white your-device icon.
    return _sf.banner(label,title,subtitle,es_href,es_label,HICON_YOUR_DEVICE)

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/photo1/self-portrait"
HERO=f"{IMG}/self-portrait-hero-v1.png"
CAP_FLOAT=f"{IMG}/self-portrait-float-v1.png"
REFLECT_FLOAT=f"{IMG}/self-portrait-reflection-float-v1.png"
REFLECT_EN=f"{SITE}/assets/course-documents/Self-Portrait-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Self-Portrait-Reflection-ES.docx"
AREA="Photography Folder"

OVER="photo1-self-portrait-overview.html"
S1="photo1-self-portrait-step01-capture.html"
S2="photo1-self-portrait-step02-reflection.html"

FRESH_EN=("Fresh photos only. Do not use pictures already in your camera roll from before this class. "
          "Every photo must be planned and taken on purpose for this project. Be honest and turn in your own new work.")
FRESH_ES=("Solo fotos nuevas. No uses fotos que ya ten&iacute;as en tu galer&iacute;a de antes de esta clase. "
          "Cada foto debe ser planeada y tomada a prop&oacute;sito para este proyecto. S&eacute; honesto y entrega tu propio trabajo nuevo.")

# ---- module-local helpers (cohesive teal, no framework equivalent) ----
def float_img(src, alt):
    # Content photo: teal-framed, FLOAT-marked so the card hoists it into the thumbnail column
    # (top-aligned with the title chip, drops below when narrow). Source had no caption, so
    # none is added (copy is preserved verbatim, nothing invented).
    return ('<!--FLOAT-->'
      f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;"><img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      '<!--/FLOAT-->')

def pills(labels):
    # Row of teal pills. Cohesive inside a teal content card (matches the source exactly).
    r="".join('<span style="display:inline-block;background:rgba(0,116,116,0.22);border:1px solid rgba(0,184,184,0.35);'
      'color:#80e0e0;font-size:10.5pt;letter-spacing:0.06em;text-transform:uppercase;padding:6px 12px;margin:0 8px 8px 0;">'
      f'<strong>{t}</strong></span>' for t in labels)
    return f'<div style="margin:6px 0 4px;">{r}</div>'

def subcols(pairs):
    # Full-width flex row of teal sub-panels (title + bullet list); wraps to stack when narrow.
    # Replaces the legacy two-column <table>, same panel visuals, cohesive teal.
    cells=""
    for title,its in pairs:
        lis="".join('<div style="margin-bottom:6px;line-height:1.45;"><span style="color:#00b8b8;">&bull;</span> '
          f'<span style="font-size:11.5pt;color:rgba(255,255,255,0.84);">{it}</span></div>' for it in its)
        cells+=('<div style="flex:1 1 260px;min-width:0;background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">'
          '<div style="background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:18px;height:100%;box-sizing:border-box;">'
          f'<div style="font-size:12pt;letter-spacing:0.04em;color:#5eead4;margin:2px 0 10px;"><strong>{title}</strong></div>{lis}</div></div>')
    return f'<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:6px;">{cells}</div>'

def downloads_block(es):
    # Orange Downloads section (Overview only). Self-Portrait holds the reflection doc.
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga aqu&iacute; todo lo que necesitas para este m&oacute;dulo. Consigue tus archivos antes de empezar." if es
          else "Download everything you need for this module here. Get your files before you start.")
    reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
    ref=REFLECT_ES if es else REFLECT_EN
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ref,reflabel,row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Self-Portrait</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 1A &bull; Self-Portrait","Self-Portrait","One creative self-portrait. Your phone. Your vision.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Make One Creative Self-Portrait",
        para("A self-portrait is a photo you take of yourself, on purpose, to show something about who you are. For this assignment you will use a cellphone or a school-provided iPad. You will make one polished, creative self-portrait.")
        + framed(HERO,"Self-Portrait")
        + para("This is not a school-ID photo or a plain profile picture. Be creative and make it yours: use light, angle, setting, props, or an idea that says something about you. One rule: I still have to be able to recognize you. If you use objects to hide part of your face, leave enough that I can tell it is you.")
        + pills(["Cellphone or iPad","Self-Timer","One Final JPG","Creative &amp; Recognizable"])
        + note_orange(FRESH_EN))
    en+=downloads_block(False)
    en+=card("","Find Your Self-Timer",
        para("You are the photographer and the subject, so use your camera&rsquo;s self-timer to give yourself time to get into your pose.")
        + subcols([
          ("On iPhone or iPad (iOS)",[
            "Open the Camera app and choose Photo or Portrait.",
            "Tap the up arrow at the top of the screen, or swipe up on the row under the viewfinder.",
            "Tap the Timer icon (it looks like a clock). It turns yellow when it is on.",
            "Choose 3, 5, or 10 seconds. Press the shutter and get into position."]),
          ("On Android",[
            "Samsung Galaxy: open Camera, tap the clock icon at the top, choose 2, 5, or 10 seconds.",
            "Google Pixel: open Camera, tap the gear or settings, find Timer, choose 3 or 10 seconds.",
            "Pixel tip: you can also hold your palm up to the camera to start the countdown.",
            "Press the shutter and get into position before the countdown ends."]),
        ]))
    en+=card("","Hold Your Phone Steady, No Tripod Needed",
        para("You do not need a tripod. Get creative and prop your phone up so it stays still while the timer counts down.")
        + bullets([
            ("","Lean your phone against a stack of books, a water bottle, or a backpack."),
            ("","Wedge it upright between two heavy objects."),
            ("","Fold a towel or cloth and tuck it under the phone to tilt it to the angle you want."),
            ("","Loop a hair tie or rubber band around the phone and a book to hold it."),
            ("","Rest it on a ledge, a railing, or a windowsill."),
        ])
        + para("Tip: set a 10-second timer so you have time to get in place. Take a few test photos first to check your framing, and glance at the screen before you pose."))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Self-Portrait","A photo you take of yourself, on purpose. You are both the photographer and the subject. A good one shows something real about who you are, not just what you look like."),
           ("Self-Timer","A camera setting that waits a few seconds after you press the button, then takes the photo for you. It gives you time to set the phone down and get into your pose."),
           ("Composition","How you arrange everything inside the frame: where you sit, what is in the background, and what you leave out. Good composition guides the viewer&rsquo;s eye to you."),
           ("Cull","Looking through all the photos you took and keeping only your strongest one. You drop the weak or blurry photos and select the single best image to turn in."),
           ("JPG","A common image file type that almost any computer or app can open. Your final photo must be a JPG so it opens easily and looks the way you edited it."),
           ("HEIF / HEIC","A newer photo format some phones use to save space. Many computers cannot open it, so you must change it to a JPG before you turn it in.")]), False)

    es=banner("Fotograf&iacute;a 1A &bull; Autorretrato","Autorretrato","Un autorretrato creativo. Tu tel&eacute;fono. Tu visi&oacute;n.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","Crea Un Autorretrato Creativo",
        para("Un autorretrato es una foto que te tomas a ti mismo, a prop&oacute;sito, para mostrar algo de qui&eacute;n eres. Para esta tarea vas a usar un tel&eacute;fono celular o un iPad de la escuela. Vas a crear un autorretrato pulido y creativo.")
        + framed(HERO,"Self-Portrait")
        + para("Esto no es una foto de credencial escolar ni una foto de perfil simple. S&eacute; creativo y h&aacute;zlo tuyo: usa la luz, el &aacute;ngulo, el lugar, objetos o una idea que diga algo de ti. Una regla: yo todav&iacute;a tengo que poder reconocerte. Si usas objetos para tapar parte de tu cara, deja lo suficiente para que yo pueda saber que eres t&uacute;.")
        + pills(["Tel&eacute;fono o iPad","Temporizador","Un JPG final","Creativo y Reconocible"])
        + note_orange(FRESH_ES))
    es+=downloads_block(True)
    es+=card("","Encuentra Tu Temporizador",
        para("T&uacute; eres el fot&oacute;grafo y el sujeto, as&iacute; que usa el temporizador de tu c&aacute;mara para tener tiempo de ponerte en tu pose.")
        + subcols([
          ("En iPhone o iPad (iOS)",[
            "Abre la app C&aacute;mara y elige Foto o Retrato.",
            "Toca la flecha hacia arriba en la parte de arriba, o desliza hacia arriba en la fila debajo del visor.",
            "Toca el &iacute;cono del Temporizador (parece un reloj). Se pone amarillo cuando est&aacute; activo.",
            "Elige 3, 5 o 10 segundos. Presiona el bot&oacute;n y ponte en posici&oacute;n."]),
          ("En Android",[
            "Samsung Galaxy: abre C&aacute;mara, toca el &iacute;cono de reloj arriba, elige 2, 5 o 10 segundos.",
            "Google Pixel: abre C&aacute;mara, toca el engrane o ajustes, busca Temporizador, elige 3 o 10 segundos.",
            "Truco Pixel: tambi&eacute;n puedes levantar la palma hacia la c&aacute;mara para empezar el conteo.",
            "Presiona el bot&oacute;n y ponte en posici&oacute;n antes de que termine el conteo."]),
        ]))
    es+=card("","Sostiene el Tel&eacute;fono Firme, Sin Tr&iacute;pode",
        para("No necesitas un tr&iacute;pode. S&eacute; creativo y apoya tu tel&eacute;fono para que se quede quieto mientras corre el temporizador.")
        + bullets([
            ("","Apoya el tel&eacute;fono contra una pila de libros, una botella de agua o una mochila."),
            ("","Encaja el tel&eacute;fono parado entre dos objetos pesados."),
            ("","Dobla una toalla o tela y m&eacute;tela debajo del tel&eacute;fono para inclinarlo al &aacute;ngulo que quieras."),
            ("","Enrolla una liga o coleta alrededor del tel&eacute;fono y un libro para sostenerlo."),
            ("","Ap&oacute;yalo en una repisa, un barandal o el borde de una ventana."),
        ])
        + para("Consejo: pon el temporizador en 10 segundos para tener tiempo de acomodarte. Toma unas fotos de prueba primero para revisar el encuadre y mira la pantalla antes de posar."))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Autorretrato","Una foto que te tomas a ti mismo, a prop&oacute;sito. Eres el fot&oacute;grafo y tambi&eacute;n el sujeto. Uno bueno muestra algo real de qui&eacute;n eres, no solo c&oacute;mo te ves."),
           ("Temporizador","Un ajuste de la c&aacute;mara que espera unos segundos despu&eacute;s de presionar el bot&oacute;n y luego toma la foto por ti. Te da tiempo de dejar el tel&eacute;fono y ponerte en tu pose."),
           ("Composici&oacute;n","C&oacute;mo acomodas todo dentro del cuadro: d&oacute;nde te pones, qu&eacute; hay en el fondo y qu&eacute; dejas fuera. Una buena composici&oacute;n gu&iacute;a la mirada hacia ti."),
           ("Seleccionar","Revisar todas las tomas que hiciste y quedarte solo con la m&aacute;s fuerte. Quitas las fotos d&eacute;biles o borrosas y eliges la mejor imagen para entregar."),
           ("JPG","Un tipo de archivo de imagen com&uacute;n que casi cualquier computadora o app puede abrir. Tu foto final debe ser un JPG para que se abra f&aacute;cil y se vea como la editaste."),
           ("HEIF / HEIC","Un formato de foto m&aacute;s nuevo que algunos tel&eacute;fonos usan para ahorrar espacio. Muchas computadoras no pueden abrirlo, as&iacute; que debes cambiarlo a JPG antes de entregar.")]), True)

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Self-Portrait | Photography 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Photography 1A &bull; Self-Portrait &bull; Step 01","Capture &amp; Submit","Set up, capture, cull, and turn in your JPG.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 JPG:","One final, polished, creative self-portrait, saved as a JPG.")])
    en+=card("","Capture, Cull, and Submit Your Self-Portrait",
        float_img(CAP_FLOAT,"Self-Portrait")
        + para("Pick your idea and set up your photo. Frame yourself, set your self-timer, and prop your phone steady (see the overview). Take several photos and adjust your pose, your angle, and the light between tries.")
        + para("Cull your photos: look through everything you took and select your single strongest, most creative self-portrait, the one that shows who you are and that I can still recognize.")
        + para("Polish it (optional): if your phone has editing tools, adjust exposure, brightness, and color to make your image look its best. Keep it clean and natural.")
        + para("Save it as a JPG: your final image must be a JPG. If your phone saves photos as HEIF or HEIC, email the photo to your school computer, open it, and save or export it as a JPG. Not sure how? Ask me in class and I will help.")
        + note_orange(FRESH_EN))

    es=banner("Fotograf&iacute;a 1A &bull; Autorretrato &bull; Paso 01","Captura y Entrega","Prepara, captura, selecciona y entrega tu JPG.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 JPG:","Un autorretrato final, pulido y creativo, guardado como JPG.")])
    es+=card("","Captura, Selecciona y Entrega Tu Autorretrato",
        float_img(CAP_FLOAT,"Autorretrato")
        + para("Elige tu idea y prepara tu toma. Enc&uacute;adrate, pon tu temporizador y apoya tu tel&eacute;fono firme (mira el resumen). Toma varias fotos y ajusta tu pose, tu &aacute;ngulo y la luz entre cada intento.")
        + para("Selecciona tus tomas: revisa todo lo que tomaste y elige tu autorretrato m&aacute;s fuerte y creativo, el que muestre qui&eacute;n eres y en el que todav&iacute;a te pueda reconocer.")
        + para("Pule tu imagen (opcional): si tu tel&eacute;fono tiene herramientas de edici&oacute;n, ajusta la exposici&oacute;n, el brillo y el color para que tu imagen se vea lo mejor posible. Mant&eacute;nla limpia y natural.")
        + para("Gu&aacute;rdala como JPG: tu imagen final debe ser un JPG. Si tu tel&eacute;fono guarda las fotos como HEIF o HEIC, env&iacute;a la foto por correo a tu computadora de la escuela, &aacute;brela y gu&aacute;rdala o exp&oacute;rtala como JPG. &iquest;No sabes c&oacute;mo? Pregunta en clase y te ayudo.")
        + note_orange(FRESH_ES))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Capture and Submit | Self-Portrait | Photography 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Photography 1A &bull; Self-Portrait &bull; Step 02","Reflection","Look back. What worked, what to improve.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to Canvas.")])
    en+=card("","Reflection",
        float_img(REFLECT_FLOAT,"Anthony typing his reflection in Word")
        + para("Take a few minutes to reflect on your self-portrait: the idea behind it, how well you think you pulled it off, and what you would do better next time.")
        + bullets([
            ("","What was your idea, and what were you trying to show about yourself?"),
            ("","How well did you execute it? What worked?"),
            ("","What was the hardest part, and what would you do better next time?"),
        ])
        + para("You will come back to this assignment later in the year, once you have more photography skills, and make an even stronger self-portrait. This reflection is your starting point.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder."))

    es=banner("Fotograf&iacute;a 1A &bull; Autorretrato &bull; Paso 02","Reflexi&oacute;n","Mira atr&aacute;s. Qu&eacute; funcion&oacute;, qu&eacute; mejorar.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word de la reflexi&oacute;n (.docx), subido a Canvas.")])
    es+=card("","Reflexi&oacute;n",
        float_img(REFLECT_FLOAT,"Anthony escribiendo su reflexi&oacute;n en Word")
        + para("T&oacute;mate unos minutos para reflexionar sobre tu autorretrato: la idea detr&aacute;s de &eacute;l, qu&eacute; tan bien crees que lo lograste y qu&eacute; har&iacute;as mejor la pr&oacute;xima vez.")
        + bullets([
            ("","&iquest;Cu&aacute;l era tu idea y qu&eacute; tratabas de mostrar de ti?"),
            ("","&iquest;Qu&eacute; tan bien lo lograste? &iquest;Qu&eacute; funcion&oacute;?"),
            ("","&iquest;Qu&eacute; fue lo m&aacute;s dif&iacute;cil y qu&eacute; har&iacute;as mejor la pr&oacute;xima vez?"),
        ])
        + para("M&aacute;s adelante en el a&ntilde;o vas a volver a esta tarea, ya con m&aacute;s habilidades de fotograf&iacute;a, y crear&aacute;s un autorretrato a&uacute;n m&aacute;s fuerte. Esta reflexi&oacute;n es tu punto de partida.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
    return wrap_page("Step 2: Reflection | Self-Portrait | Photography 1A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
