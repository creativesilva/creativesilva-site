#!/usr/bin/env python3
# Design a Sticker (display name; URL slug stays make-your-mark): DA1A module (Module 09), full color-coding kept
# (teal = learn, purple = watch/look, orange = download, gold = turn in, green = standards).
# Direction (Chris, 2026-11-04): this is an Adobe Illustrator project where students DRAW their own
# letters from scratch (no fonts) and turn a word into a STICKER. A vinyl sticker has a white border
# so it reads on ANY color (a dark car window OR a white car trunk): that IS the "works on light or
# dark" lesson, made physical. Examples are Chris's own real sticker photos (his taste, not AI art):
# a short written list gives style ideas to DRAW. Overview = Step 01. Mr. Silva, never "your teacher".
import os
from silva_framework import *

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Digital Arts Folder"
CT="Digital Arts 1A"; PFX="digarts1"
IMGDIR=f"{SITE}/assets/images/digarts1/make-your-mark"
HERO_SCRIPT=f"{IMGDIR}/example-script-sticker-v1.jpg"  # "Your Text" brush-script sticker on grass -> idea hero
EX_LOVE=f"{IMGDIR}/example-love-sticker-v1.jpg"         # LOVE bubble/pattern sticker -> Watch & look
HAVE_ART=True

# style ideas students can DRAW (no fonts): (EN name, ES name, EN desc, ES desc)
STYLE_IDEAS=[
  ("Bubble","Burbuja","fat, round letters.","letras gordas y redondas."),
  ("Script","Pincel","flowing, like fancy handwriting.","fluida, como letra elegante."),
  ("Block / 3D","Bloque / 3D","thick letters with a shadow.","letras gruesas con sombra."),
  ("Outline","Contorno","just the outline of each letter.","solo el borde de cada letra."),
  ("Patterns","Patrones","fill each letter with plaid, dots, or hearts.","llena cada letra con cuadros, puntos o corazones."),
]

# Downloadable asset files carry the DISPLAY name (Design-A-Sticker), not the make-your-mark URL slug,
# so a file Chris/students download is not named with the old module title (Chris 2026-11-04).
REFL_EN=f"{SITE}/assets/course-documents/Design-A-Sticker-Reflection-EN.docx"
REFL_ES=f"{SITE}/assets/course-documents/Design-A-Sticker-Reflection-ES.docx"
# ONE project-folder zip: extracts to a Design_A_Sticker/ folder holding the Design_A_Sticker.ai
# starter file + both reflection docx. Students download this and open the .ai.
PROJECT_ZIP=f"{SITE}/assets/course-documents/Design-A-Sticker-Project-Folder.zip"
HAVE_REFL=True

OVER=f"{PFX}-make-your-mark-overview.html"
S1=f"{PFX}-make-your-mark-step01-make-your-word.html"
S2=f"{PFX}-make-your-mark-step02-reflection.html"

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

MYM_STANDARDS=[
  {"code":"SA.11.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Elements &amp; Principles","es_title":"Elementos y Principios",
   "en_desc":"You use line, shape, and repetition to draw letters that share one clear style.",
   "es_desc":"Usas la l&iacute;nea, la forma y la repetici&oacute;n para dibujar letras que comparten un mismo estilo claro."},
  {"code":"SA.11.2","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Unity &amp; Consistency","es_title":"Unidad y Consistencia",
   "en_desc":"You keep the same stroke weight and style across every letter, so your word reads as one family.",
   "es_desc":"Mantienes el mismo grosor y estilo en cada letra, para que tu palabra se vea como una sola familia."},
  {"code":"MA.11.4","en_tier":"Media Arts","es_tier":"Artes de Medios",
   "en_title":"Digital Tools","es_title":"Herramientas Digitales",
   "en_desc":"You use Adobe Illustrator to draw original letters and export your sticker as an image.",
   "es_desc":"Usas Adobe Illustrator para dibujar letras originales y exportar tu sticker como una imagen."},
  {"code":"MA.11.6","en_tier":"Media Arts","es_tier":"Artes de Medios",
   "en_title":"Communicate a Message","es_title":"Comunicar un Mensaje",
   "en_desc":"You pick a style on purpose so your sticker shows a feeling or a vibe.",
   "es_desc":"Eliges un estilo a prop&oacute;sito para que tu sticker muestre un sentimiento o una vibra."},
]

