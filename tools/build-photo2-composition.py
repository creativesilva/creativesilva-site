#!/usr/bin/env python3
# Photography 2A - Module: Composition Photo Walk.
# In-class photo walk with shared class cameras: capture the 6 composition rules in Manual Mode
# and RAW, build a 12-Up contact sheet of the whole take, then cull / edit / rename / export the
# best 6 (with a 6-Up contact sheet), then reflect. Scavenger-hunt competition (Chick-fil-A prize).
# Re-chromed from the old hand-authored eyebrow + IDEYE framework to the shared chip-header
# framework. Photo-walk module (school camera kit): the WHITE photo-walk icon crowns every banner
# and there is NO fresh-photos note (not an own-device module). Overview + 3 steps, bilingual
# EN/ES, 5th-grade. ALL student copy preserved verbatim; only the chrome changed.
import os
from silva_framework import *
import silva_framework as _sf

def banner(label,title,subtitle,es_href,es_label):
    # Composition is an in-class photo walk: crown the banner with the white photo-walk icon.
    return _sf.banner(label,title,subtitle,es_href,es_label,HICON_PHOTO_WALK)

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/photo2/composition"
HERO=f"{IMG}/photowalk-hero.png"
CHICKFILA=f"{IMG}/chick-fil-a-prize.jpg"
S1_FLOAT=f"{IMG}/photowalk-step-float.png"
S2_FLOAT=f"{IMG}/photowalk-step2-float-v2.png"
REFLECT_EN=f"{SITE}/assets/course-documents/Composition-Photo-Walk-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Composition-Photo-Walk-Reflection-ES.docx"
AREA="Photography Folder"

OVER="photo2-composition-overview.html"
S1="photo2-composition-step01-photowalk.html"
S2="photo2-composition-step02-cull-export.html"
S3="photo2-composition-step03-reflection.html"

# ---- module-local helpers (cohesive teal, no framework equivalent) ----
def pills(labels):
    # teal capability pills under the overview hero (same markup the pictograms module uses).
    r="".join('<span style="display:inline-block;background:rgba(0,116,116,0.22);border:1px solid rgba(0,184,184,0.35);'
      'color:#80e0e0;font-size:10.5pt;letter-spacing:0.06em;text-transform:uppercase;padding:6px 12px;margin:0 8px 8px 0;">'
      f'<strong>{t}</strong></span>' for t in labels)
    return f'<div style="margin:6px 0 4px;">{r}</div>'

def teamwork_box(label,body):
    # labeled teal callout (reproduced verbatim from the source; already cohesive teal content).
    return ('<div style="background:rgba(0,116,116,0.16);border:1px solid rgba(0,184,184,0.30);border-left:4px solid #00b8b8;padding:14px 16px;margin:2px 0 18px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:5px;"><strong>{label}</strong></div>'
      f'<div style="font-size:13pt;color:rgba(255,255,255,0.92);line-height:1.5;">{body}</div></div>')

def sublabel(t):
    # teal uppercase mini-heading used inside the step-02 content card (Cull / Edit groups).
    return f'<div style="font-size:11pt;letter-spacing:0.10em;text-transform:uppercase;color:#80e0e0;margin:12px 0 8px;"><strong>{t}</strong></div>'

def rules_scroll(es,rules):
    # horizontal scroll of the 6 rule cards (image + title + description + Key Tip). Cohesive teal.
    hint="Desliza para ver las 6 reglas &rarr;" if es else "Scroll for all 6 rules &rarr;"
    ktl="Consejo Clave" if es else "Key Tip"
    cells=""
    for img,title,desc,tip in rules:
        cells+=('<div style="scroll-snap-align:start;">'
          '<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;height:100%;box-sizing:border-box;">'
          '<div style="background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:18px;height:100%;box-sizing:border-box;">'
          f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;margin-bottom:12px;line-height:0;"><img src="{IMG}/{img}" alt="{title}" style="width:100%;height:auto;display:block;" /></div>'
          f'<div style="font-size:13pt;color:#ffffff;margin-bottom:6px;"><strong>{title}</strong></div>'
          f'<div style="font-size:11.5pt;line-height:1.55;color:rgba(255,255,255,0.86);margin-bottom:10px;">{desc}</div>'
          f'<div style="font-size:10pt;letter-spacing:0.12em;text-transform:uppercase;color:#80e0e0;margin-bottom:3px;"><strong>{ktl}</strong></div>'
          f'<div style="font-size:10.5pt;line-height:1.5;color:rgba(255,255,255,0.72);">{tip}</div>'
          '</div></div></div>')
    return (f'<div style="font-size:9.5pt;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.45);margin-bottom:8px;">{hint}</div>'
      '<div style="display:grid;grid-auto-flow:column;grid-auto-columns:minmax(230px,1fr);overflow-x:auto;overflow-y:hidden;gap:14px;padding-bottom:18px;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;">'
      + cells + '</div>')

