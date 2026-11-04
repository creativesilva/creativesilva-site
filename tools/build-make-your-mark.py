#!/usr/bin/env python3
# Make Your Mark: DA1A typography module (Module 09), the first module built in the lighter DA1 dialect
# (Chris, 2026-11-04): visual-first (big examples, a style picture-menu, vocab shown as pictures, 2 turn-ins),
# built for a 5th-grade-reading, low-engagement, mixed-ability room, with the full color-coding kept
# (teal = learn, purple = watch/look, orange = download, gold = turn in, green = teacher/standards).
# Concept: design a word (student's choice, 3+ letters) where every letter shares ONE style and the SAME
# stroke weight, so it reads as a family that could grow into a real font. Start from a bold font, then
# style every letter the same (floor); redraw the letters yourself (stretch). 3 pages, Overview = Step 01.
# Styled-word art is starter art (headless-Chrome renders) for Chris to approve/replace with Illustrator.
import os
from silva_framework import *

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Digital Arts Folder"
CT="Digital Arts 1A"; PFX="digarts1"
IMGDIR=f"{SITE}/assets/images/digarts1/make-your-mark"
HERO=f"{IMGDIR}/mark-hero-v3.png"
HAVE_ART=True

# style key -> (EN name, ES name, image). v3 (Chris 2026-11-04): clean artwork on a TRANSPARENT
# background so each word sits directly on the dark card (the v2 split light/dark panels were dropped
# as too busy/ugly). The "works on a light or dark background" idea is now TEXT only.
STYLES=[
  ("chrome","Liquid Chrome","Cromo",  f"{IMGDIR}/style-chrome-v3.png"),  # DREAM
  ("neon",  "Neon",         "Neón", f"{IMGDIR}/style-neon-v3.png"),  # FOCUS
  ("paper", "Paper Cut",    "Papel",   f"{IMGDIR}/style-paper-v3.png"),   # BOLD
  ("brush", "Brush",        "Pincel",  f"{IMGDIR}/style-brush-v3.png"),   # LOVE
  ("leaf",  "Leaf",         "Hoja",    f"{IMGDIR}/style-leaf-v3.png"),    # PEACE
  ("pop",   "3D Pop",       "3D",      f"{IMGDIR}/style-pop-v3.png"),     # RISE
]
GALLERY=[f"{IMGDIR}/ex-shine-v3.png",f"{IMGDIR}/ex-brave-v3.png",f"{IMGDIR}/ex-kind-v3.png",f"{IMGDIR}/ex-hope-v3.png"]

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
   "en_desc":"You use line, shape, and repetition to build letters that share one clear style.",
   "es_desc":"Usas la l&iacute;nea, la forma y la repetici&oacute;n para crear letras que comparten un mismo estilo claro."},
  {"code":"SA.11.2","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Unity &amp; Consistency","es_title":"Unidad y Consistencia",
   "en_desc":"You keep the same stroke weight and style across every letter, so your word reads as one family.",
   "es_desc":"Mantienes el mismo grosor y estilo en cada letra, para que tu palabra se vea como una sola familia."},
  {"code":"MA.11.4","en_tier":"Media Arts","es_tier":"Artes de Medios",
   "en_title":"Digital Tools","es_title":"Herramientas Digitales",
   "en_desc":"You use Adobe Illustrator to make original type art and export it as a finished image.",
   "es_desc":"Usas Adobe Illustrator para crear arte original con letras y lo exportas como una imagen terminada."},
  {"code":"MA.11.6","en_tier":"Media Arts","es_tier":"Artes de Medios",
   "en_title":"Communicate a Message","es_title":"Comunicar un Mensaje",
   "en_desc":"You pick a style on purpose so your word shows a feeling or a vibe.",
   "es_desc":"Eliges un estilo a prop&oacute;sito para que tu palabra muestre un sentimiento o una vibra."},
]

# ---------- visual components (Canvas-safe: inline styles + images, flex not grid) ----------
def img_center(src, alt, maxh="160px"):
    # v3 art is a transparent word: seat it centered on a subtle dark inner panel.
    return (f'<div style="background:#0a1414;border:1px solid rgba(255,255,255,0.08);padding:26px 18px;'
            f'margin:10px 0 2px;text-align:center;">'
            f'<img src="{src}" alt="{alt}" style="max-width:100%;max-height:{maxh};width:auto;height:auto;display:block;margin:0 auto;" /></div>')

