#!/usr/bin/env python3
# Photography 1A - Module 05: Lightroom Editing (Lightroom Classic, Develop Basics).
# An in-depth dive into real editing: import, crop + develop in the Develop module, cull to the
# best 6 with 5-star ratings, build a PVHS 6-Up contact sheet, and export 6 high-resolution JPEGs.
# Students may edit photos they already captured OR photograph new ones for this project.
# Major focus: CROPPING (keep the original ratio or a real store frame size, never a made-up size)
# and editing in Lightroom Classic. Built on the shared silva_framework. Overview + 3 steps,
# bilingual EN/ES, 5th-grade. HEADER + all float images are PLACEHOLDERS (Chris drops art in later).
# The Develop Basics slide deck is a click-to-open PDF (opens in a new tab), EN + ES.
# Import is NOT its own step (students already learned import): the import guide lives on the
# Overview. Contact-sheet presets are a one-time install (introduced in Image Series), so this
# module does NOT re-offer the template download or an install card; it references the installed
# preset (see overview-holds-resources memory + SILVA_ANGULAR_FRAMEWORK.md).
import os, re
from silva_framework import *

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"

# Develop Basics slide deck (this module's deck): EN + ES click-to-open PDFs + cover thumbnails.
DECK_PDF_EN=f"{SITE}/assets/course-documents/Photo1-LRC-Develop-Basics-Slides-EN-v2.pdf"
DECK_PDF_ES=f"{SITE}/assets/course-documents/Photo1-LRC-Develop-Basics-Slides-ES-v1.pdf"
DECK_COVER_EN=f"{SITE}/assets/images/photo1/lrc-develop/develop-basics-cover-en-v1.jpg"
DECK_COVER_ES=f"{SITE}/assets/images/photo1/lrc-develop/develop-basics-cover-es-v1.jpg"
# Overview 21:9 hero
HEADER=f"{SITE}/assets/images/photo1/lrc-develop/develop-basics-header-v1.jpg"
# Existing Lightroom import deck (reused on the Overview; English guide).
IMPORT_PDF=f"{SITE}/assets/course-documents/Lightroom-Import-Guide.pdf"
IMPORT_COVER=f"{SITE}/assets/images/photo1/image-series/importing-photos-slidedeck-thumb-v1.jpg"
# Files to keep
REFLECT_EN=f"{SITE}/assets/course-documents/Lightroom-Editing-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Lightroom-Editing-Reflection-ES.docx"
# Photography Course Resources page (where the contact-sheet presets live for anyone who needs them again)
COURSE_RESOURCES=f"{SITE}/curriculum/shared/photo1a-course-resources.html"

OVER="photo1-lightroom-editing-overview.html"
S1="photo1-lightroom-editing-step01-edit-crop.html"
S2="photo1-lightroom-editing-step02-cull-export.html"
S3="photo1-lightroom-editing-step03-reflection.html"

# ---- module-local helpers ----
def float_ph(label):
    # Float-right PLACEHOLDER: a FLOAT-marked dashed box so a card hoists it into the thumbnail
    # column (where the real float_right image will go). Swap to float_right(src,alt,cap) later.
    return '<!--FLOAT-->' + placeholder(label, minh=220) + '<!--/FLOAT-->'

CROP_ASPECT=f"{SITE}/assets/images/photo1/lrc-develop/develop-basics-crop-aspect-float-v1.png"
def crop_aspect_float(es):
    # Portrait aspect-ratio reference (the Crop aspect menu). It is a TALL portrait, so it is capped
    # narrower (~300px) than a landscape content float and passed via floatimg (the compact column),
    # so it stays readable without dominating the row. Not an AI photo, so not in the image catalog.
    alt=("El men&uacute; de proporci&oacute;n de Recorte en Lightroom Classic, con tama&ntilde;os est&aacute;ndar como 1x1, 4x5/8x10, 5x7 y 2x3/4x6" if es
         else "The Lightroom Classic Crop aspect ratio menu, with standard sizes like 1x1, 4x5/8x10, 5x7, and 2x3/4x6")
    cap=("El men&uacute; de proporciones de Recorte." if es else "The Crop aspect ratio menu.")
    return ('<div style="max-width:300px;margin:0 auto;">'
      '<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">'
      f'<img src="{CROP_ASPECT}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      f'<div style="font-size:10.5pt;color:#80e0e0;text-align:center;margin-top:6px;opacity:0.9;line-height:1.4;">{cap}</div>'
      '</div>')

