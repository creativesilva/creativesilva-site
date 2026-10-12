#!/usr/bin/env python3
# Photography 1A - Module 10  /  Photography 2A - Module 09: Spell Your Name Photo Walk.
# Hunt for letters around campus to spell your name in photographs (minimum 4 letters: first,
# last, or a nickname of at least 4). Capture in RAW, Manual mode, any lens and settings. Build a
# 12-Up contact sheet of the full take, cull to finals, make a 6-Up contact sheet, and export each
# final letter on its own. Forecasts the next module (layers + compiling a name collage).
#   Photo 1: an existing PRINTED letter (on a sign) IS allowed, alongside found letters.
#   Photo 2: every letter must appear NATURALLY (line, shape, shadow, reflection, texture). No
#            printed or made letters.
# Overview (Step 01, read + download) + Step 02 Capture & Contact + Step 03 Cull, Edit & Export +
# Step 04 Reflection. Bilingual EN/ES, 5th-grade. Dark teal angular framework via silva_framework.
# ALL images are gated OFF (HAVE_*=False) so every slot renders NOTHING, no placeholder boxes, until
# Chris supplies art and flips the flag (Chris 2026-10-07). Camera-kit module: NO fresh-photos note.
import os
from silva_framework import *   # shared angular chrome: banner, cards, sections, vocab, deliverables

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"

# Local ent: accents -> entities AND en-dash -> plain hyphen (never emit &ndash;, per the hard dash ban).
def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

# Every image slot starts OFF. Flip to True (and drop the file in assets/images/<course>/spell-your-name/)
# when the art is ready, then re-run this builder.
HAVE_HEADER=True       # overview hero (21:9), assets/images/<course>/spell-your-name/header-v1.jpg
HAVE_S2_FLOAT=False     # Step 02 capture float
HAVE_S3_FLOAT=False     # Step 03 CULL card float (not supplied yet)
HAVE_S3_EDIT_FLOAT=True # Step 03 EDIT card float (Lightroom editing), edit-float-v1.jpg
HAVE_S4_FLOAT=False     # Step 04 reflection float
HAVE_S5_FLOAT=True      # Step 05 collage float (Photoshop with a finished name), collage-float-v1.jpg

# RAW capture panel with a daylight starting point; the lead + note make clear that any settings
# are fair game in Manual (this assignment is about seeing letters, not a fixed exposure recipe).
def raw_settings_section(es):
    red="#f90101"
    if es:
        title="Ajustes de C&aacute;mara"
        lead=("Trabaja en modo Manual (M) y captura en RAW. Estos n&uacute;meros son solo un punto de partida para la luz del d&iacute;a. "
              "Cada ajuste vale: el obturador, la apertura y el ISO pueden cambiar, y ninguno est&aacute; prohibido. "
              "Si cambias al lente de 50mm o abres a una apertura baja como f/1.8, tus n&uacute;meros se ver&aacute;n muy distintos, y eso est&aacute; bien.")
        note_t=("El expos&iacute;metro es una gu&iacute;a, no una regla fija. Mant&eacute;nlo entre -1 y +1, no tiene que quedar exactamente en 0. "
                "Seg&uacute;n lo que fotograf&iacute;es, puede que lo lleves un poco m&aacute;s brillante (+1) o m&aacute;s oscuro (-1) para que tu letra se lea bien. "
                "Tu meta es una letra clara y n&iacute;tida en cada foto, y RAW te da margen para arreglarla despu&eacute;s.")
    else:
        title="Camera Settings"
        lead=("Work in Manual mode (M) and capture in RAW. These numbers are only a starting point for daylight. "
              "Every setting is fair game: the shutter, the aperture, and the ISO can all change, and none are off limits. "
              "If you switch to the 50mm lens or open up to a low aperture like f/1.8, your numbers will look very different, and that is okay.")
        note_t=("The light meter is a guide, not a hard rule. Keep it between -1 and +1, it does not have to sit exactly on 0. "
                "Depending on what you photograph, you may push it a little brighter (+1) or a little darker (-1) so your letter reads clearly. "
                "Your goal is one clear, sharp letter in every photo, and RAW gives you room to fix it later.")
    lead_html=f'<div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{lead}</span></div>'
    note_box=(f'<div style="background:rgba(249,1,1,0.10);border:1px solid rgba(249,1,1,0.30);border-left:4px solid {red};padding:11px 14px;margin:0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.92);line-height:1.55;">{note_t}</div>')
    return (f'<div style="background:linear-gradient(180deg,rgba(249,1,1,0.06) 0%,rgba(249,1,1,0.02) 100%);border:1px solid rgba(249,1,1,0.26);border-left:6px solid {red};padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(CAMSET_ICON, title, "#f90101", "#ff8f8f")
      + f'<div class="silva-cfloat" style="float:right;width:50%;min-width:400px;margin:2px 0 16px 30px;">{capture_panel("RAW", "1/250", "F8", "100", "all")}</div>'
      + lead_html + note_box + '</div>')

STANDARDS=[
  {"code":"SA.17.5","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Equipment &amp; Image Production","es_title":"Equipo y Producci&oacute;n de Imagen",
   "en_desc":"You use the class camera kit in Manual mode and capture in RAW on purpose.",
   "es_desc":"Usas el kit de c&aacute;mara de la clase en modo Manual y capturas en RAW a prop&oacute;sito."},
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You use line, shape, texture, and framing to find letters where most people see none.",
   "es_desc":"Usas la l&iacute;nea, la forma, la textura y el encuadre para encontrar letras donde casi nadie las ve."},
  {"code":"SA.17.2","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Visual Communication","es_title":"Comunicaci&oacute;n Visual",
   "en_desc":"You turn found shapes into clear, readable letters that spell your name.",
   "es_desc":"Conviertes formas encontradas en letras claras y legibles que escriben tu nombre."},
  {"code":"SA.17.8","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Documentation of Finished Work","es_title":"Documentaci&oacute;n del Trabajo Terminado",
   "en_desc":"You build contact sheets that present your full take and your final selections clearly.",
   "es_desc":"Creas hojas de contactos que presentan tu toma completa y tus selecciones finales con claridad."},
]

