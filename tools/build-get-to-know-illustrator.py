#!/usr/bin/env python3
# Digital Arts 1A - Module 08: Get to Know Illustrator (software warm-up, NO project, NO reflection).
# Two pages: Overview (Step 01, read + download the practice files) + Step 02 (take the guided Adobe
# tour, practice with the files, turn in ONE screen capture of the workspace). Bilingual EN/ES,
# 5th-grade. Dark teal angular framework via silva_framework. HICON_DESIGN crown.
#
# Adobe content is LINKED OUT, never ripped/re-hosted (copyright). The tutorial is Adobe's own
# video walkthrough and must run on Adobe's site; a prominent teal button opens it in a new tab.
# Practice files = Adobe's official Tour1.ai / Zooming.ai / Saving.ai, cleaned + hosted as a ZIP.
# ALL image slots are gated OFF (HAVE_*=False) so nothing renders a placeholder box until Chris
# supplies art and flips the flag (Chris 2026-10-07).
import os
from silva_framework import *   # shared angular chrome: banner, cards, sections, vocab, deliverables

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Digital Arts Folder"
MODNUM="08"
CL_EN="Digital Arts 1A"
CL_ES="Arte Digital 1A"
ADOBE_URL="https://www.adobe.com/learn/illustrator/web/ai-basics-fundamentals"
ADOBE_URL2="https://www.adobe.com/learn/illustrator/web/sketch-to-vector-art"
ZIP=f"{SITE}/assets/digarts1/handouts/Get_to_Know_Illustrator.zip"
IMGDIR=f"{SITE}/assets/images/da1/get-to-know-illustrator"
HEADER=f"{IMGDIR}/header-v1.jpg"
S2_FLOAT=f"{IMGDIR}/practice-float-v1.jpg"
S3_FLOAT=f"{IMGDIR}/sketch-float-v1.jpg"

OVER="digarts1-get-to-know-illustrator-overview.html"
S2="digarts1-get-to-know-illustrator-step02-practice.html"
S3="digarts1-get-to-know-illustrator-step03-sketch-to-vector.html"

# Local ent: accents -> entities AND en-dash -> plain hyphen (never emit &ndash;, per the hard dash ban).
def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

# Image slots start OFF (no placeholder boxes). Flip to True, drop the file in
# assets/images/da1/get-to-know-illustrator/, and re-run this builder when art is ready.
HAVE_HEADER=False
HAVE_S2_FLOAT=False
HAVE_S3_FLOAT=False

STANDARDS=[
  {"code":"DGA.17.1","en_tier":"Design &amp; Graphic Arts","es_tier":"Dise&ntilde;o y Artes Gr&aacute;ficas",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You get to know the Adobe Illustrator workspace, tools, and artboard, the base for all the vector art you will make.",
   "es_desc":"Conoces el espacio de trabajo, las herramientas y la mesa de trabajo de Adobe Illustrator, la base de todo el arte vectorial que har&aacute;s."},
  {"code":"DGA.17.5","en_tier":"Design &amp; Graphic Arts","es_tier":"Dise&ntilde;o y Artes Gr&aacute;ficas",
   "en_title":"Craftsmanship &amp; Production","es_title":"Elaboraci&oacute;n y Producci&oacute;n",
   "en_desc":"You open, zoom, move around, and save files in Illustrator, the industry-standard tool, building clean digital-work habits.",
   "es_desc":"Abres, haces zoom, te mueves y guardas archivos en Illustrator, la herramienta est&aacute;ndar de la industria, formando buenos h&aacute;bitos de trabajo digital."},
]

