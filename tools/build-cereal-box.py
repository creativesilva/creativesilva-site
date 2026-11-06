#!/usr/bin/env python3
# Cereal Box Group Project: DA1A Module 10 (promoted from the MRC track into the current angular
# DA framework). Groups of 2 invent a cereal brand (name, mascot, colors), design all six box
# panels, then take it to social media. Bilingual EN + ES, teal angular look, PV crest.
# Direction (Chris, 2026-11-06):
#   - Elements of Art is DROPPED (covered in the Character Design project): no standalone EoA page
#     and no "sketch the elements" step, and the overview loses the seven-elements framing.
#   - Students DO sketch their cereal brand + box concept, and get it APPROVED by Mr. Silva before
#     any digital design (teacher sign-off gate on the Concept Sketch step).
#   - Groups of 2 share their working file over OneDrive ON A MAC (Mac-only steps: Finder,
#     Control-click, Cmd), never PC/Windows.
#   - A standalone shareable copy (no links back to the catalog or teacher tools) is generated
#     separately for sharing with another teacher. Built after the curriculum version is approved.
import os
from silva_framework import *
import silva_framework as _sf

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Digital Arts Folder"
CT="Digital Arts 1A"; PFX="digarts1"

# Images (reused from the MRC build; hosted on the whitelisted domain).
HERO=f"{SITE}/assets/images/cereal/cereal-header.png"     # row of cereal boxes on a shelf
CATS=f"{SITE}/assets/images/cereal/cereal-categories.png" # the four category lanes
HAVE_ART=True

# Project folder download: the DA folder = the 7 Illustrator templates (6 panels + print template)
# plus the 6 DA-format docs (Research / Design Choices / Reflection, each EN + ES, no Elements of
# Art). Built by tools/build-cereal-docs.js + zipped into assets/course-documents/.
PROJECT_ZIP=f"{SITE}/assets/course-documents/Cereal-Box-Project-Folder.zip"
HAVE_ZIP=True

OVER=f"{PFX}-cereal-box-overview.html"
S02=f"{PFX}-cereal-box-step02-research.html"
S03=f"{PFX}-cereal-box-step03-design-choices.html"
S04=f"{PFX}-cereal-box-step04-concept-sketch.html"
S05=f"{PFX}-cereal-box-step05-digital-design.html"
S06=f"{PFX}-cereal-box-step06-social-media.html"
S07=f"{PFX}-cereal-box-step07-reflection.html"

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

# ---- Four cereal category lanes: (EN name, ES name, EN desc, ES desc) ----
CATEGORIES=[
  ("Sugary / Kids","Azucarado / Ni&ntilde;os","bright colors, a fun mascot, sweet flavors.","colores brillantes, una mascota divertida, sabores dulces."),
  ("Health / Organic","Saludable / Org&aacute;nico","whole grains, fiber, clean and simple labels.","granos enteros, fibra, etiquetas limpias y simples."),
  ("Protein / Fitness","Prote&iacute;na / Fitness","high protein, a strong athlete look, bold claims.","alta en prote&iacute;na, estilo deportista, datos llamativos."),
  ("Family / Everyday","Familiar / Diario","simple flavors, everyday breakfast, a trusted look.","sabores simples, desayuno diario, un dise&ntilde;o confiable."),
]

# ---- 6 package-design vocab terms: (EN term, ES term, EN def, ES def) ----
VOCAB=[
  ("Mockup","Maqueta (Mockup)",
   "A real-looking picture of your design on the product. A box mockup shows what your cereal would look like on a real shelf.",
   "Una imagen realista de tu dise&ntilde;o en el producto. Una maqueta muestra c&oacute;mo se ver&iacute;a tu cereal en un estante real."),
  ("Dieline","Troquel (Dieline)",
   "The flat shape of the box before it is folded. It shows where to cut, where to fold, and where each panel goes.",
   "La forma plana de la caja antes de doblarla. Muestra d&oacute;nde cortar, d&oacute;nde doblar y d&oacute;nde va cada panel."),
  ("Mascot","Mascota",
   "A character that shows the brand. Tony the Tiger and Cap&rsquo;n Crunch are mascots. A strong mascot makes a brand easy to remember.",
   "Un personaje que representa la marca. El Tigre Tony y el Capit&aacute;n Crunch son mascotas. Una buena mascota hace la marca f&aacute;cil de recordar."),
  ("Tagline","Eslogan",
   "A short phrase that sells the product. A good tagline is short, fun, and easy to say out loud.",
   "Una frase corta que vende el producto. Un buen eslogan es corto, divertido y f&aacute;cil de decir."),
  ("Target Audience","P&uacute;blico Meta",
   "The group of people the cereal is made for: kids, teens, athletes, or grown-ups. Every choice on the box should match them.",
   "El grupo de personas para quienes se hace el cereal: ni&ntilde;os, j&oacute;venes, deportistas o adultos. Cada decisi&oacute;n de la caja debe coincidir con ellos."),
  ("Front Panel","Panel Frontal",
   "The face of the box, the part the shopper sees first. It holds the name, the mascot, and the tagline. Your strongest design goes here.",
   "La cara de la caja, lo primero que ve el comprador. Lleva el nombre, la mascota y el eslogan. Tu mejor dise&ntilde;o va aqu&iacute;."),
]

# ---- 6-step roadmap (Overview is Step 01): (EN label, ES label, EN desc, ES desc) ----
ROADMAP=[
  ("Step 02 &middot; Research","Paso 02 &middot; Investigaci&oacute;n",
   "Study a real cereal box in your lane. Learn what makes it stand out on the shelf.",
   "Estudia una caja de cereal real de tu categor&iacute;a. Aprende qu&eacute; la hace resaltar."),
  ("Step 03 &middot; Design Choices","Paso 03 &middot; Decisiones de Dise&ntilde;o",
   "With your partner, pick your cereal name, mascot, colors, and target shopper.",
   "Con tu compa&ntilde;ero, elige el nombre, la mascota, los colores y el p&uacute;blico de tu cereal."),
  ("Step 04 &middot; Concept Sketch","Paso 04 &middot; Boceto del Concepto",
   "Sketch your brand and box by hand. Get your concept approved by your teacher before you go digital.",
   "Dibuja tu marca y tu caja a mano. Tu maestro aprueba tu concepto antes de pasar a lo digital."),
  ("Step 05 &middot; Digital Design","Paso 05 &middot; Dise&ntilde;o Digital",
   "Build your box panels in Adobe Illustrator. Real colors, real type, real polish.",
   "Arma los paneles de tu caja en Adobe Illustrator. Colores reales, tipograf&iacute;a real, buen acabado."),
  ("Step 06 &middot; Social Media","Paso 06 &middot; Redes Sociales",
   "Take your cereal brand to Instagram. Make a post and an animated Story in Canva.",
   "Lleva tu marca a Instagram. Haz una publicaci&oacute;n y una historia animada en Canva."),
  ("Step 07 &middot; Reflection","Paso 07 &middot; Reflexi&oacute;n",
   "Look back at the project. Write about what you learned and what your group did well.",
   "Mira hacia atr&aacute;s. Escribe qu&eacute; aprendiste y qu&eacute; hizo bien tu grupo."),
]

# ---- CTE standards (Chris SA/MA shorthand style) ----
CEREAL_STANDARDS=[
  {"code":"MA.11.1","en_tier":"Media Arts","es_tier":"Artes de Medios",
   "en_title":"Brand Identity","es_title":"Identidad de Marca",
   "en_desc":"You build one clear brand: a name, a mascot, colors, and type that work together.",
   "es_desc":"Construyes una marca clara: un nombre, una mascota, colores y tipograf&iacute;a que combinan."},
  {"code":"MA.11.2","en_tier":"Media Arts","es_tier":"Artes de Medios",
   "en_title":"Package Design","es_title":"Dise&ntilde;o de Empaque",
   "en_desc":"You design the panels of a box so it reads as one product on a store shelf.",
   "es_desc":"Dise&ntilde;as los paneles de una caja para que se vea como un solo producto en el estante."},
  {"code":"MA.11.4","en_tier":"Media Arts","es_tier":"Artes de Medios",
   "en_title":"Digital Tools","es_title":"Herramientas Digitales",
   "en_desc":"You use Adobe Illustrator to build real, print-ready box panels with type and color.",
   "es_desc":"Usas Adobe Illustrator para crear paneles reales, listos para imprimir, con texto y color."},
  {"code":"SA.11.3","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Audience &amp; Message","es_title":"P&uacute;blico y Mensaje",
   "en_desc":"You match every choice to a target shopper so the box communicates and sells.",
   "es_desc":"Haces coincidir cada decisi&oacute;n con un p&uacute;blico meta para que la caja comunique y venda."},
  {"code":"CT.11.5","en_tier":"Career Tech","es_tier":"Carrera T&eacute;cnica",
   "en_title":"Collaboration","es_title":"Colaboraci&oacute;n",
   "en_desc":"You plan and split the work with a partner and deliver one finished box together.",
   "es_desc":"Planeas y divides el trabajo con un compa&ntilde;ero y entregan una caja terminada juntos."},
]

