#!/usr/bin/env python3
# Photography 1A - Project 02: Master Photographer.
# Pick one master photographer from a roster of 20 (4 genres), study HOW they make images,
# then capture and edit three of your own photos in that style and present master + student work
# side by side in a PowerPoint. Standard photo arc: study -> capture & contact -> cull & edit ->
# presentation (reflection is the PowerPoint's closing page). Five pages, bilingual EN/ES, 5th-grade.
# Dark teal angular framework via silva_framework. Camera-kit capture (no fresh-photos note).
# Points 15 / 25 / 25 / 35. Photo 1 only for now; Photo 2 is a separate pass later.
#
# Hard rules honored: NO em dashes, NO banned violence words (use capture / take photos / photograph);
# image selections are "selections", never "picks"; Mac-only how-to; all assets
# on www.creativesilva.com. Placement label is "Project 02" (mirrors The Important Person Project =
# Project 01); to make it "Module 13" instead, change PROJ_KIND / PROJNUM below and the catalog label.
import os
from silva_framework import *   # shared angular chrome: banner, cards, sections, vocab, deliverables, standards
import silva_framework as _sf    # for the original wrap_page (the std pass overrides wrap_page locally)

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"
HICON_CAMERA_KIT=f"{SITE}/assets/Icons/assignment/camera-kit-white-v1.png"

# Local ent: accents -> entities AND en-dash -> plain hyphen (never emit &ndash;, per the hard dash ban).
def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

PROJNUM="02"            # catalog label is "Project 02" in BOTH courses (Fall Final Project)
# Student-facing banner eyebrow (Chris 2026-11-15: this is the Fall Final Project).
PROJ_LABEL="Fall Final Project"
PROJ_LABEL_ES="Proyecto Final de Oto&ntilde;o"
IMGDIR=f"{SITE}/assets/images/master-photographer"
TPLDIR=f"{SITE}/assets/templates/master-photographer"
HERO=f"{IMGDIR}/master-photographer-hero-v2.jpg"
RESEARCH_FLOAT=f"{IMGDIR}/research-float-v1.jpg"       # Step 02 (student researching at the iMac)
CULL_FLOAT=f"{IMGDIR}/cull-float-v1.jpg"               # Step 04 (student with her three selected prints)
PRESENT_FLOAT=f"{IMGDIR}/presentation-float-v1.jpg"    # Step 05 (student presenting selected works)
# Contact-sheet presets are installed once (Image Series module); install is easy, no video.

# Two courses, one module (Chris 2026-11-16). Each course hosts its OWN project-folder ZIP on its
# OWN Overview, and the Overview is the ONLY download host (no standalone deck .pptx anywhere). The
# deck now lives only inside that ZIP (English + Spanish). Each course's deck preview is rendered
# from Chris's current deck (gray MY WORK header, correct course label on the cover). Photo 2 adds
# the growth / no-repeat disclaimer. The Drive project folders are completed + zipped into TPLDIR by
# hand; see the Master Photographer project memory. The std/share pass is built from Photo 1.
COURSES=[
 {"prefix":"photo1","cl":"Photography 1A","p2":False,
  "zip_en":f"{TPLDIR}/Master-Photographer-Photo-1-Project-Folder-EN.zip",
  "zip_es":f"{TPLDIR}/Master-Photographer-Photo-1-Project-Folder-ES.zip",
  "deck_preview":f"{IMGDIR}/deck-template-preview-v2.jpg"},
 {"prefix":"photo2","cl":"Photography 2A","p2":True,
  "zip_en":f"{TPLDIR}/Master-Photographer-Photo-2-Project-Folder-EN.zip",
  "zip_es":f"{TPLDIR}/Master-Photographer-Photo-2-Project-Folder-ES.zip",
  "deck_preview":f"{IMGDIR}/deck-template-preview-photo2-v1.jpg"},
]

HAVE_HERO=True
HAVE_RESEARCH=True
HAVE_CULL=True
HAVE_PRESENT=True
HAVE_DECK_PREVIEW=True

# Real standards (NCAS Media Arts + CA CTE Arts, Media & Entertainment), plain-language for students.
STANDARDS=[
  {"code":"MA:Re8.1.HSI","en_tier":"NCAS Media Arts","es_tier":"Artes de Medios NCAS",
   "en_title":"Analyze &amp; Interpret","es_title":"Analizar e Interpretar",
   "en_desc":"You study a master photographer&rsquo;s images and explain the techniques they use and the message their work sends.",
   "es_desc":"Estudias las im&aacute;genes de un fot&oacute;grafo maestro y explicas las t&eacute;cnicas que usa y el mensaje que env&iacute;a su trabajo."},
  {"code":"MA:Cr1.1.HSI","en_tier":"NCAS Media Arts","es_tier":"Artes de Medios NCAS",
   "en_title":"Generate &amp; Plan Ideas","es_title":"Generar y Planear Ideas",
   "en_desc":"You gather three images from your master photographer and plan your own photos inspired by their style.",
   "es_desc":"Re&uacute;nes tres im&aacute;genes de tu fot&oacute;grafo maestro y planeas tus propias fotos inspiradas en su estilo."},
  {"code":"MA:Cr3.1.HSI","en_tier":"NCAS Media Arts","es_tier":"Artes de Medios NCAS",
   "en_title":"Capture, Refine &amp; Finish","es_title":"Capturar, Refinar y Terminar",
   "en_desc":"You capture a full take, then cull and edit down to your three strongest finished images.",
   "es_desc":"Capturas una toma completa, luego seleccionas y editas hasta tus tres im&aacute;genes finales m&aacute;s fuertes."},
  {"code":"MA:Pr6.1.HSI","en_tier":"NCAS Media Arts","es_tier":"Artes de Medios NCAS",
   "en_title":"Present &amp; Share","es_title":"Presentar y Compartir",
   "en_desc":"You build a PowerPoint and present it to the class, showing how your photos connect to your master photographer.",
   "es_desc":"Creas un PowerPoint y lo presentas a la clase, mostrando c&oacute;mo tus fotos se conectan con tu fot&oacute;grafo maestro."},
  {"code":"CTE AME A4.0","en_tier":"CA CTE, Arts Media &amp; Entertainment","es_tier":"CTE de California, Artes y Medios",
   "en_title":"Analyze &amp; Assess Work","es_title":"Analizar y Evaluar el Trabajo",
   "en_desc":"You judge photographs using the elements of art, the principles of design, and professional industry standards.",
   "es_desc":"Juzgas fotograf&iacute;as usando los elementos del arte, los principios del dise&ntilde;o y los est&aacute;ndares profesionales de la industria."},
]

VOCAB_EN=[
 ("Full Take","A photographer&rsquo;s &lsquo;take&rsquo; is all the photos they capture for one project. Your full take is every photo, before you cull."),
 ("Contact Sheet","One page that shows many photos as small thumbnails, so you can see your whole take at a glance."),
 ("Cull","To go through your take and keep your strongest photos, letting the rest go."),
 ("Export","To save your edited photos out of Lightroom as new files, like high-resolution JPGs, that you can turn in."),
 ("The Decisive Moment","The exact instant when everything in the frame lines up into one strong photo. Henri Cartier-Bresson made this idea famous."),
 ("Influence","When one artist&rsquo;s style shapes another artist&rsquo;s work. Your master photographer influences your three photos."),
]
VOCAB_ES=[
 ("Full Take (Toma Completa)","La &lsquo;toma&rsquo; de un fot&oacute;grafo son todas las fotos que captura para un proyecto. Tu toma completa es cada foto, antes de seleccionar."),
 ("Contact Sheet (Hoja de Contactos)","Una p&aacute;gina que muestra muchas fotos como miniaturas peque&ntilde;as, para ver toda tu toma de un vistazo."),
 ("Cull (Seleccionar)","Revisar tu toma y quedarte con tus fotos m&aacute;s fuertes, dejando ir el resto."),
 ("Export (Exportar)","Guardar tus fotos editadas fuera de Lightroom como archivos nuevos, como JPG de alta resoluci&oacute;n, que puedes entregar."),
 ("The Decisive Moment (El Momento Decisivo)","El instante exacto en que todo en el encuadre se alinea en una sola foto fuerte. Henri Cartier-Bresson hizo famosa esta idea."),
 ("Influence (Influencia)","Cuando el estilo de un artista da forma al trabajo de otro. Tu fot&oacute;grafo maestro influye en tus tres fotos."),
]

# ---------------- The master photographers (20, grouped by genre) ----------------
# Students choose ONE from this roster. 4 genre groups x 5 = 20. Names are proper nouns (shared
# EN/ES); only the genre label swaps. Rebuilt 2026-11-16 from Chris's original "Master
# Photographer List" Canvas page (the full roster, restored into the current module).
ROSTER=[
 ("Landscape","Paisaje",["Ansel Adams","Robert Adams","Stephen Shore","Richard Misrach","Paul Strand"]),
 ("Portrait","Retrato",["Annie Leibovitz","Martin Schoeller","Platon","Brandon Stanton","Chris Buck"]),
 ("Still Life","Naturaleza Muerta",["Karl Blossfeldt","Irving Penn","Jan Groover","Josef Sudek","Laura Letinsky"]),
 ("On Location","En Locaci&oacute;n",["Joe McNally","Henri Cartier-Bresson","Scott Kelby","Lara Jade","Sebasti&atilde;o Salgado"]),
]

GENERAL_SITES=[
 ("https://www.artsy.net/","Artsy.net"),
 ("https://www.moma.org/","MoMA.org"),
 ("https://www.magnumphotos.com/","MagnumPhotos.com"),
 ("https://www.tate.org.uk/","Tate.org.uk"),
 ("https://www.getty.edu/","Getty.edu"),
]

# ---------------- Student rubric (collapsed gold accordion on the Overview) ----------------
WORKSHEET_GOLD=f"{SITE}/assets/Icons/assignment/worksheet-gold-v1.svg"   # rubric icon (Garcia share only)
RUBRIC_EN=[
 ("Study &amp; Analysis","You clearly explain how your master photographer makes images, naming real techniques, not just &lsquo;I like it.&rsquo;"),
 ("Three Master Images","You choose three strong images and write a true technique note for each one."),
 ("Capture","Your full take shows the style of your master photographer and gives you strong options."),
 ("Cull &amp; Edit","Your three final images are your strongest, well selected, and edited to match the look you studied."),
 ("Style Connection","Your photos clearly show the influence of your master photographer."),
 ("Presentation","Your PowerPoint is clean and easy to read, and you present clearly and on time."),
 ("Reflection","Your closing page is honest and thoughtful about what you learned."),
]
RUBRIC_ES=[
 ("Estudio y An&aacute;lisis","Explicas con claridad c&oacute;mo tu fot&oacute;grafo maestro hace im&aacute;genes, nombrando t&eacute;cnicas reales, no solo &lsquo;me gusta.&rsquo;"),
 ("Tres Im&aacute;genes del Maestro","Eliges tres im&aacute;genes fuertes y escribes una nota de t&eacute;cnica verdadera para cada una."),
 ("Captura","Tu toma completa muestra el estilo de tu fot&oacute;grafo maestro y te da buenas opciones."),
 ("Selecci&oacute;n y Edici&oacute;n","Tus tres im&aacute;genes finales son las m&aacute;s fuertes, bien seleccionadas y editadas para igualar el estilo que estudiaste."),
 ("Conexi&oacute;n de Estilo","Tus fotos muestran con claridad la influencia de tu fot&oacute;grafo maestro."),
 ("Presentaci&oacute;n","Tu PowerPoint es limpio y f&aacute;cil de leer, y presentas con claridad y a tiempo."),
 ("Reflexi&oacute;n","Tu p&aacute;gina final es honesta y reflexiva sobre lo que aprendiste."),
]
def rubric_box(es, share=False):
    rows=RUBRIC_ES if es else RUBRIC_EN
    heading="C&oacute;mo Te Van a Calificar" if es else "How You Will Be Graded"
    sub=("&Aacute;brelo para ver qu&eacute; hace un trabajo de nivel m&aacute;ximo en cada parte." if es
         else "Open it to see what full marks looks like in each part.")
    fm="Nivel m&aacute;ximo:" if es else "Full marks:"
    items=""
    for name,desc in rows:
        items+=('<div style="margin:0 0 14px;">'
          f'<div style="font-size:10.5pt;font-weight:bold;letter-spacing:0.08em;text-transform:uppercase;color:#ffd166;margin-bottom:3px;">{name}</div>'
          f'<div style="font-size:12pt;color:rgba(255,255,255,0.90);line-height:1.5;"><strong style="color:#f5b301;">{fm}</strong> {desc}</div>'
          '</div>')
    if share:
        # Garcia public share only (Chris, 2026-11-17): a proper UP-NEXT-style GOLD title bar
        # (section_header + the worksheet-gold icon) that is itself the accordion summary, so the
        # bar expands to the rubric points. to_light() recolors it for the light share. Silva's
        # Canvas rubric (below) is unchanged.
        summary=('<summary style="list-style:none;cursor:pointer;">'
          + section_header(WORKSHEET_GOLD, heading, "#f5b301", "#ffd166")
          + f'<div style="font-size:11.5pt;color:rgba(255,255,255,0.72);line-height:1.5;margin:-4px 2px 0;">{sub}</div>'
          + '</summary>')
        return ('<details style="background:linear-gradient(180deg,rgba(245,179,1,0.12) 0%,rgba(245,179,1,0.03) 100%);border:1px solid rgba(245,179,1,0.35);border-left:6px solid #f5b301;padding:22px 26px 24px;overflow:hidden;margin-bottom:24px;">'
          + summary
          + f'<div style="margin-top:16px;padding-top:16px;border-top:1px solid rgba(245,179,1,0.22);">{items}</div>'
          + '</details>')
    summary=(f'<summary style="list-style:none;cursor:pointer;display:flex;align-items:center;gap:12px;">'
      f'<img src="{DELIVER_ICON}" alt="" style="width:40px;height:40px;flex:0 0 auto;display:block;" />'
      f'<span style="display:block;"><span style="display:block;font-size:10.5pt;font-weight:bold;letter-spacing:0.1em;text-transform:uppercase;color:#ffd166;">{"R&Uacute;BRICA" if es else "RUBRIC"}</span>'
      f'<span style="display:block;font-size:15pt;font-weight:bold;color:#ffffff;line-height:1.3;">{heading}</span>'
      f'<span style="display:block;font-size:11.5pt;color:rgba(255,255,255,0.72);margin-top:2px;">{sub}</span></span></summary>')
    return ('<details style="background:linear-gradient(180deg,rgba(245,179,1,0.12) 0%,rgba(245,179,1,0.03) 100%);border:1px solid rgba(245,179,1,0.35);border-left:5px solid #f5b301;padding:22px 26px;overflow:hidden;margin-bottom:24px;">'
      + summary
      + f'<div style="margin-top:18px;padding-top:16px;border-top:1px solid rgba(245,179,1,0.22);">{items}</div>'
      + '</details>')

