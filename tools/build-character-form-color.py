#!/usr/bin/env python3
# Digital Arts 1A - Module 07: Character Design, Form & Color.
# Sequel to Module 06 (Line & Shape). Students REDRAW the SAME original character they invented last
# module as a NEW, clean, polished drawing, now adding the next two Elements of Art: FORM and COLOR.
# Four elements now work together: Line, Shape, Form, Color. The character must still be the student's
# own original idea, never a copy of an existing character.
# Structure (Overview numbered as Step 01, per Chris): Step 01 Overview (read + download reflection +
# lesson slides) -> Step 02 Draw & submit one clean JPG (name below) -> Step 03 Reflection (.docx).
# Text-only for now (no hero/step photos yet); gated OFF so a missing image renders nothing, never a
# placeholder box. Bilingual EN/ES, 5th-grade. Uses the shared silva_framework.
import os
from silva_framework import *

# Local ent override: map an en-dash to a plain hyphen (never &ndash;, per Chris's hard dash ban).
def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

ROOT=os.path.join(os.path.dirname(__file__),"..")
DOCS=f"{SITE}/assets/course-documents"
REFL_EN=f"{DOCS}/Character-Design-Form-Color-Reflection-EN.docx"
REFL_ES=f"{DOCS}/Character-Design-Form-Color-Reflection-ES.docx"
DECK_PDF=f"{DOCS}/DA1-Character-Design-Slides-EN-v3.pdf"   # lesson slides (English), shown on the Overview
DECK_COVER=f"{SITE}/assets/images/digarts1/character-form-color/deck-cover-v1.jpg"   # custom deck cover thumbnail
AREA="Digital Arts Folder"
MOD="07"
NXT="08"

# Images: header hero placed; step floats not supplied yet (gated OFF -> render nothing, no placeholder box).
HAVE_HEADER=True
HAVE_S1_FLOAT=False
HAVE_S2_FLOAT=False
HEADER=f"{SITE}/assets/images/digarts1/character-form-color/header-v1.jpg"
HDR_ALT_EN="A Pioneer Valley student in the design lab redrawing their original character in color, with form studies and a color wheel on the screen"
HDR_ALT_ES="Un estudiante de Pioneer Valley en el laboratorio de dise&ntilde;o volviendo a dibujar su personaje original a color, con estudios de forma y una rueda de color en la pantalla"

OVER="digarts1-character-form-color-overview.html"
S1="digarts1-character-form-color-step02-draw.html"        # Step 02 (Draw)
S2="digarts1-character-form-color-step03-reflection.html"  # Step 03 (Reflection)

ORIG_EN="Your own original character only. Redraw the same character you invented last module. It must be your own idea, not a copy of a character that already exists (no SpongeBob, no anime, game, or movie characters). Use your imagination."
ORIG_ES="Solo tu propio personaje original. Vuelve a dibujar el mismo personaje que inventaste el m&oacute;dulo pasado. Debe ser tu propia idea, no una copia de un personaje que ya existe (nada de Bob Esponja, ni personajes de anime, videojuegos o pel&iacute;culas). Usa tu imaginaci&oacute;n."