# ---------- visual components (Canvas-safe: inline styles + images, flex not grid) ----------
def float_purple(src, alt, cap=""):
    # purple-framed FLOAT content photo, for the purple Watch & look card (keeps the accent cohesive;
    # float_right is teal and belongs in teal cards). Same FLOAT markers so the card hoists it right.
    capdiv=(f'<div style="font-size:10.5pt;color:#c4b5fd;text-align:center;margin-top:6px;opacity:0.9;line-height:1.4;">{cap}</div>' if cap else '')
    return ('<!--FLOAT-->'
      f'<div style="background:linear-gradient(135deg,#8b5cf6 0%,rgba(139,92,246,0.08) 100%);padding:2px;"><img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      + capdiv + '<!--/FLOAT-->')

def style_ideas(es):
    cards=""
    for en_n,es_n,en_d,es_d in STYLE_IDEAS:
        n=es_n if es else en_n; d=es_d if es else en_d
        cards+=(f'<div style="flex:1 1 30%;min-width:170px;max-width:calc(33.333% - 8px);background:#0a1414;'
                f'border:1px solid rgba(255,255,255,0.08);border-top:2px solid #00b8b8;padding:14px 14px 13px;box-sizing:border-box;">'
                f'<div style="font-size:12.5pt;font-weight:700;letter-spacing:0.03em;text-transform:uppercase;color:#eafeff;">{n}</div>'
                f'<div style="font-size:12.5pt;color:#9fc3c3;margin-top:4px;line-height:1.45;">{d}</div></div>')
    return f'<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:4px;">{cards}</div>'

def scroll_steps(inner, rgb="0,184,184"):
    # locked contained scroller, so a long how-to never looks like a tall intimidating stack.
    # rgb sets the accent (teal content default; "139,92,246" for a purple Resources scroller).
    return (f'<div class="silva-scroll" style="max-height:440px;overflow-y:auto;padding:14px 16px 20px;'
            f'border:1px solid rgba({rgb},0.30);background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, '
            f'rgba(0,0,0,0.14) 88%, rgba({rgb},0.14) 100%);">' + inner + '</div>')

def subhead(t, color="#c4b5fd"):
    return f'<div style="font-size:12.5pt;font-weight:700;color:{color};letter-spacing:0.04em;margin:12px 0 8px;">{t}</div>'

def draw_resource(es):
    # Purple Resources deep-dive: HOW to draw a letter from scratch (Pen tool, closing shapes,
    # Pathfinder/Shape Builder) + best-practice tips, in a contained purple scroller. Steps verified
    # against Adobe docs. This is the "you design the letterforms, not pick a font" detail.
    P="#8b5cf6"; rgb="139,92,246"
    if es:
        intro=para("Aqu&iacute; dibujas cada letra t&uacute; mismo. Hay dos maneras de armar una letra. Elige la que te sea m&aacute;s f&aacute;cil. El Sr. Silva te ense&ntilde;ar&aacute; las dos.")
        inner=(subhead("Manera 1: Con formas (m&aacute;s f&aacute;cil)")
            + steps([
                ("Dibuja formas simples que se encimen para armar tu letra.","Rect&aacute;ngulos para las partes rectas, c&iacute;rculos para las partes redondas."),
                ("Selecciona las formas y &uacute;nelas.","Presiona Shift+M (Creador de formas) y arrastra sobre las partes para unirlas en una sola forma. Mant&eacute;n Option y haz clic para quitar una parte."),
                ("O usa Pathfinder.","Abre Ventana &rarr; Buscatrazos, luego haz clic en Unir para fusionar las formas en una."),
            ], accent=P)
            + subhead("Manera 2: Con la herramienta Pluma")
            + steps([
                ("Presiona P para la Pluma.","Haz clic para una esquina. Haz clic y arrastra para una curva."),
                ("Sigue el contorno de tu letra.","Haz clic alrededor de toda la letra."),
                ("Cierra la forma.","Regresa a tu primer punto hasta que aparezca un c&iacute;rculo peque&ntilde;o, y haz clic. Ya es una forma cerrada que puedes rellenar con color."),
            ], accent=P)
            + subhead("Consejos")
            + bullets([
                ("Cierra cada forma","una forma abierta no se rellena bien con color."),
                ("Mismo grosor","que cada letra tenga el mismo grosor para que combinen."),
                ("Pocos puntos","usa pocos puntos para curvas m&aacute;s limpias."),
                ("L&iacute;neas rectas","mant&eacute;n Shift al hacer clic para l&iacute;neas rectas y parejas."),
                ("Trabaja en grande","acerca el zoom (presiona Z) y trabaja grande."),
                ("Punto redondo a esquina","usa la herramienta V&eacute;rtice (Shift+C) para volver un punto redondo en una esquina."),
            ], accent=P))
        return resources_card("C&oacute;mo Dibujar Tus Letras", intro+scroll_steps(inner,rgb), es=True)
    intro=para("Here you draw every letter yourself. There are two ways to build a letter. Pick the one that feels easier. Mr. Silva will show you both.")
    inner=(subhead("Way 1: Build from shapes (easier)")
        + steps([
            ("Draw simple shapes that overlap to make your letter.","Rectangles for the straight parts, circles for the round parts."),
            ("Select the shapes and join them.","Press Shift+M for the Shape Builder tool and drag across the parts to join them into one shape. Hold Option and click to cut a part away."),
            ("Or use Pathfinder.","Open Window &rarr; Pathfinder, then click Unite to fuse the shapes into one."),
        ], accent=P)
        + subhead("Way 2: Draw with the Pen tool")
        + steps([
            ("Press P for the Pen tool.","Click to make a corner. Click and drag to make a curve."),
            ("Trace the outline of your letter.","Keep clicking around the whole letter."),
            ("Close the shape.","Go back to your first point until a small circle shows, then click. Now it is a closed shape you can fill with color."),
        ], accent=P)
        + subhead("Tips")
        + bullets([
            ("Close every shape","an open shape will not fill with solid color."),
            ("Same thickness","keep every letter the same thickness so they match."),
            ("Few points","use only a few points for smooth, clean curves."),
            ("Straight lines","hold Shift while you click for straight, even lines."),
            ("Work big","zoom in (press Z) and work large."),
            ("Round point to corner","use the Anchor Point tool (Shift+C) to turn a round point into a sharp corner."),
        ], accent=P))
    return resources_card("How to Draw Your Letters", intro+scroll_steps(inner,rgb), es=False)

def vocab3(es):
    if es:
        n1,s1=("Mismo grosor","No delgada aqu&iacute;, gruesa all&aacute;.")
        n2,s2=("Misma l&iacute;nea","Todas sobre una l&iacute;nea.")
        n3,s3=("Se parecen","Se ven como una familia.")
    else:
        n1,s1=("Same thickness","Not thin here, fat there.")
        n2,s2=("Same line","All on one line.")
        n3,s3=("They match","Looks like a family.")
    def vc(pic,name,sub):
        return (f'<div style="flex:1 1 180px;min-width:160px;background:#0a1414;border:1px solid rgba(255,255,255,0.08);'
                f'padding:16px 12px 14px;text-align:center;box-sizing:border-box;">'
                f'<div style="height:72px;display:flex;align-items:center;justify-content:center;gap:8px;margin-bottom:8px;">{pic}</div>'
                f'<div style="font-size:11pt;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#5ff0f0;">{name}</div>'
                f'<div style="font-size:11.5pt;color:#8fb6b6;margin-top:3px;">{sub}</div></div>')
    pic1=('<span style="font-family:Arial,sans-serif;font-size:40pt;font-weight:400;color:#6f9a9a;line-height:1;">A</span>'
          '<span style="font-family:Arial,sans-serif;font-size:44pt;font-weight:900;color:#eafeff;line-height:1;">A</span>')
    pic2=('<span style="font-family:Arial,sans-serif;font-size:30pt;font-weight:800;color:#eafeff;line-height:1;'
          'border-bottom:3px solid #00b8b8;padding-bottom:2px;">a b c</span>')
    pic3=('<span style="font-family:Arial,sans-serif;font-size:34pt;font-weight:900;color:#00b8b8;line-height:1;letter-spacing:2px;">A B C</span>')
    return (f'<div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:4px;">{vc(pic1,n1,s1)}{vc(pic2,n2,s2)}{vc(pic3,n3,s3)}</div>')

def downloads(es):
    if es:
        heading="Descarga Tu Carpeta del Proyecto"
        lead="Descarga la carpeta del proyecto. Adentro viene el archivo de Illustrator para empezar y tus dos hojas de reflexi&oacute;n."
        lab="Carpeta del Proyecto (ZIP)"
        note_t=("<strong style=\"color:#ffb27c;\">&Uacute;sala:</strong> abre el archivo <strong>Design_A_Sticker.ai</strong> que viene adentro para empezar tu sticker. "
                f"Gu&aacute;rdala en OneDrive &rarr; {AREA} para que no se te pierda.")
    else:
        heading="Download Your Project Folder"
        lead="Download the project folder. Inside you get the Illustrator file to start, plus both reflection sheets."
        lab="Project Folder (ZIP)"
        note_t=("<strong style=\"color:#ffb27c;\">Use it:</strong> open the <strong>Design_A_Sticker.ai</strong> file inside to start your sticker. "
                f"Save the folder in OneDrive &rarr; {AREA} so you do not lose it.")
    rows=('<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
          + dl_link(PROJECT_ZIP, lab, row=True)
          + '</div>')
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
          + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
          + para(lead) + rows
          + f'<div style="margin-top:16px;font-size:12pt;color:rgba(255,255,255,0.82);line-height:1.55;">{note_t}</div>'
          + '</div>')

