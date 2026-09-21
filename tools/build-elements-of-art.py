#!/usr/bin/env python3
# Digital Arts 1A - Module 06: Elements of Art: Character Design.
# Introduces the FIRST TWO Elements of Art (Line and Shape). Students design an ORIGINAL character
# (not a copy of an existing character) using ONLY black-and-white lines and shapes, no color /
# texture / form yet; sketch it, finalize it with clean crisp black lines, and give it an original
# name (Step 01, turn in one photo). Step 02 is a short reflection looking ahead to Form and Color.
# The last page foreshadows the next module (Form & Color, building toward all 7 Elements).
# Current standard: new header (Module NN in the title), deliverables AFTER the teal content, a
# foreshadow segue. Overview + 2 steps, bilingual EN/ES, 5th-grade. Uses the shared silva_framework.
import os
from silva_framework import *

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/digarts1/elements-of-art"
HEADER=f"{IMG}/elements-of-art-header-v1.jpg"
STEP1_FLOAT=f"{IMG}/elements-of-art-step01-float-v1.jpg"
REFLECT_FLOAT=f"{IMG}/elements-of-art-reflection-float-v1.jpg"
DOCS=f"{SITE}/assets/course-documents"
REFL_EN=f"{DOCS}/Elements-of-Art-Reflection-EN.docx"
REFL_ES=f"{DOCS}/Elements-of-Art-Reflection-ES.docx"
AREA="Digital Arts Folder"
MOD="06"
NXT="07"

OVER="digarts1-elements-of-art-overview.html"
S1="digarts1-elements-of-art-step01-draw.html"
S2="digarts1-elements-of-art-step02-reflection.html"

ORIG_EN="Original work only. Your character must be your own idea, not a copy of a character that already exists (no SpongeBob, no anime, game, or movie characters). Use your imagination and make something new."
ORIG_ES="Solo trabajo original. Tu personaje debe ser tu propia idea, no una copia de un personaje que ya existe (nada de Bob Esponja, ni personajes de anime, videojuegos o pel&iacute;culas). Usa tu imaginaci&oacute;n y crea algo nuevo."

EOA_STANDARDS=[
  {"code":"DGA.17.1","en_tier":"Design &amp; Graphic Arts","es_tier":"Dise&ntilde;o y Artes Gr&aacute;ficas",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You use the first two Elements of Art, line and shape, on purpose to build an original character.",
   "es_desc":"Usas los primeros dos Elementos del Arte, la l&iacute;nea y la forma, a prop&oacute;sito para construir un personaje original."},
  {"code":"DGA.17.3","en_tier":"Design &amp; Graphic Arts","es_tier":"Dise&ntilde;o y Artes Gr&aacute;ficas",
   "en_title":"Visual Communication","es_title":"Comunicaci&oacute;n Visual",
   "en_desc":"You design an original character with its own look using only lines and shapes.",
   "es_desc":"Dise&ntilde;as un personaje original con su propio estilo usando solo l&iacute;neas y formas."},
  {"code":"DGA.17.5","en_tier":"Design &amp; Graphic Arts","es_tier":"Dise&ntilde;o y Artes Gr&aacute;ficas",
   "en_title":"Craftsmanship &amp; Production","es_title":"Elaboraci&oacute;n y Producci&oacute;n",
   "en_desc":"You take your character from a rough sketch to a finished drawing with clean, crisp black lines.",
   "es_desc":"Llevas tu personaje de un boceto a un dibujo terminado con l&iacute;neas negras limpias y n&iacute;tidas."},
  {"code":"DGA.17.9","en_tier":"Design &amp; Graphic Arts","es_tier":"Dise&ntilde;o y Artes Gr&aacute;ficas",
   "en_title":"Critique &amp; Reflection","es_title":"Cr&iacute;tica y Reflexi&oacute;n",
   "en_desc":"You look at your work and plan what to add next: form, color, and texture.",
   "es_desc":"Revisas tu trabajo y planeas qu&eacute; agregar despu&eacute;s: forma, color y textura."},
]