VOCAB_EN=[
 ("Vector","Art built from points and lines using math. Vector art stays sharp and clean at any size, from a tiny icon to a huge banner. A photo blurs when you make it big; vector art does not."),
 ("Artboard","The page inside your Illustrator file where your art goes. One file can hold more than one artboard."),
 ("Workspace","The way your panels and tools are arranged around your artboard. You can move panels and reset the workspace back to normal."),
 ("Tools Panel","The strip of tools along the side, like the Selection tool, the Zoom tool, and the Type tool. You pick a tool, then use it on your art."),
 ("Zoom","Moving in closer or farther to see your art. Zooming changes only your view, not the real size of the art."),
 ("Save As","Saving your file with a name, a place, and a file type, so you can find it and open it again later."),
]
VOCAB_ES=[
 ("Vector (Vector)","Arte hecho de puntos y l&iacute;neas usando matem&aacute;ticas. El arte vectorial se mantiene n&iacute;tido y limpio en cualquier tama&ntilde;o, desde un &iacute;cono peque&ntilde;o hasta un cartel enorme. Una foto se ve borrosa al agrandarla; el arte vectorial no."),
 ("Artboard (Mesa de Trabajo)","La p&aacute;gina dentro de tu archivo de Illustrator donde va tu arte. Un archivo puede tener m&aacute;s de una mesa de trabajo."),
 ("Workspace (Espacio de Trabajo)","La forma en que est&aacute;n acomodados tus paneles y herramientas alrededor de la mesa de trabajo. Puedes mover los paneles y regresar el espacio de trabajo a lo normal."),
 ("Tools Panel (Panel de Herramientas)","La barra de herramientas al costado, como la de Selecci&oacute;n, la de Zoom y la de Texto. Eliges una herramienta y luego la usas en tu arte."),
 ("Zoom (Zoom)","Acercarte o alejarte para ver tu arte. El zoom cambia solo tu vista, no el tama&ntilde;o real del arte."),
 ("Save As (Guardar Como)","Guardar tu archivo con un nombre, un lugar y un tipo de archivo, para que puedas encontrarlo y abrirlo otra vez."),
]

def adobe_button(es, url=ADOBE_URL):
    label="Abrir el Tutorial de Adobe" if es else "Open the Adobe Tutorial"
    return ('<div style="margin:16px 0 6px;">'
      f'<a href="{url}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;'
      'background:#00b8b8;color:#04201f;padding:13px 28px;border-top:2px solid #80e0e0;font-size:12.5pt;'
      f'letter-spacing:0.04em;"><strong>{label} &#8599;</strong></a></div>')

def _tour_part(num, title, items):
    hd=('<div style="display:flex;align-items:center;gap:10px;margin:16px 0 8px;">'
        f'<span style="flex:0 0 auto;width:26px;height:26px;background:#00b8b8;color:#04201f;font-size:12pt;line-height:26px;text-align:center;"><strong>{num}</strong></span>'
        f'<span style="font-size:14pt;color:#80e0e0;"><strong>{title}</strong></span></div>')
    return hd+bullets(items)

