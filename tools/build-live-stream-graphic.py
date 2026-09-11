#!/usr/bin/env python3
# Digital Arts 1A - Module 05: Live Stream Graphic (Photoshop how-to).
# Guided, step-by-step: build the "History 301 Live Stream" promo in Photoshop.
# Stripped from Adobe CIB 2025 Lesson 1 to a 5th-grade reading level, production steps only
# (no work-area touring, no Generative Fill). NO reflection (it is a guided how-to).
# Overview + 1 step, bilingual EN/ES. End-example float image on the Overview; no header image;
# no image on Step 01 (the picture-by-picture guide is the Lesson Slides PDF, added later).
# Chip-header framework via silva_framework. Module-specific: scrollable 13-step guide (scrollbox +
# phase) kept as the content of a purple Module Resource card.
import os, re
from silva_framework import *

ROOT=os.path.join(os.path.dirname(__file__),"..")
END_IMG=f"{SITE}/assets/images/digarts1/live-stream-graphic/live-stream-end-example-v1.jpg"
ASSETS_ZIP=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Assets.zip"
SLIDES_PDF=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Slides.pdf"
AREA="Digital Arts Folder"   # OneDrive top folder for this course's project folders

OVER="digarts1-live-stream-graphic-overview.html"
S1="digarts1-live-stream-graphic-step01.html"