# ---------- local components ----------
def category_grid(es):
    cards=""
    for en_n,es_n,en_d,es_d in CATEGORIES:
        n=es_n if es else en_n; d=es_d if es else en_d
        cards+=('<div style="flex:1 1 44%;min-width:200px;max-width:calc(50% - 7px);background:#0a1414;'
                'border:1px solid rgba(255,255,255,0.08);border-top:2px solid #00b8b8;padding:15px 15px 14px;box-sizing:border-box;">'
                f'<div style="font-size:12.5pt;font-weight:700;letter-spacing:0.03em;text-transform:uppercase;color:#eafeff;">{n}</div>'
                f'<div style="font-size:12.5pt;color:#9fc3c3;margin-top:4px;line-height:1.45;">{d}</div></div>')
    return f'<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:4px;">{cards}</div>'

def roles_split(es):
    if es:
        d1l,d1v="Dise&ntilde;ador 1","Frente &middot; Arriba &middot; Izquierda"
        d2l,d2v="Dise&ntilde;ador 2","Atr&aacute;s &middot; Abajo &middot; Derecha"
        tail="Planeen la marca juntos, luego cada quien dise&ntilde;a sus tres paneles. Usen los mismos colores, tipograf&iacute;as, mascota y logo en los seis paneles para que la caja se vea como una sola marca."
    else:
        d1l,d1v="Designer 1","Front &middot; Top &middot; Left"
        d2l,d2v="Designer 2","Back &middot; Bottom &middot; Right"
        tail="Plan the brand together, then each of you designs your three panels. Use the same colors, fonts, mascot, and logo on all six panels so the box looks like one brand."
    def chip(lbl,val):
        return ('<div style="flex:1 1 220px;background:rgba(0,0,0,0.30);border-left:3px solid #00b8b8;padding:12px 14px;">'
                f'<div style="font-size:10pt;letter-spacing:0.16em;text-transform:uppercase;color:#80e0e0;margin-bottom:6px;"><strong>{lbl}</strong></div>'
                f'<div style="font-size:14pt;color:#ffffff;"><strong>{val}</strong></div></div>')
    return ('<div style="display:flex;flex-wrap:wrap;gap:12px;margin:6px 0 14px;">'
            + chip(d1l,d1v)+chip(d2l,d2v)+'</div>'
            + f'<div style="font-size:13pt;line-height:1.6;color:rgba(255,255,255,0.84);">{tail}</div>')

def onedrive_share(es):
    # Share the working file with a partner over OneDrive, MAC ONLY (Finder, Control-click, Cmd).
    if es:
        head="Comparte Tu Archivo con Tu Compa&ntilde;ero"
        intro="No env&iacute;as el archivo por correo. Lo compartes desde OneDrive y tu compa&ntilde;ero recibe un enlace para abrirlo y editarlo contigo."
        st=[("Busca tu archivo guardado en tu carpeta de <strong>OneDrive</strong> en <strong>Finder</strong>.",""),
            ("Haz <strong>Control-clic</strong> en el archivo y elige <strong>Compartir</strong> (la opci&oacute;n de OneDrive, busca la nube azul).",""),
            ("En la caja que se abre, empieza a escribir el <strong>n&uacute;mero de estudiante</strong> de tu compa&ntilde;ero.",""),
            ("Aparece su <strong>nombre</strong>. Haz clic para agregarlo.",""),
            ("Haz clic en <strong>Enviar</strong>. Tu compa&ntilde;ero recibe un enlace para abrir y editar el archivo contigo.",""),]
    else:
        head="Share Your File With Your Partner"
        intro="You do not email the file. You share it from OneDrive, and your partner gets a link to open and edit it with you."
        st=[("Find your saved file in your <strong>OneDrive</strong> folder in <strong>Finder</strong>.",""),
            ("<strong>Control-click</strong> the file and choose <strong>Share</strong> (the OneDrive option, look for the blue cloud).",""),
            ("In the box that opens, start typing your partner&rsquo;s <strong>student number</strong>.",""),
            ("Their <strong>name</strong> pops up. Click it to add them.",""),
            ("Click <strong>Send</strong>. Your partner gets a link to open and edit the file with you.",""),]
    return (f'<div style="font-size:15pt;color:#ffffff;margin:4px 0 6px;"><strong>{head}</strong></div>'
            + para(intro) + steps(st))

def roadmap_list(es):
    items=[]
    for en_l,es_l,en_d,es_d in ROADMAP:
        items.append((es_l if es else en_l, es_d if es else en_d))
    return bullets(items)

def downloads(es):
    if es:
        heading="Descarga la Carpeta del Proyecto"
        lead=("Toma todo en una carpeta: las <strong>6 plantillas de panel</strong> de Illustrator (Frente, Atr&aacute;s, Arriba, Abajo, Izquierda, Derecha), la "
              "<strong>plantilla de impresi&oacute;n</strong> y tus <strong>3 documentos de Word</strong> (Investigaci&oacute;n, Decisiones de Dise&ntilde;o, Reflexi&oacute;n).")
        lab="Carpeta del Proyecto (ZIP)"
    else:
        heading="Download the Project Folder"
        lead=("Grab everything in one folder: the <strong>6 Illustrator panel templates</strong> (Front, Back, Top, Bottom, Left, Right), the "
              "<strong>Print Template</strong>, and your <strong>3 Word docs</strong> (Research, Design Choices, Reflection).")
        lab="Project Folder (ZIP)"
    rows=('<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
          + (dl_link(PROJECT_ZIP, lab, row=True) if HAVE_ZIP else "")
          + '</div>')
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
          + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
          + para(lead) + rows
          + folder_note(es, AREA)
          + '</div>')

def resources(es):
    if es:
        intro=para("Estos videos y sitios gratis te ayudan en cada paso. &Aacute;brelos en tu tel&eacute;fono o en tu computadora.")
        links=(reslink("https://www.adobe.com/learn/illustrator","Adobe Learn: Illustrator")
               + reslink("https://thedieline.com/","The Dieline")
               + reslink("https://color.adobe.com/create/color-wheel","Rueda de Color de Adobe")
               + reslink("https://www.dafont.com","DaFont"))
        return resources_card("Para Cuando Te Atores", intro+links, es=True)
    intro=para("These free videos and sites help you on every step. Open them on your phone or your laptop.")
    links=(reslink("https://www.adobe.com/learn/illustrator","Adobe Learn: Illustrator")
           + reslink("https://thedieline.com/","The Dieline")
           + reslink("https://color.adobe.com/create/color-wheel","Adobe Color Wheel")
           + reslink("https://www.dafont.com","DaFont"))
    return resources_card("For When You Get Stuck", intro+links, es=False)

def ai_note(es):
    t=("<span style=\"color:#80e0e0;font-style:normal;font-weight:bold;\">&#9432;</span> Algunas im&aacute;genes de esta p&aacute;gina son generadas por IA y no muestran estudiantes reales. Todas las im&aacute;genes son apropiadas para la escuela." if es
       else "<span style=\"color:#80e0e0;font-style:normal;font-weight:bold;\">&#9432;</span> Some images on this page are AI-generated and do not show real students. All images are made to be school appropriate.")
    return ('<div style="margin-top:24px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.10);">'
            f'<div style="font-size:10pt;color:rgba(255,255,255,0.50);line-height:1.55;font-style:italic;">{t}</div></div>')

def vocab_block(es):
    if es:
        ql="ATENCI&Oacute;N: EXAMEN"
        qb="Ver&aacute;s estas seis palabras en un examen corto. Apr&eacute;ndelas ahora y hablar&aacute;s como un dise&ntilde;ador de empaques."
    else:
        ql="HEADS UP: QUIZ"
        qb="You will see these six words on a short quiz. Learn them now and you will talk like a package designer."
    terms=[(v[1] if es else v[0], v[3] if es else v[2]) for v in VOCAB]
    return vocab_grid(ql, qb, terms)

# ---------- nav (mode-aware: "cur" = in-curriculum module, "std" = standalone share copy) ----------
MODE="cur"
FILES_CUR=[OVER,S02,S03,S04,S05,S06,S07]
FILES_STD=["index.html","step02-research.html","step03-design-choices.html","step04-concept-sketch.html",
           "step05-digital-design.html","step06-social-media.html","step07-reflection.html"]
