#!/usr/bin/env python3
# Digital Arts 1A - Module 05: Live Stream Graphic + YouTube Thumbnail (Photoshop).
# Step 1 is a guided warm-up: build the "History 301 Live Stream" promo in Photoshop by following
# the Lesson Slides (learns the tools). Steps 2-4 apply those skills to the student's OWN work:
# find YouTube thumbnail inspiration (screen captures, PNG), design their own thumbnail (JPG), and
# reflect on it (.docx). Overview + 4 steps, bilingual EN/ES, 5th-grade. Chip-header framework via
# silva_framework. The Lesson Slides are a click-to-open PDF cover thumbnail (EN + ES decks).
# NOTE: use "screen capture", never the banned "screenshot"/"screen shot".
import os, re
from silva_framework import *

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/digarts1/live-stream-graphic"
END_IMG=f"{IMG}/live-stream-end-example-v1.jpg"
SLIDES_THUMB=f"{IMG}/live-stream-slides-cover-v1.jpg"
SLIDES_THUMB_ES=f"{IMG}/live-stream-slides-cover-es-v1.jpg"
YT_IMG=f"{IMG}/live-stream-youtube-channel-v1.jpg"
ASSETS_ZIP=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Assets.zip"
SLIDES_PDF_EN=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Slides.pdf"
SLIDES_PDF_ES=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Slides-ES.pdf"
REFLECT_EN=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Reflection-ES.docx"
AREA="Digital Arts Folder"
FOLDER="PS Lesson 01"   # the student project folder for this lesson

def slide_deck(es):
    # Click-to-open Lesson Slides PDF (EN or ES), shown as its own language cover thumbnail (new tab).
    return slide_deck_thumb(SLIDES_PDF_ES if es else SLIDES_PDF_EN, es, thumb=SLIDES_THUMB_ES if es else SLIDES_THUMB)

OVER="digarts1-live-stream-graphic-overview.html"
S1="digarts1-live-stream-graphic-step01.html"
S2="digarts1-live-stream-graphic-step02-inspiration.html"
S3="digarts1-live-stream-graphic-step03-design.html"
S4="digarts1-live-stream-graphic-step04-reflection.html"

def ps_folder_note(es):
    # Custom project-folder note: name the folder "PS Lesson 01" and say what goes in it.
    if es:
        return ('<div style="margin-top:16px;font-size:12pt;color:rgba(255,255,255,0.82);line-height:1.55;">'
          '<strong style="color:#ffb27c;">Mantente organizado:</strong> crea una carpeta llamada '
          f'&lsquo;{FOLDER}&rsquo; en OneDrive &rarr; {AREA}. Guarda ah&iacute; todo lo de esta lecci&oacute;n: '
          'tus archivos del proyecto, las capturas de pantalla de inspiraci&oacute;n que guardes en el Paso 2, '
          'y tu miniatura terminada.</div>')
    return ('<div style="margin-top:16px;font-size:12pt;color:rgba(255,255,255,0.82);line-height:1.55;">'
      '<strong style="color:#ffb27c;">Stay organized:</strong> make a folder called '
      f'&lsquo;{FOLDER}&rsquo; in OneDrive &rarr; {AREA}. Keep everything for this lesson there: '
      'your project files, the inspiration screen captures you save in Step 2, and your finished thumbnail.</div>')

def downloads_block(es):
    # Orange Downloads section (Overview only): project files, the Lesson Slides PDF, the reflection
    # doc. Buttons share one wrapping row; ends with the PS Lesson 01 folder note.
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Consigue aqu&iacute; tus archivos antes de empezar. Las Diapositivas de la Lecci&oacute;n muestran una imagen de cada paso del calentamiento." if es
          else "Grab your files here before you start. The Lesson Slides show a picture for every step of the warm-up.")
    zlabel="Archivos del Proyecto (ZIP)" if es else "Project Files (ZIP)"
    slabel="Diapositivas de la Lecci&oacute;n (PDF)" if es else "Lesson Slides (PDF)"
    rlabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
    spdf=SLIDES_PDF_ES if es else SLIDES_PDF_EN
    rdoc=REFLECT_ES if es else REFLECT_EN
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ASSETS_ZIP,zlabel,row=True)
      + dl_link(spdf,slabel,row=True)
      + dl_link(rdoc,rlabel,row=True)
      + '</div>'
      + ps_folder_note(es) + '</div>')

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