FC_STANDARDS=[
  {"code":"DGA.17.1","en_tier":"Design &amp; Graphic Arts","es_tier":"Dise&ntilde;o y Artes Gr&aacute;ficas",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You use four Elements of Art, line, shape, form, and color, on purpose in one drawing.",
   "es_desc":"Usas cuatro Elementos del Arte, l&iacute;nea, forma, volumen y color, a prop&oacute;sito en un solo dibujo."},
  {"code":"DGA.17.3","en_tier":"Design &amp; Graphic Arts","es_tier":"Dise&ntilde;o y Artes Gr&aacute;ficas",
   "en_title":"Visual Communication","es_title":"Comunicaci&oacute;n Visual",
   "en_desc":"You redraw your original character and use form and color to give it a stronger, clearer look.",
   "es_desc":"Vuelves a dibujar tu personaje original y usas la forma y el color para darle un estilo m&aacute;s fuerte y claro."},
  {"code":"DGA.17.5","en_tier":"Design &amp; Graphic Arts","es_tier":"Dise&ntilde;o y Artes Gr&aacute;ficas",
   "en_title":"Craftsmanship &amp; Production","es_title":"Elaboraci&oacute;n y Producci&oacute;n",
   "en_desc":"You take your character to a finished, polished drawing with clean lines, shading, and color.",
   "es_desc":"Llevas tu personaje a un dibujo terminado y pulido con l&iacute;neas limpias, sombreado y color."},
  {"code":"DGA.17.9","en_tier":"Design &amp; Graphic Arts","es_tier":"Dise&ntilde;o y Artes Gr&aacute;ficas",
   "en_title":"Critique &amp; Reflection","es_title":"Cr&iacute;tica y Reflexi&oacute;n",
   "en_desc":"You look at your work and plan the last Elements of Art to add: space, value, and texture.",
   "es_desc":"Revisas tu trabajo y planeas los &uacute;ltimos Elementos del Arte por agregar: espacio, valor y textura."},
]

VOCAB_EN=[
 ("Form","A shape that looks 3D, like it has depth. A circle is a flat shape; a ball is a form. You make form with shading."),
 ("Color","What you see when light bounces off something, like red, blue, or yellow, and all the colors you can mix from them."),
 ("Value","How light or dark a color is. Adding light and dark values is how you shade and build form."),
 ("Hue","Another name for a pure color, like red, blue, or green, before you make it lighter or darker."),
 ("Shading","Adding darker and lighter areas to a drawing so it looks round and 3D instead of flat."),
 ("Highlight","The brightest spot on your object, where the most light hits it."),
]
VOCAB_ES=[
 ("Forma (Volumen)","Cuando un dibujo se ve en 3D, como si tuviera profundidad. Un c&iacute;rculo es plano; una pelota tiene volumen. El volumen se crea con el sombreado."),
 ("Color","Lo que ves cuando la luz rebota en algo, como el rojo, el azul o el amarillo, y todos los colores que puedes mezclar."),
 ("Valor","Qu&eacute; tan claro u oscuro es un color. Agregar valores claros y oscuros es como sombreas y creas el volumen."),
 ("Matiz","Otra palabra para un color puro, como rojo, azul o verde, antes de aclararlo u oscurecerlo."),
 ("Sombreado","Agregar &aacute;reas m&aacute;s claras y m&aacute;s oscuras a un dibujo para que se vea redondo y en 3D, no plano."),
 ("Punto de Luz","El punto m&aacute;s brillante de tu objeto, donde le pega m&aacute;s la luz."),
]

def downloads_block(es):
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga aqu&iacute; lo que necesitas para este m&oacute;dulo. Consigue tu archivo antes de empezar." if es
          else "Download what you need for this module here. Get your file before you start.")
    reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
    ref=REFL_ES if es else REFL_EN
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ref,reflabel,row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

