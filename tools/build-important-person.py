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
HAVE_HEADER=True     # ON: Mr. Silva + Mr. Garcia. KEPT but REFRAMED (Chris 2026-10-15) as Mr. Silva's OWN example, who he would have chosen in high school when Mr. Garcia was actively his teacher. The "A Note From Mr. Silva" card explains it is NOT the student turn-in standard. assets/images/<course>/important-person/header-v1.jpg
HAVE_S2_FLOAT=True   # ON: the B&W Mr. Garcia headshot, same reframe (Mr. Silva's example, not the turn-in standard). assets/images/<course>/important-person/journal-float-v1.jpg
HAVE_S3_FLOAT=False  # Step 03 storyboard float (none supplied yet), assets/images/<course>/important-person/storyboard-float-v1.jpg

STANDARDS=[
  {"code":"SA.17.2","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Visual Communication &amp; Storytelling","es_title":"Comunicaci&oacute;n Visual y Narrativa",
   "en_desc":"You plan and tell a true, honest story that honors a real person, told as a three image photo essay.",
   "es_desc":"Planeas y cuentas una historia verdadera y honesta que honra a una persona real, contada como un ensayo fotogr&aacute;fico de tres im&aacute;genes."},
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You use framing, angle, light, and background to make each image strong and full of feeling.",
   "es_desc":"Usas el encuadre, el &aacute;ngulo, la luz y el fondo para que cada imagen sea fuerte y llena de sentimiento."},
  {"code":"SA.17.5","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Pre-Production &amp; Planning","es_title":"Preproducci&oacute;n y Planeaci&oacute;n",
   "en_desc":"You plan your photo essay intentionally: you choose your subject and storyboard your three images before you capture them.",
   "es_desc":"Planeas tu ensayo fotogr&aacute;fico de forma intencional: eliges tu sujeto y haces el storyboard de tus tres im&aacute;genes antes de capturarlas."},
  {"code":"SA.17.8","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Documentary &amp; Photojournalism","es_title":"Documental y Fotoperiodismo",
   "en_desc":"You work like a photojournalist: you capture real, honest moments and present a finished essay that moves the viewer.",
   "es_desc":"Trabajas como fotoperiodista: capturas momentos reales y honestos y presentas un ensayo terminado que conmueve a quien lo ve."},
]

VOCAB_EN=[
 ("Subject","The person you photograph. In this project, your subject is your important person."),
 ("Photo Essay","A set of photos that work together to tell one true story. Yours is a three image essay that honors your person."),
 ("Photojournalism","Telling a real, honest story with your camera. You capture true moments as they happen, not posed or faked."),
 ("Environmental Portraiture","Photographing a person in their own space or at work, so the surroundings help tell who they are. Your Image 1 is an environmental portrait."),
 ("Candid","A natural, unposed photo taken while a person is busy doing something, not looking at the camera."),
 ("Composition","How you arrange everything inside the frame: where your person sits, what is behind them, and what you leave out."),
]
VOCAB_ES=[
 ("Subject (Sujeto)","La persona que fotograf&iacute;as. En este proyecto, tu sujeto es tu persona importante."),
 ("Photo Essay (Ensayo Fotogr&aacute;fico)","Un grupo de fotos que juntas cuentan una sola historia verdadera. El tuyo es un ensayo de tres im&aacute;genes que honra a tu persona."),
 ("Photojournalism (Fotoperiodismo)","Contar una historia real y honesta con tu c&aacute;mara. Capturas momentos verdaderos tal como pasan, sin pose y sin fingir."),
 ("Environmental Portraiture (Retrato Ambiental)","Fotografiar a una persona en su propio espacio o en su trabajo, para que el entorno ayude a contar qui&eacute;n es. Tu Imagen 1 es un retrato ambiental."),
 ("Candid (Espont&aacute;nea)","Una foto natural y sin pose, tomada mientras la persona hace algo, sin mirar a la c&aacute;mara."),
 ("Composition (Composici&oacute;n)","C&oacute;mo acomodas todo dentro del encuadre: d&oacute;nde est&aacute; tu persona, qu&eacute; hay detr&aacute;s y qu&eacute; dejas fuera."),
]

# ---- Step 03 Mood Board assets (shared by both courses) ----
HAVE_ENV_SLIDER=True   # 4 environmental-portraiture examples for the Step 03 vertical slider
ENV_DIR=f"{SITE}/assets/images/important-person/env-examples"
MOODBOARD_ZIP=f"{SITE}/assets/templates/important-person/Important_Person.zip"
ENV_EXAMPLES=[
 ("env-portrait-metal-worker.jpg","A metalworker in his workshop","Un herrero en su taller"),
 ("env-portrait-butcher.jpg","A butcher in his meat locker","Un carnicero en su c&aacute;mara fr&iacute;a"),
 ("env-portrait-musician.jpg","A musician in his art-filled room","Un m&uacute;sico en su cuarto lleno de arte"),
 ("env-portrait-football.jpg","A football player on the field at night","Un jugador de f&uacute;tbol americano en el campo de noche"),
]