def style_menu(es):
    cards=""
    for key,en,esn,src in STYLES:
        name=esn if es else en
        cards+=(f'<div style="flex:1 1 30%;min-width:210px;max-width:calc(33.333% - 9px);background:#0a1414;'
                f'border:1px solid rgba(255,255,255,0.08);border-top:2px solid #00b8b8;padding:20px 10px 12px;'
                f'text-align:center;box-sizing:border-box;">'
                f'<div style="height:120px;display:flex;align-items:center;justify-content:center;">'
                f'<img src="{src}" alt="{name}" style="max-width:100%;max-height:110px;width:auto;height:auto;display:block;" /></div>'
                f'<div style="font-size:12pt;font-weight:600;letter-spacing:0.04em;text-transform:uppercase;color:#eafeff;margin-top:11px;">{name}</div>'
                f'</div>')
    return (f'<div style="display:flex;flex-wrap:wrap;gap:13px;margin-top:4px;">{cards}</div>')

def example_gallery():
    imgs=""
    for src in GALLERY:
        imgs+=(f'<div style="flex:1 1 44%;min-width:220px;max-width:calc(50% - 7px);background:#0a1414;'
               f'border:1px solid rgba(255,255,255,0.08);padding:18px;text-align:center;box-sizing:border-box;">'
               f'<div style="height:100px;display:flex;align-items:center;justify-content:center;">'
               f'<img src="{src}" alt="Example word" style="max-width:100%;max-height:92px;width:auto;height:auto;display:block;" /></div></div>')
    return (f'<div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:4px;">{imgs}</div>')

