#!/usr/bin/env python3
# Photography 1A - Module 11  /  Photography 2A - Module 10: The Important Person Project.
# Tell the story of a person who positively impacted your life, in a 3-image series:
#   Image 1 = a PORTRAIT of the person; Images 2 and 3 = two SUPPORTING images of them in action,
#   doing or demonstrating what they do.
# TWO PAGES NOW (more steps appended over the coming weeks):
#   Overview (Step 01, read only: NO downloads, NO reflection document) + Step 02 Choose Your Person
#   (a JOURNAL writing exercise: brainstorm 3 candidate people and 3 reasons for each as to why you
#   are considering them; turned in as a JPG photo of the journal page captured with the school
#   student iPad, the class "scan"). Bilingual EN/ES, 5th-grade. Dark teal angular framework via
#   silva_framework. ALL images gated OFF (HAVE_*=False) so every slot renders NOTHING, no
#   placeholder boxes, until Chris supplies art and flips the flag. Concept + writing module, so NO
#   camera-settings panel and NO own-device fresh-photos note (no capture happens yet). When later
#   capture/edit/reflection steps are added, keep the slug, pages:N in curriculum.html, and the
#   silva-nav.js SILVA_MODULES + pager arrays in sync, then re-run the image catalog.
import os
from silva_framework import *   # shared angular chrome: banner, cards, sections, vocab, deliverables

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"
# White header-crown for the overview (a camera photography project). Step 02 is a writing exercise,
# so it wears the sketch/handwork crown instead.
HICON_CAMERA_KIT=f"{SITE}/assets/Icons/assignment/camera-kit-white-v1.png"

# Local ent: accents -> entities AND en-dash -> plain hyphen (never emit &ndash;, per the hard dash ban).
def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

# Every image slot starts OFF. Flip to True (and drop the file in assets/images/<course>/important-person/)
# when the art is ready, then re-run this builder.
HAVE_HEADER=False    # overview hero (21:9), assets/images/<course>/important-person/header-v1.jpg
HAVE_S2_FLOAT=False  # Step 02 journaling float, assets/images/<course>/important-person/journal-float-v1.jpg

STANDARDS=[
  {"code":"SA.17.2","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Visual Communication","es_title":"Comunicaci&oacute;n Visual",
   "en_desc":"You plan and tell a true story about a real person through a three image series.",
   "es_desc":"Planeas y cuentas una historia verdadera sobre una persona real a trav&eacute;s de una serie de tres im&aacute;genes."},
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You use framing, angle, and background to build a strong portrait of your subject.",
   "es_desc":"Usas el encuadre, el &aacute;ngulo y el fondo para crear un retrato fuerte de tu sujeto."},
  {"code":"SA.17.5","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Image Production &amp; Planning","es_title":"Producci&oacute;n y Planeaci&oacute;n de Imagen",
   "en_desc":"You plan a photo project on purpose, choosing your subject and your three images before you capture them.",
   "es_desc":"Planeas un proyecto fotogr&aacute;fico a prop&oacute;sito, eligiendo tu sujeto y tus tres im&aacute;genes antes de capturarlas."},
]

VOCAB_EN=[
 ("Subject","The person you photograph. In this project, your subject is your important person."),
 ("Portrait","A photo that shows who a person is, usually their face and their expression."),
 ("Environmental Portrait","A portrait taken where the person works or does their thing, so the background helps tell their story."),
 ("Candid","A natural, unposed photo taken while a person is busy doing something, not looking at the camera."),
 ("Photo Story","A small set of photos that work together to tell one story. Yours is three images."),
 ("Composition","How you arrange everything inside the frame: where your person sits, what is behind them, and what you leave out."),
]
VOCAB_ES=[
 ("Subject (Sujeto)","La persona que fotograf&iacute;as. En este proyecto, tu sujeto es tu persona importante."),
 ("Portrait (Retrato)","Una foto que muestra qui&eacute;n es una persona, casi siempre su cara y su expresi&oacute;n."),
 ("Environmental Portrait (Retrato Ambiental)","Un retrato tomado donde la persona trabaja o hace lo suyo, para que el fondo ayude a contar su historia."),
 ("Candid (Espont&aacute;nea)","Una foto natural y sin pose, tomada mientras la persona hace algo, sin mirar a la c&aacute;mara."),
 ("Photo Story (Historia en Fotos)","Un peque&ntilde;o grupo de fotos que juntas cuentan una sola historia. La tuya son tres im&aacute;genes."),
 ("Composition (Composici&oacute;n)","C&oacute;mo acomodas todo dentro del encuadre: d&oacute;nde est&aacute; tu persona, qu&eacute; hay detr&aacute;s y qu&eacute; dejas fuera."),
]

