#!/usr/bin/env python3
# Photography 1A - Project 02: Master Photographer.
# Pick one of five master photographers, study HOW they make images (style, technique, impact),
# then capture and edit three of your own photos in that style and present master + student work
# side by side in a slide deck. Standard photo arc: study -> capture & contact -> cull & edit ->
# presentation (reflection is the deck's closing slide). Five pages, bilingual EN/ES, 5th-grade.
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

PROJNUM="02"            # catalog label is "Project 02" (change to a module number to reclassify)
# Student-facing banner eyebrow (Chris 2026-11-15: this is the Fall Final Project).
PROJ_LABEL="Fall Final Project"
PROJ_LABEL_ES="Proyecto Final de Oto&ntilde;o"
CL_EN="Photography 1A"
IMGDIR=f"{SITE}/assets/images/master-photographer"
HERO=f"{IMGDIR}/master-photographer-hero-v1.jpg"
RESEARCH_FLOAT=f"{IMGDIR}/research-float-v1.jpg"       # Step 02 (student researching at the iMac)
CULL_FLOAT=f"{IMGDIR}/cull-float-v1.jpg"               # Step 04 (student with her three selected prints)
PRESENT_FLOAT=f"{IMGDIR}/presentation-float-v1.jpg"    # Step 05 (student presenting selected works)
DECK_PREVIEW=f"{IMGDIR}/deck-template-preview-v1.jpg"  # 2x2 preview of the slide template
PROJECT_ZIP=f"{SITE}/assets/templates/master-photographer/Master-Photographer-Project-Folder.zip"
DECK_PPTX=f"{SITE}/assets/templates/master-photographer/Master-Photographer-Slide-Template.pptx"
# Contact-sheet presets are installed once (Image Series module); same install video.
CS_INSTALL_VIDEO="https://vimeo.com/1164128764/e1842e523e?share=copy&amp;fl=sv&amp;fe=ci"

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
   "en_desc":"You build a slideshow and present it to the class, showing how your photos connect to your master photographer.",
   "es_desc":"Creas una presentaci&oacute;n y la presentas a la clase, mostrando c&oacute;mo tus fotos se conectan con tu fot&oacute;grafo maestro."},
  {"code":"CTE AME A4.0","en_tier":"CA CTE, Arts Media &amp; Entertainment","es_tier":"CTE de California, Artes y Medios",
   "en_title":"Analyze &amp; Assess Work","es_title":"Analizar y Evaluar el Trabajo",
   "en_desc":"You judge photographs using the elements of art, the principles of design, and professional industry standards.",
   "es_desc":"Juzgas fotograf&iacute;as usando los elementos del arte, los principios del dise&ntilde;o y los est&aacute;ndares profesionales de la industria."},
]

VOCAB_EN=[
 ("Master Photographer","A photographer whose work is studied and respected around the world. You pick one to study in this project."),
 ("Composition","How you arrange everything inside the frame: where the subject sits, what is behind them, and what you leave out."),
 ("The Decisive Moment","The exact instant when everything in the frame lines up into one strong photo. Henri Cartier-Bresson made this idea famous."),
 ("Tonal Range","All the shades from pure black to pure white in a photo. Ansel Adams was a master of a full tonal range in black and white."),
 ("Environmental Portrait","A photo of a person in their own space, so the place around them helps tell who they are."),
 ("Influence","When one artist&rsquo;s style shapes another artist&rsquo;s work. Your master photographer influences your three photos."),
]
VOCAB_ES=[
 ("Master Photographer (Fot&oacute;grafo Maestro)","Un fot&oacute;grafo cuyo trabajo se estudia y se respeta en todo el mundo. Eliges a uno para estudiarlo en este proyecto."),
 ("Composition (Composici&oacute;n)","C&oacute;mo acomodas todo dentro del encuadre: d&oacute;nde est&aacute; el sujeto, qu&eacute; hay detr&aacute;s y qu&eacute; dejas fuera."),
 ("The Decisive Moment (El Momento Decisivo)","El instante exacto en que todo en el encuadre se alinea en una sola foto fuerte. Henri Cartier-Bresson hizo famosa esta idea."),
 ("Tonal Range (Rango Tonal)","Todos los tonos desde el negro puro hasta el blanco puro en una foto. Ansel Adams fue un maestro del rango tonal completo en blanco y negro."),
 ("Environmental Portrait (Retrato Ambiental)","Una foto de una persona en su propio espacio, para que el lugar a su alrededor ayude a contar qui&eacute;n es."),
 ("Influence (Influencia)","Cuando el estilo de un artista da forma al trabajo de otro. Tu fot&oacute;grafo maestro influye en tus tres fotos."),
]

