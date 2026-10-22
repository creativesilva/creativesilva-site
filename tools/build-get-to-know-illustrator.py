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
S4_FLOAT=f"{IMGDIR}/back-float-v1.jpg"
S5_FLOAT=f"{IMGDIR}/scene-float-v1.jpg"

OVER="digarts1-get-to-know-illustrator-overview.html"
S2="digarts1-get-to-know-illustrator-step02-practice.html"
S3="digarts1-get-to-know-illustrator-step03-sketch-to-vector.html"
S4="digarts1-get-to-know-illustrator-step04-character-back.html"
S5="digarts1-get-to-know-illustrator-step05-character-scene.html"

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
HAVE_S4_FLOAT=False  # Step 04 backside float (none supplied yet), assets/images/da1/get-to-know-illustrator/back-float-v1.jpg
HAVE_S5_FLOAT=False  # Step 05 scene float (none supplied yet), assets/images/da1/get-to-know-illustrator/scene-float-v1.jpg

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
    # Solid PURPLE action button: same geometry as the orange download button (dl_link, 11px 22px /
    # 11pt / 2px top accent), skinned to the purple Resources section it lives in. No arrow glyph
    # (Chris 2026-10-07): a button already reads as clickable.
    label="Abrir el Tutorial de Adobe" if es else "Open the Adobe Tutorial"
    return ('<div style="margin:14px 0 4px;">'
      f'<a href="{url}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;'
      'background:#8b5cf6;color:#ffffff;padding:11px 22px;border-top:2px solid #c4b5fd;font-size:11pt;'
      f'letter-spacing:0.04em;"><strong>{label}</strong></a></div>')