def build(course):
    p2 = (course == "photo2")
    MODNUM = "10" if p2 else "11"
    CL_EN = "Photography 2A" if p2 else "Photography 1A"
    IMGDIR=f"{SITE}/assets/images/{course}/important-person"
    HEADER=f"{IMGDIR}/header-v1.jpg"
    S2_FLOAT=f"{IMGDIR}/journal-float-v1.jpg"
    OVER=f"{course}-important-person-overview.html"
    S2=f"{course}-important-person-step02-choose-your-person.html"

    def nav(current,dots,stepnav):
        return ('      <div class="silva-breadcrumb">\n'
                '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
                '        <span class="bc-sep">&rsaquo;</span>\n'
                f'        <a href="{OVER}" class="bc-hide-sm">Important Person</a>\n'
                '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
                f'        <span class="bc-current">{current}</span>\n'
                '      </div>\n'
                '      <div class="silva-nav-spacer"></div>\n'
                f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
                f'      <div class="silva-step-nav">{stepnav}</div>')
    HREFS=[OVER,S2]; TITLES=[("1","Step 01"),("2","Step 02")]
    def dots_for(ai):
        return "".join(dot("" if i==ai else HREFS[i], lab, title, i==ai, module=False) for i,(lab,title) in enumerate(TITLES))

    # ================= OVERVIEW (Step 01) =================
    def overview():
        en=banner(f"Module {MODNUM} &bull; Step 01","The Important Person Project",
            "Tell the story of someone who changed your life, in three photos. Read this page, then go to Step 02.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_CAMERA_KIT)
        en+=type_card("overview","Step 01 &middot; Overview","Tell Someone&rsquo;s Story in Three Photos",
            para("In this project you tell the story of one important person in your life. Pick someone who helped you in a real, meaningful way. It could be a parent, an aunt, an uncle, a grandparent, a coach, a teacher, a mentor, or a close friend.")
            + para("You will tell their story with a <strong>three image series</strong>. The three photos work together as one story:")
            + bullets([
                ("Image 1 is a portrait:","a clear photo of your person that shows who they are."),
                ("Image 2 is them in action:","a photo of your person doing or showing what they do."),
                ("Image 3 is them in action again:","a second photo of them doing their thing, from a new angle or a new moment."),
            ])
            + (framed(HEADER,"A Pioneer Valley student&rsquo;s three image series about an important person: a portrait beside two photos of that person doing what they do") if HAVE_HEADER else ""))
        en+=standards_box(False, STANDARDS)
        en+=card("WHY THIS PERSON","Start With Someone Who Matters",
            para("The strongest photo stories come from real feelings. Think about someone who made your life better. Maybe they taught you something, believed in you, worked hard for you, or showed you how to do something you love.")
            + para("The more the person means to you, the stronger your photos will be. You will get to know their story and show it through your three images."))
        en+=card("HOW THIS MODULE WORKS","From an Idea to a Photo Story",
            para("You are on Step 01 now: read this page so you understand the project. Here is what comes next.")
            + bullets([
                ("Step 02 &middot; Choose Your Person:","in your journal, brainstorm three people you could photograph and three reasons for each, then pick the one with the strongest story."),
                ("Coming next:","over the next weeks you will plan your three images, photograph your person, and edit your series. New steps will appear here in this module."),
            ]))
        en+=resources_card("Key Words",
            vocab_grid("On the Quiz",
              "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
              VOCAB_EN), False)
        en+=next_up("UP NEXT &middot; STEP 02 - Choose Your Person","Open your journal and brainstorm three people you could tell a story about.")

        es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 01","El Proyecto de la Persona Importante",
            "Cuenta la historia de alguien que cambi&oacute; tu vida, en tres fotos. Lee esta p&aacute;gina y luego ve al Paso 02.",
            "#top","Back to English", HICON_CAMERA_KIT)
        es+=type_card("overview","Paso 01 &middot; Resumen","Cuenta la Historia de Alguien en Tres Fotos",
            para("En este proyecto cuentas la historia de una persona importante en tu vida. Elige a alguien que te ayud&oacute; de una manera real y significativa. Puede ser un pap&aacute;, una mam&aacute;, una t&iacute;a, un t&iacute;o, un abuelo, un entrenador, un maestro, un mentor o un buen amigo.")
            + para("Contar&aacute;s su historia con una <strong>serie de tres im&aacute;genes</strong>. Las tres fotos trabajan juntas como una sola historia:")
            + bullets([
                ("La imagen 1 es un retrato:","una foto clara de tu persona que muestra qui&eacute;n es."),
                ("La imagen 2 es en acci&oacute;n:","una foto de tu persona haciendo o mostrando lo que hace."),
                ("La imagen 3 es en acci&oacute;n otra vez:","una segunda foto de ella haciendo lo suyo, desde un nuevo &aacute;ngulo o un nuevo momento."),
            ])
            + (framed(HEADER,"La serie de tres im&aacute;genes de una estudiante de Pioneer Valley sobre una persona importante: un retrato junto a dos fotos de esa persona haciendo lo que hace") if HAVE_HEADER else ""))
        es+=standards_box(True, STANDARDS)
        es+=card("POR QU&Eacute; ESTA PERSONA","Empieza con Alguien que Importa",
            para("Las historias en fotos m&aacute;s fuertes nacen de sentimientos reales. Piensa en alguien que hizo tu vida mejor. Tal vez te ense&ntilde;&oacute; algo, crey&oacute; en ti, trabaj&oacute; duro por ti o te mostr&oacute; c&oacute;mo hacer algo que amas.")
            + para("Entre m&aacute;s signifique la persona para ti, m&aacute;s fuertes ser&aacute;n tus fotos. Conocer&aacute;s su historia y la mostrar&aacute;s con tus tres im&aacute;genes."))
        es+=card("C&Oacute;MO FUNCIONA ESTE M&Oacute;DULO","De una Idea a una Historia en Fotos",
            para("Est&aacute;s en el Paso 01 ahora: lee esta p&aacute;gina para entender el proyecto. Esto es lo que sigue.")
            + bullets([
                ("Paso 02 &middot; Elige a Tu Persona:","en tu diario, haz una lluvia de ideas de tres personas que podr&iacute;as fotografiar y tres razones para cada una, luego elige la de la historia m&aacute;s fuerte."),
                ("Lo que sigue:","en las pr&oacute;ximas semanas planear&aacute;s tus tres im&aacute;genes, fotografiar&aacute;s a tu persona y editar&aacute;s tu serie. Los nuevos pasos aparecer&aacute;n aqu&iacute; en este m&oacute;dulo."),
            ]))
        es+=resources_card("Palabras Clave",
            vocab_grid("En el Examen",
              "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
              VOCAB_ES), True)
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 02 - Elige a Tu Persona","Abre tu diario y haz una lluvia de ideas de tres personas sobre las que podr&iacute;as contar una historia.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S2}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
        return wrap_page(f"The Important Person Project | {CL_EN} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 02: Choose Your Person (journal writing exercise) =================
    def step02():
        en=banner(f"Module {MODNUM} &bull; Step 02","Choose Your Important Person",
            "A journal writing exercise. Brainstorm three people, then pick the one with the strongest story.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_SKETCH)
        en+=card("STEP 02 &middot; JOURNAL / BRAINSTORM","Write About Three People You Could Choose",
            (float_right(S2_FLOAT,"A Pioneer Valley student writing a brainstorm list of three important people in a journal","Think on paper first. Your best story starts here.") if HAVE_S2_FLOAT else "")
            + para("Before you pick up a camera, think on paper. In your journal, brainstorm <strong>three different people</strong> you could tell a story about. Writing it out helps you choose the person with the strongest story.")
            + para("For each of your three people, write <strong>three short reasons</strong> why you are thinking about them. That is three people, and three reasons for each.")
            + bullets([
                ("Person 1:","write their name and how you know them, then three reasons they matter to you."),
                ("Person 2:","write their name and how you know them, then three reasons they matter to you."),
                ("Person 3:","write their name and how you know them, then three reasons they matter to you."),
            ])
            + para("Stuck on your three reasons? Answer questions like these in your own words: What did this person do for you? What do they do that you admire? How did they change your life? What would you want other people to see about them?")
            + note("Write in full sentences, in your own words. There are no wrong answers here. This is your thinking on paper."))
        en+=deliverables_box(False,
            [("1 journal photo (JPG):","a clear photo of your journal page showing your three people and three reasons for each, uploaded to this Canvas assignment.")])
        en+=card("HOW TO TURN IT IN","Scan Your Journal Page With Your iPad",
            para("Your brainstorm is on paper, so you will take a photo of it to turn it in. Use your <strong>school student iPad</strong> as a camera. This is how we scan paper work in this class.")
            + bullets([
                ("Lay your journal flat:","open to your brainstorm page in good light, with no shadow across it."),
                ("Take a photo with your student iPad:","fill the frame with your page and keep it straight, so your writing is easy to read."),
                ("Upload the JPG:","upload your photo to this Canvas assignment."),
            ]))
        en+=next_up("UP NEXT &middot; PLAN &amp; CAPTURE YOUR SERIES","Soon you will plan your three images and photograph your important person. New steps are coming to this module.")

        es=banner(f"M&oacute;dulo {MODNUM} &bull; Paso 02","Elige a Tu Persona Importante",
            "Un ejercicio de escritura en el diario. Haz una lluvia de ideas de tres personas y elige la de la historia m&aacute;s fuerte.",
            "#top","Back to English", HICON_SKETCH)
        es+=card("PASO 02 &middot; DIARIO / LLUVIA DE IDEAS","Escribe Sobre Tres Personas que Podr&iacute;as Elegir",
            (float_right(S2_FLOAT,"Una estudiante de Pioneer Valley escribiendo una lista de tres personas importantes en un diario","Piensa en papel primero. Tu mejor historia empieza aqu&iacute;.") if HAVE_S2_FLOAT else "")
            + para("Antes de tomar una c&aacute;mara, piensa en papel. En tu diario, haz una lluvia de ideas de <strong>tres personas distintas</strong> sobre las que podr&iacute;as contar una historia. Escribirlo te ayuda a elegir a la persona de la historia m&aacute;s fuerte.")
            + para("Para cada una de tus tres personas, escribe <strong>tres razones cortas</strong> de por qu&eacute; est&aacute;s pensando en ellas. Son tres personas, y tres razones para cada una.")
            + bullets([
                ("Persona 1:","escribe su nombre y c&oacute;mo la conoces, luego tres razones por las que es importante para ti."),
                ("Persona 2:","escribe su nombre y c&oacute;mo la conoces, luego tres razones por las que es importante para ti."),
                ("Persona 3:","escribe su nombre y c&oacute;mo la conoces, luego tres razones por las que es importante para ti."),
            ])
            + para("&iquest;No se te ocurren las tres razones? Contesta preguntas como estas con tus propias palabras: &iquest;Qu&eacute; hizo esta persona por ti? &iquest;Qu&eacute; hace que admiras? &iquest;C&oacute;mo cambi&oacute; tu vida? &iquest;Qu&eacute; te gustar&iacute;a que otras personas vieran de ella?")
            + note("Escribe en oraciones completas, con tus propias palabras. Aqu&iacute; no hay respuestas incorrectas. Este es tu pensamiento en papel."))
        es+=deliverables_box(True,
            [("1 foto del diario (JPG):","una foto clara de tu p&aacute;gina del diario que muestre tus tres personas y tres razones para cada una, subida a esta tarea de Canvas.")])
        es+=card("C&Oacute;MO ENTREGARLO","Escanea Tu P&aacute;gina del Diario con Tu iPad",
            para("Tu lluvia de ideas est&aacute; en papel, as&iacute; que tomar&aacute;s una foto de ella para entregarla. Usa tu <strong>iPad escolar de estudiante</strong> como c&aacute;mara. As&iacute; escaneamos el trabajo en papel en esta clase.")
            + bullets([
                ("Pon tu diario plano:","&aacute;brelo en tu p&aacute;gina de ideas con buena luz, sin que una sombra la cruce."),
                ("Toma una foto con tu iPad de estudiante:","llena el encuadre con tu p&aacute;gina y mantenla derecha, para que tu letra se lea f&aacute;cil."),
                ("Sube el JPG:","sube tu foto a esta tarea de Canvas."),
            ]))
        es+=next_up("A CONTINUACI&Oacute;N &middot; PLANEA Y CAPTURA TU SERIE","Pronto planear&aacute;s tus tres im&aacute;genes y fotografiar&aacute;s a tu persona importante. Vienen nuevos pasos a este m&oacute;dulo.")

        stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
        return wrap_page(f"Step 2: Choose Your Person | The Important Person Project | {CL_EN} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

    for fname,gen in [(OVER,overview),(S2,step02)]:
        html=ent(gen())
        ban_check(html, fname)
        open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
        print("wrote", fname, len(html), "bytes")

for course in ("photo1","photo2"):
    print(f"--- {course} ---")
    build(course)