def vocab3(es):
    # three ideas shown as pictures, done with inline styles (no font files needed, Canvas-safe)
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
        "Read this page, then go to Step 02 to make your word.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=card("Learn &middot; the idea","Turn a Word Into One Cool Style",
        para("This is an <strong>Adobe Illustrator</strong> project. Pick a word you like: your name, a nickname, or any short word. <strong>Give every letter the same cool style.</strong> That is the whole job.")
        + para("When all your letters match, they look like a real font: one family.")
        + (img_center(HERO,"The word MARK styled as bold 3D art") if HAVE_ART else ""))
    en+=resources_card("Watch &amp; look",
        para("Here are words other people turned into art. Look at how every letter in a word matches. Pick a style you like.")
        + (example_gallery() if HAVE_ART else "")
        + para("<strong>Watch:</strong> Mr. Silva will show you a quick demo before you start."),es=False)
    en+=card("Learn &middot; 3 things that make it work","Check These Three",
        vocab3(False)
        + para("If you added one more letter, would it fit right in? If yes, your word is a family."))
    en+=card("Learn &middot; one more rule","Make It Work Anywhere",
        para("A strong word looks good on a <strong>light</strong> background and a <strong>dark</strong> one.")
        + para("Make your word work on both. You will check this before you turn it in."))
    en+=downloads(False)
    en+=card("How It Works / Your Plan","Your Next 2 Steps",
        para("You are on Step 01 now: read this page and get your reflection sheet. Here are the two steps that follow.")
        + bullets([
            ("Step 02 &middot; Make Your Word:","pick a style, type your word, and give every letter the same look."),
            ("Step 03 &middot; Reflection:","fill in a short sheet about your word."),
        ]))
    en+=standards_box(False, MYM_STANDARDS)
    en+=next_up("UP NEXT &middot; STEP 02 - Make Your Word","Pick a style, type a word you like, and make every letter match.")
    # ---- ES ----
    es=banner("M&oacute;dulo 09 &bull; Paso 01","Make Your Mark: Empieza Aqu&iacute;",
        "Lee esta p&aacute;gina y luego ve al Paso 02 para hacer tu palabra.","#top","Back to English",hicon=HICON_DESIGN)
    es+=card("Aprende &middot; la idea","Convierte una Palabra en un Solo Estilo",
        para("Este es un proyecto de <strong>Adobe Illustrator</strong>. Elige una palabra que te guste: tu nombre, un apodo o cualquier palabra corta. <strong>Dale a cada letra el mismo estilo.</strong> Ese es todo el trabajo.")
        + para("Cuando todas tus letras se parecen, se ven como una fuente real: una familia.")
        + (img_center(HERO,"La palabra MARK como arte 3D en negrita") if HAVE_ART else ""))
    es+=resources_card("Mira y observa",
        para("Aqu&iacute; hay palabras que otras personas convirtieron en arte. Mira c&oacute;mo cada letra de una palabra se parece. Elige un estilo que te guste.")
        + (example_gallery() if HAVE_ART else "")
        + para("<strong>Mira:</strong> el Sr. Silva te ense&ntilde;ar&aacute; una demostraci&oacute;n corta antes de empezar."),es=True)
    es+=card("Aprende &middot; 3 cosas que lo hacen funcionar","Revisa Estas Tres",
        vocab3(True)
        + para("Si agregaras una letra m&aacute;s, &iquest;combinar&iacute;a bien? Si s&iacute;, tu palabra es una familia."))
    es+=card("Aprende &middot; una regla m&aacute;s","Haz Que Funcione en Todos Lados",
        para("Una palabra fuerte se ve bien en un fondo <strong>claro</strong> y en uno <strong>oscuro</strong>.")
        + para("Haz que tu palabra funcione en los dos. Revisar&aacute;s esto antes de entregar."))
    es+=downloads(True)
    es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Siguientes 2 Pasos",
        para("Est&aacute;s en el Paso 01 ahora: lee esta p&aacute;gina y descarga tu hoja de reflexi&oacute;n. Aqu&iacute; est&aacute;n los dos pasos que siguen.")
        + bullets([
            ("Paso 02 &middot; Haz Tu Palabra:","elige un estilo, escribe tu palabra y dale a cada letra el mismo look."),
            ("Paso 03 &middot; Reflexi&oacute;n:","llena una hoja corta sobre tu palabra."),
        ]))
    es+=standards_box(True, MYM_STANDARDS)
    es+=next_up("SIGUIENTE &middot; PASO 02 - Haz Tu Palabra","Elige un estilo, escribe una palabra que te guste y haz que cada letra combine.")
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
    return wrap_page(f"Make Your Mark | {CT} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

def make_word():
    # ---- EN ----
    en=banner("Module 09 &bull; Step 02","Make Your Word",
        "Pick a style, type your word, and make every letter match.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=card("Learn &middot; pick your style","Pick ONE Style",
        para("Tap a style you like. <strong>Every letter in your word gets this same style.</strong> You only pick one.")
        + (style_menu(False) if HAVE_ART else "")
        + para("Pick a style you can keep the same on every letter. It should look good on a <strong>light</strong> and a <strong>dark</strong> background."))
    en+=card("Learn &middot; make it","Make It in Adobe Illustrator",
        steps([
            ("Open Adobe Illustrator.","Find it in the Dock or in Launchpad."),
            ("Make a new file.","Click <strong>File &rarr; New</strong> (or press Cmd+N). Click the <strong>Web</strong> tab, name it your word, and check that Color Mode is <strong>RGB</strong>. Click <strong>Create</strong>."),
            ("Type your word.","Pick the <strong>Type tool</strong>, click on the artboard, and type your word (3 or more letters). Pick a big, <strong>bold</strong> font."),
            ("Give it ONE style.","Give the whole word the same look: same colors, same effect, on every letter."),
            ("Keep it even.","Every letter the same thickness, all sitting on the same line."),
            ("Save your file.","Click <strong>File &rarr; Save</strong>. Keep the Illustrator (.ai) file so you can fix it later."),
            ("Export a JPG.","Click <strong>File &rarr; Export &rarr; Export As</strong>. Pick <strong>JPEG</strong>, then Export. This JPG is what you turn in."),
        ], accent="#00b8b8")
        + note("On the Mac, press <strong>Cmd</strong> (not Ctrl). Ask Mr. Silva if you get stuck."))
    en+=card("Learn &middot; check yourself","Before You Turn It In",
        para("Look at your word. Can you check all five?")
        + bullets([
            ("Same thickness","every letter is the same weight."),
            ("Same style","every letter has the same look."),
            ("Same line","all letters sit on one line."),
            ("Works on light AND dark","it looks good on a light background and a dark one."),
            ("Would a new letter fit in?","if yes, your word is a family."),
        ]))
    en+=deliverables_box(False,
        [("1 image:","your finished word, saved as a <strong>JPG</strong> (File &rarr; Export), uploaded to this Canvas assignment.")])
    en+=next_up("UP NEXT &middot; STEP 03 - Reflection","Tell about your word: your style, and the hardest part.")
    # ---- ES ----
    es=banner("M&oacute;dulo 09 &bull; Paso 02","Haz Tu Palabra",
        "Elige un estilo, escribe tu palabra y haz que cada letra combine.","#top","Back to English",hicon=HICON_DESIGN)
    es+=card("Aprende &middot; elige tu estilo","Elige UN Estilo",
        para("Toca un estilo que te guste. <strong>Cada letra de tu palabra recibe este mismo estilo.</strong> Solo eliges uno.")
        + (style_menu(True) if HAVE_ART else "")
        + para("Elige un estilo que puedas repetir en cada letra. Debe verse bien en un fondo <strong>claro</strong> y en uno <strong>oscuro</strong>."))
    es+=card("Aprende &middot; hazlo","Hazlo en Adobe Illustrator",
        steps([
            ("Abre Adobe Illustrator.","B&uacute;scalo en el Dock o en Launchpad."),
            ("Haz un archivo nuevo.","Haz clic en <strong>Archivo &rarr; Nuevo</strong> (o presiona Cmd+N). Haz clic en la pesta&ntilde;a <strong>Web</strong>, ponle el nombre de tu palabra y revisa que el Modo de Color sea <strong>RGB</strong>. Haz clic en <strong>Crear</strong>."),
            ("Escribe tu palabra.","Elige la <strong>herramienta Texto</strong>, haz clic en la mesa de trabajo y escribe tu palabra (3 letras o m&aacute;s). Elige una fuente grande y <strong>gruesa</strong>."),
            ("Dale UN estilo.","Dale a toda la palabra el mismo look: los mismos colores, el mismo efecto, en cada letra."),
            ("Mant&eacute;nla pareja.","Cada letra del mismo grosor, todas sobre la misma l&iacute;nea."),
            ("Guarda tu archivo.","Haz clic en <strong>Archivo &rarr; Guardar</strong>. Guarda el archivo de Illustrator (.ai) para arreglarlo despu&eacute;s."),
            ("Exporta un JPG.","Haz clic en <strong>Archivo &rarr; Exportar &rarr; Exportar como</strong>. Elige <strong>JPEG</strong> y luego Exportar. Ese JPG es lo que entregas."),
        ], accent="#00b8b8")
        + note("En la Mac, presiona <strong>Cmd</strong> (no Ctrl). Preg&uacute;ntale al Sr. Silva si te atoras."))
    es+=card("Aprende &middot; rev&iacute;sate","Antes de Entregar",
        para("Mira tu palabra. &iquest;Puedes marcar las cinco?")
        + bullets([
            ("Mismo grosor","cada letra tiene el mismo peso."),
            ("Mismo estilo","cada letra tiene el mismo look."),
            ("Misma l&iacute;nea","todas las letras sobre una l&iacute;nea."),
            ("Funciona en claro Y oscuro","se ve bien en un fondo claro y en uno oscuro."),
            ("&iquest;Combinar&iacute;a una letra nueva?","si s&iacute;, tu palabra es una familia."),
        ]))
    es+=deliverables_box(True,
        [("1 imagen:","tu palabra terminada, guardada como <strong>JPG</strong> (Archivo &rarr; Exportar), subida a esta tarea de Canvas.")])
    es+=next_up("SIGUIENTE &middot; PASO 03 - Reflexi&oacute;n","Cuenta sobre tu palabra: tu estilo y la parte m&aacute;s dif&iacute;cil.")
    stepnav=f'<a href="{S2}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S2}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page(f"Step 2: Make Your Word | Make Your Mark | {CT} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

def reflection():
    # ---- EN ----
    en=banner("Module 09 &bull; Step 03","Reflection",
        "You made your word. Now tell me about it.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_REFLECT)
    en+=card("Learn &middot; last step","Fill In Your Reflection",
        para("You made your word. Nice work. Now open your reflection sheet and fill it in. It is short: just finish the sentences.")
        + para("You downloaded it on Step 01, the Overview. Open the English or the Spanish one, and type right in the boxes."))
    en+=deliverables_box(False,
        [("1 reflection:","your finished reflection (.docx), uploaded to this Canvas assignment.")])
    en+=next_up("MODULE COMPLETE","Nice work. You took one word and made every letter into one family, just like a real font designer.")
    # ---- ES ----
    es=banner("M&oacute;dulo 09 &bull; Paso 03","Reflexi&oacute;n",
        "Hiciste tu palabra. Ahora cu&eacute;ntame sobre ella.","#top","Back to English",hicon=HICON_REFLECT)
    es+=card("Aprende &middot; &uacute;ltimo paso","Llena Tu Reflexi&oacute;n",
        para("Hiciste tu palabra. Buen trabajo. Ahora abre tu hoja de reflexi&oacute;n y ll&eacute;nala. Es corta: solo termina las frases.")
        + para("La descargaste en el Paso 01, el Resumen. Abre la de ingl&eacute;s o la de espa&ntilde;ol y escribe en las cajas."))
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu reflexi&oacute;n terminada (.docx), subida a esta tarea de Canvas.")])
    es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Tomaste una palabra e hiciste que cada letra fuera una familia, como un dise&ntilde;ador de fuentes real.")
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