# ---------------- The five masters (genre, summary, what to look for) ----------------
MASTERS_EN=[
 ("Landscape","Ansel Adams",
  "Ansel Adams took huge black-and-white photos of the American West: mountains, rivers, and national parks like Yosemite. He is famous for razor-sharp detail and a full range of tones, from deep black to bright white. He planned his exposure and printing with a method he helped invent called the Zone System.",
  "Look at how he uses the whole range from pure black to pure white. Notice the sharp focus from the front of the photo all the way to the back."),
 ("Documentary","Sebasti&atilde;o Salgado",
  "Sebasti&atilde;o Salgado is a photographer from Brazil. He spends years on big black-and-white projects about workers, people who had to leave their homes, and the natural world. His photos use strong light and deep shadows to make real life feel powerful and important.",
  "Look at the dramatic light and the high contrast. Notice how he photographs real people and real moments with respect."),
 ("Portrait / Editorial","Annie Leibovitz",
  "Annie Leibovitz is known for famous portraits of musicians, actors, and leaders. She often builds a whole scene with bold color and dramatic light, so the photo tells a story about the person. Her pictures appear on magazine covers.",
  "Look at how she builds a scene around the person and uses color and light. Notice how the setting tells you who they are."),
 ("Portrait / Close-up","Platon",
  "Platon makes tight, close-up portraits of world leaders and famous people. He uses a plain background and strong, simple studio light, so there is nothing to look at but the person&rsquo;s face and eyes. His photos feel honest and powerful.",
  "Look at how close he gets and how simple the background is. Notice the direct eye contact and the strong light on the face."),
 ("Street / Documentary","Henri Cartier-Bresson",
  "Henri Cartier-Bresson was a photographer from France. He walked the streets with a small camera and waited for &lsquo;the decisive moment,&rsquo; the exact second when everything in the frame lines up into one strong photo. His black-and-white street photos are famous for perfect timing and clean composition.",
  "Look for perfect timing and clean composition. Notice how people, shapes, and lines all come together at the right second."),
]
MASTERS_ES=[
 ("Paisaje","Ansel Adams",
  "Ansel Adams tomaba enormes fotos en blanco y negro del Oeste de Estados Unidos: monta&ntilde;as, r&iacute;os y parques nacionales como Yosemite. Es famoso por el detalle muy n&iacute;tido y un rango completo de tonos, del negro profundo al blanco brillante. Planeaba su exposici&oacute;n y su impresi&oacute;n con un m&eacute;todo que ayud&oacute; a inventar, el Sistema de Zonas.",
  "Mira c&oacute;mo usa todo el rango del negro puro al blanco puro. Fíjate en el enfoque n&iacute;tido desde el frente de la foto hasta el fondo."),
 ("Documental","Sebasti&atilde;o Salgado",
  "Sebasti&atilde;o Salgado es un fot&oacute;grafo de Brasil. Pasa a&ntilde;os en grandes proyectos en blanco y negro sobre trabajadores, personas que tuvieron que dejar su hogar y la naturaleza. Sus fotos usan luz fuerte y sombras profundas para que la vida real se sienta poderosa e importante.",
  "Mira la luz dram&aacute;tica y el alto contraste. Fíjate en c&oacute;mo fotograf&iacute;a a personas y momentos reales con respeto."),
 ("Retrato / Editorial","Annie Leibovitz",
  "Annie Leibovitz es conocida por retratos famosos de m&uacute;sicos, actores y l&iacute;deres. Muchas veces arma toda una escena con color fuerte y luz dram&aacute;tica, para que la foto cuente una historia sobre la persona. Sus im&aacute;genes salen en portadas de revistas.",
  "Mira c&oacute;mo arma una escena alrededor de la persona y usa el color y la luz. Fíjate en c&oacute;mo el lugar te dice qui&eacute;n es."),
 ("Retrato / Primer Plano","Platon",
  "Platon hace retratos cerrados y de primer plano de l&iacute;deres del mundo y personas famosas. Usa un fondo simple y una luz de estudio fuerte y sencilla, para que no haya nada que mirar m&aacute;s que la cara y los ojos de la persona. Sus fotos se sienten honestas y poderosas.",
  "Mira qu&eacute; tan cerca llega y qu&eacute; tan simple es el fondo. Fíjate en el contacto directo con los ojos y la luz fuerte en la cara."),
 ("Calle / Documental","Henri Cartier-Bresson",
  "Henri Cartier-Bresson fue un fot&oacute;grafo de Francia. Caminaba por las calles con una c&aacute;mara peque&ntilde;a y esperaba &lsquo;el momento decisivo,&rsquo; el segundo exacto en que todo en el encuadre se alinea en una sola foto fuerte. Sus fotos de calle en blanco y negro son famosas por el momento perfecto y la composici&oacute;n limpia.",
  "Busca el momento perfecto y la composici&oacute;n limpia. Fíjate en c&oacute;mo las personas, las formas y las l&iacute;neas se juntan en el segundo correcto."),
]

RESLINKS=[
 ("https://anseladams.com/","Ansel Adams, official site"),
 ("https://www.amazonasimages.com/","Sebasti&atilde;o Salgado, Amazonas Images studio"),
 ("https://www.artsy.net/artist/annie-leibovitz","Annie Leibovitz on Artsy"),
 ("https://platonphoto.com/","Platon, official site"),
 ("https://www.henricartierbresson.org/en/","Henri Cartier-Bresson Foundation"),
]
GENERAL_SITES=[
 ("https://www.artsy.net/","Artsy.net"),
 ("https://www.moma.org/","MoMA.org"),
 ("https://www.magnumphotos.com/","MagnumPhotos.com"),
 ("https://www.tate.org.uk/","Tate.org.uk"),
 ("https://www.getty.edu/","Getty.edu"),
]

# ---------------- Student rubric (collapsed gold accordion on the Overview) ----------------
RUBRIC_EN=[
 ("Study &amp; Analysis","You clearly explain how your master photographer makes images, naming real techniques, not just &lsquo;I like it.&rsquo;"),
 ("Three Master Images","You choose three strong images and write a true technique note for each one."),
 ("Capture","Your full take shows the style of your master photographer and gives you strong options."),
 ("Cull &amp; Edit","Your three final images are your strongest, well selected, and edited to match the look you studied."),
 ("Style Connection","Your photos clearly show the influence of your master photographer."),
 ("Presentation","Your deck is clean and easy to read, and you present clearly and on time."),
 ("Reflection","Your closing slide is honest and thoughtful about what you learned."),
]
RUBRIC_ES=[
 ("Estudio y An&aacute;lisis","Explicas con claridad c&oacute;mo tu fot&oacute;grafo maestro hace im&aacute;genes, nombrando t&eacute;cnicas reales, no solo &lsquo;me gusta.&rsquo;"),
 ("Tres Im&aacute;genes del Maestro","Eliges tres im&aacute;genes fuertes y escribes una nota de t&eacute;cnica verdadera para cada una."),
 ("Captura","Tu toma completa muestra el estilo de tu fot&oacute;grafo maestro y te da buenas opciones."),
 ("Selecci&oacute;n y Edici&oacute;n","Tus tres im&aacute;genes finales son las m&aacute;s fuertes, bien seleccionadas y editadas para igualar el estilo que estudiaste."),
 ("Conexi&oacute;n de Estilo","Tus fotos muestran con claridad la influencia de tu fot&oacute;grafo maestro."),
 ("Presentaci&oacute;n","Tu presentaci&oacute;n es limpia y f&aacute;cil de leer, y presentas con claridad y a tiempo."),
 ("Reflexi&oacute;n","Tu diapositiva final es honesta y reflexiva sobre lo que aprendiste."),
]
def rubric_box(es):
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
    summary=(f'<summary style="list-style:none;cursor:pointer;display:flex;align-items:center;gap:12px;">'
      f'<img src="{DELIVER_ICON}" alt="" style="width:40px;height:40px;flex:0 0 auto;display:block;" />'
      f'<span style="display:block;"><span style="display:block;font-size:10.5pt;font-weight:bold;letter-spacing:0.1em;text-transform:uppercase;color:#ffd166;">{"R&Uacute;BRICA" if es else "RUBRIC"}</span>'
      f'<span style="display:block;font-size:15pt;font-weight:bold;color:#ffffff;line-height:1.3;">{heading}</span>'
      f'<span style="display:block;font-size:11.5pt;color:rgba(255,255,255,0.72);margin-top:2px;">{sub}</span></span></summary>')
    return ('<details style="background:linear-gradient(180deg,rgba(245,179,1,0.12) 0%,rgba(245,179,1,0.03) 100%);border:1px solid rgba(245,179,1,0.35);border-left:5px solid #f5b301;padding:22px 26px;overflow:hidden;margin-bottom:24px;">'
      + summary
      + f'<div style="margin-top:18px;padding-top:16px;border-top:1px solid rgba(245,179,1,0.22);">{items}</div>'
      + '</details>')