def pnote(t):
    # PURPLE note: a callout INSIDE a purple Resources card, matching the section color (cohesion).
    return ('<div style="background:rgba(139,92,246,0.10);border:1px solid rgba(139,92,246,0.30);'
      f'border-left:4px solid #8b5cf6;padding:11px 14px;margin:8px 0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def _tour_part(num, title, items):
    # Numbered part inside a purple Resources scroller: purple badge + purple title + purple bullets.
    hd=('<div style="display:flex;align-items:center;gap:10px;margin:16px 0 8px;">'
        f'<span style="flex:0 0 auto;width:26px;height:26px;background:#8b5cf6;color:#140f24;font-size:12pt;line-height:26px;text-align:center;"><strong>{num}</strong></span>'
        f'<span style="font-size:14pt;color:#c4b5fd;"><strong>{title}</strong></span></div>')
    return hd+bullets(items, "#8b5cf6")

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
            ("Herramienta Mano:","b&uacute;scala en el panel de herramientas, o mant&eacute;n presionada la barra espaciadora para tomarla en cualquier momento. Te deja deslizarte por la mesa de trabajo."),
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
            ("Hand tool:","find it in the Tools panel, or hold down the Spacebar to grab it anytime. It lets you slide (pan) around your artboard."),
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
    hintline=f'<div style="font-size:11pt;color:#c4b5fd;margin-bottom:8px;opacity:0.85;">&#8595; {hint}</div>'
    scroll=('<div class="silva-scroll" style="max-height:460px;overflow-y:auto;padding:14px 16px 20px;border:1px solid rgba(139,92,246,0.30);'
      'background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, rgba(0,0,0,0.14) 88%, rgba(139,92,246,0.16) 100%);">'
      f'{parts}</div>')
    return hintline+scroll

def sketch_notes(es):
    # Sketch-to-vector steps (Step 03), rewritten simple + Mac-only, in the same locked scroller.
    if es:
        hint="Despl&aacute;zate dentro del cuadro para ver los pasos."
        parts=(
         _tour_part("1","Coloca tu boceto como gu&iacute;a",[
            ("Fotograf&iacute;a tu boceto del personaje:","usa tu iPad escolar para tomarle una foto a tu boceto del personaje, luego pasa esa foto a tu Mac."),
            ("Col&oacute;calo en Illustrator:","usa Archivo &gt; Colocar y elige la foto de tu boceto para traerla."),
            ("Ponlo en su capa y bloqu&eacute;alo:","esta es tu gu&iacute;a. Bloquea la capa para que no se mueva mientras dibujas encima."),
         ])
         + _tour_part("2","Construye tu personaje",[
            ("Capa nueva encima:","crea una capa nueva para tu arte vectorial, arriba del boceto."),
            ("Herramientas de forma:","usa Rect&aacute;ngulo y Elipse para las formas grandes y simples de tu personaje."),
            ("Herramienta Pluma:","dibuja las formas y contornos que las herramientas de forma no pueden hacer."),
            ("Constr&uacute;yelo sobre el boceto:","pieza por pieza, cubre tu boceto con formas vectoriales limpias."),
         ])
         + _tour_part("3","Une y ordena",[
            ("Pathfinder para unir:","selecciona las formas que deben ser una sola pieza y usa el panel Pathfinder (Unificar) para unirlas."),
            ("Orden de capas:","en el panel Capas, arrastra las capas para decidir qu&eacute; va adelante y qu&eacute; va atr&aacute;s."),
         ])
         + _tour_part("4","Agrega color",[
            ("Dale color a cada forma:","haz clic en una forma y elige un color de relleno en el panel Propiedades o Muestras. Colorea todo tu personaje."),
         ])
         + _tour_part("5","Termina y guarda",[
            ("Borra la capa del boceto:","ya no necesitas la gu&iacute;a. En el panel Capas, borra la capa de la imagen del boceto para que solo quede tu personaje vectorial."),
            ("Guarda como .ai:","Archivo &gt; Guardar Como, y elige Adobe Illustrator en el men&uacute; Formato."),
            ("Guarda una copia como .svg:","Archivo &gt; Guardar Como otra vez, y elige SVG en el men&uacute; Formato. Ya tienes los dos archivos."),
         ])
        )
    else:
        hint="Scroll inside the box to see the steps."
        parts=(
         _tour_part("1","Place your sketch as a guide",[
            ("Photograph your character sketch:","use your school iPad to take a photo of your character sketch, then get that photo onto your Mac."),
            ("Place it in Illustrator:","use File &gt; Place and choose your sketch photo to bring it in."),
            ("Put it on its own layer and lock it:","this is your roadmap. Lock the layer so it stays still while you draw on top."),
         ])
         + _tour_part("2","Build your character",[
            ("New layer on top:","make a new layer for your vector art, above the sketch."),
            ("Shape tools:","use the Rectangle and Ellipse tools for the big, simple forms of your character."),
            ("Pen tool:","draw the custom shapes and outlines the shape tools cannot make."),
            ("Build it over your sketch:","piece by piece, cover your sketch with clean vector shapes."),
         ])
         + _tour_part("3","Unite and order",[
            ("Pathfinder to unite:","select the shapes that should be one piece, then open the Pathfinder panel and click Unite to combine them into one shape."),
            ("Layer order:","in the Layers panel, drag layers up or down to set what is in front and what is behind."),
         ])
         + _tour_part("4","Add color",[
            ("Give each shape a color:","click a shape, then choose a fill color in the Properties or Swatches panel. Color your whole character."),
         ])
         + _tour_part("5","Finish and save",[
            ("Delete the sketch layer:","you do not need the roadmap anymore. In the Layers panel, delete the sketch image layer so only your vector character is left."),
            ("Save as .ai:","File &gt; Save As, and pick Adobe Illustrator in the Format menu."),
            ("Save a copy as .svg:","File &gt; Save As again, and pick SVG in the Format menu. You now have both files."),
         ])
        )
    hintline=f'<div style="font-size:11pt;color:#c4b5fd;margin-bottom:8px;opacity:0.85;">&#8595; {hint}</div>'
    scroll=('<div class="silva-scroll" style="max-height:460px;overflow-y:auto;padding:14px 16px 20px;border:1px solid rgba(139,92,246,0.30);'
      'background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, rgba(0,0,0,0.14) 88%, rgba(139,92,246,0.16) 100%);">'
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

HREFS=[OVER,S2,S3,S4,S5]; TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04"),("5","Step 05")]
def dots_for(ai):
    return "".join(dot("" if i==ai else HREFS[i], lab, title, i==ai, module=False) for i,(lab,title) in enumerate(TITLES))

# ================= OVERVIEW (Step 01) =================
def overview():
    en=banner(f"Module {MODNUM} &bull; Step 01","Get to Know Illustrator",
        "Read this page and download your practice files, then go to Step 02 to take the tour. Steps 01 and 02 are your warm-up. The project begins in Step 03.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
    en+=type_card("overview","Step 01 &middot; Overview &amp; Download","Meet Adobe Illustrator",
        para("Illustrator is the program artists and designers use to make logos, icons, posters, and art that can be printed at any size. This module is a warm-up. You will take a short guided tour to learn your way around the program. There is nothing to turn in for the tour, so relax and get comfortable. Your project begins in Step 03, where you draw your character.")
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
    en+=card("HOW THIS MODULE WORKS","Five Steps",
        para("This module has five steps. You are on Step 01 now.")
        + bullets([
            ("Step 01 &middot; Overview &amp; Download (you are here):","read this page and download your practice files below."),
            ("Step 02 &middot; Take the Tour &amp; Practice:","follow the short Adobe tutorial, practice with your files, then turn in one screen capture of your Illustrator workspace."),
            ("Step 03 &middot; Sketch to Vector Art:","now that you know your way around, draw your character in vector and turn in your .ai and .svg files so it can be 3D printed."),
            ("Step 04 &middot; Draw the Back of Your Character:","add a second artboard and make the back view of your character, keeping the same silhouette, and turn in your .ai and .svg files."),
            ("Step 05 &middot; Put Your Character in a Scene:","build a 16:9 widescreen scene around your character, show its scale, and turn in your .ai and .svg files."),
        ])
        + note("There is no written reflection in this module. You get comfortable in Illustrator, draw your character front and back, then build a scene around it."))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words show up on your Digital Arts quizzes. Learn them now, not the night before.",
          VOCAB_EN), False)
    en+=next_up("UP NEXT &middot; STEP 02 - Take the Tour &amp; Practice","Follow the guided Adobe tour, practice with your files, and capture your workspace.")

    es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 01","Conoce Illustrator",
        "Lee esta p&aacute;gina y descarga tus archivos de pr&aacute;ctica, luego ve al Paso 02 para hacer el recorrido. Los Pasos 01 y 02 son tu calentamiento. El proyecto empieza en el Paso 03.","#top","Back to English", HICON_DESIGN)
    es+=type_card("overview","Paso 01 &middot; Resumen y Descarga","Conoce Adobe Illustrator",
        para("Illustrator es el programa que usan los artistas y dise&ntilde;adores para hacer logotipos, &iacute;conos, carteles y arte que se puede imprimir en cualquier tama&ntilde;o. Este m&oacute;dulo es un calentamiento. Har&aacute;s un recorrido corto y guiado para aprender a moverte en el programa. No hay nada que entregar en el recorrido, as&iacute; que rel&aacute;jate y toma confianza. Tu proyecto empieza en el Paso 03, donde dibujas tu personaje.")
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
    es+=card("C&Oacute;MO FUNCIONA ESTE M&Oacute;DULO","Cinco Pasos",
        para("Este m&oacute;dulo tiene cinco pasos. Est&aacute;s en el Paso 01 ahora.")
        + bullets([
            ("Paso 01 &middot; Resumen y Descarga (est&aacute;s aqu&iacute;):","lee esta p&aacute;gina y descarga tus archivos de pr&aacute;ctica abajo."),
            ("Paso 02 &middot; Haz el Recorrido y Practica:","sigue el tutorial corto de Adobe, practica con tus archivos y luego entrega una captura de pantalla de tu espacio de trabajo de Illustrator."),
            ("Paso 03 &middot; De Boceto a Arte Vectorial:","ahora que ya sabes moverte, dibuja tu personaje en vector y entrega tus archivos .ai y .svg para poder imprimirlo en 3D."),
            ("Paso 04 &middot; Dibuja la Espalda de Tu Personaje:","agrega una segunda mesa de trabajo y haz la vista de atr&aacute;s de tu personaje, con la misma silueta, y entrega tus archivos .ai y .svg."),
            ("Paso 05 &middot; Pon Tu Personaje en una Escena:","construye una escena 16:9 panor&aacute;mica alrededor de tu personaje, muestra su escala y entrega tus archivos .ai y .svg."),
        ])
        + note("Este m&oacute;dulo no tiene reflexi&oacute;n escrita. Toma confianza en Illustrator, dibuja tu personaje de frente y de espalda, y luego construye una escena a su alrededor."))
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
    en+=card("YOUR TASK","Watch, Practice, Submit",
        para("Open Adobe Illustrator on your Mac. In this step you follow Adobe&rsquo;s short guided tour, practice with the files you downloaded in Step 01, and turn in one screen capture of your workspace."))
    en+=resources_card("Adobe Tutorial",
        para("This guided tour is made by Adobe. It has four short videos: the workspace, zooming and panning, making a new document, and saving your work. Open it, watch each one, then do the same in your own copy of Illustrator.")
        + adobe_button(False)
        + pnote("The tutorial opens on Adobe&rsquo;s own website in a new tab. Keep this page open so you can come back to it."), False)
    en+=resources_card("What the Tour Teaches",
        para("Here is what each part of the tour teaches, in short. Use it as a cheat sheet while you watch and while you practice. These steps are for a Mac.")
        + tour_notes(False), False)
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
    es+=card("TU TAREA","Mira, Practica, Entrega",
        para("Abre Adobe Illustrator en tu Mac. En este paso sigues el recorrido guiado corto de Adobe, practicas con los archivos que descargaste en el Paso 01 y entregas una captura de pantalla de tu espacio de trabajo."))
    es+=resources_card("Tutorial de Adobe",
        para("Este recorrido guiado est&aacute; hecho por Adobe. Tiene cuatro videos cortos: el espacio de trabajo, el zoom, c&oacute;mo crear un documento nuevo y c&oacute;mo guardar tu trabajo. &Aacute;brelo, mira cada uno y luego haz lo mismo en tu propia copia de Illustrator.")
        + adobe_button(True)
        + pnote("El tutorial se abre en el sitio web de Adobe en una pesta&ntilde;a nueva. Deja esta p&aacute;gina abierta para que puedas regresar."), True)
    es+=resources_card("Qu&eacute; Ense&ntilde;a el Recorrido",
        para("Esto es lo que ense&ntilde;a cada parte del recorrido, en corto. &Uacute;salo como ayuda mientras miras y mientras practicas. Estos pasos son para una Mac.")
        + tour_notes(True), True)
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
        "Take your character sketch and draw it in vector in Illustrator, then turn in two files, your .ai and your .svg, so it can be 3D printed.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
    en+=card("FROM SKETCH TO VECTOR / WHAT YOU WILL DO","Draw Your Character in Vector",
        para("Now that you know your way around Illustrator, you will take <strong>your character sketch</strong> and draw it in <strong>vector</strong>. You place your sketch in Illustrator as a guide, then build your character on top of it with clean vector shapes and lines.")
        + para("Your finished vector character can be <strong>3D printed</strong>. That is why you turn in <strong>two files</strong>: the native Illustrator file (<strong>.ai</strong>) and an exported (<strong>.svg</strong>) file. Mr. Silva needs <strong>both</strong> files to print your figure.")
        + note("Vector art is made from lines and shapes, so it never gets blurry when you make it bigger, and it gives a 3D printer a clean path to follow."))
    en+=resources_card("Adobe Tutorial",
        para("Open Adobe Illustrator, then follow this short Adobe tutorial. It is about five minutes and shows you how to bring in a sketch and trace it with the drawing tools.")
        + adobe_button(False, ADOBE_URL2)
        + pnote("The tutorial opens on Adobe&rsquo;s own website in a new tab. It also has its own practice sketch you can download there if you want one. Watch it, then try the same steps on your own sketch."), False)
    en+=resources_card("How to Build Your Character",
        para("Here are the steps in short. Use them as a cheat sheet while you work. These steps are for a Mac.")
        + sketch_notes(False), False)
    en+=card("YOU PRACTICE / ON YOUR OWN","Make Your Vector Character",
        (float_right(S3_FLOAT,"A Pioneer Valley student drawing a character into vector art in Adobe Illustrator on an iMac in the lab","Place your sketch, lock it, and draw your character on a new layer.") if HAVE_S3_FLOAT else "")
        + para("Draw your character on paper first, then photograph it with your school iPad. That sketch becomes the guide you draw over in Illustrator.")
        + bullets([
            ("Place your character sketch:","photograph your sketch with your school iPad, get it onto your Mac, then use File &gt; Place in Illustrator. Put it on its own layer and lock it as your guide."),
            ("Build your character:","on a new layer, use the Shape tools and the Pen tool to draw your character over the sketch."),
            ("Unite and color:","in the Pathfinder panel, click Unite to combine shapes into one, set your layer order, and give each shape a fill color."),
            ("Delete the sketch layer:","once your character is done, delete the sketch image layer so only your vector art is left."),
            ("Save .ai and .svg:","File &gt; Save As and pick Adobe Illustrator for the .ai, then File &gt; Save As again and pick SVG for the .svg. Turn in both files."),
        ])
        + note("When Mr. Silva has both your <strong>.ai</strong> and <strong>.svg</strong> files, he can 3D print your character. Turn in both so he can print your figure."))
    en+=deliverables_box(False,
        [("Your Illustrator file (.ai):","your finished vector character saved as a native Adobe Illustrator file. Use File &gt; Save As and pick Adobe Illustrator in the Format menu, then upload it to this Canvas assignment."),
         ("Your exported file (.svg):","the same character saved again as an SVG. Use File &gt; Save As and pick SVG in the Format menu, then upload it to this Canvas assignment."),
         ])
    en+=next_up("UP NEXT &middot; STEP 04 - Draw the Back of Your Character","Next you add a second artboard and draw the back of your character, keeping the same silhouette, so your figure has detail from every side for 3D printing.")

    es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 03","De Boceto a Arte Vectorial",
        "Toma tu boceto del personaje y dib&uacute;jalo en vector en Illustrator, luego entrega dos archivos, tu .ai y tu .svg, para poder imprimirlo en 3D.","#top","Back to English", HICON_DESIGN)
    es+=card("DE BOCETO A VECTOR / QU&Eacute; VAS A HACER","Dibuja Tu Personaje en Vector",
        para("Ahora que ya sabes moverte en Illustrator, vas a tomar <strong>tu boceto del personaje</strong> y dibujarlo en <strong>vector</strong>. Colocas tu boceto en Illustrator como gu&iacute;a, y luego construyes tu personaje encima con formas y l&iacute;neas vectoriales limpias.")
        + para("Tu personaje vectorial terminado se puede <strong>imprimir en 3D</strong>. Por eso entregas <strong>dos archivos</strong>: el archivo nativo de Illustrator (<strong>.ai</strong>) y un archivo exportado (<strong>.svg</strong>). El Sr. Silva necesita <strong>los dos</strong> para imprimir tu figura.")
        + note("El arte vectorial est&aacute; hecho de l&iacute;neas y formas, as&iacute; que nunca se ve borroso al agrandarlo, y le da a una impresora 3D un trazo limpio que seguir."))
    es+=resources_card("Tutorial de Adobe",
        para("Abre Adobe Illustrator, luego sigue este tutorial corto de Adobe. Dura unos cinco minutos y te muestra c&oacute;mo traer un boceto y calcarlo con las herramientas de dibujo.")
        + adobe_button(True, ADOBE_URL2)
        + pnote("El tutorial se abre en el sitio web de Adobe en una pesta&ntilde;a nueva. Tambi&eacute;n tiene su propio boceto de pr&aacute;ctica que puedes descargar ah&iacute; si quieres uno. M&iacute;ralo, luego prueba los mismos pasos en tu propio boceto."), True)
    es+=resources_card("C&oacute;mo Construir Tu Personaje",
        para("Estos son los pasos en corto. &Uacute;salos como ayuda mientras trabajas. Estos pasos son para una Mac.")
        + sketch_notes(True), True)
    es+=card("T&Uacute; PRACTICAS / POR TU CUENTA","Haz Tu Personaje Vectorial",
        (float_right(S3_FLOAT,"Un estudiante de Pioneer Valley dibujando un personaje a arte vectorial en Adobe Illustrator en una iMac en el laboratorio","Coloca tu boceto, bloqu&eacute;alo y dibuja tu personaje en una capa nueva.") if HAVE_S3_FLOAT else "")
        + para("Dibuja tu personaje en papel primero, luego fotograf&iacute;alo con tu iPad escolar. Ese boceto se convierte en la gu&iacute;a que dibujas encima en Illustrator.")
        + bullets([
            ("Coloca tu boceto del personaje:","fotograf&iacute;a tu boceto con tu iPad escolar, p&aacute;salo a tu Mac, luego usa Archivo &gt; Colocar en Illustrator. Ponlo en su propia capa y bloqu&eacute;alo como gu&iacute;a."),
            ("Construye tu personaje:","en una capa nueva, usa las herramientas de Forma y la Pluma para dibujar tu personaje sobre el boceto."),
            ("Une y colorea:","usa el panel Pathfinder para unir formas en una, ordena tus capas y dale un color de relleno a cada forma."),
            ("Borra la capa del boceto:","cuando tu personaje est&eacute; listo, borra la capa de la imagen del boceto para que solo quede tu arte vectorial."),
            ("Guarda .ai y .svg:","Archivo &gt; Guardar Como y elige Adobe Illustrator para el .ai, luego Archivo &gt; Guardar Como otra vez y elige SVG para el .svg. Entrega los dos archivos."),
        ])
        + note("Cuando el Sr. Silva tenga tus dos archivos, <strong>.ai</strong> y <strong>.svg</strong>, puede imprimir tu personaje en 3D. Entrega los dos para que imprima tu figura."))
    es+=deliverables_box(True,
        [("Tu archivo de Illustrator (.ai):","tu personaje vectorial terminado guardado como archivo nativo de Adobe Illustrator. Usa Archivo &gt; Guardar Como y elige Adobe Illustrator en el men&uacute; Formato, luego s&uacute;belo a esta tarea de Canvas."),
         ("Tu archivo exportado (.svg):","el mismo personaje guardado otra vez como SVG. Usa Archivo &gt; Guardar Como y elige SVG en el men&uacute; Formato, luego s&uacute;belo a esta tarea de Canvas."),
         ])
    es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 04 - Dibuja la Espalda de Tu Personaje","Luego agregas una segunda mesa de trabajo y dibujas la espalda de tu personaje, con la misma silueta, para que tu figura tenga detalle por todos lados para la impresi&oacute;n 3D.")

    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S4}" class="silva-step-btn">Step 04 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S4}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
    return wrap_page(f"Step 3: Sketch to Vector Art | Get to Know Illustrator | {CL_EN} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

def backside_notes(es):
    # Step 04 "draw the back of your character" steps, in the same locked purple scroller.
    if es:
        hint="Despl&aacute;zate dentro del cuadro para ver los pasos."
        parts=(
         _tour_part("1","Agrega una segunda mesa de trabajo",[
            ("Elige la herramienta Mesa de trabajo:","en el panel de herramientas, elige la herramienta Mesa de trabajo. Aparece un marco alrededor de tu mesa."),
            ("Mant&eacute;n Opci&oacute;n y arrastra:","mant&eacute;n presionada la tecla Opci&oacute;n y arrastra tu mesa hacia un lado. Esto copia toda la mesa y tu personaje a una segunda mesa. Presiona Escape cuando termines."),
         ])
         + _tour_part("2","Selecciona todo tu personaje",[
            ("Agr&uacute;palo primero:","haz clic en tu personaje con la herramienta Selecci&oacute;n y elige Objeto &gt; Agrupar (Cmd+G) para que todas las piezas se muevan como una."),
            ("Selecciona todo:","con la herramienta Selecci&oacute;n, haz clic en tu personaje agrupado, o elige Edici&oacute;n &gt; Seleccionar todo (Cmd+A) para tomar todas las piezas de una vez."),
         ])
         + _tour_part("3","Voltea horizontalmente",[
            ("Refleja tu personaje:","con tu personaje seleccionado, elige Objeto &gt; Transformar &gt; Reflejar. Elige el eje Vertical y haz clic en OK. Esto lo voltea de izquierda a derecha, para que mire hacia el otro lado."),
            ("La misma silueta:","voltear mantiene el mismo contorno (silueta) exacto, as&iacute; la espalda va a coincidir con el frente cuando se imprima."),
         ])
         + _tour_part("4","Convi&eacute;rtela en la espalda",[
            ("Quita los detalles del frente:","borra lo que solo se ve de frente, como la cara, los ojos y los botones."),
            ("Agrega detalles de la espalda:","usa las herramientas de Forma y la Pluma para dibujar lo que se ve por detr&aacute;s, como la parte de atr&aacute;s del cabello, una mochila, una cola o un dise&ntilde;o en la espalda. Reusa las formas que coinciden."),
            ("Combina tus colores:","usa los mismos colores de relleno para que el frente y la espalda se vean como el mismo personaje."),
         ])
         + _tour_part("5","Termina y guarda",[
            ("Ordena tus capas:","en el panel Capas, aseg&uacute;rate de que tu vista de espalda quede limpia y que no quede nada del frente."),
            ("Guarda como .ai:","Archivo &gt; Guardar Como, elige Adobe Illustrator."),
            ("Guarda una copia como .svg:","Archivo &gt; Guardar Como otra vez, elige SVG. Ya tienes los dos archivos."),
         ])
        )
    else:
        hint="Scroll inside the box to see the steps."
        parts=(
         _tour_part("1","Add a second artboard",[
            ("Pick the Artboard tool:","in the Tools panel, choose the Artboard tool. A frame appears around your artboard."),
            ("Hold Option and drag:","hold the Option key and drag your artboard to the side. This copies the whole artboard and your character onto a second artboard. Press Escape when you are done."),
         ])
         + _tour_part("2","Select your whole character",[
            ("Group it first:","click your character with the Selection tool and choose Object &gt; Group (Cmd+G) so all the pieces move as one."),
            ("Select the whole thing:","with the Selection tool, click your grouped character, or choose Edit &gt; Select All (Cmd+A) to grab every piece at once."),
         ])
         + _tour_part("3","Flip it horizontally",[
            ("Mirror your character:","with your character selected, choose Object &gt; Transform &gt; Reflect. Pick the Vertical axis and click OK. This flips it left to right, so it faces the other way."),
            ("Same silhouette:","flipping keeps the exact same outline (silhouette), so the back will line up with the front when it is printed."),
         ])
         + _tour_part("4","Make it the back",[
            ("Remove front-only details:","take away the things you only see from the front, like the face, eyes, and buttons."),
            ("Add back details:","use the Shape tools and the Pen tool to draw what you see from behind, like the back of the hair, a backpack, a tail, or a design on the back. Reuse the shapes that match."),
            ("Match your colors:","use the same fill colors so the front and back look like the same character."),
         ])
         + _tour_part("5","Finish and save",[
            ("Order your layers:","in the Layers panel, make sure your back view is clean and nothing from the front is left over."),
            ("Save as .ai:","File &gt; Save As, pick Adobe Illustrator."),
            ("Save a copy as .svg:","File &gt; Save As again, pick SVG. You now have both files."),
         ])
        )
    hintline=f'<div style="font-size:11pt;color:#c4b5fd;margin-bottom:8px;opacity:0.85;">&#8595; {hint}</div>'
    scroll=('<div class="silva-scroll" style="max-height:460px;overflow-y:auto;padding:14px 16px 20px;border:1px solid rgba(139,92,246,0.30);'
      'background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, rgba(0,0,0,0.14) 88%, rgba(139,92,246,0.16) 100%);">'
      f'{parts}</div>')
    return hintline+scroll

# ================= STEP 04: Draw the Back of Your Character =================
def step04():
    en=banner(f"Module {MODNUM} &bull; Step 04","Draw the Back of Your Character",
        "Add a second artboard and draw the back of your character in Illustrator, keeping the same silhouette, then turn in your .ai and .svg files.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
    en+=card("FRONT AND BACK / WHAT YOU WILL DO","Draw Your Character from Behind",
        para("In Step 03 you drew the <strong>front</strong> of your character. Now you draw the <strong>back</strong>. You add a <strong>second artboard</strong>, keep the <strong>same silhouette</strong> (the outer shape), and change what is inside so your figure has detail from every side.")
        + para("A 3D print needs to look right from <strong>every angle</strong>. The back view gives the printer the detail it needs so your character is not flat or blank behind.")
        + note("You <strong>duplicate</strong> your whole artboard and character, <strong>mirror</strong> the copy, then change it into the back. You do not start over."))
    en+=resources_card("How to Draw the Back",
        para("Here are the steps in short. Use them as a cheat sheet while you work. These steps are for a Mac.")
        + backside_notes(False), False)
    en+=card("YOU PRACTICE / ON YOUR OWN","Draw the Back of Your Character",
        (float_right(S4_FLOAT,"A Pioneer Valley student drawing the back view of a vector character on a second artboard in Adobe Illustrator","Duplicate your artboard and turn the copy into the back view.") if HAVE_S4_FLOAT else "")
        + para("Duplicate your artboard, keep the outline the same, and turn the copy into the back view.")
        + bullets([
            ("Add a second artboard:","pick the Artboard tool, hold Option, and drag your artboard to the side to copy it and your character."),
            ("Select your whole character:","group it with Object &gt; Group (Cmd+G), then click it with the Selection tool, or use Edit &gt; Select All (Cmd+A)."),
            ("Flip it horizontally:","choose Object &gt; Transform &gt; Reflect, pick the Vertical axis, and click OK. Your character mirrors left to right and keeps the same silhouette."),
            ("Make it the back:","remove front-only details like the face, then add back details like the back of the hair, a backpack, or a design. Reuse the shapes that match and keep the same colors."),
            ("Save .ai and .svg:","File &gt; Save As and pick Adobe Illustrator for the .ai, then File &gt; Save As again and pick SVG for the .svg. Turn in both files."),
        ])
        + note("Keeping the <strong>same silhouette</strong> is the key, so the front and back line up when printed. One tip: if your character has any letters or numbers on it, flip those back so they still read the right way."))
    en+=deliverables_box(False,
        [("Your Illustrator file (.ai):","your character with its back view on a second artboard, saved as a native Adobe Illustrator file. File &gt; Save As, pick Adobe Illustrator, then upload it to this Canvas assignment."),
         ("Your exported file (.svg):","the same file saved again as an SVG. File &gt; Save As again, pick SVG, then upload it to this Canvas assignment."),
         ])
    en+=next_up("UP NEXT &middot; STEP 05 - Put Your Character in a Scene","Next you build a 16:9 widescreen scene around your character and show its scale, then turn in your .ai and .svg files.")

    es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 04","Dibuja la Espalda de Tu Personaje",
        "Agrega una segunda mesa de trabajo y dibuja la espalda de tu personaje en Illustrator, con la misma silueta, luego entrega tus archivos .ai y .svg.","#top","Back to English", HICON_DESIGN)
    es+=card("FRENTE Y ESPALDA / QU&Eacute; VAS A HACER","Dibuja Tu Personaje por Detr&aacute;s",
        para("En el Paso 03 dibujaste el <strong>frente</strong> de tu personaje. Ahora dibujas la <strong>espalda</strong>. Agregas una <strong>segunda mesa de trabajo</strong>, mantienes la <strong>misma silueta</strong> (la forma de afuera) y cambias lo de adentro para que tu figura tenga detalle por todos lados.")
        + para("Una impresi&oacute;n 3D tiene que verse bien desde <strong>todos los &aacute;ngulos</strong>. La vista de espalda le da a la impresora el detalle que necesita para que tu personaje no quede plano ni vac&iacute;o por detr&aacute;s.")
        + note("<strong>Duplicas</strong> toda tu mesa de trabajo y tu personaje, <strong>reflejas</strong> la copia y luego la conviertes en la espalda. No empiezas de nuevo."))
    es+=resources_card("C&oacute;mo Dibujar la Espalda",
        para("Estos son los pasos en corto. &Uacute;salos como ayuda mientras trabajas. Estos pasos son para una Mac.")
        + backside_notes(True), True)
    es+=card("T&Uacute; PRACTICAS / POR TU CUENTA","Dibuja la Espalda de Tu Personaje",
        (float_right(S4_FLOAT,"Un estudiante de Pioneer Valley dibujando la vista de espalda de un personaje vectorial en una segunda mesa de trabajo en Adobe Illustrator","Duplica tu mesa de trabajo y convierte la copia en la vista de espalda.") if HAVE_S4_FLOAT else "")
        + para("Duplica tu mesa de trabajo, mant&eacute;n el contorno igual y convierte la copia en la vista de espalda.")
        + bullets([
            ("Agrega una segunda mesa:","elige la herramienta Mesa de trabajo, mant&eacute;n Opci&oacute;n y arrastra tu mesa hacia un lado para copiarla junto con tu personaje."),
            ("Selecciona todo tu personaje:","agr&uacute;palo con Objeto &gt; Agrupar (Cmd+G), luego haz clic en &eacute;l con la herramienta Selecci&oacute;n, o usa Edici&oacute;n &gt; Seleccionar todo (Cmd+A)."),
            ("Voltea horizontalmente:","elige Objeto &gt; Transformar &gt; Reflejar, elige el eje Vertical y haz clic en OK. Tu personaje se refleja de izquierda a derecha y mantiene la misma silueta."),
            ("Convi&eacute;rtela en la espalda:","quita los detalles del frente como la cara, luego agrega detalles de la espalda como la parte de atr&aacute;s del cabello, una mochila o un dise&ntilde;o. Reusa las formas que coinciden y mant&eacute;n los mismos colores."),
            ("Guarda .ai y .svg:","Archivo &gt; Guardar Como y elige Adobe Illustrator para el .ai, luego Archivo &gt; Guardar Como otra vez y elige SVG para el .svg. Entrega los dos archivos."),
        ])
        + note("Mantener la <strong>misma silueta</strong> es la clave, para que el frente y la espalda se alineen al imprimir. Un consejo: si tu personaje tiene letras o n&uacute;meros, voltea esos de nuevo para que se lean bien."))
    es+=deliverables_box(True,
        [("Tu archivo de Illustrator (.ai):","tu personaje con su vista de espalda en una segunda mesa de trabajo, guardado como archivo nativo de Adobe Illustrator. Archivo &gt; Guardar Como, elige Adobe Illustrator, luego s&uacute;belo a esta tarea de Canvas."),
         ("Tu archivo exportado (.svg):","el mismo archivo guardado otra vez como SVG. Archivo &gt; Guardar Como otra vez, elige SVG, luego s&uacute;belo a esta tarea de Canvas."),
         ])
    es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 05 - Pon Tu Personaje en una Escena","Luego construyes una escena 16:9 panor&aacute;mica alrededor de tu personaje y muestras su escala, luego entregas tus archivos .ai y .svg.")

    stepnav=f'<a href="{S3}" class="silva-step-btn">&#8592; Step 03</a> <a href="{S5}" class="silva-step-btn">Step 05 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S3}" class="silva-bottom-btn">&#8592; Step 03</a><a href="{S5}" class="silva-bottom-btn">Step 05 &#8594;</a></div>'
    return wrap_page(f"Step 4: Draw the Back of Your Character | Get to Know Illustrator | {CL_EN} | PVHS", nav("Step 04",dots_for(3),stepnav), top_wrap(en,es), bottom)

def scene_notes(es):
    # Step 05 "put your character in a scene" steps, in the same locked purple scroller.
    if es:
        hint="Despl&aacute;zate dentro del cuadro para ver los pasos."
        parts=(
         _tour_part("1","Mesa de trabajo panor&aacute;mica",[
            ("Archivo &gt; Nuevo:","abre la ventana de Documento Nuevo para empezar un archivo nuevo."),
            ("Hazla 16:9 panor&aacute;mica:","pon el tama&ntilde;o en forma 16:9, como 1920 por 1080 p&iacute;xeles. Es una forma ancha, como una pantalla de cine."),
            ("Modo de color RGB:","abre Opciones Avanzadas y elige Color RGB. RGB es el modo de color para arte que se ve en una pantalla."),
         ])
         + _tour_part("2","Dise&ntilde;a tu fondo",[
            ("Construye la escena:","usa las herramientas de Forma y la Pluma para hacer el mundo detr&aacute;s de tu personaje: un cuarto, un paisaje, el cielo, donde viva tu personaje."),
            ("Agrega color:","dale colores de relleno a las formas del fondo para que la escena se sienta real."),
            ("En su propia capa:","pon el fondo en una capa debajo de tu personaje."),
         ])
         + _tour_part("3","Trae tu personaje",[
            ("Abre tu archivo del Paso 03:","abre el .ai del personaje que hiciste el paso pasado. No lo vuelves a dibujar."),
            ("Copia y pega:","selecciona tu personaje, c&oacute;pialo y p&eacute;galo en tu escena. Col&oacute;calo donde va."),
         ])
         + _tour_part("4","Muestra la escala",[
            ("Agrega objetos de tama&ntilde;o:","pon objetos en la escena que muestren qu&eacute; tan grande o peque&ntilde;o es tu personaje. Un personaje diminuto junto a una flor gigante, o uno enorme junto a una casita."),
            ("Usa cosas conocidas:","usa objetos cuyo tama&ntilde;o el p&uacute;blico ya conoce, para que entiendan el tama&ntilde;o de tu personaje de un vistazo."),
         ])
         + _tour_part("5","Termina y guarda",[
            ("Ordena tus capas:","en el panel Capas, aseg&uacute;rate de que tu personaje quede delante del fondo."),
            ("Guarda como .ai:","Archivo &gt; Guardar Como, elige Adobe Illustrator."),
            ("Guarda una copia como .svg:","Archivo &gt; Guardar Como otra vez, elige SVG. Ya tienes los dos archivos."),
         ])
        )
    else:
        hint="Scroll inside the box to see the steps."
        parts=(
         _tour_part("1","New widescreen artboard",[
            ("File &gt; New:","open the New Document window to start a fresh file."),
            ("Make it 16:9 widescreen:","set the size to a 16:9 shape, like 1920 by 1080 pixels. That is a wide, movie-screen shape."),
            ("Set the color mode to RGB:","open Advanced Options and choose RGB Color. RGB is the color mode for art made to be seen on a screen."),
         ])
         + _tour_part("2","Design your background",[
            ("Build the scene:","use the Shape tools and the Pen tool to make the world behind your character: a room, a landscape, the sky, wherever your character lives."),
            ("Add color:","give your background shapes fill colors so the scene feels real."),
            ("Keep it on its own layer:","put the background on a layer below your character."),
         ])
         + _tour_part("3","Bring in your character",[
            ("Open your Step 03 file:","open the character .ai you made last step. You do not redraw it."),
            ("Copy and paste:","select your character, copy it, then paste it into your scene. Place it where it belongs."),
         ])
         + _tour_part("4","Show the scale",[
            ("Add objects for size:","put objects in the scene that show how big or small your character is: a tiny character next to a giant flower, or a huge character next to a little house."),
            ("Pick things we know:","use objects the viewer already knows the size of, so they can read your character&rsquo;s size at a glance."),
         ])
         + _tour_part("5","Finish and save",[
            ("Order your layers:","in the Layers panel, make sure your character sits in front of the background."),
            ("Save as .ai:","File &gt; Save As, pick Adobe Illustrator."),
            ("Save a copy as .svg:","File &gt; Save As again, pick SVG. You now have both files."),
         ])
        )
    hintline=f'<div style="font-size:11pt;color:#c4b5fd;margin-bottom:8px;opacity:0.85;">&#8595; {hint}</div>'
    scroll=('<div class="silva-scroll" style="max-height:460px;overflow-y:auto;padding:14px 16px 20px;border:1px solid rgba(139,92,246,0.30);'
      'background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, rgba(0,0,0,0.14) 88%, rgba(139,92,246,0.16) 100%);">'
      f'{parts}</div>')
    return hintline+scroll

# ================= STEP 05: Put Your Character in a Scene =================
def step05():
    en=banner(f"Module {MODNUM} &bull; Step 05","Put Your Character in a Scene",
        "Build a 16:9 widescreen scene around your character in Illustrator, then turn in your .ai and .svg files.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
    en+=card("YOUR CHARACTER&rsquo;S WORLD / WHAT YOU WILL DO","Give Your Character a Scene",
        para("In Step 03 you drew your character in vector. Now you give them a <strong>world</strong>. You will make a <strong>16:9 widescreen</strong> artboard in <strong>RGB</strong> color, design a <strong>background scene</strong>, and place your character into it.")
        + para("The big idea is <strong>scale</strong>. Add objects to the scene that show how big or small your character is, so the viewer can tell their size at a glance.")
        + note("You do <strong>not</strong> redraw your character. Bring in the one you already made in Step 03."))
    en+=resources_card("How to Build Your Scene",
        para("Here are the steps in short. Use them as a cheat sheet while you work. These steps are for a Mac.")
        + scene_notes(False), False)
    en+=card("YOU PRACTICE / ON YOUR OWN","Make Your Scene",
        (float_right(S4_FLOAT,"A Pioneer Valley student designing a widescreen scene around a vector character in Adobe Illustrator","Place your character in a scene that shows its scale.") if HAVE_S4_FLOAT else "")
        + para("Build the scene around your character and make its size clear.")
        + bullets([
            ("New 16:9 RGB artboard:","File &gt; New. Set the size to a 16:9 widescreen shape like 1920 by 1080, and set the Color Mode to RGB in Advanced Options."),
            ("Design a background:","use the Shape tools and the Pen tool to build the world behind your character, on a layer below it, and give it color."),
            ("Bring in your character:","open your Step 03 .ai, copy your character, and paste it into the scene. Do not redraw it."),
            ("Show the scale:","add objects the viewer knows the size of, so your character&rsquo;s size reads at a glance."),
            ("Save .ai and .svg:","File &gt; Save As and pick Adobe Illustrator for the .ai, then File &gt; Save As again and pick SVG for the .svg. Turn in both files."),
        ])
        + note("Have fun building your character&rsquo;s world. Keep your character in front and your background behind."))
    en+=deliverables_box(False,
        [("Your Illustrator file (.ai):","your finished scene with your character in it, saved as a native Adobe Illustrator file. File &gt; Save As, pick Adobe Illustrator, then upload it to this Canvas assignment."),
         ("Your exported file (.svg):","the same scene saved again as an SVG. File &gt; Save As, pick SVG, then upload it to this Canvas assignment."),
         ])
    en+=next_up("MODULE COMPLETE","Nice work. You drew your character and built a scene that shows its scale, and you turned in your .ai and .svg files. You are ready for your next Illustrator project.")

    es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 05","Pon Tu Personaje en una Escena",
        "Construye una escena 16:9 panor&aacute;mica alrededor de tu personaje en Illustrator, luego entrega tus archivos .ai y .svg.","#top","Back to English", HICON_DESIGN)
    es+=card("EL MUNDO DE TU PERSONAJE / QU&Eacute; VAS A HACER","Dale una Escena a Tu Personaje",
        para("En el Paso 03 dibujaste tu personaje en vector. Ahora le das un <strong>mundo</strong>. Vas a hacer una mesa de trabajo <strong>16:9 panor&aacute;mica</strong> en color <strong>RGB</strong>, dise&ntilde;ar un <strong>fondo</strong> y colocar tu personaje en &eacute;l.")
        + para("La idea principal es la <strong>escala</strong>. Agrega objetos a la escena que muestren qu&eacute; tan grande o peque&ntilde;o es tu personaje, para que el p&uacute;blico entienda su tama&ntilde;o de un vistazo.")
        + note("<strong>No</strong> vuelves a dibujar tu personaje. Trae el que ya hiciste en el Paso 03."))
    es+=resources_card("C&oacute;mo Construir Tu Escena",
        para("Estos son los pasos en corto. &Uacute;salos como ayuda mientras trabajas. Estos pasos son para una Mac.")
        + scene_notes(True), True)
    es+=card("T&Uacute; PRACTICAS / POR TU CUENTA","Haz Tu Escena",
        (float_right(S4_FLOAT,"Un estudiante de Pioneer Valley dise&ntilde;ando una escena panor&aacute;mica alrededor de un personaje vectorial en Adobe Illustrator","Coloca tu personaje en una escena que muestre su escala.") if HAVE_S4_FLOAT else "")
        + para("Construye la escena alrededor de tu personaje y deja clara su escala.")
        + bullets([
            ("Mesa 16:9 en RGB:","Archivo &gt; Nuevo. Pon el tama&ntilde;o en forma 16:9 panor&aacute;mica como 1920 por 1080, y pon el Modo de Color en RGB en Opciones Avanzadas."),
            ("Dise&ntilde;a un fondo:","usa las herramientas de Forma y la Pluma para construir el mundo detr&aacute;s de tu personaje, en una capa debajo de &eacute;l, y dale color."),
            ("Trae tu personaje:","abre tu .ai del Paso 03, copia tu personaje y p&eacute;galo en la escena. No lo vuelvas a dibujar."),
            ("Muestra la escala:","agrega objetos cuyo tama&ntilde;o el p&uacute;blico conoce, para que el tama&ntilde;o de tu personaje se entienda de un vistazo."),
            ("Guarda .ai y .svg:","Archivo &gt; Guardar Como y elige Adobe Illustrator para el .ai, luego Archivo &gt; Guardar Como otra vez y elige SVG para el .svg. Entrega los dos archivos."),
        ])
        + note("Divi&eacute;rtete construyendo el mundo de tu personaje. Mant&eacute;n tu personaje adelante y tu fondo atr&aacute;s."))
    es+=deliverables_box(True,
        [("Tu archivo de Illustrator (.ai):","tu escena terminada con tu personaje, guardada como archivo nativo de Adobe Illustrator. Archivo &gt; Guardar Como, elige Adobe Illustrator, luego s&uacute;belo a esta tarea de Canvas."),
         ("Tu archivo exportado (.svg):","la misma escena guardada otra vez como SVG. Archivo &gt; Guardar Como, elige SVG, luego s&uacute;belo a esta tarea de Canvas."),
         ])
    es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Dibujaste tu personaje y construiste una escena que muestra su escala, y entregaste tus archivos .ai y .svg. Est&aacute;s listo para tu pr&oacute;ximo proyecto de Illustrator.")

    stepnav=f'<a href="{S4}" class="silva-step-btn">&#8592; Step 04</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S4}" class="silva-bottom-btn">&#8592; Step 04</a><span></span></div>'
    return wrap_page(f"Step 5: Put Your Character in a Scene | Get to Know Illustrator | {CL_EN} | PVHS", nav("Step 05",dots_for(4),stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S2,step02),(S3,step03),(S4,step04),(S5,step05)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
