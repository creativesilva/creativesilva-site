#!/usr/bin/env python3
# Photography 1A - Module: Composition Concepts.
# Watch a 20-concept video, pick 3 favorites, take one photo for each on your OWN DEVICE
# (phone or school iPad), then reflect. Own-device capture, so the banner wears the white
# your-device crown and the capture step + overview carry the orange fresh-photos note.
# Converted from the legacy hand-authored pages (eyebrow chips + right-side IDEYE icon +
# orange language toggle + <table> concept accordion) to the shared chip-header framework.
# All student copy (EN + ES) is preserved verbatim; only the chrome is rebuilt.
# Overview + 2 steps, bilingual EN/ES, 5th-grade.
import os
from silva_framework import *
import silva_framework as _sf
def banner(label,title,subtitle,es_href,es_label):
    # Composition Concepts is an own-device module: crown the banner with the white your-device icon.
    return _sf.banner(label,title,subtitle,es_href,es_label,HICON_YOUR_DEVICE)

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/photo1/composition-concepts"
HEADER=f"{IMG}/composition-concepts-header-v1.png"
VIDEO_THUMB=f"{IMG}/composition-video-thumb.png"
STEP1_FLOAT=f"{IMG}/composition-concepts-step01-float-v1.png"
REFLECT_FLOAT=f"{IMG}/reflection-float-v1.jpg"
VIMEO="https://vimeo.com/1115623437/f676128e30"
REFLECT_EN=f"{SITE}/assets/course-documents/Composition-Concepts-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Composition-Concepts-Reflection-ES.docx"
AREA="Photography Folder"

FRESH_EN="Fresh photos only. Do not use pictures already in your camera roll from before this class. Every photo must be planned and taken on purpose for this project. Be honest and turn in your own new work."
FRESH_ES="Solo fotos nuevas. No uses fotos que ya ten&iacute;as en tu galer&iacute;a de antes de esta clase. Cada foto debe ser planeada y tomada a prop&oacute;sito para este proyecto. S&eacute; honesto y entrega tu propio trabajo nuevo."

OVER="photo1-composition-concepts-overview.html"
S1="photo1-composition-concepts-step01-capture.html"
S2="photo1-composition-concepts-step02-reflection.html"

# ---- module-local helpers (no framework equivalent) ----
def downloads_block(es):
    # Orange Downloads section (Overview only). Composition Concepts holds the reflection doc.
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

def video_float(es):
    # Clickable, TEAL-framed video cover that floats right inside the teal content card (cohesion:
    # a content-card accent stays teal). Real CSS float so the full-width concept grid can sit below
    # it after a clear, matching the legacy layout. No caption in the source, so none added.
    alt="Haz Clic para Ver en Vimeo" if es else "Click to Watch on Vimeo"
    return (f'<a href="{VIMEO}" target="_blank" rel="noopener" style="text-decoration:none;display:block;float:right;width:28%;min-width:200px;margin:0 0 14px 22px;line-height:0;">'
      '<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;line-height:0;">'
      f'<img src="{VIDEO_THUMB}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div></a>')