HREFS=FILES_CUR
OVER_LINK=OVER
DT=[("1","Step 01 &middot; Overview"),("2","Step 02 &middot; Research"),("3","Step 03 &middot; Design Choices"),
    ("4","Step 04 &middot; Concept Sketch"),("5","Step 05 &middot; Digital Design"),
    ("6","Step 06 &middot; Social Media"),("7","Step 07 &middot; Reflection")]
def dots_for(active):
    r=""
    for i,(lab,title) in enumerate(DT):
        r+=dot("" if i==active else HREFS[i], lab, title, i==active, module=False)
    return r
def nav(current,dots,stepnav):
    if MODE=="std":
        # Standalone share copy: NO catalog link, nothing links back out. Module name is plain text.
        crumb=('      <div class="silva-breadcrumb">\n'
               '        <span class="bc-current">Cereal Box Group Project</span>\n'
               '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
               f'        <span class="bc-current">{current}</span>\n'
               '      </div>\n')
    else:
        crumb=('      <div class="silva-breadcrumb">\n'
               '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
               '        <span class="bc-sep">&rsaquo;</span>\n'
               f'        <a href="{OVER_LINK}" class="bc-hide-sm">Cereal Box Group Project</a>\n'
               '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
               f'        <span class="bc-current">{current}</span>\n'
               '      </div>\n')
    return (crumb
            + '      <div class="silva-nav-spacer"></div>\n'
            + f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            + f'      <div class="silva-step-nav">{stepnav}</div>')