def project_downloads(es, zip_url):
    heading="Descarga Tu Carpeta del Proyecto" if es else "Download Your Project Folder"
    if es:
        lead="Descarga tu carpeta del proyecto <strong>en espa&ntilde;ol</strong>. Trae tu plantilla de PowerPoint de 16:9, una carpeta de Im&aacute;genes de Referencia para las fotos de tu maestro, y una carpeta RAW_Images para tus propias fotos cuando las captures."
        label="Carpeta del Proyecto en Espa&ntilde;ol (ZIP)"
        note_t="Despu&eacute;s de que se descargue, descompr&iacute;mela y mueve la carpeta del proyecto a OneDrive &rarr; Carpeta de Fotograf&iacute;a. Esa es tu carpeta para todo este proyecto."
    else:
        lead="Download your project folder <strong>in English</strong>. It holds your 16:9 PowerPoint template, a Reference Images folder for your master photographer&rsquo;s photos, and a RAW_Images folder for your own photos once you capture them."
        label="Project Folder in English (ZIP)"
        note_t="After it downloads, unzip it and move the project folder into OneDrive &rarr; Photography Folder. That is your folder for this whole project."
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">' + dl_link(zip_url, label, row=True) + '</div>'
      + note_orange(note_t) + '</div>')

def growth_box(es):
    # Photo 2 ONLY: firm + motivational growth disclaimer (Chris 2026-11-16). Red accent = important
    # rule. First person (Mr. Silva voice). No repeating last year's master; raise the bar.
    if es:
        eyebrow="FOTO 2 &middot; SUBE EL NIVEL"
        heading="Muestra Tu Crecimiento"
        body=(para("Ahora est&aacute;s en Fotograf&iacute;a 2. Ya tienes habilidad de verdad, y este proyecto debe mostrar cu&aacute;nto has avanzado.")
          + para("<strong>Elige un fot&oacute;grafo maestro NUEVO.</strong> No puedes elegir el mismo que estudiaste el a&ntilde;o pasado. Si entregas el mismo fot&oacute;grafo del a&ntilde;o pasado, no lo voy a aceptar.")
          + para("Este a&ntilde;o el nivel es m&aacute;s alto. Espero un trabajo m&aacute;s planeado, m&aacute;s cuidadoso y de mejor calidad que el a&ntilde;o pasado. T&oacute;mate tu tiempo, toma decisiones fuertes a prop&oacute;sito y mu&eacute;strame el fot&oacute;grafo en que te has convertido."))
    else:
        eyebrow="PHOTO 2 &middot; RAISE THE BAR"
        heading="Show Your Growth"
        body=(para("You are in Photography 2 now. You have real skill, and this project should show how far you have come.")
          + para("<strong>Choose a NEW master photographer.</strong> You may not choose the same one you studied last year. If you turn in the same photographer as last year, I will not accept it.")
          + para("This year the bar is higher. I expect work that is more planned, more careful, and higher quality than last year. Slow down, make strong choices on purpose, and show me the photographer you have become."))
    return ('<div style="background:linear-gradient(180deg,rgba(230,36,41,0.12) 0%,rgba(230,36,41,0.03) 100%);border:1px solid rgba(230,36,41,0.32);border-left:6px solid #E62429;padding:26px 30px;overflow:hidden;margin-bottom:24px;">'
      + f'<div style="font-size:10.5pt;font-weight:bold;letter-spacing:0.12em;text-transform:uppercase;color:#ff8a8d;margin-bottom:4px;">{eyebrow}</div>'
      + f'<div style="font-size:17pt;font-weight:bold;color:#ffffff;line-height:1.25;margin-bottom:10px;">{heading}</div>'
      + body + '</div>')

def growth_reminder(es):
    # Compact Photo 2 reminder placed where students actually choose (Step 02).
    t=("<strong>Recordatorio de Foto 2:</strong> elige un maestro NUEVO, no el que estudiaste el a&ntilde;o pasado."
       if es else "<strong>Photo 2 reminder:</strong> choose a NEW master, not the one you studied last year.")
    return ('<div style="background:rgba(230,36,41,0.10);border:1px solid rgba(230,36,41,0.30);border-left:4px solid #E62429;'
      f'padding:11px 14px;margin:0 0 14px;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.92);">{t}</div>')

def _site_pill(url,label):
    # Compact PURPLE research-site chip: hugs its label (not a full-width bar). A small set of
    # general research sites sit in a wrapping row; opens in a new tab.
    return (f'<a href="{url}" target="_blank" rel="noopener" '
      'style="flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;text-decoration:none;'
      'background:#8b5cf6;color:#ffffff;padding:11px 20px;border-top:2px solid #c4b5fd;'
      f'font-size:11.5pt;line-height:1.3;"><strong>{label}</strong></a>')

def roster_grid(es):
    # The 20 master photographers in a 4-column genre grid (Landscape / Portrait / Still Life /
    # On Location), reflowing 4 -> 2 -> 1 columns. Scoped .mp-* styles ride with the page (linked
    # module, so the <style> survives). Equal grid tracks = straight columns, no wave.
    style=('<style>.mp-roster{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin:12px 0 4px;}'
      '@media (max-width:1024px){.mp-roster{grid-template-columns:repeat(2,minmax(0,1fr));}}'
      '@media (max-width:560px){.mp-roster{grid-template-columns:minmax(0,1fr);}}'
      '.mp-cat{background:linear-gradient(180deg,rgba(0,116,116,0.16) 0%,rgba(0,116,116,0.05) 100%);'
      'border:1px solid rgba(0,184,184,0.22);border-top:3px solid #00b8b8;padding:16px 18px 18px;box-sizing:border-box;}'
      '.mp-cat-h{font-size:11pt;letter-spacing:0.08em;text-transform:uppercase;color:#80e0e0;'
      'padding-bottom:9px;margin-bottom:10px;border-bottom:1px solid rgba(0,184,184,0.22);}'
      '.mp-cat-n{font-size:13.5pt;color:rgba(255,255,255,0.90);line-height:1.95;}</style>')
    cards=""
    for en_l,es_l,names in ROSTER:
        label=es_l if es else en_l
        rows="".join(f'<div>{n}</div>' for n in names)
        cards+=(f'<div class="mp-cat"><div class="mp-cat-h"><strong>{label}</strong></div>'
          f'<div class="mp-cat-n">{rows}</div></div>')
    return style+f'<div class="mp-roster">{cards}</div>'

def reslist(es):
    # General research sites only (5-7 total, NOT one per photographer): a tidy wrapping row of
    # purple chips + a tip to search each photographer\'s own official site. Lives in the purple
    # "Recommended Research Websites" resource card on Step 02.
    lead=("Buenos lugares para ver fotos y leer sobre fot&oacute;grafos. Empieza aqu&iacute;, luego busca el sitio oficial de tu fot&oacute;grafo."
          if es else "Good places to see photos and read about photographers. Start here, then search your photographer&rsquo;s own official website.")
    tip=("Consejo: para fot&oacute;grafos de hoy, busca tambi&eacute;n su sitio web oficial para ver su trabajo m&aacute;s reciente."
         if es else "Tip: for today&rsquo;s photographers, also search for their official website to see their most recent work.")
    pills='<div style="display:flex;flex-wrap:wrap;align-items:stretch;gap:12px 14px;margin:10px 0 2px;">'
    for url,lab in GENERAL_SITES: pills+=_site_pill(url,lab)
    pills+='</div>'
    tip_box=('<div style="background:rgba(139,92,246,0.10);border:1px solid rgba(139,92,246,0.30);'
      'border-left:4px solid #8b5cf6;padding:11px 14px;margin:12px 0 2px;font-size:12pt;'
      f'color:rgba(255,255,255,0.90);"><strong>{tip}</strong></div>')
    return para(lead)+pills+tip_box

def deck_showcase(es, deck_preview):
    heading="Tu Plantilla de PowerPoint" if es else "Your PowerPoint Template"
    if es:
        lead="Usa esta plantilla de 16:9 como punto de partida. Tiene todo lo que necesitas:"
        items=[
            ("Portada:","un retrato de tu fot&oacute;grafo maestro, un autorretrato tuyo, y tu nombre, tu periodo y el curso."),
            ("3 p&aacute;ginas del maestro:","una imagen de tu maestro por p&aacute;gina, con la t&eacute;cnica que estudiaste."),
            ("3 p&aacute;ginas de tu trabajo:","una de tus fotos editadas por p&aacute;gina, con c&oacute;mo usaste lo que aprendiste."),
            ("P&aacute;gina de reflexi&oacute;n:","la p&aacute;gina final, donde respondes la reflexi&oacute;n."),
        ]
        inside="La plantilla ya est&aacute; dentro de la carpeta del proyecto que descargaste en el Resumen."
        cap="Las 8 p&aacute;ginas del PowerPoint: portada, tres del maestro, tres de tu trabajo y la reflexi&oacute;n."
    else:
        lead="Use this 16:9 template as your starting point. It has everything you need:"
        items=[
            ("Cover page:","a headshot of your master photographer, a self-portrait of you, and your name, period, and course."),
            ("3 master pages:","one master image per page, with the technique you studied."),
            ("3 of-your-work pages:","one of your edited photos per page, with how you used what you learned."),
            ("Reflection page:","the closing page, where you answer the reflection."),
        ]
        inside="The template is already inside the project folder you downloaded on the Overview."
        cap="All 8 PowerPoint pages: cover, three master, three of your work, and the reflection."
    inner=(para(lead)+bullets(items,accent="#8b5cf6")
      + (framed(deck_preview, "A preview of the eight-page Master Photographer PowerPoint template: cover, three master pages, three student pages, and the reflection")
         + f'<div style="font-size:11pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.45;">{cap}</div>' if HAVE_DECK_PREVIEW else "")
      + para(inside))
    return resources_card(heading, inner, es)

