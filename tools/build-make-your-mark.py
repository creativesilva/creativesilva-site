#!/usr/bin/env python3
# Make Your Mark: DA1A typography module (Module 09), lighter DA1 dialect, full color-coding kept
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

REFL_EN=f"{SITE}/assets/course-documents/Make-Your-Mark-Reflection-EN.docx"
REFL_ES=f"{SITE}/assets/course-documents/Make-Your-Mark-Reflection-ES.docx"
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
def photo(src, alt, maxw="540px"):
    # one of Chris's real sticker photos, centered and framed
    return (f'<div style="margin:10px 0 2px;text-align:center;">'
            f'<img src="{src}" alt="{alt}" style="width:100%;max-width:{maxw};height:auto;display:block;margin:0 auto;'
            f'border:1px solid rgba(255,255,255,0.12);box-sizing:border-box;" /></div>')

def style_ideas(es):
    cards=""
    for en_n,es_n,en_d,es_d in STYLE_IDEAS:
        n=es_n if es else en_n; d=es_d if es else en_d
        cards+=(f'<div style="flex:1 1 30%;min-width:170px;max-width:calc(33.333% - 8px);background:#0a1414;'
                f'border:1px solid rgba(255,255,255,0.08);border-top:2px solid #00b8b8;padding:14px 14px 13px;box-sizing:border-box;">'
                f'<div style="font-size:12.5pt;font-weight:700;letter-spacing:0.03em;text-transform:uppercase;color:#eafeff;">{n}</div>'
                f'<div style="font-size:12.5pt;color:#9fc3c3;margin-top:4px;line-height:1.45;">{d}</div></div>')
    return f'<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:4px;">{cards}</div>'