def project_downloads(es):
    heading="Descarga Tu Carpeta del Proyecto" if es else "Download Your Project Folder"
    if es:
        lead="Descarga la carpeta del proyecto Master_Photographer. Trae tu plantilla de presentaci&oacute;n de 16:9 y una carpeta RAW_Images donde ir&aacute;n tus fotos cuando las captures."
        label="Carpeta del Proyecto Master_Photographer (ZIP)"
        note_t="Despu&eacute;s de que se descargue, descompr&iacute;mela y mueve la carpeta Master_Photographer a OneDrive &rarr; Carpeta de Fotograf&iacute;a. Esa es tu carpeta para todo este proyecto."
    else:
        lead="Download the Master_Photographer project folder. It holds your 16:9 slideshow template and a RAW_Images folder where your photos will go once you capture them."
        label="Master_Photographer Project Folder (ZIP)"
        note_t="After it downloads, unzip it and move the Master_Photographer folder into OneDrive &rarr; Photography Folder. That is your folder for this whole project."
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">' + dl_link(PROJECT_ZIP, label, row=True) + '</div>'
      + note_orange(note_t) + '</div>')

def reslist(es):
    lead=("Buenos lugares para ver fotos y leer sobre fot&oacute;grafos. Empieza con el sitio de tu maestro, luego explora los dem&aacute;s."
          if es else "Good places to see photos and read about photographers. Start with your master&rsquo;s own site, then explore the rest.")
    ph_head="Tu Fot&oacute;grafo Maestro" if es else "Your Master Photographer"
    gen_head="Sitios de Investigaci&oacute;n" if es else "Research Sites"
    def rows(pairs):
        out='<div style="display:flex;flex-direction:column;gap:8px;margin:8px 0 4px;">'
        for url,lab in pairs: out+=reslink(url,lab)
        return out+'</div>'
    return (para(lead)
      + f'<div style="font-size:10.5pt;font-weight:bold;letter-spacing:0.08em;text-transform:uppercase;color:#c4b5fd;margin:14px 0 2px;">{ph_head}</div>'
      + rows(RESLINKS)
      + f'<div style="font-size:10.5pt;font-weight:bold;letter-spacing:0.08em;text-transform:uppercase;color:#c4b5fd;margin:16px 0 2px;">{gen_head}</div>'
      + rows(GENERAL_SITES))

