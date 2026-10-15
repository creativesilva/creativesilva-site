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
HAVE_HEADER=False    # GATED OFF (Chris 2026-10-15): retracted the Mr. Silva + Mr. Garcia photo. It is a retrospective of his OWN high-school important person, which contradicts the project's "current, actively-impacting person" rule, so it modeled the wrong thing. Awaiting a fitting present-day image. assets/images/<course>/important-person/header-v1.jpg
HAVE_S2_FLOAT=False  # GATED OFF (Chris 2026-10-15): retracted the younger-Mr-Garcia headshot (a past image, same reason). assets/images/<course>/important-person/journal-float-v1.jpg
HAVE_S3_FLOAT=False  # Step 03 storyboard float (none supplied yet), assets/images/<course>/important-person/storyboard-float-v1.jpg

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
    PROJNUM = "01"  # Important Person is each course's FIRST project (a project, not a module)
    CL_EN = "Photography 2A" if p2 else "Photography 1A"
    IMGDIR=f"{SITE}/assets/images/{course}/important-person"
    HEADER=f"{IMGDIR}/header-v1.jpg"
    S2_FLOAT=f"{IMGDIR}/journal-float-v1.jpg"
    S3_FLOAT=f"{IMGDIR}/storyboard-float-v1.jpg"
    OVER=f"{course}-important-person-overview.html"
    S2=f"{course}-important-person-step02-choose-your-person.html"
    S3=f"{course}-important-person-step03-storyboard.html"

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
    HREFS=[OVER,S2,S3]; TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03")]
    def dots_for(ai):
        return "".join(dot("" if i==ai else HREFS[i], lab, title, i==ai, module=False) for i,(lab,title) in enumerate(TITLES))

    # ================= OVERVIEW (Step 01) =================
    def overview():
        en=banner(f"Project {PROJNUM} &bull; Step 01","The Important Person Project",
            "Tell the story of someone who changed your life, in three photos. Read this page, then go to Step 02.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_CAMERA_KIT)
        en+=type_card("overview","Step 01 &middot; Overview","Tell Someone&rsquo;s Story in Three Photos",
            para("In this project you tell the story of one important person in your life. Pick someone who is part of your life <strong>right now</strong> and still makes it better today. It could be a parent, an aunt, an uncle, a grandparent, a coach, a teacher, a mentor, or a close friend.")
            + para("You will tell their story with a <strong>three image series</strong>, and all three photos are captured in <strong>horizontal (landscape) orientation</strong>. The three images work together as one story:")
            + bullets([
                ("Image 1 &middot; Environmental portrait:","your person in their own space, surrounded by the things that show who they are. Waist up, and they can look at the camera or be caught in a real moment."),
                ("Image 2 &middot; Close action:","a medium to close photo of your person in action, doing their thing, framed tight so we feel the intensity."),
                ("Image 3 &middot; Wide action:","a wider photo, framed from the knees up to full body, that shows the whole scene and the bigger moment."),
            ])
            + note("All three photos are horizontal. Together they move from who your person is, to them in action up close, to the full scene.")
            + (framed(HEADER,"A student with the important person they chose for their series") if HAVE_HEADER else ""))
        en+=standards_box(False, STANDARDS)
        en+=card("WHY THIS PERSON","Start With Someone Who Matters",
            para("The strongest photo stories come from real feelings. Think about someone who makes your life better. Maybe they teach you something, believe in you, work hard for you, or show you how to do something you love.")
            + note("<strong>Choose someone who is in your life right now.</strong> They must still be actively helping, teaching, or inspiring you today, in the present. You can write about what they have done for you in the past, but they need to be a positive part of your life now. This is not a look back at someone from your past.")
            + para("The more the person means to you, the stronger your photos will be. You will get to know their story and show it through your three images."))
        en+=card("AN EXAMPLE SERIES","A Coach, Told in Three Photos",
            para("Here is what a finished series could look like. Picture an important person who is a football coach.")
            + bullets([
                ("Image 1 &middot; Environmental portrait:","the coach in the locker room after hours, fastening a facemask onto a helmet. He is surrounded by gear, still in his team polo with a whistle around his neck, lit by moody low light. Waist up and horizontal. We learn who he is before he says a word."),
                ("Image 2 &middot; Close action:","the coach grabbing a player by the facemask, firing him up, telling him he can do it. Framed close and full of intensity. We see what he does."),
                ("Image 3 &middot; Wide action:","the whole team celebrating the win, the coach lifting his arm in the middle of it. A wide photo, knees to full body. We feel the big moment."),
            ])
            + note("Your person does not have to be a coach. A cook in their kitchen, a mechanic in the shop, an abuela at the stove, a musician on a stage, anyone with a space and a craft works. Pick someone you can be with while they do their thing, then plan your own three photos the same way: who they are, them in action up close, then the wide moment."))
        en+=card("HOW THIS PROJECT WORKS","From an Idea to a Photo Story",
            para("You are on Step 01 now: read this page so you understand the project. Here is what comes next.")
            + bullets([
                ("Step 02 &middot; Choose Your Person:","in your journal, brainstorm three important people, with why you are considering each one and how they impacted your life, then pick the one with the strongest story."),
                ("Step 03 &middot; Storyboard &amp; Treatment:","plan your three images on paper. Sketch each one and write its full plan: composition, focal length, aperture, and lighting."),
                ("Coming next:","with your plan ready, you will photograph your important person and edit your series. New steps will appear here in this project."),
            ]))
        en+=resources_card("Key Words",
            vocab_grid("On the Quiz",
              "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
              VOCAB_EN), False)
        en+=next_up("UP NEXT &middot; STEP 02 - Choose Your Person","Open your journal and brainstorm three people you could tell a story about.")

        es=banner(f"Proyecto {PROJNUM} &bull; Paso 01","El Proyecto de la Persona Importante",
            "Cuenta la historia de alguien que cambi&oacute; tu vida, en tres fotos. Lee esta p&aacute;gina y luego ve al Paso 02.",
            "#top","Back to English", HICON_CAMERA_KIT)
        es+=type_card("overview","Paso 01 &middot; Resumen","Cuenta la Historia de Alguien en Tres Fotos",
            para("En este proyecto cuentas la historia de una persona importante en tu vida. Elige a alguien que sea parte de tu vida <strong>ahora mismo</strong> y que todav&iacute;a la haga mejor hoy. Puede ser un pap&aacute;, una mam&aacute;, una t&iacute;a, un t&iacute;o, un abuelo, un entrenador, un maestro, un mentor o un buen amigo.")
            + para("Contar&aacute;s su historia con una <strong>serie de tres im&aacute;genes</strong>, y las tres fotos se capturan en <strong>orientaci&oacute;n horizontal</strong>. Las tres im&aacute;genes trabajan juntas como una sola historia:")
            + bullets([
                ("Imagen 1 &middot; Retrato ambiental:","tu persona en su propio espacio, rodeada de las cosas que muestran qui&eacute;n es. De la cintura para arriba, y puede mirar a la c&aacute;mara o estar en un momento real."),
                ("Imagen 2 &middot; Acci&oacute;n cercana:","una foto media a cercana de tu persona en acci&oacute;n, haciendo lo suyo, encuadrada de cerca para sentir la intensidad."),
                ("Imagen 3 &middot; Acci&oacute;n abierta:","una foto m&aacute;s abierta, encuadrada de las rodillas hasta el cuerpo completo, que muestra toda la escena y el momento m&aacute;s grande."),
            ])
            + note("Las tres fotos son horizontales. Juntas van de qui&eacute;n es tu persona, a ella en acci&oacute;n de cerca, hasta la escena completa.")
            + (framed(HEADER,"Un estudiante con la persona importante que eligi&oacute; para su serie") if HAVE_HEADER else ""))
        es+=standards_box(True, STANDARDS)
        es+=card("POR QU&Eacute; ESTA PERSONA","Empieza con Alguien que Importa",
            para("Las historias en fotos m&aacute;s fuertes nacen de sentimientos reales. Piensa en alguien que hace tu vida mejor. Tal vez te ense&ntilde;a algo, cree en ti, trabaja duro por ti o te muestra c&oacute;mo hacer algo que amas.")
            + note("<strong>Elige a alguien que est&eacute; en tu vida ahora mismo.</strong> Debe seguir ayud&aacute;ndote, ense&ntilde;&aacute;ndote o inspir&aacute;ndote hoy, en el presente. Puedes escribir sobre lo que ha hecho por ti en el pasado, pero debe ser una parte positiva de tu vida ahora. Este no es un recuerdo de alguien de tu pasado.")
            + para("Entre m&aacute;s signifique la persona para ti, m&aacute;s fuertes ser&aacute;n tus fotos. Conocer&aacute;s su historia y la mostrar&aacute;s con tus tres im&aacute;genes."))
        es+=card("UNA SERIE DE EJEMPLO","Un Entrenador, Contado en Tres Fotos",
            para("As&iacute; podr&iacute;a verse una serie terminada. Imagina que tu persona importante es un entrenador de f&uacute;tbol americano.")
            + bullets([
                ("Imagen 1 &middot; Retrato ambiental:","el entrenador en el vestidor despu&eacute;s de clases, ajustando la careta a un casco. Est&aacute; rodeado de equipo, todav&iacute;a con su polo del equipo y un silbato al cuello, con luz baja y de ambiente. De la cintura para arriba y horizontal. Sabemos qui&eacute;n es antes de que diga una palabra."),
                ("Imagen 2 &middot; Acci&oacute;n cercana:","el entrenador agarrando a un jugador por la careta, d&aacute;ndole &aacute;nimo, dici&eacute;ndole que s&iacute; puede. Encuadrada de cerca y llena de intensidad. Vemos lo que hace."),
                ("Imagen 3 &middot; Acci&oacute;n abierta:","todo el equipo celebrando la victoria, con el entrenador levantando el brazo en medio de todos. Una foto abierta, de las rodillas al cuerpo completo. Sentimos el gran momento."),
            ])
            + note("Tu persona no tiene que ser un entrenador. Un cocinero en su cocina, un mec&aacute;nico en el taller, una abuela en la estufa, un m&uacute;sico en un escenario, cualquiera con un espacio y un oficio sirve. Elige a alguien con quien puedas estar mientras hace lo suyo, y luego planea tus propias tres fotos igual: qui&eacute;n es, en acci&oacute;n de cerca, y luego el momento abierto."))
        es+=card("C&Oacute;MO FUNCIONA ESTE PROYECTO","De una Idea a una Historia en Fotos",
            para("Est&aacute;s en el Paso 01 ahora: lee esta p&aacute;gina para entender el proyecto. Esto es lo que sigue.")
            + bullets([
                ("Paso 02 &middot; Elige a Tu Persona:","en tu diario, haz una lluvia de ideas de tres personas importantes, con por qu&eacute; consideras a cada una y c&oacute;mo impactaron tu vida, luego elige la de la historia m&aacute;s fuerte."),
                ("Paso 03 &middot; Storyboard y Tratamiento:","planea tus tres im&aacute;genes en papel. Dibuja cada una y escribe su plan completo: composici&oacute;n, distancia focal, apertura e iluminaci&oacute;n."),
                ("Lo que sigue:","con tu plan listo, fotografiar&aacute;s a tu persona importante y editar&aacute;s tu serie. Los nuevos pasos aparecer&aacute;n aqu&iacute; en este proyecto."),
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
        en=banner(f"Project {PROJNUM} &bull; Step 02","Choose Your Important Person",
            "A journal writing exercise. Brainstorm three people, then pick the one with the strongest story.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_SKETCH)
        en+=card("STEP 02 &middot; JOURNAL / BRAINSTORM","Write About Three People You Could Choose",
            (float_right(S2_FLOAT,"An important person in their element, doing what they do","Your important person, in their element. Who is yours?") if HAVE_S2_FLOAT else "")
            + para("Before you pick up a camera, think on paper. In your journal, brainstorm <strong>three different people</strong> you could tell a story about. Writing it out helps you choose the person with the strongest story.")
            + note("Each person on your list must be in your life <strong>right now</strong> and still helping, teaching, or inspiring you today. You can mention the past, but they have to be a positive part of your life in the present, not someone only from your past.")
            + para("For each of your three people, write <strong>why you are considering them</strong> and <strong>how they have impacted your life</strong>. A few honest sentences for each.")
            + bullets([
                ("Person 1:","their name and how you know them, why you are considering them, and how they have impacted your life."),
                ("Person 2:","their name and how you know them, why you are considering them, and how they have impacted your life."),
                ("Person 3:","their name and how you know them, why you are considering them, and how they have impacted your life."),
            ])
            + para("Stuck? Answer questions like these in your own words: What has this person done for you? What do they do that you admire? How did they change your life or help you grow? What would you want other people to see about them?")
            + note("Write in full sentences, in your own words. There are no wrong answers here. This is your thinking on paper."))
        en+=deliverables_box(False,
            [("1 journal photo (JPG):","a clear photo of your journal page showing your three people, why you are considering each one, and how they impacted your life, uploaded to this Canvas assignment.")])
        en+=card("HOW TO TURN IT IN","Scan Your Journal Page With Your iPad",
            para("Your brainstorm is on paper, so you will take a photo of it to turn it in. Use your <strong>school student iPad</strong> as a camera. This is how we scan paper work in this class.")
            + bullets([
                ("Lay your journal flat:","open to your brainstorm page in good light, with no shadow across it."),
                ("Take a photo with your student iPad:","fill the frame with your page and keep it straight, so your writing is easy to read."),
                ("Upload the JPG:","upload your photo to this Canvas assignment."),
            ]))
        en+=next_up("UP NEXT &middot; STEP 03 - Storyboard &amp; Treatment","Plan your three images on paper: sketch each one and write its full plan before you pick up a camera.")

        es=banner(f"Proyecto {PROJNUM} &bull; Paso 02","Elige a Tu Persona Importante",
            "Un ejercicio de escritura en el diario. Haz una lluvia de ideas de tres personas y elige la de la historia m&aacute;s fuerte.",
            "#top","Back to English", HICON_SKETCH)
        es+=card("PASO 02 &middot; DIARIO / LLUVIA DE IDEAS","Escribe Sobre Tres Personas que Podr&iacute;as Elegir",
            (float_right(S2_FLOAT,"Una persona importante en su elemento, haciendo lo suyo","Tu persona importante, en su elemento. &iquest;Qui&eacute;n es la tuya?") if HAVE_S2_FLOAT else "")
            + para("Antes de tomar una c&aacute;mara, piensa en papel. En tu diario, haz una lluvia de ideas de <strong>tres personas distintas</strong> sobre las que podr&iacute;as contar una historia. Escribirlo te ayuda a elegir a la persona de la historia m&aacute;s fuerte.")
            + note("Cada persona de tu lista debe estar en tu vida <strong>ahora mismo</strong> y seguir ayud&aacute;ndote, ense&ntilde;&aacute;ndote o inspir&aacute;ndote hoy. Puedes mencionar el pasado, pero debe ser una parte positiva de tu vida en el presente, no alguien solo de tu pasado.")
            + para("Para cada una de tus tres personas, escribe <strong>por qu&eacute; la est&aacute;s considerando</strong> y <strong>c&oacute;mo ha impactado tu vida</strong>. Unas cuantas oraciones honestas para cada una.")
            + bullets([
                ("Persona 1:","su nombre y c&oacute;mo la conoces, por qu&eacute; la est&aacute;s considerando y c&oacute;mo ha impactado tu vida."),
                ("Persona 2:","su nombre y c&oacute;mo la conoces, por qu&eacute; la est&aacute;s considerando y c&oacute;mo ha impactado tu vida."),
                ("Persona 3:","su nombre y c&oacute;mo la conoces, por qu&eacute; la est&aacute;s considerando y c&oacute;mo ha impactado tu vida."),
            ])
            + para("&iquest;No sabes qu&eacute; escribir? Contesta preguntas como estas con tus propias palabras: &iquest;Qu&eacute; ha hecho esta persona por ti? &iquest;Qu&eacute; hace que admiras? &iquest;C&oacute;mo cambi&oacute; tu vida o te ayud&oacute; a crecer? &iquest;Qu&eacute; te gustar&iacute;a que otras personas vieran de ella?")
            + note("Escribe en oraciones completas, con tus propias palabras. Aqu&iacute; no hay respuestas incorrectas. Este es tu pensamiento en papel."))
        es+=deliverables_box(True,
            [("1 foto del diario (JPG):","una foto clara de tu p&aacute;gina del diario que muestre tus tres personas, por qu&eacute; consideras a cada una y c&oacute;mo impactaron tu vida, subida a esta tarea de Canvas.")])
        es+=card("C&Oacute;MO ENTREGARLO","Escanea Tu P&aacute;gina del Diario con Tu iPad",
            para("Tu lluvia de ideas est&aacute; en papel, as&iacute; que tomar&aacute;s una foto de ella para entregarla. Usa tu <strong>iPad escolar de estudiante</strong> como c&aacute;mara. As&iacute; escaneamos el trabajo en papel en esta clase.")
            + bullets([
                ("Pon tu diario plano:","&aacute;brelo en tu p&aacute;gina de ideas con buena luz, sin que una sombra la cruce."),
                ("Toma una foto con tu iPad de estudiante:","llena el encuadre con tu p&aacute;gina y mantenla derecha, para que tu letra se lea f&aacute;cil."),
                ("Sube el JPG:","sube tu foto a esta tarea de Canvas."),
            ]))
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 03 - Storyboard y Tratamiento","Planea tus tres im&aacute;genes en papel: dibuja cada una y escribe su plan completo antes de tomar la c&aacute;mara.")

        stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
        return wrap_page(f"Step 2: Choose Your Person | The Important Person Project | {CL_EN} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 03: Storyboard & Treatment (plan the series, hand journal) =================
    def step03():
        en=banner(f"Project {PROJNUM} &bull; Step 03","Storyboard Your Three Images",
            "Plan your series on paper before you pick up a camera. Sketch each image and write its plan.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_SKETCH)
        en+=card("STEP 03 &middot; PLAN YOUR SERIES","Storyboard and Treatment",
            (float_right(S3_FLOAT,"A storyboard page with a hand sketch of a planned photo and a written plan beside it","Plan each image before you make it.") if HAVE_S3_FLOAT else "")
            + para("Before you photograph your important person, plan it. Real photographers call this <strong>pre-production</strong>, the thinking you do before the camera comes out. A strong plan makes a strong series.")
            + para("You will make two things in your journal for your series: a <strong>storyboard</strong> and a <strong>treatment</strong>.")
            + bullets([
                ("Storyboard:","a simple sketch of each of your three images. It does not need to be fancy. Draw a box and show where your person is, what is behind them, and what is happening."),
                ("Treatment:","a short written plan for each image. It describes exactly how you will make that photo. Treatment is the real industry word for your written plan."),
            ])
            + note("You already picked your person in Step 02. Now you plan the three photos you will take of them: one portrait and two of them in action."))
        en+=card("WHAT TO PLAN / EACH IMAGE","Write a Full Plan for All Three Images",
            para("Make one page for each of your three images. On every page, sketch the image, then write a paragraph that covers your full plan. Answer all of these:")
            + bullets([
                ("What is happening:","what is your person doing in this image, and what story does it tell?"),
                ("Composition:","how will you frame it? Where will your person sit in the photo? Think about the rule of thirds, the foreground, and the background."),
                ("Focal length:","which lens or zoom will you use? Close and tight on your person, or wide to show the whole scene?"),
                ("Aperture:","do you want a blurry background (a low f-number like f/2.8) or a sharp background (a higher f-number like f/8)?"),
                ("Lighting:","where will your light come from, and how will you shape it? Think about window light, open shade, or adding your own light."),
            ])
            + note("Remember the three image plan: image 1 is a portrait, and images 2 and 3 are your person in action, doing what they do."))
        en+=deliverables_box(False,
            [("3 storyboard pages (JPG):","a clear photo of each of your three storyboard pages, one per image, with a sketch and a full written plan on every page, uploaded to this Canvas assignment.")])
        en+=card("HOW TO TURN IT IN","Scan Your Storyboard Pages With Your iPad",
            para("Your storyboard is on paper, so take a photo of each page to turn it in. Use your <strong>school student iPad</strong> as a camera. This is how we scan paper work in this class.")
            + bullets([
                ("Lay each page flat:","good light, with no shadow across your sketch or your writing."),
                ("Take a photo with your student iPad:","fill the frame with the page and keep it straight, so your sketch and plan are easy to read."),
                ("Upload all three JPGs:","upload one photo for each image, three pages in all."),
            ]))
        en+=next_up("UP NEXT &middot; CAPTURE YOUR SERIES","With your plan ready, you will photograph your important person: your portrait and two images of them in action. New steps are coming to this project.")

        es=banner(f"Proyecto {PROJNUM} &bull; Paso 03","Haz el Storyboard de Tus Tres Im&aacute;genes",
            "Planea tu serie en papel antes de tomar la c&aacute;mara. Dibuja cada imagen y escribe su plan.",
            "#top","Back to English", HICON_SKETCH)
        es+=card("PASO 03 &middot; PLANEA TU SERIE","Storyboard y Tratamiento",
            (float_right(S3_FLOAT,"Una p&aacute;gina de storyboard con el dibujo a mano de una foto planeada y un plan escrito al lado","Planea cada imagen antes de hacerla.") if HAVE_S3_FLOAT else "")
            + para("Antes de fotografiar a tu persona importante, plan&eacute;alo. Los fot&oacute;grafos de verdad llaman a esto <strong>preproducci&oacute;n</strong>, el pensar que haces antes de sacar la c&aacute;mara. Un buen plan hace una buena serie.")
            + para("Har&aacute;s dos cosas en tu diario para tu serie: un <strong>storyboard</strong> y un <strong>tratamiento</strong>.")
            + bullets([
                ("Storyboard (gui&oacute;n gr&aacute;fico):","un dibujo sencillo de cada una de tus tres im&aacute;genes. No tiene que ser elegante. Dibuja un recuadro y muestra d&oacute;nde est&aacute; tu persona, qu&eacute; hay detr&aacute;s y qu&eacute; est&aacute; pasando."),
                ("Tratamiento (treatment):","un plan corto escrito para cada imagen. Describe exactamente c&oacute;mo vas a hacer esa foto. Tratamiento es la palabra profesional para tu plan escrito."),
            ])
            + note("Ya elegiste a tu persona en el Paso 02. Ahora planeas las tres fotos que le tomar&aacute;s: un retrato y dos de ella en acci&oacute;n."))
        es+=card("QU&Eacute; PLANEAR / CADA IMAGEN","Escribe un Plan Completo para las Tres Im&aacute;genes",
            para("Haz una p&aacute;gina para cada una de tus tres im&aacute;genes. En cada p&aacute;gina, dibuja la imagen y luego escribe un p&aacute;rrafo con tu plan completo. Contesta todo esto:")
            + bullets([
                ("Qu&eacute; est&aacute; pasando:","&iquest;qu&eacute; hace tu persona en esta imagen y qu&eacute; historia cuenta?"),
                ("Composici&oacute;n:","&iquest;c&oacute;mo vas a encuadrar? &iquest;D&oacute;nde estar&aacute; tu persona en la foto? Piensa en la regla de los tercios, el primer plano y el fondo."),
                ("Distancia focal:","&iquest;qu&eacute; lente o zoom usar&aacute;s? &iquest;Cerca y cerrado sobre tu persona, o abierto para mostrar toda la escena?"),
                ("Apertura:","&iquest;quieres un fondo borroso (un n&uacute;mero f bajo como f/2.8) o un fondo n&iacute;tido (un n&uacute;mero f m&aacute;s alto como f/8)?"),
                ("Iluminaci&oacute;n:","&iquest;de d&oacute;nde vendr&aacute; tu luz y c&oacute;mo la vas a controlar? Piensa en luz de ventana, sombra abierta o agregar tu propia luz."),
            ])
            + note("Recuerda el plan de tres im&aacute;genes: la imagen 1 es un retrato, y las im&aacute;genes 2 y 3 son tu persona en acci&oacute;n, haciendo lo que hace."))
        es+=deliverables_box(True,
            [("3 p&aacute;ginas de storyboard (JPG):","una foto clara de cada una de tus tres p&aacute;ginas de storyboard, una por imagen, con un dibujo y un plan escrito completo en cada p&aacute;gina, subida a esta tarea de Canvas.")])
        es+=card("C&Oacute;MO ENTREGARLO","Escanea Tus P&aacute;ginas de Storyboard con Tu iPad",
            para("Tu storyboard est&aacute; en papel, as&iacute; que toma una foto de cada p&aacute;gina para entregarlo. Usa tu <strong>iPad escolar de estudiante</strong> como c&aacute;mara. As&iacute; escaneamos el trabajo en papel en esta clase.")
            + bullets([
                ("Pon cada p&aacute;gina plana:","buena luz, sin que una sombra cruce tu dibujo o tu texto."),
                ("Toma una foto con tu iPad de estudiante:","llena el encuadre con la p&aacute;gina y mantenla derecha, para que tu dibujo y tu plan se lean f&aacute;cil."),
                ("Sube las tres JPG:","sube una foto por cada imagen, tres p&aacute;ginas en total."),
            ]))
        es+=next_up("A CONTINUACI&Oacute;N &middot; CAPTURA TU SERIE","Con tu plan listo, fotografiar&aacute;s a tu persona importante: tu retrato y dos im&aacute;genes de ella en acci&oacute;n. Vienen nuevos pasos a este proyecto.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
        return wrap_page(f"Step 3: Storyboard and Treatment | The Important Person Project | {CL_EN} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

    for fname,gen in [(OVER,overview),(S2,step02),(S3,step03)]:
        html=ent(gen())
        ban_check(html, fname)
        open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
        print("wrote", fname, len(html), "bytes")

for course in ("photo1","photo2"):
    print(f"--- {course} ---")
    build(course)