# The 20 composition concepts, in video order.
# (en_name, es_name, timecode_label, seconds, en_desc, es_desc)
CONCEPTS=[
 ("Rule of Thirds","Regla de los Tercios","01:23","83",
  "Imagine your frame split into 9 equal boxes by two lines across and two lines down. Put your subject where the lines cross, not dead center, and the photo feels more balanced.",
  "Imagina tu encuadre dividido en 9 cuadros iguales por dos l&iacute;neas de lado a lado y dos de arriba abajo. Pon tu tema donde se cruzan las l&iacute;neas, no en el centro, y la foto se ve m&aacute;s equilibrada."),
 ("Strong Lines","L&iacute;neas Fuertes","02:02","122",
  "Look for clear, bold lines like a road edge, a fence, or the side of a building. Strong lines give your photo structure and hold the whole frame together.",
  "Busca l&iacute;neas claras y fuertes como el borde de una calle, una reja o el lado de un edificio. Las l&iacute;neas fuertes le dan estructura a tu foto y unen todo el encuadre."),
 ("Leading Lines","L&iacute;neas Gu&iacute;a","02:58","178",
  "Use lines that point toward your subject, like a path, a rail, or a row of trees. They guide the eye straight to the main thing in your photo.",
  "Usa l&iacute;neas que apunten hacia tu tema, como un camino, un riel o una fila de &aacute;rboles. Gu&iacute;an la mirada directo a lo m&aacute;s importante de tu foto."),
 ("Symmetry","Simetr&iacute;a","03:36","216",
  "Symmetry is when both halves of the frame match, like a building or a reflection in water. It makes a calm, clean, and balanced photo.",
  "La simetr&iacute;a es cuando las dos mitades del encuadre son iguales, como un edificio o un reflejo en el agua. Hace una foto tranquila, limpia y equilibrada."),
 ("Patterns","Patrones","04:13","253",
  "Patterns are shapes or colors that repeat, like tiles, windows, or steps. A clear pattern makes a photo feel neat and satisfying to look at.",
  "Los patrones son formas o colores que se repiten, como azulejos, ventanas o escalones. Un patr&oacute;n claro hace que la foto se vea ordenada y agradable."),
 ("Dynamic Diagonals","Diagonales Din&aacute;micas","04:55","295",
  "Diagonal lines run at an angle across the frame instead of flat. They add energy and make a still photo feel like it is moving.",
  "Las l&iacute;neas diagonales cruzan el encuadre en &aacute;ngulo en vez de planas. Dan energ&iacute;a y hacen que una foto fija se sienta en movimiento."),
 ("Frame in a Frame","Marco Dentro del Marco","05:38","338",
  "Use something in the scene, like a doorway, a window, or branches, to frame your subject. It adds depth and points the eye to the center.",
  "Usa algo de la escena, como una puerta, una ventana o unas ramas, para enmarcar tu tema. Da profundidad y dirige la mirada al centro."),
 ("Diminishing Perspectives","Perspectivas que Disminuyen","06:27","387",
  "This is when things look smaller as they move away from you, like poles or posts along a road. It gives your photo strong, real depth.",
  "Es cuando las cosas se ven m&aacute;s peque&ntilde;as al alejarse de ti, como postes a lo largo de una calle. Le da a tu foto una profundidad fuerte y real."),
 ("Strong Shapes","Formas Fuertes","07:23","443",
  "Look for bold, simple shapes like circles, triangles, or squares in your scene. A clear shape makes your subject stand out fast.",
  "Busca formas simples y fuertes como c&iacute;rculos, tri&aacute;ngulos o cuadrados en tu escena. Una forma clara hace que tu tema resalte r&aacute;pido."),
 ("Low Angle","&Aacute;ngulo Bajo","08:20","500",
  "Get down low and aim the camera up at your subject. A low angle makes things look big, tall, and powerful.",
  "Ag&aacute;chate y apunta la c&aacute;mara hacia arriba a tu tema. Un &aacute;ngulo bajo hace que las cosas se vean grandes, altas y con fuerza."),
 ("High Angle","&Aacute;ngulo Alto","09:13","553",
  "Hold the camera up high and aim it down at your subject. A high angle can make things look small or show a scene like a map.",
  "Sube la c&aacute;mara y ap&uacute;ntala hacia abajo a tu tema. Un &aacute;ngulo alto puede hacer que las cosas se vean peque&ntilde;as o mostrar la escena como un mapa."),
 ("Two Points of Interest","Dos Puntos de Inter&eacute;s","10:14","614",
  "Put two subjects in the frame that connect, like two people or two objects. The eye moves between them and starts to tell a story.",
  "Pon dos temas en el encuadre que se conecten, como dos personas o dos objetos. La mirada va de uno a otro y empieza a contar una historia."),
 ("The Power of Three","El Poder del Tres","11:08","668",
  "Groups of three feel balanced and pleasing to the eye. Try three subjects together, or line them up across the frame.",
  "Los grupos de tres se sienten equilibrados y agradables. Prueba tres temas juntos, o acom&oacute;dalos a lo largo del encuadre."),
 ("Negative Space","Espacio Negativo","12:13","733",
  "Negative space is the empty area around your subject. Leaving open space makes the subject pop and gives the photo a calm feel.",
  "El espacio negativo es el &aacute;rea vac&iacute;a alrededor de tu tema. Dejar espacio abierto hace que el tema resalte y le da calma a la foto."),
 ("Fill the Frame","Llenar el Encuadre","13:15","795",
  "Move in close so your subject fills the whole photo. This shows off detail and cuts out anything that distracts.",
  "Ac&eacute;rcate para que tu tema llene toda la foto. Esto muestra el detalle y quita lo que distrae."),
 ("Layering","Capas","14:24","864",
  "Build a front, a middle, and a back into your photo. Layers turn a flat picture into one that feels deep and real.",
  "Crea un frente, un medio y un fondo en tu foto. Las capas convierten una imagen plana en una que se siente profunda y real."),
 ("Multiple Points of Interest","M&uacute;ltiples Puntos de Inter&eacute;s","15:29","929",
  "Include a few subjects that each catch the eye. Done well, the eye travels around and explores the whole frame.",
  "Incluye varios temas que llamen la atenci&oacute;n. Bien hecho, la mirada recorre y explora todo el encuadre."),
 ("Center Focus","Enfoque Central","16:19","979",
  "Place your subject right in the middle of the frame. This works great for symmetry or for one strong, bold subject.",
  "Coloca tu tema justo en el centro del encuadre. Funciona muy bien para la simetr&iacute;a o para un tema fuerte y llamativo."),
 ("Triangular Formation","Formaci&oacute;n Triangular","17:14","1034",
  "Arrange your subjects so they form a triangle. Triangles feel stable and lead the eye around the photo.",
  "Acomoda tus temas para que formen un tri&aacute;ngulo. Los tri&aacute;ngulos se sienten estables y gu&iacute;an la mirada por la foto."),
 ("S-Curve","Curva en S","18:10","1090",
  "Look for a shape that curves like the letter S, like a winding road or river. An S-curve leads the eye smoothly through the photo.",
  "Busca una forma que se curve como la letra S, como un camino o un r&iacute;o sinuoso. Una curva en S gu&iacute;a la mirada suavemente por la foto."),
]

