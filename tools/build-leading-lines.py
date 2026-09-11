#!/usr/bin/env python3
# Photography 1A - Module 03: Leading Lines Photo Walk.
# Followup to Composition Concepts. In-class photo walk, shared class cameras (2 per camera),
# each partner takes 3 leading-line examples, swap, cull to best 6 (3 own + 3 partner), JPG only.
# Chip-header framework via silva_framework. Overview + 2 steps, bilingual EN/ES, 5th-grade.
import os, re
from silva_framework import *
import silva_framework as _sf
def banner(label,title,subtitle,es_href,es_label):
    # Leading Lines is a photo walk: crown the banner with the white photo-walk icon.
    return _sf.banner(label,title,subtitle,es_href,es_label,HICON_PHOTO_WALK)

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/photo1/leading-lines"
HEADER=f"{IMG}/leading-lines-header-v1.jpg"
FLOAT=f"{IMG}/leading-lines-step01-float-v1.jpg"
ARTICLE="https://digital-photography-school.com/how-to-use-leading-lines-for-better-compositions/"
REFLECT_EN=f"{SITE}/assets/course-documents/Leading-Lines-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Leading-Lines-Reflection-ES.docx"
AREA="Photography Folder"

OVER="photo1-leading-lines-overview.html"
S1="photo1-leading-lines-step01-capture.html"
S2="photo1-leading-lines-step02-reflection.html"