def env_slider(es):
    # HORIZONTAL slider: ONE large landscape image per view (flex:0 0 100%), scroll/snap to the next.
    # Image capped at ~1100px and centered so it showcases big without upscaling the 1000px source much.
    hint = "Despl&aacute;zate de lado para ver los cuatro ejemplos." if es else "Scroll sideways to see all four examples."
    hintline=f'<div style="font-size:11pt;color:#80e0e0;margin-bottom:8px;opacity:0.85;">&#8594; {hint}</div>'
    cards=""
    for slug,en_lab,es_lab in ENV_EXAMPLES:
        lab = es_lab if es else en_lab
        alt = (f"Retrato ambiental: {es_lab}" if es else f"Environmental portrait: {en_lab}")
        cards += ('<div style="flex:0 0 100%;box-sizing:border-box;scroll-snap-align:center;padding:0 4px;">'
                  + '<div style="max-width:1100px;margin:0 auto;">' + framed(f"{ENV_DIR}/{slug}", alt)
                  + f'<div style="font-size:12pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.4;">{lab}</div></div></div>')
    scroll=('<div class="silva-scroll" style="display:flex;flex-wrap:nowrap;overflow-x:auto;overflow-y:hidden;scroll-snap-type:x mandatory;'
      'padding:14px 8px 18px;margin:4px 0 2px;border:1px solid rgba(0,184,184,0.30);'
      'background:linear-gradient(90deg, rgba(0,0,0,0.16) 0%, rgba(0,0,0,0.10) 100%);">'
      f'{cards}</div>')
    return hintline+scroll