def concepts_grid(es):
    # TEAL collapsible concept accordion. Mirrors vocab_grid()'s <details> flex-wrap 2-column
    # structure, themed TEAL for content cohesion: teal gradient frame, dark-teal summary with the
    # 30px accent stripe, #5eead4 number. Each concept keeps its name (both languages), time code,
    # description, and the time-coded "watch at" jump link, verbatim.
    watch_word="Ver en " if es else "Watch at "
    items=""
    for n,(en_name,es_name,tc,sec,en_desc,es_desc) in enumerate(CONCEPTS,1):
        title = es_name if es else en_name
        sub   = en_name if es else es_name
        desc  = es_desc if es else en_desc
        items+=('<details style="flex:1 1 45%;min-width:260px;background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">'
          '<summary style="background:linear-gradient(135deg,#094043 0,#094043 30px,#041d1c 30px,#041d1c 100%);padding:12px 14px;cursor:pointer;">'
          f'<span style="font-size:12pt;color:#5eead4;"><strong>{n:02d}</strong></span> '
          f'<span style="font-size:12.5pt;color:#ffffff;"><strong>{title}</strong></span> '
          f'<span style="font-size:10.5pt;color:#80e0e0;"><strong>{tc}</strong></span>'
          f'<div style="font-size:10pt;color:rgba(255,255,255,0.6);margin-top:2px;">{sub}</div></summary>'
          f'<div style="padding:12px 14px 6px;font-size:11pt;line-height:1.55;color:rgba(255,255,255,0.85);">{desc}<div style="margin-top:8px;">'
          f'<a href="{VIMEO}#t={sec}s" target="_blank" rel="noopener" style="color:#5eead4;font-size:10.5pt;text-decoration:none;"><strong>{watch_word}{tc} &#8594;</strong></a>'
          '</div></div></details>')
    return f'<div style="display:flex;flex-wrap:wrap;gap:10px;align-items:flex-start;">{items}</div>'

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Composition Concepts</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 1A &bull; Composition Concepts","Composition Concepts","20 ways to frame a photo. Pick 3.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Composition Concepts",
        para("Composition is how you arrange what is in your photo. In this project you watch a short video that shows 20 composition concepts, pick your 3 favorites, and take one photo for each. This is not about camera settings: it is all about how you frame the photo. You use your own phone or a school iPad, so everyone has a fair and equal way to take part.")
        + framed(HEADER,"Composition Concepts")
        + note_orange(FRESH_EN))
    en+=downloads_block(False)
    en+=card("WATCH, THEN PICK 3","The 20 Composition Concepts",
        video_float(False)
        + para("Watch the whole video first: it walks through all 20 concepts in about 20 minutes. Click the image to watch it on Vimeo. Then pick any 3 of the 20 below. Tap a concept to open a short description, and use its time code to jump to that moment in the video and watch it in action. You will take one photo for each concept you choose.")
        + '<div style="margin-top:12px;">' + dl_link(VIMEO,"Watch on Vimeo",download=False) + '</div>'
        + '<div style="clear:both;"></div>'
        + concepts_grid(False))

    es=banner("Fotograf&iacute;a 1A &bull; Conceptos de Composici&oacute;n","Conceptos de Composici&oacute;n","20 formas de encuadrar una foto. Elige 3.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","Conceptos de Composici&oacute;n",
        para("La composici&oacute;n es c&oacute;mo acomodas lo que aparece en tu foto. En este proyecto ves un video corto que muestra 20 conceptos de composici&oacute;n, eliges tus 3 favoritos y tomas una foto para cada uno. Esto no se trata de los ajustes de la c&aacute;mara: se trata de c&oacute;mo encuadras la foto. Usas tu propio tel&eacute;fono o un iPad de la escuela, para que todos tengan una forma justa e igual de participar.")
        + framed(HEADER,"Conceptos de Composici&oacute;n")
        + note_orange(FRESH_ES))
    es+=downloads_block(True)
    es+=card("MIRA, LUEGO ELIGE 3","Los 20 Conceptos de Composici&oacute;n",
        video_float(True)
        + para("Mira todo el video primero: muestra los 20 conceptos en unos 20 minutos. Haz clic en la imagen para verlo en Vimeo. Luego elige 3 de los 20 de abajo. Toca un concepto para abrir una descripci&oacute;n corta, y usa su tiempo para saltar a ese momento del video y verlo en acci&oacute;n. Tomar&aacute;s una foto para cada concepto que elijas.")
        + '<div style="margin-top:12px;">' + dl_link(VIMEO,"Ver en Vimeo",download=False) + '</div>'
        + '<div style="clear:both;"></div>'
        + concepts_grid(True))

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Composition Concepts | Photography 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Photography 1A &bull; Composition Concepts","Composition Concepts","Capture your 3 concepts.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("Your 3 final photos (JPG),","uploaded to this Canvas assignment.")])
    en+=card("STEP 01 / CAPTURE &amp; CULL","Capture Your 3 Concepts",
        float_right(STEP1_FLOAT,"A student reviewing her photos on a phone","")
        + para("Go take photos for each of your 3 chosen concepts with your own phone or a school iPad. Take a few tries for each one, then select your single best photo for each concept. You end with 3 photos, one for each concept, and all 3 are different.")
        + note_orange(FRESH_EN)
        + bullets([
            ("Take a few tries:","photograph each concept more than once, then keep the best."),
            ("One per concept:","your 3 final photos must each show a different concept."),
            ("Keep it simple:","no editing, no file renaming, and no contact sheet. The photo straight from your device is fine."),
        ]))
    en+=card("TURN IT IN","Upload Your 3 Photos",
        para("Upload your 3 final photos to Canvas. A photo straight from your phone or iPad (JPG) is perfect. Then go to Step 02 for the reflection."))

    es=banner("Fotograf&iacute;a 1A &bull; Conceptos de Composici&oacute;n","Conceptos de Composici&oacute;n","Captura tus 3 conceptos.","#top","Back to English")
    es+=deliverables_box(True,
        [("Tus 3 fotos finales (JPG),","subidas a esta tarea de Canvas.")])
    es+=card("PASO 01 / CAPTURA Y SELECCI&Oacute;N","Captura Tus 3 Conceptos",
        float_right(STEP1_FLOAT,"Una estudiante revisando sus fotos en un tel&eacute;fono","")
        + para("Ve a tomar fotos para cada uno de tus 3 conceptos elegidos con tu propio tel&eacute;fono o un iPad de la escuela. Haz varios intentos de cada uno y luego elige tu mejor foto para cada concepto. Terminas con 3 fotos, una por cada concepto, y las 3 son diferentes.")
        + note_orange(FRESH_ES)
        + bullets([
            ("Haz varios intentos:","toma cada concepto m&aacute;s de una vez y qu&eacute;date con la mejor."),
            ("Una por concepto:","tus 3 fotos finales deben mostrar cada una un concepto diferente."),
            ("M&aacute;ntenlo simple:","sin edici&oacute;n, sin renombrar archivos y sin hoja de contactos. La foto directa de tu dispositivo est&aacute; bien."),
        ]))
    es+=card("ENTR&Eacute;GALO","Sube Tus 3 Fotos",
        para("Sube tus 3 fotos finales a Canvas. Una foto directa de tu tel&eacute;fono o iPad (JPG) es perfecta. Luego ve al Paso 02 para la reflexi&oacute;n."))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Composition Concepts: Capture | Photography 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Photography 1A &bull; Composition Concepts","Composition Concepts","Reflect on your work.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("3 photos:","one for each concept, all different (from Step 01)."),
         ("1 reflection:","the completed Word document (.docx).")])
    en+=card("STEP 02 / REFLECTION","Reflect on Your 3 Photos",
        float_right(REFLECT_FLOAT,"A student typing the Composition Concepts reflection on a lab computer","")
        + para("Finish the project with a short reflection. Name the 3 concepts you chose, then tell which one was the hardest, which was your favorite, and what you learned about composition.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + para("Type your answers in the document, save it, and upload it to Canvas with your 3 photos."))

    es=banner("Fotograf&iacute;a 1A &bull; Conceptos de Composici&oacute;n","Conceptos de Composici&oacute;n","Reflexiona sobre tu trabajo.","#top","Back to English")
    es+=deliverables_box(True,
        [("3 fotos:","una para cada concepto, todas diferentes (del Paso 01)."),
         ("1 reflexi&oacute;n:","el documento de Word completo (.docx).")])
    es+=card("PASO 02 / REFLEXI&Oacute;N","Reflexiona Sobre Tus 3 Fotos",
        float_right(REFLECT_FLOAT,"Una estudiante escribiendo la reflexi&oacute;n de Conceptos de Composici&oacute;n en una computadora del laboratorio","")
        + para("Termina el proyecto con una reflexi&oacute;n corta. Nombra los 3 conceptos que elegiste, luego di cu&aacute;l fue el m&aacute;s dif&iacute;cil, cu&aacute;l fue tu favorito y qu&eacute; aprendiste sobre la composici&oacute;n.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + para("Escribe tus respuestas en el documento, gu&aacute;rdalo y s&uacute;belo a Canvas con tus 3 fotos."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
    return wrap_page("Composition Concepts: Reflection | Photography 1A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