def downloads_block(es):
    # Orange Downloads section (Overview only). Leading Lines holds the reflection doc.
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
            f'        <a href="{OVER}" class="bc-hide-sm">Leading Lines</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 1A &bull; Leading Lines","Leading Lines Photo Walk","Pair up, take leading-line photos, and cull your best six.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Leading Lines on the Walk",
        para("On this photo walk you and a partner hunt for leading lines: lines that pull your eye through a photo toward the subject. You share one class camera, two students per camera. Each of you takes 3 different examples of leading lines. Then you swap photos, cull your best, and turn in 6 photos in all.")
        + framed(HEADER,"Two Pioneer Valley students on a photo walk, one holding a Canon camera, outside the Academy of Arts building"))
    en+=downloads_block(False)
    en+=card("THE CONCEPT / WHAT TO LOOK FOR","How Leading Lines Work",
        para("A leading line is any line that guides your eye through the photo. It can be a road, a fence, a hallway, a row of lockers, a shadow, or a crack in the sidewalk. Strong leading lines often run from the front of the photo toward the subject in the back.")
        + para("Sometimes the lines seem to meet at one spot far away. That spot is the vanishing point. Lines that head toward a vanishing point add depth and make a flat photo feel three-dimensional."))
    en+=resources_card("Leading Lines Guide",
        para("Want more examples? This short guide shows leading lines and vanishing points in real photos.")
        + '<div style="margin-top:6px;">' + reslink(ARTICLE,"Read the Leading Lines Guide") + '</div>', False)
    en+=card("HOW IT WORKS / YOU AND YOUR PARTNER","Work as a Pair",
        bullets([
            ("Pair up:","two students share one class camera."),
            ("Take:","each person takes 3 different examples of leading lines. Different lines, different spots, not the same photo twice."),
            ("Share:","swap your photos so each partner has the other&rsquo;s 3 examples."),
            ("Cull:","select the single best photo of each example. You keep your best 3 and your partner&rsquo;s best 3."),
            ("Submit:","turn in 6 photos in all (your 3 plus your partner&rsquo;s 3)."),
        ])
        + note("You take photos as JPG. You will not edit them, so get the photo right in the camera."))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Leading Lines","Lines that guide your eye through a photo toward the subject."),
           ("Cull","To look through your photos and keep only the best ones."),
           ("Take","A photographer&rsquo;s take is all the images they take for one session, gig, or project. A wedding take can be several thousand images."),
           ("Composition","How you arrange everything inside the frame."),
           ("JPG","A common photo file that is ready to share without editing."),
           ("Vanishing Point","The spot far away where leading lines seem to meet.")]), False)

    es=banner("Fotograf&iacute;a 1A &bull; L&iacute;neas Gu&iacute;a","Caminata de L&iacute;neas Gu&iacute;a","Trabaja en pareja, toma fotos de l&iacute;neas gu&iacute;a y selecciona tus mejores seis.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","L&iacute;neas Gu&iacute;a en la Caminata",
        para("En esta caminata fotogr&aacute;fica t&uacute; y un compa&ntilde;ero buscan l&iacute;neas gu&iacute;a: l&iacute;neas que llevan tu mirada a trav&eacute;s de la foto hacia el sujeto. Comparten una c&aacute;mara de la clase, dos estudiantes por c&aacute;mara. Cada uno toma 3 ejemplos diferentes de l&iacute;neas gu&iacute;a. Luego intercambian fotos, seleccionan sus mejores y entregan 6 fotos en total.")
        + framed(HEADER,"Dos estudiantes de Pioneer Valley en una caminata fotogr&aacute;fica, uno con una c&aacute;mara Canon, afuera del edificio Academy of Arts"))
    es+=downloads_block(True)
    es+=card("EL CONCEPTO / QU&Eacute; BUSCAR","C&oacute;mo Funcionan las L&iacute;neas Gu&iacute;a",
        para("Una l&iacute;nea gu&iacute;a es cualquier l&iacute;nea que lleva tu mirada a trav&eacute;s de la foto. Puede ser un camino, una reja, un pasillo, una fila de casilleros, una sombra o una grieta en la acera. Las l&iacute;neas gu&iacute;a fuertes suelen ir desde el frente de la foto hacia el sujeto al fondo.")
        + para("A veces las l&iacute;neas parecen unirse en un solo punto a lo lejos. Ese punto es el punto de fuga. Las l&iacute;neas que van hacia un punto de fuga dan profundidad y hacen que una foto plana se sienta tridimensional."))
    es+=resources_card("Gu&iacute;a de L&iacute;neas Gu&iacute;a",
        para("&iquest;Quieres m&aacute;s ejemplos? Esta gu&iacute;a corta muestra l&iacute;neas gu&iacute;a y puntos de fuga en fotos reales.")
        + '<div style="margin-top:6px;">' + reslink(ARTICLE,"Lee la Gu&iacute;a de L&iacute;neas Gu&iacute;a") + '</div>', True)
    es+=card("C&Oacute;MO FUNCIONA / T&Uacute; Y TU COMPA&Ntilde;ERO","Trabaja en Pareja",
        bullets([
            ("Formen pareja:","dos estudiantes comparten una c&aacute;mara de la clase."),
            ("Toma:","cada persona toma 3 ejemplos diferentes de l&iacute;neas gu&iacute;a. L&iacute;neas distintas, lugares distintos, no la misma foto dos veces."),
            ("Comparte:","intercambien sus fotos para que cada uno tenga los 3 ejemplos del otro."),
            ("Selecciona (cull):","elige la mejor foto de cada ejemplo. Te quedas con tus mejores 3 y los mejores 3 de tu compa&ntilde;ero."),
            ("Entrega:","entrega 6 fotos en total (tus 3 m&aacute;s los 3 de tu compa&ntilde;ero)."),
        ])
        + note("Tomas las fotos en JPG. No las vas a editar, as&iacute; que logra la foto bien desde la c&aacute;mara."))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Leading Lines (L&iacute;neas Gu&iacute;a)","L&iacute;neas que llevan tu mirada a trav&eacute;s de la foto hacia el sujeto."),
           ("Cull (Seleccionar)","Revisar tus fotos y quedarte solo con las mejores."),
           ("Take (Toma Completa)","El take de un fot&oacute;grafo son todas las im&aacute;genes que toma para una sesi&oacute;n, trabajo o proyecto. El take de una boda puede tener varios miles de im&aacute;genes."),
           ("Composition (Composici&oacute;n)","C&oacute;mo acomodas todo dentro del encuadre."),
           ("JPG","Un archivo de foto com&uacute;n, listo para compartir sin editar."),
           ("Vanishing Point (Punto de Fuga)","El punto a lo lejos donde las l&iacute;neas gu&iacute;a parecen unirse.")]), True)

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Leading Lines Photo Walk | Photography 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Leading Lines &bull; Step 1","Capture, Cull &amp; Submit","Take your leading lines, then select your best six.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("6 JPGs:","your best 3 leading-line photos and your partner&rsquo;s best 3, uploaded to this Canvas assignment.")])
    en+=card("CAPTURE / ON THE WALK","Take Your Leading Lines",
        float_right(FLOAT,"A student kneeling to photograph down a long covered walkway whose columns lead the eye to a vanishing point, while a partner watches","Hunting leading lines on the walk.")
        + para("Pair up and share one class camera, two students per camera. Set the camera to JPG. Then walk campus and hunt for leading lines.")
        + bullets([
            ("Take 3 examples:","each of you takes 3 different examples of leading lines."),
            ("Make each different:","a different line and a different spot each time."),
            ("Get it right in camera:","you will not edit these, so frame it well and check the photo."),
            ("Take a few extra:","take a couple of extra photos of each example so you have choices when you cull."),
        ]))
    en+=card("SHARE / WITH YOUR PARTNER","Swap Your Photos",
        para("When you both finish, share your photos so each of you has all of them: your 3 examples and your partner&rsquo;s 3 examples.")
        + bullets([
            ("Import first:","bring the camera to a computer and import the photos."),
            ("Share both sets:","give your partner your photos and get theirs, so you each have all six examples as JPGs."),
        ]))
    en+=card("CULL / SELECT YOUR BEST","Cull to Your Best 6",
        para("Now cull. Culling means looking through your photos and keeping only the best. For each example, select the single strongest photo.")
        + bullets([
            ("Your 3:","keep your best photo of each of your 3 examples."),
            ("Your partner&rsquo;s 3:","keep the best photo of each of your partner&rsquo;s 3 examples."),
            ("6 in all:","that is 6 photos, 3 of yours and 3 of your partner&rsquo;s."),
        ]))

    es=banner("L&iacute;neas Gu&iacute;a &bull; Paso 1","Captura, Selecciona y Entrega","Toma tus l&iacute;neas gu&iacute;a y luego elige tus mejores seis.","#top","Back to English")
    es+=deliverables_box(True,
        [("6 JPG:","tus mejores 3 fotos de l&iacute;neas gu&iacute;a y las mejores 3 de tu compa&ntilde;ero, subidas a esta tarea de Canvas.")])
    es+=card("CAPTURA / EN LA CAMINATA","Toma Tus L&iacute;neas Gu&iacute;a",
        float_right(FLOAT,"Un estudiante arrodillado fotografiando por un pasillo largo cuyas columnas gu&iacute;an la mirada hacia un punto de fuga, mientras un compa&ntilde;ero observa","Buscando l&iacute;neas gu&iacute;a en la caminata.")
        + para("Formen pareja y compartan una c&aacute;mara de la clase, dos estudiantes por c&aacute;mara. Pon la c&aacute;mara en JPG. Luego caminen por la escuela y busquen l&iacute;neas gu&iacute;a.")
        + bullets([
            ("Toma 3 ejemplos:","cada uno toma 3 ejemplos diferentes de l&iacute;neas gu&iacute;a."),
            ("Haz cada uno distinto:","una l&iacute;nea distinta y un lugar distinto cada vez."),
            ("Logra la foto en la c&aacute;mara:","no vas a editarlas, as&iacute; que encuadra bien y revisa la foto."),
            ("Toma algunas de m&aacute;s:","toma un par de fotos extra de cada ejemplo para tener opciones al seleccionar."),
        ]))
    es+=card("COMPARTE / CON TU COMPA&Ntilde;ERO","Intercambien Sus Fotos",
        para("Cuando ambos terminen, compartan sus fotos para que cada uno tenga todas: tus 3 ejemplos y los 3 ejemplos de tu compa&ntilde;ero.")
        + bullets([
            ("Importa primero:","lleva la c&aacute;mara a una computadora e importa las fotos."),
            ("Compartan ambos grupos:","dale a tu compa&ntilde;ero tus fotos y recibe las suyas, para que cada uno tenga los seis ejemplos en JPG."),
        ]))
    es+=card("SELECCIONA / ELIGE TUS MEJORES","Selecciona (Cull) Tus Mejores 6",
        para("Ahora selecciona (cull). Seleccionar significa revisar tus fotos y quedarte solo con las mejores. Para cada ejemplo, elige la foto m&aacute;s fuerte.")
        + bullets([
            ("Tus 3:","qu&eacute;date con tu mejor foto de cada uno de tus 3 ejemplos."),
            ("Los 3 de tu compa&ntilde;ero:","qu&eacute;date con la mejor foto de cada uno de los 3 ejemplos de tu compa&ntilde;ero."),
            ("6 en total:","son 6 fotos, 3 tuyas y 3 de tu compa&ntilde;ero."),
        ]))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Capture, Cull and Submit | Leading Lines | Photography 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Leading Lines &bull; Step 2","Turn In Your Reflection","Reflect on the walk, your partner, and your photos.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), with your partner named, uploaded to this Canvas assignment.")])
    en+=card("STEP 02 / REFLECT","Complete and Upload the Reflection",
        para("Finish with a short reflection. It asks you to name your partner, explain what leading lines are, tell how you culled, and select your favorite photo.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + bullets([
            ("Open it:","open the reflection Word document (.docx) from your project folder."),
            ("Name your partner:","write your partner&rsquo;s full name where it asks."),
            ("Answer every question:","type your answers in the boxes, in full sentences."),
            ("Save and upload:","save the document and upload it to this Canvas assignment."),
        ])
        + note("Answer honestly, in your own words."))

    es=banner("L&iacute;neas Gu&iacute;a &bull; Paso 2","Entrega Tu Reflexi&oacute;n","Reflexiona sobre la caminata, tu compa&ntilde;ero y tus fotos.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n, con el nombre de tu compa&ntilde;ero, subido a esta tarea de Canvas.")])
    es+=card("PASO 02 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        para("Termina con una reflexi&oacute;n corta. Te pide el nombre de tu compa&ntilde;ero, explicar qu&eacute; son las l&iacute;neas gu&iacute;a, contar c&oacute;mo seleccionaste (cull) y elegir tu foto favorita.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + bullets([
            ("&Aacute;brelo:","abre el documento de Word (.docx) de la reflexi&oacute;n desde tu carpeta del proyecto."),
            ("Nombra a tu compa&ntilde;ero:","escribe el nombre completo de tu compa&ntilde;ero donde lo pide."),
            ("Contesta cada pregunta:","escribe tus respuestas en los cuadros, en oraciones completas."),
            ("Guarda y sube:","guarda el documento y s&uacute;belo a esta tarea de Canvas."),
        ])
        + note("Contesta con honestidad, en tus propias palabras."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
    return wrap_page("Step 2: Reflection | Leading Lines | Photography 1A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
