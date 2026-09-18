#!/usr/bin/env python3
# Photography 1A - Module 06: Tiny Things.
# A weekend challenge: see the world from a bug's-eye view. Students find and photograph 6 tiny
# things we normally overlook (high, low, or eye level) on their OWN DEVICE (phone or iPad), upload
# all 6 (Step 1), then write a short reflection (Step 2). Own-device, so the banner wears the white
# your-device crown and the overview + capture step carry the orange fresh-photos note.
# Overview + 2 steps, bilingual EN/ES, 5th-grade. Uses the shared silva_framework chrome.
import os
from silva_framework import *
import silva_framework as _sf
def banner(label,title,subtitle,es_href,es_label):
    # Own-device module: crown the banner with the white your-device icon.
    return _sf.banner(label,title,subtitle,es_href,es_label,HICON_YOUR_DEVICE)

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/photo1/tiny-things"
HEADER=f"{IMG}/tiny-things-header-v1.jpg"
STEP1_FLOAT=f"{IMG}/tiny-things-step01-float-v1.jpg"
REFLECT_FLOAT=f"{SITE}/assets/images/photo1/composition-concepts/reflection-float-v1.jpg"
REFLECT_EN=f"{SITE}/assets/course-documents/Tiny-Things-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Tiny-Things-Reflection-ES.docx"
AREA="Photography Folder"

FRESH_EN="Fresh photos only. Do not use pictures already in your camera roll from before this class. Every photo must be planned and taken on purpose for this project. Be honest and turn in your own new work."
FRESH_ES="Solo fotos nuevas. No uses fotos que ya tenías en tu galería de antes de esta clase. Cada foto debe ser planeada y tomada a propósito para este proyecto. Sé honesto y entrega tu propio trabajo nuevo."

OVER="photo1-tiny-things-overview.html"
S1="photo1-tiny-things-step01-capture.html"
S2="photo1-tiny-things-step02-reflection.html"

# CTE Studio Arts standards (draft, pending validation with the others).
TT_STANDARDS=[
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Diseño",
   "en_desc":"You use angle, light, and composition on purpose to turn a small, overlooked thing into a strong photo.",
   "es_desc":"Usas el ángulo, la luz y la composición a propósito para convertir algo pequeño y olvidado en una buena foto."},
  {"code":"SA.17.2","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Visual Communication","es_title":"Comunicación Visual",
   "en_desc":"You show something people walk past every day in a fresh, surprising way.",
   "es_desc":"Muestras algo que la gente pasa por alto todos los días de una forma nueva y sorprendente."},
  {"code":"SA.17.5","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Equipment &amp; Image Production","es_title":"Equipo y Producción de Imagen",
   "en_desc":"You use your phone or iPad camera, get close, and hold steady to make a clean, sharp close-up.",
   "es_desc":"Usas la cámara de tu teléfono o iPad, te acercas y mantienes firme para hacer un primer plano limpio y nítido."},
  {"code":"SA.17.9","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Critique","es_title":"Crítica",
   "en_desc":"You look back at your six photos and share an idea for the next weekend challenge.",
   "es_desc":"Revisas tus seis fotos y compartes una idea para el próximo reto del fin de semana."},
]