def contact_sheets_setup(es, cur):
    """Overview contact-sheet block. Install steps + video go to ALL versions
    (Chris moved the video off Steps 3/4, 2026-11-17). The deep 'what is a
    contact sheet / 12-up vs 6-up' primer is Garcia's public share ONLY
    (not cur): her students are new to contact sheets; Silva's already know.
    Names no teacher (shared module + ES 'maestro' already means the master)."""
    out = ""
    if not cur:   # deep primer: Garcia public share only
        if es:
            out += card("HOJAS DE CONTACTOS &middot; QU&Eacute; SON","Dos Hojas, Dos Trabajos",
                para("Una <strong>hoja de contactos</strong> es una sola p&aacute;gina que muestra muchas fotos como miniaturas peque&ntilde;as, todas juntas, para ver todo tu trabajo de un vistazo. En este proyecto usas <strong>dos</strong>:")
                + bullets([
                    ("Hoja de 12 (fondo blanco), tu toma SIN editar:","aqu&iacute; va <strong>toda</strong> tu toma, cada foto que tomaste para este proyecto, <strong>antes</strong> de editar. Muestra tus ajustes de c&aacute;mara."),
                    ("Hoja de 6 (fondo negro), tu trabajo YA editado:","aqu&iacute; van solo tus <strong>fotos finales editadas</strong>, listas para presentar."),
                ], accent="#007474")
                + note("No dejes que el nombre te confunda. El <strong>12</strong> y el <strong>6</strong> solo dicen cu&aacute;ntas fotos caben en una p&aacute;gina, no cu&aacute;ntas necesitas. Tu hoja de 12 puede tener 8 fotos o 32; Lightroom hace m&aacute;s p&aacute;ginas solo. En este proyecto, tu hoja de 6 lleva solo tus <strong>3</strong> fotos editadas, y est&aacute; bien dejar 3 espacios vac&iacute;os."))
        else:
            out += card("CONTACT SHEETS &middot; WHAT THEY ARE","Two Sheets, Two Jobs",
                para("A <strong>contact sheet</strong> is one page that shows a lot of photos as small thumbnails, all together, so your whole take is easy to see at a glance. In this project you use <strong>two</strong>:")
                + bullets([
                    ("12-up (white background), your UNEDITED take:","this holds your <strong>whole</strong> take, every photo you took for this project, <strong>before</strong> you edit. It shows your camera settings."),
                    ("6-up (black background), your EDITED work:","this holds only your <strong>final edited photos</strong>, ready to present."),
                ], accent="#007474")
                + note("Do not let the name fool you. <strong>12</strong> and <strong>6</strong> only say how many photos fit on one page, not how many you need. Your 12-up can have 8 photos or 32; Lightroom just makes more pages. In this project, your 6-up holds only your <strong>3</strong> edited photos, and it is fine to leave 3 empty spaces."))
    # install steps + video: ALL versions
    if es:
        out += resources_card("Instala Tus Ajustes de Hoja de Contactos",
            para("Tus dos ajustes de hoja de contactos vienen dentro de la carpeta del proyecto que descargaste arriba. Inst&aacute;lalos una vez y se quedan en Lightroom.")
            + steps([
                ("Abre Lightroom Classic.","D&eacute;jalo abierto mientras instalas."),
                ("Abre tu carpeta del proyecto y entra a la carpeta Contact Sheet Templates.","Es la carpeta que descargaste arriba."),
                ("Haz doble clic en el ajuste 12-Up.","Aparece un cuadro que dice instalar ajuste. Haz clic en OK. Se instala en segundos."),
                ("Haz doble clic en el ajuste 6-Up y haz clic en OK.","Haz lo mismo con el segundo."),
                ("B&uacute;scalos en el m&oacute;dulo Print, en tus User Templates.","Los dos estar&aacute;n ah&iacute; cuando los necesites."),
            ]), True)
    else:
        out += resources_card("Install Your Contact Sheet Presets",
            para("Your two contact sheet presets come inside the project folder you downloaded above. Install them once and they stay in Lightroom.")
            + steps([
                ("Open Lightroom Classic.","Leave it open while you install."),
                ("Open your project folder and go into the Contact Sheet Templates folder.","It is the folder you downloaded above."),
                ("Double-click the 12-Up preset.","A box pops up that says install preset. Click OK. It installs in seconds."),
                ("Double-click the 6-Up preset and click OK.","Do the same for the second one."),
                ("Find them in the Print module, under your User Templates.","Both will be there when you need them."),
            ]), False)
    return out

def scroll_steps(inner, rgb="139,92,246"):
    # Contained vertical scroller, so a long how-to never looks like a tall,
    # intimidating stack (easier for a 5th-grade / IEP reader). Purple default to
    # sit inside a Resources card. to_light recolors it for the Garcia share.
    return (f'<div class="silva-scroll" style="max-height:300px;overflow-y:auto;padding:14px 16px 20px;'
            f'border:1px solid rgba({rgb},0.30);background:linear-gradient(to bottom, rgba(0,0,0,0.14) 0%, '
            f'rgba(0,0,0,0.14) 88%, rgba({rgb},0.14) 100%);">' + inner + '</div>')

# ============================================================================
# LIGHT-MODE SKIN FOR THE PUBLIC SHARE COPY ONLY (Chris, one-time teacher request,
# 2026-11-16). Applies ONLY in the std/share pass. The Canvas (cur) output, the
# shared silva_framework.py, and css/silva-module.css are ALL left untouched, so the
# locked dark angular framework is unchanged. This takes the generated dark #top
# content and recolors it to a clean light theme: watermark removed, light page,
# white content cards, dark ink, accent color-coding kept. The EN + ES banner
# mastheads are protected from the body recolor and lightened to a teal masthead
# (white crown + title + eyebrow kept, nothing removed, no new assets). Done by exact
# inline-token replacement so the conversion is complete, not partial.
# ============================================================================
_BANNER_SIG = "background-color:#04191a;background-image:linear-gradient(90deg,rgba(3,18,20,0.95)"

def _balanced_div_end(html, start):
    """Index just past the </div> that closes the <div> opening at `start`."""
    depth = 0; k = start
    while k < len(html):
        nd = html.find('<div', k); cd = html.find('</div>', k)
        if cd == -1:
            return len(html)
        if nd != -1 and nd < cd:
            depth += 1; k = nd + 4
        else:
            depth -= 1; k = cd + 6
            if depth == 0:
                return k
    return len(html)

_BANNER_DARK_FILL="background-color:#04191a;background-image:linear-gradient(90deg,rgba(3,18,20,0.95) 0%,rgba(0,66,68,0.5) 50%,rgba(3,18,20,0.95) 100%)"
_BANNER_TEAL_FILL="background-color:#0a6e6e;background-image:linear-gradient(90deg,#0a6a6a 0%,#128a8a 50%,#0a6a6a 100%)"
_BANNER_TEXTCOL='<div style="flex:100 1 260px;min-width:200px;text-align:center;">'

def _recolor_banner(block):
    # Lighten ONLY the outer masthead fill; inner white text / crown / eyebrow stay.
    block = block.replace(_BANNER_DARK_FILL, _BANNER_TEAL_FILL)
    # Brand the public light module with the teacher of record (Mrs. Garcia, this share only).
    teacher = "Sra. Garcia" if "Proyecto" in block else "Mrs. Garcia"
    credit = ('<div style="margin-top:9px;"><span style="font-size:10.5pt;color:#d6fbfb;'
              'letter-spacing:0.05em;"><strong>' + teacher + ' &middot; Pioneer Valley High School'
              '</strong></span></div>')
    i = block.find(_BANNER_TEXTCOL)
    if i >= 0:
        depth = 1; k = i + len(_BANNER_TEXTCOL)
        while k < len(block) and depth > 0:
            nd = block.find('<div', k); cd = block.find('</div>', k)
            if cd == -1: break
            if nd != -1 and nd < cd: depth += 1; k = nd + 4
            else:
                depth -= 1; k = cd + 6
        close = k - 6               # position of the column's matching </div>
        block = block[:close] + credit + block[close:]
    return block

# Ordered (find, replace) inline-token map: dark content tokens -> light equivalents.
_LIGHT_MAP = [
    # section-header icons: the light-teal (#80E1E1) PNGs wash out on a light bar, so swap in
    # deep-teal (#007474) variants (share only; the dark Canvas pages keep the light-teal ones).
    ("Icons/assignment/next-teal-v2.png", "Icons/assignment/next-deep-v1.png"),
    ("Icons/assignment/overview-teal-v1.png", "Icons/assignment/overview-deep-v1.png"),
    ("Icons/assignment/step-check-teal-v3.png", "Icons/assignment/step-check-deep-v1.png"),
    # page wrapper: strip the watermark image, lighten the page
    (",url('https://www.creativesilva.com/assets/PV_Panther_Watermark.png')", ""),
    ("linear-gradient(180deg,rgba(8,8,8,0.97) 0%,rgba(0,56,56,0.94) 50%,rgba(8,8,8,0.97) 100%)",
     "linear-gradient(180deg,#f2f7f7 0%,#e8f1f1 100%)"),
    ("background-color:#080808", "background-color:#eef4f4"),
    ("background-color:#04191a", "background-color:#ffffff"),   # any stray non-banner dark card
    # section-header dark fade -> subtle neutral fade (keeps the left accent bar)
    ("background:linear-gradient(90deg,rgba(0,0,0,0.45) 0%,rgba(0,0,0,0.28) 45%,rgba(0,0,0,0) 100%)",
     "background:linear-gradient(90deg,rgba(0,0,0,0.06) 0%,rgba(0,0,0,0.03) 45%,rgba(0,0,0,0) 100%)"),
    ("background:linear-gradient(90deg,rgba(0,0,0,0.48) 0%,rgba(0,0,0,0.28) 45%,rgba(0,0,0,0) 100%)",
     "background:linear-gradient(90deg,rgba(0,0,0,0.06) 0%,rgba(0,0,0,0.03) 45%,rgba(0,0,0,0) 100%)"),
    # dark inset -> light inset
    ("background:rgba(0,0,0,0.40)", "background:rgba(0,0,0,0.045)"),
    # dark purple angular block -> light purple angular
    ("linear-gradient(135deg,#241d3a 0,#241d3a 30px,#140f24 30px,#140f24 100%)",
     "linear-gradient(135deg,#efeafc 0,#efeafc 30px,#f7f4fe 30px,#f7f4fe 100%)"),
    # light-accent top stripes -> solid accent so they read on white
    ("border-top:2px solid #c4b5fd", "border-top:2px solid #8b5cf6"),
    ("border-top:2px solid #ffb27c", "border-top:2px solid #FF6B1A"),
    # body text: white -> dark ink
    ("color:#ffffff", "color:#16211f"),
    ("color:rgba(255,255,255,0.92)", "color:rgba(22,33,31,0.93)"),
    ("color:rgba(255,255,255,0.90)", "color:rgba(22,33,31,0.92)"),
    ("color:rgba(255,255,255,0.88)", "color:rgba(22,33,31,0.90)"),
    ("color:rgba(255,255,255,0.85)", "color:rgba(22,33,31,0.85)"),
    ("color:rgba(255,255,255,0.82)", "color:rgba(22,33,31,0.80)"),
    ("color:rgba(255,255,255,0.72)", "color:rgba(22,33,31,0.64)"),
    # accent text: lighten-for-dark -> darken-for-light (color meaning kept)
    ("color:#80e0e0", "color:#0b7777"),
    ("color:#a9f2f2", "color:#0b7777"),
    ("color:#00b8b8", "color:#007474"),
    ("color:#c4b5fd", "color:#6d28d9"),
    ("color:#ffd166", "color:#9a6a00"),
    ("color:#f5b301", "color:#8a5a00"),
    ("color:#7bf0a8", "color:#13803f"),
    ("color:#26de78", "color:#12803f"),
    ("color:#8b5cf6", "color:#6d28d9"),
    ("color:#ffb27c", "color:#c2480f"),
    ("color:#FF6B1A", "color:#c2480f"),
    # hairlines: white -> dark
    ("solid rgba(255,255,255,0.08)", "solid rgba(0,0,0,0.10)"),
    ("solid rgba(255,255,255,0.12)", "solid rgba(0,0,0,0.12)"),
    ("rgba(255,255,255,0.08)", "rgba(0,0,0,0.10)"),
    ("rgba(255,255,255,0.12)", "rgba(0,0,0,0.12)"),
]