def wrap_standalone(title, nav_inner, top_html, bottom):
    # Self-contained page: the module's own css + a minimal internal nav, NO silva-nav.js (so no
    # site nav / Equipment Manager / Catalog), NO builder buttons, NO links out. Internal step links
    # only. Language toggle kept (inline JS runs on the hosted page). Assets load absolute from the
    # whitelisted domain so the page works from the /share/ path.
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="icon" type="image/svg+xml" href="https://www.creativesilva.com/logos/CS_Logo_Only.svg" />
  <style>:root {{ --course-accent: #007474; }}</style>
  <link rel="stylesheet" href="https://www.creativesilva.com/css/silva-module.css" />
</head>
<body>
  <nav class="silva-nav" aria-label="Module navigation">
    <div class="silva-nav-inner">
{nav_inner}
    </div>
  </nav>
  <div class="silva-page">
  <div id="silva-module-content">
  {top_html}
  </div>
  {bottom}
  </div>
  <script>
  (function(){{
    var lang=document.querySelector('details.silva-langbar');
    if(!lang){{return;}}
    lang.addEventListener('toggle',function(){{
      if(lang.open){{requestAnimationFrame(function(){{lang.scrollIntoView({{behavior:'smooth',block:'start'}});}});}}
      else{{requestAnimationFrame(function(){{window.scrollTo({{top:0,behavior:'smooth'}});}});}}
    }});
    function bind(sel,op){{var ls=document.querySelectorAll(sel);for(var i=0;i<ls.length;i++){{ls[i].addEventListener('click',function(e){{e.preventDefault();lang.open=op;}});}}}}
    bind('#top a[href="#espanol"]',true);
    bind('#top a[href="#top"]',false);
  }})();
  </script>
</body>
</html>'''

def wrap_page(title, nav_inner, top_html, bottom):
    if MODE=="std":
        return wrap_standalone(title, nav_inner, top_html, bottom)
    return _sf.wrap_page(title, nav_inner, top_html, bottom)

# ---------- overview (Step 01) ----------
def overview():
    # ---- EN ----
    en=banner("Module 10 &bull; Step 01","Cereal Box Group Project",
        "Team up. Build a brand. Win the shelf.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=type_card("overview","The Module Overview","What You Will Make",
        para("You and one partner invent your own brand of cereal. Together you name it, draw a mascot, pick the colors, and design all <strong>six sides</strong> of the box in <strong>Adobe Illustrator</strong>. Make it so good a real shopper would grab it off the shelf.")
        + (framed(HERO,"A row of bright, colorful cereal boxes on a grocery shelf") if HAVE_ART else "")
        + note("<strong>Keep it school appropriate.</strong> Your brand, your name, and your mascot must be clean and okay for school."))
    en+=downloads(False)
    en+=card("Learn &middot; pick a lane","Four Cereal Lanes to Pick From",
        para("Every cereal fits a category. Early on, you and your partner pick <strong>one</strong> of these four lanes for your brand. In Step 02 you study a real box in your lane, and in Step 05 you design your own to match.")
        + category_grid(False)
        + (framed(CATS,"Four cereal categories to pick from: Sugary or Kids, Health or Organic, Protein or Fitness, and Family or Everyday.") if HAVE_ART else ""))
    en+=card("How this group project works","Two Designers, One Box",
        para("You work in a group of two: a Designer 1 and a Designer 2. Together you pick one cereal idea and build one box. You split the six panels, and you plan the brand together.")
        + roles_split(False)
        + note("Every student turns in their own copy on Canvas for each step. No group member skips a submission.")
        + onedrive_share(False))
    en+=card("How It Works / Your Plan","Six Steps to Finish",
        para("Here is your plan. You are on Step 01 now: read this page, pick your lane, and download your project folder. Here are the six steps that follow.")
        + roadmap_list(False))
    en+=resources_card("Key Words", vocab_block(False), es=False)
    en+=standards_box(False, CEREAL_STANDARDS)
    en+=ai_note(False)
    en+=next_up("UP NEXT &middot; STEP 02 - Research","Study a real cereal box in your lane and learn what makes it win the shelf.")
    # ---- ES ----
    es=banner("M&oacute;dulo 10 &bull; Paso 01","Proyecto Grupal: Caja de Cereal",
        "Hagan equipo. Creen una marca. Ganen el estante.","#top","Back to English",hicon=HICON_DESIGN)
    es+=type_card("overview","El Resumen del M&oacute;dulo","Lo Que Vas a Crear",
        para("T&uacute; y un compa&ntilde;ero inventan su propia marca de cereal. Juntos le ponen nombre, dibujan una mascota, eligen los colores y dise&ntilde;an los <strong>seis lados</strong> de la caja en <strong>Adobe Illustrator</strong>. H&aacute;ganla tan buena que un comprador de verdad la tome del estante.")
        + (framed(HERO,"Una fila de cajas de cereal coloridas en un estante de tienda") if HAVE_ART else "")
        + note("<strong>Mant&eacute;nlo apropiado para la escuela.</strong> Tu marca, tu nombre y tu mascota deben ser limpios y adecuados para la clase."))
    es+=downloads(True)
    es+=card("Aprende &middot; elige una categor&iacute;a","Cuatro Categor&iacute;as para Elegir",
        para("Cada cereal tiene una categor&iacute;a. Al inicio, t&uacute; y tu compa&ntilde;ero eligen <strong>una</strong> de estas cuatro para su marca. En el Paso 02 estudias una caja real de tu categor&iacute;a, y en el Paso 05 dise&ntilde;as la tuya para que combine.")
        + category_grid(True)
        + (framed(CATS,"Cuatro categor&iacute;as de cereal para elegir: Azucarado o Ni&ntilde;os, Saludable u Org&aacute;nico, Prote&iacute;na o Fitness, y Familiar o Diario.") if HAVE_ART else ""))
    es+=card("C&oacute;mo funciona este proyecto grupal","Dos Dise&ntilde;adores, Una Caja",
        para("Trabajas en un grupo de dos: un Dise&ntilde;ador 1 y un Dise&ntilde;ador 2. Juntos eligen una idea de cereal y arman una caja. Se dividen los seis paneles y planean la marca juntos.")
        + roles_split(True)
        + note("Cada estudiante entrega su propia copia en Canvas en cada paso. Ning&uacute;n integrante se salta una entrega.")
        + onedrive_share(True))
    es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Seis Pasos para Terminar",
        para("Aqu&iacute; est&aacute; tu plan. Est&aacute;s en el Paso 01 ahora: lee esta p&aacute;gina, elige tu categor&iacute;a y descarga tu carpeta del proyecto. Aqu&iacute; est&aacute;n los seis pasos que siguen.")
        + roadmap_list(True))
    es+=resources_card("Palabras Clave", vocab_block(True), es=True)
    es+=standards_box(True, CEREAL_STANDARDS)
    es+=ai_note(True)
    es+=next_up("SIGUIENTE &middot; PASO 02 - Investigaci&oacute;n","Estudia una caja de cereal real de tu categor&iacute;a y aprende qu&eacute; la hace ganar el estante.")
    return wrap_page(f"Cereal Box Group Project | {CT} | PVHS", nav("Step 01",dots_for(0),step_topnav(0)), top_wrap(en,es), step_bottom(0))

# ---------- step helpers ----------
def subhead(t, color="#80e0e0"):
    return f'<div style="font-size:12.5pt;font-weight:700;color:{color};letter-spacing:0.04em;margin:14px 0 8px;">{t}</div>'

def scroll(inner, rgb="0,184,184"):
    # contained vertical scroller for a long how-to (so it never looks like a tall intimidating stack).
    return (f'<div class="silva-scroll" style="max-height:440px;overflow-y:auto;padding:14px 16px 20px;'
            f'border:1px solid rgba({rgb},0.30);background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, '
            f'rgba(0,0,0,0.14) 88%, rgba({rgb},0.14) 100%);">' + inner + '</div>')

def step_topnav(i):
    p=""
    if i>0: p+=f'<a href="{HREFS[i-1]}" class="silva-step-btn">&#8592; Step {i:02d}</a>'
    if i<len(HREFS)-1: p+=f'<a href="{HREFS[i+1]}" class="silva-step-btn">Step {i+2:02d} &#8594;</a>'
    return p
def step_bottom(i):
    left=(f'<a href="{HREFS[i-1]}" class="silva-bottom-btn">&#8592; Step {i:02d}</a>' if i>0 else '<span></span>')
    right=(f'<a href="{HREFS[i+1]}" class="silva-bottom-btn">Next: Step {i+2:02d} &#8594;</a>' if i<len(HREFS)-1 else '<span></span>')
    return f'<div class="silva-bottom-nav">{left}{right}</div>'

def roles_detail(es):
    if es:
        return para("El Frente lleva el nombre, la mascota y el eslogan. La parte de Arriba es la tapa. La Izquierda lleva un logo peque&ntilde;o y el eslogan. La parte de Atr&aacute;s dice por qu&eacute; tu cereal es especial. La parte de Abajo lleva el c&oacute;digo de barras. La Derecha lleva la informaci&oacute;n nutricional.")
    return para("The Front carries the name, mascot, and tagline. The Top is the lid. The Left holds a small logo and the tagline. The Back tells why your cereal is special. The Bottom holds the barcode. The Right holds the nutrition facts.")

# ---------- Step 02: Research ----------
def research():
    en=banner("Module 10 &bull; Step 02","Cereal Box Research","Pick a real cereal. Study the box. Learn why it sells.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=card("Learn &middot; why designers research","Start Like a Real Designer",
        para("Before you draw a single line, you study what already works. Real designers do this on every project. They look at what is on the shelf and ask why it sells.")
        + para("You and your partner pick <strong>one real cereal</strong> in your category. You study how its box is designed, who it is made for, and how the design helps it sell. Everything you learn here goes into your own brand later."))
    en+=deliverables_box(False,[("1 research doc:","your completed Cereal Box Research doc (.docx), uploaded to this Canvas assignment.")])
    en+=card("How to finish this step","Three Steps to Finish",
        steps([("Pick one cold cereal.","Pick a real cold cereal you can study. Look in your kitchen or use a clear store photo."),
               ("Fill the Research doc.","Open the Research doc from your project folder. Answer every question in full sentences. Add a clear front-of-box photo where the doc asks."),
               ("Save and submit.","Save it to OneDrive, then upload the .docx to this Canvas assignment.")])
        + note("<strong>Name your file:</strong> CerealBoxResearch_LastName_FirstName.docx (example: CerealBoxResearch_Silva_Chris.docx)."))
    en+=card("What the doc asks","The Eight Research Questions",
        para("Here is what the Research doc asks. Answer each one with full sentences.")
        + bullets([("Q1 Cereal Name:","the full name, exactly as it is on the box."),
                   ("Q2 Front Photo:","a clear photo of the front of the box, with the words easy to read."),
                   ("Q3 Official Website:","find the brand&rsquo;s website and paste the link."),
                   ("Q4 Target Audience:","who is it selling to (kids, parents, athletes, busy adults)? Explain why."),
                   ("Q5 Colors &amp; Type:","what colors and fonts does the box use, and what mood do they create?"),
                   ("Q6 Two Competitors:","find two cereals that compete with it. What do they have in common?"),
                   ("Q7 How Design Sells:","how does the box design help it sell? Use words like contrast, typography, and layout."),
                   ("Q8 Your Hot Take:","would you buy it? Why or why not? What would you change?")]))
    en+=card("Score higher","Tips for Strong Answers",
        bullets([("Complete sentences","no one-word answers."),
                 ("Be specific","point at exact words, colors, or pictures on the box."),
                 ("Use art words","drop in contrast, typography, layout, and hierarchy."),
                 ("Connect back","tie every answer to the shopper the cereal is trying to reach.")]))
    en+=next_up("UP NEXT &middot; STEP 03 - Design Choices","Huddle with your partner and lock in your cereal name, mascot, colors, and fonts.")
    es=banner("M&oacute;dulo 10 &bull; Paso 02","Investigaci&oacute;n de la Caja","Elige un cereal real. Estudia la caja. Aprende por qu&eacute; se vende.","#top","Back to English",hicon=HICON_DESIGN)
    es+=card("Aprende &middot; por qu&eacute; se investiga","Empieza Como un Dise&ntilde;ador Real",
        para("Antes de dibujar una sola l&iacute;nea, estudias lo que ya funciona. Los dise&ntilde;adores reales hacen esto en cada proyecto. Miran lo que hay en el estante y preguntan por qu&eacute; se vende.")
        + para("T&uacute; y tu compa&ntilde;ero eligen <strong>un cereal real</strong> de su categor&iacute;a. Estudian c&oacute;mo est&aacute; dise&ntilde;ada su caja, para qui&eacute;n se hizo y c&oacute;mo el dise&ntilde;o ayuda a venderlo. Todo lo que aprendas aqu&iacute; se usa en tu propia marca despu&eacute;s."))
    es+=deliverables_box(True,[("1 documento:","tu documento de Investigaci&oacute;n terminado (.docx), subido a esta tarea de Canvas.")])
    es+=card("C&oacute;mo terminar este paso","Tres Pasos para Terminar",
        steps([("Elige un cereal fr&iacute;o.","Elige un cereal fr&iacute;o real que puedas estudiar. Busca en tu cocina o usa una foto clara de la tienda."),
               ("Llena el documento.","Abre el documento de Investigaci&oacute;n de tu carpeta del proyecto. Contesta cada pregunta en oraciones completas. Agrega una foto clara del frente de la caja donde el documento la pide."),
               ("Guarda y entrega.","Gu&aacute;rdalo en OneDrive, luego sube el .docx a esta tarea de Canvas.")])
        + note("<strong>Nombra tu archivo:</strong> CerealBoxResearch_LastName_FirstName.docx (ejemplo: CerealBoxResearch_Silva_Chris.docx)."))
    es+=card("Qu&eacute; pide el documento","Las Ocho Preguntas",
        para("Esto es lo que pide el documento de Investigaci&oacute;n. Contesta cada una con oraciones completas.")
        + bullets([("P1 Nombre del Cereal:","el nombre completo, tal como est&aacute; en la caja."),
                   ("P2 Foto del Frente:","una foto clara del frente de la caja, con las palabras f&aacute;ciles de leer."),
                   ("P3 Sitio Web Oficial:","busca el sitio web de la marca y pega el enlace."),
                   ("P4 P&uacute;blico Meta:","&iquest;a qui&eacute;n le vende (ni&ntilde;os, pap&aacute;s, deportistas, adultos ocupados)? Explica por qu&eacute;."),
                   ("P5 Colores y Tipograf&iacute;a:","&iquest;qu&eacute; colores y fuentes usa la caja, y qu&eacute; sensaci&oacute;n crean?"),
                   ("P6 Dos Competidores:","busca dos cereales que compitan con este. &iquest;Qu&eacute; tienen en com&uacute;n?"),
                   ("P7 C&oacute;mo Vende el Dise&ntilde;o:","&iquest;c&oacute;mo ayuda el dise&ntilde;o a venderlo? Usa palabras como contraste, tipograf&iacute;a y composici&oacute;n."),
                   ("P8 Tu Opini&oacute;n:","&iquest;lo comprar&iacute;as? &iquest;Por qu&eacute; s&iacute; o por qu&eacute; no? &iquest;Qu&eacute; cambiar&iacute;as?")]))
    es+=card("Sube tu calificaci&oacute;n","Consejos para Buenas Respuestas",
        bullets([("Oraciones completas","nada de respuestas de una palabra."),
                 ("S&eacute; espec&iacute;fico","se&ntilde;ala palabras, colores o im&aacute;genes exactas de la caja."),
                 ("Usa palabras de arte","incluye contraste, tipograf&iacute;a, composici&oacute;n y jerarqu&iacute;a."),
                 ("Conecta","liga cada respuesta con el comprador al que el cereal quiere llegar.")]))
    es+=next_up("SIGUIENTE &middot; PASO 03 - Decisiones de Dise&ntilde;o","J&uacute;ntate con tu compa&ntilde;ero y define el nombre, la mascota, los colores y las fuentes.")
    return wrap_page(f"Step 2: Research | Cereal Box Group Project | {CT} | PVHS", nav("Step 02",dots_for(1),step_topnav(1)), top_wrap(en,es), step_bottom(1))

# ---------- Step 03: Design Choices ----------
def design_choices():
    en=banner("Module 10 &bull; Step 03","Design Choices","Partner huddle. Lock in the name, mascot, colors, and fonts.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=card("Learn &middot; the big choices","Make the Big Choices Together",
        para("Now you and your partner make the big design choices for your box. Agree on the name, the category, the shopper, the mascot, the colors, the fonts, and the tagline.")
        + para("Lock in these choices now so all six panels look like one brand, even though you each design three. Different colors and fonts on each side ruin the brand.")
        + para("You fill out the Design Choices doc so you both leave with the same plan, the same HEX colors, and the same font names."))
    en+=deliverables_box(False,[("1 design doc:","your completed Cereal Box Design Choices doc (.docx), uploaded to this Canvas assignment.")])
    en+=card("How to finish this step","Three Steps to Finish",
        steps([("Partner huddle.","Talk through every choice and decide who is Designer 1 and who is Designer 2. Do not stop until you both agree."),
               ("Fill your own doc.","Every student fills out their own copy. Same answers as your partner. Same HEX codes. Same font names."),
               ("Save and submit.","Save to OneDrive, then upload the .docx to this Canvas assignment.")])
        + note("<strong>Name your file:</strong> CerealBoxDesignChoices_LastName_FirstName.docx."))
    en+=card("What the doc locks in","The Six Group Decisions",
        bullets([("Cereal Name","short, fun, easy to say. Write it exactly how it goes on the box."),
                 ("Target Audience","who is it for? Write the age group and the lifestyle."),
                 ("Mascot","a quick sketch or paragraph of your mascot. Give it a name."),
                 ("Color Palette","pick 3 to 5 colors. Write the HEX code for each. Everyone uses the same codes."),
                 ("Three Fonts","one fun title font, one accent font, one easy-to-read font for small text."),
                 ("Tagline","a short phrase that sells your cereal. Goes on the front.")]))
    en+=card("Group rule","Every Student Turns In Their Own Doc",
        para("This is a group project, but every student turns in their own doc. Same answers as your partner, your own copy. This proves you know the plan, the HEX codes, and the fonts."))
    en+=next_up("UP NEXT &middot; STEP 04 - Concept Sketch","Sketch your three box sides by hand, then get your concept approved before you go digital.")
    es=banner("M&oacute;dulo 10 &bull; Paso 03","Decisiones de Dise&ntilde;o","Re&uacute;nanse. Definan el nombre, la mascota, los colores y las fuentes.","#top","Back to English",hicon=HICON_DESIGN)
    es+=card("Aprende &middot; las grandes decisiones","Tomen las Grandes Decisiones Juntos",
        para("Ahora t&uacute; y tu compa&ntilde;ero toman las grandes decisiones de dise&ntilde;o para su caja. Pongan de acuerdo el nombre, la categor&iacute;a, el comprador, la mascota, los colores, las fuentes y el eslogan.")
        + para("Definan estas decisiones ahora para que los seis paneles se vean como una sola marca, aunque cada uno dise&ntilde;e tres. Colores y fuentes distintos en cada lado arruinan la marca.")
        + para("Llenan el documento de Decisiones de Dise&ntilde;o para que ambos salgan con el mismo plan, los mismos colores HEX y los mismos nombres de fuentes."))
    es+=deliverables_box(True,[("1 documento:","tu documento de Decisiones de Dise&ntilde;o terminado (.docx), subido a esta tarea de Canvas.")])
    es+=card("C&oacute;mo terminar este paso","Tres Pasos para Terminar",
        steps([("Re&uacute;nanse.","Hablen de cada decisi&oacute;n y decidan qui&eacute;n es el Dise&ntilde;ador 1 y qui&eacute;n el Dise&ntilde;ador 2. No paren hasta estar de acuerdo."),
               ("Llena tu propio documento.","Cada estudiante llena su propia copia. Las mismas respuestas que tu compa&ntilde;ero. Los mismos c&oacute;digos HEX. Los mismos nombres de fuentes."),
               ("Guarda y entrega.","Guarda en OneDrive, luego sube el .docx a esta tarea de Canvas.")])
        + note("<strong>Nombra tu archivo:</strong> CerealBoxDesignChoices_LastName_FirstName.docx."))
    es+=card("Qu&eacute; define el documento","Las Seis Decisiones del Grupo",
        bullets([("Nombre del Cereal","corto, divertido, f&aacute;cil de decir. Escr&iacute;belo tal como ir&aacute; en la caja."),
                 ("P&uacute;blico Meta","&iquest;para qui&eacute;n es? Escribe la edad y el estilo de vida."),
                 ("Mascota","un boceto r&aacute;pido o un p&aacute;rrafo de tu mascota. Ponle nombre."),
                 ("Paleta de Colores","elige de 3 a 5 colores. Escribe el c&oacute;digo HEX de cada uno. Todos usan los mismos c&oacute;digos."),
                 ("Tres Fuentes","una fuente divertida para el t&iacute;tulo, una de acento, y una f&aacute;cil de leer para texto peque&ntilde;o."),
                 ("Eslogan","una frase corta que vende tu cereal. Va en el frente.")]))
    es+=card("Regla del grupo","Cada Estudiante Entrega Su Propio Documento",
        para("Este es un proyecto grupal, pero cada estudiante entrega su propio documento. Las mismas respuestas que tu compa&ntilde;ero, tu propia copia. Esto prueba que conoces el plan, los c&oacute;digos HEX y las fuentes."))
    es+=next_up("SIGUIENTE &middot; PASO 04 - Boceto del Concepto","Dibuja a mano tus tres lados de la caja, y luego recibe la aprobaci&oacute;n antes de pasar a lo digital.")
    return wrap_page(f"Step 3: Design Choices | Cereal Box Group Project | {CT} | PVHS", nav("Step 03",dots_for(2),step_topnav(2)), top_wrap(en,es), step_bottom(2))

# ---------- Step 04: Concept Sketch ----------
def concept_sketch():
    en=banner("Module 10 &bull; Step 04","Concept Sketch","Sketch your box sides by hand. Sketch first. Design smarter.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_SKETCH)
    en+=card("Learn &middot; plan before you click","Why You Sketch First",
        para("In this step you sketch a plan for the panels you are designing. This helps you figure out your ideas before you open Adobe Illustrator.")
        + para("You and your partner already picked colors, fonts, and style in Step 03. Now you sketch your three assigned sides so all six sides look like one brand. Real designers sketch every project before they open software."))
    en+=deliverables_box(False,[("1 PDF:","one PDF of your three sketch pages, after your teacher approves them, uploaded to this Canvas assignment.")])
    en+=card("Designer roles","Who Sketches What",
        roles_split(False) + roles_detail(False))
    en+=card("How to finish this step","Three Steps to Finish",
        steps([("Check your sides.","Confirm which three sides are yours before you draw anything."),
               ("Sketch your three sides.","Sketch each side on its own sketchbook page. Show where pictures, text, and the logo go."),
               ("Get approval, then submit.","Show your teacher your sketches for approval. Then scan them to one PDF and upload to Canvas.")])
        + note("<strong>Get your teacher&rsquo;s approval before Step 05.</strong> Show your teacher your sketches in person. No approval means no Illustrator. This saves you from designing in the wrong direction for hours."))
    en+=card("Make your sketch useful","Sketching Tips",
        bullets([("Map it out","show where every piece goes: name, mascot, tagline, bullets, logo. Use boxes to block out space."),
                 ("Add color notes","write the HEX codes from your group palette next to each area."),
                 ("Talk to your partner","make sure your sides feel like the same brand as your partner&rsquo;s."),
                 ("Clear as a map","it does not have to be perfect, but it must be clear. You will use it as a map in Illustrator.")])
        + note("<strong>No scanner needed.</strong> Use your school iPad to take a clear, bright photo of each sketchbook page (this is how you scan it), then save the pages as one PDF."))
    en+=next_up("UP NEXT &middot; STEP 05 - Digital Design","Build your three approved panels in Adobe Illustrator.")
    es=banner("M&oacute;dulo 10 &bull; Paso 04","Boceto del Concepto","Dibuja los lados de tu caja a mano. Boceta primero. Dise&ntilde;a mejor.","#top","Back to English",hicon=HICON_SKETCH)
    es+=card("Aprende &middot; planea antes de hacer clic","Por Qu&eacute; Bocetas Primero",
        para("En este paso dibujas un plan de los paneles que vas a dise&ntilde;ar. Esto te ayuda a resolver tus ideas antes de abrir Adobe Illustrator.")
        + para("T&uacute; y tu compa&ntilde;ero ya eligieron colores, fuentes y estilo en el Paso 03. Ahora dibujas tus tres lados para que los seis lados se vean como una sola marca. Los dise&ntilde;adores reales bocetan cada proyecto antes de abrir el programa."))
    es+=deliverables_box(True,[("1 PDF:","un PDF de tus tres p&aacute;ginas de boceto, despu&eacute;s de que tu maestro las apruebe, subido a esta tarea de Canvas.")])
    es+=card("Roles de dise&ntilde;ador","Qui&eacute;n Dibuja Qu&eacute;",
        roles_split(True) + roles_detail(True))
    es+=card("C&oacute;mo terminar este paso","Tres Pasos para Terminar",
        steps([("Revisa tus lados.","Confirma cu&aacute;les tres lados son tuyos antes de dibujar."),
               ("Dibuja tus tres lados.","Dibuja cada lado en su propia p&aacute;gina del cuaderno. Muestra d&oacute;nde van las im&aacute;genes, el texto y el logo."),
               ("Recibe aprobaci&oacute;n y entrega.","Mu&eacute;strale tus bocetos a tu maestro para que los apruebe. Luego esc&aacute;nealos en un PDF y s&uacute;belo a Canvas.")])
        + note("<strong>Recibe la aprobaci&oacute;n de tu maestro antes del Paso 05.</strong> Mu&eacute;strale tus bocetos en persona. Sin aprobaci&oacute;n no hay Illustrator. Esto te evita dise&ntilde;ar en la direcci&oacute;n equivocada por horas."))
    es+=card("Haz &uacute;til tu boceto","Consejos para Bocetar",
        bullets([("Ubica todo","muestra d&oacute;nde va cada parte: nombre, mascota, eslogan, vi&ntilde;etas, logo. Usa cajas para bloquear el espacio."),
                 ("Agrega notas de color","escribe los c&oacute;digos HEX de la paleta de tu grupo junto a cada &aacute;rea."),
                 ("Habla con tu compa&ntilde;ero","aseg&uacute;rate de que tus lados se sientan de la misma marca que los de tu compa&ntilde;ero."),
                 ("Claro como un mapa","no tiene que ser perfecto, pero debe ser claro. Lo usar&aacute;s como mapa en Illustrator.")])
        + note("<strong>No se necesita esc&aacute;ner.</strong> Usa tu iPad de la escuela para tomar una foto clara y brillante de cada p&aacute;gina del cuaderno (as&iacute; la escaneas), luego guarda las p&aacute;ginas en un solo PDF."))
    es+=next_up("SIGUIENTE &middot; PASO 05 - Dise&ntilde;o Digital","Arma tus tres paneles aprobados en Adobe Illustrator.")
    return wrap_page(f"Step 4: Concept Sketch | Cereal Box Group Project | {CT} | PVHS", nav("Step 04",dots_for(3),step_topnav(3)), top_wrap(en,es), step_bottom(3))

# ---------- Step 05: Digital Design ----------
def digital_design():
    en=banner("Module 10 &bull; Step 05","Digital Design","Design. Export. Build the print template.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=card("Learn &middot; from sketch to Illustrator","Build the Real Thing",
        para("Your sketches are approved. Now you build the final cereal box in <strong>Adobe Illustrator</strong>. You design only the three sides you were assigned. You and your partner share JPG exports so you both build the same print template.")
        + para("When you finish, you print the box on thick paper, then cut, fold, and build a real product."))
    en+=deliverables_box(False,[("4 PDFs:","the print template plus the three panels you designed. Export each as a PDF and upload all four to this Canvas assignment.")],files=4)
    en+=card("Open your project folder","Start From Your Templates",
        para("Open the project folder you downloaded on the module Overview. Inside the Templates folder are all 6 blank panel files and the print template. If you skipped it, go back to the Overview and download the Project Folder first."))
    en+=card("Designer roles","Who Designs What",
        roles_split(False)
        + para("Designer 1 opens the Front, Top, and Left panel files. Designer 2 opens the Back, Bottom, and Right panel files."))
    en+=card("Design rules","Make It Match Your Partner",
        para("You only do your three panels, but you work with your partner so the whole box looks like one product.")
        + bullets([("Same HEX, same fonts","use the exact colors and fonts from your Step 03 doc. No swapping mid-design."),
                   ("Visual hierarchy","the most important info is the biggest and boldest; less important info is smaller."),
                   ("Clean and readable","keep small words easy to read on the real printed box."),
                   ("Make it look real","treat it like a real product and a real job.")])
        + para("Use <strong>MagicSchool AI</strong> to draft fun text for your box, then edit it to match your brand voice. Use <strong>Adobe Firefly</strong> or <strong>Photoshop</strong> for images, then place them into your Illustrator panel."))
    en+=card("Panel contents","What Goes on Each Side",
        bullets([("Front","cereal name or logo, company name, tagline, main claim, and the mascot or a big main image."),
                 ("Back","a short story or mission, bullet points (no long paragraphs), a small logo, and an optional game or QR code."),
                 ("Top","sell-by date, a small logo, and the tagline."),
                 ("Bottom","barcode, company name, and basic product info."),
                 ("Right","a small logo and the nutrition facts (make the image high-quality so it is easy to read)."),
                 ("Left","a small logo, the tagline, and extra fun details.")]))
    en+=card("How to export","Save It the Right Way",
        scroll(subhead("Part A: Export each panel as a JPG (to share with your partner)")
            + steps([("Open your finished panel file (.ai) in Adobe Illustrator.",""),
                     ("Top menu: File &rarr; Export &rarr; Export As.",""),
                     ("Change the format to JPEG (.jpg).",""),
                     ("Check <strong>Use Artboards</strong>, so only what is inside your artboard exports.",""),
                     ("Save inside your project folder, then click Export.",""),
                     ("In JPEG Options set Color Model CMYK, Quality 10 (Maximum), and Resolution High (300 ppi). Click OK.","")])
            + subhead("Part B: Build the print template and export your PDFs")
            + steps([("Share your JPGs with your partner and get theirs, so you both have all six panels.",""),
                     ("Open the print template and place each panel JPG in its spot.",""),
                     ("Export the print template as a PDF (File &rarr; Save As &rarr; Adobe PDF, Press Quality).",""),
                     ("Export your three panels as PDFs the same way.",""),
                     ("Upload all four PDFs to this Canvas assignment.","")])))
    en+=next_up("UP NEXT &middot; STEP 06 - Social Media","Take your finished brand to Instagram with a post and an animated Story.")
    es=banner("M&oacute;dulo 10 &bull; Paso 05","Dise&ntilde;o Digital","Dise&ntilde;a. Exporta. Arma la plantilla de impresi&oacute;n.","#top","Back to English",hicon=HICON_DESIGN)
    es+=card("Aprende &middot; del boceto a Illustrator","Arma lo Real",
        para("Tus bocetos est&aacute;n aprobados. Ahora armas la caja final en <strong>Adobe Illustrator</strong>. Dise&ntilde;as solo los tres lados que te tocaron. T&uacute; y tu compa&ntilde;ero comparten exportaciones JPG para armar la misma plantilla de impresi&oacute;n.")
        + para("Cuando termines, imprimes la caja en papel grueso, luego cortas, doblas y armas un producto real."))
    es+=deliverables_box(True,[("4 PDFs:","la plantilla de impresi&oacute;n m&aacute;s los tres paneles que dise&ntilde;aste. Exporta cada uno como PDF y sube los cuatro a esta tarea de Canvas.")],files=4)
    es+=card("Abre tu carpeta del proyecto","Empieza con Tus Plantillas",
        para("Abre la carpeta del proyecto que descargaste en el Resumen del m&oacute;dulo. Dentro de la carpeta Templates est&aacute;n los 6 paneles en blanco y la plantilla de impresi&oacute;n. Si te la saltaste, regresa al Resumen y descarga la Carpeta del Proyecto primero."))
    es+=card("Roles de dise&ntilde;ador","Qui&eacute;n Dise&ntilde;a Qu&eacute;",
        roles_split(True)
        + para("El Dise&ntilde;ador 1 abre los paneles de Frente, Arriba e Izquierda. El Dise&ntilde;ador 2 abre los paneles de Atr&aacute;s, Abajo y Derecha."))
    es+=card("Reglas de dise&ntilde;o","Haz Que Combine con Tu Compa&ntilde;ero",
        para("Solo haces tus tres paneles, pero trabajas con tu compa&ntilde;ero para que toda la caja se vea como un solo producto.")
        + bullets([("Mismo HEX, mismas fuentes","usa los colores y fuentes exactos de tu documento del Paso 03. No los cambies a medias."),
                   ("Jerarqu&iacute;a visual","lo m&aacute;s importante es lo m&aacute;s grande y llamativo; lo menos importante es m&aacute;s peque&ntilde;o."),
                   ("Limpio y legible","que las palabras peque&ntilde;as se lean f&aacute;cil en la caja impresa."),
                   ("Que se vea real","tr&aacute;talo como un producto real y un trabajo real.")])
        + para("Usa <strong>MagicSchool AI</strong> para redactar texto divertido, luego ed&iacute;talo para que combine con la voz de tu marca. Usa <strong>Adobe Firefly</strong> o <strong>Photoshop</strong> para im&aacute;genes, luego col&oacute;calas en tu panel de Illustrator."))
    es+=card("Contenido de los paneles","Qu&eacute; Va en Cada Lado",
        bullets([("Frente","nombre del cereal o logo, nombre de la compa&ntilde;&iacute;a, eslogan, afirmaci&oacute;n principal, y la mascota o una imagen grande."),
                 ("Atr&aacute;s","una historia o misi&oacute;n corta, vi&ntilde;etas (sin p&aacute;rrafos largos), un logo peque&ntilde;o y un juego o c&oacute;digo QR opcional."),
                 ("Arriba","fecha de caducidad, un logo peque&ntilde;o y el eslogan."),
                 ("Abajo","c&oacute;digo de barras, nombre de la compa&ntilde;&iacute;a e informaci&oacute;n b&aacute;sica."),
                 ("Derecha","un logo peque&ntilde;o y la informaci&oacute;n nutricional (que la imagen sea de alta calidad para leerla f&aacute;cil)."),
                 ("Izquierda","un logo peque&ntilde;o, el eslogan y detalles divertidos extra.")]))
    es+=card("C&oacute;mo exportar","Gu&aacute;rdalo Bien",
        scroll(subhead("Parte A: Exporta cada panel como JPG (para compartir con tu compa&ntilde;ero)")
            + steps([("Abre tu panel terminado (.ai) en Adobe Illustrator.",""),
                     ("Men&uacute; superior: Archivo &rarr; Exportar &rarr; Exportar como.",""),
                     ("Cambia el formato a JPEG (.jpg).",""),
                     ("Marca <strong>Usar mesas de trabajo</strong>, para exportar solo lo que est&aacute; dentro de tu mesa de trabajo.",""),
                     ("Guarda dentro de tu carpeta del proyecto, luego haz clic en Exportar.",""),
                     ("En Opciones JPEG elige Modelo de color CMYK, Calidad 10 (M&aacute;xima) y Resoluci&oacute;n Alta (300 ppp). Haz clic en OK.","")])
            + subhead("Parte B: Arma la plantilla de impresi&oacute;n y exporta tus PDFs")
            + steps([("Comparte tus JPG con tu compa&ntilde;ero y recibe los suyos, para que ambos tengan los seis paneles.",""),
                     ("Abre la plantilla de impresi&oacute;n y coloca cada panel JPG en su lugar.",""),
                     ("Exporta la plantilla como PDF (Archivo &rarr; Guardar como &rarr; Adobe PDF, Calidad de prensa).",""),
                     ("Exporta tus tres paneles como PDF de la misma manera.",""),
                     ("Sube los cuatro PDF a esta tarea de Canvas.","")])))
    es+=next_up("SIGUIENTE &middot; PASO 06 - Redes Sociales","Lleva tu marca terminada a Instagram con una publicaci&oacute;n y una historia animada.")
    return wrap_page(f"Step 5: Digital Design | Cereal Box Group Project | {CT} | PVHS", nav("Step 05",dots_for(4),step_topnav(4)), top_wrap(en,es), step_bottom(4))

# ---------- Step 06: Social Media ----------
def social_media():
    en=banner("Module 10 &bull; Step 06","Social Media","Take your cereal brand to Instagram.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_DESIGN)
    en+=card("Learn &middot; sell it online","Sell Your Cereal Online",
        para("Your cereal box is built. Now you sell it online. Real brands do not stop at the box. They post on Instagram to get people excited.")
        + para("You make two Instagram pieces for your brand: a short <strong>animated Story</strong> and a square <strong>Post</strong>. You build them in <strong>Canva</strong>. Use the same brand from Step 05: the same name, logo, colors, fonts, and mascot."))
    en+=deliverables_box(False,[("Animated Story (.mp4):","a 5 to 15 second Instagram Story, 1080 x 1920, with at least one thing that moves."),
                                ("Instagram Post (.jpg):","one clean square image, 1080 x 1080, with your cereal, your logo, and one clear message.")])
    en+=card("Build it in Canva","Your One Tool",
        para("Canva is free with your school Google login. It has ready-made Instagram sizes, animation tools, and fonts.")
        + steps([("Log in.","Go to canva.com and click Log in with Google. Use your school account."),
                 ("Upload your brand.","In the Uploads tab, add your logo, mascot, and box images from Step 05."),
                 ("Build the Story.","Create an Instagram Story (1080 x 1920). Add your name, logo, one image, and a call to action."),
                 ("Animate it.","Click an element, then Animate, so your text or logo moves. Keep it 5 to 15 seconds."),
                 ("Build the Post.","Create an Instagram Post (1080 x 1080). One clean image with your cereal, logo, and one clear message."),
                 ("Export the Story.","Share, then Download, then pick MP4 Video. Name it LastName_Cereal_Story.mp4."),
                 ("Export the Post.","Share, then Download, then pick JPG. Name it LastName_Cereal_Post.jpg."),
                 ("Submit both.","Upload your MP4 and your JPG to this Canvas assignment in one submission.")]))
    en+=card("Pro tip","Give People a Call to Action",
        para("A call to action tells the viewer what to do next. It is short and easy to see. Both your Story and your Post need one.")
        + bullets([("","&ldquo;Try it today.&rdquo;"),("","&ldquo;Find it at your store.&rdquo;"),("","&ldquo;Follow for more.&rdquo;"),("","&ldquo;New flavor, out now.&rdquo;")]))
    en+=card("Stay on brand","Use Your Own Cereal Brand",
        bullets([("Same logo","use the exact logo from your box."),
                 ("Same colors","use the same HEX colors from your Step 03 doc."),
                 ("Same fonts","pick Canva fonts that match your box style."),
                 ("Same mascot","if your box has a mascot, put it in your posts too.")]))
    en+=next_up("UP NEXT &middot; STEP 07 - Reflection","Look back at the project and write about what you learned.")
    es=banner("M&oacute;dulo 10 &bull; Paso 06","Redes Sociales","Lleva tu marca de cereal a Instagram.","#top","Back to English",hicon=HICON_DESIGN)
    es+=card("Aprende &middot; v&eacute;ndelo en l&iacute;nea","Vende Tu Cereal en L&iacute;nea",
        para("Tu caja de cereal est&aacute; lista. Ahora la vendes en l&iacute;nea. Las marcas reales no paran en la caja. Publican en Instagram para emocionar a la gente.")
        + para("Haces dos piezas de Instagram para tu marca: una <strong>historia animada</strong> corta y una <strong>publicaci&oacute;n</strong> cuadrada. Las armas en <strong>Canva</strong>. Usa la misma marca del Paso 05: el mismo nombre, logo, colores, fuentes y mascota."))
    es+=deliverables_box(True,[("Historia animada (.mp4):","una historia de Instagram de 5 a 15 segundos, 1080 x 1920, con al menos algo que se mueva."),
                               ("Publicaci&oacute;n (.jpg):","una imagen cuadrada limpia, 1080 x 1080, con tu cereal, tu logo y un mensaje claro.")])
    es+=card("Arma en Canva","Tu &Uacute;nica Herramienta",
        para("Canva es gratis con tu cuenta Google de la escuela. Tiene tama&ntilde;os de Instagram listos, herramientas de animaci&oacute;n y fuentes.")
        + steps([("Inicia sesi&oacute;n.","Ve a canva.com y haz clic en Iniciar sesi&oacute;n con Google. Usa tu cuenta de la escuela."),
                 ("Sube tu marca.","En la pesta&ntilde;a Subidas, agrega tu logo, mascota e im&aacute;genes de la caja del Paso 05."),
                 ("Arma la historia.","Crea una historia de Instagram (1080 x 1920). Agrega tu nombre, logo, una imagen y un llamado a la acci&oacute;n."),
                 ("Anim&aacute;la.","Haz clic en un elemento, luego Animar, para que tu texto o logo se mueva. Mant&eacute;nla de 5 a 15 segundos."),
                 ("Arma la publicaci&oacute;n.","Crea una publicaci&oacute;n de Instagram (1080 x 1080). Una imagen limpia con tu cereal, logo y un mensaje claro."),
                 ("Exporta la historia.","Compartir, luego Descargar, luego elige Video MP4. Nombra: LastName_Cereal_Story.mp4."),
                 ("Exporta la publicaci&oacute;n.","Compartir, luego Descargar, luego elige JPG. Nombra: LastName_Cereal_Post.jpg."),
                 ("Entrega ambos.","Sube tu MP4 y tu JPG a esta tarea de Canvas en una sola entrega.")]))
    es+=card("Consejo","Dale a la Gente un Llamado a la Acci&oacute;n",
        para("Un llamado a la acci&oacute;n le dice al espectador qu&eacute; hacer. Es corto y f&aacute;cil de ver. Tu historia y tu publicaci&oacute;n necesitan uno.")
        + bullets([("","&ldquo;Pru&eacute;balo hoy.&rdquo;"),("","&ldquo;B&uacute;scalo en tu tienda.&rdquo;"),("","&ldquo;S&iacute;guenos para m&aacute;s.&rdquo;"),("","&ldquo;Nuevo sabor, ya disponible.&rdquo;")]))
    es+=card("Mant&eacute;n la marca","Usa Tu Propia Marca de Cereal",
        bullets([("Mismo logo","usa el logo exacto de tu caja."),
                 ("Mismos colores","usa los mismos colores HEX de tu documento del Paso 03."),
                 ("Mismas fuentes","elige fuentes de Canva que combinen con el estilo de tu caja."),
                 ("Misma mascota","si tu caja tiene mascota, ponla tambi&eacute;n en tus publicaciones.")]))
    es+=next_up("SIGUIENTE &middot; PASO 07 - Reflexi&oacute;n","Mira hacia atr&aacute;s y escribe qu&eacute; aprendiste.")
    return wrap_page(f"Step 6: Social Media | Cereal Box Group Project | {CT} | PVHS", nav("Step 06",dots_for(5),step_topnav(5)), top_wrap(en,es), step_bottom(5))

# ---------- Step 07: Reflection ----------
def reflection():
    en=banner("Module 10 &bull; Step 07","Project Reflection","Reflect. Learn. Grow.","#espanol","Clic para Espa&ntilde;ol",hicon=HICON_REFLECT)
    en+=card("Learn &middot; look back","Look Back at What You Built",
        para("You finished your cereal box. Now think about how the project went. Real designers do this at the end of every job.")
        + para("You fill out a reflection doc. Write about your design choices, how you and your partner worked together, and what you learned. Be honest. Be specific."))
    en+=deliverables_box(False,[("1 reflection:","your completed Cereal Box Reflection doc (.docx), uploaded to this Canvas assignment.")])
    en+=card("How to finish this step","Three Steps to Finish",
        steps([("Open the reflection doc.","Open the Reflection doc from your project folder."),
               ("Answer every prompt.","Read each prompt and write in full sentences. No one-word answers."),
               ("Save and submit.","Save with your name in the file title, then upload the .docx to this Canvas assignment.")])
        + note("<strong>Name your file:</strong> CerealBoxReflection_LastName_FirstName.docx."))
    en+=card("Preview of the prompts","Six Things to Reflect On",
        bullets([("My design choices","what choices did you make on your panels, and why those colors, fonts, or images?"),
                 ("What went right","what part went best, and why did it work?"),
                 ("What I would change","if you could redo one thing on your box, what would it be and why?"),
                 ("Partner wins","what did you and your partner do well together? Name something specific."),
                 ("What was hard","what was the hardest part, and how did you handle it?"),
                 ("Real-world connect","how is what you did the same as a real package designer&rsquo;s job?")]))
    en+=next_up("MODULE COMPLETE","Nice work. You built a real brand, designed a six-panel box, and took it to social media, just like a working package designer.")
    es=banner("M&oacute;dulo 10 &bull; Paso 07","Reflexi&oacute;n del Proyecto","Reflexiona. Aprende. Crece.","#top","Back to English",hicon=HICON_REFLECT)
    es+=card("Aprende &middot; mira hacia atr&aacute;s","Mira lo Que Construiste",
        para("Terminaste tu caja de cereal. Ahora piensa en c&oacute;mo fue el proyecto. Los dise&ntilde;adores reales hacen esto al final de cada trabajo.")
        + para("Llenas un documento de reflexi&oacute;n. Escribe sobre tus decisiones de dise&ntilde;o, c&oacute;mo trabajaron t&uacute; y tu compa&ntilde;ero, y qu&eacute; aprendiste. S&eacute; honesto. S&eacute; espec&iacute;fico."))
    es+=deliverables_box(True,[("1 reflexi&oacute;n:","tu documento de Reflexi&oacute;n terminado (.docx), subido a esta tarea de Canvas.")])
    es+=card("C&oacute;mo terminar este paso","Tres Pasos para Terminar",
        steps([("Abre el documento de reflexi&oacute;n.","Abre el documento de Reflexi&oacute;n de tu carpeta del proyecto."),
               ("Contesta cada pregunta.","Lee cada pregunta y escribe en oraciones completas. Nada de respuestas de una palabra."),
               ("Guarda y entrega.","Guarda con tu nombre en el t&iacute;tulo del archivo, luego sube el .docx a esta tarea de Canvas.")])
        + note("<strong>Nombra tu archivo:</strong> CerealBoxReflection_LastName_FirstName.docx."))
    es+=card("Vista previa de las preguntas","Seis Cosas para Reflexionar",
        bullets([("Mis decisiones de dise&ntilde;o","&iquest;qu&eacute; decisiones tomaste en tus paneles, y por qu&eacute; esos colores, fuentes o im&aacute;genes?"),
                 ("Qu&eacute; sali&oacute; bien","&iquest;qu&eacute; parte sali&oacute; mejor, y por qu&eacute; funcion&oacute;?"),
                 ("Qu&eacute; cambiar&iacute;a","si pudieras rehacer una cosa de tu caja, &iquest;qu&eacute; ser&iacute;a y por qu&eacute;?"),
                 ("Logros con tu compa&ntilde;ero","&iquest;qu&eacute; hicieron bien juntos? Nombra algo espec&iacute;fico."),
                 ("Qu&eacute; fue dif&iacute;cil","&iquest;cu&aacute;l fue la parte m&aacute;s dif&iacute;cil, y c&oacute;mo la resolviste?"),
                 ("Conexi&oacute;n real","&iquest;en qu&eacute; se parece tu trabajo al de un dise&ntilde;ador de empaques real?")]))
    es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Creaste una marca real, dise&ntilde;aste una caja de seis paneles y la llevaste a las redes sociales, como un dise&ntilde;ador de empaques profesional.")
    return wrap_page(f"Step 7: Reflection | Cereal Box Group Project | {CT} | PVHS", nav("Step 07",dots_for(6),step_topnav(6)), top_wrap(en,es), step_bottom(6))

# ================= BUILD =================
PAGES=[overview,research,design_choices,concept_sketch,digital_design,social_media,reflection]
def _check(fname, html):
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    assert "–" not in html and "&ndash;" not in html, "en dash in "+fname
    ban_check(html, fname)

# Pass 1: in-curriculum module (catalog breadcrumb + site nav via silva-nav.js).
MODE="cur"; HREFS=FILES_CUR; OVER_LINK=OVER
for gen,fname in zip(PAGES,FILES_CUR):
    html=ent(gen()); _check(fname,html)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote cur", fname, len(html))

# Pass 2: standalone shareable copy (no catalog, no site nav, internal links only).
MODE="std"; HREFS=FILES_STD; OVER_LINK="index.html"
SHARE_DIR=os.path.join(ROOT,"share/cereal-box"); os.makedirs(SHARE_DIR,exist_ok=True)
for gen,fname in zip(PAGES,FILES_STD):
    html=ent(gen()); _check(fname,html)
    open(os.path.join(SHARE_DIR,fname),"w",encoding="utf-8").write(html)
    print("wrote std", fname, len(html))