def scroll_steps(inner):
    # locked contained scroller (teal), so a long how-to never looks like a tall intimidating stack
    return ('<div class="silva-scroll" style="max-height:440px;overflow-y:auto;padding:14px 16px 20px;'
            'border:1px solid rgba(0,184,184,0.30);background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, '
            'rgba(0,0,0,0.14) 88%, rgba(0,184,184,0.14) 100%);">' + inner + '</div>')

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
        heading="Descarga Tu Hoja de Reflexi&oacute;n"
        lead="Descarga tu hoja de reflexi&oacute;n. La llenas al final, en el Paso 03."
        lab_en="Reflexi&oacute;n (ingl&eacute;s)"; lab_es="Reflexi&oacute;n (espa&ntilde;ol)"
        note_t=("<strong style=\"color:#ffb27c;\">Gu&aacute;rdala:</strong> ponla en "
                f"OneDrive &rarr; {AREA} para que no se te pierda.")
    else:
        heading="Download Your Reflection Sheet"
        lead="Download your reflection sheet. You fill it in at the end, on Step 03."
        lab_en="Reflection (English)"; lab_es="Reflection (Spanish)"
        note_t=("<strong style=\"color:#ffb27c;\">Keep it:</strong> save it in "
                f"OneDrive &rarr; {AREA} so you do not lose it.")
    rows=''
    if HAVE_REFL:
        rows=('<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
              + dl_link(REFL_ES if es else REFL_EN, lab_es if es else lab_en, row=True)
              + dl_link(REFL_EN if es else REFL_ES, lab_en if es else lab_es, row=True)
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
            f'        <a href="{OVER}" class="bc-hide-sm">Make Your Mark</a>\n'
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
    en=banner("Module 09 &bull; Step 01","Make Your Mark: Start Here",
        "Read this page, then go to Step 02 to make your sticker.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=card("Learn &middot; the idea","Turn a Word Into a Sticker",
        para("This is an <strong>Adobe Illustrator</strong> project. You will <strong>draw your own letters</strong> and turn a word into a <strong>sticker</strong>.")
        + para("Pick a word you like: your name, a nickname, or any short word. Give every letter the same style, so your word looks like one set.")
        + (photo(HERO_SCRIPT,"A brush-script vinyl sticker with a white border, held over grass") if HAVE_ART else ""))
    en+=resources_card("Watch &amp; look",
        para("Here are real stickers. Look how every letter is drawn in <strong>one style</strong>, with a black outline. The <strong>white border</strong> around the word makes the sticker pop on any color.")
        + (photo(EX_LOVE,"A LOVE sticker: each letter drawn in one style with a pattern, a black outline, and a white border") if HAVE_ART else "")
        + para("<strong>Watch:</strong> Mr. Silva will show you a quick demo before you start."),es=False)
    en+=card("Learn &middot; 3 things that make it work","Check These Three",
        vocab3(False)
        + para("If you added one more letter, would it fit right in? If yes, your word is a family."))
    en+=card("Learn &middot; the sticker trick","Make It Work Anywhere",
        para("A sticker needs a <strong>white border</strong> around it. That border makes your word pop on <strong>any</strong> color: a dark window or a white car.")
        + para("You will add a white border in Step 02. You will check for it before you turn it in."))
    en+=downloads(False)
    en+=card("How It Works / Your Plan","Your Next 2 Steps",
        para("You are on Step 01 now: read this page and get your reflection sheet. Here are the two steps that follow.")
        + bullets([
            ("Step 02 &middot; Make Your Word:","pick a style, draw your letters, and add the white sticker border."),
            ("Step 03 &middot; Reflection:","fill in a short sheet about your sticker."),
        ]))
    en+=standards_box(False, MYM_STANDARDS)
    en+=next_up("UP NEXT &middot; STEP 02 - Make Your Word","Pick a style, draw a word you like, and turn it into a sticker.")
    # ---- ES ----
    es=banner("M&oacute;dulo 09 &bull; Paso 01","Make Your Mark: Empieza Aqu&iacute;",
        "Lee esta p&aacute;gina y luego ve al Paso 02 para hacer tu sticker.","#top","Back to English",hicon=HICON_DESIGN)
    es+=card("Aprende &middot; la idea","Convierte una Palabra en un Sticker",
        para("Este es un proyecto de <strong>Adobe Illustrator</strong>. Vas a <strong>dibujar tus propias letras</strong> y convertir una palabra en un <strong>sticker</strong>.")
        + para("Elige una palabra que te guste: tu nombre, un apodo o cualquier palabra corta. Dale a cada letra el mismo estilo, para que tu palabra se vea como un solo conjunto.")
        + (photo(HERO_SCRIPT,"Un sticker de letra de pincel con borde blanco, sobre el pasto") if HAVE_ART else ""))
    es+=resources_card("Mira y observa",
        para("Aqu&iacute; hay stickers reales. Mira c&oacute;mo cada letra est&aacute; dibujada en <strong>un estilo</strong>, con un borde negro. El <strong>borde blanco</strong> alrededor de la palabra hace que el sticker resalte en cualquier color.")
        + (photo(EX_LOVE,"Un sticker de LOVE: cada letra dibujada en un estilo con un patr&oacute;n, un borde negro y un borde blanco") if HAVE_ART else "")
        + para("<strong>Mira:</strong> el Sr. Silva te ense&ntilde;ar&aacute; una demostraci&oacute;n corta antes de empezar."),es=True)
    es+=card("Aprende &middot; 3 cosas que lo hacen funcionar","Revisa Estas Tres",
        vocab3(True)
        + para("Si agregaras una letra m&aacute;s, &iquest;combinar&iacute;a bien? Si s&iacute;, tu palabra es una familia."))
    es+=card("Aprende &middot; el truco del sticker","Haz Que Funcione en Todos Lados",
        para("Un sticker necesita un <strong>borde blanco</strong> alrededor. Ese borde hace que tu palabra resalte en <strong>cualquier</strong> color: una ventana oscura o un carro blanco.")
        + para("Agregar&aacute;s un borde blanco en el Paso 02. Lo revisar&aacute;s antes de entregar."))
    es+=downloads(True)
    es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Siguientes 2 Pasos",
        para("Est&aacute;s en el Paso 01 ahora: lee esta p&aacute;gina y descarga tu hoja de reflexi&oacute;n. Aqu&iacute; est&aacute;n los dos pasos que siguen.")
        + bullets([
            ("Paso 02 &middot; Haz Tu Palabra:","elige un estilo, dibuja tus letras y agrega el borde blanco del sticker."),
            ("Paso 03 &middot; Reflexi&oacute;n:","llena una hoja corta sobre tu sticker."),
        ]))
    es+=standards_box(True, MYM_STANDARDS)
    es+=next_up("SIGUIENTE &middot; PASO 02 - Haz Tu Palabra","Elige un estilo, dibuja una palabra que te guste y convi&eacute;rtela en un sticker.")
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
    return wrap_page(f"Make Your Mark | {CT} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

def make_word():
    # ---- EN ----
    en=banner("Module 09 &bull; Step 02","Make Your Word",
        "Draw your letters and turn your word into a sticker.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=card("Learn &middot; pick your style","Pick a Style to Draw",
        para("You will <strong>draw</strong> your letters, no fonts. Pick <strong>ONE</strong> style and draw every letter the same way.")
        + (style_ideas(False) if HAVE_ART else "")
        + para("Your sticker should look good on a <strong>light</strong> and a <strong>dark</strong> background. The white border is what makes that happen."))
    en+=card("Learn &middot; make it","Make It in Adobe Illustrator",
        scroll_steps(steps([
            ("Open Adobe Illustrator.","Find it in the Dock or in Launchpad."),
            ("Make a new file.","Click <strong>File &rarr; New</strong> (or press Cmd+N). Click the <strong>Web</strong> tab, name it your word, and check that Color Mode is <strong>RGB</strong>. Click <strong>Create</strong>."),
            ("Sketch your word first.","On paper or your student iPad, draw your word in big letters. Take a photo with your iPad and bring it into Illustrator to trace."),
            ("Draw your letters.","Trace your sketch with the <strong>Pencil</strong> or <strong>Pen</strong> tool. No fonts. Use your one style on every letter, the same thickness."),
            ("Color and outline.","Fill every letter the same way (one color or a pattern). Give every letter the same <strong>black outline</strong>."),
            ("Add the white sticker border.","Put a thick <strong>white border</strong> around the whole word so it looks like a real sticker and pops on any color. Mr. Silva will show you how."),
            ("Save, then export a JPG.","Click <strong>File &rarr; Save</strong> (your .ai file). Then <strong>File &rarr; Export &rarr; Export As</strong> and pick <strong>JPEG</strong>. This JPG is what you turn in."),
        ], accent="#00b8b8"))
        + note("On the Mac, press <strong>Cmd</strong> (not Ctrl). Ask Mr. Silva if you get stuck."))
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
        [("1 image:","your finished <strong>sticker</strong>, saved as a <strong>JPG</strong> (File &rarr; Export &rarr; Export As &rarr; JPEG), uploaded to this Canvas assignment.")])
    en+=next_up("UP NEXT &middot; STEP 03 - Reflection","Tell about your sticker: your style, and the hardest part.")
    # ---- ES ----
    es=banner("M&oacute;dulo 09 &bull; Paso 02","Haz Tu Palabra",
        "Dibuja tus letras y convierte tu palabra en un sticker.","#top","Back to English",hicon=HICON_DESIGN)
    es+=card("Aprende &middot; elige tu estilo","Elige un Estilo para Dibujar",
        para("Vas a <strong>dibujar</strong> tus letras, sin fuentes. Elige <strong>UN</strong> estilo y dibuja cada letra de la misma manera.")
        + (style_ideas(True) if HAVE_ART else "")
        + para("Tu sticker debe verse bien en un fondo <strong>claro</strong> y en uno <strong>oscuro</strong>. El borde blanco es lo que lo logra."))
    es+=card("Aprende &middot; hazlo","Hazlo en Adobe Illustrator",
        scroll_steps(steps([
            ("Abre Adobe Illustrator.","B&uacute;scalo en el Dock o en Launchpad."),
            ("Haz un archivo nuevo.","Haz clic en <strong>Archivo &rarr; Nuevo</strong> (o presiona Cmd+N). Haz clic en la pesta&ntilde;a <strong>Web</strong>, ponle el nombre de tu palabra y revisa que el Modo de Color sea <strong>RGB</strong>. Haz clic en <strong>Crear</strong>."),
            ("Primero haz un boceto.","En papel o en tu iPad de estudiante, dibuja tu palabra en letras grandes. Toma una foto con tu iPad y ll&eacute;vala a Illustrator para calcarla."),
            ("Dibuja tus letras.","Calca tu boceto con la herramienta <strong>L&aacute;piz</strong> o <strong>Pluma</strong>. Sin fuentes. Usa tu mismo estilo en cada letra, del mismo grosor."),
            ("Color y contorno.","Rellena cada letra igual (un color o un patr&oacute;n). Dale a cada letra el mismo <strong>contorno negro</strong>."),
            ("Agrega el borde blanco del sticker.","Pon un <strong>borde blanco</strong> grueso alrededor de toda la palabra para que se vea como un sticker real y resalte en cualquier color. El Sr. Silva te ense&ntilde;ar&aacute; c&oacute;mo."),
            ("Guarda y exporta un JPG.","Haz clic en <strong>Archivo &rarr; Guardar</strong> (tu archivo .ai). Luego <strong>Archivo &rarr; Exportar &rarr; Exportar como</strong> y elige <strong>JPEG</strong>. Ese JPG es lo que entregas."),
        ], accent="#00b8b8"))
        + note("En la Mac, presiona <strong>Cmd</strong> (no Ctrl). Preg&uacute;ntale al Sr. Silva si te atoras."))
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
        [("1 imagen:","tu <strong>sticker</strong> terminado, guardado como <strong>JPG</strong> (Archivo &rarr; Exportar &rarr; Exportar como &rarr; JPEG), subido a esta tarea de Canvas.")])
    es+=next_up("SIGUIENTE &middot; PASO 03 - Reflexi&oacute;n","Cuenta sobre tu sticker: tu estilo y la parte m&aacute;s dif&iacute;cil.")
    stepnav=f'<a href="{S2}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S2}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page(f"Step 2: Make Your Word | Make Your Mark | {CT} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