def tour_notes(es):
    # The tutorial's written takeaways, rewritten simple + Mac-only, inside the LOCKED vertical
    # .silva-scroll panel so the step-by-step stays contained and never looks overwhelming (Chris).
    if es:
        hint="Despl&aacute;zate dentro del cuadro para ver las cuatro partes."
        parts=(
         _tour_part("1","Recorre el espacio de trabajo",[
            ("Barra de men&uacute;:","la tira de hasta arriba (Archivo, Edici&oacute;n y m&aacute;s). Guarda los comandos y los ajustes."),
            ("Panel de herramientas:","a la izquierda. Tiene las herramientas para crear y cambiar el arte. Las parecidas est&aacute;n juntas; mant&eacute;n presionada una para ver el grupo."),
            ("Paneles:","a la derecha (como Propiedades y Capas). Te dan controles para tu arte. La lista completa est&aacute; en el men&uacute; Ventana."),
            ("Ventana del documento:","el centro, donde se ve tu arte. Cada archivo abierto tiene su propia pesta&ntilde;a."),
         ])
         + _tour_part("2","Haz zoom y mu&eacute;vete",[
            ("Herramienta Zoom:","en el panel de herramientas. Te deja ver m&aacute;s detalle. Mant&eacute;n Opci&oacute;n para cambiar de Acercar a Alejar."),
            ("Herramienta Mano:","mant&eacute;n presionada la herramienta Zoom para encontrarla. Te deja deslizarte por la mesa de trabajo."),
         ])
         + _tour_part("3","Crea un documento nuevo",[
            ("Archivo &gt; Nuevo:","abre el cuadro Nuevo documento. Elige un preset (como Impresi&oacute;n) para fijar el tama&ntilde;o y las opciones."),
            ("Pantalla de inicio:","aparece cuando no hay archivos abiertos. Lista tus archivos recientes y presets listos para usar."),
         ])
         + _tour_part("4","Guarda tu trabajo",[
            ("Archivo &gt; Guardar o Guardar como:","eliges Guardar en tu computadora o Guardar en Documentos en la nube."),
            ("En tu computadora:","guarda el archivo directo en tu Mac."),
            ("Documentos en la nube:","se guardan en la nube de Adobe. Los abres en cualquier dispositivo y se guardan solos."),
            ("D&eacute;jalo editable:","guarda como archivo de Illustrator (.ai). Eso conserva tus capas y tu texto para editar despu&eacute;s."),
            ("En el cuadro Guardar como:","nombra tu archivo, elige d&oacute;nde va, aseg&uacute;rate de que Adobe Illustrator est&eacute; elegido en el men&uacute; Formato y haz clic en Guardar."),
         ])
        )
    else:
        hint="Scroll inside the box to see all four parts."
        parts=(
         _tour_part("1","Tour the workspace",[
            ("Menu bar:","the strip at the very top (File, Edit, and more). It holds commands and settings."),
            ("Tools panel:","on the left. It holds the tools you use to make and change art. Tools that are alike are grouped; click and hold one to see the group."),
            ("Panels:","on the right (like Properties and Layers). They give you controls for your art. The full list is under the Window menu."),
            ("Document window:","the middle, where your art shows. Each open file has its own tab."),
         ])
         + _tour_part("2","Zoom and pan",[
            ("Zoom tool:","in the Tools panel. It lets you see more detail. Hold Option to switch from Zoom In to Zoom Out."),
            ("Hand tool:","click and hold the Zoom tool to find it. It lets you slide (pan) around your artboard."),
         ])
         + _tour_part("3","Make a new document",[
            ("File &gt; New:","opens the New Document box. Pick a preset, like Print, to set the size and options."),
            ("Start screen:","shows when no file is open. It lists your recent files and ready-made presets."),
         ])
         + _tour_part("4","Save your work",[
            ("File &gt; Save or Save As:","you choose Save On Your Computer or Save To Cloud Documents."),
            ("On your computer:","saves the file right on your Mac."),
            ("Cloud documents:","save to Adobe&rsquo;s cloud. You can open them on any device, and they autosave as you work."),
            ("Keep it editable:","save as an Illustrator file (.ai). That keeps your layers and type so you can edit it later."),
            ("In the Save As box:","name your file, pick where it goes, make sure Adobe Illustrator is chosen in the Format menu, then click Save."),
         ])
        )
    hintline=f'<div style="font-size:11pt;color:#80e0e0;margin-bottom:8px;opacity:0.85;">&#8595; {hint}</div>'
    scroll=('<div class="silva-scroll" style="max-height:460px;overflow-y:auto;padding:14px 16px 20px;border:1px solid rgba(0,184,184,0.22);'
      'background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, rgba(0,0,0,0.14) 88%, rgba(0,184,184,0.16) 100%);">'
      f'{parts}</div>')
    return hintline+scroll