# ---------- nav ----------
def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Design a Sticker</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')
DT=[("1","Step 01"),("2","Step 02"),("3","Step 03")]
def dots_for(active):
    hrefs=[OVER,S1,S2]; r=""
    for i,(lab,title) in enumerate(DT):
        r+=dot("" if i==active else hrefs[i], lab, title, i==active, module=False)
    return r

# ================= PAGES =================
def overview():
    # ---- EN ----
    en=banner("Module 09 &bull; Step 01","Design a Sticker: Start Here",
        "Read this page, then go to Step 02 to make your sticker.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=card("Learn &middot; the idea","Turn a Word Into a Sticker",
        (float_right(HERO_SCRIPT,"A brush-script vinyl sticker with a white border, held over grass","Your word can become a sticker like this.") if HAVE_ART else "")
        + para("This is an <strong>Adobe Illustrator</strong> project. You will <strong>draw your own letters</strong> and turn a word into a <strong>sticker</strong>.")
        + para("Your sticker will be printed on a big <strong>wide format sticker printer</strong>, so this project uses print colors (<strong>CMYK</strong>). The file is already set up that way.")
        + para("You are <strong>not</strong> picking a font. You design every letter yourself, from scratch, like a type designer who builds a whole font face.")
        + para("Pick a word you like: your name, a nickname, or any short word. Give every letter the same style, so your word looks like one set.")
        + note("<strong>School appropriate only.</strong> Your word must be clean and okay for school. No bad words, and nothing mean."))
    en+=resources_card("Watch &amp; look",
        (float_purple(EX_LOVE,"A LOVE sticker: each letter drawn in one style with a pattern, a black outline, and a white border","One style on every letter, with a white sticker border.") if HAVE_ART else "")
        + para("Here are real stickers. Look how every letter is drawn in <strong>one style</strong>, with a black outline. The <strong>white border</strong> around the word makes the sticker pop on any color.")
        + para("<strong>Watch:</strong> Mr. Silva will show you a quick demo before you start."),es=False)
    en+=card("Learn &middot; 3 things that make it work","Check These Three",
        vocab3(False)
        + para("If you added one more letter, would it fit right in? If yes, your word is a family."))
    en+=card("Learn &middot; the sticker trick","Make It Work Anywhere",
        para("A sticker needs a <strong>white border</strong> around it. That border makes your word pop on <strong>any</strong> color: a dark window or a white car.")
        + para("You will add a white border in Step 02. You will check for it before you turn it in."))
    en+=downloads(False)
    en+=card("How It Works / Your Plan","Your Next 2 Steps",
        para("You are on Step 01 now: read this page and download your project folder. Here are the two steps that follow.")
        + bullets([
            ("Step 02 &middot; Make Your Word:","pick a style, draw your letters, and add the white sticker border."),
            ("Step 03 &middot; Reflection:","fill in a short sheet about your sticker."),
        ]))
    en+=standards_box(False, MYM_STANDARDS)
    en+=next_up("UP NEXT &middot; STEP 02 - Make Your Word","Pick a style, draw a word you like, and turn it into a sticker.")
    # ---- ES ----
    es=banner("M&oacute;dulo 09 &bull; Paso 01","Dise&ntilde;a un Sticker: Empieza Aqu&iacute;",
        "Lee esta p&aacute;gina y luego ve al Paso 02 para hacer tu sticker.","#top","Back to English",hicon=HICON_DESIGN)
    es+=card("Aprende &middot; la idea","Convierte una Palabra en un Sticker",
        (float_right(HERO_SCRIPT,"Un sticker de letra de pincel con borde blanco, sobre el pasto","Tu palabra puede volverse un sticker as&iacute;.") if HAVE_ART else "")
        + para("Este es un proyecto de <strong>Adobe Illustrator</strong>. Vas a <strong>dibujar tus propias letras</strong> y convertir una palabra en un <strong>sticker</strong>.")
        + para("Tu sticker se imprimir&aacute; en una <strong>impresora grande de stickers</strong>, por eso este proyecto usa colores de impresi&oacute;n (<strong>CMYK</strong>). El archivo ya est&aacute; listo as&iacute;.")
        + para("<strong>No</strong> est&aacute;s eligiendo una fuente. T&uacute; dise&ntilde;as cada letra, desde cero, como un dise&ntilde;ador que crea una fuente completa.")
        + para("Elige una palabra que te guste: tu nombre, un apodo o cualquier palabra corta. Dale a cada letra el mismo estilo, para que tu palabra se vea como un solo conjunto.")
        + note("<strong>Solo palabras apropiadas para la escuela.</strong> Tu palabra debe ser limpia y adecuada para la clase. Nada de groser&iacute;as, y nada ofensivo."))
    es+=resources_card("Mira y observa",
        (float_purple(EX_LOVE,"Un sticker de LOVE: cada letra dibujada en un estilo con un patr&oacute;n, un borde negro y un borde blanco","Un estilo en cada letra, con un borde blanco de sticker.") if HAVE_ART else "")
        + para("Aqu&iacute; hay stickers reales. Mira c&oacute;mo cada letra est&aacute; dibujada en <strong>un estilo</strong>, con un borde negro. El <strong>borde blanco</strong> alrededor de la palabra hace que el sticker resalte en cualquier color.")
        + para("<strong>Mira:</strong> el Sr. Silva te ense&ntilde;ar&aacute; una demostraci&oacute;n corta antes de empezar."),es=True)
    es+=card("Aprende &middot; 3 cosas que lo hacen funcionar","Revisa Estas Tres",
        vocab3(True)
        + para("Si agregaras una letra m&aacute;s, &iquest;combinar&iacute;a bien? Si s&iacute;, tu palabra es una familia."))
    es+=card("Aprende &middot; el truco del sticker","Haz Que Funcione en Todos Lados",
        para("Un sticker necesita un <strong>borde blanco</strong> alrededor. Ese borde hace que tu palabra resalte en <strong>cualquier</strong> color: una ventana oscura o un carro blanco.")
        + para("Agregar&aacute;s un borde blanco en el Paso 02. Lo revisar&aacute;s antes de entregar."))
    es+=downloads(True)
    es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Siguientes 2 Pasos",
        para("Est&aacute;s en el Paso 01 ahora: lee esta p&aacute;gina y descarga tu carpeta del proyecto. Aqu&iacute; est&aacute;n los dos pasos que siguen.")
        + bullets([
            ("Paso 02 &middot; Haz Tu Palabra:","elige un estilo, dibuja tus letras y agrega el borde blanco del sticker."),
            ("Paso 03 &middot; Reflexi&oacute;n:","llena una hoja corta sobre tu sticker."),
        ]))
    es+=standards_box(True, MYM_STANDARDS)
    es+=next_up("SIGUIENTE &middot; PASO 02 - Haz Tu Palabra","Elige un estilo, dibuja una palabra que te guste y convi&eacute;rtela en un sticker.")
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
    return wrap_page(f"Design a Sticker | {CT} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

def make_word():
    # ---- EN ----
    en=banner("Module 09 &bull; Step 02","Make Your Word",
        "Draw your letters and turn your word into a sticker.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=card("Learn &middot; pick your style","Pick a Style to Draw",
        note("You are <strong>designing</strong> the letters yourself. You are NOT choosing a font. Every letter is drawn by you, from scratch.")
        + para("Pick <strong>ONE</strong> style and draw every letter the same way. Keep your word <strong>school appropriate</strong>.")
        + (style_ideas(False) if HAVE_ART else "")
        + para("Your sticker should look good on a <strong>light</strong> and a <strong>dark</strong> background. The white border is what makes that happen."))
    en+=card("Learn &middot; make it","Make It in Adobe Illustrator",
        scroll_steps(steps([
            ("Open Adobe Illustrator.","Find it in the Dock or in Launchpad."),
            ("Open the provided file.","In your project folder (from Step 01), open <strong>Design_A_Sticker.ai</strong>. It is already set up for you: the right size, and <strong>CMYK</strong> colors for the sticker printer. Do not change the color mode."),
            ("Sketch your word first.","On paper or your student iPad, draw your word in big letters. Take a photo with your iPad and bring it into Illustrator to trace."),
            ("Draw your letters.","Trace your sketch with the <strong>Pencil</strong> or <strong>Pen</strong> tool. No fonts. Use your one style on every letter, the same thickness."),
            ("Color and outline.","Fill every letter the same way (one color or a pattern). Give every letter the same <strong>black outline</strong>."),
            ("Add the white sticker border.","Put a thick <strong>white border</strong> around the whole word so it looks like a real sticker and pops on any color. Mr. Silva will show you how."),
            ("Save your Illustrator file.","Click <strong>File &rarr; Save</strong> to keep your <strong>.ai</strong> file. You do NOT turn in the .ai file."),
            ("Save a vector PDF.","Click <strong>File &rarr; Save As</strong> and pick <strong>Adobe PDF</strong>. Choose the <strong>[Press Quality]</strong> preset, then click <strong>Save PDF</strong>. It stays sharp vector art in CMYK. This PDF is what you turn in."),
        ], accent="#00b8b8"))
        + note("On the Mac, press <strong>Cmd</strong> (not Ctrl). Ask Mr. Silva if you get stuck."))
    en+=draw_resource(False)
    en+=card("Learn &middot; check yourself","Before You Turn It In",
        para("Look at your sticker. Can you check all five?")
        + bullets([
            ("Same thickness","every letter is the same weight."),
            ("Same style","every letter is drawn the same way."),
            ("Same line","all letters sit on one line."),
            ("White sticker border","it pops on a light background and a dark one."),
            ("Would a new letter fit in?","if yes, your word is a family."),
        ]))
    en+=deliverables_box(False,
        [("1 vector PDF:","your finished <strong>sticker</strong>, saved as a <strong>vector PDF</strong> (File &rarr; Save As &rarr; Adobe PDF &rarr; [Press Quality]), uploaded to this Canvas assignment. <strong>Not</strong> the .ai file, and not a JPG.")])
    en+=next_up("UP NEXT &middot; STEP 03 - Reflection","Tell about your sticker: your style, and the hardest part.")
    # ---- ES ----
    es=banner("M&oacute;dulo 09 &bull; Paso 02","Haz Tu Palabra",
        "Dibuja tus letras y convierte tu palabra en un sticker.","#top","Back to English",hicon=HICON_DESIGN)
    es+=card("Aprende &middot; elige tu estilo","Elige un Estilo para Dibujar",
        note("T&uacute; <strong>dise&ntilde;as</strong> las letras. NO est&aacute;s eligiendo una fuente. Cada letra la dibujas t&uacute;, desde cero.")
        + para("Elige <strong>UN</strong> estilo y dibuja cada letra de la misma manera. Mant&eacute;n tu palabra <strong>apropiada para la escuela</strong>.")
        + (style_ideas(True) if HAVE_ART else "")
        + para("Tu sticker debe verse bien en un fondo <strong>claro</strong> y en uno <strong>oscuro</strong>. El borde blanco es lo que lo logra."))
    es+=card("Aprende &middot; hazlo","Hazlo en Adobe Illustrator",
        scroll_steps(steps([
            ("Abre Adobe Illustrator.","B&uacute;scalo en el Dock o en Launchpad."),
            ("Abre el archivo provisto.","En tu carpeta del proyecto (del Paso 01), abre <strong>Design_A_Sticker.ai</strong>. Ya est&aacute; listo para ti: el tama&ntilde;o y los colores correctos."),
            ("Primero haz un boceto.","En papel o en tu iPad de estudiante, dibuja tu palabra en letras grandes. Toma una foto con tu iPad y ll&eacute;vala a Illustrator para calcarla."),
            ("Dibuja tus letras.","Calca tu boceto con la herramienta <strong>L&aacute;piz</strong> o <strong>Pluma</strong>. Sin fuentes. Usa tu mismo estilo en cada letra, del mismo grosor."),
            ("Color y contorno.","Rellena cada letra igual (un color o un patr&oacute;n). Dale a cada letra el mismo <strong>contorno negro</strong>."),
            ("Agrega el borde blanco del sticker.","Pon un <strong>borde blanco</strong> grueso alrededor de toda la palabra para que se vea como un sticker real y resalte en cualquier color. El Sr. Silva te ense&ntilde;ar&aacute; c&oacute;mo."),
            ("Guarda tu archivo de Illustrator.","Haz clic en <strong>Archivo &rarr; Guardar</strong> para conservar tu archivo <strong>.ai</strong>. NO entregas el archivo .ai."),
            ("Guarda un PDF vectorial.","Haz clic en <strong>Archivo &rarr; Guardar como</strong> y elige <strong>Adobe PDF</strong>. Escoge el ajuste <strong>[Press Quality]</strong> y haz clic en <strong>Guardar PDF</strong>. Queda como arte vectorial n&iacute;tido en CMYK. Ese PDF es lo que entregas."),
        ], accent="#00b8b8"))
        + note("En la Mac, presiona <strong>Cmd</strong> (no Ctrl). Preg&uacute;ntale al Sr. Silva si te atoras."))
    es+=draw_resource(True)
    es+=card("Aprende &middot; rev&iacute;sate","Antes de Entregar",
        para("Mira tu sticker. &iquest;Puedes marcar las cinco?")
        + bullets([
            ("Mismo grosor","cada letra tiene el mismo peso."),
            ("Mismo estilo","cada letra est&aacute; dibujada de la misma manera."),
            ("Misma l&iacute;nea","todas las letras sobre una l&iacute;nea."),
            ("Borde blanco del sticker","resalta en un fondo claro y en uno oscuro."),
            ("&iquest;Combinar&iacute;a una letra nueva?","si s&iacute;, tu palabra es una familia."),
        ]))
    es+=deliverables_box(True,
        [("1 PDF vectorial:","tu <strong>sticker</strong> terminado, guardado como <strong>PDF vectorial</strong> (Archivo &rarr; Guardar como &rarr; Adobe PDF &rarr; [Press Quality]), subido a esta tarea de Canvas. <strong>No</strong> el archivo .ai, y no un JPG.")])
    es+=next_up("SIGUIENTE &middot; PASO 03 - Reflexi&oacute;n","Cuenta sobre tu sticker: tu estilo y la parte m&aacute;s dif&iacute;cil.")
    stepnav=f'<a href="{S2}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S2}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page(f"Step 2: Make Your Word | Design a Sticker | {CT} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

def reflection():
    # ---- EN ----
    en=banner("Module 09 &bull; Step 03","Reflection",
        "You made your sticker. Now tell me about it.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_REFLECT)
    en+=card("Learn &middot; last step","Fill In Your Reflection",
        para("You made your sticker. Nice work. Now open your reflection sheet and fill it in. It is short: just finish the sentences.")
        + para("It is inside your project folder from Step 01. Open the English or the Spanish reflection, and type right in the boxes."))
    en+=deliverables_box(False,
        [("1 reflection:","your finished reflection (.docx), uploaded to this Canvas assignment.")])
    en+=next_up("MODULE COMPLETE","Nice work. You drew your own letters and turned a word into a sticker, just like a real lettering artist.")
    # ---- ES ----
    es=banner("M&oacute;dulo 09 &bull; Paso 03","Reflexi&oacute;n",
        "Hiciste tu sticker. Ahora cu&eacute;ntame sobre &eacute;l.","#top","Back to English",hicon=HICON_REFLECT)
    es+=card("Aprende &middot; &uacute;ltimo paso","Llena Tu Reflexi&oacute;n",
        para("Hiciste tu sticker. Buen trabajo. Ahora abre tu hoja de reflexi&oacute;n y ll&eacute;nala. Es corta: solo termina las frases.")
        + para("Est&aacute; dentro de tu carpeta del proyecto del Paso 01. Abre la reflexi&oacute;n de ingl&eacute;s o de espa&ntilde;ol y escribe en las cajas."))
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu reflexi&oacute;n terminada (.docx), subida a esta tarea de Canvas.")])
    es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Dibujaste tus propias letras y convertiste una palabra en un sticker, como un verdadero artista de letras.")
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page(f"Step 3: Reflection | Design a Sticker | {CT} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

# ================= BUILD =================
for fname,gen in [(OVER,overview),(S1,make_word),(S2,reflection)]:
    html=ent(gen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    assert "–" not in html and "&ndash;" not in html, "en dash in "+fname
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