def module_resources(es):
    # ONE consolidated purple Resources section (LOCKED 2026-09-30): slide deck FIRST, then Key Words
    # below, in the SAME purple section. Never split resources into two purple sections spread across
    # the page. See SILVA_ANGULAR_FRAMEWORK.md.
    sub=lambda t:f'<div style="font-size:11pt;letter-spacing:0.12em;text-transform:uppercase;color:#c4b5fd;font-weight:700;margin:2px 0 12px;"><strong>{t}</strong></div>'
    div='<div style="border-top:1px solid rgba(139,92,246,0.28);margin:24px 0 20px;"></div>'
    if es:
        heading="Diapositivas y Palabras Clave"; slides_lab="Diapositivas de la Lecci&oacute;n"; keys_lab="Palabras Clave"
        intro="Mira estas diapositivas antes de dibujar. Repasan el dise&ntilde;o de personaje y los Elementos del Arte, incluyendo la Forma y el Color."
        cap="Diapositivas de la lecci&oacute;n (PDF, en ingl&eacute;s). Toca para abrir en una pesta&ntilde;a nueva."
        vg=vocab_grid("En el Examen","Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes. Apr&eacute;ndelas ahora, no la noche anterior.", VOCAB_ES)
    else:
        heading="Slides &amp; Key Words"; slides_lab="Lesson Slides"; keys_lab="Key Words"
        intro="Look through these slides before you draw. They review character design and the Elements of Art, including Form and Color."
        cap="Lesson slides (PDF). Tap to open in a new tab."
        vg=vocab_grid("On the Quiz","Heads up: these key words will show up on your quizzes. Learn them now, not the night before.", VOCAB_EN)
    deck='<div style="max-width:440px;margin:2px 0 6px;">'+slide_deck_thumb(DECK_PDF, es, thumb=DECK_COVER, cap=cap)+'</div>'
    return resources_card(heading, sub(slides_lab)+para(intro)+deck+div+sub(keys_lab)+vg, es)

# ---- nav breadcrumb + progress dots (Overview is Step 01; dots 1-2-3, no "M") ----
def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Character Design: Form &amp; Color</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

DOTS_TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03")]
def dots_for(active_idx):
    hrefs=[OVER,S1,S2]
    r=""
    for i,(lab,title) in enumerate(DOTS_TITLES):
        r+=dot("" if i==active_idx else hrefs[i], lab, title, i==active_idx, module=False)
    return r