def sketch_notes(es):
    # Sketch-to-vector steps (Step 03), rewritten simple + Mac-only, in the same locked scroller.
    if es:
        hint="Despl&aacute;zate dentro del cuadro para ver los pasos."
        parts=(
         _tour_part("1","Dibuja e importa",[
            ("Haz un boceto simple:","dib&uacute;jalo en papel y t&oacute;male una foto. O descarga el boceto de pr&aacute;ctica desde la p&aacute;gina del tutorial de Adobe."),
            ("Col&oacute;calo en Illustrator:","usa Archivo &gt; Colocar y elige la foto de tu boceto para traerla."),
            ("Ponlo en su propia capa:","as&iacute; puedes calcar encima sin moverlo."),
         ])
         + _tour_part("2","Calca con las herramientas",[
            ("Bloquea la capa del boceto:","haz clic en el candado junto a la capa en el panel Capas para que no se mueva."),
            ("Crea una capa nueva encima:","ah&iacute; ir&aacute;n tus l&iacute;neas vectoriales."),
            ("Herramienta Pluma:","para l&iacute;neas limpias y exactas."),
            ("Herramienta L&aacute;piz:","para l&iacute;neas sueltas y fluidas. Calca tu boceto, l&iacute;nea por l&iacute;nea."),
         ])
         + _tour_part("3","Mejora tus trazos",[
            ("Haz las l&iacute;neas m&aacute;s gruesas:","cambia el grosor del trazo en el panel Propiedades o Trazo para un look fuerte."),
            ("Limpia las l&iacute;neas:","arregla las partes disparejas hasta que el arte se vea n&iacute;tido."),
         ])
         + _tour_part("4","Agrega texto (opcional)",[
            ("Elige una fuente:","si tu arte necesita palabras, elige una fuente de Adobe Fonts."),
            ("Acomoda el texto:","col&oacute;calo para que combine bien con tu arte."),
         ])
        )
    else:
        hint="Scroll inside the box to see the steps."
        parts=(
         _tour_part("1","Sketch and import",[
            ("Make a simple sketch:","draw it on paper and take a photo of it. Or download the practice sketch from the Adobe tutorial page."),
            ("Place it in Illustrator:","use File &gt; Place and choose your sketch photo to bring it in."),
            ("Put it on its own layer:","so you can trace on top without moving it."),
         ])
         + _tour_part("2","Trace with the tools",[
            ("Lock the sketch layer:","click the lock box next to the layer in the Layers panel so it cannot move."),
            ("Make a new layer on top:","your vector lines go there."),
            ("Pen tool:","for clean, exact lines."),
            ("Pencil tool:","for loose, flowing lines. Trace your sketch, line by line."),
         ])
         + _tour_part("3","Refine your strokes",[
            ("Thicken your lines:","change the stroke weight in the Properties or Stroke panel for a bold look."),
            ("Clean it up:","fix any bumpy lines until the art looks sharp."),
         ])
         + _tour_part("4","Add type (optional)",[
            ("Pick a font:","if your art needs words, choose a font from Adobe Fonts."),
            ("Arrange the type:","place it so it fits your art nicely."),
         ])
        )
    hintline=f'<div style="font-size:11pt;color:#80e0e0;margin-bottom:8px;opacity:0.85;">&#8595; {hint}</div>'
    scroll=('<div class="silva-scroll" style="max-height:460px;overflow-y:auto;padding:14px 16px 20px;border:1px solid rgba(0,184,184,0.22);'
      'background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, rgba(0,0,0,0.14) 88%, rgba(0,184,184,0.16) 100%);">'
      f'{parts}</div>')
    return hintline+scroll

def downloads_block(es):
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga los archivos de pr&aacute;ctica de Illustrator. Son tres archivos .ai dentro de un ZIP. Descompr&iacute;melo y gu&aacute;rdalo en la carpeta de tu proyecto para usarlo en el Paso 02." if es
          else "Download the Illustrator practice files. It is three .ai files inside a ZIP. Unzip it and keep it in your project folder to use in Step 02.")
    zlabel="Archivos de Pr&aacute;ctica de Illustrator (ZIP)" if es else "Illustrator Practice Files (ZIP)"
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ZIP, zlabel, row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Get to Know Illustrator</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

HREFS=[OVER,S2,S3]; TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03")]
def dots_for(ai):
    return "".join(dot("" if i==ai else HREFS[i], lab, title, i==ai, module=False) for i,(lab,title) in enumerate(TITLES))