def downloads_block(es):
    # Orange Downloads section (Overview only). This module holds the project files and the
    # lesson slides. Both buttons share one flex-wrap row.
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Consigue aqu&iacute; los archivos del proyecto antes de empezar. Las Diapositivas de la Lecci&oacute;n muestran una imagen de cada paso." if es
          else "Grab the project files here before you start. The Lesson Slides show a picture for every step.")
    zlabel="Archivos del Proyecto (ZIP)" if es else "Project Files (ZIP)"
    slabel="Diapositivas de la Lecci&oacute;n (PDF)" if es else "Lesson Slides (PDF)"
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ASSETS_ZIP,zlabel,row=True)
      + dl_link(SLIDES_PDF,slabel,row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Live Stream Graphic</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

def dots_for(active_idx):
    hrefs=[OVER,S1]; titles=[("M","Overview"),("1","Step 01")]
    r=""
    for i,(lab,title) in enumerate(titles):
        r+=dot("" if i==active_idx else hrefs[i], lab, title, i==active_idx, module=(i==0 and active_idx!=0))
    return r

def scrollbox(es, inner):
    # Long step sequence in a contained scroll panel so the page looks less intimidating.
    # Purple accents: this guide is the content of the purple Module Resource card (cohesion).
    hint=('Scroll inside the box to see all 13 steps' if not es else 'Despl&aacute;zate en el cuadro para ver los 13 pasos')
    return (f'<div style="font-size:11pt;color:#c4b5fd;margin-bottom:8px;opacity:0.85;">&#8595; {hint}</div>'
      '<div class="silva-scroll" style="max-height:520px;overflow-y:auto;padding:16px 18px 20px;border:1px solid rgba(139,92,246,0.28);border-radius:14px;'
      'background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, rgba(0,0,0,0.14) 88%, rgba(139,92,246,0.16) 100%);">'
      f'{inner}</div>')

def phase(title, items, intro=''):
    # One lesson phase inside the scroll panel: a purple left-accent bar, the phase title, then
    # the numbered steps with purple badges to match the Module Resource section.
    introhtml=(f'<div style="margin-bottom:10px;line-height:1.6;"><span style="font-size:13pt;color:rgba(255,255,255,0.86);">{intro}</span></div>' if intro else '')
    return ('<div style="border-left:4px solid #8b5cf6;padding:2px 0 2px 16px;margin:0 0 22px;">'
      f'<div style="font-size:15pt;color:#ffffff;margin-bottom:8px;"><strong>{title}</strong></div>'
      f'{introhtml}{steps(items, "#8b5cf6")}</div>')

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Digital Arts 1A &bull; Module 05","Live Stream Graphic","Follow the steps to build a live stream promo image in Photoshop.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Build a Live Stream Graphic",
        float_right(END_IMG,"Finished History 301 Live Stream graphic: an arch photo with an orange bar on the left, a blue bar on the right, a green wash, and the words HISTORY 301 and LIVE STREAM in white","What your finished graphic will look like.")
        + para("In this project you follow clear steps in Adobe Photoshop to build a live stream promo graphic. Everyone starts from the same photo and follows the same steps, so all your graphics will come out looking alike.")
        + para("You will make a new Photoshop file, add a photo, add two colored bars, add the words &ldquo;History 301&rdquo; and &ldquo;Live Stream,&rdquo; add a green color wash, paint a blue spatter, move the photo and use Generative Fill to fill the gap, and export your finished image to turn in.")
        + note("This is a follow-along how-to, not a free-choice project. Do the steps in order so your result matches the example."))
    en+=downloads_block(False)
    en+=card("SKILLS / WHAT YOU WILL LEARN","New Photoshop Skills",
        para("This project teaches you the basics you will use in every Photoshop project after this one:")
        + bullets([
            ("Start a file:","make a new Photoshop document the right size."),
            ("Add a photo:","place a photo into your design and size it."),
            ("Select and fill:","use the Rectangular Marquee to make a box and fill it with color."),
            ("Add type:","add and style words (text) on your image."),
            ("Layers and blending:","stack layers and use a blending mode to mix colors."),
            ("Adjustment layers and AI:","add a solid color layer, and use Generative Fill to extend the photo."),
            ("Export:","save a finished copy to hand in."),
        ]))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Layer","One level of your image. Layers stack on top of each other, and you can edit one without changing the others."),
           ("Selection","The part of the image you mark off to work on. A moving dashed line shows the edge."),
           ("Fill","To pour a color into a selection or a layer."),
           ("Type","Words (text) you add to your image. Type sits on its own layer."),
           ("Blending Mode","A setting that changes how a layer&rsquo;s colors mix with the layers under it."),
           ("Export","To save a finished copy of your work as a JPG or PNG to share or hand in.")]), False)

    es=banner("Arte Digital 1A &bull; M&oacute;dulo 05","Gr&aacute;fico de Live Stream","Sigue los pasos para crear una imagen promocional de live stream en Photoshop.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","Crea un Gr&aacute;fico de Live Stream",
        float_right(END_IMG,"Gr&aacute;fico terminado de History 301 Live Stream: una foto de un arco con una barra naranja a la izquierda, una barra azul a la derecha, un ba&ntilde;o verde y las palabras HISTORY 301 y LIVE STREAM en blanco","As&iacute; se ver&aacute; tu gr&aacute;fico terminado.")
        + para("En este proyecto sigues pasos claros en Adobe Photoshop para crear un gr&aacute;fico promocional de live stream. Todos empiezan con la misma foto y siguen los mismos pasos, as&iacute; que todos los gr&aacute;ficos quedar&aacute;n parecidos.")
        + para("Vas a crear un archivo nuevo de Photoshop, agregar una foto, agregar dos barras de color, agregar las palabras &ldquo;History 301&rdquo; y &ldquo;Live Stream,&rdquo; agregar un ba&ntilde;o de color verde, pintar un salpicado azul, mover la foto y usar Relleno Generativo para llenar el hueco, y exportar tu imagen terminada para entregar.")
        + note("Esto es un instructivo para seguir paso a paso, no un proyecto de elecci&oacute;n libre. Haz los pasos en orden para que tu resultado se parezca al ejemplo."))
    es+=downloads_block(True)
    es+=card("HABILIDADES / LO QUE APRENDER&Aacute;S","Nuevas Habilidades de Photoshop",
        para("Este proyecto te ense&ntilde;a lo b&aacute;sico que usar&aacute;s en cada proyecto de Photoshop despu&eacute;s de este:")
        + bullets([
            ("Crear un archivo:","haz un documento nuevo de Photoshop del tama&ntilde;o correcto."),
            ("Agregar una foto:","coloca una foto en tu dise&ntilde;o y ajusta su tama&ntilde;o."),
            ("Seleccionar y rellenar:","usa el Marco Rectangular para hacer una caja y rellenarla con color."),
            ("Agregar texto:","agrega y da estilo a las palabras (texto) en tu imagen."),
            ("Capas y mezcla:","apila capas y usa un modo de fusi&oacute;n para mezclar colores."),
            ("Capas de ajuste e IA:","agrega una capa de color s&oacute;lido y usa Relleno Generativo para extender la foto."),
            ("Exportar:","guarda una copia terminada para entregar."),
        ]))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Layer (Capa)","Un nivel de tu imagen. Las capas se apilan una sobre otra y puedes editar una sin cambiar las dem&aacute;s."),
           ("Selection (Selecci&oacute;n)","La parte de la imagen que marcas para trabajar. Una l&iacute;nea punteada en movimiento muestra el borde."),
           ("Fill (Rellenar)","Poner un color dentro de una selecci&oacute;n o una capa."),
           ("Type (Texto)","Las palabras que agregas a tu imagen. El texto va en su propia capa."),
           ("Blending Mode (Modo de Fusi&oacute;n)","Un ajuste que cambia c&oacute;mo se mezclan los colores de una capa con las capas de abajo."),
           ("Export (Exportar)","Guardar una copia terminada de tu trabajo como JPG o PNG para compartir o entregar.")]), True)

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Live Stream Graphic | Digital Arts 1A | PVHS", nav("Overview",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Live Stream Graphic &bull; Step 1","Build It in Photoshop","Follow the steps in order to build your graphic.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 image:","your finished Live Stream graphic (01Working.jpg), uploaded to this Canvas assignment.")])
    en+=card("BEFORE YOU START / THE SLIDES","Follow Along With the Slides",
        para("Do these steps in Adobe Photoshop, in order. The Lesson Slides show a picture for each step, so open them next to Photoshop as you work.")
        + dl_row(SLIDES_PDF,"Lesson Slides (PDF)")
        + note("Use color codes exactly as written (like ff7f00) so your colors match the example."))
    en+=resources_card("Build Your Graphic",
        para("Do these steps in Adobe Photoshop, in order. Scroll through the box below, and open the Lesson Slides to see a picture for each step.")
        + scrollbox(False,
            phase("Step 1 &middot; New Document",[
                ("Open Photoshop.",""),
                ("Make a new file:","choose File &gt; New. Click the Film &amp; Video tab, then click the HDTV 1080p preset (1920 by 1080). Click Create."),
                ("Save it:","choose File &gt; Save As, name it 01Working, and click Save. Click OK if a box pops up."),
            ])
            + phase("Step 2 &middot; Place the Photo",[
                ("Place the photo:","choose File &gt; Place Embedded. Find Arch.jpg in your project files, and click Place."),
                ("Fill the width:","drag a corner handle out so the photo covers the whole width of the canvas."),
                ("Lock it in:","click the checkmark in the top bar, or press Enter (Windows) or Return (Mac)."),
            ],intro="Do not center the building yet. You move it near the end.")
            + phase("Step 3 &middot; Set Units to Pixels",[
                ("Open the setting:","choose Edit &gt; Preferences &gt; Units &amp; Rulers (Windows) or Photoshop &gt; Settings &gt; Units &amp; Rulers (Mac)."),
                ("Choose pixels:","set Rulers to Pixels, and click OK. You only do this once."),
            ])
            + phase("Step 4 &middot; New Layer",[
                ("Pick the layer:","in the Layers panel, click the Arch layer."),
                ("Add a layer:","click the Create a New Layer button at the bottom of the Layers panel."),
                ("Name it:","double-click the new layer&rsquo;s name, type Rectangles, and press Enter or Return."),
            ])
            + phase("Step 5 &middot; Orange Bar",[
                ("Get ready:","make sure the Rectangles layer is selected. Pick the Rectangular Marquee tool (press M)."),
                ("Draw the box:","start just outside the top-left corner and drag down and right. Release when the info reads W 96px and H 1080px."),
                ("Fill it orange:","in the Contextual Task Bar, click Fill Selection, then Fill Color. Type ff7f00 in the # field, click OK, then OK again."),
                ("Clear it:","choose Select &gt; Deselect."),
            ])
            + phase("Step 6 &middot; Blue Bar",[
                ("Draw the box:","with the Rectangular Marquee tool, start just outside the top-right corner and drag down and left. Release when the info reads W 660px and H 1080px."),
                ("Fill it blue:","choose Edit &gt; Fill. Set Contents to Color, type 0053b2, and click OK, then OK again."),
                ("Clear it:","choose Select &gt; Deselect."),
            ])
            + phase("Step 7 &middot; Color Blend Mode",[
                ("Blend the bars:","in the Layers panel, click the blend mode menu (it says Normal) at the top-left, and choose Color. Now the photo shows through both bars."),
                ("Save:","choose File &gt; Save."),
            ])
            + phase("Step 8 &middot; Title Text",[
                ("Set up type:","pick the Horizontal Type tool (press T). In the top bar, choose a bold serif font (the deck uses Abril Fatface), set the size to 210 pt, click Center, and set the color to white (ffffff)."),
                ("Turn on All Caps:","in the Properties panel, click the All Caps (TT) button."),
                ("Type the title:","click near the lower-center of the canvas and type History 301. It shows as HISTORY 301."),
                ("Finish:","click the checkmark, or press Ctrl+Enter (Windows) or Cmd+Return (Mac). Do not press plain Enter."),
                ("Center it:","pick the Move tool (press V) and drag the words to center them."),
            ])
            + phase("Step 9 &middot; Subtitle Text",[
                ("Start a new line:","choose Select &gt; Deselect Layers so Photoshop makes a new type layer."),
                ("Change the type:","with the Type tool, change the font to a condensed bold italic (the deck uses Acumin Pro Condensed Black Italic), set the size to 165 pt, and click Right align."),
                ("Type it:","click near the right side, about two-thirds down the canvas, and type Live Stream. It shows as LIVE STREAM."),
                ("Finish:","click the checkmark to commit."),
            ])
            + phase("Step 10 &middot; Solid Color Layer",[
                ("Pick the layer:","in the Layers panel, click the Arch layer."),
                ("Add a solid color:","click the Create New Fill or Adjustment Layer button (the half-filled circle) at the bottom of the Layers panel, and choose Solid Color."),
                ("Choose dark green:","type 0c3303, and click OK."),
                ("Blend it in:","set this layer&rsquo;s blend mode to Hard Light, then change its Opacity to 90%."),
                ("Hide the guides:","choose View &gt; Show &gt; Guides to turn off the cyan guides."),
            ],intro="This dark green layer makes the white text easier to read.")
            + phase("Step 11 &middot; Sample and Paint",[
                ("Sample a blue:","pick the Eyedropper tool (press I) and click a lighter blue area on the right side to load that color."),
                ("Brighten it:","choose Window &gt; Color. From the panel menu, choose Web Color Sliders, type 4099ff, and press Enter."),
                ("Make a paint layer:","in the Layers panel, click the Rectangles layer. Hold Alt (Windows) or Option (Mac) and click the Create a New Layer button. Name it Paint, and click OK."),
                ("Pick a spatter brush:","pick the Brush tool (press B). Choose Window &gt; Brushes, open the Special Effects Brushes group, and pick Kyle&rsquo;s Spatter Brushes - Spatter Bot Tilt. Set the brush Size to 80px."),
                ("Paint it:","with the Paint layer selected, drag in small circles over the word LIVE to build up a blue spatter. Choose File &gt; Save."),
            ])
            + phase("Step 12 &middot; Move and Generative Fill",[
                ("Set up the Move tool:","pick the Move tool (press V). In the top bar, uncheck Auto-Select."),
                ("Center the building:","in the Layers panel, click the Arch layer. Drag the photo on the canvas until the building is centered in the green area. A gap shows on the left."),
                ("See the gap:","hold Alt (Windows) or Option (Mac) and click the eye icon on the Arch layer to hide the other layers."),
                ("Select the gap:","pick the Rectangular Marquee tool (press M) and drag to select the empty left gap. Overlap the photo edge a little."),
                ("Fill it with AI:","click the Arch layer in the Layers panel. In the Contextual Task Bar, click Generative Fill, leave the box blank, and click Generate. Click Agree if asked."),
                ("Select the best:","in the Properties panel, click each Variation and choose the one that looks most natural."),
                ("Show everything:","right-click (Windows) or Control-click (Mac) the eye icon on the Generative Fill layer, and choose Show/Hide All Other Layers. Choose File &gt; Save."),
            ])
            + phase("Step 13 &middot; Export",[
                ("Open Export As:","choose File &gt; Export &gt; Export As."),
                ("Set the file type:","set Format to JPG and Quality to 6."),
                ("Set the size:","set Width to 1280 and press Tab. The Height becomes 720."),
                ("Match the colors:","make sure Convert to sRGB and Embed Color Profile are on."),
                ("Save the copy:","click Export, name it 01Working, and click Save."),
            ])
        ), False)

    es=banner("Gr&aacute;fico de Live Stream &bull; Paso 1","Cr&eacute;alo en Photoshop","Sigue los pasos en orden para crear tu gr&aacute;fico.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 imagen:","tu gr&aacute;fico de Live Stream terminado (01Working.jpg), subido a esta tarea de Canvas.")])
    es+=card("ANTES DE EMPEZAR / LAS DIAPOSITIVAS","Sigue las Diapositivas",
        para("Haz estos pasos en Adobe Photoshop, en orden. Las Diapositivas de la Lecci&oacute;n muestran una imagen de cada paso, as&iacute; que &aacute;brelas junto a Photoshop mientras trabajas.")
        + dl_row(SLIDES_PDF,"Diapositivas de la Lecci&oacute;n (PDF)")
        + note("Usa los c&oacute;digos de color tal como est&aacute;n escritos (como ff7f00) para que tus colores coincidan con el ejemplo."))
    es+=resources_card("Crea Tu Gr&aacute;fico",
        para("Haz estos pasos en Adobe Photoshop, en orden. Despl&aacute;zate por el cuadro de abajo y abre las Diapositivas de la Lecci&oacute;n para ver una imagen de cada paso.")
        + scrollbox(True,
            phase("Paso 1 &middot; Documento Nuevo",[
                ("Abre Photoshop.",""),
                ("Crea un archivo nuevo:","elige Archivo &gt; Nuevo. Haz clic en la pesta&ntilde;a Cine y Video, luego en el ajuste HDTV 1080p (1920 por 1080). Haz clic en Crear."),
                ("Gu&aacute;rdalo:","elige Archivo &gt; Guardar Como, nombra el archivo 01Working y haz clic en Guardar. Haz clic en OK si aparece un cuadro."),
            ])
            + phase("Paso 2 &middot; Coloca la Foto",[
                ("Coloca la foto:","elige Archivo &gt; Colocar Incrustado. Busca Arch.jpg en tus archivos del proyecto y haz clic en Colocar."),
                ("Llena el ancho:","arrastra una esquina hacia afuera para que la foto cubra todo el ancho del lienzo."),
                ("F&iacute;jala:","haz clic en la palomita de la barra de arriba, o presiona Enter (Windows) o Return (Mac)."),
            ],intro="No centres el edificio todav&iacute;a. Lo mueves casi al final.")
            + phase("Paso 3 &middot; Pon las Unidades en P&iacute;xeles",[
                ("Abre el ajuste:","elige Edici&oacute;n &gt; Preferencias &gt; Unidades y Reglas (Windows) o Photoshop &gt; Ajustes &gt; Unidades y Reglas (Mac)."),
                ("Elige p&iacute;xeles:","pon Reglas en P&iacute;xeles y haz clic en OK. Solo lo haces una vez."),
            ])
            + phase("Paso 4 &middot; Capa Nueva",[
                ("Elige la capa:","en el panel Capas, haz clic en la capa Arch."),
                ("Agrega una capa:","haz clic en el bot&oacute;n Crear una Capa Nueva abajo del panel Capas."),
                ("N&oacute;mbrala:","haz doble clic en el nombre de la capa nueva, escribe Rectangles y presiona Enter o Return."),
            ])
            + phase("Paso 5 &middot; Barra Naranja",[
                ("Prep&aacute;rate:","aseg&uacute;rate de que la capa Rectangles est&eacute; seleccionada. Elige la herramienta Marco Rectangular (presiona M)."),
                ("Dibuja la caja:","empieza justo afuera de la esquina superior izquierda y arrastra hacia abajo y a la derecha. Suelta cuando la info diga W 96px y H 1080px."),
                ("Rell&eacute;nala de naranja:","en la Barra de Tareas Contextual, haz clic en Rellenar Selecci&oacute;n, luego en Rellenar con Color. Escribe ff7f00 en el campo #, haz clic en OK y OK otra vez."),
                ("Qu&iacute;tala:","elige Selecci&oacute;n &gt; Deseleccionar."),
            ])
            + phase("Paso 6 &middot; Barra Azul",[
                ("Dibuja la caja:","con la herramienta Marco Rectangular, empieza justo afuera de la esquina superior derecha y arrastra hacia abajo y a la izquierda. Suelta cuando la info diga W 660px y H 1080px."),
                ("Rell&eacute;nala de azul:","elige Edici&oacute;n &gt; Rellenar. Pon Contenido en Color, escribe 0053b2 y haz clic en OK, luego OK otra vez."),
                ("Qu&iacute;tala:","elige Selecci&oacute;n &gt; Deseleccionar."),
            ])
            + phase("Paso 7 &middot; Modo de Fusi&oacute;n Color",[
                ("Mezcla las barras:","en el panel Capas, haz clic en el men&uacute; de modo de fusi&oacute;n (dice Normal) arriba a la izquierda y elige Color. Ahora la foto se ve a trav&eacute;s de las dos barras."),
                ("Guarda:","elige Archivo &gt; Guardar."),
            ])
            + phase("Paso 8 &middot; Texto del T&iacute;tulo",[
                ("Prepara el texto:","elige la herramienta Texto Horizontal (presiona T). En la barra de arriba, elige una fuente serif en negrita (el deck usa Abril Fatface), pon el tama&ntilde;o en 210 pt, haz clic en Centrar y pon el color en blanco (ffffff)."),
                ("Activa May&uacute;sculas:","en el panel Propiedades, haz clic en el bot&oacute;n May&uacute;sculas (TT)."),
                ("Escribe el t&iacute;tulo:","haz clic cerca del centro-inferior del lienzo y escribe History 301. Se ve como HISTORY 301."),
                ("Termina:","haz clic en la palomita, o presiona Ctrl+Enter (Windows) o Cmd+Return (Mac). No presiones solo Enter."),
                ("Cent&eacute;ralo:","elige la herramienta Mover (presiona V) y arrastra las palabras para centrarlas."),
            ])
            + phase("Paso 9 &middot; Texto del Subt&iacute;tulo",[
                ("Empieza una l&iacute;nea nueva:","elige Selecci&oacute;n &gt; Deseleccionar Capas para que Photoshop haga una capa de texto nueva."),
                ("Cambia el texto:","con la herramienta Texto, cambia la fuente a una condensada en negrita cursiva (el deck usa Acumin Pro Condensed Black Italic), pon el tama&ntilde;o en 165 pt y haz clic en Alinear a la derecha."),
                ("Escr&iacute;belo:","haz clic cerca del lado derecho, como a dos tercios hacia abajo, y escribe Live Stream. Se ve como LIVE STREAM."),
                ("Termina:","haz clic en la palomita para confirmar."),
            ])
            + phase("Paso 10 &middot; Capa de Color S&oacute;lido",[
                ("Elige la capa:","en el panel Capas, haz clic en la capa Arch."),
                ("Agrega un color s&oacute;lido:","haz clic en el bot&oacute;n Crear Nueva Capa de Relleno o Ajuste (el c&iacute;rculo medio lleno) abajo del panel Capas y elige Color S&oacute;lido."),
                ("Elige verde oscuro:","escribe 0c3303 y haz clic en OK."),
                ("M&eacute;zclalo:","pon el modo de fusi&oacute;n de esta capa en Luz Fuerte, luego cambia su Opacidad a 90%."),
                ("Oculta las gu&iacute;as:","elige Vista &gt; Mostrar &gt; Gu&iacute;as para apagar las gu&iacute;as cian."),
            ],intro="Esta capa verde oscuro hace que el texto blanco se lea mejor.")
            + phase("Paso 11 &middot; Muestrea y Pinta",[
                ("Muestrea un azul:","elige la herramienta Cuentagotas (presiona I) y haz clic en una zona azul m&aacute;s clara del lado derecho para cargar ese color."),
                ("Acl&aacute;ralo:","elige Ventana &gt; Color. Del men&uacute; del panel, elige Deslizadores de Color Web, escribe 4099ff y presiona Enter."),
                ("Crea una capa para pintar:","en el panel Capas, haz clic en la capa Rectangles. Mant&eacute;n Alt (Windows) u Option (Mac) y haz clic en el bot&oacute;n Crear una Capa Nueva. N&oacute;mbrala Paint y haz clic en OK."),
                ("Elige un pincel de salpicado:","elige la herramienta Pincel (presiona B). Elige Ventana &gt; Pinceles, abre el grupo Pinceles de Efectos Especiales y elige Kyle&rsquo;s Spatter Brushes - Spatter Bot Tilt. Pon el Tama&ntilde;o del pincel en 80px."),
                ("Pinta:","con la capa Paint seleccionada, arrastra en c&iacute;rculos peque&ntilde;os sobre la palabra LIVE para crear un salpicado azul. Elige Archivo &gt; Guardar."),
            ])
            + phase("Paso 12 &middot; Mueve y Relleno Generativo",[
                ("Prepara la herramienta Mover:","elige la herramienta Mover (presiona V). En la barra de arriba, desmarca Selecci&oacute;n Autom&aacute;tica (Auto-Select)."),
                ("Centra el edificio:","en el panel Capas, haz clic en la capa Arch. Arrastra la foto en el lienzo hasta que el edificio quede centrado en la zona verde. Aparece un hueco a la izquierda."),
                ("Ve el hueco:","mant&eacute;n Alt (Windows) u Option (Mac) y haz clic en el &iacute;cono de ojo de la capa Arch para ocultar las dem&aacute;s capas."),
                ("Selecciona el hueco:","elige la herramienta Marco Rectangular (presiona M) y arrastra para seleccionar el hueco vac&iacute;o de la izquierda. Traslapa un poco el borde de la foto."),
                ("Rell&eacute;nalo con IA:","haz clic en la capa Arch en el panel Capas. En la Barra de Tareas Contextual, haz clic en Relleno Generativo, deja el cuadro en blanco y haz clic en Generar. Haz clic en Aceptar si te lo pide."),
                ("Elige la mejor:","en el panel Propiedades, haz clic en cada Variaci&oacute;n y elige la que se vea m&aacute;s natural."),
                ("Muestra todo:","haz clic derecho (Windows) o Control-clic (Mac) en el &iacute;cono de ojo de la capa Relleno Generativo y elige Mostrar/Ocultar Todas las Dem&aacute;s Capas. Elige Archivo &gt; Guardar."),
            ])
            + phase("Paso 13 &middot; Exporta",[
                ("Abre Exportar Como:","elige Archivo &gt; Exportar &gt; Exportar Como."),
                ("Elige el tipo de archivo:","pon Formato en JPG y Calidad en 6."),
                ("Pon el tama&ntilde;o:","pon el Ancho en 1280 y presiona Tab. El Alto se vuelve 720."),
                ("Iguala los colores:","aseg&uacute;rate de que Convertir a sRGB e Incrustar Perfil de Color est&eacute;n activados."),
                ("Guarda la copia:","haz clic en Exportar, nombra el archivo 01Working y haz clic en Guardar."),
            ])
        ), True)

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><span></span></div>'
    return wrap_page("Step 1: Build It in Photoshop | Live Stream Graphic | Digital Arts 1A | PVHS", nav("Step 01",dots_for(1),stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