STAR_RATING=f"{SITE}/assets/images/photo1/lrc-develop/develop-basics-star-rating-float-v1.jpg"
def star_float(es):
    # Landscape UI reference (the Library filtered to 5 stars). It is a screen capture, so it is
    # shown as a compact reference float (floatimg column), not the 44% AI-content column, and stays
    # out of the image catalog (which excludes screen captures), consistent with the crop aspect float.
    alt=("La vista de Biblioteca de Lightroom Classic filtrada a fotos de 5 estrellas, con la barra de filtros en Atributo" if es
         else "The Lightroom Classic Library view filtered to 5-star photos, with the Filter Bar set to Attribute")
    cap=("Filtra a 5 estrellas para ver solo tus mejores." if es else "Filter to 5 stars to see only your best.")
    return ('<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">'
      f'<img src="{STAR_RATING}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      f'<div style="font-size:10.5pt;color:#80e0e0;text-align:center;margin-top:6px;opacity:0.9;line-height:1.4;">{cap}</div>')

def deck(es):
    # Develop Basics slide deck: click-to-open PDF (opens in a new tab), per language.
    pdf = DECK_PDF_ES if es else DECK_PDF_EN
    cover = DECK_COVER_ES if es else DECK_COVER_EN
    cap = ("Haz clic para abrir la presentaci&oacute;n. Se abre como PDF en una pesta&ntilde;a nueva, donde la ves en pantalla completa y la descargas." if es
           else "Click to open the slide deck. It opens as a PDF in a new tab, where you can read it full screen and download it.")
    return slide_deck_thumb(pdf, es, thumb=cover, cap=cap)

def import_deck(es):
    cap = ("Haz clic para abrir la gu&iacute;a de importaci&oacute;n (PDF en una pesta&ntilde;a nueva)." if es
           else "Click to open the import guide (PDF in a new tab).")
    return slide_deck_thumb(IMPORT_PDF, es, thumb=IMPORT_COVER, cap=cap)

def downloads_block(es):
    # Files to keep for this module: just the reflection document. The contact-sheet presets are a
    # ONE-TIME install introduced in Image Series, so they are NOT re-offered here.
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga el documento de reflexi&oacute;n de este m&oacute;dulo. Cons&iacute;guelo antes de empezar." if es
          else "Download this module&rsquo;s reflection document. Get it before you start.")
    reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
    ref=REFLECT_ES if es else REFLECT_EN
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ref,reflabel,row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

def import_resource(es):
    # Import lives on the Overview (students already learned import in an earlier module). The
    # import guide is a click-to-open PDF; the choose-your-photos + import note is merged in here.
    if es:
        body=(para("Primero elige las fotos que quieres editar: im&aacute;genes que <strong>ya capturaste</strong>, o un conjunto <strong>nuevo</strong> que tomes para este proyecto. Luego ll&eacute;valas a Lightroom Classic.")
          + para("Ya aprendiste a importar en un m&oacute;dulo anterior, as&iacute; que si tus fotos ya est&aacute;n en Lightroom, sigue adelante. &iquest;Necesitas un repaso? Abre la gu&iacute;a de importaci&oacute;n. Se abre como PDF en una pesta&ntilde;a nueva.")
          + note("Empieza con m&aacute;s de 6 fotos para escoger. Vas a reducir a tus mejores 6."))
        return resources_card("Importar a Lightroom Classic", body, True, floatimg=import_deck(True))
    body=(para("First, choose the photos you want to edit: images you <strong>already captured</strong>, or a <strong>new</strong> set you take for this project. Then bring them into Lightroom Classic.")
      + para("You already learned importing in an earlier module, so if your photos are already in Lightroom, go ahead. Need a refresher? Open the import guide. It opens as a PDF in a new tab.")
      + note("Start with more than 6 photos to choose from. You will cull down to your best 6."))
    return resources_card("Importing Into Lightroom Classic", body, False, floatimg=import_deck(False))