VOCAB_EN=[
 ("Texture","The surface feel of a thing in a photo, like rough bark, smooth metal, or cracked paint. Textures can hide letters."),
 ("Pattern","A design that repeats, like bricks, tiles, or fence posts. Letters can appear inside patterns."),
 ("Framing","Choosing what to keep in your photo and what to leave out. Fill the frame with one clear letter."),
 ("Rule of Thirds","Splitting your photo into a 3 by 3 grid and placing your subject on the lines or where they cross, so it looks balanced."),
 ("Abstract","A photo that shows shapes, lines, and textures more than an obvious object. Found letters often look abstract."),
 ("Found Letter","A letter you discover already in the world, made by lines, shapes, shadows, or reflections, not one you wrote or printed."),
]
VOCAB_ES=[
 ("Texture (Textura)","La sensaci&oacute;n de la superficie de algo en una foto, como corteza &aacute;spera, metal liso o pintura agrietada. Las texturas pueden esconder letras."),
 ("Pattern (Patr&oacute;n)","Un dise&ntilde;o que se repite, como ladrillos, azulejos o postes de una reja. Las letras pueden aparecer dentro de los patrones."),
 ("Framing (Encuadre)","Elegir qu&eacute; dejas dentro de tu foto y qu&eacute; dejas fuera. Llena el encuadre con una letra clara."),
 ("Rule of Thirds (Regla de los Tercios)","Dividir tu foto en una cuadr&iacute;cula de 3 por 3 y colocar tu sujeto en las l&iacute;neas o donde se cruzan, para que se vea equilibrada."),
 ("Abstract (Abstracto)","Una foto que muestra formas, l&iacute;neas y texturas m&aacute;s que un objeto obvio. Las letras encontradas suelen verse abstractas."),
 ("Found Letter (Letra Encontrada)","Una letra que descubres ya en el mundo, hecha por l&iacute;neas, formas, sombras o reflejos, no una que escribiste o imprimiste."),
]

# ---- Step 05 teal scroller: numbered how-to parts inside a contained, LOCKED .silva-scroll panel
# (scrollable-long-content rule). Teal because these are core CONTENT steps, not a linked resource.
def _sp(num, title, items):
    hd=('<div style="display:flex;align-items:center;gap:10px;margin:16px 0 8px;">'
        f'<span style="flex:0 0 auto;width:26px;height:26px;background:#00b8b8;color:#04201f;font-size:12pt;line-height:26px;text-align:center;"><strong>{num}</strong></span>'
        f'<span style="font-size:14pt;color:#80e0e0;"><strong>{title}</strong></span></div>')
    return hd+bullets(items, "#00b8b8")

def teal_scroller(hint, parts):
    hintline=f'<div style="font-size:11pt;color:#80e0e0;margin-bottom:8px;opacity:0.85;">&#8595; {hint}</div>'
    scroll=('<div class="silva-scroll" style="max-height:470px;overflow-y:auto;padding:14px 16px 20px;border:1px solid rgba(0,184,184,0.30);'
      'background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, rgba(0,0,0,0.14) 88%, rgba(0,184,184,0.16) 100%);">'
      f'{parts}</div>')
    return hintline+scroll