PAGES=[(OVER,"M","Overview"),(S1,"1","Step 01"),(S2,"2","Step 02"),(S3,"3","Step 03"),(S4,"4","Step 04")]
def dots_for(active_idx):
    r=""
    for i,(href,lab,title) in enumerate(PAGES):
        r+=dot("" if i==active_idx else href, lab, title, i==active_idx, module=(i==0 and active_idx!=0))
    return r

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Digital Arts 1A &bull; Module 05","Live Stream Graphic","Learn Photoshop, then design your own YouTube thumbnail.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Build a Graphic, Then Design Your Own Thumbnail",
        float_right(END_IMG,"Finished History 301 Live Stream graphic: an arch photo with an orange bar on the left, a blue bar on the right, a green wash, and the words HISTORY 301 and LIVE STREAM in white","The live stream graphic you build in Step 1 (your warm-up).")
        + para("In this project you learn Adobe Photoshop, then use it to make something of your own. First, in Step 1, you follow clear steps to build a live stream promo graphic, so everyone learns the same tools. Then, in Steps 2 to 4, you find YouTube thumbnail inspiration, design your own thumbnail, and reflect on it.")
        + para("In the warm-up you will make a new Photoshop file, add a photo, add colored bars, add words, blend colors, use Generative Fill, and export. Those are the same skills you will reuse to make your own thumbnail.")
        + note("Step 1 is a follow-along how-to. Steps 2 to 4 are your own YouTube thumbnail: inspiration, design, and reflection."))
    en+=downloads_block(False)
    en+=card("SKILLS / WHAT YOU WILL LEARN","New Photoshop Skills",
        para("This project teaches you the basics you will use in every Photoshop project after this one, starting with your own thumbnail:")
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
           ("Thumbnail","The small preview image on a YouTube video. A good one grabs attention and reads clearly even when it is small.")]), False)

    es=banner("Arte Digital 1A &bull; M&oacute;dulo 05","Gr&aacute;fico de Live Stream","Aprende Photoshop y luego dise&ntilde;a tu propia miniatura de YouTube.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","Crea un Gr&aacute;fico y Luego Dise&ntilde;a Tu Propia Miniatura",
        float_right(END_IMG,"Gr&aacute;fico terminado de History 301 Live Stream: una foto de un arco con una barra naranja a la izquierda, una barra azul a la derecha, un ba&ntilde;o verde y las palabras HISTORY 301 y LIVE STREAM en blanco","El gr&aacute;fico de live stream que creas en el Paso 1 (tu calentamiento).")
        + para("En este proyecto aprendes Adobe Photoshop y luego lo usas para crear algo tuyo. Primero, en el Paso 1, sigues pasos claros para crear un gr&aacute;fico promocional de live stream, para que todos aprendan las mismas herramientas. Luego, en los Pasos 2 al 4, buscas inspiraci&oacute;n de miniaturas de YouTube, dise&ntilde;as tu propia miniatura y reflexionas sobre ella.")
        + para("En el calentamiento vas a crear un archivo nuevo de Photoshop, agregar una foto, agregar barras de color, agregar palabras, mezclar colores, usar Relleno Generativo y exportar. Esas son las mismas habilidades que vas a reusar para crear tu propia miniatura.")
        + note("El Paso 1 es un instructivo para seguir. Los Pasos 2 al 4 son tu propia miniatura de YouTube: inspiraci&oacute;n, dise&ntilde;o y reflexi&oacute;n."))
    es+=downloads_block(True)
    es+=card("HABILIDADES / LO QUE APRENDER&Aacute;S","Nuevas Habilidades de Photoshop",
        para("Este proyecto te ense&ntilde;a lo b&aacute;sico que usar&aacute;s en cada proyecto de Photoshop despu&eacute;s de este, empezando con tu propia miniatura:")
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
           ("Thumbnail (Miniatura)","La imagen peque&ntilde;a de vista previa de un video de YouTube. Una buena llama la atenci&oacute;n y se entiende clara aunque sea peque&ntilde;a.")]), True)

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Live Stream Graphic | Digital Arts 1A | PVHS", nav("Overview",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 : warm-up build ----------------
def step01():
    en=banner("Live Stream Graphic &bull; Step 1","Build It in Photoshop","Follow the steps to build your warm-up graphic.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 image (JPG):","your finished Live Stream graphic (01Working.jpg), uploaded to this Canvas assignment.")])
    en+=resources_card("Lesson Slides",
        para("Build your graphic in Adobe Photoshop by following the Lesson Slides. They show a picture for every step, from the new document all the way to the final export. Click the cover to open the slides in a new tab, then keep them next to Photoshop and work through the steps in order.")
        + para("Use the color codes exactly as written (like ff7f00) so your colors match the example.")
        + note("This build is your warm-up. You will use these same skills to design your own YouTube thumbnail in Step 3."),
        False, floatimg=slide_deck(False))

    es=banner("Gr&aacute;fico de Live Stream &bull; Paso 1","Cr&eacute;alo en Photoshop","Sigue los pasos para crear tu gr&aacute;fico de calentamiento.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 imagen (JPG):","tu gr&aacute;fico de Live Stream terminado (01Working.jpg), subido a esta tarea de Canvas.")])
    es+=resources_card("Diapositivas de la Lecci&oacute;n",
        para("Crea tu gr&aacute;fico en Adobe Photoshop siguiendo las Diapositivas de la Lecci&oacute;n. Muestran una imagen de cada paso, desde el documento nuevo hasta la exportaci&oacute;n final. Haz clic en la portada para abrir las diapositivas en una pesta&ntilde;a nueva, luego mantenlas junto a Photoshop y haz los pasos en orden.")
        + para("Usa los c&oacute;digos de color tal como est&aacute;n escritos (como ff7f00) para que tus colores coincidan con el ejemplo.")
        + note("Este gr&aacute;fico es tu calentamiento. Vas a usar estas mismas habilidades para dise&ntilde;ar tu propia miniatura de YouTube en el Paso 3."),
        True, floatimg=slide_deck(True))

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Build It in Photoshop | Live Stream Graphic | Digital Arts 1A | PVHS", nav("Step 01",dots_for(1),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 : YouTube thumbnail inspiration ----------------
def step02():
    en=banner("Live Stream Graphic &bull; Step 2","Find Your Inspiration","Pick one channel you love and study its thumbnails.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("Inspiration (PNG):","one or more screen captures of thumbnails from the channel you chose, saved as PNG in your &lsquo;"+FOLDER+"&rsquo; folder and uploaded to this Canvas assignment.")])
    en+=card("STEP 02 / INSPIRATION","Study One Channel You Love on YouTube",
        para("Before you design your own, look at what already works. A thumbnail is the small preview image on a YouTube video, the one that makes you want to click. Pick ONE specific channel you like and study ITS thumbnails, not random search results.")
        + para("Look at the channel&rsquo;s design language: the colors, fonts, faces, and layout it uses again and again, so all its videos look like they belong to the same channel.")
        + steps([
            ("","Pick one specific YouTube channel you like, then open it and click its Home or Videos tab."),
            ("","Look at that channel&rsquo;s thumbnails together. What is its design language? Notice the colors, fonts, and layout it repeats."),
            ("","Take a screen capture of 1 to 3 thumbnails from that channel that grab you: press F15 on your keyboard. F15 saves the screen capture as a PNG file on your Desktop."),
            ("","Move your screen captures into your &lsquo;"+FOLDER+"&rsquo; folder."),
            ("","Upload one or several of them to this Canvas assignment."),
        ])
        + note("What makes a thumbnail work? A big, clear subject; a few bold words; strong colors; and it still reads when it is small. Look for those in your channel&rsquo;s thumbnails."),
        floatimg=float_right(YT_IMG,"A YouTube channel page open in a browser, showing a row of the channel&rsquo;s video thumbnails that share the same bold-text, big-face design language","One channel you chose. See how its thumbnails share a design language."))

    es=banner("Gr&aacute;fico de Live Stream &bull; Paso 2","Busca Tu Inspiraci&oacute;n","Elige un canal que te encante y estudia sus miniaturas.","#top","Back to English")
    es+=deliverables_box(True,
        [("Inspiraci&oacute;n (PNG):","una o varias capturas de pantalla de miniaturas del canal que elegiste, guardadas en formato PNG en tu carpeta &lsquo;"+FOLDER+"&rsquo; y subidas a esta tarea de Canvas.")])
    es+=card("PASO 02 / INSPIRACI&Oacute;N","Estudia Un Canal Que Te Encante en YouTube",
        para("Antes de dise&ntilde;ar la tuya, mira lo que ya funciona. Una miniatura es la imagen peque&ntilde;a de vista previa de un video de YouTube, la que te dan ganas de hacer clic. Elige UN canal espec&iacute;fico que te guste y estudia SUS miniaturas, no resultados de b&uacute;squeda al azar.")
        + para("Mira el lenguaje de dise&ntilde;o del canal: los colores, las fuentes, las caras y el dise&ntilde;o que usa una y otra vez, para que todos sus videos se vean del mismo canal.")
        + steps([
            ("","Elige un canal espec&iacute;fico de YouTube que te guste, luego &aacute;brelo y haz clic en su pesta&ntilde;a Inicio o Videos."),
            ("","Mira las miniaturas de ese canal juntas. &iquest;Cu&aacute;l es su lenguaje de dise&ntilde;o? F&iacute;jate en los colores, las fuentes y el dise&ntilde;o que repite."),
            ("","Toma una captura de pantalla de 1 a 3 miniaturas de ese canal que te llamen la atenci&oacute;n: presiona F15 en el teclado. F15 guarda la captura como un archivo PNG en tu Escritorio."),
            ("","Mueve tus capturas de pantalla a tu carpeta &lsquo;"+FOLDER+"&rsquo;."),
            ("","Sube una o varias a esta tarea de Canvas."),
        ])
        + note("&iquest;Qu&eacute; hace buena a una miniatura? Un sujeto grande y claro; pocas palabras en negrita; colores fuertes; y que a&uacute;n se entienda cuando es peque&ntilde;a. Busca eso en las miniaturas de tu canal."),
        floatimg=float_right(YT_IMG,"La p&aacute;gina de un canal de YouTube abierta en un navegador, mostrando una fila de las miniaturas del canal que comparten el mismo lenguaje de dise&ntilde;o de texto en negrita y caras grandes","Un canal que elegiste. Mira c&oacute;mo sus miniaturas comparten un lenguaje de dise&ntilde;o."))

    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a><a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Find Your Inspiration | Live Stream Graphic | Digital Arts 1A | PVHS", nav("Step 02",dots_for(2),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 03 : design your own thumbnail ----------------
def step03():
    en=banner("Live Stream Graphic &bull; Step 3","Design Your Own Thumbnail","Make your own YouTube thumbnail in Photoshop.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 thumbnail (JPG):","your finished, polished YouTube thumbnail, exported as a JPG and uploaded to this Canvas assignment.")])
    en+=card("STEP 03 / DESIGN","Design Your Thumbnail",
        para("Now make your own. Use the Photoshop skills from your Step 1 warm-up and the ideas you gathered in Step 2.")
        + steps([
            ("","Make a new Photoshop file at 1280 by 720 pixels, the YouTube thumbnail size."),
            ("","Add a background: a photo, a solid color, or a gradient."),
            ("","Add a clear subject: a person, a face, or an object that shows what the video is about."),
            ("","Add bold words with the Type tool: just a few, big and easy to read."),
            ("","Use strong color and contrast so it pops."),
            ("","Export it as a JPG: choose File &gt; Export &gt; Export As, and set the format to JPG."),
        ])
        + note("Test it small. Shrink your thumbnail down. Can you still read the words and tell what the video is about? If yes, you nailed it."))

    es=banner("Gr&aacute;fico de Live Stream &bull; Paso 3","Dise&ntilde;a Tu Propia Miniatura","Crea tu propia miniatura de YouTube en Photoshop.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 miniatura (JPG):","tu miniatura de YouTube terminada y pulida, exportada como JPG y subida a esta tarea de Canvas.")])
    es+=card("PASO 03 / DISE&Ntilde;O","Dise&ntilde;a Tu Miniatura",
        para("Ahora crea la tuya. Usa las habilidades de Photoshop de tu calentamiento del Paso 1 y las ideas que juntaste en el Paso 2.")
        + steps([
            ("","Crea un archivo nuevo de Photoshop de 1280 por 720 p&iacute;xeles, el tama&ntilde;o de una miniatura de YouTube."),
            ("","Agrega un fondo: una foto, un color s&oacute;lido o un degradado."),
            ("","Agrega un sujeto claro: una persona, una cara o un objeto que muestre de qu&eacute; trata el video."),
            ("","Agrega palabras en negrita con la herramienta Texto: solo unas pocas, grandes y f&aacute;ciles de leer."),
            ("","Usa color y contraste fuertes para que resalte."),
            ("","Exp&oacute;rtala como JPG: elige Archivo &gt; Exportar &gt; Exportar Como y pon el formato en JPG."),
        ])
        + note("Pru&eacute;bala peque&ntilde;a. Reduce tu miniatura. &iquest;Todav&iacute;a puedes leer las palabras y saber de qu&eacute; trata el video? Si s&iacute;, lo lograste."))

    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a><a href="{S4}" class="silva-step-btn">Step 04 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S4}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
    return wrap_page("Step 3: Design Your Own Thumbnail | Live Stream Graphic | Digital Arts 1A | PVHS", nav("Step 03",dots_for(3),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 04 : reflection ----------------
def step04():
    en=banner("Live Stream Graphic &bull; Step 4","Turn In Your Reflection","Reflect on the thumbnail you made.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
    en+=card("STEP 04 / REFLECT","Complete and Upload the Reflection",
        para("Finish with a short reflection about the YouTube thumbnail you designed. It asks what your thumbnail is for, what inspired you, how you made it, and what you are proud of.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your &lsquo;"+FOLDER+"&rsquo; folder.")
        + bullets([
            ("Open it:","open the reflection Word document (.docx) from your &lsquo;"+FOLDER+"&rsquo; folder."),
            ("Answer every question:","type your answers in the boxes, in full sentences."),
            ("Save and upload:","save the document and upload it to this Canvas assignment."),
        ])
        + note("Answer honestly, in your own words, about your own thumbnail."))

    es=banner("Gr&aacute;fico de Live Stream &bull; Paso 4","Entrega Tu Reflexi&oacute;n","Reflexiona sobre la miniatura que creaste.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n, subido a esta tarea de Canvas.")])
    es+=card("PASO 04 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        para("Termina con una reflexi&oacute;n corta sobre la miniatura de YouTube que dise&ntilde;aste. Te pregunta para qu&eacute; es tu miniatura, qu&eacute; te inspir&oacute;, c&oacute;mo la hiciste y de qu&eacute; est&aacute;s orgulloso.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta &lsquo;"+FOLDER+"&rsquo;.")
        + bullets([
            ("&Aacute;brelo:","abre el documento de Word (.docx) de la reflexi&oacute;n desde tu carpeta &lsquo;"+FOLDER+"&rsquo;."),
            ("Contesta cada pregunta:","escribe tus respuestas en los cuadros, en oraciones completas."),
            ("Guarda y sube:","guarda el documento y s&uacute;belo a esta tarea de Canvas."),
        ])
        + note("Contesta con honestidad, en tus propias palabras, sobre tu propia miniatura."))

    stepnav=f'<a href="{S3}" class="silva-step-btn">&#8592; Step 03</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S3}" class="silva-bottom-btn">&#8592; Step 03</a><span></span></div>'
    return wrap_page("Step 4: Reflection | Live Stream Graphic | Digital Arts 1A | PVHS", nav("Step 04",dots_for(4),stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03),(S4,step04)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