def to_light(html):
    # 1) pull the banner mastheads out so the body recolor can't touch their text
    parts=[]; banners=[]; i=0
    while True:
        j = html.find(_BANNER_SIG, i)
        if j < 0:
            parts.append(html[i:]); break
        ds = html.rfind('<div', 0, j)
        parts.append(html[i:ds])
        end = _balanced_div_end(html, ds)
        banners.append(html[ds:end])
        parts.append("\x00B%d\x00" % (len(banners)-1))
        i = end
    body = "".join(parts)
    # 2) recolor the content to light
    for a,b in _LIGHT_MAP:
        body = body.replace(a,b)
    # 3) tidy the now single-layer wrapper background (watermark layer removed)
    body = body.replace("background-position:center center,center center", "background-position:center center")
    body = body.replace("background-repeat:no-repeat,no-repeat", "background-repeat:no-repeat")
    body = body.replace("background-attachment:fixed,fixed", "background-attachment:fixed")
    # 4) reinsert the (lightened) banner mastheads
    for n,blk in enumerate(banners):
        body = body.replace("\x00B%d\x00" % n, _recolor_banner(blk))
    return body

# Light skin for the standalone chrome (nav / step dots / step buttons / bottom nav /
# teacher-tools bar). Emitted AFTER the silva-module.css link so it wins by source order
# without !important. Share pages only.
LIGHT_CHROME = (
    "body{background:#eef4f4;color:#13211f;}"
    ".silva-nav{background:rgba(255,255,255,0.82);border-bottom:1px solid rgba(0,0,0,0.08);}"
    ".silva-breadcrumb a{color:#007474;}"
    ".silva-breadcrumb a:hover{color:#005a5a;}"
    ".silva-breadcrumb .bc-sep{color:rgba(0,116,116,0.5);}"
    ".silva-breadcrumb .bc-current{color:#2a3a38;}"
    ".sdot{border-color:rgba(0,0,0,0.18);color:rgba(0,0,0,0.22);}"
    ".sdot-link{border-color:rgba(0,116,116,0.45);color:rgba(0,116,116,0.70);}"
    ".sdot-link:hover{border-color:#007474;color:#007474;background:rgba(0,116,116,0.08);}"
    ".sdot-active{background:#007474;border-color:#007474;color:#fff;}"
    ".silva-step-btn{background:#fff;border:1px solid rgba(0,116,116,0.35);color:#0a6a6a;}"
    ".silva-step-btn:hover{background:rgba(0,116,116,0.08);color:#005a5a;border-color:#007474;}"
    ".silva-bottom-nav{border-top:1px solid rgba(0,0,0,0.10);}"
    ".silva-bottom-btn{background:#fff;border:1px solid rgba(0,116,116,0.35);color:#0a6a6a;}"
    ".silva-bottom-btn:hover{background:rgba(0,116,116,0.08);color:#005a5a;border-color:#007474;}"
    ".silva-share-bar{border-top:1px solid rgba(0,0,0,0.08);}"
    ".silva-share-inner .stt-label{color:#0a7777;}"
    ".share-btn{color:#06403f;background:rgba(0,184,184,0.12);border:1px solid rgba(0,116,116,0.50);}"
    ".share-btn:hover{background:rgba(0,184,184,0.22);}"
    ".share-btn.ok{background:#00b8b8;color:#04201f;border-color:#00b8b8;}")