# ---- nav / dots ----
DOTS_TITLES=[("M","Overview"),("1","Step 01"),("2","Step 02"),("3","Step 03")]
HREFS=[OVER,S1,S2,S3]
def dots_for(active_idx):
    r=""
    for i,(lab,title) in enumerate(DOTS_TITLES):
        r+=dot("" if i==active_idx else HREFS[i], lab, title, i==active_idx, module=(i==0 and active_idx!=0))
    return r
def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Lightroom Editing</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

# ================= OVERVIEW =================
def overview():
    en=banner("Photography 1A &bull; Module 05","Lightroom Editing","Import, crop and develop in Lightroom Classic, cull your best 6, and export finals.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("edit","The Module Overview","Go Deeper Into Real Editing",
        para("This week you take a deeper dive into real editing in Lightroom Classic. You will work in the Develop module: the place where you crop, fix color, and bring your photos to life. Editing is non-destructive, which means your original photo file is never changed.")
        + para("You can edit photos you have <strong>already captured</strong>, or take <strong>new photos</strong> for this project. Either way, you will import them, crop and develop them, cull down to your best 6, build a 6-Up contact sheet, and export your 6 finals as high-resolution JPEGs.")
        + framed(HEADER,"A Pioneer Valley student editing a cityscape photo in the Lightroom Classic Develop module on an iMac in the creative lab, a Canon EOS camera on the desk, with other students editing behind her"))
    en+=downloads_block(False)
    en+=import_resource(False)
    en+=card("THE BIG IDEA / EDITING MATTERS","Editing Is Where a Photo Becomes Finished",
        para("A great photo is made twice: once when you capture it, and again when you edit it. In the Develop module you correct color, set the right brightness, recover detail, and crop for a stronger composition. Small, careful edits turn a good frame into a finished image.")
        + bullets([
            ("Crop with a purpose:","tighten the composition and fix a tilted horizon, using a real size, not a made-up one."),
            ("Develop the tones:","set your white balance, exposure, highlights, shadows, and presence."),
            ("Keep it natural:","subtle edits look professional; maxed-out sliders do not."),
        ]))
    en+=card("HOW IT WORKS / YOUR PLAN","Your Three Steps",
        steps([
            ("Edit &amp; Crop:","crop to a real size and develop each photo in the Develop module. This is the main focus of the module."),
            ("Cull, Contact Sheet &amp; Export:","rate and cull to your best 6, build a 6-Up contact sheet, and export your 6 finals as high-resolution JPEGs."),
            ("Reflection:","tell the story of your edits and your crop choices."),
        ])
        + note("Your final turn-in is 7 files: your 6-Up contact sheet plus your 6 exported high-resolution JPEGs."))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Develop Module","The editing workspace in Lightroom Classic where you crop, correct color, and enhance your photos."),
           ("Crop / Aspect Ratio","Trimming your frame to a shape. Keep the original ratio or pick a real print size like 4x6, 5x7, or 8x10. Never a made-up size."),
           ("White Balance","The setting that makes colors look warm, cool, or true to life, and removes color casts."),
           ("Exposure","The overall brightness of a photo, set with the Exposure slider in the Tone section."),
           ("Cull","Looking through your photos and keeping only the strongest ones. In this class you cull with the 5-star rating."),
           ("Contact Sheet","One page that shows a set of your photos as small thumbnails, saved as a high-resolution JPG.")]))

    es=banner("Fotograf&iacute;a 1A &bull; M&oacute;dulo 05","Edici&oacute;n en Lightroom","Importa, recorta y revela en Lightroom Classic, elige tus mejores 6 y exporta tus finales.","#top","Back to English")
    es+=type_card("edit","El Resumen del M&oacute;dulo","Profundiza en la Edici&oacute;n Real",
        para("Esta semana profundizas en la edici&oacute;n real en Lightroom Classic. Trabajar&aacute;s en el m&oacute;dulo Revelar: el lugar donde recortas, corriges el color y das vida a tus fotos. La edici&oacute;n no es destructiva, lo que significa que tu archivo de foto original nunca cambia.")
        + para("Puedes editar fotos que <strong>ya capturaste</strong>, o tomar <strong>fotos nuevas</strong> para este proyecto. En ambos casos, las importar&aacute;s, las recortar&aacute;s y revelar&aacute;s, elegir&aacute;s tus mejores 6, crear&aacute;s una hoja de contactos de 6 y exportar&aacute;s tus 6 finales como JPEG de alta resoluci&oacute;n.")
        + framed(HEADER,"Una estudiante de Pioneer Valley editando una foto de una ciudad en el m&oacute;dulo Revelar de Lightroom Classic en una iMac en el laboratorio creativo, una c&aacute;mara Canon EOS en el escritorio, con otros estudiantes editando detr&aacute;s de ella"))
    es+=downloads_block(True)
    es+=import_resource(True)
    es+=card("LA GRAN IDEA / EDITAR IMPORTA","Editar Es Donde una Foto Queda Terminada",
        para("Una gran foto se hace dos veces: una cuando la capturas y otra cuando la editas. En el m&oacute;dulo Revelar corriges el color, ajustas el brillo, recuperas detalle y recortas para una composici&oacute;n m&aacute;s fuerte. Ediciones peque&ntilde;as y cuidadas convierten una buena toma en una imagen terminada.")
        + bullets([
            ("Recorta con prop&oacute;sito:","ajusta la composici&oacute;n y endereza un horizonte torcido, usando un tama&ntilde;o real, no uno inventado."),
            ("Revela los tonos:","ajusta tu balance de blancos, exposici&oacute;n, luces, sombras y presencia."),
            ("Mant&eacute;nlo natural:","las ediciones sutiles se ven profesionales; los controles al m&aacute;ximo no."),
        ]))
    es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Tres Pasos",
        steps([
            ("Editar y Recortar:","recorta a un tama&ntilde;o real y revela cada foto en el m&oacute;dulo Revelar. Este es el enfoque principal del m&oacute;dulo."),
            ("Selecciona, Hoja de Contactos y Exporta:","califica y elige tus mejores 6, crea una hoja de contactos de 6 y exporta tus 6 finales como JPEG de alta resoluci&oacute;n."),
            ("Reflexi&oacute;n:","cuenta la historia de tus ediciones y tus decisiones de recorte."),
        ])
        + note("Tu entrega final son 7 archivos: tu hoja de contactos de 6 m&aacute;s tus 6 JPEG de alta resoluci&oacute;n exportados."))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Develop Module (M&oacute;dulo Revelar)","El espacio de edici&oacute;n en Lightroom Classic donde recortas, corriges el color y mejoras tus fotos."),
           ("Crop / Aspect Ratio (Recorte / Proporci&oacute;n)","Recortar tu cuadro a una forma. Mant&eacute;n la proporci&oacute;n original o elige un tama&ntilde;o real de impresi&oacute;n como 4x6, 5x7 u 8x10. Nunca un tama&ntilde;o inventado."),
           ("White Balance (Balance de Blancos)","El ajuste que hace que los colores se vean c&aacute;lidos, fr&iacute;os o reales, y quita los tintes de color."),
           ("Exposure (Exposici&oacute;n)","El brillo general de una foto, ajustado con el control de Exposici&oacute;n en la secci&oacute;n de Tono."),
           ("Cull (Seleccionar)","Revisar tus fotos y quedarte solo con las m&aacute;s fuertes. En esta clase seleccionas con la calificaci&oacute;n de 5 estrellas."),
           ("Contact Sheet (Hoja de Contactos)","Una p&aacute;gina que muestra un conjunto de tus fotos como miniaturas, guardada como JPG de alta resoluci&oacute;n.")]), True)

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Lightroom Editing | Photography 1A | PVHS", nav("Overview",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ================= STEP 01: EDIT & CROP =================
def step01():
    en=banner("Lightroom Editing &bull; Step 1","Edit &amp; Crop","Crop to a real size and develop each photo in the Develop module.","#espanol","Clic para Espa&ntilde;ol")
    en+=resources_card("Develop Basics Slide Deck",
        para("This is your main guide for the whole module. Open the slide deck to see every Develop tool step by step: the workspace, crop and straighten, camera profile, white balance, exposure and contrast, highlights and shadows, and the presence sliders. It opens as a PDF in a new tab, so you can read it full screen and keep it open while you edit."),
        False, floatimg=deck(False))
    en+=card("CROP / THE RULE","Crop to a Real Size, Never a Made-Up One",
        para("Cropping is the biggest focus of this module. A good crop tightens your composition and fixes a tilted horizon. But you cannot just drag the crop box to any random shape. You must crop to a <strong>real size</strong>.")
        + para("<strong>You have two choices when you crop:</strong>")
        + bullets([
            ("Keep the original ratio:","leave the crop set to Original so the shape matches your camera. This is always a safe choice."),
            ("Or pick a real frame size:","choose a size that stores actually sell and print, like 4x6, 5x7, 8x10, 11x14, 16x20, or 24x36."),
        ])
        + note("No made-up sizes. Never invent a random crop shape. Real photos are printed and framed at real sizes, so your crop has to match one.")
        + steps([
            ("Press R to open the Crop Overlay:","the crop box and the Crop &amp; Straighten panel appear."),
            ("Set your Aspect ratio:","click the Aspect menu and choose Original, or pick a real size like 4x5 / 8x10, 5x7, or 2x3 / 4x6."),
            ("Drag the handles:","frame your subject. Press O to cycle guide overlays like Rule of Thirds."),
            ("Straighten if needed:","drag the Angle slider to level a tilted horizon."),
            ("Press Return to confirm:","press R again any time to go back and adjust."),
        ]),
        floatimg=crop_aspect_float(False))
    en+=card("DEVELOP / THE WORKFLOW","Develop Your Photo, Step by Step",
        para("After you crop, develop your photo in the Basic panel. Work in this order for the best results. The slide deck shows each step in detail.")
        + steps([
            ("Camera Profile:","at the top of the Basic panel, set the Profile to Adaptive Color as your starting point."),
            ("White Balance:","fix any color cast so the colors look true. Use the WB menu, or the Temp and Tint sliders."),
            ("Exposure:","set the overall brightness first. Do not max it out."),
            ("Highlights &amp; Shadows:","pull Highlights down to recover a bright sky; push Shadows up to open dark areas."),
            ("Whites &amp; Blacks:","set your brightest and darkest points so the tones fill the histogram."),
            ("Presence:","add a little Texture, Clarity, and Vibrance to finish. Go easy: subtle looks best."),
        ])
        + note("Editing is non-destructive. Your original file is never changed, so you can always press Reset and start over."))

    es=banner("Edici&oacute;n en Lightroom &bull; Paso 1","Edita y Recorta","Recorta a un tama&ntilde;o real y revela cada foto en el m&oacute;dulo Revelar.","#top","Back to English")
    es+=resources_card("Presentaci&oacute;n de Conceptos de Revelado",
        para("Esta es tu gu&iacute;a principal para todo el m&oacute;dulo. Abre la presentaci&oacute;n para ver cada herramienta de Revelar paso a paso: el espacio de trabajo, recortar y enderezar, el perfil de c&aacute;mara, el balance de blancos, la exposici&oacute;n y el contraste, las luces y sombras, y los controles de presencia. Se abre como PDF en una pesta&ntilde;a nueva, para verla en pantalla completa y tenerla abierta mientras editas."),
        True, floatimg=deck(True))
    es+=card("RECORTE / LA REGLA","Recorta a un Tama&ntilde;o Real, Nunca a Uno Inventado",
        para("El recorte es el enfoque m&aacute;s grande de este m&oacute;dulo. Un buen recorte ajusta tu composici&oacute;n y endereza un horizonte torcido. Pero no puedes arrastrar el cuadro de recorte a cualquier forma al azar. Debes recortar a un <strong>tama&ntilde;o real</strong>.")
        + para("<strong>Tienes dos opciones al recortar:</strong>")
        + bullets([
            ("Mant&eacute;n la proporci&oacute;n original:","deja el recorte en Original para que la forma coincida con tu c&aacute;mara. Siempre es una opci&oacute;n segura."),
            ("O elige un tama&ntilde;o real de marco:","elige un tama&ntilde;o que las tiendas realmente venden e imprimen, como 4x6, 5x7, 8x10, 11x14, 16x20 o 24x36."),
        ])
        + note("Nada de tama&ntilde;os inventados. Nunca inventes una forma de recorte al azar. Las fotos reales se imprimen y enmarcan en tama&ntilde;os reales, as&iacute; que tu recorte debe coincidir con uno.")
        + steps([
            ("Presiona R para abrir el Recorte:","aparecen el cuadro de recorte y el panel de Recortar y Enderezar."),
            ("Ajusta tu proporci&oacute;n (Aspect):","abre el men&uacute; Aspect y elige Original, o un tama&ntilde;o real como 4x5 / 8x10, 5x7 o 2x3 / 4x6."),
            ("Arrastra las esquinas:","encuadra tu sujeto. Presiona O para cambiar las gu&iacute;as como la Regla de los Tercios."),
            ("Endereza si hace falta:","arrastra el control de &Aacute;ngulo para nivelar un horizonte torcido."),
            ("Presiona Return para confirmar:","presiona R otra vez cuando quieras para regresar y ajustar."),
        ]),
        floatimg=crop_aspect_float(True))
    es+=card("REVELAR / EL FLUJO DE TRABAJO","Revela Tu Foto, Paso a Paso",
        para("Despu&eacute;s de recortar, revela tu foto en el panel B&aacute;sico. Trabaja en este orden para el mejor resultado. La presentaci&oacute;n muestra cada paso en detalle.")
        + steps([
            ("Perfil de C&aacute;mara:","arriba del panel B&aacute;sico, pon el Perfil en Adaptive Color como punto de partida."),
            ("Balance de Blancos:","corrige cualquier tinte de color para que se vea real. Usa el men&uacute; WB, o los controles Temp y Tint."),
            ("Exposici&oacute;n:","ajusta el brillo general primero. No lo pongas al m&aacute;ximo."),
            ("Luces y Sombras:","baja las Luces para recuperar un cielo brillante; sube las Sombras para abrir las zonas oscuras."),
            ("Blancos y Negros:","ajusta tus puntos m&aacute;s brillante y m&aacute;s oscuro para que los tonos llenen el histograma."),
            ("Presencia:","agrega un poco de Textura, Claridad y Vibrancia para terminar. Con calma: lo sutil se ve mejor."),
        ])
        + note("La edici&oacute;n no es destructiva. Tu archivo original nunca cambia, as&iacute; que siempre puedes presionar Restablecer y empezar de nuevo."))

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Edit and Crop | Lightroom Editing | Photography 1A | PVHS", nav("Step 01",dots_for(1),stepnav), top_wrap(en,es), bottom)