# ================= STEP 01 = OVERVIEW =================
def overview():
    en=banner("Digital Arts 1A",f"Module {MOD}: Character Design, Form &amp; Color","Redraw your character and bring it to life with Form and Color.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
    en+=type_card("overview","Step 01 &middot; Overview &amp; Download","Redraw Your Character with Form &amp; Color",
        para("Last module you designed your very own original character using the first two Elements of Art: <strong>Line</strong> and <strong>Shape</strong>. Now bring it to life. In this module you redraw that <strong>same</strong> character as a new, clean, polished drawing and add the next two Elements of Art: <strong>Form</strong> and <strong>Color</strong>. Four elements now work together: Line, Shape, Form, and Color.")
        + (framed(HEADER,HDR_ALT_EN) if HAVE_HEADER else "")
        + para("You are on Step 01 now: read this page and download your reflection document below.")
        + note_orange(ORIG_EN))
    en+=standards_box(False, FC_STANDARDS)
    en+=downloads_block(False)
    en+=card("THE NEXT 2 ELEMENTS","Meet Form &amp; Color",
        para("Form and Color are what turn a flat outline into a character that looks alive. Add them on purpose.")
        + bullets([
            ("Form:","form is a shape that looks 3D. A circle is a flat shape; a ball is a form. You make form with shading, adding light and dark values so your character looks round, not flat."),
            ("Color:","color brings your character to life. Pick colors on purpose and think about where each one goes and why."),
            ("Value:","value is how light or dark a color is. Light and dark values are how you shade and build form."),
            ("Four elements now:","keep your clean lines and strong shapes from last time, then add form and color on top."),
        ]))
    en+=card("YOUR CHALLENGE","Redraw the Same Character, Add Form &amp; Color",
        para("Make a new, clean, polished drawing of your same original character. Keep your line and shape, then add form with shading and add color. When you are done it should use all four Elements of Art we have covered: Line, Shape, Form, and Color.")
        + bullets([
            ("Same character:","redraw the original character you invented last module, now improved."),
            ("Add Form:","shade with light and dark values so your character looks 3D, not flat."),
            ("Add Color:","choose your colors on purpose and color it in cleanly."),
            ("All four elements:","line, shape, form, and color, working together."),
            ("Name it:","write your character&rsquo;s name below the drawing."),
        ]))
    en+=module_resources(False)
    en+=card("HOW THIS MODULE WORKS","The Steps",
        para("You are on Step 01 now: read this page and download your file. Here are the steps that follow.")
        + bullets([
            ("Step 02 &middot; Draw &amp; Submit:","redraw your character with form and color, then turn in one clean picture (JPG) with its name below."),
            ("Step 03 &middot; Reflection:","tell what you added and why, and what you would add next."),
        ]))
    en+=next_up("UP NEXT &middot; STEP 02 - Draw Your Character","Open your character and redraw it with form and color. Make it clean and polished.")

    es=banner("Arte Digital 1A",f"M&oacute;dulo {MOD}: Dise&ntilde;o de Personaje, Forma y Color","Vuelve a dibujar tu personaje y dale vida con la Forma y el Color.","#top","Back to English", HICON_DESIGN)
    es+=type_card("overview","Paso 01 &middot; Resumen y Descarga","Vuelve a Dibujar Tu Personaje con Forma y Color",
        para("El m&oacute;dulo pasado dise&ntilde;aste tu propio personaje original usando los primeros dos Elementos del Arte: la <strong>L&iacute;nea</strong> y la <strong>Forma</strong>. Ahora dale vida. En este m&oacute;dulo vuelves a dibujar ese <strong>mismo</strong> personaje como un dibujo nuevo, limpio y pulido, y agregas los siguientes dos Elementos del Arte: la <strong>Forma (volumen)</strong> y el <strong>Color</strong>. Ahora trabajan cuatro elementos juntos: L&iacute;nea, Forma, Volumen y Color.")
        + (framed(HEADER,HDR_ALT_ES) if HAVE_HEADER else "")
        + para("Est&aacute;s en el Paso 01: lee esta p&aacute;gina y descarga tu documento de reflexi&oacute;n abajo.")
        + note_orange(ORIG_ES))
    es+=standards_box(True, FC_STANDARDS)
    es+=downloads_block(True)
    es+=card("LOS SIGUIENTES 2 ELEMENTOS","Conoce la Forma y el Color",
        para("La forma (el volumen) y el color son lo que convierte un contorno plano en un personaje que se ve vivo. Agr&eacute;galos a prop&oacute;sito.")
        + bullets([
            ("Volumen:","el volumen es cuando una forma se ve en 3D. Un c&iacute;rculo es plano; una pelota tiene volumen. El volumen se crea con el sombreado, agregando valores claros y oscuros para que tu personaje se vea redondo, no plano."),
            ("Color:","el color le da vida a tu personaje. Elige los colores a prop&oacute;sito y piensa d&oacute;nde va cada uno y por qu&eacute;."),
            ("Valor:","el valor es qu&eacute; tan claro u oscuro es un color. Los valores claros y oscuros son la forma de sombrear y crear el volumen."),
            ("Ahora cuatro elementos:","conserva tus l&iacute;neas limpias y tus formas fuertes del m&oacute;dulo pasado, y luego agrega la forma y el color encima."),
        ]))
    es+=card("TU RETO","Vuelve a Dibujar el Mismo Personaje, Agrega Forma y Color",
        para("Haz un dibujo nuevo, limpio y pulido de tu mismo personaje original. Conserva tu l&iacute;nea y tu forma, y luego agrega volumen con sombreado y agrega color. Cuando termines, debe usar los cuatro Elementos del Arte que hemos visto: L&iacute;nea, Forma, Volumen y Color.")
        + bullets([
            ("El mismo personaje:","vuelve a dibujar el personaje original que inventaste el m&oacute;dulo pasado, ahora mejorado."),
            ("Agrega Volumen:","sombrea con valores claros y oscuros para que tu personaje se vea en 3D, no plano."),
            ("Agrega Color:","elige tus colores a prop&oacute;sito y col&oacute;realo con limpieza."),
            ("Los cuatro elementos:","l&iacute;nea, forma, volumen y color, trabajando juntos."),
            ("Ponle nombre:","escribe el nombre de tu personaje debajo del dibujo."),
        ]))
    es+=module_resources(True)
    es+=card("C&Oacute;MO FUNCIONA ESTE M&Oacute;DULO","Los Pasos",
        para("Est&aacute;s en el Paso 01: lee esta p&aacute;gina y descarga tu archivo. Estos son los pasos que siguen.")
        + bullets([
            ("Paso 02 &middot; Dibuja y Entrega:","vuelve a dibujar tu personaje con forma y color, y entrega una foto limpia (JPG) con su nombre debajo."),
            ("Paso 03 &middot; Reflexi&oacute;n:","cuenta qu&eacute; agregaste y por qu&eacute;, y qu&eacute; agregar&iacute;as despu&eacute;s."),
        ]))
    es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 02 - Dibuja Tu Personaje","Abre tu personaje y vu&eacute;lvelo a dibujar con forma y color. Que quede limpio y pulido.")

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
    return wrap_page("Character Design, Form & Color | Digital Arts 1A | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ================= STEP 02 = DRAW =================
def step01():
    en=banner(f"Module {MOD} &bull; Step 02","Draw Your Character","Redraw it with form and color, clean and polished.","#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
    en+=card("STEP 02 / DRAW","Redraw Your Character with Form &amp; Color",
        para("Start from your original character. Redraw it as a new, clean drawing on your iPad. First lay down your clean lines and shapes, just like last module. Then add the two new elements: use shading (light and dark values) to give it Form so it looks 3D, and add Color on purpose.")
        + para("Take your time and make it polished. When you are done, your drawing should clearly use all four Elements of Art we have covered: Line, Shape, Form, and Color. Write your character&rsquo;s name below the drawing.")
        + bullets([
            ("Same character:","redraw the original character you made last module, now improved."),
            ("Add Form:","shade with light and dark values so it looks round and 3D, not flat."),
            ("Add Color:","choose your colors on purpose and color it in cleanly."),
            ("All four elements:","line, shape, form, and color, working together."),
            ("Name below:","write your character&rsquo;s name under the drawing."),
        ])
        + note_orange(ORIG_EN))
    en+=deliverables_box(False,
        [("1 picture (JPG),","a clear picture of your finished, colored character with its name written below, uploaded to this Canvas assignment.")])
    en+=card("TURN IT IN","Save and Upload Your Character",
        para("When your character is finished, colored, and named, save it as a JPG (or take a clean, clear photo of it with your iPad). Make sure the whole drawing and the name show, with good light and no glare. Upload the JPG to this Canvas assignment. Then go to Step 03 for the reflection.")
        + note("Be honest and turn in your own original work."))
    en+=next_up("UP NEXT &middot; STEP 03 - Reflection","With your character turned in, you&rsquo;ll reflect on the form and color choices you made.")

    es=banner(f"M&oacute;dulo {MOD} &bull; Paso 02","Dibuja Tu Personaje","Vu&eacute;lvelo a dibujar con forma y color, limpio y pulido.","#top","Back to English", HICON_DESIGN)
    es+=card("PASO 02 / DIBUJA","Vuelve a Dibujar Tu Personaje con Forma y Color",
        para("Empieza con tu personaje original. Vu&eacute;lvelo a dibujar como un dibujo nuevo y limpio en tu iPad. Primero pon tus l&iacute;neas y formas limpias, igual que el m&oacute;dulo pasado. Luego agrega los dos elementos nuevos: usa el sombreado (valores claros y oscuros) para darle Volumen y que se vea en 3D, y agrega Color a prop&oacute;sito.")
        + para("T&oacute;mate tu tiempo y que quede pulido. Cuando termines, tu dibujo debe usar claramente los cuatro Elementos del Arte que hemos visto: L&iacute;nea, Forma, Volumen y Color. Escribe el nombre de tu personaje debajo del dibujo.")
        + bullets([
            ("El mismo personaje:","vuelve a dibujar el personaje original que hiciste el m&oacute;dulo pasado, ahora mejorado."),
            ("Agrega Volumen:","sombrea con valores claros y oscuros para que se vea redondo y en 3D, no plano."),
            ("Agrega Color:","elige tus colores a prop&oacute;sito y col&oacute;realo con limpieza."),
            ("Los cuatro elementos:","l&iacute;nea, forma, volumen y color, trabajando juntos."),
            ("Nombre debajo:","escribe el nombre de tu personaje debajo del dibujo."),
        ])
        + note_orange(ORIG_ES))
    es+=deliverables_box(True,
        [("1 foto (JPG),","una foto clara de tu personaje terminado y con color, con su nombre escrito debajo, subida a esta tarea de Canvas.")])
    es+=card("ENTR&Eacute;GALO","Guarda y Sube Tu Personaje",
        para("Cuando tu personaje est&eacute; terminado, con color y con nombre, gu&aacute;rdalo como JPG (o toma una foto limpia y clara con tu iPad). Aseg&uacute;rate de que se vea todo el dibujo y el nombre, con buena luz y sin reflejo. Sube el JPG a esta tarea de Canvas. Luego ve al Paso 03 para la reflexi&oacute;n.")
        + note("S&eacute; honesto y entrega tu propio trabajo original."))
    es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 03 - Reflexi&oacute;n","Con tu personaje entregado, vas a reflexionar sobre las decisiones de forma y color que tomaste.")

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S2}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S2}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Draw Your Character | Character Design, Form & Color | Digital Arts 1A | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

# ================= STEP 03 = REFLECTION =================
def step02():
    en=banner(f"Module {MOD} &bull; Step 03","Reflection","What did you add, and what comes next?","#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
    en+=card("STEP 03 / REFLECTION","Reflect on Your Form &amp; Color",
        para("Your character now has form and color. In a short reflection, think about the choices you made: where you added form and how you shaded it, what colors you chose and why, and how this new version is stronger than your first line-and-shape drawing. Then look ahead to the last Elements of Art: space, value, and texture.")
        + note("The reflection document is on Step 01 (the Overview), the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + para("Type your answers in the document, save it, and upload it to this Canvas assignment."))
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
    en+=next_up(f"UP NEXT &middot; MODULE {NXT} - The Last Elements","Next module you keep building your character toward all 7 Elements of Art, adding space, value, and texture.")

    es=banner(f"M&oacute;dulo {MOD} &bull; Paso 03","Reflexi&oacute;n","&iquest;Qu&eacute; agregaste y qu&eacute; sigue?","#top","Back to English", HICON_REFLECT)
    es+=card("PASO 03 / REFLEXI&Oacute;N","Reflexiona Sobre Tu Forma y Color",
        para("Tu personaje ya tiene forma y color. En una reflexi&oacute;n corta, piensa en las decisiones que tomaste: d&oacute;nde agregaste volumen y c&oacute;mo lo sombreaste, qu&eacute; colores elegiste y por qu&eacute;, y c&oacute;mo esta nueva versi&oacute;n es m&aacute;s fuerte que tu primer dibujo de l&iacute;neas y formas. Luego mira hacia los &uacute;ltimos Elementos del Arte: el espacio, el valor y la textura.")
        + note("El documento de reflexi&oacute;n est&aacute; en el Paso 01 (el Resumen), la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + para("Escribe tus respuestas en el documento, gu&aacute;rdalo y s&uacute;belo a esta tarea de Canvas."))
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word de reflexi&oacute;n completo (.docx), subido a esta tarea de Canvas.")])
    es+=next_up(f"A CONTINUACI&Oacute;N &middot; M&Oacute;DULO {NXT} - Los &Uacute;ltimos Elementos","El pr&oacute;ximo m&oacute;dulo sigues construyendo tu personaje hacia los 7 Elementos del Arte, agregando el espacio, el valor y la textura.")

    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page("Reflection | Character Design, Form & Color | Digital Arts 1A | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