def reflection():
    # ---- EN ----
    en=banner("Module 09 &bull; Step 03","Reflection",
        "You made your sticker. Now tell me about it.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_REFLECT)
    en+=card("Learn &middot; last step","Fill In Your Reflection",
        para("You made your sticker. Nice work. Now open your reflection sheet and fill it in. It is short: just finish the sentences.")
        + para("You downloaded it on Step 01, the Overview. Open the English or the Spanish one, and type right in the boxes."))
    en+=deliverables_box(False,
        [("1 reflection:","your finished reflection (.docx), uploaded to this Canvas assignment.")])
    en+=next_up("MODULE COMPLETE","Nice work. You drew your own letters and turned a word into a sticker, just like a real lettering artist.")
    # ---- ES ----
    es=banner("M&oacute;dulo 09 &bull; Paso 03","Reflexi&oacute;n",
        "Hiciste tu sticker. Ahora cu&eacute;ntame sobre &eacute;l.","#top","Back to English",hicon=HICON_REFLECT)
    es+=card("Aprende &middot; &uacute;ltimo paso","Llena Tu Reflexi&oacute;n",
        para("Hiciste tu sticker. Buen trabajo. Ahora abre tu hoja de reflexi&oacute;n y ll&eacute;nala. Es corta: solo termina las frases.")
        + para("La descargaste en el Paso 01, el Resumen. Abre la de ingl&eacute;s o la de espa&ntilde;ol y escribe en las cajas."))
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu reflexi&oacute;n terminada (.docx), subida a esta tarea de Canvas.")])
    es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Dibujaste tus propias letras y convertiste una palabra en un sticker, como un verdadero artista de letras.")
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page(f"Step 3: Reflection | Make Your Mark | {CT} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

# ================= BUILD =================
for fname,gen in [(OVER,overview),(S1,make_word),(S2,reflection)]:
    html=ent(gen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    assert "–" not in html and "&ndash;" not in html, "en dash in "+fname
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