def build(course):
    p2 = (course == "photo2")
    MODNUM = "09" if p2 else "10"
    CL_EN = "Photography 2A" if p2 else "Photography 1A"
    CL_ES = "Fotograf&iacute;a 2A" if p2 else "Fotograf&iacute;a 1A"
    PHOTO2TAG = "-Photo2" if p2 else ""
    IMGDIR=f"{SITE}/assets/images/{course}/spell-your-name"
    HEADER=f"{IMGDIR}/header-v2.jpg"
    S2_FLOAT=f"{IMGDIR}/capture-float-v1.jpg"
    S3_FLOAT=f"{IMGDIR}/cull-float-v1.jpg"
    S3_EDIT_FLOAT=f"{IMGDIR}/edit-float-v1.jpg"
    S4_FLOAT=f"{IMGDIR}/reflection-float-v1.jpg"
    S5_FLOAT=f"{IMGDIR}/collage-float-v1.jpg"
    REFLECT_EN=f"{SITE}/assets/course-documents/Spell-Your-Name{PHOTO2TAG}-Reflection-EN.docx"
    REFLECT_ES=f"{SITE}/assets/course-documents/Spell-Your-Name{PHOTO2TAG}-Reflection-ES.docx"
    OVER=f"{course}-spell-your-name-overview.html"
    S2=f"{course}-spell-your-name-step02-capture-contact.html"
    S3=f"{course}-spell-your-name-step03-cull-edit-export.html"
    S4=f"{course}-spell-your-name-step04-reflection.html"
    S5=f"{course}-spell-your-name-step05-name-collage.html"
    # Name-collage PSD templates (shared by both courses). Hosted as raw .psd files (Chris: a single
    # .psd does not need zipping). Each is a transparent template, one 3.5in letter slot per "up"
    # (4-Up ... 7-Up). The download attribute makes the browser save the .psd rather than open it.
    TPL_DIR=f"{SITE}/assets/templates/psd/name-collage"
    TPL={n:f"{TPL_DIR}/Name_Template_{n}up.psd" for n in (4,5,6,7)}

    def nav(current,dots,stepnav):
        return ('      <div class="silva-breadcrumb">\n'
                '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
                '        <span class="bc-sep">&rsaquo;</span>\n'
                f'        <a href="{OVER}" class="bc-hide-sm">Spell Your Name</a>\n'
                '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
                f'        <span class="bc-current">{current}</span>\n'
                '      </div>\n'
                '      <div class="silva-nav-spacer"></div>\n'
                f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
                f'      <div class="silva-step-nav">{stepnav}</div>')
    HREFS=[OVER,S2,S3,S4,S5]; TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04"),("5","Step 05")]
    def dots_for(ai):
        return "".join(dot("" if i==ai else HREFS[i], lab, title, i==ai, module=False) for i,(lab,title) in enumerate(TITLES))

    # ---- course-specific concept copy (the one real Photo 1 vs Photo 2 difference) ----
    if p2:
        concept_rule_en=("In Photography 2 every letter must appear <strong>naturally</strong>, made by lines, shapes, shadows, reflections, or textures. "
                         "You may <strong>not</strong> photograph a letter that was made as a letter: no signs, no printed letters, no painted letters. "
                         "Train your eye to see letters hiding in things that are not letters at all.")
        concept_rule_es=("En Fotograf&iacute;a 2 cada letra debe aparecer de forma <strong>natural</strong>, hecha por l&iacute;neas, formas, sombras, reflejos o texturas. "
                         "<strong>No</strong> puedes fotografiar una letra hecha como letra: nada de letreros, letras impresas ni letras pintadas. "
                         "Entrena tu ojo para ver letras escondidas en cosas que no son letras.")
        capture_rule_en=("Natural letters only. Every letter has to be formed by line, shape, shadow, reflection, or texture. Do not photograph a printed or made letter.")
        capture_rule_es=("Solo letras naturales. Cada letra debe estar formada por l&iacute;nea, forma, sombra, reflejo o textura. No fotograf&iacute;es una letra impresa o hecha.")
    else:
        concept_rule_en=("In Photography 1 you have two ways to find a letter. You may photograph a letter that is already <strong>printed</strong> somewhere, like a letter on a sign, "
                         "and you may also find letters hiding in <strong>shadows, lines, reflections, and textures</strong>. Mix both and have fun hunting.")
        concept_rule_es=("En Fotograf&iacute;a 1 tienes dos maneras de encontrar una letra. Puedes fotografiar una letra que ya est&eacute; <strong>impresa</strong> en alg&uacute;n lugar, como una letra en un letrero, "
                         "y tambi&eacute;n puedes encontrar letras escondidas en <strong>sombras, l&iacute;neas, reflejos y texturas</strong>. Combina las dos y div&iacute;ertete buscando.")
        capture_rule_en=("A printed letter on a sign is allowed in Photography 1, and so are letters you find in shadows, lines, reflections, and textures.")
        capture_rule_es=("En Fotograf&iacute;a 1 se permite una letra impresa en un letrero, y tambi&eacute;n las letras que encuentras en sombras, l&iacute;neas, reflejos y texturas.")

    def downloads_block(es):
        heading="Descarga Tus Archivos" if es else "Download Your Files"
        lead=("Descarga el documento de reflexi&oacute;n de este m&oacute;dulo. Tus ajustes de hoja de contactos ya est&aacute;n instalados en Lightroom; si alguna vez los necesitas otra vez, est&aacute;n en la p&aacute;gina de Resumen del curso." if es
              else "Download this module&rsquo;s reflection document. Your contact sheet presets are already installed in Lightroom; if you ever need them again, they are on the Course Overview page.")
        reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
        ref=REFLECT_ES if es else REFLECT_EN
        return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
          + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
          + para(lead)
          + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
          + dl_link(ref,reflabel,row=True)
          + '</div>'
          + folder_note(es, AREA) + '</div>')

    # Step 05 ONLY: the 4 name-collage templates, embedded so students pick the one that fits their
    # name length (Chris: put the template downloads ON this final step, student chooses which).
    def tpl_downloads(es):
        heading="Descarga Tu Plantilla" if es else "Download Your Template"
        if es:
            lead="Elige la plantilla que le queda a tu nombre, luego desc&aacute;rgala. Cuenta las letras del nombre que escribiste."
            picks=[("4 letras:","descarga la plantilla 4-Up."),
                   ("5 letras:","descarga la plantilla 5-Up."),
                   ("6 letras:","descarga la plantilla 6-Up."),
                   ("7 letras o m&aacute;s:","descarga la plantilla 7-Up y acomoda las letras de m&aacute;s de forma creativa.")]
            labels={4:"Plantilla 4-Up (.psd)",5:"Plantilla 5-Up (.psd)",6:"Plantilla 6-Up (.psd)",7:"Plantilla 7-Up (.psd)"}
            tnote="El fondo de la plantilla es transparente a prop&oacute;sito: se ve como un tablero de cuadros. T&uacute; le pondr&aacute;s tu propio fondo en Photoshop."
        else:
            lead="Pick the template that fits your name, then download it. Count the letters in the name you spelled."
            picks=[("4 letters:","download the 4-Up template."),
                   ("5 letters:","download the 5-Up template."),
                   ("6 letters:","download the 6-Up template."),
                   ("7 letters or more:","download the 7-Up template and fit the extra letters in creatively.")]
            labels={4:"4-Up Template (.psd)",5:"5-Up Template (.psd)",6:"6-Up Template (.psd)",7:"7-Up Template (.psd)"}
            tnote="The template background is see-through on purpose: it looks like a checkerboard. You will add your own background in Photoshop."
        btns=('<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:10px;">'
              + "".join(dl_link(TPL[n],labels[n],row=True) for n in (4,5,6,7)) + '</div>')
        return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
          + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
          + para(lead)
          + bullets(picks, "#FF6B1A")
          + btns
          + note_orange(tnote)
          + folder_note(es, AREA) + '</div>')

    # ================= OVERVIEW (Step 01) =================
    def overview():
        en=banner(f"Module {MODNUM} &bull; Step 01","Spell Your Name: Start Here","Read this page and download your files, then go to Step 02 to capture. This is a photo walk about finding letters.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
        en+=type_card("overview","Step 01 &middot; Overview &amp; Download","Spell Your Name in Photographs",
            para("On this photo walk you hunt for letters around campus to spell your name in photographs. Find one letter at a time, in signs, shadows, lines, reflections, textures, and shapes.")
            + para("You need at least <strong>4 letters</strong>. Use your first name, your last name, or a nickname, whatever fits you, as long as it is at least 4 letters long. A short 3-letter nickname is not enough, so pick a name with 4 or more.")
            + para(concept_rule_en)
            + (framed(HEADER,"A Pioneer Valley student working in Adobe Photoshop on an iMac in a bright computer lab, placing found-letter photos to spell the name RENEE, with classmates working at iMacs behind her") if HAVE_HEADER else ""))
        en+=standards_box(False, STANDARDS)
        en+=downloads_block(False)
        en+=card("THE CONCEPT / WHAT TO LOOK FOR","Letters Are Everywhere",
            para("Once you start looking, letters hide in plain sight. The legs of a bench can make an <strong>A</strong>. A railing and its shadow can make an <strong>H</strong>. A puddle can reflect a curve into a <strong>C</strong>. A crack in the cement can make an <strong>L</strong>.")
            + para("Look for <strong>line, shape, shadow, reflection, texture, and pattern</strong>. Move around and change your angle until the shape reads clearly as a letter."))
        en+=card("HOW THIS MODULE WORKS","From the Walk to Finished Letters",
            para("You are on Step 01 now: read this page and download your reflection document below. Here are the steps that follow.")
            + bullets([
                ("Step 02 &middot; Capture &amp; Contact Sheet:","on the walk, capture the letters of your name in RAW. Import your full take and build a 12-Up contact sheet of everything you captured."),
                ("Step 03 &middot; Cull, Edit &amp; Export:","select your strongest photo for each letter, edit it clean, build a 6-Up contact sheet of your finals, and export each final letter on its own."),
                ("Step 04 &middot; Reflection:","tell what you learned about finding letters and making them read."),
                ("Step 05 &middot; Name Collage in Photoshop:","open Photoshop for the first time and place your letters into one template to spell your name, then export your finished piece."),
            ]))
        en+=resources_card("Key Words",
            vocab_grid("On the Quiz",
              "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
              VOCAB_EN), False)
        en+=next_up("UP NEXT &middot; STEP 02 - Capture &amp; Contact Sheet","Walk campus, capture your letters in RAW, and build a 12-Up contact sheet.")

        es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 01","Escribe Tu Nombre: Empieza Aqu&iacute;","Lee esta p&aacute;gina y descarga tus archivos, luego ve al Paso 02 para capturar. Esta es una caminata para encontrar letras.","#top","Back to English", HICON_PHOTO_WALK)
        es+=type_card("overview","Paso 01 &middot; Resumen y Descarga","Escribe Tu Nombre en Fotograf&iacute;as",
            para("En esta caminata fotogr&aacute;fica buscas letras por la escuela para escribir tu nombre en fotograf&iacute;as. Encuentra una letra a la vez, en letreros, sombras, l&iacute;neas, reflejos, texturas y formas.")
            + para("Necesitas al menos <strong>4 letras</strong>. Usa tu primer nombre, tu apellido o un apodo, el que te quede, siempre que tenga al menos 4 letras. Un apodo corto de 3 letras no alcanza, as&iacute; que elige un nombre de 4 o m&aacute;s.")
            + para(concept_rule_es)
            + (framed(HEADER,"Una estudiante de Pioneer Valley trabajando en Adobe Photoshop en una iMac en un laboratorio de c&oacute;mputo iluminado, colocando fotos de letras encontradas para escribir el nombre RENEE, con compa&ntilde;eros trabajando en iMacs detr&aacute;s") if HAVE_HEADER else ""))
        es+=standards_box(True, STANDARDS)
        es+=downloads_block(True)
        es+=card("EL CONCEPTO / QU&Eacute; BUSCAR","Las Letras Est&aacute;n en Todas Partes",
            para("Cuando empiezas a mirar, las letras se esconden a la vista. Las patas de una banca pueden formar una <strong>A</strong>. Un barandal y su sombra pueden formar una <strong>H</strong>. Un charco puede reflejar una curva en una <strong>C</strong>. Una grieta en el cemento puede formar una <strong>L</strong>.")
            + para("Busca <strong>l&iacute;nea, forma, sombra, reflejo, textura y patr&oacute;n</strong>. Mu&eacute;vete y cambia tu &aacute;ngulo hasta que la forma se lea claramente como una letra."))
        es+=card("C&Oacute;MO FUNCIONA ESTE M&Oacute;DULO","De la Caminata a las Letras Terminadas",
            para("Est&aacute;s en el Paso 01 ahora: lee esta p&aacute;gina y descarga tu documento de reflexi&oacute;n abajo. Estos son los pasos que siguen.")
            + bullets([
                ("Paso 02 &middot; Captura y Hoja de Contactos:","en la caminata, captura las letras de tu nombre en RAW. Importa tu toma completa y crea una hoja de contactos 12-Up de todo lo que capturaste."),
                ("Paso 03 &middot; Selecciona, Edita y Exporta:","elige tu mejor foto de cada letra, ed&iacute;tala limpia, crea una hoja de contactos 6-Up de tus finales y exporta cada letra final por separado."),
                ("Paso 04 &middot; Reflexi&oacute;n:","cuenta qu&eacute; aprendiste al encontrar letras y hacer que se lean."),
                ("Paso 05 &middot; Collage del Nombre en Photoshop:","abre Photoshop por primera vez y coloca tus letras en una plantilla para escribir tu nombre, luego exporta tu pieza terminada."),
            ]))
        es+=resources_card("Palabras Clave",
            vocab_grid("En el Examen",
              "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
              VOCAB_ES), True)
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 02 - Captura y Hoja de Contactos","Camina por la escuela, captura tus letras en RAW y crea una hoja de contactos 12-Up.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S2}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
        return wrap_page(f"Spell Your Name | {CL_EN} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 02: Capture & Contact =================
    def step02():
        en=banner(f"Module {MODNUM} &bull; Step 02","Capture &amp; Contact Sheet","Capture the letters of your name in RAW, then build a 12-Up contact sheet of your full take.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
        en+=raw_settings_section(False)
        en+=card("CAPTURE / ON THE WALK","Find and Photograph Your Letters",
            (float_right(S2_FLOAT,"A Pioneer Valley student kneeling to photograph a letter shape found in a railing on campus","Fill the frame with one clear letter, then try another angle.") if HAVE_S2_FLOAT else "")
            + para("Walk campus and hunt for the letters of your name. Capture one clear letter in each photo and fill the frame with it.")
            + note(capture_rule_en)
            + bullets([
                ("One letter per photo:","each photo shows only one letter, clear and easy to read."),
                ("Fill the frame:","get close so the letter fills the photo, with little empty space around it."),
                ("At least 4 letters:","capture every letter of your name, 4 or more."),
                ("Take a few of each:","capture each letter a few times, from different angles, so you have choices when you cull."),
            ]))
        en+=card("CONTACT SHEET / YOUR FULL TAKE","Build Your 12-Up Contact Sheet",
            para("Bring the camera to a computer and import your full take into Lightroom Classic, into your project folder. Then build a 12-Up contact sheet that shows your whole take, every letter photo you captured.")
            + note("12-Up is just the name of the contact sheet template. Your sheet can show more or fewer than 12 photos, that is fine. It just shows your full take.")
            + bullets([
                ("Import first:","import your photos into Lightroom, into your Photography project folder."),
                ("Use the 12-Up preset:","make the contact sheet with the 12-Up preset, already installed in Lightroom."),
                ("Export as JPG:","print the contact sheet to file as a high-resolution JPG."),
            ]))
        en+=deliverables_box(False,
            [("1 contact sheet (JPG):","a 12-Up contact sheet of your full take, exported as a high-resolution JPG, uploaded to this Canvas assignment.")])
        en+=next_up("UP NEXT &middot; STEP 03 - Cull, Edit &amp; Export","Select your strongest letters, edit them clean, and export each one.")

        es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 02","Captura y Hoja de Contactos","Captura las letras de tu nombre en RAW, luego crea una hoja de contactos 12-Up de tu toma completa.","#top","Back to English", HICON_PHOTO_WALK)
        es+=raw_settings_section(True)
        es+=card("CAPTURA / EN LA CAMINATA","Encuentra y Fotograf&iacute;a Tus Letras",
            (float_right(S2_FLOAT,"Un estudiante de Pioneer Valley arrodillado fotografiando la forma de una letra encontrada en un barandal de la escuela","Llena el encuadre con una letra clara, luego prueba otro &aacute;ngulo.") if HAVE_S2_FLOAT else "")
            + para("Camina por la escuela y busca las letras de tu nombre. Captura una letra clara en cada foto y llena el encuadre con ella.")
            + note(capture_rule_es)
            + bullets([
                ("Una letra por foto:","cada foto muestra solo una letra, clara y f&aacute;cil de leer."),
                ("Llena el encuadre:","ac&eacute;rcate para que la letra llene la foto, con poco espacio vac&iacute;o alrededor."),
                ("Al menos 4 letras:","captura cada letra de tu nombre, 4 o m&aacute;s."),
                ("Toma varias de cada una:","captura cada letra varias veces, desde &aacute;ngulos distintos, para tener opciones al seleccionar."),
            ]))
        es+=card("HOJA DE CONTACTOS / TU TOMA COMPLETA","Crea Tu Hoja de Contactos 12-Up",
            para("Lleva la c&aacute;mara a una computadora e importa tu toma completa a Lightroom Classic, a tu carpeta del proyecto. Luego crea una hoja de contactos 12-Up que muestre toda tu toma, cada foto de letra que capturaste.")
            + note("12-Up es solo el nombre de la plantilla de la hoja de contactos. Tu hoja puede mostrar m&aacute;s o menos de 12 fotos, eso est&aacute; bien. Solo muestra tu toma completa.")
            + bullets([
                ("Importa primero:","importa tus fotos a Lightroom, a tu carpeta del proyecto de Fotograf&iacute;a."),
                ("Usa el preset 12-Up:","crea la hoja de contactos con el preset 12-Up, ya instalado en Lightroom."),
                ("Exporta como JPG:","imprime la hoja de contactos a archivo como un JPG de alta resoluci&oacute;n."),
            ]))
        es+=deliverables_box(True,
            [("1 hoja de contactos (JPG):","una hoja de contactos 12-Up de tu toma completa, exportada como JPG de alta resoluci&oacute;n, subida a esta tarea de Canvas.")])
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 03 - Selecciona, Edita y Exporta","Elige tus letras m&aacute;s fuertes, ed&iacute;talas limpias y exporta cada una.")

        stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
        return wrap_page(f"Step 2: Capture and Contact Sheet | Spell Your Name | {CL_EN} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 03: Cull, Edit & Export =================
    def step03():
        en=banner(f"Module {MODNUM} &bull; Step 03","Cull, Edit &amp; Export","Select your strongest letters, edit them clean, build a 6-Up contact sheet, and export each one.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
        en+=card("CULL / SELECT YOUR FINALS","Cull to Your Best Letters",
            (float_right(S3_FLOAT,"A Pioneer Valley student culling letter photos in Lightroom Classic on an iMac in the lab","Compare your angles and keep the clearest letter of each.") if HAVE_S3_FLOAT else "")
            + para("Now cull. Culling means looking through your full take and keeping only the strongest. For each letter of your name, select the single clearest, sharpest photo.")
            + bullets([
                ("One per letter:","select your best photo of each letter, at least 4 letters in all."),
                ("Clear and readable:","each letter must be easy to read, sharp, and well framed."),
                ("Put them in order:","keep your selected letters in the order they spell your name."),
            ]))
        en+=card("EDIT / MAKE THEM CLEAN","Edit Your Selected Letters",
            (float_right(S3_EDIT_FLOAT,"A Pioneer Valley student editing her letter photos in Adobe Lightroom Classic on an iMac in the lab, a tree forming a letter on the screen","Edit each letter clean in Lightroom so it reads sharp.") if HAVE_S3_EDIT_FLOAT else "")
            + para("Edit each selected letter so it looks clean and natural. You captured in RAW, so you have room to adjust.")
            + bullets([
                ("Crop and straighten:","crop tight to the letter and straighten it so it reads clearly."),
                ("Exposure and white balance:","fix the exposure and white balance so the letter looks right."),
                ("Keep it natural:","clean, simple edits. Do not over-do it."),
            ]))
        en+=card("CONTACT SHEET + EXPORT / YOUR FINALS","Build a 6-Up Sheet, Then Export Each Letter",
            para("Make a 6-Up contact sheet of your final edited letters, then export each final letter on its own.")
            + note("6-Up is just the name of the template. Your sheet can show more or fewer than 6 letters, as long as it shows your finished letters.")
            + bullets([
                ("6-Up contact sheet:","build a 6-Up contact sheet of your final letters and export it as a high-resolution JPG."),
                ("Export each letter:","export each final letter image on its own as a JPG. Name them so they stay in order, like 1_C.jpg, 2_H.jpg."),
                ("Count your files:","that is the 6-Up contact sheet plus one JPG per letter, at least 5 files in all."),
            ]))
        en+=deliverables_box(False,
            [("1 contact sheet (JPG):","a 6-Up contact sheet of your final letters, as a high-resolution JPG."),
             ("Each letter (JPG):","every final letter exported on its own as a JPG, at least 4 letters.")])
        en+=next_up("UP NEXT &middot; STEP 04 - Reflection","Reflect on your photo walk, your letters, and what you learned.")

        es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 03","Selecciona, Edita y Exporta","Elige tus letras m&aacute;s fuertes, ed&iacute;talas limpias, crea una hoja de contactos 6-Up y exporta cada una.","#top","Back to English", HICON_PHOTO_WALK)
        es+=card("SELECCIONA / ELIGE TUS FINALES","Selecciona (Cull) Tus Mejores Letras",
            (float_right(S3_FLOAT,"Un estudiante de Pioneer Valley seleccionando fotos de letras en Lightroom Classic en una iMac en el laboratorio","Compara tus &aacute;ngulos y qu&eacute;date con la letra m&aacute;s clara de cada una.") if HAVE_S3_FLOAT else "")
            + para("Ahora selecciona (cull). Seleccionar significa revisar tu toma completa y quedarte solo con las m&aacute;s fuertes. Para cada letra de tu nombre, elige la foto m&aacute;s clara y n&iacute;tida.")
            + bullets([
                ("Una por letra:","elige tu mejor foto de cada letra, al menos 4 letras en total."),
                ("Clara y legible:","cada letra debe ser f&aacute;cil de leer, n&iacute;tida y bien encuadrada."),
                ("Ponlas en orden:","mant&eacute;n tus letras seleccionadas en el orden en que escriben tu nombre."),
            ]))
        es+=card("EDITA / D&Eacute;JALAS LIMPIAS","Edita Tus Letras Seleccionadas",
            (float_right(S3_EDIT_FLOAT,"Una estudiante de Pioneer Valley editando sus fotos de letras en Adobe Lightroom Classic en una iMac en el laboratorio, un &aacute;rbol formando una letra en la pantalla","Edita cada letra limpia en Lightroom para que se lea n&iacute;tida.") if HAVE_S3_EDIT_FLOAT else "")
            + para("Edita cada letra seleccionada para que se vea limpia y natural. Capturaste en RAW, as&iacute; que tienes margen para ajustar.")
            + bullets([
                ("Recorta y endereza:","recorta pegado a la letra y ender&eacute;zala para que se lea con claridad."),
                ("Exposici&oacute;n y balance de blancos:","corrige la exposici&oacute;n y el balance de blancos para que la letra se vea bien."),
                ("Mant&eacute;nla natural:","ediciones limpias y simples. No exageres."),
            ]))
        es+=card("HOJA DE CONTACTOS + EXPORTAR / TUS FINALES","Crea una Hoja 6-Up y Luego Exporta Cada Letra",
            para("Crea una hoja de contactos 6-Up de tus letras finales editadas, luego exporta cada letra final por separado.")
            + note("6-Up es solo el nombre de la plantilla. Tu hoja puede mostrar m&aacute;s o menos de 6 letras, siempre que muestre tus letras terminadas.")
            + bullets([
                ("Hoja de contactos 6-Up:","crea una hoja de contactos 6-Up de tus letras finales y exp&oacute;rtala como JPG de alta resoluci&oacute;n."),
                ("Exporta cada letra:","exporta cada letra final por separado como JPG. Nómbralas para que queden en orden, como 1_C.jpg, 2_H.jpg."),
                ("Cuenta tus archivos:","esa es la hoja de contactos 6-Up m&aacute;s un JPG por letra, al menos 5 archivos en total."),
            ]))
        es+=deliverables_box(True,
            [("1 hoja de contactos (JPG):","una hoja de contactos 6-Up de tus letras finales, como JPG de alta resoluci&oacute;n."),
             ("Cada letra (JPG):","cada letra final exportada por separado como JPG, al menos 4 letras.")])
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 04 - Reflexi&oacute;n","Reflexiona sobre tu caminata, tus letras y lo que aprendiste.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S4}" class="silva-step-btn">Step 04 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S4}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
        return wrap_page(f"Step 3: Cull, Edit and Export | Spell Your Name | {CL_EN} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 04: Reflection =================
    def step04():
        en=banner(f"Module {MODNUM} &bull; Step 04","Turn In Your Reflection","Reflect on your photo walk, your letters, and what you learned.","#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
        en+=card("STEP 04 / REFLECT","Complete and Upload the Reflection",
            (float_right(S4_FLOAT,"A Pioneer Valley student typing the Spell Your Name reflection in the Word document on an iMac in the lab","Type your answers right in the reflection document.") if HAVE_S4_FLOAT else "")
            + para("Finish with a short reflection. It asks which name you spelled, where you found your letters, how you culled, and which letter is your favorite.")
            + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
            + bullets([
                ("Open it:","open the reflection Word document (.docx) from your project folder."),
                ("Answer every question:","type your answers in the boxes, in full sentences."),
                ("Save and upload:","save the document and upload it to this Canvas assignment."),
            ])
            + note("Answer honestly, in your own words."))
        en+=deliverables_box(False,
            [("1 reflection (.docx):","your completed reflection Word document, uploaded to this Canvas assignment.")])
        en+=next_up("UP NEXT &middot; STEP 05 - Spell Your Name as One Collage","Open Photoshop for the first time and place your finished letters into one template to spell your name.")

        es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 04","Entrega Tu Reflexi&oacute;n","Reflexiona sobre tu caminata, tus letras y lo que aprendiste.","#top","Back to English", HICON_REFLECT)
        es+=card("PASO 04 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
            (float_right(S4_FLOAT,"Un estudiante de Pioneer Valley escribiendo la reflexi&oacute;n de Escribe Tu Nombre en el documento de Word en una iMac en el laboratorio","Escribe tus respuestas directamente en el documento de reflexi&oacute;n.") if HAVE_S4_FLOAT else "")
            + para("Termina con una reflexi&oacute;n corta. Te pregunta qu&eacute; nombre escribiste, d&oacute;nde encontraste tus letras, c&oacute;mo seleccionaste y cu&aacute;l letra es tu favorita.")
            + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
            + bullets([
                ("&Aacute;brelo:","abre el documento de Word (.docx) de la reflexi&oacute;n desde tu carpeta del proyecto."),
                ("Contesta cada pregunta:","escribe tus respuestas en los cuadros, en oraciones completas."),
                ("Guarda y sube:","guarda el documento y s&uacute;belo a esta tarea de Canvas."),
            ])
            + note("Contesta con honestidad, en tus propias palabras."))
        es+=deliverables_box(True,
            [("1 reflexi&oacute;n (.docx):","tu documento de Word de la reflexi&oacute;n, subido a esta tarea de Canvas.")])
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 05 - Escribe Tu Nombre en un Collage","Abre Photoshop por primera vez y coloca tus letras terminadas en una plantilla para escribir tu nombre.")

        stepnav=f'<a href="{S3}" class="silva-step-btn">&#8592; Step 03</a> <a href="{S5}" class="silva-step-btn">Step 05 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S3}" class="silva-bottom-btn">&#8592; Step 03</a><a href="{S5}" class="silva-bottom-btn">Step 05 &#8594;</a></div>'
        return wrap_page(f"Step 4: Reflection | Spell Your Name | {CL_EN} | PVHS", nav("Step 04",dots_for(3),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 05: Name Collage in Photoshop (first Photoshop use) =================
    def step05():
        en=banner(f"Module {MODNUM} &bull; Step 05","Spell Your Name as One Collage","Open Photoshop for the first time and place your letters into one template to spell your name.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
        en+=card("STEP 05 / BUILD IT IN PHOTOSHOP","Put Your Letters Together",
            (float_right(S5_FLOAT,"Adobe Photoshop open with the name RENEE spelled out in the collage template: five found-letter photos in a row over a starry background, with the layers listed on the right","What you are building: your letters placed in the template to spell your name.") if HAVE_S5_FLOAT else "")
            + para("Now put it all together. You will open <strong>Photoshop</strong> for the first time and build one finished piece: your letters placed in a row that spells your name.")
            + para("This is your first time in Photoshop, so go slow. This page walks you through every click. If you make a mistake, press <strong>Cmd</strong> + <strong>Z</strong> to undo it.")
            + note("You already made your letters in Step 03. Here you just place them into one template and spell your name. You do not take any new photos."))
        en+=deliverables_box(False,
            [("1 name collage (JPG):","your finished name, spelled out in the template with a background, exported as a high-resolution JPG and uploaded to this Canvas assignment.")])
        en+=tpl_downloads(False)
        en+=card("CHOOSE YOUR BACKGROUND","Your Template Is See-Through, So Add a Background",
            para("Your template background is see-through, so it looks like a checkerboard. You need to put a background photo behind your letters. Pick one of two ways:")
            + bullets([
                ("Use your own photo:","any photo you like, from your project folder."),
                ("Download a free photo:","go to <strong>unsplash.com</strong>, search for something you like, like sky, wall, or paper, and download it for free. You do not need an account."),
            ])
            + note("Readability tip: a plain, simple background makes your letters easier to read than a busy, cluttered one."))
        hint_en="Scroll inside the box to see all six parts."
        parts_en=(
          _sp("1","Set up Photoshop (do this once)",[
            ("Open Photoshop:","click the Photoshop icon in your Dock, or open it from your Applications folder."),
            ("Open Settings:","in the top menu bar, click <strong>Photoshop &gt; Settings &gt; General</strong>. A shortcut is <strong>Cmd</strong> + <strong>K</strong>."),
            ("Turn off Smart Objects:","find the box that says <strong>Always Create Smart Objects when Placing</strong> and click it so the checkmark is OFF (empty)."),
            ("Click OK:","now your letters come in as normal layers you can crop and erase, not locked Smart Objects. You only do this once on a computer."),
          ])
          + _sp("2","Open your template",[
            ("Find your template:","the template you downloaded is a .psd file in your Downloads folder. Move it into your project folder first."),
            ("Open it:","in Photoshop, go to <strong>File &gt; Open</strong>. Click your template .psd, then click Open. You will see a long, see-through strip. Each square is one slot for a letter."),
          ])
          + _sp("3","Add your background",[
            ("Place your photo:","go to <strong>File &gt; Place Embedded</strong>. Click your background photo, your own or the one from Unsplash, then click Place."),
            ("Make it fill the strip:","your photo drops in with a box and handles around it. Drag a corner handle outward until the photo covers the whole strip. Drag from the middle to move it."),
            ("Set it in place:","press <strong>Return</strong> (Enter) to finish placing it."),
            ("Keep it on the bottom:","look at the Layers panel on the right side. Your background should sit at the bottom of the list, under your letters."),
          ])
          + _sp("4","Place and trim your first letter",[
            ("Place a letter:","go to <strong>File &gt; Place Embedded</strong> again. Click your first letter photo, like 1_C.jpg, then click Place."),
            ("Move it to the first slot:","drag the letter to the first slot on the left."),
            ("Size it to fit:","drag a corner handle to make the letter fit its slot. It keeps its shape as you drag."),
            ("Set it in place:","press <strong>Return</strong> (Enter) to finish."),
            ("Trim the extra space:","if there is extra photo on the side of your letter, pick the <strong>Rectangular Marquee</strong> tool, drag a box around the extra part, then press <strong>Delete</strong>. It disappears and your background shows through. This works because your letter is a normal layer, not a Smart Object."),
          ])
          + _sp("5","Place the rest of your letters",[
            ("Repeat for each letter:","do <strong>File &gt; Place Embedded</strong> for each letter, in order, left to right, so they spell your name. Trim each one the same way if it needs it."),
            ("Line them up:","keep the letters in a neat row across the strip so your name reads clearly."),
            ("More letters than slots?","if your name is longer than the template, use the 7-Up template and fit the extra letters in creatively. Make them a little smaller or overlap them a bit, but keep the name easy to read."),
          ])
          + _sp("6","Export and turn it in",[
            ("Export as a JPG:","go to <strong>File &gt; Export &gt; Export As</strong>. Set the format to <strong>JPG</strong> and the quality to high, then click Export."),
            ("Save it to your project folder:","name it with your name, like Collage_Chris.jpg, and save it in your Photography project folder."),
            ("Upload to Canvas:","upload your finished JPG to this Canvas assignment."),
          ])
        )
        en+=card("HOW TO BUILD IT / STEP BY STEP","Place Your Letters in Photoshop",
            para("Follow these steps in order. Take your time.")
            + teal_scroller(hint_en, parts_en))
        en+=next_up("UP NEXT &middot; MORE APERTURE WORK","This week&rsquo;s photo walk: explore aperture with all three lenses in your kit, the 50mm, the 18-45mm, and the 55-210mm. More details soon.")

        es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 05","Escribe Tu Nombre en un Collage","Abre Photoshop por primera vez y coloca tus letras en una plantilla para escribir tu nombre.","#top","Back to English", HICON_DESIGN)
        es+=card("PASO 05 / H&Aacute;ZLO EN PHOTOSHOP","Junta Tus Letras",
            (float_right(S5_FLOAT,"Adobe Photoshop abierto con el nombre RENEE escrito en la plantilla del collage: cinco fotos de letras en fila sobre un fondo de estrellas, con las capas a la derecha","Lo que vas a crear: tus letras colocadas en la plantilla para escribir tu nombre.") if HAVE_S5_FLOAT else "")
            + para("Ahora junta todo. Abrirás <strong>Photoshop</strong> por primera vez y crearás una pieza terminada: tus letras en fila que escriben tu nombre.")
            + para("Es tu primera vez en Photoshop, así que ve despacio. Esta página te guía en cada clic. Si te equivocas, presiona <strong>Cmd</strong> + <strong>Z</strong> para deshacer.")
            + note("Ya hiciste tus letras en el Paso 03. Aquí solo las colocas en una plantilla y escribes tu nombre. No tomas fotos nuevas."))
        es+=deliverables_box(True,
            [("1 collage del nombre (JPG):","tu nombre terminado, escrito en la plantilla con un fondo, exportado como JPG de alta resolución y subido a esta tarea de Canvas.")])
        es+=tpl_downloads(True)
        es+=card("ELIGE TU FONDO","Tu Plantilla Es Transparente, Ponle un Fondo",
            para("El fondo de tu plantilla es transparente, por eso se ve como un tablero de cuadros. Necesitas poner una foto de fondo detrás de tus letras. Elige una de dos maneras:")
            + bullets([
                ("Usa tu propia foto:","cualquier foto que te guste, de tu carpeta del proyecto."),
                ("Descarga una foto gratis:","ve a <strong>unsplash.com</strong>, busca algo que te guste, como cielo, pared o papel, y descárgala gratis. No necesitas cuenta."),
            ])
            + note("Consejo de legibilidad: un fondo sencillo hace que tus letras se lean más fácil que uno muy cargado."))
        hint_es="Desplázate dentro del cuadro para ver las seis partes."
        parts_es=(
          _sp("1","Configura Photoshop (hazlo una vez)",[
            ("Abre Photoshop:","haz clic en el ícono de Photoshop en el Dock, o ábrelo desde la carpeta de Aplicaciones."),
            ("Abre Ajustes:","en la barra de menú de arriba, haz clic en <strong>Photoshop &gt; Ajustes &gt; Generales</strong>. Un atajo es <strong>Cmd</strong> + <strong>K</strong>."),
            ("Desactiva los objetos inteligentes:","busca la casilla que dice <strong>Crear siempre objetos inteligentes al colocar</strong> y haz clic para quitar la palomita (que quede vacía)."),
            ("Haz clic en OK:","ahora tus letras entran como capas normales que puedes recortar y borrar, no como objetos inteligentes bloqueados. Esto solo se hace una vez en una computadora."),
          ])
          + _sp("2","Abre tu plantilla",[
            ("Busca tu plantilla:","la plantilla que descargaste es un archivo .psd en tu carpeta de Descargas. Primero muévela a tu carpeta del proyecto."),
            ("Ábrela:","en Photoshop, ve a <strong>Archivo &gt; Abrir</strong>. Haz clic en tu plantilla .psd y luego en Abrir. Verás una tira larga y transparente. Cada cuadro es un espacio para una letra."),
          ])
          + _sp("3","Pon tu fondo",[
            ("Coloca tu foto:","ve a <strong>Archivo &gt; Colocar incrustado</strong>. Haz clic en tu foto de fondo, la tuya o la de Unsplash, y luego en Colocar."),
            ("Que llene la tira:","tu foto entra con un recuadro y unos tiradores alrededor. Arrastra un tirador de la esquina hacia afuera hasta que la foto cubra toda la tira. Arrastra desde el centro para moverla."),
            ("Fíjala en su lugar:","presiona <strong>Retorno</strong> (Enter) para terminar de colocarla."),
            ("Déjala hasta abajo:","mira el panel Capas del lado derecho. Tu fondo debe quedar hasta abajo de la lista, debajo de tus letras."),
          ])
          + _sp("4","Coloca y recorta tu primera letra",[
            ("Coloca una letra:","ve otra vez a <strong>Archivo &gt; Colocar incrustado</strong>. Haz clic en tu primera foto de letra, como 1_C.jpg, y luego en Colocar."),
            ("Llévala al primer espacio:","arrastra la letra al primer espacio de la izquierda."),
            ("Ajusta su tamaño:","arrastra un tirador de la esquina para que la letra quepa en su espacio. Mantiene su forma mientras arrastras."),
            ("Fíjala en su lugar:","presiona <strong>Retorno</strong> (Enter) para terminar."),
            ("Recorta el espacio de más:","si hay foto de más al lado de tu letra, elige la herramienta <strong>Marco rectangular</strong>, arrastra un recuadro alrededor de la parte de más y presiona <strong>Suprimir</strong> (Delete). Desaparece y tu fondo se ve por detrás. Esto funciona porque tu letra es una capa normal, no un objeto inteligente."),
          ])
          + _sp("5","Coloca el resto de tus letras",[
            ("Repite con cada letra:","haz <strong>Archivo &gt; Colocar incrustado</strong> con cada letra, en orden, de izquierda a derecha, para que escriban tu nombre. Recorta cada una igual si lo necesita."),
            ("Alínealas:","mantén las letras en una fila pareja a lo largo de la tira para que tu nombre se lea claro."),
            ("¿Más letras que espacios?","si tu nombre es más largo que la plantilla, usa la plantilla 7-Up y acomoda las letras de más de forma creativa. Hazlas un poco más pequeñas o encimálas un poco, pero que el nombre se lea fácil."),
          ])
          + _sp("6","Exporta y entrégalo",[
            ("Exporta como JPG:","ve a <strong>Archivo &gt; Exportar &gt; Exportar como</strong>. Pon el formato en <strong>JPG</strong> y la calidad en alta, luego haz clic en Exportar."),
            ("Guárdalo en tu carpeta del proyecto:","nómbralo con tu nombre, como Collage_Chris.jpg, y guárdalo en tu carpeta del proyecto de Fotografía."),
            ("Súbelo a Canvas:","sube tu JPG terminado a esta tarea de Canvas."),
          ])
        )
        es+=card("CÓMO HACERLO / PASO A PASO","Coloca Tus Letras en Photoshop",
            para("Sigue estos pasos en orden. Tómate tu tiempo.")
            + teal_scroller(hint_es, parts_es))
        es+=next_up("A CONTINUACIÓN &middot; MÁS TRABAJO DE APERTURA","La caminata de esta semana: explora la apertura con los tres lentes de tu kit, el 50mm, el 18-45mm y el 55-210mm. Más detalles pronto.")

        stepnav=f'<a href="{S4}" class="silva-step-btn">&#8592; Step 04</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S4}" class="silva-bottom-btn">&#8592; Step 04</a><span></span></div>'
        return wrap_page(f"Step 5: Name Collage | Spell Your Name | {CL_EN} | PVHS", nav("Step 05",dots_for(4),stepnav), top_wrap(en,es), bottom)

    for fname,gen in [(OVER,overview),(S2,step02),(S3,step03),(S4,step04),(S5,step05)]:
        html=ent(gen())
        ban_check(html, fname)
        open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
        print("wrote", fname, len(html), "bytes")

for course in ("photo1","photo2"):
    print(f"--- {course} ---")
    build(course)