# ================= STEP 02: CULL, CONTACT SHEET & EXPORT =================
def step02():
    en=banner("Lightroom Editing &bull; Step 2","Cull, Contact Sheet &amp; Export","Rate and cull to 6, build a 6-Up contact sheet, and export your finals.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 contact sheet:","your 6-Up contact sheet (high-resolution JPG) showing your best 6 edited images."),
         ("6 final images:","your 6 edited photos, each exported as a high-resolution JPG."),
         ("7 files total:","upload all 7 files (the contact sheet plus the 6 images) to this Canvas assignment.")])
    en+=card("CULL / RATE AND SORT","Cull to Your Best 6 with 5-Star Ratings",
        para("Culling means keeping only your strongest work. In this class you cull with the 5-star rating. Only give 5 stars to photos you are proud of and want to keep.")
        + steps([
            ("Rate your best:","with a photo selected, press 5 on your keyboard to give it 5 stars. Repeat for each keeper."),
            ("Show only 5-star photos:","press the backslash key (\\) to open the Filter Bar, click Attribute, then click the 5th star."),
            ("Land on your best 6:","choose the 6 strongest edited images. Make sure they are your best work."),
        ])
        + note("Press 0 to remove a rating if you change your mind. You want exactly 6 for this project."),
        floatimg=star_float(False))
    en+=card("CONTACT SHEET / SHOW YOUR SIX","Build Your 6-Up Contact Sheet",
        para("A contact sheet is one page that shows your photos as thumbnails. Build a 6-Up contact sheet of your best 6 using your PVHS 6-Up preset in the Print module, then save it as a high-resolution JPG.")
        + steps([
            ("Select your 6:","in the Library, select your 6 edited images."),
            ("Open the Print module:","choose your PVHS 6-Up contact sheet preset."),
            ("Print to file as JPG:","the preset saves your page as a high-resolution JPG. This is one of your 7 files."),
        ])
        + note("You installed the contact sheet presets earlier this year, so they are ready in your Print module. If you ever need them again, they are on the Photography Course Resources page.")
        + note("Contact sheets are always saved as a high-resolution JPG, never a PDF. The preset already sets this for you."))
    en+=card("EXPORT / DELIVER YOUR FINALS","Export Your 6 Finals as High-Resolution JPEGs",
        para("Last, export your 6 edited images as high-resolution JPEGs. These are your finished photos.")
        + steps([
            ("Select your 6:","select your best 6 edited images in the Library."),
            ("Open Export:","go to File &rarr; Export."),
            ("Set the format:","choose JPEG, quality 90 or higher, and the largest size. Sharpen for screen."),
            ("Export to your project folder:","export all 6 into your OneDrive project folder so they stay together."),
        ])
        + note("Turn in all 7 files here: your 6-Up contact sheet plus your 6 exported high-resolution JPGs."))

    es=banner("Edici&oacute;n en Lightroom &bull; Paso 2","Selecciona, Hoja de Contactos y Exporta","Califica y elige 6, crea una hoja de contactos de 6 y exporta tus finales.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 hoja de contactos:","tu hoja de contactos de 6 (JPG de alta resoluci&oacute;n) que muestra tus mejores 6 im&aacute;genes editadas."),
         ("6 im&aacute;genes finales:","tus 6 fotos editadas, cada una exportada como JPG de alta resoluci&oacute;n."),
         ("7 archivos en total:","sube los 7 archivos (la hoja de contactos m&aacute;s las 6 im&aacute;genes) a esta tarea de Canvas.")])
    es+=card("SELECCIONA / CALIFICA Y ORDENA","Elige Tus Mejores 6 con 5 Estrellas",
        para("Seleccionar (cull) significa quedarte solo con tu trabajo m&aacute;s fuerte. En esta clase seleccionas con la calificaci&oacute;n de 5 estrellas. Solo da 5 estrellas a las fotos de las que est&aacute;s orgulloso y quieres guardar.")
        + steps([
            ("Califica tus mejores:","con una foto seleccionada, presiona 5 en el teclado para darle 5 estrellas. Repite con cada una que guardes."),
            ("Muestra solo las de 5 estrellas:","presiona la tecla de barra invertida (\\) para abrir la Barra de Filtros, haz clic en Atributo y luego en la 5.&ordf; estrella."),
            ("Llega a tus mejores 6:","elige las 6 im&aacute;genes editadas m&aacute;s fuertes. Aseg&uacute;rate de que sean tu mejor trabajo."),
        ])
        + note("Presiona 0 para quitar una calificaci&oacute;n si cambias de opini&oacute;n. Necesitas exactamente 6 para este proyecto."),
        floatimg=star_float(True))
    es+=card("HOJA DE CONTACTOS / MUESTRA TUS SEIS","Crea Tu Hoja de Contactos de 6",
        para("Una hoja de contactos es una p&aacute;gina que muestra tus fotos como miniaturas. Crea una hoja de contactos de 6 con tus mejores 6 usando tu ajuste PVHS de 6 en el m&oacute;dulo Imprimir, y gu&aacute;rdala como JPG de alta resoluci&oacute;n.")
        + steps([
            ("Selecciona tus 6:","en la Biblioteca, selecciona tus 6 im&aacute;genes editadas."),
            ("Abre el m&oacute;dulo Imprimir:","elige tu ajuste PVHS de hoja de contactos de 6."),
            ("Imprime a archivo como JPG:","el ajuste guarda tu p&aacute;gina como JPG de alta resoluci&oacute;n. Este es uno de tus 7 archivos."),
        ])
        + note("Instalaste los ajustes de hoja de contactos antes este a&ntilde;o, as&iacute; que ya est&aacute;n listos en tu m&oacute;dulo Imprimir. Si alguna vez los necesitas de nuevo, est&aacute;n en la p&aacute;gina de Recursos del Curso de Fotograf&iacute;a.")
        + note("Las hojas de contactos siempre se guardan como JPG de alta resoluci&oacute;n, nunca como PDF. El ajuste ya lo hace por ti."))
    es+=card("EXPORTA / ENTREGA TUS FINALES","Exporta Tus 6 Finales como JPEG de Alta Resoluci&oacute;n",
        para("Por &uacute;ltimo, exporta tus 6 im&aacute;genes editadas como JPEG de alta resoluci&oacute;n. Estas son tus fotos terminadas.")
        + steps([
            ("Selecciona tus 6:","selecciona tus mejores 6 im&aacute;genes editadas en la Biblioteca."),
            ("Abre Exportar:","ve a Archivo &rarr; Exportar."),
            ("Ajusta el formato:","elige JPEG, calidad 90 o m&aacute;s, y el tama&ntilde;o m&aacute;s grande. Enfoca para pantalla."),
            ("Exporta a tu carpeta del proyecto:","exporta las 6 a tu carpeta del proyecto en OneDrive para que queden juntas."),
        ])
        + note("Entrega los 7 archivos aqu&iacute;: tu hoja de contactos de 6 m&aacute;s tus 6 JPG de alta resoluci&oacute;n exportados."))

    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a><a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Cull, Contact Sheet and Export | Lightroom Editing | Photography 1A | PVHS", nav("Step 02",dots_for(2),stepnav), top_wrap(en,es), bottom)