VOCAB_EN=[
 ("Elements of Art","The building blocks artists use to make any artwork. There are 7: line, shape, form, space, value, color, and texture. This module uses the first two."),
 ("Line","A mark that travels from one point to another. Lines can be straight, curved, wavy, zigzag, thick, or thin. Every drawing starts with lines."),
 ("Shape","A flat, closed area you get when a line connects back to itself. Shapes are 2D (flat): they have length and width, but no depth."),
 ("Geometric Shape","A shape with clean, exact edges and a math name, like a circle, square, triangle, or rectangle."),
 ("Organic Shape","A free, natural, curvy shape that has no perfect math name, like a puddle, a leaf, or a blob."),
 ("Contour Line","A line that follows the outer edge, or outline, of a shape or object to show what it looks like."),
]
VOCAB_ES=[
 ("Elementos del Arte","Las piezas b&aacute;sicas que los artistas usan para crear cualquier obra. Son 7: l&iacute;nea, forma, volumen, espacio, valor, color y textura. Este m&oacute;dulo usa los primeros dos."),
 ("L&iacute;nea","Una marca que va de un punto a otro. Las l&iacute;neas pueden ser rectas, curvas, onduladas, en zigzag, gruesas o delgadas. Todo dibujo empieza con l&iacute;neas."),
 ("Forma","Un &aacute;rea plana y cerrada que se crea cuando una l&iacute;nea se une consigo misma. Las formas son 2D (planas): tienen largo y ancho, pero no profundidad."),
 ("Forma Geom&eacute;trica","Una forma con bordes limpios y exactos y un nombre matem&aacute;tico, como un c&iacute;rculo, un cuadrado, un tri&aacute;ngulo o un rect&aacute;ngulo."),
 ("Forma Org&aacute;nica","Una forma libre, natural y curva que no tiene un nombre matem&aacute;tico exacto, como un charco, una hoja o una mancha."),
 ("L&iacute;nea de Contorno","Una l&iacute;nea que sigue el borde exterior, o el contorno, de una forma u objeto para mostrar c&oacute;mo se ve."),
]

def downloads_block(es):
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga aqu&iacute; todo lo que necesitas para este m&oacute;dulo. Consigue tus archivos antes de empezar." if es
          else "Download everything you need for this module here. Get your files before you start.")
    reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
    ref=REFL_ES if es else REFL_EN
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ref,reflabel,row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