def downloads_block(es):
    # Orange Downloads section (Overview only). Composition holds the reflection doc.
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    lead=("Descarga aqu&iacute; todo lo que necesitas para este m&oacute;dulo. Consigue tus archivos antes de empezar." if es
          else "Download everything you need for this module here. Get your files before you start.")
    reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
    ref=REFLECT_ES if es else REFLECT_EN
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ref,reflabel,row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Composition Photo Walk</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

EN_RULES=[
  ("01-rule-of-thirds.jpg","Rule of Thirds","Place your subject on a grid line or power point, not the center.","Turn on your camera grid. The four points where the lines cross are your power points."),
  ("02-leading-lines.jpg","Leading Lines","Use hallways, fences, or edges to pull the eye toward your subject.","Find lines that point toward your subject, not away. Diagonal lines feel more energetic."),
  ("03-framing.jpg","Framing","Surround your subject with a doorway, arch, or foreground element.","Your frame does not need to be sharp. A dark frame around a bright subject adds contrast."),
  ("04-negative-space.jpg","Negative Space","Leave empty space around your subject. Let the scene breathe.","Sky, open ground, and blank walls make great negative space. Do not fill every corner."),
  ("08-point-of-view.jpg","Point of View","Get low, climb high, or capture from a first person angle. Change your angle a lot from normal eye level.","Try two or three angles before you pick one. Low angles make a subject look strong."),
  ("07-depth-layers.jpg","Depth and Layers","Put a foreground, a midground, and a background in one frame.","Get low or move close to build a strong foreground. Overlapping layers add depth."),
]
ES_RULES=[
  ("01-rule-of-thirds.jpg","Regla de los Tercios","Coloca tu sujeto en una l&iacute;nea de la cuadr&iacute;cula o en un punto de poder, no en el centro.","Activa la cuadr&iacute;cula de tu c&aacute;mara. Los cuatro puntos donde se cruzan las l&iacute;neas son tus puntos de poder."),
  ("02-leading-lines.jpg","L&iacute;neas Gu&iacute;a","Usa pasillos, cercas o bordes para llevar la mirada hacia tu sujeto.","Busca l&iacute;neas que apunten hacia tu sujeto, no en contra. Las l&iacute;neas diagonales se sienten m&aacute;s din&aacute;micas."),
  ("03-framing.jpg","Encuadre","Rodea tu sujeto con una puerta, un arco o un elemento en primer plano.","El marco no necesita estar enfocado. Un marco oscuro alrededor de un sujeto brillante agrega contraste."),
  ("04-negative-space.jpg","Espacio Negativo","Deja espacio vac&iacute;o alrededor de tu sujeto. Deja que la escena respire.","El cielo, el suelo abierto y las paredes lisas son buen espacio negativo. No llenes cada esquina."),
  ("08-point-of-view.jpg","Punto de Vista","Ponte bajo, s&uacute;bete alto o fotograf&iacute;a en primera persona. Cambia mucho tu &aacute;ngulo desde el nivel normal de los ojos.","Prueba dos o tres &aacute;ngulos antes de elegir. Los &aacute;ngulos bajos hacen que el sujeto se vea fuerte."),
  ("07-depth-layers.jpg","Profundidad y Capas","Pon un primer plano, un plano medio y un fondo en una sola toma.","Ponte bajo o ac&eacute;rcate para crear un primer plano fuerte. Las capas que se superponen agregan profundidad."),
]

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 2A &bull; Composition Photo Walk","Composition Photo Walk","Six rules. One photo walk. One photo at Chick-fil-A.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","The Photo Walk",
        para("You will take a photo walk on campus and capture the 6 composition rules. All images are captured in Manual Mode and in RAW, indoor or outdoor. Capture one strong image for each concept.")
        + framed(HERO,"Composition Photo Walk")
        + pills(["Manual Mode","RAW Format","On Campus","One image per rule"]))
    en+=downloads_block(False)
    en+=card("","The Challenge",
        float_right(CHICKFILA,"Chick-fil-A prize","")
        + para("This photo walk is a scavenger-hunt competition. You and your partner each capture, cull, edit, name, and turn in your own 6 images. Mr. Silva selects the single strongest set: the most well-executed and most creative. When one partner&rsquo;s set wins, both partners win, each of you gets a Chick-fil-A gift card. You both turn in your own work, so think of it as holding two tickets."))
    en+=card("","The 6 Rules You Will Capture",
        rules_scroll(False, EN_RULES))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Composition","How you arrange everything inside the frame: where the subject sits, the angle, and what you leave out."),
           ("Photo Walk","Walking with your camera to capture images on purpose, capturing one strong photo for each concept."),
           ("Contact Sheet","One page that shows small thumbnail versions of many photos together, so you can compare them fast."),
           ("Cull","Looking through all your photos and keeping only the strongest, then dropping the weak or blurry ones."),
           ("Export","Saving your finished edit as a new JPG, separate from the RAW, so it is ready to turn in."),
           ("Naming Convention","A clear, steady way to name your files so they stay organized. Here, you name each by its concept.")]), False)

    es=banner("Fotograf&iacute;a 2A &bull; Caminata de Composici&oacute;n","Caminata de Composici&oacute;n","Seis reglas. Una caminata. Una oportunidad de ganar Chick-fil-A.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","La Caminata Fotogr&aacute;fica",
        para("Vas a hacer una caminata fotogr&aacute;fica en el campus y capturar las 6 reglas de composici&oacute;n. Todas las im&aacute;genes se toman en Modo Manual y en formato RAW, dentro o fuera del sal&oacute;n. Captura una imagen fuerte para cada concepto.")
        + framed(HERO,"Caminata de Composici&oacute;n")
        + pills(["Modo Manual","Formato RAW","En el Campus","Una imagen por regla"]))
    es+=downloads_block(True)
    es+=card("","El Reto",
        float_right(CHICKFILA,"Chick-fil-A prize","")
        + para("Esta caminata es una competencia estilo b&uacute;squeda del tesoro. T&uacute; y tu compa&ntilde;ero, cada uno, captura, selecciona, edita, nombra y entrega sus propias 6 im&aacute;genes. El Sr. Silva elige el mejor conjunto: el m&aacute;s logrado y m&aacute;s creativo. Cuando el conjunto de un compa&ntilde;ero gana, ganan los dos: cada uno recibe una tarjeta de regalo de Chick-fil-A. Los dos entregan su propio trabajo, as&iacute; que es como tener dos boletos."))
    es+=card("","Las 6 Reglas que Vas a Capturar",
        rules_scroll(True, ES_RULES))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Aviso: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas desde ahora, no la noche anterior.",
          [("Composici&oacute;n","C&oacute;mo acomodas todo dentro del cuadro: d&oacute;nde va el sujeto, el &aacute;ngulo y qu&eacute; dejas fuera."),
           ("Caminata Fotogr&aacute;fica","Caminar con tu c&aacute;mara para capturar im&aacute;genes a prop&oacute;sito, una foto fuerte por cada concepto."),
           ("Hoja de Contactos","Una p&aacute;gina que muestra versiones peque&ntilde;as de muchas fotos juntas, para compararlas r&aacute;pido."),
           ("Seleccionar","Revisar todas tus tomas y quedarte solo con las m&aacute;s fuertes, quitando las d&eacute;biles o borrosas."),
           ("Exportar","Guardar tu edici&oacute;n final como un JPG nuevo, aparte del RAW, listo para entregar."),
           ("Convenci&oacute;n de Nombres","Una forma clara y constante de nombrar tus archivos. Aqu&iacute;, nombras cada uno por su concepto.")]), True)

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Composition Photo Walk | CTE Photography 2A | PVHS", nav("Composition Photo Walk",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Photography 2A &bull; Composition Photo Walk &bull; Step 01","Photo Walk &amp; Contact Sheet","Capture the six. Prove your whole take.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("Contact sheet(s), high-resolution JPG:","your 12-Up contact sheet(s) showing your entire take: all the images you and your partner captured.")])
    en+=card("","The Photo Walk &amp; Contact Sheet",
        float_right(S1_FLOAT,"On the photo walk","")
        + para("Work with a partner and take turns as photographer and assistant. All images are captured in Manual Mode and in RAW, on campus, indoor or outdoor.")
        + para("Capture one strong image for each of the 6 concepts. If you and your partner share one camera, keep all of your photos together on the same card.")
        + para("When the walk is done, import all of your RAW files into Lightroom and back them up.")
        + para("Then build a 12-Up contact sheet that shows your ENTIRE take: every image you and your partner captured together. Export it as a high-resolution JPG. If you have more than 12 images, turn in more than one sheet so every photo is shown.")
        + note("The contact sheet preset is on this module&rsquo;s Overview page (marked M at the top)."))

    es=banner("Fotograf&iacute;a 2A &bull; Caminata de Composici&oacute;n &bull; Paso 01","Caminata y Hoja de Contactos","Captura las seis. Prueba toda tu toma.","#top","Back to English")
    es+=deliverables_box(True,
        [("Hoja(s) de contactos, JPG de alta resoluci&oacute;n:","tu hoja o hojas de contactos 12-Up que muestren toda tu toma: todas las im&aacute;genes que t&uacute; y tu compa&ntilde;ero capturaron.")])
    es+=card("","La Caminata y la Hoja de Contactos",
        float_right(S1_FLOAT,"On the photo walk","")
        + para("Trabaja con un compa&ntilde;ero y t&uacute;rnense como fot&oacute;grafo y asistente. Todas las im&aacute;genes se toman en Modo Manual y en RAW, en el campus, dentro o fuera.")
        + para("Captura una imagen fuerte para cada uno de los 6 conceptos. Si t&uacute; y tu compa&ntilde;ero comparten una c&aacute;mara, mant&eacute;n todas sus tomas juntas en la misma tarjeta.")
        + para("Al terminar la caminata, importa todos tus archivos RAW a Lightroom y haz una copia de seguridad.")
        + para("Luego arma una hoja de contactos 12-Up que muestre TODA tu toma: cada imagen que t&uacute; y tu compa&ntilde;ero capturaron juntos. Exp&oacute;rtala como JPG de alta resoluci&oacute;n. Si tienes m&aacute;s de 12 im&aacute;genes, entrega m&aacute;s de una hoja para que se vean todas.")
        + note("El ajuste de la hoja de contactos est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba)."))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Photo Walk and Contact Sheet | CTE Photography 2A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Photography 2A &bull; Composition Photo Walk &bull; Step 02","Cull, Edit &amp; Export","Your six best. Your ticket to win.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("7 files:","one 6-Up contact sheet of your final 6, plus the 6 individual JPGs, each named by its rule.")])
    en+=card("","Cull, Edit, Rename &amp; Export Your Best 6",
        float_right(S2_FLOAT,"Renee editing her photos in Lightroom","")
        + para("From your whole take, build your final six: one image for each of the 6 composition rules. This part is about judgment and craft, choosing your strongest frame for each rule and editing it so it truly stands out.")
        + teamwork_box("Teamwork","This is a collaborative project. If you and your partner both photo the same concept, you may share images and choose from the whole take. But each of you turns in your OWN best six and your OWN edits: one image per rule, all six rules, your own versions.")
        + sublabel("Cull: Select Your Strongest")
        + bullets([
            ("","For each rule, compare all your options side by side and keep only one."),
            ("","Choose the frame that shows the rule the clearest, a viewer should read the concept instantly."),
            ("","Check sharpness first: is the important part in focus?"),
            ("","Then judge the moment, the light, and the composition. Select the one with the most impact."),
          ])
        + sublabel("Edit: Make It Yours")
        + bullets([
            ("","Set exposure and white balance so the image looks the way you saw it."),
            ("","Crop to strengthen the composition and remove anything at the edges that distracts."),
            ("","Shape the light with contrast, highlights, and shadows to guide the eye."),
            ("","Adjust color and add a little sharpening. Small, intentional moves beat heavy filters."),
            ("","Aim to make each image unique and present it at its very best."),
          ])
        + para("Rename each file with the name of the composition rule it shows (for example: rule-of-thirds.jpg). Export all six as JPGs. Then build a 6-Up contact sheet of your final six with the 6-Up preset.")
        + note("The contact sheet preset is on this module&rsquo;s Overview page (marked M at the top)."))

    es=banner("Fotograf&iacute;a 2A &bull; Caminata de Composici&oacute;n &bull; Paso 02","Selecciona, Edita y Exporta","Tus seis mejores. Tu boleto para ganar.","#top","Back to English")
    es+=deliverables_box(True,
        [("7 archivos:","una hoja de contactos 6-Up de tus 6 finales, m&aacute;s los 6 JPG individuales, cada uno con el nombre de su regla.")])
    es+=card("","Selecciona, Edita, Renombra y Exporta tus 6 Mejores",
        float_right(S2_FLOAT,"Renee editando sus fotos en Lightroom","")
        + para("De toda tu toma, arma tus seis finales: una imagen para cada una de las 6 reglas de composici&oacute;n. Esta parte se trata de criterio y oficio: elegir tu mejor toma para cada regla y editarla para que realmente destaque.")
        + teamwork_box("Trabajo en Equipo","Este es un proyecto colaborativo. Si t&uacute; y tu compa&ntilde;ero fotografiaron el mismo concepto, pueden compartir im&aacute;genes y elegir de toda la toma. Pero cada uno entrega sus PROPIAS seis mejores y sus PROPIAS ediciones: una imagen por regla, las seis reglas, tus propias versiones.")
        + sublabel("Selecciona: Elige la M&aacute;s Fuerte")
        + bullets([
            ("","Para cada regla, compara todas tus opciones lado a lado y qu&eacute;date solo con una."),
            ("","Elige la toma que muestre la regla con m&aacute;s claridad: el que ve debe leer el concepto al instante."),
            ("","Revisa el enfoque primero: &iquest;est&aacute; n&iacute;tida la parte importante?"),
            ("","Luego juzga el momento, la luz y la composici&oacute;n. Elige la de mayor impacto."),
          ])
        + sublabel("Edita: Hazla Tuya")
        + bullets([
            ("","Ajusta exposici&oacute;n y balance de blancos para que la imagen se vea como t&uacute; la viste."),
            ("","Recorta para fortalecer la composici&oacute;n y quitar lo que distrae en los bordes."),
            ("","Da forma a la luz con contraste, altas luces y sombras para guiar la mirada."),
            ("","Ajusta el color y agrega un poco de nitidez. Los cambios peque&ntilde;os e intencionales ganan a los filtros pesados."),
            ("","Busca que cada imagen sea &uacute;nica y pres&eacute;ntala en su mejor versi&oacute;n."),
          ])
        + para("Renombra cada archivo con el nombre de la regla que muestra (por ejemplo: regla-de-los-tercios.jpg). Exporta las seis como JPG. Luego arma una hoja de contactos 6-Up de tus seis finales con el ajuste 6-Up.")
        + note("El ajuste de la hoja de contactos est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba)."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a><a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Cull, Edit and Export | CTE Photography 2A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 03 ----------------
def step03():
    en=banner("Photography 2A &bull; Composition Photo Walk &bull; Step 03","Reflection","Look back. What worked, what was hard.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to Canvas.")])
    en+=card("","Reflection",
        para("Take a few minutes to reflect on your process: what worked, what was hard, and which concept you are most proud of.")
        + para("Download the reflection document, complete it, and turn it in.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder."))

    es=banner("Fotograf&iacute;a 2A &bull; Caminata de Composici&oacute;n &bull; Paso 03","Reflexi&oacute;n","Mira atr&aacute;s. Qu&eacute; funcion&oacute;, qu&eacute; fue dif&iacute;cil.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word de la reflexi&oacute;n (.docx), subido a Canvas.")])
    es+=card("","Reflexi&oacute;n",
        para("T&oacute;mate unos minutos para reflexionar sobre tu proceso: qu&eacute; funcion&oacute;, qu&eacute; fue dif&iacute;cil y de cu&aacute;l concepto est&aacute;s m&aacute;s orgulloso.")
        + para("Descarga el documento de reflexi&oacute;n, compl&eacute;talo y entr&eacute;galo.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)+dot("",'3',"Step 03",True)
    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page("Reflection | CTE Photography 2A | PVHS", nav("Step 03",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