def project_downloads(es):
    # ORANGE Downloads section on the Overview: the Important_Person project-folder zip.
    heading="Descarga Tu Carpeta del Proyecto" if es else "Download Your Project Folder"
    if es:
        lead="Descarga la carpeta del proyecto Important_Person. Trae tu plantilla de mood board y dos carpetas, Inspo_Images y RAW_Images, donde ir&aacute;n tus im&aacute;genes. La usar&aacute;s en el Paso 03."
        label="Carpeta del Proyecto Important_Person (ZIP)"
        note_t="Despu&eacute;s de que se descargue, descompr&iacute;mela y mueve la carpeta Important_Person a OneDrive &rarr; Carpeta de Fotograf&iacute;a. Esa es tu carpeta para todo este proyecto."
    else:
        lead="Download the Important_Person project folder. It holds your mood board template and two folders, Inspo_Images and RAW_Images, where your images will go. You use it on Step 03."
        label="Important_Person Project Folder (ZIP)"
        note_t="After it downloads, unzip it and move the Important_Person folder into OneDrive &rarr; Photography Folder. That is your folder for this whole project."
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(lead)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">' + dl_link(MOODBOARD_ZIP, label, row=True) + '</div>'
      + note_orange(note_t) + '</div>')

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
    S3=f"{course}-important-person-step03-mood-board.html"
    S4=f"{course}-important-person-step04-storyboard.html"

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
    HREFS=[OVER,S2,S3,S4]; TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04")]
    def dots_for(ai):
        return "".join(dot("" if i==ai else HREFS[i], lab, title, i==ai, module=False) for i,(lab,title) in enumerate(TITLES))

    # ================= OVERVIEW (Step 01) =================
    def overview():
        en=banner(f"Project {PROJNUM} &bull; Step 01","The Important Person Project",
            "A three photo essay to honor someone who makes your life better. Read this page, then go to Step 02.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_CAMERA_KIT)
        en+=type_card("overview","Step 01 &middot; Overview","Honor Someone, in Three Photos",
            para("In this project you <strong>honor</strong> one important person in your life with a <strong>three image photo essay</strong>. Pick someone who is part of your life <strong>right now</strong> and still makes it better today. It could be a parent, an aunt, an uncle, a grandparent, a coach, a teacher, a mentor, or a close friend.")
            + para("This is more than three photos. It is a true story, told in images, meant to <strong>move the people who see it</strong> and make them feel why this person matters to you. All three photos are captured in <strong>horizontal (landscape) orientation</strong>, and they work together as one story:")
            + bullets([
                ("Image 1 &middot; Environmental portrait:","your person in their own space, surrounded by the things that show who they are. Waist up, and they can look at the camera or be caught in a real moment."),
                ("Image 2 &middot; Close action:","a medium to close photo of your person in action, doing their thing, framed tight so we feel the intensity."),
                ("Image 3 &middot; Wide action:","a wider photo, framed from the knees up to full body, that shows the whole scene and the bigger moment."),
            ])
            + note("All three photos are horizontal. Together they move from who your person is, to them in action up close, to the full scene.")
            + (framed(HEADER,"Mr. Silva with Mr. Garcia, the teacher who was there for him during a hard time in his childhood") + '<div style="font-size:11pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.45;">Mr. Silva with Mr. Garcia at a celebration dinner, fall 2021. The teacher he would have honored with this project back in high school. Read the note below.</div>' if HAVE_HEADER else ""))
        en+=card("A NOTE FROM MR. SILVA","Who I Would Have Chosen",
            para("The two people in the photo above are me, Mr. Silva, and Mr. Garcia. He is who I would have chosen for this project if I had done it in high school. Mr. Garcia was my teacher, and he was there for me through a hard, tumultuous time in my childhood. He still mentors me today, but the moment to tell this story was back then, when he was actively my teacher and in my corner every day. That is exactly why you choose someone who is in your life and holding you up <strong>right now</strong>.")
            + note("<strong>These photos are not what you turn in.</strong> They are images to show you who Mr. Garcia is. Your three images will be all new: thoughtful, creative, and intentional photos you plan and capture with the school camera kit, made just for this project. Every image is new work, not old pictures pulled from your camera roll."))
        en+=project_downloads(False)
        en+=card("WORK LIKE A PHOTOJOURNALIST","Tell the Truth With Your Camera",
            para("A <strong>photojournalist</strong> tells a true story with honest photos. They do not fake it. They capture real moments as they happen, and that is what makes the photos powerful.")
            + para("Do the same here. Show your person as they really are, doing what they really do. The most moving image is almost always the most honest one."))
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
                ("Step 03 &middot; Mood Board:","research reference images for all three people, then design a mood board for the one you choose."),
                ("Step 04 &middot; Storyboard &amp; Treatment:","plan your three images on paper. Sketch each one and write its full plan: composition, focal length, aperture, and lighting."),
                ("Coming next:","with your plan ready, you will photograph your important person and edit your series. New steps will appear here in this project."),
            ]))
        en+=resources_card("Key Words",
            vocab_grid("On the Quiz",
              "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
              VOCAB_EN), False)
        en+=next_up("UP NEXT &middot; STEP 02 - Choose Your Person","Open your journal and brainstorm three people you could tell a story about.")

        es=banner(f"Proyecto {PROJNUM} &bull; Paso 01","El Proyecto de la Persona Importante",
            "Un ensayo fotogr&aacute;fico de tres im&aacute;genes para honrar a alguien que hace tu vida mejor. Lee esta p&aacute;gina y luego ve al Paso 02.",
            "#top","Back to English", HICON_CAMERA_KIT)
        es+=type_card("overview","Paso 01 &middot; Resumen","Honra a Alguien, en Tres Fotos",
            para("En este proyecto <strong>honras</strong> a una persona importante en tu vida con un <strong>ensayo fotogr&aacute;fico de tres im&aacute;genes</strong>. Elige a alguien que sea parte de tu vida <strong>ahora mismo</strong> y que todav&iacute;a la haga mejor hoy. Puede ser un pap&aacute;, una mam&aacute;, una t&iacute;a, un t&iacute;o, un abuelo, un entrenador, un maestro, un mentor o un buen amigo.")
            + para("Esto es m&aacute;s que tres fotos. Es una historia verdadera, contada en im&aacute;genes, hecha para <strong>conmover a quien la ve</strong> y hacer que sienta por qu&eacute; esta persona es importante para ti. Las tres fotos se capturan en <strong>orientaci&oacute;n horizontal</strong> y trabajan juntas como una sola historia:")
            + bullets([
                ("Imagen 1 &middot; Retrato ambiental:","tu persona en su propio espacio, rodeada de las cosas que muestran qui&eacute;n es. De la cintura para arriba, y puede mirar a la c&aacute;mara o estar en un momento real."),
                ("Imagen 2 &middot; Acci&oacute;n cercana:","una foto media a cercana de tu persona en acci&oacute;n, haciendo lo suyo, encuadrada de cerca para sentir la intensidad."),
                ("Imagen 3 &middot; Acci&oacute;n abierta:","una foto m&aacute;s abierta, encuadrada de las rodillas hasta el cuerpo completo, que muestra toda la escena y el momento m&aacute;s grande."),
            ])
            + note("Las tres fotos son horizontales. Juntas van de qui&eacute;n es tu persona, a ella en acci&oacute;n de cerca, hasta la escena completa.")
            + (framed(HEADER,"El Sr. Silva con el Sr. Garcia, el maestro que estuvo con &eacute;l durante una &eacute;poca dif&iacute;cil de su ni&ntilde;ez") + '<div style="font-size:11pt;color:#80e0e0;text-align:center;margin-top:8px;opacity:0.9;line-height:1.45;">El Sr. Silva con el Sr. Garcia en una cena de celebraci&oacute;n, oto&ntilde;o de 2021. El maestro que habr&iacute;a honrado con este proyecto cuando estaba en la prepa. Lee la nota abajo.</div>' if HAVE_HEADER else ""))
        es+=card("UNA NOTA DEL SR. SILVA","A Qui&eacute;n Habr&iacute;a Elegido Yo",
            para("Las dos personas en la foto de arriba somos yo, el Sr. Silva, y el Sr. Garcia. &Eacute;l es a quien yo habr&iacute;a elegido para este proyecto si lo hubiera hecho en la prepa. El Sr. Garcia fue mi maestro, y estuvo conmigo durante una &eacute;poca dif&iacute;cil y dolorosa de mi ni&ntilde;ez. Todav&iacute;a es mi mentor hoy, pero el momento de contar esta historia era entonces, cuando era activamente mi maestro y estaba conmigo cada d&iacute;a. Por eso eliges a alguien que est&eacute; en tu vida y te sostenga <strong>ahora mismo</strong>.")
            + note("<strong>Estas fotos no son lo que entregas.</strong> Son im&aacute;genes para mostrarte qui&eacute;n es el Sr. Garcia. Tus tres im&aacute;genes ser&aacute;n todas nuevas: fotos pensadas, creativas e intencionales que planeas y capturas con el kit de c&aacute;mara de la escuela, hechas solo para este proyecto. Cada imagen es trabajo nuevo, no fotos viejas sacadas de tu galer&iacute;a."))
        es+=project_downloads(True)
        es+=card("TRABAJA COMO FOTOPERIODISTA","Di la Verdad con Tu C&aacute;mara",
            para("Un <strong>fotoperiodista</strong> cuenta una historia verdadera con fotos honestas. No finge. Captura momentos reales tal como pasan, y eso es lo que hace poderosas a las fotos.")
            + para("Haz lo mismo aqu&iacute;. Muestra a tu persona tal como es, haciendo lo que de verdad hace. La imagen que m&aacute;s conmueve casi siempre es la m&aacute;s honesta."))
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
                ("Paso 03 &middot; Mood Board:","investiga im&aacute;genes de referencia para las tres personas, luego dise&ntilde;a un mood board para la que elijas."),
                ("Paso 04 &middot; Storyboard y Tratamiento:","planea tus tres im&aacute;genes en papel. Dibuja cada una y escribe su plan completo: composici&oacute;n, distancia focal, apertura e iluminaci&oacute;n."),
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
            "A journal writing exercise. Brainstorm three people you could honor, then pick the one with the strongest story.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_SKETCH)
        en+=card("STEP 02 &middot; JOURNAL / BRAINSTORM","Write About Three People You Could Choose",
            (float_right(S2_FLOAT,"Mr. Garcia in 1996, a black and white portrait with his Hasselblad 500C medium format camera on a tripod","Mr. Garcia in 1996, with his own Hasselblad 500C. Mr. Silva&rsquo;s example (see the overview); your important person is someone active in your life now.") if HAVE_S2_FLOAT else "")
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
        en+=next_up("UP NEXT &middot; STEP 03 - Build Your Mood Board","Research reference images for your three people, then design a mood board for the one you choose.")

        es=banner(f"Proyecto {PROJNUM} &bull; Paso 02","Elige a Tu Persona Importante",
            "Un ejercicio de escritura en el diario. Haz una lluvia de ideas de tres personas que podr&iacute;as honrar y elige la de la historia m&aacute;s fuerte.",
            "#top","Back to English", HICON_SKETCH)
        es+=card("PASO 02 &middot; DIARIO / LLUVIA DE IDEAS","Escribe Sobre Tres Personas que Podr&iacute;as Elegir",
            (float_right(S2_FLOAT,"El Sr. Garcia en 1996, un retrato en blanco y negro con su c&aacute;mara Hasselblad 500C de formato medio sobre un tr&iacute;pode","El Sr. Garcia en 1996, con su propia Hasselblad 500C. El ejemplo del Sr. Silva (ver el resumen); tu persona importante es alguien activo en tu vida ahora.") if HAVE_S2_FLOAT else "")
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
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 03 - Crea Tu Mood Board","Investiga im&aacute;genes de referencia para tus tres personas, luego dise&ntilde;a un mood board para la que elijas.")

        stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
        return wrap_page(f"Step 2: Choose Your Person | The Important Person Project | {CL_EN} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 03: Mood Board (research + design, Photoshop) =================
    def step03():
        en=banner(f"Project {PROJNUM} &bull; Step 03","Build Your Mood Board",
            "Research the photos you want to make, then design a mood board for the person you choose.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_DESIGN)
        en+=card("STEP 03 &middot; GATHER YOUR VISION","What a Mood Board Is",
            para("A <strong>mood board</strong> is a collage of reference images that shows the look and the feeling you are going for, before you ever pick up a camera. Photographers, designers, and filmmakers all build one. Yours collects the kinds of photos you want to make of your important person.")
            + para("Study these <strong>environmental portraits</strong>. Each one shows a person in their own world, their space, their tools, their light, so you understand who they are before they say a word. That is what your Image 1 is after.")
            + (env_slider(False) if HAVE_ENV_SLIDER else "")
            + note("Reference images are for inspiration only. They are not your photos. You will capture your own real images later with the school camera kit."))
        if p2:
            en+=card("YOUR LIGHTING &middot; REQUIRED","You Light Every Image With Off-Camera Flash",
                para("In Photography 2, you <strong>light all three images with off-camera flash</strong>. You will use our <strong>Godox AD200 Pro II</strong> on a light stand with a modifier, placed off to the side to shape the light the way you want. This is required for every photo.")
                + para("So your research and your mood board should show the <strong>lighting look</strong> you are going for: light that is placed intentionally and shaped, not just whatever light is already there. Look for reference images with strong, directional, off-camera light.")
                + note("Photographing outdoors in bright sun? You may also need <strong>ND filters</strong> to control the exposure, and a <strong>scrim</strong> with an assistant, a classmate or a family member, to soften or block the sun. Plan for that in your mood board."))
        else:
            en+=card("YOUR LIGHTING","Work With the Light You Have",
                para("In Photography 1, you are <strong>not required</strong> to use off-camera flash, strobes, or modifiers. Work with the natural light in your person&rsquo;s space. Real, honest light is part of telling a true story.")
                + para("If you want to push for higher-quality images, <strong>reflectors and scrims</strong> are available to bounce light into shadows or soften harsh sun. Use them if they help your photo, they are optional for you. Let your research and mood board show the light you can actually work with."))
        en+=card("RESEARCH ALL THREE / COLLECT YOUR INSPO","Find Reference Images for Your Three People",
            para("In Step 02 you brainstormed three people. Now research <strong>all three</strong>. For each person, collect <strong>six reference images</strong> from the internet that show the kinds of photos you want to make of them.")
            + bullets([
                ("2 for the environmental portrait:","a person in their own space, like your Image 1."),
                ("2 for the first action image:","a person doing the thing your person is known for."),
                ("2 for the second action image:","that same action from a wider angle or a different moment."),
            ])
            + para("That is six images per person, for all three people, so <strong>18 reference images</strong> in all. Save them into the <strong>Inspo_Images</strong> folder inside the Important_Person project folder you downloaded on Step 01.")
            + note("Look for images of your person helping or inspiring others the way they help you, doing what they are known to do. This is research, so you know what you want to capture."))
        en+=deliverables_box(False,
            [("1 inspo folder (PNG):","a screen capture of your Inspo_Images folder in icon view, showing all 18 reference images, uploaded to this Canvas assignment."),
             ("1 mood board (JPG):","your finished mood board for the person you chose, with their name in the bottom right, exported as a JPG and uploaded to this Canvas assignment.")])
        en+=card("SHOW YOUR RESEARCH","Capture Your Inspo Folder (All 18)",
            para("Prove you did the research for all three people. Open your <strong>Inspo_Images</strong> folder and capture it.")
            + bullets([
                ("Set the view to icons:","in Finder, click <strong>View &gt; as Icons</strong> so every image shows as a thumbnail."),
                ("Capture the whole screen:","press <strong>Shift</strong> + <strong>Cmd</strong> + <strong>3</strong>. A PNG of your screen saves to your Desktop."),
                ("Check it shows all 18:","your capture should show all 18 reference images."),
                ("Upload the PNG:","upload that PNG to this Canvas assignment."),
            ]))
        en+=card("CHOOSE, THEN BUILD IT / IN PHOTOSHOP","Pick One Person and Make the Mood Board",
            para("Now choose. Look at your research and pick the one person with the strongest story, the one you will actually photograph. <strong>Talk to Mr. Silva about your choice.</strong> He will come around next week to see your three people and your inspiration images, so he knows who you picked and what you plan to capture.")
            + note("You build <strong>one</strong> mood board, for the person you settle on. Your Inspo folder still has to show the research for all three.")
            + bullets([
                ("Open the template:","open <strong>Important_Person_Mood_Board.psd</strong> from your project folder in Photoshop."),
                ("Place your images:","go to <strong>File &gt; Place Embedded</strong> and add at least six of your reference images for the person you chose, two for each of your three planned images. Arrange them to fill the board."),
                ("Add the name:","in the <strong>Name:</strong> field at the bottom right, type your important person&rsquo;s name."),
                ("Save a copy as JPG:","go to <strong>File &gt; Save a Copy</strong>, change the format to <strong>JPG</strong>, and save it in your project folder."),
                ("Upload the JPG:","upload your mood board JPG to this Canvas assignment."),
            ]))
        en+=next_up("UP NEXT &middot; STEP 04 - Storyboard &amp; Treatment","With your person chosen and your vision set, plan your three images on paper: sketch each one and write its full plan.")

        es=banner(f"Proyecto {PROJNUM} &bull; Paso 03","Crea Tu Mood Board",
            "Investiga las fotos que quieres hacer, luego dise&ntilde;a un mood board para la persona que elijas.",
            "#top","Back to English", HICON_DESIGN)
        es+=card("PASO 03 &middot; RE&Uacute;NE TU VISI&Oacute;N","Qu&eacute; Es un Mood Board",
            para("Un <strong>mood board</strong> es un collage de im&aacute;genes de referencia que muestra el estilo y el sentimiento que buscas, antes de tomar una c&aacute;mara. Los fot&oacute;grafos, dise&ntilde;adores y cineastas lo usan. El tuyo re&uacute;ne el tipo de fotos que quieres hacer de tu persona importante.")
            + para("Observa estos <strong>retratos ambientales</strong>. Cada uno muestra a una persona en su propio mundo, su espacio, sus herramientas, su luz, para que sepas qui&eacute;n es antes de que diga una palabra. Eso es lo que busca tu Imagen 1.")
            + (env_slider(True) if HAVE_ENV_SLIDER else "")
            + note("Las im&aacute;genes de referencia son solo inspiraci&oacute;n. No son tus fotos. Captura tus propias im&aacute;genes reales despu&eacute;s con el kit de c&aacute;mara de la escuela."))
        if p2:
            es+=card("TU ILUMINACI&Oacute;N &middot; OBLIGATORIA","Iluminas Cada Imagen con Flash Fuera de C&aacute;mara",
                para("En Fotograf&iacute;a 2, <strong>iluminas las tres im&aacute;genes con flash fuera de c&aacute;mara</strong>. Usar&aacute;s nuestro <strong>Godox AD200 Pro II</strong> en un tr&iacute;pode de luz con un modificador, colocado a un lado para dar forma a la luz como t&uacute; quieras. Es obligatorio para cada foto.")
                + para("Por eso tu investigaci&oacute;n y tu mood board deben mostrar el <strong>estilo de luz</strong> que buscas: luz colocada de forma intencional y con forma, no solo la que ya hay. Busca im&aacute;genes de referencia con luz fuerte, direccional y fuera de c&aacute;mara.")
                + note("&iquest;Fotografiando al aire libre bajo el sol fuerte? Tambi&eacute;n puedes necesitar <strong>filtros ND</strong> para controlar la exposici&oacute;n, y un <strong>scrim</strong> con un asistente, un compa&ntilde;ero o un familiar, para suavizar o bloquear el sol. Pl&aacute;nealo en tu mood board."))
        else:
            es+=card("TU ILUMINACI&Oacute;N","Trabaja con la Luz que Tienes",
                para("En Fotograf&iacute;a 1, <strong>no est&aacute;s obligado</strong> a usar flash fuera de c&aacute;mara, estrobos ni modificadores. Trabaja con la luz natural del espacio de tu persona. La luz real y honesta es parte de contar una historia verdadera.")
                + para("Si quieres lograr im&aacute;genes de mayor calidad, hay <strong>reflectores y scrims</strong> disponibles para rebotar luz hacia las sombras o suavizar el sol fuerte. &Uacute;salos si ayudan a tu foto, para ti son opcionales. Deja que tu investigaci&oacute;n y tu mood board muestren la luz con la que de verdad puedes trabajar."))
        es+=card("INVESTIGA LAS TRES / RE&Uacute;NE TU INSPO","Busca Im&aacute;genes de Referencia para Tus Tres Personas",
            para("En el Paso 02 pensaste en tres personas. Ahora investiga a <strong>las tres</strong>. Para cada persona, re&uacute;ne <strong>seis im&aacute;genes de referencia</strong> de internet que muestren el tipo de fotos que quieres hacer de ella.")
            + bullets([
                ("2 para el retrato ambiental:","una persona en su propio espacio, como tu Imagen 1."),
                ("2 para la primera imagen de acci&oacute;n:","una persona haciendo aquello por lo que tu persona es conocida."),
                ("2 para la segunda imagen de acci&oacute;n:","esa misma acci&oacute;n desde un &aacute;ngulo m&aacute;s abierto o en otro momento."),
            ])
            + para("Son seis im&aacute;genes por persona, para las tres personas, as&iacute; que <strong>18 im&aacute;genes de referencia</strong> en total. Gu&aacute;rdalas en la carpeta <strong>Inspo_Images</strong> dentro de la carpeta del proyecto Important_Person que descargaste en el Paso 01.")
            + note("Busca im&aacute;genes de tu persona ayudando o inspirando a otros como te ayuda a ti, haciendo lo que la hace conocida. Es investigaci&oacute;n, para saber qu&eacute; quieres capturar."))
        es+=deliverables_box(True,
            [("1 carpeta inspo (PNG):","una captura de pantalla de tu carpeta Inspo_Images en vista de iconos, que muestre las 18 im&aacute;genes de referencia, subida a esta tarea de Canvas."),
             ("1 mood board (JPG):","tu mood board terminado de la persona que elegiste, con su nombre abajo a la derecha, exportado como JPG y subido a esta tarea de Canvas.")])
        es+=card("MUESTRA TU INVESTIGACI&Oacute;N","Captura Tu Carpeta Inspo (Las 18)",
            para("Demuestra que investigaste a las tres personas. Abre tu carpeta <strong>Inspo_Images</strong> y capt&uacute;rala.")
            + bullets([
                ("Pon la vista en iconos:","en Finder, haz clic en <strong>Visualizaci&oacute;n &gt; como Iconos</strong> para que cada imagen se vea como miniatura."),
                ("Captura toda la pantalla:","presiona <strong>Shift</strong> + <strong>Cmd</strong> + <strong>3</strong>. Un PNG de tu pantalla se guarda en tu Escritorio."),
                ("Revisa que se vean las 18:","tu captura debe mostrar las 18 im&aacute;genes de referencia."),
                ("Sube el PNG:","sube ese PNG a esta tarea de Canvas."),
            ]))
        es+=card("ELIGE Y CONSTR&Uacute;YELO / EN PHOTOSHOP","Elige a Una Persona y Haz el Mood Board",
            para("Ahora elige. Mira tu investigaci&oacute;n y escoge a la persona con la historia m&aacute;s fuerte, la que de verdad vas a fotografiar. <strong>Habla con el Sr. Silva sobre tu elecci&oacute;n.</strong> &Eacute;l pasar&aacute; la pr&oacute;xima semana a ver tus tres personas y tus im&aacute;genes de inspiraci&oacute;n, para saber a qui&eacute;n elegiste y qu&eacute; planeas capturar.")
            + note("Haces <strong>un</strong> mood board, de la persona que elijas. Tu carpeta Inspo igual debe mostrar la investigaci&oacute;n de las tres.")
            + bullets([
                ("Abre la plantilla:","abre <strong>Important_Person_Mood_Board.psd</strong> de tu carpeta del proyecto en Photoshop."),
                ("Coloca tus im&aacute;genes:","ve a <strong>Archivo &gt; Colocar incrustado</strong> y agrega al menos seis de tus im&aacute;genes de referencia de la persona que elegiste, dos por cada una de tus tres im&aacute;genes planeadas. Acom&oacute;dalas para llenar el tablero."),
                ("Agrega el nombre:","en el campo <strong>Name:</strong> de abajo a la derecha, escribe el nombre de tu persona importante."),
                ("Guarda una copia como JPG:","ve a <strong>Archivo &gt; Guardar una copia</strong>, cambia el formato a <strong>JPG</strong> y gu&aacute;rdalo en tu carpeta del proyecto."),
                ("Sube el JPG:","sube tu mood board JPG a esta tarea de Canvas."),
            ]))
        es+=next_up("A CONTINUACI&Oacute;N &middot; PASO 04 - Storyboard y Tratamiento","Con tu persona elegida y tu visi&oacute;n lista, planea tus tres im&aacute;genes en papel: dibuja cada una y escribe su plan completo.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S4}" class="silva-step-btn">Step 04 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S4}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
        return wrap_page(f"Step 3: Mood Board | The Important Person Project | {CL_EN} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 04: Storyboard & Treatment (plan the series, hand journal) =================
    def step04():
        en=banner(f"Project {PROJNUM} &bull; Step 04","Storyboard Your Three Images",
            "Plan your series on paper before you pick up a camera. Sketch each image and write its plan.",
            "#espanol","Clic para Espa&ntilde;ol", HICON_SKETCH)
        en+=card("STEP 04 &middot; PLAN YOUR SERIES","Storyboard and Treatment",
            (float_right(S3_FLOAT,"A storyboard page with a hand sketch of a planned photo and a written plan beside it","Plan each image before you make it.") if HAVE_S3_FLOAT else "")
            + para("Before you photograph your important person, plan it. Real photographers call this <strong>pre-production</strong>, the thinking you do before the camera comes out. A strong plan makes a strong series.")
            + para("You will make two things in your journal for your series: a <strong>storyboard</strong> and a <strong>treatment</strong>.")
            + bullets([
                ("Storyboard:","a simple sketch of each of your three images. It does not need to be fancy. Draw a box and show where your person is, what is behind them, and what is happening."),
                ("Treatment:","a short written plan for each image. It describes exactly how you will make that photo. Treatment is the real industry word for your written plan."),
            ])
            + note("You chose your person in Step 02 and built your mood board in Step 03. Now plan the three photos you will take of them: one portrait and two of them in action."))
        en+=card("WHAT TO PLAN / EACH IMAGE","Write a Full Plan for All Three Images",
            para("Make one page for each of your three images. On every page, sketch the image, then write a paragraph that covers your full plan. Answer all of these:")
            + bullets([
                ("What is happening, and the feeling:","what is your person doing in this image, what story does it tell, and what should the viewer <strong>feel</strong> when they see it?"),
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

        es=banner(f"Proyecto {PROJNUM} &bull; Paso 04","Haz el Storyboard de Tus Tres Im&aacute;genes",
            "Planea tu serie en papel antes de tomar la c&aacute;mara. Dibuja cada imagen y escribe su plan.",
            "#top","Back to English", HICON_SKETCH)
        es+=card("PASO 04 &middot; PLANEA TU SERIE","Storyboard y Tratamiento",
            (float_right(S3_FLOAT,"Una p&aacute;gina de storyboard con el dibujo a mano de una foto planeada y un plan escrito al lado","Planea cada imagen antes de hacerla.") if HAVE_S3_FLOAT else "")
            + para("Antes de fotografiar a tu persona importante, plan&eacute;alo. Los fot&oacute;grafos de verdad llaman a esto <strong>preproducci&oacute;n</strong>, el pensar que haces antes de sacar la c&aacute;mara. Un buen plan hace una buena serie.")
            + para("Har&aacute;s dos cosas en tu diario para tu serie: un <strong>storyboard</strong> y un <strong>tratamiento</strong>.")
            + bullets([
                ("Storyboard (gui&oacute;n gr&aacute;fico):","un dibujo sencillo de cada una de tus tres im&aacute;genes. No tiene que ser elegante. Dibuja un recuadro y muestra d&oacute;nde est&aacute; tu persona, qu&eacute; hay detr&aacute;s y qu&eacute; est&aacute; pasando."),
                ("Tratamiento (treatment):","un plan corto escrito para cada imagen. Describe exactamente c&oacute;mo vas a hacer esa foto. Tratamiento es la palabra profesional para tu plan escrito."),
            ])
            + note("Elegiste a tu persona en el Paso 02 y creaste tu mood board en el Paso 03. Ahora planeas las tres fotos que le tomar&aacute;s: un retrato y dos de ella en acci&oacute;n."))
        es+=card("QU&Eacute; PLANEAR / CADA IMAGEN","Escribe un Plan Completo para las Tres Im&aacute;genes",
            para("Haz una p&aacute;gina para cada una de tus tres im&aacute;genes. En cada p&aacute;gina, dibuja la imagen y luego escribe un p&aacute;rrafo con tu plan completo. Contesta todo esto:")
            + bullets([
                ("Qu&eacute; est&aacute; pasando y qu&eacute; se siente:","&iquest;qu&eacute; hace tu persona en esta imagen, qu&eacute; historia cuenta y qu&eacute; debe <strong>sentir</strong> quien la ve?"),
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

        stepnav=f'<a href="{S3}" class="silva-step-btn">&#8592; Step 03</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S3}" class="silva-bottom-btn">&#8592; Step 03</a><span></span></div>'
        return wrap_page(f"Step 4: Storyboard and Treatment | The Important Person Project | {CL_EN} | PVHS", nav("Step 04",dots_for(3),stepnav), top_wrap(en,es), bottom)

    for fname,gen in [(OVER,overview),(S2,step02),(S3,step03),(S4,step04)]:
        html=ent(gen())
        ban_check(html, fname)
        open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
        print("wrote", fname, len(html), "bytes")

for course in ("photo1","photo2"):
    print(f"--- {course} ---")
    build(course)