def wrap_standalone(title, nav_inner, top_html, bottom, files_std, share_name, light=False):
    # Self-contained share page: the module's own css + a minimal internal nav, NO silva-nav.js (so no
    # site nav / Equipment Manager / Catalog), NO builder buttons, NO links out. Internal step links
    # only. Language toggle kept (inline JS runs on the hosted page). Assets load absolute from the
    # whitelisted domain so the page works from the /share/ path. Teacher tools (Copy URL / Copy HTML /
    # Download All) ride in their own full-width bar UNDER the nav row. Locked pattern, see framework 10.3.
    pages_js='['+','.join('"'+f+'"' for f in files_std)+']'
    name_js='"'+share_name.replace('\\','\\\\').replace('"','\\"')+'"'
    share_css=(
      ".silva-share-bar{border-top:1px solid rgba(255,255,255,0.08);}"
      ".silva-share-inner{display:flex;flex-wrap:wrap;align-items:center;gap:8px;padding:9px 10px;}"
      ".silva-share-inner .stt-label{font-size:11px;font-weight:700;letter-spacing:0.12em;"
      "text-transform:uppercase;color:#80e0e0;margin-right:4px;}"
      ".share-btn{font-family:Arial,sans-serif;font-size:12px;font-weight:700;letter-spacing:0.04em;"
      "color:#eafeff;background:rgba(0,184,184,0.14);border:1px solid rgba(0,184,184,0.55);"
      "padding:7px 13px;cursor:pointer;border-radius:0;line-height:1.1;transition:background .15s;}"
      ".share-btn:hover{background:rgba(0,184,184,0.28);}"
      ".share-btn.ok{background:#00b8b8;color:#04201f;border-color:#00b8b8;}")
    share_js=(
      "(function(){"
      "var btns=document.querySelectorAll('.share-btn');if(!btns.length){return;}"
      "var PAGES="+pages_js+";var NAME="+name_js+";"
      "var base=location.pathname.replace(/[^/]*$/,'');"
      "function flash(b,msg){var o=b.getAttribute('data-orig')||b.textContent;b.setAttribute('data-orig',o);b.textContent=msg;b.classList.add('ok');setTimeout(function(){b.textContent=b.getAttribute('data-orig');b.classList.remove('ok');},2200);}"
      "function copy(t,b){navigator.clipboard.writeText(t).then(function(){flash(b,'Copied!');}).catch(function(){alert('Copy failed.');});}"
      "function dlAll(b){var o=b.textContent;b.textContent='Building...';"
      "Promise.all(PAGES.map(function(u){return fetch(base+u).then(function(r){return r.text();}).then(function(h){var d=new DOMParser().parseFromString(h,'text/html');var t=d.querySelector('title');var pt=t?t.textContent.split('|')[0].trim():u;var top=d.getElementById('top');return{t:pt,code:top?top.outerHTML:h};}).catch(function(){return{t:u,code:'(could not load this page)'};});})).then(function(ps){"
      "var md='# '+NAME+'\\n\\n_All pages, downloaded '+new Date().toISOString().slice(0,10)+' from creativesilva.com._\\n\\nEach section holds that page Canvas-pasteable HTML (the same code the Copy HTML button copies).\\n\\n';"
      "ps.forEach(function(p,i){md+='---\\n\\n## '+(i+1)+'. '+p.t+'\\n\\n```html\\n'+p.code+'\\n```\\n\\n';});"
      "var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([md],{type:'text/markdown;charset=utf-8'}));a.download=NAME.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'')+'-all-pages.md';document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},1000);"
      "b.textContent=o;flash(b,'Downloaded');"
      "}).catch(function(){b.textContent=o;alert('Download failed.');});}"
      "for(var i=0;i<btns.length;i++){(function(b){b.addEventListener('click',function(){var act=b.getAttribute('data-act');if(act==='url'){copy(location.href,b);}else if(act==='html'){var el=document.getElementById('top');if(el){copy(el.outerHTML,b);}}else if(act==='all'){dlAll(b);}});})(btns[i]);}"
      "})();")
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="icon" type="image/svg+xml" href="https://www.creativesilva.com/logos/CS_Logo_Only.svg" />
  <style>:root {{ --course-accent: #007474; }}
  {share_css}</style>
  <link rel="stylesheet" href="https://www.creativesilva.com/css/silva-module.css" />
  {('<style id="silva-light-skin">'+LIGHT_CHROME+'</style>') if light else ''}
</head>
<body>
  <nav class="silva-nav" aria-label="Module navigation">
    <div class="silva-nav-inner">
{nav_inner}
    </div>
    <div class="silva-share-bar"><div class="silva-share-inner"><span class="stt-label">Teacher tools</span><button type="button" class="share-btn" data-act="url">Copy URL</button><button type="button" class="share-btn" data-act="html">Copy HTML</button><button type="button" class="share-btn" data-act="all">Download All</button></div></div>
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
  {share_js}
  </script>
</body>
</html>'''

def build(mode, C):
    cur = (mode == "cur")
    CL=C["cl"]; PREFIX=C["prefix"]; ZIP_EN=C["zip_en"]; ZIP_ES=C["zip_es"]; DECKPREV=C["deck_preview"]; IS_P2=C["p2"]
    OVER=f"{PREFIX}-master-photographer-overview.html"
    S2=f"{PREFIX}-master-photographer-step02-choose-your-master.html"
    S3=f"{PREFIX}-master-photographer-step03-capture-contact.html"
    S4=f"{PREFIX}-master-photographer-step04-cull-edit.html"
    S5=f"{PREFIX}-master-photographer-step05-presentation-reflection.html"
    FILES_STD=["index.html","step02-choose-your-master.html","step03-capture-contact.html",
               "step04-cull-edit.html","step05-presentation-reflection.html"]
    FILES = [OVER,S2,S3,S4,S5] if cur else FILES_STD
    HREFS = FILES
    TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04"),("5","Step 05")]
    STEPNUM=["01","02","03","04","05"]
    SHARE_NAME="Master Photographer"

    def wrap_page(title, nav_inner, top_html, bottom):
        if cur:
            return _sf.wrap_page(title, nav_inner, top_html, bottom)
        # Public share copy is LIGHT MODE (Chris, one-time request): recolor the dark
        # content and emit the light chrome skin. Canvas (cur) output is unchanged.
        return wrap_standalone(title, nav_inner, to_light(top_html), bottom, FILES_STD, SHARE_NAME, light=True)

    def step_topnav(i):
        parts=[]
        if i>0: parts.append(f'<a href="{HREFS[i-1]}" class="silva-step-btn">&#8592; Step {STEPNUM[i-1]}</a>')
        if i<4: parts.append(f'<a href="{HREFS[i+1]}" class="silva-step-btn">Step {STEPNUM[i+1]} &#8594;</a>')
        return ' '.join(parts)

    def step_bottom(i):
        left = f'<a href="{HREFS[i-1]}" class="silva-bottom-btn">&#8592; Step {STEPNUM[i-1]}</a>' if i>0 else '<span></span>'
        if i<4:
            lab = f'Next: Step {STEPNUM[i+1]} &#8594;' if i==0 else f'Step {STEPNUM[i+1]} &#8594;'
            right = f'<a href="{HREFS[i+1]}" class="silva-bottom-btn">{lab}</a>'
        else:
            right = '<span></span>'
        return f'<div class="silva-bottom-nav">{left}{right}</div>'

    def nav(current,dots,stepnav):
        if cur:
            crumb=('      <div class="silva-breadcrumb">\n'
                   '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
                   '        <span class="bc-sep">&rsaquo;</span>\n'
                   f'        <a href="{OVER}" class="bc-hide-sm">Master Photographer</a>\n'
                   '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
                   f'        <span class="bc-current">{current}</span>\n'
                   '      </div>\n')
        else:
            # Standalone share copy: NO catalog link, nothing links back out.
            crumb=('      <div class="silva-breadcrumb">\n'
                   '        <span class="bc-current">Master Photographer</span>\n'
                   '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
                   f'        <span class="bc-current">{current}</span>\n'
                   '      </div>\n')
        return (crumb
                + '      <div class="silva-nav-spacer"></div>\n'
                + f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
                + f'      <div class="silva-step-nav">{stepnav}</div>')
    def dots_for(ai):
        return "".join(dot("" if i==ai else HREFS[i], lab, title, i==ai, module=False) for i,(lab,title) in enumerate(TITLES))

    # ================= OVERVIEW (Step 01) =================
    def overview():
        en=banner(f"{PROJ_LABEL} &bull;Step 01","Master Photographer",
            "Study one master photographer, then capture and present three photos in their style. Read this page, then go to Step 02.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_CAMERA_KIT)
        en+=type_card("overview","Step 01 &middot; Overview","Learn From a Master, Then Make Your Own",
            para("In this project you pick <strong>one master photographer</strong> and study <strong>how they make their images</strong>. This is not a report about their life. You study their <strong>style, technique, and impact</strong>: how they compose, light, and edit their photos.")
            + para("Then you become the photographer. You <strong>capture three of your own photos</strong> in that style with the school camera kit, edit your best three, and present your master&rsquo;s work and your work <strong>side by side</strong> in a PowerPoint.")
            + (framed(HERO,"Master photographers, each with a camera: the styles you choose from in this project") + '<div style="font-size:11pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.45;">Many styles, many photographers. You pick one to study and bring into your own photos.</div>' if HAVE_HERO else ""))
        if IS_P2: en+=growth_box(False)
        en+=project_downloads(False, ZIP_EN)
        en+=contact_sheets_setup(False, cur)
        en+=card("HOW THIS PROJECT WORKS","From Studying a Master to Your Own Photos",
            para("You are on Step 01 now: read this page so you understand the project. Here is the path.")
            + bullets([
                ("Step 02 &middot; Choose Your Master:","meet the master photographers, pick one, and start your PowerPoint with three of their images."),
                ("Step 03 &middot; Capture &amp; Contact:","capture a full take of your own photos in your master&rsquo;s style, then build a contact sheet."),
                ("Step 04 &middot; Cull &amp; Edit:","select your three strongest images and edit them to match the look you studied."),
                ("Step 05 &middot; Presentation &amp; Reflection:","finish your PowerPoint, present it to the class, and answer the reflection on the closing page."),
            ]))
        en+=card("WHY THIS MATTERS","See Like a Pro",
            para("Understanding <strong>how professional photographers make their images</strong> helps you make stronger choices in your own work. When you can name what makes a photo great, you can do it on purpose.")
            + note("You keep your three master images and your three photos together, so everyone can see where your ideas came from and how you made them your own."))
        en+=rubric_box(False, share=not cur)          # Garcia share gets the gold title-bar + worksheet icon; Canvas keeps the plain rubric
        if cur: en+=standards_box(False, STANDARDS)   # CTE Standards: Canvas pages only; Garcia's public share drops it (Chris, 2026-11-17)
        en+=resources_card("Key Words",
            vocab_grid("Know These Words",
              "These key words are important for this project. Tap each one to see what it means.",
              VOCAB_EN, es=False), False)
        en+=next_up("UP NEXT &middot; STEP 02 - Choose Your Master","Meet the master photographers, pick the one whose work pulls you in, and start your PowerPoint.")

        es=banner(f"{PROJ_LABEL_ES} &bull;Paso 01","Fot&oacute;grafo Maestro",
            "Estudia a un fot&oacute;grafo maestro, luego captura y presenta tres fotos en su estilo. Lee esta p&aacute;gina y ve al Paso 02.",
            "#top","Back to English", HICON_CAMERA_KIT)
        es+=type_card("overview","Paso 01 &middot; Resumen","Aprende de un Maestro, Luego Haz lo Tuyo",
            para("En este proyecto eliges a <strong>un fot&oacute;grafo maestro</strong> y estudias <strong>c&oacute;mo hacen sus im&aacute;genes</strong>. Esto no es un reporte sobre su vida. Estudias su <strong>estilo, su t&eacute;cnica y su impacto</strong>: c&oacute;mo componen, iluminan y editan sus fotos.")
            + para("Luego t&uacute; te vuelves el fot&oacute;grafo. <strong>Capturas tres fotos propias</strong> en ese estilo con el kit de c&aacute;mara de la escuela, editas tus mejores tres y presentas el trabajo de tu maestro y el tuyo <strong>lado a lado</strong> en un PowerPoint.")
            + (framed(HERO,"Fot&oacute;grafos maestros, cada uno con una c&aacute;mara: los estilos entre los que eliges en este proyecto") + '<div style="font-size:11pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.45;">Muchos estilos, muchos fot&oacute;grafos. Eliges a uno para estudiarlo y traerlo a tus propias fotos.</div>' if HAVE_HERO else ""))
        if IS_P2: es+=growth_box(True)
        es+=project_downloads(True, ZIP_ES)
        es+=contact_sheets_setup(True, cur)
        es+=card("C&Oacute;MO FUNCIONA ESTE PROYECTO","De Estudiar a un Maestro a Tus Propias Fotos",
            para("Est&aacute;s en el Paso 01 ahora: lee esta p&aacute;gina para entender el proyecto. Este es el camino.")
            + bullets([
                ("Paso 02 &middot; Elige a Tu Maestro:","conoce a los fot&oacute;grafos maestros, elige a uno y empieza tu PowerPoint con tres de sus im&aacute;genes."),
                ("Paso 03 &middot; Captura y Contacto:","captura una toma completa de tus propias fotos en el estilo de tu maestro, luego arma una hoja de contactos."),
                ("Paso 04 &middot; Selecciona y Edita:","elige tus tres im&aacute;genes m&aacute;s fuertes y ed&iacute;talas para igualar el estilo que estudiaste."),
                ("Paso 05 &middot; Presentaci&oacute;n y Reflexi&oacute;n:","termina tu PowerPoint, pres&eacute;ntalo a la clase y responde la reflexi&oacute;n en la p&aacute;gina final."),
            ]))
        es+=card("POR QU&Eacute; IMPORTA","Mira Como un Profesional",
            para("Entender <strong>c&oacute;mo los fot&oacute;grafos profesionales hacen sus im&aacute;genes</strong> te ayuda a tomar mejores decisiones en tu propio trabajo. Cuando puedes nombrar lo que hace grande a una foto, puedes hacerlo a prop&oacute;sito.")
            + note("Mantienes tus tres im&aacute;genes del maestro y tus tres fotos juntas, para que todos vean de d&oacute;nde vinieron tus ideas y c&oacute;mo las hiciste tuyas."))
        es+=rubric_box(True, share=not cur)          # Garcia share gets the gold title-bar + worksheet icon; Canvas keeps the plain rubric
        if cur: es+=standards_box(True, STANDARDS)   # CTE Standards: Canvas pages only; Garcia's public share drops it (Chris, 2026-11-17)
        es+=resources_card("Palabras Clave",
            vocab_grid("Conoce Estas Palabras",
              "Estas palabras clave son importantes para este proyecto. Toca cada una para ver qu&eacute; significa.",
              VOCAB_ES, es=True), True)
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 02 - Elige a Tu Maestro","Conoce a los fot&oacute;grafos maestros, elige al que m&aacute;s te atraiga y empieza tu PowerPoint.")

        return wrap_page(f"Master Photographer | {CL} | PVHS", nav("Step 01",dots_for(0),step_topnav(0)), top_wrap(en,es), step_bottom(0))

    # ================= STEP 02: Choose Your Master =================
    def step02():
        en=banner(f"{PROJ_LABEL} &bull;Step 02","Choose Your Master",
            "Meet the master photographers, pick one, and start your PowerPoint with three of their images.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
        en+=card("STEP 02 &middot; STUDY YOUR MASTER","Pick One, Then Study How They Work",
            (float_right(RESEARCH_FLOAT,"A student researching a master photographer on a lab computer","Study their style online before you choose. Look at a lot of their photos.") if HAVE_RESEARCH else "")
            + para("You will study <strong>one master photographer</strong> and bring their style into your own photos. First, meet the photographers below and <strong>pick the one</strong> whose work pulls you in the most.")
            + para("You are studying <strong>how they make images</strong>, not their life story. For your master, look closely at their <strong>composition, light, subjects, and editing</strong>. These are the ideas you will bring into your own three photos.")
            + note("Choose the photographer you would most want to photograph like. The more their work excites you, the stronger your own photos will be."))
        en+=deliverables_box(False,
            [("Pages 1 to 4 as a PDF (not the whole PowerPoint yet):","fill just your <strong>first 4 pages</strong>: the <strong>Cover page</strong> (a headshot of your master, a self-portrait of you, and your name, period, and course) and your <strong>3 Master Photographer pages</strong> (one of their photos and a technique note on each). Export <strong>only pages 1 to 4</strong> as a PDF and upload it. You finish the other pages in Step 05.")])
        en+=card("CHOOSE YOUR MASTER","Master Photographers",
            para("Here are your master photographers in four styles: <strong>Landscape, Portrait, Still Life, and On Location</strong>. Look through all four groups before you choose.")
            + (growth_reminder(False) if IS_P2 else "")
            + roster_grid(False))
        en+=resources_card("Recommended Research Websites", reslist(False), False)
        en+=card("START YOUR POWERPOINT","Build Your First 4 Pages",
            para("Now build the <strong>first 4 pages</strong> of your PowerPoint: the cover and your 3 master photographer pages. You are <strong>not</strong> finishing the whole PowerPoint yet. You finish the rest in Step 05.")
            + steps([
                ("Open the PowerPoint template.","It is in the project folder you downloaded on the Overview."),
                ("Fill in the Cover page.","Add a <strong>headshot of your master photographer</strong>, a <strong>self-portrait of you</strong> (a photo of yourself), and type your name, period, and course."),
                ("Find three photos by your master.","Search online for three of their best photos, the ones that show their style. Save them in your project folder."),
                ("Put one photo on each Master page.","One master photo per page, on pages 2, 3, and 4."),
                ("Write your technique note on each.","Name the technique you see: composition, lighting, the moment, tonal range, or editing. Say why it works."),
                ("Export only pages 1 to 4 as a PDF.","Follow the steps in the box below, then upload the PDF to this Canvas assignment."),
            ])
            + note("It is OK that pages 5 to 8 are still empty. You only turn in these first 4 pages now. The photos on your master pages are <strong>their</strong> work, from online. You capture your <strong>own</strong> photos next, in Step 03."))
        en+=resources_card("How to Export Only Pages 1 to 4 as a PDF (Mac)",
            para("On a Mac, <strong>File &gt; Export</strong> sends every page. To pick just pages 1 to 4, you use <strong>Print</strong>. Follow each step:")
            + scroll_steps(steps([
                ("Save your PowerPoint first.","Press Cmd + S so your work is safe."),
                ("Open the Print window.","Go to <strong>File &gt; Print</strong>."),
                ("Choose only pages 1 to 4.","Find the page range and set it to print <strong>From 1 To 4</strong>. That is your cover and your 3 master pages."),
                ("Click the PDF button.","It is at the <strong>bottom-left</strong> of the Print window."),
                ("Choose Save as PDF.","Pick it from the little menu that pops up."),
                ("Name it and save.","Name it LastName_First_MasterPhotographer_Start.pdf, then click Save."),
                ("Upload the PDF to Canvas.","Turn it in to this Canvas assignment."),
            ])), False)
        en+=next_up("UP NEXT &middot; STEP 03 - Capture &amp; Contact","Check out a camera kit and capture a full take of your own photos in your master&rsquo;s style.")

        es=banner(f"{PROJ_LABEL_ES} &bull;Paso 02","Elige a Tu Maestro",
            "Conoce a los fot&oacute;grafos maestros, elige a uno y empieza tu PowerPoint con tres de sus im&aacute;genes.",
            "#top","Back to English", HICON_DESIGN)
        es+=card("PASO 02 &middot; ESTUDIA A TU MAESTRO","Elige a Uno y Estudia C&oacute;mo Trabaja",
            (float_right(RESEARCH_FLOAT,"Una estudiante investigando a un fot&oacute;grafo maestro en una computadora del laboratorio","Estudia su estilo en internet antes de elegir. Mira muchas de sus fotos.") if HAVE_RESEARCH else "")
            + para("Vas a estudiar a <strong>un fot&oacute;grafo maestro</strong> y traer su estilo a tus propias fotos. Primero, conoce a los fot&oacute;grafos de abajo y <strong>elige al que m&aacute;s te atraiga</strong>.")
            + para("Est&aacute;s estudiando <strong>c&oacute;mo hacen im&aacute;genes</strong>, no su biograf&iacute;a. Para tu maestro, observa de cerca su <strong>composici&oacute;n, luz, sujetos y edici&oacute;n</strong>. Estas son las ideas que traer&aacute;s a tus propias tres fotos.")
            + note("Elige al fot&oacute;grafo como el que m&aacute;s te gustar&iacute;a fotografiar. Entre m&aacute;s te emocione su trabajo, m&aacute;s fuertes ser&aacute;n tus propias fotos."))
        es+=deliverables_box(True,
            [("P&aacute;ginas 1 a 4 como PDF (a&uacute;n no todo el PowerPoint):","llena solo tus <strong>primeras 4 p&aacute;ginas</strong>: la <strong>p&aacute;gina de portada</strong> (un retrato de tu maestro, un autorretrato tuyo, y tu nombre, tu periodo y el curso) y tus <strong>3 p&aacute;ginas del fot&oacute;grafo maestro</strong> (una de sus fotos y una nota de t&eacute;cnica en cada una). Exporta <strong>solo las p&aacute;ginas 1 a 4</strong> como PDF y s&uacute;belo. Terminas las dem&aacute;s p&aacute;ginas en el Paso 05.")])
        es+=card("ELIGE A TU MAESTRO","Fot&oacute;grafos Maestros",
            para("Aqu&iacute; est&aacute;n tus fot&oacute;grafos maestros en cuatro estilos: <strong>Paisaje, Retrato, Naturaleza Muerta y En Locaci&oacute;n</strong>. Mira los cuatro grupos antes de elegir.")
            + (growth_reminder(True) if IS_P2 else "")
            + roster_grid(True))
        es+=resources_card("Sitios de Investigaci&oacute;n Recomendados", reslist(True), True)
        es+=card("EMPIEZA TU POWERPOINT","Arma Tus Primeras 4 P&aacute;ginas",
            para("Ahora arma las <strong>primeras 4 p&aacute;ginas</strong> de tu PowerPoint: la portada y tus 3 p&aacute;ginas del fot&oacute;grafo maestro. <strong>No</strong> terminas todo el PowerPoint todav&iacute;a. Terminas el resto en el Paso 05.")
            + steps([
                ("Abre la plantilla de PowerPoint.","Est&aacute; en la carpeta del proyecto que descargaste en el Resumen."),
                ("Llena la p&aacute;gina de portada.","Agrega un <strong>retrato de tu fot&oacute;grafo maestro</strong>, un <strong>autorretrato tuyo</strong> (una foto de ti), y escribe tu nombre, tu periodo y el curso."),
                ("Busca tres fotos de tu maestro.","Busca en internet tres de sus mejores fotos, las que muestran su estilo. Gu&aacute;rdalas en tu carpeta del proyecto."),
                ("Pon una foto en cada p&aacute;gina del maestro.","Una foto del maestro por p&aacute;gina, en las p&aacute;ginas 2, 3 y 4."),
                ("Escribe tu nota de t&eacute;cnica en cada una.","Nombra la t&eacute;cnica que ves: composici&oacute;n, iluminaci&oacute;n, el momento, el rango tonal o la edici&oacute;n. Di por qu&eacute; funciona."),
                ("Exporta solo las p&aacute;ginas 1 a 4 como PDF.","Sigue los pasos del recuadro de abajo, luego sube el PDF a esta tarea de Canvas."),
            ])
            + note("Est&aacute; bien que las p&aacute;ginas 5 a 8 sigan vac&iacute;as. Solo entregas estas primeras 4 p&aacute;ginas ahora. Las fotos de tus p&aacute;ginas del maestro son <strong>su</strong> trabajo, de internet. T&uacute; capturas tus <strong>propias</strong> fotos despu&eacute;s, en el Paso 03."))
        es+=resources_card("C&oacute;mo Exportar Solo las P&aacute;ginas 1 a 4 como PDF (Mac)",
            para("En una Mac, <strong>File &gt; Export</strong> (Archivo &gt; Exportar) env&iacute;a todas las p&aacute;ginas. Para elegir solo las p&aacute;ginas 1 a 4, usas <strong>Print</strong> (Imprimir). Sigue cada paso:")
            + scroll_steps(steps([
                ("Guarda tu PowerPoint primero.","Presiona Cmd + S para que tu trabajo est&eacute; seguro."),
                ("Abre la ventana de imprimir.","Ve a <strong>File &gt; Print</strong> (Archivo &gt; Imprimir)."),
                ("Elige solo las p&aacute;ginas 1 a 4.","Busca el rango de p&aacute;ginas y ponlo en <strong>From 1 To 4</strong> (Desde 1 Hasta 4). Esa es tu portada y tus 3 p&aacute;ginas del maestro."),
                ("Haz clic en el bot&oacute;n PDF.","Est&aacute; <strong>abajo a la izquierda</strong> de la ventana de imprimir."),
                ("Elige Save as PDF.","Esc&oacute;gelo del men&uacute; que aparece."),
                ("N&oacute;mbralo y gu&aacute;rdalo.","N&oacute;mbralo LastName_First_MasterPhotographer_Start.pdf, luego haz clic en Save (Guardar)."),
                ("Sube el PDF a Canvas.","Entr&eacute;galo en esta tarea de Canvas."),
            ])), True)
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 03 - Captura y Contacto","Pide un kit de c&aacute;mara y captura una toma completa de tus propias fotos en el estilo de tu maestro.")

        return wrap_page(f"Step 2: Choose Your Master | Master Photographer | {CL} | PVHS", nav("Step 02",dots_for(1),step_topnav(1)), top_wrap(en,es), step_bottom(1))

    # ================= STEP 03: Capture & Contact =================
    def step03():
        en=banner(f"{PROJ_LABEL} &bull;Step 03","Capture &amp; Contact",
            "Capture a full take of your own photos in your master&rsquo;s style, then build a contact sheet.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_CAMERA_KIT)
        en+=card("STEP 03 &middot; MAKE YOUR PHOTOS","Capture in Your Master&rsquo;s Style",
            para("Now you are the photographer. Check out a <strong>camera kit</strong> and capture your own photos in the style of the master you studied. Think about what made their work strong, and try to do the same on purpose.")
            + bullets([
                ("Match their eye:","their subjects, their composition, their light, and their moment. What did you notice in Step 02?"),
                ("Capture a full take:","take more than three photos. Try different angles, distances, and moments so you have strong options to choose from later."),
                ("Capture in RAW:","set your camera to RAW so you have the most to work with when you edit."),
            ])
            + note("A real photographer always captures more than they keep. More options now means a stronger final three later."))
        en+=deliverables_box(False,
            [("1 contact sheet (high-resolution JPG):","a 12-up contact sheet of your full take, uploaded to this Canvas assignment.")])
        en+=card("MATCH THE LOOK","Pick Settings That Fit the Style",
            para("Your camera settings help you match your master&rsquo;s look. Here are a few starting points:")
            + bullets([
                ("Sharp, detailed scene (like Ansel Adams):","use a higher f-number, like f/11, so the whole scene is in focus front to back."),
                ("Soft background behind a person (like Platon):","use a lower f-number, like f/2.8, so the face is sharp and the background goes soft."),
                ("Catch a moment on the move (like Cartier-Bresson):","use a faster shutter speed, like 1/500, so the action stays sharp."),
            ])
            + note("These are starting points, not rules. Match the feeling of your master&rsquo;s work."))
        en+=card("OFFLOAD YOUR PHOTOS","Copy Your Card to RAW_Images",
            para("You do not use a cable. You <strong>off-load</strong> your SD card with the <strong>card reader</strong> on your desk, then copy every photo into your project folder. Follow each step:")
            + scroll_steps(steps([
                ("Put your SD card in the card reader.","Use the card reader mounted to your desk."),
                ("Open the card, then DCIM, then 100CANON.","Open your SD card in Finder, open the <strong>DCIM</strong> folder, then open <strong>100CANON</strong>. Your photos are here."),
                ("Select all, then copy.","Press <strong>Cmd + A</strong> to select every photo. Right-click and choose <strong>Copy</strong>."),
                ("Open your RAW_Images folder.","In OneDrive, open your project folder, then open the <strong>RAW_Images</strong> folder."),
                ("Paste them in.","Press <strong>Cmd + V</strong> to paste every photo into RAW_Images."),
                ("Check the count matches.","Wait for every photo to finish. The number of photos in RAW_Images must match the number on your card."),
                ("Eject, return, and format.","Eject the card, put it back in the camera, and format the card so it is clean for next time."),
            ]), rgb="0,184,184")
            + note("Off-load your <strong>full take</strong>, every photo you captured. You select your best three later, in the next step."))
        en+=card("BUILD YOUR CONTACT SHEET","Make Your 12-Up Contact Sheet",
            para("A <strong>12-up contact sheet</strong> shows your whole take as small thumbnails on one page, 12 per page. Make it <strong>before you edit</strong>: this is your <strong>unedited</strong> take, and it shows your camera settings.")
            + para("First, bring your photos into Lightroom Classic and put them in a collection. Follow each step:")
            + scroll_steps(steps([
                ("Open Lightroom Classic.","Open the app on your Mac."),
                ("Click Import.","Click the <strong>Import</strong> button at the bottom-left."),
                ("Pick your RAW_Images folder.","On the left, open your project folder in OneDrive and click the <strong>RAW_Images</strong> folder. Your photos show in the middle."),
                ("Import every photo.","Make sure all your photos are checked, then click <strong>Import</strong> at the bottom-right."),
                ("Select all your photos.","Go to the Library. Press <strong>Cmd + A</strong> to select every imported photo."),
                ("Make a collection called Master Photographer.","Right-click your selected photos and choose <strong>Create Collection</strong>. Name it <strong>Master Photographer</strong>, then click Create. This keeps your take together."),
            ]), rgb="0,184,184")
            + para("Now make your 12-up contact sheet:")
            + steps([
                ("Open the Print module.","Open your <strong>Master Photographer</strong> collection, then go to the <strong>Print</strong> module."),
                ("Pick the 12-Up Contact Sheet preset.","Choose it from your User Templates. If you do not see it, install it on the Overview first."),
                ("Print to a high-resolution JPG.","Set Print To: JPEG File, then click Print to File. The preset already saves a high-resolution JPG for you."),
                ("Name it and upload.","Name it <strong>12 Up Master Photographer</strong> plus your name, like <strong>12 Up Master Photographer Jane Smith</strong>. Then upload the JPG to this Canvas assignment."),
            ])
            + note("Turn in a <strong>high-resolution JPG</strong>, never a PDF. The contact-sheet preset already saves the right format.")
            + (note("Do not let the name fool you. Put <strong>every</strong> photo from your take in. The 12-up fits 12 per page, but it is not a minimum. More than 12? Lightroom just makes more pages. 8 photos or 32, all good.") if not cur else ""))
        en+=next_up("UP NEXT &middot; STEP 04 - Cull &amp; Edit","Select your three strongest images and edit them to match the look you studied.")

        es=banner(f"{PROJ_LABEL_ES} &bull;Paso 03","Captura y Contacto",
            "Captura una toma completa de tus propias fotos en el estilo de tu maestro, luego arma una hoja de contactos.",
            "#top","Back to English", HICON_CAMERA_KIT)
        es+=card("PASO 03 &middot; HAZ TUS FOTOS","Captura en el Estilo de Tu Maestro",
            para("Ahora t&uacute; eres el fot&oacute;grafo. Pide un <strong>kit de c&aacute;mara</strong> y captura tus propias fotos en el estilo del maestro que estudiaste. Piensa en lo que hizo fuerte su trabajo e intenta hacer lo mismo a prop&oacute;sito.")
            + bullets([
                ("Iguala su mirada:","sus sujetos, su composici&oacute;n, su luz y su momento. &iquest;Qu&eacute; notaste en el Paso 02?"),
                ("Captura una toma completa:","toma m&aacute;s de tres fotos. Prueba diferentes &aacute;ngulos, distancias y momentos para tener buenas opciones despu&eacute;s."),
                ("Captura en RAW:","pon tu c&aacute;mara en RAW para tener lo m&aacute;s posible al editar."),
            ])
            + note("Un fot&oacute;grafo de verdad siempre captura m&aacute;s de lo que conserva. M&aacute;s opciones ahora significan mejores tres finales despu&eacute;s."))
        es+=deliverables_box(True,
            [("1 hoja de contactos (JPG de alta resoluci&oacute;n):","una hoja de contactos de 12 de tu toma completa, subida a esta tarea de Canvas.")])
        es+=card("IGUALA EL ESTILO","Elige Ajustes que Vayan con el Estilo",
            para("Tus ajustes de c&aacute;mara te ayudan a igualar el estilo de tu maestro. Aqu&iacute; hay algunos puntos de partida:")
            + bullets([
                ("Escena n&iacute;tida y con detalle (como Ansel Adams):","usa un n&uacute;mero f m&aacute;s alto, como f/11, para que toda la escena quede enfocada del frente al fondo."),
                ("Fondo suave detr&aacute;s de una persona (como Platon):","usa un n&uacute;mero f m&aacute;s bajo, como f/2.8, para que la cara quede n&iacute;tida y el fondo se suavice."),
                ("Atrapar un momento en movimiento (como Cartier-Bresson):","usa una velocidad m&aacute;s r&aacute;pida, como 1/500, para que la acci&oacute;n quede n&iacute;tida."),
            ])
            + note("Son puntos de partida, no reglas. Iguala el sentimiento del trabajo de tu maestro."))
        es+=card("DESCARGA TUS FOTOS","Copia Tu Tarjeta a RAW_Images",
            para("No usas un cable. <strong>Descargas</strong> tu tarjeta SD con el <strong>lector de tarjetas</strong> de tu escritorio, luego copias cada foto a tu carpeta del proyecto. Sigue cada paso:")
            + scroll_steps(steps([
                ("Pon tu tarjeta SD en el lector de tarjetas.","Usa el lector de tarjetas que est&aacute; en tu escritorio."),
                ("Abre la tarjeta, luego DCIM, luego 100CANON.","Abre tu tarjeta SD en Finder, abre la carpeta <strong>DCIM</strong>, luego abre <strong>100CANON</strong>. Tus fotos est&aacute;n aqu&iacute;."),
                ("Selecciona todo y copia.","Presiona <strong>Cmd + A</strong> para seleccionar cada foto. Haz clic derecho y elige <strong>Copy</strong> (Copiar)."),
                ("Abre tu carpeta RAW_Images.","En OneDrive, abre tu carpeta del proyecto, luego abre la carpeta <strong>RAW_Images</strong>."),
                ("P&eacute;galas ah&iacute;.","Presiona <strong>Cmd + V</strong> para pegar cada foto en RAW_Images."),
                ("Revisa que el n&uacute;mero coincida.","Espera a que terminen todas. El n&uacute;mero de fotos en RAW_Images debe coincidir con el n&uacute;mero de tu tarjeta."),
                ("Expulsa, regresa y formatea.","Expulsa la tarjeta, ponla de nuevo en la c&aacute;mara y formatea la tarjeta para que est&eacute; limpia para la pr&oacute;xima vez."),
            ]), rgb="0,184,184")
            + note("Descarga tu <strong>toma completa</strong>, cada foto que capturaste. Seleccionas tus mejores tres despu&eacute;s, en el siguiente paso."))
        es+=card("ARMA TU HOJA DE CONTACTOS","Haz Tu Hoja de Contactos de 12",
            para("Una <strong>hoja de contactos de 12</strong> muestra toda tu toma como miniaturas en una p&aacute;gina, 12 por p&aacute;gina. Hazla <strong>antes de editar</strong>: esta es tu toma <strong>sin editar</strong>, y muestra tus ajustes de c&aacute;mara.")
            + para("Primero, trae tus fotos a Lightroom Classic y ponlas en una colecci&oacute;n. Sigue cada paso:")
            + scroll_steps(steps([
                ("Abre Lightroom Classic.","Abre la app en tu Mac."),
                ("Haz clic en Import.","Haz clic en el bot&oacute;n <strong>Import</strong> (Importar), abajo a la izquierda."),
                ("Elige tu carpeta RAW_Images.","A la izquierda, abre tu carpeta del proyecto en OneDrive y haz clic en la carpeta <strong>RAW_Images</strong>. Tus fotos aparecen en el centro."),
                ("Importa cada foto.","Aseg&uacute;rate de que todas tus fotos est&eacute;n marcadas, luego haz clic en <strong>Import</strong> abajo a la derecha."),
                ("Selecciona todas tus fotos.","Ve a la Biblioteca. Presiona <strong>Cmd + A</strong> para seleccionar cada foto importada."),
                ("Haz una colecci&oacute;n llamada Master Photographer.","Haz clic derecho en tus fotos seleccionadas y elige <strong>Create Collection</strong> (Crear colecci&oacute;n). N&oacute;mbrala <strong>Master Photographer</strong>, luego haz clic en Create. As&iacute; tu toma se queda junta."),
            ]), rgb="0,184,184")
            + para("Ahora haz tu hoja de contactos de 12:")
            + steps([
                ("Abre el m&oacute;dulo Print.","Abre tu colecci&oacute;n <strong>Master Photographer</strong>, luego ve al m&oacute;dulo <strong>Print</strong>."),
                ("Elige el ajuste 12-Up Contact Sheet.","El&iacute;gelo de tus User Templates. Si no lo ves, inst&aacute;lalo primero en el Resumen."),
                ("Imprime a un JPG de alta resoluci&oacute;n.","Pon Print To: JPEG File, luego haz clic en Print to File. El ajuste ya guarda un JPG de alta resoluci&oacute;n por ti."),
                ("N&oacute;mbrala y s&uacute;bela.","N&oacute;mbrala <strong>12 Up Master Photographer</strong> y tu nombre, como <strong>12 Up Master Photographer Jane Smith</strong>. Luego sube el JPG a esta tarea de Canvas."),
            ])
            + note("Entrega un <strong>JPG de alta resoluci&oacute;n</strong>, nunca un PDF. El ajuste de hoja de contactos ya guarda el formato correcto.")
            + (note("No dejes que el nombre te confunda. Pon <strong>cada</strong> foto de tu toma. La hoja de 12 cabe 12 por p&aacute;gina, pero no es un m&iacute;nimo. &iquest;M&aacute;s de 12? Lightroom hace m&aacute;s p&aacute;ginas solo. 8 fotos o 32, todo bien.") if not cur else ""))
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 04 - Selecciona y Edita","Elige tus tres im&aacute;genes m&aacute;s fuertes y ed&iacute;talas para igualar el estilo que estudiaste.")

        return wrap_page(f"Step 3: Capture and Contact | Master Photographer | {CL} | PVHS", nav("Step 03",dots_for(2),step_topnav(2)), top_wrap(en,es), step_bottom(2))

    # ================= STEP 04: Cull & Edit =================
    def step04():
        en=banner(f"{PROJ_LABEL} &bull;Step 04","Cull &amp; Edit",
            "Select your three strongest images and edit them to match the look you studied.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
        en+=card("STEP 04 &middot; CHOOSE AND EDIT","Select Your Best Three, Then Edit",
            (float_right(CULL_FLOAT,"A student looking at three selected photos laid out on a table","Cull down to the three photos that best show your master&rsquo;s style.") if HAVE_CULL else "")
            + para("You captured a full take. Now you <strong>cull</strong>, which means you select your strongest work and let the rest go. Choose the <strong>three images</strong> that best show the style of your master photographer.")
            + para("Then <strong>edit</strong> your three selections in Lightroom to match the look you studied: the tones, the contrast, the mood. Make them feel like they belong next to your master&rsquo;s work.")
            + note("Pick the three that are strongest together as a set, not just three nice photos. They should all point to the same style."))
        en+=deliverables_box(False,
            [("3 edited images (high-resolution JPG):","your three final selections, edited in Lightroom and exported as high-resolution JPGs."),
             ("1 contact sheet (high-resolution JPG):","a 6-up contact sheet with your three edited images on it, printed to file as a high-resolution JPG.")], files=4)
        en+=card("CULL YOUR TAKE","Select Your Three Strongest Images",
            para("Work in Lightroom Classic to find your best three.")
            + steps([
                ("Look at your whole take.","In the Library, click through every photo. Compare them, do not just grab the first ones."),
                ("Flag your favorites.","Press P to flag a photo as a pick. Flag more than three at first, then narrow down."),
                ("Choose your final three.","Select the three that best show your master&rsquo;s style and work as a set."),
            ])
            + note("Remember: these are your <strong>selections</strong>, the three strongest images, not just the first three you took."))
        en+=card("EDIT TO MATCH THE STYLE","Give Your Three a Clean Edit",
            para("In the Develop module, edit each of your three images so they match the look you studied.")
            + bullets([
                ("Set exposure and contrast:","get the brightness right, then push contrast toward your master&rsquo;s look."),
                ("Match the tones:","studying a black-and-white master like Adams or Cartier-Bresson? Convert to black and white and build a full tonal range."),
                ("Keep it honest:","edit to strengthen the photo, not to fake it. Clean, strong, and true to your style."),
            ]))
        en+=card("EXPORT AND NAME YOUR FILES","Export High-Resolution JPGs",
            para("Export your final three as high-resolution JPGs with clear names, so your teacher knows whose work it is.")
            + steps([
                ("Select your three edited photos.","In the Library, click all three."),
                ("Export as JPG.","File &rarr; Export. Set the format to JPEG and the quality high."),
                ("Name them by last name and number.","LastName_First_MasterPhotographer_1.jpg, LastName_First_MasterPhotographer_2.jpg, LastName_First_MasterPhotographer_3.jpg."),
                ("Upload all three.","Upload your three edited JPG files to this Canvas assignment."),
            ]))
        en+=card("BUILD YOUR CONTACT SHEET","Make a 6-Up Contact Sheet",
            para("Last, make a <strong>6-up contact sheet</strong> with your three edited images on it. This shows your three final photos together on one page.")
            + steps([
                ("Load your three edited images.","In Lightroom Classic, select your three final edited photos in the Library."),
                ("Open the Print module and pick the 6-Up Contact Sheet preset.","If you do not see it, install it on the Overview first."),
                ("Print to file as a JPG.","Click Print to File. The preset already saves a high-resolution JPG, so you never choose the format."),
                ("Name it and upload.","Name it <strong>6 Up Master Photographer</strong> plus your name, like <strong>6 Up Master Photographer Jane Smith</strong>. Then upload the JPG to this Canvas assignment."),
            ])
            + note("Turn in a <strong>high-resolution JPG</strong>, never a PDF. The contact-sheet preset already saves the right format.")
            + (note("Your 6-up is for your <strong>edited, finished</strong> work, on a black background. It is called 6-up because 6 fit per page, but here you only need your <strong>3</strong> edited photos. Three empty spaces is fine.") if not cur else ""))
        en+=next_up("UP NEXT &middot; STEP 05 - Presentation &amp; Reflection","Finish your PowerPoint, present it to the class, and answer the reflection on the closing page.")

        es=banner(f"{PROJ_LABEL_ES} &bull;Paso 04","Selecciona y Edita",
            "Elige tus tres im&aacute;genes m&aacute;s fuertes y ed&iacute;talas para igualar el estilo que estudiaste.",
            "#top","Back to English", HICON_DESIGN)
        es+=card("PASO 04 &middot; ELIGE Y EDITA","Selecciona Tus Mejores Tres y Luego Edita",
            (float_right(CULL_FLOAT,"Una estudiante mirando tres fotos seleccionadas sobre una mesa","Selecciona las tres fotos que mejor muestren el estilo de tu maestro.") if HAVE_CULL else "")
            + para("Capturaste una toma completa. Ahora <strong>seleccionas</strong>, que significa elegir tu trabajo m&aacute;s fuerte y dejar ir el resto. Elige las <strong>tres im&aacute;genes</strong> que mejor muestren el estilo de tu fot&oacute;grafo maestro.")
            + para("Luego <strong>edita</strong> tus tres selecciones en Lightroom para igualar el estilo que estudiaste: los tonos, el contraste, el ambiente. Haz que se sientan como que pertenecen junto al trabajo de tu maestro.")
            + note("Elige las tres que sean m&aacute;s fuertes juntas como conjunto, no solo tres fotos bonitas. Todas deben apuntar al mismo estilo."))
        es+=deliverables_box(True,
            [("3 im&aacute;genes editadas (JPG de alta resoluci&oacute;n):","tus tres selecciones finales, editadas en Lightroom y exportadas como JPG de alta resoluci&oacute;n."),
             ("1 hoja de contactos (JPG de alta resoluci&oacute;n):","una hoja de contactos de 6 con tus tres im&aacute;genes editadas, impresa a archivo como JPG de alta resoluci&oacute;n.")], files=4)
        es+=card("SELECCIONA TU TOMA","Elige Tus Tres Im&aacute;genes M&aacute;s Fuertes",
            para("Trabaja en Lightroom Classic para encontrar tus mejores tres.")
            + steps([
                ("Mira toda tu toma.","En la Biblioteca, revisa cada foto. Compara, no solo tomes las primeras."),
                ("Marca tus favoritas.","Presiona P para marcar una foto como selecci&oacute;n. Marca m&aacute;s de tres al principio y luego reduce."),
                ("Elige tus tres finales.","Selecciona las tres que mejor muestren el estilo de tu maestro y funcionen como conjunto."),
            ])
            + note("Recuerda: estas son tus <strong>selecciones</strong>, las tres im&aacute;genes m&aacute;s fuertes, no solo las primeras tres que tomaste."))
        es+=card("EDITA PARA IGUALAR EL ESTILO","Dale a Tus Tres una Edici&oacute;n Limpia",
            para("En el m&oacute;dulo Develop (Revelar), edita cada una de tus tres im&aacute;genes para que igualen el estilo que estudiaste.")
            + bullets([
                ("Ajusta exposici&oacute;n y contraste:","deja bien el brillo, luego lleva el contraste hacia el estilo de tu maestro."),
                ("Iguala los tonos:","&iquest;estudiaste a un maestro en blanco y negro como Adams o Cartier-Bresson? Convierte a blanco y negro y construye un rango tonal completo."),
                ("Mant&eacute;nlo honesto:","edita para hacer m&aacute;s fuerte la foto, no para fingirla. Limpio, fuerte y fiel a tu estilo."),
            ]))
        es+=card("EXPORTA Y NOMBRA TUS ARCHIVOS","Exporta JPG de Alta Resoluci&oacute;n",
            para("Exporta tus tres finales como JPG de alta resoluci&oacute;n con nombres claros, para que tu maestro sepa de qui&eacute;n es el trabajo.")
            + steps([
                ("Selecciona tus tres fotos editadas.","En la Biblioteca, haz clic en las tres."),
                ("Exporta como JPG.","File (Archivo) &rarr; Export (Exportar). Pon el formato en JPEG y la calidad alta."),
                ("N&oacute;mbralas por apellido y n&uacute;mero.","LastName_First_MasterPhotographer_1.jpg, LastName_First_MasterPhotographer_2.jpg, LastName_First_MasterPhotographer_3.jpg."),
                ("Sube las tres.","Sube tus tres archivos JPG editados a esta tarea de Canvas."),
            ]))
        es+=card("ARMA TU HOJA DE CONTACTOS","Haz una Hoja de Contactos de 6",
            para("Por &uacute;ltimo, haz una <strong>hoja de contactos de 6</strong> con tus tres im&aacute;genes editadas. Muestra tus tres fotos finales juntas en una p&aacute;gina.")
            + steps([
                ("Carga tus tres im&aacute;genes editadas.","En Lightroom Classic, selecciona tus tres fotos finales editadas en la Biblioteca."),
                ("Abre el m&oacute;dulo Print y elige el ajuste 6-Up Contact Sheet.","Si no lo ves, inst&aacute;lalo primero en el Resumen."),
                ("Imprime a archivo como JPG.","Haz clic en Print to File (Imprimir a archivo). El ajuste ya guarda un JPG de alta resoluci&oacute;n, as&iacute; que nunca eliges el formato."),
                ("N&oacute;mbrala y s&uacute;bela.","N&oacute;mbrala <strong>6 Up Master Photographer</strong> y tu nombre, como <strong>6 Up Master Photographer Jane Smith</strong>. Luego sube el JPG a esta tarea de Canvas."),
            ])
            + note("Entrega un <strong>JPG de alta resoluci&oacute;n</strong>, nunca un PDF. El ajuste de hoja de contactos ya guarda el formato correcto.")
            + (note("Tu hoja de 6 es para tu trabajo <strong>editado y terminado</strong>, con fondo negro. Se llama de 6 porque 6 caben por p&aacute;gina, pero aqu&iacute; solo necesitas tus <strong>3</strong> fotos editadas. Est&aacute; bien dejar 3 espacios vac&iacute;os.") if not cur else ""))
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 05 - Presentaci&oacute;n y Reflexi&oacute;n","Termina tu PowerPoint, pres&eacute;ntalo a la clase y responde la reflexi&oacute;n en la p&aacute;gina final.")

        return wrap_page(f"Step 4: Cull and Edit | Master Photographer | {CL} | PVHS", nav("Step 04",dots_for(3),step_topnav(3)), top_wrap(en,es), step_bottom(3))

    # ================= STEP 05: Presentation & Reflection =================
    def step05():
        en=banner(f"{PROJ_LABEL} &bull;Step 05","Presentation &amp; Reflection",
            "Finish your PowerPoint, present it to the class, and answer the reflection on the closing page.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
        en+=card("STEP 05 &middot; FINISH AND PRESENT","Put Master and Student Work Side by Side",
            (float_right(PRESENT_FLOAT,"A student presenting their master photographer PowerPoint to the class","Present your master&rsquo;s work and your own, side by side.") if HAVE_PRESENT else "")
            + para("Time to finish your PowerPoint. This is your <strong>Fall Final</strong>. You already have your Cover and three Master pages from Step 02. Now add your <strong>three edited photos</strong> and your <strong>reflection</strong>, turn in your PDF, and present on the day of the final.")
            + para("Your PowerPoint shows your master photographer&rsquo;s work and your work <strong>side by side</strong>, so everyone can see what you studied and how you made it your own."))
        en+=deliverables_box(False,
            [("Your finished PowerPoint, exported as a PDF (due before the final):","finish all 8 pages (cover, 3 master pages, your 3 edited photos, and the reflection closing page), export it as a PDF, and upload the PDF <strong>before the day of the final</strong>. Turning it in early lets the presentation order be ready for final day. You present your PowerPoint to the class on the day of the final.")])
        en+=deck_showcase(False, DECKPREV)
        en+=card("BUILD THE REST OF YOUR POWERPOINT","Add Your Photos and Your Notes",
            para("Open the PowerPoint you started in Step 02 and finish it.")
            + steps([
                ("Add your three edited photos.","Place one of your final JPGs on each of the three My Work pages."),
                ("Write how you used your master&rsquo;s style.","On each page, say what you borrowed: composition, light, the moment, tonal range, or editing."),
                ("Fill the reflection page.","Answer the three reflection questions on the closing page."),
                ("Check every page.","Make sure your name is on the cover and all six images are in place."),
                ("Export a PDF and upload.","In PowerPoint, go to File &gt; Export and choose PDF, then upload the PDF to this Canvas assignment."),
            ]))
        en+=card("PRESENT ON FINAL DAY","Share Your Work Out Loud",
            para("On the <strong>day of the Fall Final</strong>, you present your PowerPoint to the class. Your PDF is already turned in, so today you just present. This presentation <strong>is</strong> your final. Keep it short and clear, about <strong>3 to 5 minutes</strong>.")
            + bullets([
                ("Introduce your master:","who they are and the style you studied."),
                ("Walk through your three master images:","name the technique on each one."),
                ("Show your three photos:","explain how each one shows your master&rsquo;s influence."),
                ("End with your reflection:","what you learned and what you will carry forward."),
            ])
            + note("Come ready on final day: your PDF already turned in before today, and your part practiced. Speak clearly and look up at your classmates. You know your work better than anyone in the room."))
        en+=card("REFLECTION &middot; CLOSING PAGE","Finish With an Honest Reflection",
            para("Your last page is your <strong>reflection</strong>. Answer these three questions in a few honest sentences:")
            + bullets([
                ("What you learned:","what is the most important thing you learned from your master photographer?"),
                ("What changed:","how did studying their work change the way you capture or edit your own photos?"),
                ("What is next:","what will you carry into your next photography project?"),
            ]))
        en+=next_up("YOU DID IT &middot; PROJECT COMPLETE","You studied a master, made the style your own, and presented it. That is how real photographers grow.")

        es=banner(f"{PROJ_LABEL_ES} &bull;Paso 05","Presentaci&oacute;n y Reflexi&oacute;n",
            "Termina tu PowerPoint, pres&eacute;ntalo a la clase y responde la reflexi&oacute;n en la p&aacute;gina final.",
            "#top","Back to English", HICON_REFLECT)
        es+=card("PASO 05 &middot; TERMINA Y PRESENTA","Pon el Trabajo del Maestro y el Tuyo Lado a Lado",
            (float_right(PRESENT_FLOAT,"Una estudiante presentando su PowerPoint del fot&oacute;grafo maestro a la clase","Presenta el trabajo de tu maestro y el tuyo, lado a lado.") if HAVE_PRESENT else "")
            + para("Hora de terminar tu PowerPoint. Este es tu <strong>Final de Oto&ntilde;o</strong>. Ya tienes tu portada y tus tres p&aacute;ginas del maestro del Paso 02. Ahora agrega tus <strong>tres fotos editadas</strong> y tu <strong>reflexi&oacute;n</strong>, entrega tu PDF y presenta el d&iacute;a del final.")
            + para("Tu PowerPoint muestra el trabajo de tu fot&oacute;grafo maestro y el tuyo <strong>lado a lado</strong>, para que todos vean qu&eacute; estudiaste y c&oacute;mo lo hiciste tuyo."))
        es+=deliverables_box(True,
            [("Tu PowerPoint terminado, exportado como PDF (se entrega antes del final):","termina las 8 p&aacute;ginas (portada, 3 p&aacute;ginas del maestro, tus 3 fotos editadas y la p&aacute;gina final de reflexi&oacute;n), exp&oacute;rtalo como PDF y sube el PDF <strong>antes del d&iacute;a del final</strong>. Entregarlo temprano deja listo el orden de las presentaciones para el d&iacute;a del final. Presentas tu PowerPoint a la clase el d&iacute;a del final.")])
        es+=deck_showcase(True, DECKPREV)
        es+=card("CONSTRUYE EL RESTO DE TU POWERPOINT","Agrega Tus Fotos y Tus Notas",
            para("Abre el PowerPoint que empezaste en el Paso 02 y term&iacute;nalo.")
            + steps([
                ("Agrega tus tres fotos editadas.","Coloca uno de tus JPG finales en cada una de las tres p&aacute;ginas de Tu Trabajo."),
                ("Escribe c&oacute;mo usaste el estilo de tu maestro.","En cada p&aacute;gina, di qu&eacute; tomaste prestado: composici&oacute;n, luz, el momento, el rango tonal o la edici&oacute;n."),
                ("Llena la p&aacute;gina de reflexi&oacute;n.","Responde las tres preguntas de reflexi&oacute;n en la p&aacute;gina final."),
                ("Revisa cada p&aacute;gina.","Aseg&uacute;rate de que tu nombre est&eacute; en la portada y las seis im&aacute;genes est&eacute;n en su lugar."),
                ("Exporta un PDF y s&uacute;belo.","En PowerPoint, ve a File (Archivo) &gt; Export (Exportar) y elige PDF, luego sube el PDF a esta tarea de Canvas."),
            ]))
        es+=card("PRESENTA EL D&Iacute;A DEL FINAL","Comparte Tu Trabajo en Voz Alta",
            para("El <strong>d&iacute;a del Final de Oto&ntilde;o</strong>, presentas tu PowerPoint a la clase. Tu PDF ya est&aacute; entregado, as&iacute; que hoy solo presentas. Esta presentaci&oacute;n <strong>es</strong> tu examen final. Que sea corto y claro, como <strong>3 a 5 minutos</strong>.")
            + bullets([
                ("Presenta a tu maestro:","qui&eacute;n es y el estilo que estudiaste."),
                ("Recorre tus tres im&aacute;genes del maestro:","nombra la t&eacute;cnica en cada una."),
                ("Muestra tus tres fotos:","explica c&oacute;mo cada una muestra la influencia de tu maestro."),
                ("Termina con tu reflexi&oacute;n:","qu&eacute; aprendiste y qu&eacute; vas a llevarte contigo."),
            ])
            + note("Ven listo el d&iacute;a del final: tu PDF ya entregado antes de hoy, y tu parte practicada. Habla con claridad y mira a tus compa&ntilde;eros. T&uacute; conoces tu trabajo mejor que nadie en el sal&oacute;n."))
        es+=card("REFLEXI&Oacute;N &middot; P&Aacute;GINA FINAL","Termina con una Reflexi&oacute;n Honesta",
            para("Tu &uacute;ltima p&aacute;gina es tu <strong>reflexi&oacute;n</strong>. Responde estas tres preguntas en unas cuantas oraciones honestas:")
            + bullets([
                ("Qu&eacute; aprendiste:","&iquest;qu&eacute; es lo m&aacute;s importante que aprendiste de tu fot&oacute;grafo maestro?"),
                ("Qu&eacute; cambi&oacute;:","&iquest;c&oacute;mo cambi&oacute; estudiar su trabajo la forma en que capturas o editas tus propias fotos?"),
                ("Qu&eacute; sigue:","&iquest;qu&eacute; vas a llevar a tu pr&oacute;ximo proyecto de fotograf&iacute;a?"),
            ]))
        es+=next_up("LO LOGRASTE &middot; PROYECTO COMPLETO","Estudiaste a un maestro, hiciste tuyo el estilo y lo presentaste. As&iacute; crecen los fot&oacute;grafos de verdad.")

        return wrap_page(f"Step 5: Presentation and Reflection | Master Photographer | {CL} | PVHS", nav("Step 05",dots_for(4),step_topnav(4)), top_wrap(en,es), step_bottom(4))

    outdir = os.path.join(ROOT,"curriculum/shared") if cur else os.path.join(ROOT,"share/master-photographer")
    os.makedirs(outdir, exist_ok=True)
    for fname,gen in zip(FILES,[overview,step02,step03,step04,step05]):
        html=ent(gen())
        assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
        assert "–" not in html and "&ndash;" not in html, "en dash in "+fname
        ban_check(html, fname)
        open(os.path.join(outdir,fname),"w",encoding="utf-8").write(html)
        print(f"wrote {mode}", fname, len(html), "bytes")

# Purple note helper (for callouts inside a purple resources_card).
def pnote_mp(t):
    return (f'<div style="background:rgba(139,92,246,0.12);border:1px solid rgba(139,92,246,0.30);border-left:4px solid #8b5cf6;padding:11px 14px;margin:8px 0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

if __name__=="__main__":
    for C in COURSES:
        build("cur", C)        # in-curriculum module for each course (photo1 + photo2)
    build("std", COURSES[0])   # standalone public share copy at share/master-photographer/ (built from Photo 1)