# ================= STEP 03: REFLECTION =================
def step03():
    en=banner("Lightroom Editing &bull; Step 3","Reflection","Tell the story of your edits and your crop choices.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
    en+=card("STEP 03 / REFLECT","Complete and Upload the Reflection",
        float_ph("FLOAT IMAGE &bull; STUDENT TYPING THE REFLECTION &bull; DROP ART HERE")
        + para("Finish with a short reflection. It asks where your photos came from, how you cropped, what Develop edits you made, and how you culled to your best 6.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + bullets([
            ("Open it:","open the reflection Word document (.docx) from your project folder."),
            ("Answer every question:","type your answers in the boxes, in full sentences."),
            ("Save and upload:","save the document and upload it to this Canvas assignment."),
        ])
        + note("Answer honestly, in your own words."))

    es=banner("Edici&oacute;n en Lightroom &bull; Paso 3","Reflexi&oacute;n","Cuenta la historia de tus ediciones y tus decisiones de recorte.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completado, subido a esta tarea de Canvas.")])
    es+=card("PASO 03 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        float_ph("IMAGEN FLOTANTE &bull; ESTUDIANTE ESCRIBIENDO LA REFLEXI&Oacute;N &bull; PON EL ARTE AQU&Iacute;")
        + para("Termina con una reflexi&oacute;n corta. Te pregunta de d&oacute;nde salieron tus fotos, c&oacute;mo recortaste, qu&eacute; ediciones del m&oacute;dulo Revelar hiciste y c&oacute;mo elegiste tus mejores 6.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + bullets([
            ("&Aacute;brelo:","abre el documento de Word (.docx) de la reflexi&oacute;n desde tu carpeta del proyecto."),
            ("Contesta cada pregunta:","escribe tus respuestas en los cuadros, en oraciones completas."),
            ("Guarda y sube:","guarda el documento y s&uacute;belo a esta tarea de Canvas."),
        ])
        + note("Contesta con honestidad, en tus propias palabras."))

    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page("Step 3: Reflection | Lightroom Editing | Photography 1A | PVHS", nav("Step 03",dots_for(3),stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