def downloads_block(es):
    # Orange Downloads section (Overview only). Tiny Things holds the reflection doc.
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga aquí todo lo que necesitas para este módulo. Consigue tus archivos antes de empezar." if es
          else "Download everything you need for this module here. Get your files before you start.")
    reflabel="Documento de Reflexión (Word)" if es else "Reflection Document (Word)"
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
            f'        <a href="{OVER}" class="bc-hide-sm">Tiny Things</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 1A &bull; Tiny Things","Tiny Things","A weekend challenge: see the world from a bug&rsquo;s eye view.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Tiny Things",
        para("This weekend, slow down and look closer. Your challenge is to see the world the way a bug sees it: from down low, up high, or right at eye level with something small. Find 6 tiny things we normally walk right past and photograph them so they finally get noticed. You use your own phone or a school iPad, so everyone has a fair and equal way to take part.")
        + framed(HEADER,"Tiny Things")
        + para("Think about the small stuff: a crack in the sidewalk, a bug on a leaf, a screw in a door hinge, a drop of water, a crumb, a key, or the tip of a shoelace. Get close, change your angle, and make the ordinary look amazing.")
        + note_orange(FRESH_EN))
    en+=standards_box(False, TT_STANDARDS)
    en+=downloads_block(False)
    en+=card("HOW TO FIND THEM","Tips for Tiny Things",
        para("The best tiny-thing photos come from getting low and getting close. Move your whole body, not just your arm, and try a few angles before you tap.")
        + bullets([
            ("Get down to its level:","kneel, crouch, or set the phone on the ground for a true bug&rsquo;s-eye view."),
            ("Fill the frame:","move in close so the tiny thing is the star, not lost in a big background."),
            ("Use macro or close-up mode:","many phones switch to a close-up or macro mode when you move in near a subject. Tap the screen to lock focus on the detail."),
            ("Look where no one looks:","corners, cracks, undersides, and the ground are full of overlooked tiny things."),
        ]))
    en+=vocab_grid("On the Quiz",
        "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
        [("Macro","An extreme close-up photo that makes a tiny thing look big and shows detail your eyes usually miss, like the fuzz on a bee or the bumps on a strawberry."),
         ("Close-Up","A photo taken very near your subject so the small thing fills most of the frame. Getting close is the easiest way to make a tiny thing feel important."),
         ("Perspective","The spot and angle you photograph from. Change your perspective, like kneeling down low, and an ordinary object can look huge."),
         ("Point of View (POV)","Where your camera &lsquo;stands&rsquo; when you take the photo. A low point of view, like a bug on the ground, makes small things feel powerful."),
         ("Worm&rsquo;s-Eye View","A very low angle that looks up at your subject, as if you were down on the ground like a worm or a bug. It is the opposite of a bird&rsquo;s-eye view."),
         ("Depth of Field","How much of your photo is in sharp focus. In a close-up, often only the tiny subject is sharp and the background goes soft and blurry.")])

    es=banner("Fotograf&iacute;a 1A &bull; Cosas Peque&ntilde;as","Cosas Peque&ntilde;as","Un reto de fin de semana: ve el mundo como lo ve un insecto.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","Cosas Peque&ntilde;as",
        para("Este fin de semana, ve más despacio y mira de cerca. Tu reto es ver el mundo como lo ve un insecto: desde muy abajo, desde arriba o justo al nivel de los ojos de algo pequeño. Encuentra 6 cosas pequeñas que normalmente pasamos por alto y fotografíalas para que por fin se noten. Usas tu propio teléfono o un iPad de la escuela, para que todos tengan una forma justa e igual de participar.")
        + framed(HEADER,"Cosas Peque&ntilde;as")
        + para("Piensa en las cosas pequeñas: una grieta en la banqueta, un insecto en una hoja, un tornillo en una bisagra, una gota de agua, una miga, una llave o la punta de una agujeta. Acércate, cambia tu ángulo y haz que lo común se vea increíble.")
        + note_orange(FRESH_ES))
    es+=standards_box(True, TT_STANDARDS)
    es+=downloads_block(True)
    es+=card("C&Oacute;MO ENCONTRARLAS","Consejos Para Cosas Peque&ntilde;as",
        para("Las mejores fotos de cosas pequeñas salen de ponerte abajo y acercarte. Mueve todo tu cuerpo, no solo el brazo, y prueba varios ángulos antes de tomar la foto.")
        + bullets([
            ("Ponte a su nivel:","arrodíllate, agáchate o pon el teléfono en el suelo para una vista real de insecto."),
            ("Llena el encuadre:","acércate para que la cosa pequeña sea la estrella, no algo perdido en un fondo grande."),
            ("Usa el modo macro o primer plano:","muchos teléfonos cambian a modo primer plano o macro cuando te acercas a un objeto. Toca la pantalla para fijar el enfoque en el detalle."),
            ("Mira donde nadie mira:","las esquinas, las grietas, la parte de abajo y el suelo están llenos de cosas pequeñas que pasamos por alto."),
        ]))
    es+=vocab_grid("En el Examen",
        "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el de mitad de semestre y el del final. Apr&eacute;ndelas ahora, no la noche anterior.",
        [("Macro","Una foto de primer plano extremo que hace que una cosa pequeña se vea grande y muestra detalles que tus ojos normalmente no ven, como el pelito de una abeja o los bultitos de una fresa."),
         ("Primer Plano","Una foto tomada muy cerca de tu tema para que la cosa pequeña llene casi todo el encuadre. Acercarte es la forma más fácil de hacer que una cosa pequeña se sienta importante."),
         ("Perspectiva","El lugar y el ángulo desde donde fotografías. Cambia tu perspectiva, como arrodillarte muy abajo, y un objeto común puede verse enorme."),
         ("Punto de Vista (POV)","Desde d&oacute;nde &lsquo;mira&rsquo; tu c&aacute;mara cuando tomas la foto. Un punto de vista bajo, como un insecto en el suelo, hace que las cosas pequeñas se sientan poderosas."),
         ("Vista de Gusano","Un ángulo muy bajo que mira hacia arriba a tu tema, como si estuvieras en el suelo como un gusano o un insecto. Es lo contrario de la vista de pájaro."),
         ("Profundidad de Campo","Cuánto de tu foto está en foco nítido. En un primer plano, muchas veces solo la cosa pequeña está nítida y el fondo se ve suave y borroso.")])

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Tiny Things | Photography 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Photography 1A &bull; Tiny Things","Tiny Things","Photograph your 6 tiny things.","#espanol","Clic para Espa&ntilde;ol")
    en+=capture_format("jpg")
    en+=deliverables_box(False,
        [("Your 6 photos (JPG),","all 6 tiny-thing captures, uploaded to this Canvas assignment.")])
    en+=card("STEP 01 / CAPTURE","Photograph 6 Tiny Things",
        float_right(STEP1_FLOAT,"A student crouching low to photograph a small object up close with a phone","")
        + para("Head outside or around the room and hunt for tiny things. Find 6 different small things we usually overlook and take a photo of each one. Move around and change your height for every photo: some down low like a bug, some up high, some at eye level.")
        + note_orange(FRESH_EN)
        + bullets([
            ("Six different things:","6 separate tiny things, not the same thing 6 times."),
            ("Change your angle:","get low for a bug&rsquo;s-eye view, up high, or at eye level. Move before you tap."),
            ("Get close and sharp:","fill the frame, use close-up or macro mode, and tap to focus so the detail is crisp."),
            ("Keep it simple:","no editing and no renaming. The photo straight from your device is fine."),
        ]))
    en+=card("TURN IT IN","Upload Your 6 Photos",
        para("Upload all 6 photos to Canvas. A photo straight from your phone or iPad (JPG) is perfect. Then go to Step 02 for the reflection."))

    es=banner("Fotograf&iacute;a 1A &bull; Cosas Peque&ntilde;as","Cosas Peque&ntilde;as","Fotograf&iacute;a tus 6 cosas peque&ntilde;as.","#top","Back to English")
    es+=capture_format("jpg", True)
    es+=deliverables_box(True,
        [("Tus 6 fotos (JPG),","las 6 capturas de cosas pequeñas, subidas a esta tarea de Canvas.")])
    es+=card("PASO 01 / CAPTURA","Fotograf&iacute;a 6 Cosas Peque&ntilde;as",
        float_right(STEP1_FLOAT,"Un estudiante agach&aacute;ndose para fotografiar de cerca un objeto peque&ntilde;o con un tel&eacute;fono","")
        + para("Sal afuera o camina por el salón y busca cosas pequeñas. Encuentra 6 cosas pequeñas diferentes que normalmente pasamos por alto y toma una foto de cada una. Muévete y cambia tu altura en cada foto: algunas muy abajo como un insecto, algunas arriba, algunas al nivel de los ojos.")
        + note_orange(FRESH_ES)
        + bullets([
            ("Seis cosas diferentes:","6 cosas pequeñas distintas, no la misma cosa 6 veces."),
            ("Cambia tu ángulo:","ponte abajo para una vista de insecto, arriba o al nivel de los ojos. Muévete antes de tomar la foto."),
            ("Acércate y que salga nítida:","llena el encuadre, usa el modo primer plano o macro y toca para enfocar para que el detalle salga claro."),
            ("Mántenlo simple:","sin edición y sin renombrar. La foto directa de tu dispositivo está bien."),
        ]))
    es+=card("ENTR&Eacute;GALO","Sube Tus 6 Fotos",
        para("Sube las 6 fotos a Canvas. Una foto directa de tu teléfono o iPad (JPG) es perfecta. Luego ve al Paso 02 para la reflexión."))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Tiny Things: Capture | Photography 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Photography 1A &bull; Tiny Things","Tiny Things","Reflect and pitch next week&rsquo;s challenge.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to Canvas.")])
    en+=card("STEP 02 / REFLECTION","Reflect on Your Tiny Things",
        float_right(REFLECT_FLOAT,"A student typing a short reflection on a lab computer","")
        + para("Finish with a short reflection. Tell which tiny thing was your favorite and why, name something small you usually overlook that you noticed this weekend, and pitch one idea for a fun photo challenge to try next weekend with your own device.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + para("Type your answers in the document, save it, and upload it to Canvas with your 6 photos."))

    es=banner("Fotograf&iacute;a 1A &bull; Cosas Peque&ntilde;as","Cosas Peque&ntilde;as","Reflexiona y propon el reto de la pr&oacute;xima semana.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word de reflexión completo (.docx), subido a Canvas.")])
    es+=card("PASO 02 / REFLEXI&Oacute;N","Reflexiona Sobre Tus Cosas Peque&ntilde;as",
        float_right(REFLECT_FLOAT,"Una estudiante escribiendo una reflexi&oacute;n corta en una computadora del laboratorio","")
        + para("Termina con una reflexión corta. Di cuál cosa pequeña fue tu favorita y por qué, nombra algo pequeño que normalmente pasas por alto y que notaste este fin de semana, y propon una idea para un reto de fotos divertido para probar el próximo fin de semana con tu propio dispositivo.")
        + note("El documento de reflexión está en la página de Resumen de este módulo, la primera página de este módulo. Si aún no lo has descargado, regresa y consíguelo. Antes de abrirlo, muévelo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + para("Escribe tus respuestas en el documento, gu&aacute;rdalo y súbelo a Canvas con tus 6 fotos."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
    return wrap_page("Tiny Things: Reflection | Photography 1A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