def deck_showcase(es):
    heading="Tu Plantilla de Presentaci&oacute;n" if es else "Your Slide Deck Template"
    if es:
        lead="Usa esta plantilla de 16:9 como punto de partida. Du&eacute;rala y hazla tuya. Tiene todo lo que necesitas:"
        items=[
            ("Portada:","el nombre de tu fot&oacute;grafo maestro, tu nombre, tu periodo y el curso."),
            ("3 diapositivas del maestro:","una imagen de tu maestro por diapositiva, con la t&eacute;cnica que estudiaste."),
            ("3 diapositivas de tu trabajo:","una de tus fotos editadas por diapositiva, con c&oacute;mo usaste lo que aprendiste."),
            ("Diapositiva de reflexi&oacute;n:","la diapositiva final, donde respondes la reflexi&oacute;n."),
        ]
        inside="La plantilla ya est&aacute; dentro de la carpeta del proyecto que descargaste, o puedes bajarla directo aqu&iacute;."
        label="Plantilla de Presentaci&oacute;n (.pptx)"
        cap="Las 8 diapositivas de la plantilla: portada, tres del maestro, tres de tu trabajo y la reflexi&oacute;n."
    else:
        lead="Use this 16:9 template as your starting point. Duplicate it and make it yours. It has everything you need:"
        items=[
            ("Cover slide:","your master photographer&rsquo;s name, your name, your period, and the course."),
            ("3 master slides:","one master image per slide, with the technique you studied."),
            ("3 of-your-work slides:","one of your edited photos per slide, with how you used what you learned."),
            ("Reflection slide:","the closing slide, where you answer the reflection."),
        ]
        inside="The template is already inside the project folder you downloaded, or you can grab it straight here."
        label="Slide Deck Template (.pptx)"
        cap="All 8 template slides: cover, three master, three of your work, and the reflection."
    inner=(para(lead)+bullets(items,accent="#8b5cf6")
      + (framed(DECK_PREVIEW, "A preview of the eight-slide Master Photographer template: cover, three master slides, three student slides, and the reflection")
         + f'<div style="font-size:11pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.45;">{cap}</div>' if HAVE_DECK_PREVIEW else "")
      + para(inside)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:10px;">' + dl_link(DECK_PPTX, label, row=True) + '</div>')
    return resources_card(heading, inner, es)

def wrap_standalone(title, nav_inner, top_html, bottom, files_std, share_name):
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

def build(mode):
    cur = (mode == "cur")
    OVER="photo1-master-photographer-overview.html"
    S2="photo1-master-photographer-step02-meet-the-five.html"
    S3="photo1-master-photographer-step03-capture-contact.html"
    S4="photo1-master-photographer-step04-cull-edit.html"
    S5="photo1-master-photographer-step05-presentation-reflection.html"
    FILES_STD=["index.html","step02-meet-the-five.html","step03-capture-contact.html",
               "step04-cull-edit.html","step05-presentation-reflection.html"]
    FILES = [OVER,S2,S3,S4,S5] if cur else FILES_STD
    HREFS = FILES
    TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04"),("5","Step 05")]
    STEPNUM=["01","02","03","04","05"]
    SHARE_NAME="Master Photographer"

    def wrap_page(title, nav_inner, top_html, bottom):
        if cur:
            return _sf.wrap_page(title, nav_inner, top_html, bottom)
        return wrap_standalone(title, nav_inner, top_html, bottom, FILES_STD, SHARE_NAME)

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

    def master_cards(es):
        data=MASTERS_ES if es else MASTERS_EN
        look=("Qu&eacute; observar:" if es else "What to look for:")
        out=""
        for genre,name,summary,watch in data:
            out+=card(genre,name, para(summary)+note(f"<strong>{look}</strong> {watch}"))
        return out

    # ================= OVERVIEW (Step 01) =================
    def overview():
        en=banner(f"{PROJ_LABEL} &bull;Step 01","Master Photographer",
            "Study one master photographer, then capture and present three photos in their style. Read this page, then go to Step 02.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_CAMERA_KIT)
        en+=type_card("overview","Step 01 &middot; Overview","Learn From a Master, Then Make Your Own",
            para("In this project you pick <strong>one of five master photographers</strong> and study <strong>how they make their images</strong>. This is not a report about their life. You study their <strong>style, technique, and impact</strong>: how they compose, light, and edit their photos.")
            + para("Then you become the photographer. You <strong>capture three of your own photos</strong> in that style with the school camera kit, edit your best three, and present your master&rsquo;s work and your work <strong>side by side</strong> in a slideshow.")
            + (framed(HERO,"Five master photographers, each with a camera: the five you choose from in this project") + '<div style="font-size:11pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.45;">Five masters, five different styles. You pick one to study and bring into your own photos.</div>' if HAVE_HERO else ""))
        en+=project_downloads(False)
        en+=card("HOW THIS PROJECT WORKS","From Studying a Master to Your Own Photos",
            para("You are on Step 01 now: read this page so you understand the project. Here is the path.")
            + bullets([
                ("Step 02 &middot; Meet the Five &amp; Choose:","meet the five master photographers, pick one, and start your slide deck with three of their images."),
                ("Step 03 &middot; Capture &amp; Contact:","capture a full take of your own photos in your master&rsquo;s style, then build a contact sheet."),
                ("Step 04 &middot; Cull &amp; Edit:","select your three strongest images and edit them to match the look you studied."),
                ("Step 05 &middot; Presentation &amp; Reflection:","finish your slideshow, present it to the class, and answer the reflection on the closing slide."),
            ]))
        en+=card("WHY THIS MATTERS","See Like a Pro",
            para("Understanding <strong>how professional photographers make their images</strong> helps you make stronger choices in your own work. When you can name what makes a photo great, you can do it on purpose.")
            + note("You keep your three master images and your three photos together, so everyone can see where your ideas came from and how you made them your own."))
        en+=rubric_box(False)
        en+=standards_box(False, STANDARDS)
        en+=resources_card("Key Words",
            vocab_grid("On the Quiz",
              "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
              VOCAB_EN), False)
        en+=next_up("UP NEXT &middot; STEP 02 - Meet the Five &amp; Choose","Meet the five master photographers, pick the one whose work pulls you in, and start your deck.")

        es=banner(f"{PROJ_LABEL_ES} &bull;Paso 01","Fot&oacute;grafo Maestro",
            "Estudia a un fot&oacute;grafo maestro, luego captura y presenta tres fotos en su estilo. Lee esta p&aacute;gina y ve al Paso 02.",
            "#top","Back to English", HICON_CAMERA_KIT)
        es+=type_card("overview","Paso 01 &middot; Resumen","Aprende de un Maestro, Luego Haz lo Tuyo",
            para("En este proyecto eliges a <strong>uno de cinco fot&oacute;grafos maestros</strong> y estudias <strong>c&oacute;mo hacen sus im&aacute;genes</strong>. Esto no es un reporte sobre su vida. Estudias su <strong>estilo, su t&eacute;cnica y su impacto</strong>: c&oacute;mo componen, iluminan y editan sus fotos.")
            + para("Luego t&uacute; te vuelves el fot&oacute;grafo. <strong>Capturas tres fotos propias</strong> en ese estilo con el kit de c&aacute;mara de la escuela, editas tus mejores tres y presentas el trabajo de tu maestro y el tuyo <strong>lado a lado</strong> en una presentaci&oacute;n.")
            + (framed(HERO,"Cinco fot&oacute;grafos maestros, cada uno con una c&aacute;mara: los cinco entre los que eliges en este proyecto") + '<div style="font-size:11pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.45;">Cinco maestros, cinco estilos distintos. Eliges a uno para estudiarlo y traerlo a tus propias fotos.</div>' if HAVE_HERO else ""))
        es+=project_downloads(True)
        es+=card("C&Oacute;MO FUNCIONA ESTE PROYECTO","De Estudiar a un Maestro a Tus Propias Fotos",
            para("Est&aacute;s en el Paso 01 ahora: lee esta p&aacute;gina para entender el proyecto. Este es el camino.")
            + bullets([
                ("Paso 02 &middot; Conoce a los Cinco y Elige:","conoce a los cinco fot&oacute;grafos maestros, elige a uno y empieza tu presentaci&oacute;n con tres de sus im&aacute;genes."),
                ("Paso 03 &middot; Captura y Contacto:","captura una toma completa de tus propias fotos en el estilo de tu maestro, luego arma una hoja de contactos."),
                ("Paso 04 &middot; Selecciona y Edita:","elige tus tres im&aacute;genes m&aacute;s fuertes y ed&iacute;talas para igualar el estilo que estudiaste."),
                ("Paso 05 &middot; Presentaci&oacute;n y Reflexi&oacute;n:","termina tu presentaci&oacute;n, pres&eacute;ntala a la clase y responde la reflexi&oacute;n en la diapositiva final."),
            ]))
        es+=card("POR QU&Eacute; IMPORTA","Mira Como un Profesional",
            para("Entender <strong>c&oacute;mo los fot&oacute;grafos profesionales hacen sus im&aacute;genes</strong> te ayuda a tomar mejores decisiones en tu propio trabajo. Cuando puedes nombrar lo que hace grande a una foto, puedes hacerlo a prop&oacute;sito.")
            + note("Mantienes tus tres im&aacute;genes del maestro y tus tres fotos juntas, para que todos vean de d&oacute;nde vinieron tus ideas y c&oacute;mo las hiciste tuyas."))
        es+=rubric_box(True)
        es+=standards_box(True, STANDARDS)
        es+=resources_card("Palabras Clave",
            vocab_grid("En el Examen",
              "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
              VOCAB_ES), True)
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 02 - Conoce a los Cinco y Elige","Conoce a los cinco fot&oacute;grafos maestros, elige al que m&aacute;s te atraiga y empieza tu presentaci&oacute;n.")

        return wrap_page(f"Master Photographer | {CL_EN} | PVHS", nav("Step 01",dots_for(0),step_topnav(0)), top_wrap(en,es), step_bottom(0))

    # ================= STEP 02: Meet the Five & Choose =================
    def step02():
        en=banner(f"{PROJ_LABEL} &bull;Step 02","Meet the Five &amp; Choose",
            "Meet the five master photographers, pick one, and start your slide deck with three of their images.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
        en+=card("STEP 02 &middot; STUDY YOUR MASTER","Pick One, Then Study How They Work",
            (float_right(RESEARCH_FLOAT,"A student researching a master photographer on a lab computer","Study their style online before you choose. Look at a lot of their photos.") if HAVE_RESEARCH else "")
            + para("Below are your <strong>five master photographers</strong>. Each one works in a different style. Read all five, look at their photos online, then <strong>pick the one</strong> whose work pulls you in the most.")
            + para("You are studying <strong>how they make images</strong>, not their life story. For your master, look closely at their <strong>composition, light, subjects, and editing</strong>. These are the ideas you will bring into your own three photos.")
            + note("Choose the photographer you would most want to photograph like. The more their work excites you, the stronger your own photos will be."))
        en+=deliverables_box(False,
            [("Your deck, started (PDF):","download the slide template, fill the <strong>Cover slide</strong> and your <strong>3 Master Photographer slides</strong> (one image you chose on each, plus your technique note), export it as a PDF, and upload it to this Canvas assignment.")])
        en+=master_cards(False)
        en+=resources_card("Where to See Their Work", reslist(False), False)
        en+=card("GATHER YOUR THREE IMAGES / START YOUR DECK","Choose 3 Images and Start Your Slideshow",
            para("Now build the first part of your slideshow. Open the <strong>slide template</strong> from your project folder, then do this:")
            + steps([
                ("Fill the Cover slide.","Type your master photographer&rsquo;s name, your name, your period, and the course."),
                ("Find three strong images by your master.","Search online for three of their photos that best show their style. Save them in your project folder."),
                ("Place one image on each Master slide.","Put one image on each of the three Master Photographer slides in the template."),
                ("Write your technique note on each.","On each slide, name the technique you see: composition, lighting, the moment, tonal range, or editing. Say why it works."),
                ("Export a PDF and upload.","Go to File &gt; Export To &gt; PDF (or File &gt; Save a Copy as PDF), then upload the PDF to this Canvas assignment."),
            ])
            + note("These three images are your <strong>master photographer&rsquo;s</strong> work, from online. You capture your <strong>own</strong> photos next, in Step 03."))
        en+=next_up("UP NEXT &middot; STEP 03 - Capture &amp; Contact","Check out a camera kit and capture a full take of your own photos in your master&rsquo;s style.")

        es=banner(f"{PROJ_LABEL_ES} &bull;Paso 02","Conoce a los Cinco y Elige",
            "Conoce a los cinco fot&oacute;grafos maestros, elige a uno y empieza tu presentaci&oacute;n con tres de sus im&aacute;genes.",
            "#top","Back to English", HICON_DESIGN)
        es+=card("PASO 02 &middot; ESTUDIA A TU MAESTRO","Elige a Uno y Estudia C&oacute;mo Trabaja",
            (float_right(RESEARCH_FLOAT,"Una estudiante investigando a un fot&oacute;grafo maestro en una computadora del laboratorio","Estudia su estilo en internet antes de elegir. Mira muchas de sus fotos.") if HAVE_RESEARCH else "")
            + para("Abajo est&aacute;n tus <strong>cinco fot&oacute;grafos maestros</strong>. Cada uno trabaja en un estilo distinto. Lee los cinco, mira sus fotos en internet y luego <strong>elige al que m&aacute;s te atraiga</strong>.")
            + para("Est&aacute;s estudiando <strong>c&oacute;mo hacen im&aacute;genes</strong>, no su biograf&iacute;a. Para tu maestro, observa de cerca su <strong>composici&oacute;n, luz, sujetos y edici&oacute;n</strong>. Estas son las ideas que traer&aacute;s a tus propias tres fotos.")
            + note("Elige al fot&oacute;grafo como el que m&aacute;s te gustar&iacute;a fotografiar. Entre m&aacute;s te emocione su trabajo, m&aacute;s fuertes ser&aacute;n tus propias fotos."))
        es+=deliverables_box(True,
            [("Tu presentaci&oacute;n, empezada (PDF):","descarga la plantilla, llena la <strong>diapositiva de portada</strong> y tus <strong>3 diapositivas del fot&oacute;grafo maestro</strong> (una imagen que elegiste en cada una, m&aacute;s tu nota de t&eacute;cnica), exp&oacute;rtala como PDF y s&uacute;bela a esta tarea de Canvas.")])
        es+=master_cards(True)
        es+=resources_card("D&oacute;nde Ver Su Trabajo", reslist(True), True)
        es+=card("RE&Uacute;NE TUS TRES IM&Aacute;GENES / EMPIEZA TU PRESENTACI&Oacute;N","Elige 3 Im&aacute;genes y Empieza Tu Presentaci&oacute;n",
            para("Ahora construye la primera parte de tu presentaci&oacute;n. Abre la <strong>plantilla de diapositivas</strong> de tu carpeta del proyecto y haz esto:")
            + steps([
                ("Llena la diapositiva de portada.","Escribe el nombre de tu fot&oacute;grafo maestro, tu nombre, tu periodo y el curso."),
                ("Busca tres im&aacute;genes fuertes de tu maestro.","Busca en internet tres de sus fotos que mejor muestren su estilo. Gu&aacute;rdalas en tu carpeta del proyecto."),
                ("Pon una imagen en cada diapositiva del maestro.","Coloca una imagen en cada una de las tres diapositivas del fot&oacute;grafo maestro de la plantilla."),
                ("Escribe tu nota de t&eacute;cnica en cada una.","En cada diapositiva, nombra la t&eacute;cnica que ves: composici&oacute;n, iluminaci&oacute;n, el momento, el rango tonal o la edici&oacute;n. Di por qu&eacute; funciona."),
                ("Exporta un PDF y s&uacute;belo.","Ve a Archivo &gt; Exportar a &gt; PDF (o Archivo &gt; Guardar una copia como PDF), luego sube el PDF a esta tarea de Canvas."),
            ])
            + note("Estas tres im&aacute;genes son el trabajo de <strong>tu fot&oacute;grafo maestro</strong>, de internet. T&uacute; capturas tus <strong>propias</strong> fotos despu&eacute;s, en el Paso 03."))
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 03 - Captura y Contacto","Pide un kit de c&aacute;mara y captura una toma completa de tus propias fotos en el estilo de tu maestro.")

        return wrap_page(f"Step 2: Meet the Five | Master Photographer | {CL_EN} | PVHS", nav("Step 02",dots_for(1),step_topnav(1)), top_wrap(en,es), step_bottom(1))

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
        en+=card("OFFLOAD YOUR PHOTOS","Move Your Full Take to RAW_Images",
            para("Get every photo off the camera and into your project folder so nothing gets lost.")
            + steps([
                ("Connect your camera or card.","Use the cable, or put the memory card in a card reader on your Mac."),
                ("Open your project folder in Finder.","Find the <strong>Master_Photographer</strong> folder you downloaded on the Overview."),
                ("Copy every photo into RAW_Images.","Drag your whole take into the <strong>RAW_Images</strong> folder inside that project folder. Keep them all, not just three."),
            ])
            + note("Offload your <strong>full take</strong>, every photo you captured. You select your best three later, in the next step."))
        en+=card("BUILD YOUR CONTACT SHEET","Make a 12-Up Contact Sheet",
            para("A <strong>contact sheet</strong> is one page that shows all your photos as small thumbnails, so you and your teacher can see your whole take at a glance. You make a <strong>12-up</strong> sheet, 12 photos per page.")
            + steps([
                ("Import RAW_Images into Lightroom Classic.","Open Lightroom Classic, click Import, and bring in your RAW_Images folder."),
                ("Select all your photos.","Edit menu &rarr; Select All, so your whole take is on the sheet."),
                ("Open the Print module and pick the 12-Up Contact Sheet preset.","If you do not see it, install it first (see the resource below)."),
                ("Print to a high-resolution JPG.","Set Print To: JPEG File, then click Print to File. The preset already saves a high-resolution JPG for you."),
                ("Name it and upload.","Name it LastName_First_MasterPhotographer_ContactSheet.jpg, then upload the JPG to this Canvas assignment."),
            ])
            + note("Turn in a <strong>high-resolution JPG</strong>, never a PDF. The contact-sheet preset already saves the right format."))
        en+=resources_card("Contact Sheet Preset",
            pnote_mp('Need the 12-Up preset? <a href="'+CS_INSTALL_VIDEO+'" target="_blank" rel="noopener" style="color:#c4b5fd;"><strong>Watch the install video</strong></a>, then add it to Lightroom Classic &rarr; Print module. You set these up back in the Image Series module.'), False)
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
        es+=card("DESCARGA TUS FOTOS","Mueve Tu Toma Completa a RAW_Images",
            para("Saca todas las fotos de la c&aacute;mara y ll&eacute;valas a tu carpeta del proyecto para que no se pierda ninguna.")
            + steps([
                ("Conecta tu c&aacute;mara o tarjeta.","Usa el cable, o pon la tarjeta de memoria en un lector de tarjetas en tu Mac."),
                ("Abre tu carpeta del proyecto en Finder.","Busca la carpeta <strong>Master_Photographer</strong> que descargaste en el Resumen."),
                ("Copia cada foto a RAW_Images.","Arrastra toda tu toma a la carpeta <strong>RAW_Images</strong> dentro de esa carpeta del proyecto. Cons&eacute;rvalas todas, no solo tres."),
            ])
            + note("Descarga tu <strong>toma completa</strong>, cada foto que capturaste. Seleccionas tus mejores tres despu&eacute;s, en el siguiente paso."))
        es+=card("ARMA TU HOJA DE CONTACTOS","Haz una Hoja de Contactos de 12",
            para("Una <strong>hoja de contactos</strong> es una p&aacute;gina que muestra todas tus fotos como miniaturas, para que t&uacute; y tu maestro vean toda tu toma de un vistazo. Haces una hoja de <strong>12</strong>, 12 fotos por p&aacute;gina.")
            + steps([
                ("Importa RAW_Images a Lightroom Classic.","Abre Lightroom Classic, haz clic en Import (Importar) y trae tu carpeta RAW_Images."),
                ("Selecciona todas tus fotos.","Men&uacute; Edit (Editar) &rarr; Select All (Seleccionar todo), para que toda tu toma est&eacute; en la hoja."),
                ("Abre el m&oacute;dulo Print y elige el ajuste 12-Up Contact Sheet.","Si no lo ves, inst&aacute;lalo primero (mira el recurso de abajo)."),
                ("Imprime a un JPG de alta resoluci&oacute;n.","Pon Print To: JPEG File, luego haz clic en Print to File. El ajuste ya guarda un JPG de alta resoluci&oacute;n por ti."),
                ("N&oacute;mbrala y s&uacute;bela.","N&oacute;mbrala LastName_First_MasterPhotographer_ContactSheet.jpg, luego sube el JPG a esta tarea de Canvas."),
            ])
            + note("Entrega un <strong>JPG de alta resoluci&oacute;n</strong>, nunca un PDF. El ajuste de hoja de contactos ya guarda el formato correcto."))
        es+=resources_card("Ajuste de Hoja de Contactos",
            pnote_mp('&iquest;Necesitas el ajuste 12-Up? <a href="'+CS_INSTALL_VIDEO+'" target="_blank" rel="noopener" style="color:#c4b5fd;"><strong>Mira el video de instalaci&oacute;n</strong></a>, luego agr&eacute;galo a Lightroom Classic &rarr; m&oacute;dulo Print. Los configuraste en el m&oacute;dulo Image Series.'), True)
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 04 - Selecciona y Edita","Elige tus tres im&aacute;genes m&aacute;s fuertes y ed&iacute;talas para igualar el estilo que estudiaste.")

        return wrap_page(f"Step 3: Capture and Contact | Master Photographer | {CL_EN} | PVHS", nav("Step 03",dots_for(2),step_topnav(2)), top_wrap(en,es), step_bottom(2))

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
            [("3 edited images (high-resolution JPG):","your three final selections, edited in Lightroom and exported as high-resolution JPGs, uploaded to this Canvas assignment.")], files=3)
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
                ("Upload all three.","Upload your three JPG files to this Canvas assignment."),
            ]))
        en+=next_up("UP NEXT &middot; STEP 05 - Presentation &amp; Reflection","Finish your slideshow, present it to the class, and answer the reflection on the closing slide.")

        es=banner(f"{PROJ_LABEL_ES} &bull;Paso 04","Selecciona y Edita",
            "Elige tus tres im&aacute;genes m&aacute;s fuertes y ed&iacute;talas para igualar el estilo que estudiaste.",
            "#top","Back to English", HICON_DESIGN)
        es+=card("PASO 04 &middot; ELIGE Y EDITA","Selecciona Tus Mejores Tres y Luego Edita",
            (float_right(CULL_FLOAT,"Una estudiante mirando tres fotos seleccionadas sobre una mesa","Selecciona las tres fotos que mejor muestren el estilo de tu maestro.") if HAVE_CULL else "")
            + para("Capturaste una toma completa. Ahora <strong>seleccionas</strong>, que significa elegir tu trabajo m&aacute;s fuerte y dejar ir el resto. Elige las <strong>tres im&aacute;genes</strong> que mejor muestren el estilo de tu fot&oacute;grafo maestro.")
            + para("Luego <strong>edita</strong> tus tres selecciones en Lightroom para igualar el estilo que estudiaste: los tonos, el contraste, el ambiente. Haz que se sientan como que pertenecen junto al trabajo de tu maestro.")
            + note("Elige las tres que sean m&aacute;s fuertes juntas como conjunto, no solo tres fotos bonitas. Todas deben apuntar al mismo estilo."))
        es+=deliverables_box(True,
            [("3 im&aacute;genes editadas (JPG de alta resoluci&oacute;n):","tus tres selecciones finales, editadas en Lightroom y exportadas como JPG de alta resoluci&oacute;n, subidas a esta tarea de Canvas.")], files=3)
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
                ("Sube las tres.","Sube tus tres archivos JPG a esta tarea de Canvas."),
            ]))
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 05 - Presentaci&oacute;n y Reflexi&oacute;n","Termina tu presentaci&oacute;n, pres&eacute;ntala a la clase y responde la reflexi&oacute;n en la diapositiva final.")

        return wrap_page(f"Step 4: Cull and Edit | Master Photographer | {CL_EN} | PVHS", nav("Step 04",dots_for(3),step_topnav(3)), top_wrap(en,es), step_bottom(3))

    # ================= STEP 05: Presentation & Reflection =================
    def step05():
        en=banner(f"{PROJ_LABEL} &bull;Step 05","Presentation &amp; Reflection",
            "Finish your slideshow, present it to the class, and answer the reflection on the closing slide.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
        en+=card("STEP 05 &middot; FINISH AND PRESENT","Put Master and Student Work Side by Side",
            (float_right(PRESENT_FLOAT,"A student presenting their master photographer slides to the class","Present your master&rsquo;s work and your own, side by side.") if HAVE_PRESENT else "")
            + para("Time to finish your slideshow. You already have your Cover and three Master slides from Step 02. Now add your <strong>three edited photos</strong> and your <strong>reflection</strong>, then present the whole thing to the class.")
            + para("Your deck shows your master photographer&rsquo;s work and your work <strong>side by side</strong>, so everyone can see what you studied and how you made it your own."))
        en+=deliverables_box(False,
            [("Your finished deck (.pptx or .key):","the full slideshow (cover, 3 master slides, your 3 edited photos, and the reflection closing slide), presented to the class and uploaded to this Canvas assignment.")])
        en+=deck_showcase(False)
        en+=card("BUILD THE REST OF YOUR DECK","Add Your Photos and Your Notes",
            para("Open the deck you started in Step 02 and finish it.")
            + steps([
                ("Add your three edited photos.","Place one of your final JPGs on each of the three My Work slides."),
                ("Write how you used your master&rsquo;s style.","On each slide, say what you borrowed: composition, light, the moment, tonal range, or editing."),
                ("Fill the reflection slide.","Answer the three reflection questions on the closing slide."),
                ("Check every slide.","Make sure your name is on the cover and all six images are in place."),
            ]))
        en+=card("PRESENT TO THE CLASS","Share Your Work Out Loud",
            para("You will present your slideshow to the class. Keep it short and clear, about <strong>3 to 5 minutes</strong>.")
            + bullets([
                ("Introduce your master:","who they are and the style you studied."),
                ("Walk through your three master images:","name the technique on each one."),
                ("Show your three photos:","explain how each one shows your master&rsquo;s influence."),
                ("End with your reflection:","what you learned and what you will carry forward."),
            ])
            + note("Speak clearly and look up at your classmates. You know your work better than anyone in the room."))
        en+=card("REFLECTION &middot; CLOSING SLIDE","Finish With an Honest Reflection",
            para("Your last slide is your <strong>reflection</strong>. Answer these three questions in a few honest sentences:")
            + bullets([
                ("What you learned:","what is the most important thing you learned from your master photographer?"),
                ("What changed:","how did studying their work change the way you capture or edit your own photos?"),
                ("What is next:","what will you carry into your next photography project?"),
            ]))
        en+=next_up("YOU DID IT &middot; PROJECT COMPLETE","You studied a master, made the style your own, and presented it. That is how real photographers grow.")

        es=banner(f"{PROJ_LABEL_ES} &bull;Paso 05","Presentaci&oacute;n y Reflexi&oacute;n",
            "Termina tu presentaci&oacute;n, pres&eacute;ntala a la clase y responde la reflexi&oacute;n en la diapositiva final.",
            "#top","Back to English", HICON_REFLECT)
        es+=card("PASO 05 &middot; TERMINA Y PRESENTA","Pon el Trabajo del Maestro y el Tuyo Lado a Lado",
            (float_right(PRESENT_FLOAT,"Una estudiante presentando sus diapositivas del fot&oacute;grafo maestro a la clase","Presenta el trabajo de tu maestro y el tuyo, lado a lado.") if HAVE_PRESENT else "")
            + para("Hora de terminar tu presentaci&oacute;n. Ya tienes tu portada y tus tres diapositivas del maestro del Paso 02. Ahora agrega tus <strong>tres fotos editadas</strong> y tu <strong>reflexi&oacute;n</strong>, luego presenta todo a la clase.")
            + para("Tu presentaci&oacute;n muestra el trabajo de tu fot&oacute;grafo maestro y el tuyo <strong>lado a lado</strong>, para que todos vean qu&eacute; estudiaste y c&oacute;mo lo hiciste tuyo."))
        es+=deliverables_box(True,
            [("Tu presentaci&oacute;n terminada (.pptx o .key):","la presentaci&oacute;n completa (portada, 3 diapositivas del maestro, tus 3 fotos editadas y la diapositiva final de reflexi&oacute;n), presentada a la clase y subida a esta tarea de Canvas.")])
        es+=deck_showcase(True)
        es+=card("CONSTRUYE EL RESTO DE TU PRESENTACI&Oacute;N","Agrega Tus Fotos y Tus Notas",
            para("Abre la presentaci&oacute;n que empezaste en el Paso 02 y term&iacute;nala.")
            + steps([
                ("Agrega tus tres fotos editadas.","Coloca uno de tus JPG finales en cada una de las tres diapositivas de Tu Trabajo."),
                ("Escribe c&oacute;mo usaste el estilo de tu maestro.","En cada diapositiva, di qu&eacute; tomaste prestado: composici&oacute;n, luz, el momento, el rango tonal o la edici&oacute;n."),
                ("Llena la diapositiva de reflexi&oacute;n.","Responde las tres preguntas de reflexi&oacute;n en la diapositiva final."),
                ("Revisa cada diapositiva.","Aseg&uacute;rate de que tu nombre est&eacute; en la portada y las seis im&aacute;genes est&eacute;n en su lugar."),
            ]))
        es+=card("PRESENTA A LA CLASE","Comparte Tu Trabajo en Voz Alta",
            para("Presentar&aacute;s tu presentaci&oacute;n a la clase. Que sea corta y clara, como <strong>3 a 5 minutos</strong>.")
            + bullets([
                ("Presenta a tu maestro:","qui&eacute;n es y el estilo que estudiaste."),
                ("Recorre tus tres im&aacute;genes del maestro:","nombra la t&eacute;cnica en cada una."),
                ("Muestra tus tres fotos:","explica c&oacute;mo cada una muestra la influencia de tu maestro."),
                ("Termina con tu reflexi&oacute;n:","qu&eacute; aprendiste y qu&eacute; vas a llevarte contigo."),
            ])
            + note("Habla con claridad y mira a tus compa&ntilde;eros. T&uacute; conoces tu trabajo mejor que nadie en el sal&oacute;n."))
        es+=card("REFLEXI&Oacute;N &middot; DIAPOSITIVA FINAL","Termina con una Reflexi&oacute;n Honesta",
            para("Tu &uacute;ltima diapositiva es tu <strong>reflexi&oacute;n</strong>. Responde estas tres preguntas en unas cuantas oraciones honestas:")
            + bullets([
                ("Qu&eacute; aprendiste:","&iquest;qu&eacute; es lo m&aacute;s importante que aprendiste de tu fot&oacute;grafo maestro?"),
                ("Qu&eacute; cambi&oacute;:","&iquest;c&oacute;mo cambi&oacute; estudiar su trabajo la forma en que capturas o editas tus propias fotos?"),
                ("Qu&eacute; sigue:","&iquest;qu&eacute; vas a llevar a tu pr&oacute;ximo proyecto de fotograf&iacute;a?"),
            ]))
        es+=next_up("LO LOGRASTE &middot; PROYECTO COMPLETO","Estudiaste a un maestro, hiciste tuyo el estilo y lo presentaste. As&iacute; crecen los fot&oacute;grafos de verdad.")

        return wrap_page(f"Step 5: Presentation and Reflection | Master Photographer | {CL_EN} | PVHS", nav("Step 05",dots_for(4),step_topnav(4)), top_wrap(en,es), step_bottom(4))

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
    build("cur")   # in-curriculum module (catalog breadcrumb + site nav via silva-nav.js)
    build("std")   # standalone public share copy at share/master-photographer/ (no catalog, no site nav)