# ================= OVERVIEW (Step 01) =================
def overview():
    en=banner(f"Module {MODNUM} &bull; Step 01","Get to Know Illustrator",
        "Read this page and download your practice files, then go to Step 02 to take the tour. This is a warm-up, there is no project to turn in yet.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
    en+=type_card("overview","Step 01 &middot; Overview &amp; Download","Meet Adobe Illustrator",
        para("Illustrator is the program artists and designers use to make logos, icons, posters, and art that can be printed at any size. This module is a warm-up. You will take a short guided tour to learn your way around the program. There is no project to turn in yet, so relax and just get comfortable.")
        + para("Illustrator makes <strong>vector</strong> art. Vector art is built from points and lines using math, so it stays sharp and clean at any size, from a tiny icon to a wall-sized banner. A photo gets blurry when you blow it up. Vector art never does.")
        + para("In this warm-up you will tour the workspace, learn to zoom and move around, make a new document, and save your work. Then you will practice with the files you download below.")
        + (framed(HEADER,"The Adobe Illustrator workspace with the Tools panel and an artboard") if HAVE_HEADER else ""))
    en+=standards_box(False, STANDARDS)
    en+=downloads_block(False)
    en+=card("WHAT YOU WILL LEARN","Your Four-Part Tour",
        para("The tour in Step 02 is short and has four quick parts. Here is what each part teaches you.")
        + bullets([
            ("The workspace tour:","get to know the Illustrator window: the artboard in the middle, the Tools panel on the side, and the panels around the edges."),
            ("Zooming and moving:","learn to zoom in close and move around your artboard so you can work on small details."),
            ("Make a new document:","start a fresh file and choose a size, so you know how every project begins."),
            ("Saving your work:","save your file the right way so you never lose your work and can open it again later."),
        ]))
    en+=card("HOW THIS MODULE WORKS","Three Steps",
        para("This module has three steps. You are on Step 01 now.")
        + bullets([
            ("Step 01 &middot; Overview &amp; Download (you are here):","read this page and download your practice files below."),
            ("Step 02 &middot; Take the Tour &amp; Practice:","follow the short Adobe tutorial, practice with your files, then turn in one screen capture of your Illustrator workspace."),
            ("Step 03 &middot; Sketch to Vector Art:","now that you know your way around, turn a simple sketch into clean vector art and turn in a screen capture of it."),
        ])
        + note("There is no written reflection in this module. It stays low-stakes: get comfortable in Illustrator, then make your first attempt at real vector art."))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words show up on your Digital Arts quizzes. Learn them now, not the night before.",
          VOCAB_EN), False)
    en+=next_up("UP NEXT &middot; STEP 02 - Take the Tour &amp; Practice","Follow the guided Adobe tour, practice with your files, and capture your workspace.")

    es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 01","Conoce Illustrator",
        "Lee esta p&aacute;gina y descarga tus archivos de pr&aacute;ctica, luego ve al Paso 02 para hacer el recorrido. Esto es un calentamiento, todav&iacute;a no hay proyecto que entregar.","#top","Back to English", HICON_DESIGN)
    es+=type_card("overview","Paso 01 &middot; Resumen y Descarga","Conoce Adobe Illustrator",
        para("Illustrator es el programa que usan los artistas y dise&ntilde;adores para hacer logotipos, &iacute;conos, carteles y arte que se puede imprimir en cualquier tama&ntilde;o. Este m&oacute;dulo es un calentamiento. Har&aacute;s un recorrido corto y guiado para aprender a moverte en el programa. Todav&iacute;a no hay proyecto que entregar, as&iacute; que rel&aacute;jate y toma confianza.")
        + para("Illustrator hace arte <strong>vectorial</strong>. El arte vectorial se construye con puntos y l&iacute;neas usando matem&aacute;ticas, as&iacute; que se mantiene n&iacute;tido y limpio en cualquier tama&ntilde;o, desde un &iacute;cono peque&ntilde;o hasta un cartel del tama&ntilde;o de una pared. Una foto se ve borrosa al agrandarla. El arte vectorial nunca.")
        + para("En este calentamiento vas a recorrer el espacio de trabajo, aprender a hacer zoom y moverte, crear un documento nuevo y guardar tu trabajo. Luego practicar&aacute;s con los archivos que descargues abajo.")
        + (framed(HEADER,"El espacio de trabajo de Adobe Illustrator con el panel de herramientas y una mesa de trabajo") if HAVE_HEADER else ""))
    es+=standards_box(True, STANDARDS)
    es+=downloads_block(True)
    es+=card("LO QUE VAS A APRENDER","Tu Recorrido de Cuatro Partes",
        para("El recorrido del Paso 02 es corto y tiene cuatro partes r&aacute;pidas. Esto es lo que te ense&ntilde;a cada parte.")
        + bullets([
            ("El recorrido del espacio de trabajo:","conoce la ventana de Illustrator: la mesa de trabajo en el centro, el panel de herramientas al costado y los paneles alrededor."),
            ("Zoom y movimiento:","aprende a acercarte y a moverte por tu mesa de trabajo para trabajar en los detalles peque&ntilde;os."),
            ("Crear un documento nuevo:","empieza un archivo nuevo y elige un tama&ntilde;o, para que sepas c&oacute;mo empieza cada proyecto."),
            ("Guardar tu trabajo:","guarda tu archivo de la forma correcta para que nunca pierdas tu trabajo y puedas abrirlo otra vez."),
        ]))
    es+=card("C&Oacute;MO FUNCIONA ESTE M&Oacute;DULO","Tres Pasos",
        para("Este m&oacute;dulo tiene tres pasos. Est&aacute;s en el Paso 01 ahora.")
        + bullets([
            ("Paso 01 &middot; Resumen y Descarga (est&aacute;s aqu&iacute;):","lee esta p&aacute;gina y descarga tus archivos de pr&aacute;ctica abajo."),
            ("Paso 02 &middot; Haz el Recorrido y Practica:","sigue el tutorial corto de Adobe, practica con tus archivos y luego entrega una captura de pantalla de tu espacio de trabajo de Illustrator."),
            ("Paso 03 &middot; De Boceto a Arte Vectorial:","ahora que ya sabes moverte, convierte un boceto simple en arte vectorial limpio y entrega una captura de pantalla."),
        ])
        + note("Este m&oacute;dulo no tiene reflexi&oacute;n escrita. Sigue siendo de baja presi&oacute;n: toma confianza en Illustrator y luego haz tu primer intento de arte vectorial de verdad."))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecen en tus ex&aacute;menes de Arte Digital. Apr&eacute;ndelas ahora, no la noche anterior.",
          VOCAB_ES), True)
    es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 02 - Haz el Recorrido y Practica","Sigue el recorrido guiado de Adobe, practica con tus archivos y captura tu espacio de trabajo.")

    stepnav=f'<a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S2}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
    return wrap_page(f"Get to Know Illustrator | {CL_EN} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ================= STEP 02: Take the Tour & Practice =================
def step02():
    en=banner(f"Module {MODNUM} &bull; Step 02","Take the Tour &amp; Practice",
        "Follow the short Adobe tutorial, practice with your files, then turn in one screen capture of your workspace.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
    en+=card("THE TOUR / WE DO IT TOGETHER","Follow the Adobe Tutorial",
        para("Open Adobe Illustrator on your Mac. Then follow this short tutorial. It is made by Adobe and has four quick videos: the workspace, zooming and panning, making a new document, and saving your work.")
        + adobe_button(False)
        + note("The tutorial opens on Adobe&rsquo;s own website in a new tab. Watch each short video, then do the same thing in your own copy of Illustrator. Keep this page open so you can come back to it."))
    en+=card("QUICK NOTES FROM THE TOUR","What Each Part Teaches",
        para("Here is what each part of the tour teaches, in short. Use it as a cheat sheet while you watch and while you practice. These steps are for a Mac.")
        + tour_notes(False))
    en+=card("YOU PRACTICE / ON YOUR OWN","Practice With Your Files",
        (float_right(S2_FLOAT,"A Pioneer Valley student practicing in Adobe Illustrator on an iMac in the lab","Open each practice file and try the moves from the tour.") if HAVE_S2_FLOAT else "")
        + para("Now practice on your own with the three files you downloaded in Step 01. Open them from your Digital Arts project folder.")
        + bullets([
            ("Open Tour1.ai:","look around the workspace. Find the Tools panel and try clicking a few tools."),
            ("Open Zooming.ai:","practice zooming in and out and moving around the artboard."),
            ("Open Saving.ai:","practice Save As. Save a copy into your project folder with a clear name."),
        ])
        + note("Take your time. Nobody is graded on speed here. The point is to feel comfortable opening files, moving around, and saving.")
        + note("To take a screen capture on a Mac, press Cmd + Shift + 4 to grab part of the screen, or Cmd + Shift + 3 for the whole screen. The image saves to your desktop."))
    en+=deliverables_box(False,
        [("1 screen capture (JPG or PNG):","a screen capture of your Illustrator workspace with one of the practice files open, uploaded to this Canvas assignment. It just needs to show that you opened Illustrator and found your way around.")])
    en+=next_up("UP NEXT &middot; STEP 03 - Sketch to Vector Art","Now that you know your way around, you will turn a simple sketch into clean vector art.")

    es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 02","Haz el Recorrido y Practica",
        "Sigue el tutorial corto de Adobe, practica con tus archivos y luego entrega una captura de pantalla de tu espacio de trabajo.","#top","Back to English", HICON_DESIGN)
    es+=card("EL RECORRIDO / LO HACEMOS JUNTOS","Sigue el Tutorial de Adobe",
        para("Abre Adobe Illustrator en tu Mac. Luego sigue este tutorial corto. Est&aacute; hecho por Adobe y tiene cuatro videos r&aacute;pidos: el espacio de trabajo, el zoom, c&oacute;mo crear un documento nuevo y c&oacute;mo guardar tu trabajo.")
        + adobe_button(True)
        + note("El tutorial se abre en el sitio web de Adobe en una pesta&ntilde;a nueva. Mira cada video corto y luego haz lo mismo en tu propia copia de Illustrator. Deja esta p&aacute;gina abierta para que puedas regresar."))
    es+=card("NOTAS R&Aacute;PIDAS DEL RECORRIDO","Qu&eacute; Ense&ntilde;a Cada Parte",
        para("Esto es lo que ense&ntilde;a cada parte del recorrido, en corto. &Uacute;salo como ayuda mientras miras y mientras practicas. Estos pasos son para una Mac.")
        + tour_notes(True))
    es+=card("TU PRACTICAS / POR TU CUENTA","Practica Con Tus Archivos",
        (float_right(S2_FLOAT,"Un estudiante de Pioneer Valley practicando en Adobe Illustrator en una iMac en el laboratorio","Abre cada archivo de pr&aacute;ctica y prueba los pasos del recorrido.") if HAVE_S2_FLOAT else "")
        + para("Ahora practica por tu cuenta con los tres archivos que descargaste en el Paso 01. &Aacute;brelos desde la carpeta de tu proyecto de Arte Digital.")
        + bullets([
            ("Abre Tour1.ai:","mira el espacio de trabajo. Encuentra el panel de herramientas y prueba a hacer clic en algunas herramientas."),
            ("Abre Zooming.ai:","practica acercar y alejar la vista y moverte por la mesa de trabajo."),
            ("Abre Saving.ai:","practica Guardar Como. Guarda una copia en la carpeta de tu proyecto con un nombre claro."),
        ])
        + note("T&oacute;mate tu tiempo. Nadie se califica por rapidez. La idea es sentirte c&oacute;modo abriendo archivos, movi&eacute;ndote y guardando.")
        + note("Para tomar una captura de pantalla en una Mac, presiona Cmd + Shift + 4 para capturar una parte de la pantalla, o Cmd + Shift + 3 para toda la pantalla. La imagen se guarda en tu escritorio."))
    es+=deliverables_box(True,
        [("1 captura de pantalla (JPG o PNG):","una captura de pantalla de tu espacio de trabajo de Illustrator con uno de los archivos de pr&aacute;ctica abierto, subida a esta tarea de Canvas. Solo necesita mostrar que abriste Illustrator y que te supiste mover.")])
    es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 03 - De Boceto a Arte Vectorial","Ahora que ya sabes moverte, convertir&aacute;s un boceto simple en arte vectorial limpio.")

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page(f"Step 2: Take the Tour and Practice | Get to Know Illustrator | {CL_EN} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

# ================= STEP 03: Sketch to Vector Art =================
def step03():
    en=banner(f"Module {MODNUM} &bull; Step 03","Sketch to Vector Art",
        "Turn a simple sketch into clean vector art by tracing it with the Pen and Pencil tools, then turn in a screen capture.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
    en+=card("FROM SKETCH TO VECTOR / WHAT YOU WILL DO","Trace a Sketch Into Vector Art",
        para("Now that you know your way around Illustrator, you get to try real vector art. You will take a simple sketch, bring it into Illustrator, and trace over it to make clean lines that stay sharp at any size.")
        + para("This is your first attempt, so keep your sketch simple: a shape, a letter, or a small drawing. The goal is to practice tracing, not to make a perfect piece.")
        + note("Vector art is made from lines and shapes, so it never gets blurry when you make it bigger. That is why logos and icons are built this way."))
    en+=card("FOLLOW THE ADOBE TUTORIAL","Watch: Turn a Sketch Into Vector Art",
        para("Open Adobe Illustrator, then follow this short Adobe tutorial. It is about five minutes and shows you how to bring in a sketch and trace it with the drawing tools.")
        + adobe_button(False, ADOBE_URL2)
        + note("The tutorial opens on Adobe&rsquo;s own website in a new tab. It also has its own practice sketch you can download there if you want one. Watch it, then try the same steps on your own sketch."))
    en+=card("QUICK NOTES FROM THE TUTORIAL","How to Trace Your Sketch",
        para("Here are the steps in short. Use them as a cheat sheet while you work. These steps are for a Mac.")
        + sketch_notes(False))
    en+=card("YOU PRACTICE / ON YOUR OWN","Make Your Vector Art",
        (float_right(S3_FLOAT,"A Pioneer Valley student tracing a sketch into vector art in Adobe Illustrator on an iMac in the lab","Place your sketch, lock it, and trace on a new layer.") if HAVE_S3_FLOAT else "")
        + para("Pick a simple sketch to trace. You can draw your own on paper and take a photo of it, or download the practice sketch from the Adobe tutorial.")
        + bullets([
            ("Place your sketch:","use File &gt; Place to bring your sketch into Illustrator."),
            ("Lock the sketch layer:","so it stays still while you trace."),
            ("Trace it:","use the Pen tool for clean lines and the Pencil tool for loose lines."),
            ("Make it bold:","thicken your strokes so the art looks strong."),
        ])
        + note("Keep it simple and have fun. This is a first attempt, not a graded project."))
    en+=deliverables_box(False,
        [("1 screen capture (JPG or PNG):","a screen capture of your vector art in Illustrator, your traced sketch, uploaded to this Canvas assignment.")])
    en+=next_up("MODULE COMPLETE","Nice work. You know your way around Illustrator and you have turned a sketch into vector art. You are ready for your first real Illustrator project.")

    es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 03","De Boceto a Arte Vectorial",
        "Convierte un boceto simple en arte vectorial limpio calc&aacute;ndolo con las herramientas Pluma y L&aacute;piz, luego entrega una captura de pantalla.","#top","Back to English", HICON_DESIGN)
    es+=card("DE BOCETO A VECTOR / QU&Eacute; VAS A HACER","Calca un Boceto a Arte Vectorial",
        para("Ahora que ya sabes moverte en Illustrator, vas a probar arte vectorial de verdad. Vas a tomar un boceto simple, traerlo a Illustrator y calcarlo encima para hacer l&iacute;neas limpias que se mantienen n&iacute;tidas en cualquier tama&ntilde;o.")
        + para("Es tu primer intento, as&iacute; que mant&eacute;n tu boceto simple: una forma, una letra o un dibujo peque&ntilde;o. La meta es practicar el calcado, no hacer una obra perfecta.")
        + note("El arte vectorial est&aacute; hecho de l&iacute;neas y formas, as&iacute; que nunca se ve borroso al agrandarlo. Por eso los logotipos y los &iacute;conos se hacen as&iacute;."))
    es+=card("SIGUE EL TUTORIAL DE ADOBE","Mira: Convierte un Boceto en Arte Vectorial",
        para("Abre Adobe Illustrator, luego sigue este tutorial corto de Adobe. Dura unos cinco minutos y te muestra c&oacute;mo traer un boceto y calcarlo con las herramientas de dibujo.")
        + adobe_button(True, ADOBE_URL2)
        + note("El tutorial se abre en el sitio web de Adobe en una pesta&ntilde;a nueva. Tambi&eacute;n tiene su propio boceto de pr&aacute;ctica que puedes descargar ah&iacute; si quieres uno. M&iacute;ralo, luego prueba los mismos pasos en tu propio boceto."))
    es+=card("NOTAS R&Aacute;PIDAS DEL TUTORIAL","C&oacute;mo Calcar Tu Boceto",
        para("Estos son los pasos en corto. &Uacute;salos como ayuda mientras trabajas. Estos pasos son para una Mac.")
        + sketch_notes(True))
    es+=card("T&Uacute; PRACTICAS / POR TU CUENTA","Haz Tu Arte Vectorial",
        (float_right(S3_FLOAT,"Un estudiante de Pioneer Valley calcando un boceto a arte vectorial en Adobe Illustrator en una iMac en el laboratorio","Coloca tu boceto, bloqu&eacute;alo y calca en una capa nueva.") if HAVE_S3_FLOAT else "")
        + para("Elige un boceto simple para calcar. Puedes dibujar el tuyo en papel y tomarle una foto, o descargar el boceto de pr&aacute;ctica del tutorial de Adobe.")
        + bullets([
            ("Coloca tu boceto:","usa Archivo &gt; Colocar para traer tu boceto a Illustrator."),
            ("Bloquea la capa del boceto:","para que no se mueva mientras calcas."),
            ("C&aacute;lcalo:","usa la herramienta Pluma para l&iacute;neas limpias y la herramienta L&aacute;piz para l&iacute;neas sueltas."),
            ("Hazlo fuerte:","engrosa tus trazos para que el arte se vea s&oacute;lido."),
        ])
        + note("Mant&eacute;nlo simple y div&iacute;ertete. Es un primer intento, no un proyecto calificado."))
    es+=deliverables_box(True,
        [("1 captura de pantalla (JPG o PNG):","una captura de pantalla de tu arte vectorial en Illustrator, tu boceto calcado, subida a esta tarea de Canvas.")])
    es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Ya sabes moverte en Illustrator y convertiste un boceto en arte vectorial. Est&aacute;s listo para tu primer proyecto de verdad en Illustrator.")

    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page(f"Step 3: Sketch to Vector Art | Get to Know Illustrator | {CL_EN} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S2,step02),(S3,step03)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
