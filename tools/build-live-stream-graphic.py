#!/usr/bin/env python3
# Digital Arts 1A - Module 05: Live Stream Graphic (Photoshop how-to).
# Guided, step-by-step: build the "History 301 Live Stream" promo in Photoshop.
# Stripped from Adobe CIB 2025 Lesson 1 to a 5th-grade reading level, production steps only
# (no work-area touring, no Generative Fill). NO reflection (it is a guided how-to).
# Overview + 1 step, bilingual EN/ES. End-example float image on the Overview; no header image.
# Chip-header framework via silva_framework. Step 01 presents the picture-by-picture build guide as
# a single click-to-open Lesson Slides PDF thumbnail (slide_deck_thumb), the same pattern as the
# other modules; the old scrollable 13-step written guide was removed (no need for two sets).
import os, re
from silva_framework import *

ROOT=os.path.join(os.path.dirname(__file__),"..")
END_IMG=f"{SITE}/assets/images/digarts1/live-stream-graphic/live-stream-end-example-v1.jpg"
SLIDES_THUMB=f"{SITE}/assets/images/digarts1/live-stream-graphic/live-stream-slides-cover-v1.jpg"
ASSETS_ZIP=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Assets.zip"
SLIDES_PDF=f"{SITE}/assets/course-documents/Live-Stream-Graphic-Slides.pdf"
AREA="Digital Arts Folder"   # OneDrive top folder for this course's project folders

def slide_deck(es):
    # Click-to-open Lesson Slides PDF, shown as a purple cover thumbnail (opens in a new tab).
    return slide_deck_thumb(SLIDES_PDF, es, thumb=SLIDES_THUMB)

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
    en+=resources_card("Lesson Slides",
        para("Build your graphic in Adobe Photoshop by following the Lesson Slides. They show a picture for every step, from the new document all the way to the final export. Click the cover to open the slides in a new tab, then keep them next to Photoshop and work through the steps in order.")
        + para("Use the color codes exactly as written (like ff7f00) so your colors match the example."),
        False, floatimg=slide_deck(False))

    es=banner("Gr&aacute;fico de Live Stream &bull; Paso 1","Cr&eacute;alo en Photoshop","Sigue los pasos en orden para crear tu gr&aacute;fico.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 imagen:","tu gr&aacute;fico de Live Stream terminado (01Working.jpg), subido a esta tarea de Canvas.")])
    es+=resources_card("Diapositivas de la Lecci&oacute;n",
        para("Crea tu gr&aacute;fico en Adobe Photoshop siguiendo las Diapositivas de la Lecci&oacute;n. Muestran una imagen de cada paso, desde el documento nuevo hasta la exportaci&oacute;n final. Haz clic en la portada para abrir las diapositivas en una pesta&ntilde;a nueva, luego mantenlas junto a Photoshop y haz los pasos en orden.")
        + para("Usa los c&oacute;digos de color tal como est&aacute;n escritos (como ff7f00) para que tus colores coincidan con el ejemplo."),
        True, floatimg=slide_deck(True))

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><span></span></div>'
    return wrap_page("Step 1: Build It in Photoshop | Live Stream Graphic | Digital Arts 1A | PVHS", nav("Step 01",dots_for(1),stepnav), top_wrap(en,es), bottom)
for fname,gen in [(OVER,overview),(S1,step01)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