def nav(current, dots, stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Elements of Art</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Digital Arts 1A",f"Module {MOD}: Elements of Art, Character Design","Meet the first two Elements of Art: Line and Shape.","#espanol","Clic para Espa&ntilde;ol", HICON_SKETCH)
    en+=type_card("overview","The Module Overview","Design a Character from Line &amp; Shape",
        para("Welcome to the Elements of Art. Artists build every drawing from 7 simple building blocks called the Elements of Art. In this module you meet the first two: <strong>Line</strong> and <strong>Shape</strong>. Your job is to design your very own original character using only lines and shapes, in black and white. No color, no texture, no shading yet: just line and shape. The rest come later.")
        + framed(HEADER,"A Pioneer Valley student in the Academy of Arts lab sketching an original character in a sketchbook, with a screen showing the 7 Elements of Art")
        + para("Your character must be YOUR idea. Do not copy a character that already exists. Use your imagination, make something new, and give it an original name.")
        + note_orange(ORIG_EN))
    en+=standards_box(False, EOA_STANDARDS)
    en+=downloads_block(False)
    en+=card("THE FIRST 2 ELEMENTS","Meet Line &amp; Shape",
        para("Line and shape are the foundation of every drawing. Get these two right and everything else you learn will build on top of them.")
        + bullets([
            ("Line:","a mark that travels from one point to another. Lines can be straight, curved, wavy, zigzag, thick, or thin."),
            ("Shape:","when a line connects back to itself it makes a shape. Shapes are flat (2D): length and width, but no depth."),
            ("Geometric vs organic:","geometric shapes have clean edges and math names (circle, square, triangle). Organic shapes are free and natural, like a puddle or a leaf. A good character mixes both."),
            ("Build with shapes:","most characters start as simple shapes (a circle for a head, ovals for arms), then lines add the face and details."),
        ]))
    en+=card("YOUR CHALLENGE","Design One Original Character",
        para("Design a single original character using only lines and shapes. Think about which shapes make its head, body, arms, and legs, then use lines for the face and small details. Keep it black and white for now.")
        + bullets([
            ("Original only:","your own idea, never a copy of an existing character."),
            ("Lines and shapes only:","no color, texture, or shading yet."),
            ("Build from shapes:","start with simple shapes, then add lines."),
            ("Name it:","give your character an original name."),
        ]))
    en+=resources_card("Key Words", vocab_grid("On the Quiz",
        "Heads up: these key words will show up on your quizzes. Learn them now, not the night before.",
        VOCAB_EN), False)
    en+=next_up("UP NEXT &middot; STEP 01 - Draw Your Character","Grab your sketchbook and a pencil. Next you&rsquo;ll sketch, finalize, and name your original character.")

    es=banner("Arte Digital 1A",f"M&oacute;dulo {MOD}: Elementos del Arte, Dise&ntilde;o de Personaje","Conoce los primeros dos Elementos del Arte: la L&iacute;nea y la Forma.","#top","Back to English", HICON_SKETCH)
    es+=type_card("overview","El Resumen del M&oacute;dulo","Dise&ntilde;a un Personaje con L&iacute;nea y Forma",
        para("Bienvenido a los Elementos del Arte. Los artistas construyen todo dibujo a partir de 7 piezas b&aacute;sicas llamadas los Elementos del Arte. En este m&oacute;dulo conoces los primeros dos: la <strong>L&iacute;nea</strong> y la <strong>Forma</strong>. Tu trabajo es dise&ntilde;ar tu propio personaje original usando solo l&iacute;neas y formas, en blanco y negro. Nada de color, textura ni sombras todav&iacute;a: solo l&iacute;nea y forma. Lo dem&aacute;s viene despu&eacute;s.")
        + framed(HEADER,"Un estudiante de Pioneer Valley en el laboratorio de la Academia de Artes dibujando un personaje original en un cuaderno, con una pantalla que muestra los 7 Elementos del Arte")
        + para("Tu personaje debe ser TU idea. No copies un personaje que ya existe. Usa tu imaginaci&oacute;n, crea algo nuevo y dale un nombre original.")
        + note_orange(ORIG_ES))
    es+=standards_box(True, EOA_STANDARDS)
    es+=downloads_block(True)
    es+=card("LOS PRIMEROS 2 ELEMENTOS","Conoce la L&iacute;nea y la Forma",
        para("La l&iacute;nea y la forma son la base de todo dibujo. Si dominas estas dos, todo lo dem&aacute;s que aprendas se construir&aacute; sobre ellas.")
        + bullets([
            ("L&iacute;nea:","una marca que va de un punto a otro. Las l&iacute;neas pueden ser rectas, curvas, onduladas, en zigzag, gruesas o delgadas."),
            ("Forma:","cuando una l&iacute;nea se une consigo misma crea una forma. Las formas son planas (2D): largo y ancho, pero sin profundidad."),
            ("Geom&eacute;trica vs org&aacute;nica:","las formas geom&eacute;tricas tienen bordes limpios y nombres matem&aacute;ticos (c&iacute;rculo, cuadrado, tri&aacute;ngulo). Las org&aacute;nicas son libres y naturales, como un charco o una hoja. Un buen personaje mezcla ambas."),
            ("Construye con formas:","la mayor&iacute;a de los personajes empiezan como formas simples (un c&iacute;rculo para la cabeza, &oacute;valos para los brazos) y luego las l&iacute;neas agregan la cara y los detalles."),
        ]))
    es+=card("TU RETO","Dise&ntilde;a Un Personaje Original",
        para("Dise&ntilde;a un solo personaje original usando solo l&iacute;neas y formas. Piensa qu&eacute; formas hacen su cabeza, cuerpo, brazos y piernas, y luego usa l&iacute;neas para la cara y los detalles peque&ntilde;os. Mantenlo en blanco y negro por ahora.")
        + bullets([
            ("Solo original:","tu propia idea, nunca una copia de un personaje que ya existe."),
            ("Solo l&iacute;neas y formas:","sin color, textura ni sombras todav&iacute;a."),
            ("Construye con formas:","empieza con formas simples y luego agrega l&iacute;neas."),
            ("Ponle nombre:","dale a tu personaje un nombre original."),
        ]))
    es+=resources_card("Palabras Clave", vocab_grid("En el Examen",
        "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes. Apr&eacute;ndelas ahora, no la noche anterior.",
        VOCAB_ES), True)
    es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 01 - Dibuja Tu Personaje","Toma tu cuaderno y un l&aacute;piz. Ahora vas a bocetar, finalizar y nombrar tu personaje original.")

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Elements of Art, Character Design | Digital Arts 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner(f"Module {MOD} &bull; Step 01","Draw Your Character","Sketch it, finalize it, name it.","#espanol","Clic para Espa&ntilde;ol", HICON_SKETCH)
    en+=card("STEP 01 / DRAW","Sketch, Finalize &amp; Name Your Character",
        float_right(STEP1_FLOAT,"A student photographing a finished sketchbook character named Blobby with an iPad","A finished character, drawn with clean lines and simple shapes, ready to photograph and turn in.")
        + para("Grab your sketchbook and a pencil. Start by lightly sketching your character using only simple shapes: maybe a circle for the head, an oval for the body, and lines for the arms and legs. Move things around until you like how it looks, then add lines for the face and small details.")
        + para("When you are happy with your character, lock in your lines. Take it from a rough sketch to a finished drawing with sharp, crisp, clean black lines. If you want to redraw a clean final version on a fresh page, that is fine.")
        + bullets([
            ("Shapes first:","block in the body with simple shapes, then add your lines."),
            ("Original only:","your own character, never a copy of an existing one."),
            ("Lines and shapes only:","black and white, no color or shading yet."),
            ("Clean it up:","finish with sharp, clean black lines."),
            ("Name it:","give your character an original name."),
        ])
        + note_orange(ORIG_EN))
    en+=deliverables_box(False,
        [("1 photo (JPG),","a clear photo of your finished, named character drawing, uploaded to this Canvas assignment.")])
    en+=card("TURN IT IN","Photograph and Upload Your Character",
        para("When your character is finished and named, take a clean, clear photo of your sketchbook page with your school iPad. Use good light, hold the iPad straight above the page, and avoid glare. Upload the photo (JPG) to this Canvas assignment. Then go to Step 02 for the reflection.")
        + note("Be honest and turn in your own original work."))
    en+=next_up("UP NEXT &middot; STEP 02 - Reflection","With your character turned in, you&rsquo;ll reflect on what to add next: color, form, and texture.")

    es=banner(f"M&oacute;dulo {MOD} &bull; Paso 01","Dibuja Tu Personaje","Boc&eacute;talo, final&iacute;zalo, nómbralo.","#top","Back to English", HICON_SKETCH)
    es+=card("PASO 01 / DIBUJA","Boceta, Finaliza y Nombra Tu Personaje",
        float_right(STEP1_FLOAT,"Un estudiante fotografiando con un iPad su personaje terminado en el cuaderno","Un personaje terminado, dibujado con l&iacute;neas limpias y formas simples, listo para fotografiar y entregar.")
        + para("Toma tu cuaderno y un l&aacute;piz. Empieza bocetando suave tu personaje usando solo formas simples: tal vez un c&iacute;rculo para la cabeza, un &oacute;valo para el cuerpo y l&iacute;neas para los brazos y las piernas. Mueve las cosas hasta que te guste c&oacute;mo se ve, y luego agrega l&iacute;neas para la cara y los detalles peque&ntilde;os.")
        + para("Cuando est&eacute;s contento con tu personaje, fija tus l&iacute;neas. Ll&eacute;valo de un boceto a un dibujo terminado con l&iacute;neas negras filosas, n&iacute;tidas y limpias. Si quieres volver a dibujar una versi&oacute;n final limpia en una hoja nueva, est&aacute; bien.")
        + bullets([
            ("Formas primero:","arma el cuerpo con formas simples y luego agrega tus l&iacute;neas."),
            ("Solo original:","tu propio personaje, nunca una copia de uno que ya existe."),
            ("Solo l&iacute;neas y formas:","blanco y negro, sin color ni sombras todav&iacute;a."),
            ("L&iacute;mpialo:","termina con l&iacute;neas negras filosas y limpias."),
            ("Ponle nombre:","dale a tu personaje un nombre original."),
        ])
        + note_orange(ORIG_ES))
    es+=deliverables_box(True,
        [("1 foto (JPG),","una foto clara de tu dibujo del personaje terminado y con nombre, subida a esta tarea de Canvas.")])
    es+=card("ENTR&Eacute;GALO","Fotograf&iacute;a y Sube Tu Personaje",
        para("Cuando tu personaje est&eacute; terminado y con nombre, toma una foto limpia y clara de la p&aacute;gina de tu cuaderno con tu iPad de la escuela. Usa buena luz, sostiene el iPad recto sobre la p&aacute;gina y evita el reflejo. Sube la foto (JPG) a esta tarea de Canvas. Luego ve al Paso 02 para la reflexi&oacute;n.")
        + note("S&eacute; honesto y entrega tu propio trabajo original."))
    es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 02 - Reflexi&oacute;n","Con tu personaje entregado, vas a reflexionar sobre qu&eacute; agregar despu&eacute;s: color, forma y textura.")

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Elements of Art: Draw Your Character | Digital Arts 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner(f"Module {MOD} &bull; Step 02","Reflection","What comes next for your character?","#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
    en+=card("STEP 02 / REFLECTION","Reflect on Your Character",
        float_right(REFLECT_FLOAT,"A Pioneer Valley student typing the Character Design reflection in the Word document on an iMac in the creative lab, a decorated sketchbook on the desk","")
        + para("Your character is built from line and shape. Now look ahead. In a short reflection, think about what you would add next to bring it to life: what would you add, what colors would fit and where, how you could use Form to make it look 3D instead of flat, and what textures are missing.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + para("Type your answers in the document, save it, and upload it to this Canvas assignment."))
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
    en+=next_up(f"UP NEXT &middot; MODULE {NXT} - Form &amp; Color","Next module you add the next two Elements of Art, Form and Color, to a new draft of your character, and keep building toward all 7 Elements of Art.")

    es=banner(f"M&oacute;dulo {MOD} &bull; Paso 02","Reflexi&oacute;n","&iquest;Qu&eacute; sigue para tu personaje?","#top","Back to English", HICON_REFLECT)
    es+=card("PASO 02 / REFLEXI&Oacute;N","Reflexiona Sobre Tu Personaje",
        float_right(REFLECT_FLOAT,"Un estudiante de Pioneer Valley escribiendo la reflexi&oacute;n de Dise&ntilde;o de Personaje en el documento de Word en una iMac del laboratorio, con un cuaderno decorado en el escritorio","")
        + para("Tu personaje est&aacute; hecho de l&iacute;nea y forma. Ahora mira hacia adelante. En una reflexi&oacute;n corta, piensa qu&eacute; le agregar&iacute;as para darle vida: qu&eacute; agregar&iacute;as, qu&eacute; colores le quedar&iacute;an y d&oacute;nde, c&oacute;mo podr&iacute;as usar la Forma para que se vea en 3D y no plano, y qu&eacute; texturas le faltan.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + para("Escribe tus respuestas en el documento, gu&aacute;rdalo y s&uacute;belo a esta tarea de Canvas."))
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word de reflexi&oacute;n completo (.docx), subido a esta tarea de Canvas.")])
    es+=next_up(f"A CONTINUACI&Oacute;N &middot; M&Oacute;DULO {NXT} - Forma y Color","El pr&oacute;ximo m&oacute;dulo agregas los siguientes dos Elementos del Arte, la Forma y el Color, a un nuevo borrador de tu personaje, y sigues construyendo hacia los 7 Elementos del Arte.")

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
    return wrap_page("Elements of Art: Reflection | Digital Arts 1A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
