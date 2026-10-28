#!/usr/bin/env python3
# Spooky Portraits: Lighting Plan & Portrait Project. The two courses now DIVERGE (Chris, 2026-10-28):
#   Photography 2A (Module 11, struct="plan", ADVANCED): Overview, Plan (reference folder + lighting-plan
#     journal page), Capture & Deliver, Reflection. Keeps the hand-drawn lighting-plan journal.
#   Photography 1A (Module 11, struct="contact", 1ST-YEAR, simplified): NO journal page. Panther-style
#     flow: Overview, Capture & Contact Sheet (gather the inspiration folder, then capture + contact
#     sheet), Cull/Edit/Deliver, Reflection. The light-direction grid + cheat sheet live on the Overview.
# Both: groups of three rotate subject / lighting assistant / camera operator and make THREE portraits
# from a lighting design (continuous Amaran RGB lights). The group makes 3 (one per rotation); all three
# share the files and each student culls, edits, and submits their own 3 edited JPGs (RAW capture).
# Bilingual, 5th-grade, camera-kit studio (no own-device note). Hero = Chris's Spooky poster. Floats:
# header + the underlit example + the direction grid + the Pennywise-style fun example are LIVE; the
# plan-diagram float is gated off.
import os, re
from silva_framework import *

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"

IMGDIR=f"{SITE}/assets/images/shared/spooky-portraits"
HEADER=f"{IMGDIR}/header-v1.jpg"
PLAN_FLOAT=f"{IMGDIR}/plan-float-v1.jpg"
CAP_FLOAT=f"{IMGDIR}/capture-float-v1.jpg"
DIRECTIONS=f"{IMGDIR}/directions-v1.jpg"   # 5-direction lighting reference grid (Chris)
INSPO=f"{IMGDIR}/inspo-float-v1.jpg"        # fun horror-lighting example portrait (Chris)
HAVE_HEADER=True
HAVE_PLAN_FLOAT=False
HAVE_CAP_FLOAT=True
HAVE_DIRECTIONS=True
HAVE_INSPO=True

COURSES=[
  {"prefix":"photo1","title":"Photography 1A","zip":f"{SITE}/assets/course-documents/Spooky-Portraits-Project-Folder-Photo1.zip","struct":"contact"},
  {"prefix":"photo2","title":"Photography 2A","zip":f"{SITE}/assets/course-documents/Spooky-Portraits-Project-Folder-Photo2.zip","struct":"plan"},
]

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

SPOOKY_STANDARDS=[
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You use light position, height, and color on purpose to build a mood.",
   "es_desc":"Usas la posici&oacute;n, la altura y el color de la luz a prop&oacute;sito para crear un ambiente."},
  {"code":"SA.17.3","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Planning &amp; Pre-Production","es_title":"Planeaci&oacute;n y Preproducci&oacute;n",
   "en_desc":"You study horror-lighting references and plan the look before you capture.",
   "es_desc":"Estudias referencias de iluminaci&oacute;n de terror y planeas el look antes de capturar."},
  {"code":"SA.17.5","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Equipment &amp; Image Production","es_title":"Equipo y Producci&oacute;n de Imagen",
   "en_desc":"You run continuous RGB studio lights and a camera in Manual, and capture in RAW.",
   "es_desc":"Manejas luces de estudio RGB continuas y una c&aacute;mara en Manual, y capturas en RAW."},
  {"code":"SA.17.6","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Digital Editing &amp; Workflow","es_title":"Edici&oacute;n Digital y Flujo de Trabajo",
   "en_desc":"You import RAW files, build contact sheets, edit in Lightroom Classic, and export clean JPGs.",
   "es_desc":"Importas archivos RAW, creas hojas de contactos, editas en Lightroom Classic y exportas JPG limpios."},
]

def spooky_settings(es):
    # RED camera settings. Continuous studio lights, so the key teaching point is a FIXED white balance
    # (Daylight), NOT Auto, so the colored lights show up as chosen.
    red="#f90101"
    raw_badge=f'<img src="{RAW_BADGE}" alt="RAW" style="height:1.5em;width:auto;vertical-align:middle;margin:0 3px;display:inline-block;" />'
    if es:
        title="Ajustes de C&aacute;mara"
        lead=("Usa la c&aacute;mara en modo Manual (M). Con luces de colores, el ajuste m&aacute;s importante es el "
               "<strong>balance de blancos</strong>: ponlo fijo en Luz de D&iacute;a (Daylight), NO en autom&aacute;tico, "
               "para que tus colores se vean como los planeaste.")
        items=[
            ("Modo:","Manual (M)."),
            ("Balance de blancos:","fijo en Luz de D&iacute;a (Daylight). No uses autom&aacute;tico."),
            ("Apertura:","f/4 a f/5.6, para una cara n&iacute;tida."),
            ("ISO:","lo m&aacute;s bajo que permita la luz."),
            ("Obturador:","lo bastante r&aacute;pido para evitar movimiento. Revisa la pantalla."),
            ("Enfoque:","en los ojos."),
            ("Formato:",f"captura en RAW {raw_badge} para tener el mayor detalle al editar."),
        ]
        note_t="Una foto un poco subexpuesta puede dar m&aacute;s ambiente, pero cuida las luces altas. Revisa el histograma."
    else:
        title="Camera Settings"
        lead=("Use the camera in Manual mode (M). With colored lights, the most important setting is your "
               "<strong>white balance</strong>: set it to a fixed Daylight value, NOT Auto, so your colors "
               "show up the way you planned them.")
        items=[
            ("Mode:","Manual (M)."),
            ("White balance:","fixed on Daylight. Do not use Auto."),
            ("Aperture:","f/4 to f/5.6, for a sharp face."),
            ("ISO:","as low as the light allows."),
            ("Shutter:","fast enough to avoid blur. Check the screen."),
            ("Focus:","on the eyes."),
            ("Format:",f"capture in RAW {raw_badge} so you have the most detail to edit."),
        ]
        note_t="A slightly underexposed frame can add mood, but protect the highlights. Check the histogram."
    lead_html=f'<div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{lead}</span></div>'
    note_box=f'<div style="background:rgba(249,1,1,0.10);border:1px solid rgba(249,1,1,0.30);border-left:4px solid {red};padding:11px 14px;margin:8px 0 0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.92);line-height:1.55;"><strong>{note_t}</strong></div>'
    return (f'<div style="background:linear-gradient(180deg,rgba(249,1,1,0.06) 0%,rgba(249,1,1,0.02) 100%);border:1px solid rgba(249,1,1,0.26);border-left:6px solid {red};padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(CAMSET_ICON, title, "#f90101", "#ff8f8f")
      + lead_html + bullets(items, accent=red) + note_box + '</div>')

def safety_card(es):
    if es:
        return card("SEGURIDAD Y RESPETO","Mant&eacute;n el Estudio Seguro y Amable",
            bullets([
                ("Asegura las bases:","pon sacos de arena en las bases de las luces y pega los cables con cinta."),
                ("Cuida tus ojos:","no mires fijo a las luces cuando est&eacute;n muy brillantes."),
                ("Sin parpadeos:","mant&eacute;n los colores fijos. Sin parpadeos ni efectos de estrobo."),
                ("Apropiado para la escuela:","los disfraces, el maquillaje y los objetos deben ser apropiados para la escuela. Nada de armas ni objetos que parezcan armas."),
                ("Pregunta primero:","pide permiso al sujeto antes de posar, usar disfraces o tocar el cabello o la ropa. S&eacute; respetuoso con tus compa&ntilde;eros."),
            ]))
    return card("SAFETY &amp; RESPECT","Keep the Studio Safe and Kind",
        bullets([
            ("Steady the stands:","put sandbags on light stands and tape down any cables."),
            ("Protect your eyes:","do not stare into the lights at high brightness."),
            ("No flashing:","keep the colors steady. No flashing or strobe effects."),
            ("School appropriate:","costumes, makeup, and props must be school appropriate. No weapons or items that look like weapons."),
            ("Ask first:","get the subject&rsquo;s okay before posing, costumes, or touching hair or clothing. Be respectful with your classmates."),
        ]))

def build_course(c):
    prefix=c["prefix"]; CT=c["title"]; ZIP=c["zip"]; struct=c["struct"]
    CONTACT = (struct=="contact")
    OVER=f"{prefix}-spooky-portraits-overview.html"
    if CONTACT:
        S1=f"{prefix}-spooky-portraits-step01-capture-contact.html"
        S2=f"{prefix}-spooky-portraits-step02-cull-edit-deliver.html"
    else:
        S1=f"{prefix}-spooky-portraits-step01-plan.html"
        S2=f"{prefix}-spooky-portraits-step02-capture-deliver.html"
    S3=f"{prefix}-spooky-portraits-step03-reflection.html"

    def nav(current,dots,stepnav):
        return ('      <div class="silva-breadcrumb">\n'
                '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
                '        <span class="bc-sep">&rsaquo;</span>\n'
                f'        <a href="{OVER}" class="bc-hide-sm">Spooky Portraits</a>\n'
                '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
                f'        <span class="bc-current">{current}</span>\n'
                '      </div>\n'
                '      <div class="silva-nav-spacer"></div>\n'
                f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
                f'      <div class="silva-step-nav">{stepnav}</div>')
    DT=[("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04")]
    def dots_for(active):
        hrefs=[OVER,S1,S2,S3]; r=""
        for i,(lab,title) in enumerate(DT):
            r+=dot("" if i==active else hrefs[i], lab, title, i==active, module=False)
        return r

    def project_downloads(es):
        if es:
            heading="Descarga Tu Carpeta del Proyecto"
            lead=("Descarga tu carpeta del proyecto. Es un archivo .zip. Al abrirlo tendr&aacute;s la carpeta "
                  "<strong>Spooky_Portraits</strong>, y adentro hay una carpeta <strong>RAW_Images</strong> para tus fotos RAW, "
                  "una carpeta <strong>Reference_Images</strong> para tus im&aacute;genes de inspiraci&oacute;n, "
                  "y tu documento de reflexi&oacute;n (en ingl&eacute;s y en espa&ntilde;ol).")
            label="Carpeta del Proyecto (.zip)"
            note_t=("<strong style=\"color:#ffb27c;\">Mantente organizado:</strong> cuando el .zip termine de descargarse, "
                    "&aacute;brelo y mueve la carpeta <strong>Spooky_Portraits</strong> a "
                    f"OneDrive &rarr; {AREA}. Guarda tus fotos RAW dentro de <strong>RAW_Images</strong> y tus im&aacute;genes de inspiraci&oacute;n dentro de <strong>Reference_Images</strong>.")
        else:
            heading="Download Your Project Folder"
            lead=("Download your project folder. It is a .zip file. When you open it you get the "
                  "<strong>Spooky_Portraits</strong> folder, and inside it is a <strong>RAW_Images</strong> folder for your RAW "
                  "photos, a <strong>Reference_Images</strong> folder for your inspiration images, "
                  "and your reflection document (English and Spanish).")
            label="Project Folder (.zip)"
            note_t=("<strong style=\"color:#ffb27c;\">Stay organized:</strong> when the .zip finishes downloading, "
                    "open it and move the <strong>Spooky_Portraits</strong> folder into "
                    f"OneDrive &rarr; {AREA}. Keep your RAW photos inside <strong>RAW_Images</strong> and your inspiration images inside <strong>Reference_Images</strong>.")
        return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
          + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
          + para(lead)
          + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
          + dl_link(ZIP, label, row=True)
          + '</div>'
          + f'<div style="margin-top:16px;font-size:12pt;color:rgba(255,255,255,0.82);line-height:1.55;">{note_t}</div>'
          + '</div>')

    def cheat_sheet(es):
        if es:
            heading="Gu&iacute;a R&aacute;pida de Iluminaci&oacute;n"
            body=(para("Usa esta gu&iacute;a mientras dise&ntilde;as. T&uacute; decides: elige a prop&oacute;sito y explica tu elecci&oacute;n.")
              + '<div style="font-size:11pt;letter-spacing:0.14em;text-transform:uppercase;color:#c4b5fd;margin:6px 0 6px;"><strong>Altura de la Luz</strong></div>'
              + bullets([("A la altura de los ojos:","pareja y plana. Normal y tranquila."),
                         ("Baja, apuntando arriba:","luz desde abajo. Rara y espeluznante, estilo monstruo cl&aacute;sico."),
                         ("Alta, apuntando abajo:","sombras profundas en los ojos y bajo la nariz. Misteriosa.")], accent="#8b5cf6")
              + '<div style="font-size:11pt;letter-spacing:0.14em;text-transform:uppercase;color:#c4b5fd;margin:10px 0 6px;"><strong>Direcci&oacute;n</strong></div>'
              + bullets([("De frente:","plana, menos dram&aacute;tica."),
                         ("De lado:","sombras fuertes, mucho drama."),
                         ("Desde atr&aacute;s (rim):","un borde de luz alrededor del pelo y los hombros.")], accent="#8b5cf6")
              + '<div style="font-size:11pt;letter-spacing:0.14em;text-transform:uppercase;color:#c4b5fd;margin:10px 0 6px;"><strong>Color y Ambiente</strong></div>'
              + bullets([("Verde:","enfermizo, t&oacute;xico."),("Rojo:","peligro, miedo."),("Azul:","fr&iacute;o, de luna, fantasmal."),
                         ("Morado:","sobrenatural, extra&ntilde;o."),("&Aacute;mbar:","de vela, c&aacute;lido, vintage."),
                         ("Dos colores juntos:","azul y &aacute;mbar, o verde y magenta, dan un look de cine.")], accent="#8b5cf6"))
            return resources_card(heading, body, True)
        heading="Lighting Cheat Sheet"
        body=(para("Use this while you design. You decide: choose on purpose and be ready to explain your choice.")
          + '<div style="font-size:11pt;letter-spacing:0.14em;text-transform:uppercase;color:#c4b5fd;margin:6px 0 6px;"><strong>Light Height</strong></div>'
          + bullets([("Eye level:","even and flat. Plain and calm."),
                     ("Low, angled up:","light from below. Eerie and unnatural, the classic monster feel."),
                     ("High, angled down:","deep shadows in the eyes and under the nose. Mysterious.")], accent="#8b5cf6")
          + '<div style="font-size:11pt;letter-spacing:0.14em;text-transform:uppercase;color:#c4b5fd;margin:10px 0 6px;"><strong>Direction</strong></div>'
          + bullets([("Front:","flat, less dramatic."),
                     ("Side:","strong shadows, high drama."),
                     ("From behind (rim):","a glowing edge around the hair and shoulders.")], accent="#8b5cf6")
          + '<div style="font-size:11pt;letter-spacing:0.14em;text-transform:uppercase;color:#c4b5fd;margin:10px 0 6px;"><strong>Color &amp; Mood</strong></div>'
          + bullets([("Green:","sickly, toxic."),("Red:","danger, fear."),("Blue:","cold, moonlight, ghostly."),
                     ("Purple:","supernatural, strange."),("Amber:","candlelight, warm, vintage."),
                     ("Two colors together:","blue and amber, or green and magenta, give a cinematic look.")], accent="#8b5cf6"))
        return resources_card(heading, body, False)

    def direction_card(es):
        if es:
            return card("DIRECCI&Oacute;N DE LA LUZ / VE LA DIFERENCIA","Cinco Formas de Iluminar una Cara",
                para("D&oacute;nde pones la luz lo cambia todo. Aqu&iacute; est&aacute; la misma cara iluminada desde cinco direcciones. &Uacute;sala para elegir la posici&oacute;n de tu luz.")
                + (framed(DIRECTIONS,"Una referencia de iluminaci&oacute;n: la misma cara iluminada desde el frente, a 45 grados, de lado, por detr&aacute;s y desde abajo, cada una con un peque&ntilde;o diagrama de la posici&oacute;n de la luz") if HAVE_DIRECTIONS else "")
                + note("La luz desde abajo (la &uacute;ltima) es la cl&aacute;sica luz inferior de terror. La luz de lado divide la cara en luz y sombra."))
        return card("LIGHT DIRECTION / SEE THE DIFFERENCE","Five Ways to Light a Face",
            para("Where you put the light changes everything. Here is the same face lit from five directions. Use it to choose your light position.")
            + (framed(DIRECTIONS,"A lighting reference: the same face lit from the front, 45 degrees, the side, behind, and below, each with a small diagram of the light position") if HAVE_DIRECTIONS else "")
            + note("Light from below (the last one) is the classic spooky underlight. Light from the side splits the face into light and shadow."))

    # ---------- OVERVIEW (shared, struct-aware) ----------
    def overview():
        if CONTACT:
            sub_en="Gather your horror-lighting inspiration, then capture three spooky portraits. You make the creative choices."
            sub_es="Re&uacute;ne tu inspiraci&oacute;n de iluminaci&oacute;n de terror, luego captura tres retratos de terror. T&uacute; tomas las decisiones creativas."
            first_en="<strong>gather your inspiration</strong>"; first_es="<strong>re&uacute;nes tu inspiraci&oacute;n</strong>"
            head_en="Find Your Look, Then Capture the Mood"; head_es="Encuentra Tu Look, Luego Captura el Ambiente"
            steps_en=[
                ("Step 02 &middot; Capture &amp; Contact Sheet:","gather your 5 to 8 inspiration images, then rotate roles and capture your three portraits in RAW. Share the files and build a contact sheet."),
                ("Step 03 &middot; Cull, Edit &amp; Deliver:","choose your best version of each portrait, edit it, and export your three JPGs."),
                ("Step 04 &middot; Reflection:","tell what inspired you, what you changed, and how your group worked."),
            ]
            steps_es=[
                ("Paso 02 &middot; Captura y Hoja de Contactos:","junta tus 5 a 8 im&aacute;genes de inspiraci&oacute;n, luego roten los roles y capturen sus tres retratos en RAW. Comparte los archivos y arma una hoja de contactos."),
                ("Paso 03 &middot; Selecciona, Edita y Entrega:","elige tu mejor versi&oacute;n de cada retrato, ed&iacute;tala y exporta tus tres JPG."),
                ("Paso 04 &middot; Reflexi&oacute;n:","cuenta qu&eacute; te inspir&oacute;, qu&eacute; cambiaste y c&oacute;mo trabaj&oacute; tu grupo."),
            ]
            note_en="Find your inspiration. Study the light. Then capture."; note_es="Busca tu inspiraci&oacute;n. Estudia la luz. Luego captura."
            upnext_en=("UP NEXT &middot; STEP 02 - Capture &amp; Contact Sheet","Gather your inspiration, capture your three portraits, and build a contact sheet.")
            upnext_es=("SIGUIENTE &middot; PASO 02 - Captura y Hoja de Contactos","Junta tu inspiraci&oacute;n, captura tus tres retratos y arma una hoja de contactos.")
        else:
            sub_en="Plan your lighting on paper, then capture three spooky portraits. You make the creative choices."
            sub_es="Planea tu iluminaci&oacute;n en papel, luego captura tres retratos de terror. T&uacute; tomas las decisiones creativas."
            first_en="<strong>plan on paper</strong>"; first_es="<strong>planeas en papel</strong>"
            head_en="Plan the Light, Then Capture the Mood"; head_es="Planea la Luz, Luego Captura el Ambiente"
            steps_en=[
                ("Step 02 &middot; Plan:","build a reference folder of 5 to 8 horror-lighting images, then draw your lighting plan on a journal page."),
                ("Step 03 &middot; Capture &amp; Deliver:","capture your three portraits in RAW, share the files, then cull, edit, and export your three JPGs."),
                ("Step 04 &middot; Reflection:","tell what you planned, what you changed, and how your group worked."),
            ]
            steps_es=[
                ("Paso 02 &middot; Planea:","arma una carpeta de referencia con 5 a 8 im&aacute;genes de iluminaci&oacute;n de terror, luego dibuja tu plan de iluminaci&oacute;n en una p&aacute;gina de tu diario."),
                ("Paso 03 &middot; Captura y Entrega:","captura tus tres retratos en RAW, comparte los archivos, luego selecciona, edita y exporta tus tres JPG."),
                ("Paso 04 &middot; Reflexi&oacute;n:","cuenta qu&eacute; planeaste, qu&eacute; cambiaste y c&oacute;mo trabaj&oacute; tu grupo."),
            ]
            note_en="Plan first. Sketch it. Call out color and height. Then capture."; note_es="Planea primero. Dib&uacute;jalo. Anota el color y la altura. Luego captura."
            upnext_en=("UP NEXT &middot; STEP 02 - Plan","Build your reference folder and draw your lighting-plan journal page.")
            upnext_es=("SIGUIENTE &middot; PASO 02 - Planea","Arma tu carpeta de referencia y dibuja la p&aacute;gina de tu plan de iluminaci&oacute;n.")

        en=banner("Module 11 &bull; Step 01","Spooky Portraits: Start Here", sub_en,"#espanol","Clic para Espa&ntilde;ol")
        en+=type_card("overview","Step 01 &middot; Overview &amp; Download", head_en,
            para("You will design three spooky portraits. First you " + first_en + ". Then you capture them in the studio with colored lights. You make the creative choices.")
            + para("You work in <strong>groups of three</strong> and take turns: one is the <strong>subject</strong>, one is the <strong>lighting assistant</strong>, and one is the <strong>camera operator</strong>. You switch roles so everyone plans, lights, and photographs.")
            + (framed(HEADER,"Spooky Portraits lighting-plan poster: the one-light and two-light setups and the three light-height choices") if HAVE_HEADER else ""))
        en+=standards_box(False, SPOOKY_STANDARDS)
        en+=project_downloads(False)
        en+=card("THE PROJECT / WHAT YOU MAKE","Three Portraits, Your Creative Control",
            para("Your look comes from horror movie lighting: where the light comes from, how high it is, and what color it is. Old or new, any style. You are not limited to the 1950s.")
            + (float_right(INSPO,"A horror-movie portrait: warm candlelight glowing up from below and a cool rim light behind","Horror lighting at work: a warm glow from below, a cool rim behind. Spooky.") if HAVE_INSPO else "")
            + bullets([
                ("Three portraits:","your group makes three, one for each rotation, so everyone operates the camera once."),
                ("Change one thing:","change at least one thing between portraits: light position, light height, or color."),
                ("You decide:","you choose the light setup, the color, and the mood, and you explain why."),
            ]))
        en+=card("YOUR LIGHTS / TWO SETUPS","One Light or Two",
            para("You use studio lights made by Aputure under the name <strong>Amaran</strong>. Each light can be a daylight white or any RGB color.")
            + bullets([
                ("One-light setup:","the Amaran 300C. Make a strong mood with just one light. Position and height matter most."),
                ("Two-light setup:","the Amaran 300C plus the Amaran 150C. Try a main light and an accent, or two contrasting colors."),
            ])
            + note("Light height sets the mood fast: eye level is flat, low and angled up is eerie, high and angled down is menacing."))
        if CONTACT:
            en+=direction_card(False)
            en+=cheat_sheet(False)
        en+=card("HOW IT WORKS / YOUR PLAN","Your Next Three Steps",
            para("You are on Step 01 now: read this page and download your project folder above. Here are the three steps that follow.")
            + bullets(steps_en) + note(note_en))
        en+=resources_card("Key Words",
            vocab_grid("On the Quiz",
              "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
              [("Underlighting","Light aimed up from below the face. Shadows fall upward: the classic monster look."),
               ("Split Lighting","Light from the side so one half of the face is lit and the other half is in shadow."),
               ("Rim Light","A light behind the subject that glows around the edges of the hair and shoulders."),
               ("Hard Light","A light that makes sharp, strong shadow edges and high contrast. Soft light is the opposite."),
               ("Low Key","A mostly dark photo with small areas of light. Moody and dramatic."),
               ("RGB","A light set to any color, not just white. Your Amaran lights can be any RGB color.")]))
        en+=next_up(*upnext_en)

        es=banner("M&oacute;dulo 11 &bull; Paso 01","Retratos de Terror: Empieza Aqu&iacute;", sub_es,"#top","Back to English")
        es+=type_card("overview","Paso 01 &middot; Resumen y Descarga", head_es,
            para("Vas a dise&ntilde;ar tres retratos de terror. Primero " + first_es + ". Luego los capturas en el estudio con luces de colores. T&uacute; tomas las decisiones creativas.")
            + para("Trabajas en <strong>grupos de tres</strong> y se turnan: uno es el <strong>sujeto</strong>, uno es el <strong>asistente de iluminaci&oacute;n</strong> y uno es el <strong>operador de c&aacute;mara</strong>. Cambian de rol para que todos planeen, iluminen y fotograf&iacute;en.")
            + (framed(HEADER,"P&oacute;ster de iluminaci&oacute;n de Retratos de Terror: los montajes de una y dos luces y las tres alturas de luz") if HAVE_HEADER else ""))
        es+=standards_box(True, SPOOKY_STANDARDS)
        es+=project_downloads(True)
        es+=card("EL PROYECTO / QU&Eacute; HACES","Tres Retratos, Tu Control Creativo",
            para("Tu look viene de la iluminaci&oacute;n de pel&iacute;culas de terror: de d&oacute;nde viene la luz, qu&eacute; tan alta est&aacute; y de qu&eacute; color es. Vieja o nueva, cualquier estilo. No te limitas a los a&ntilde;os 50.")
            + (float_right(INSPO,"Un retrato de pel&iacute;cula de terror: luz c&aacute;lida de vela brillando desde abajo y una luz fr&iacute;a de contorno por detr&aacute;s","Iluminaci&oacute;n de terror en acci&oacute;n: un brillo c&aacute;lido desde abajo y una luz fr&iacute;a por detr&aacute;s. Espeluznante.") if HAVE_INSPO else "")
            + bullets([
                ("Tres retratos:","tu grupo hace tres, uno por cada rotaci&oacute;n, para que cada quien opere la c&aacute;mara una vez."),
                ("Cambia una cosa:","cambia al menos una cosa entre retratos: posici&oacute;n de la luz, altura de la luz o color."),
                ("T&uacute; decides:","eliges el montaje de luz, el color y el ambiente, y explicas por qu&eacute;."),
            ]))
        es+=card("TUS LUCES / DOS MONTAJES","Una Luz o Dos",
            para("Usas luces de estudio hechas por Aputure con el nombre <strong>Amaran</strong>. Cada luz puede ser blanca (luz de d&iacute;a) o cualquier color RGB.")
            + bullets([
                ("Montaje de una luz:","la Amaran 300C. Crea un ambiente fuerte con una sola luz. La posici&oacute;n y la altura importan m&aacute;s."),
                ("Montaje de dos luces:","la Amaran 300C m&aacute;s la Amaran 150C. Prueba una luz principal y un acento, o dos colores que contrasten."),
            ])
            + note("La altura de la luz marca el ambiente r&aacute;pido: a la altura de los ojos es plana, baja apuntando arriba es espeluznante, alta apuntando abajo es amenazante."))
        if CONTACT:
            es+=direction_card(True)
            es+=cheat_sheet(True)
        es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Siguientes Tres Pasos",
            para("Est&aacute;s en el Paso 01: lee esta p&aacute;gina y descarga tu carpeta del proyecto arriba. Estos son los tres pasos que siguen.")
            + bullets(steps_es) + note(note_es))
        es+=resources_card("Palabras Clave",
            vocab_grid("En el Examen",
              "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
              [("Underlighting (Luz Inferior)","Luz apuntada hacia arriba desde abajo de la cara. Las sombras suben: el look cl&aacute;sico de monstruo."),
               ("Split Lighting (Luz Dividida)","Luz de un lado para que la mitad de la cara quede iluminada y la otra mitad en sombra."),
               ("Rim Light (Luz de Contorno)","Una luz detr&aacute;s del sujeto que brilla alrededor del pelo y los hombros."),
               ("Hard Light (Luz Dura)","Una luz que hace sombras con bordes marcados y mucho contraste. La luz suave es lo contrario."),
               ("Low Key (Clave Baja)","Una foto casi oscura con peque&ntilde;as zonas de luz. Con ambiente y drama."),
               ("RGB","Una luz puesta en cualquier color, no solo blanco. Tus luces Amaran pueden ser cualquier color RGB.")]), True)
        es+=next_up(*upnext_es)

        stepnav=f'<a href="{S1}" class="silva-step-btn">Step 02 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Next: Step 02 &#8594;</a></div>'
        return wrap_page(f"Spooky Portraits | {CT} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

    # ========================= PLAN STRUCT (Photo 2, advanced) =========================
    def plan():
        en=banner("Module 11 &bull; Step 02","Plan Your Lighting",
            "Build a reference folder, then draw your lighting plan on a journal page.","#espanol","Clic para Espa&ntilde;ol")
        en+=card("PLAN BEFORE YOU LIGHT","Good Lighting Starts on Paper",
            para("Great spooky portraits are planned, not lucky. First you gather ideas in a reference folder. Then you draw a lighting plan so your group can set up fast and repeat it.")
            + (float_right(PLAN_FLOAT,"An example Spooky Portraits top-view lighting diagram on a photo journal page") if HAVE_PLAN_FLOAT else ""))
        en+=deliverables_box(False,
            [("Reference folder:","1 screen capture of your Reference_Images folder, showing your 5 to 8 inspiration images."),
             ("Lighting plan photo:","1 photo of your lighting-plan journal page (the top-view diagram with your call-outs).")])
        en+=card("STEP A / REFERENCE FOLDER","Gather 5 to 8 Inspiration Images",
            para("Search for <strong>horror movie lighting</strong> you like. Old or new, any style. Your project folder already has a <strong>Reference_Images</strong> folder waiting for them.")
            + bullets([
                ("Save 5 to 8 images:","save them into your <strong>Reference_Images</strong> folder. Pick images that show where the light comes from, what color it is, and how it feels."),
                ("For each one, be ready to say:","where is the light, what color is it, and what mood does it make?"),
            ])
            + note("These images are for your private study. Do not repost them or turn them in as your own work. You turn in a screen capture of your folder, not the images.")
            + note("Take a screen capture of your Reference_Images folder showing your 5 to 8 images and upload it here."))
        en+=card("STEP B / LIGHTING PLAN","Draw Your Journal Page",
            para("On one page of your photo journal, draw a <strong>top view</strong>, like looking straight down from the ceiling.")
            + steps([
                ("Draw the diagram:","show the backdrop, where the subject stands, where the camera is, and where each light goes."),
                ("Label each light:","which light it is (300C or 150C) and how far from the subject."),
                ("Call out color:","write the color of every light (daylight or an RGB color)."),
                ("Call out height:","write the height of every light (eye level, low angled up, or high angled down)."),
                ("Write the mood:","one sentence on why this setup creates the mood you want."),
                ("Name the image:","name the inspiration image from your folder that guided you."),
            ])
            + note("There is no scanner on campus. Take a photo of your finished journal page with your student iPad and upload it here."))
        en+=direction_card(False)
        en+=cheat_sheet(False)
        en+=next_up("UP NEXT &middot; STEP 03 - Capture &amp; Deliver","Rotate roles, capture your three portraits, then cull, edit, and export your JPGs.")

        es=banner("M&oacute;dulo 11 &bull; Paso 02","Planea Tu Iluminaci&oacute;n",
            "Arma una carpeta de referencia, luego dibuja tu plan de iluminaci&oacute;n en una p&aacute;gina de tu diario.","#top","Back to English")
        es+=card("PLANEA ANTES DE ILUMINAR","La Buena Luz Empieza en Papel",
            para("Los buenos retratos de terror se planean, no son suerte. Primero juntas ideas en una carpeta de referencia. Luego dibujas un plan de iluminaci&oacute;n para que tu grupo monte r&aacute;pido y lo pueda repetir.")
            + (float_right(PLAN_FLOAT,"Un diagrama de iluminaci&oacute;n de vista superior de ejemplo de Retratos de Terror en una p&aacute;gina del diario de fotograf&iacute;a") if HAVE_PLAN_FLOAT else ""))
        es+=deliverables_box(True,
            [("Carpeta de referencia:","1 captura de pantalla de tu carpeta Reference_Images, mostrando tus 5 a 8 im&aacute;genes de inspiraci&oacute;n."),
             ("Foto del plan de iluminaci&oacute;n:","1 foto de la p&aacute;gina de tu plan de iluminaci&oacute;n (el diagrama de vista superior con tus anotaciones).")])
        es+=card("PARTE A / CARPETA DE REFERENCIA","Junta 5 a 8 Im&aacute;genes de Inspiraci&oacute;n",
            para("Busca <strong>iluminaci&oacute;n de pel&iacute;culas de terror</strong> que te guste. Vieja o nueva, cualquier estilo. Tu carpeta del proyecto ya tiene una carpeta <strong>Reference_Images</strong> lista para ellas.")
            + bullets([
                ("Guarda 5 a 8 im&aacute;genes:","gu&aacute;rdalas en tu carpeta <strong>Reference_Images</strong>. Elige im&aacute;genes que muestren de d&oacute;nde viene la luz, de qu&eacute; color es y c&oacute;mo se siente."),
                ("De cada una, prep&aacute;rate para decir:","&iquest;d&oacute;nde est&aacute; la luz, de qu&eacute; color es y qu&eacute; ambiente crea?"),
            ])
            + note("Estas im&aacute;genes son para tu estudio privado. No las vuelvas a publicar ni las entregues como tu propio trabajo. Entregas una captura de pantalla de tu carpeta, no las im&aacute;genes.")
            + note("Toma una captura de pantalla de tu carpeta Reference_Images mostrando tus 5 a 8 im&aacute;genes y s&uacute;bela aqu&iacute;."))
        es+=card("PARTE B / PLAN DE ILUMINACI&Oacute;N","Dibuja la P&aacute;gina de Tu Diario",
            para("En una p&aacute;gina de tu diario de fotograf&iacute;a, dibuja una <strong>vista superior</strong>, como si miraras hacia abajo desde el techo.")
            + steps([
                ("Dibuja el diagrama:","muestra el fondo, d&oacute;nde se para el sujeto, d&oacute;nde est&aacute; la c&aacute;mara y d&oacute;nde va cada luz."),
                ("Etiqueta cada luz:","cu&aacute;l luz es (300C o 150C) y a qu&eacute; distancia del sujeto."),
                ("Anota el color:","escribe el color de cada luz (luz de d&iacute;a o un color RGB)."),
                ("Anota la altura:","escribe la altura de cada luz (a la altura de los ojos, baja apuntando arriba, o alta apuntando abajo)."),
                ("Escribe el ambiente:","una oraci&oacute;n sobre por qu&eacute; este montaje crea el ambiente que buscas."),
                ("Nombra la imagen:","nombra la imagen de inspiraci&oacute;n de tu carpeta que te gui&oacute;."),
            ])
            + note("No hay esc&aacute;ner en la escuela. Toma una foto de tu p&aacute;gina del diario terminada con tu iPad de estudiante y s&uacute;bela aqu&iacute;."))
        es+=direction_card(True)
        es+=cheat_sheet(True)
        es+=next_up("SIGUIENTE &middot; PASO 03 - Captura y Entrega","Roten los roles, capturen sus tres retratos, luego selecciona, edita y exporta tus JPG.")

        stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S2}" class="silva-step-btn">Step 03 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S2}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
        return wrap_page(f"Step 2: Plan Your Lighting | Spooky Portraits | {CT} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

    def capture_deliver():
        en=banner("Module 11 &bull; Step 03","Capture &amp; Deliver",
            "Rotate roles, capture your three portraits, then cull, edit, and export your JPGs.","#espanol","Clic para Espa&ntilde;ol")
        en+=card("IN THE STUDIO / TAKE TURNS","Rotate and Capture Three Portraits",
            para("Set up your lights from your journal plan. Your group of three rotates roles: <strong>subject</strong>, <strong>lighting assistant</strong>, and <strong>camera operator</strong>. After each portrait, switch roles, so everyone operates the camera once and your group makes three portraits.")
            + (float_right(CAP_FLOAT,"An example spooky portrait lit from below, the classic underlighting look","Underlighting: the light comes from below, so the shadows climb upward for an eerie look.") if HAVE_CAP_FLOAT else "")
            + bullets([
                ("Three portraits:","one per rotation. Each one is a new look."),
                ("Change one thing:","change at least one thing between portraits: light position, light height, or color."),
                ("Follow your plan:","build each setup from your journal diagram so it is easy to repeat."),
            ]))
        en+=deliverables_box(False,
            [("Portrait 1, edited JPG:","your best edited version of your first portrait, exported at full resolution."),
             ("Portrait 2, edited JPG:","your best edited version of your second portrait, exported at full resolution."),
             ("Portrait 3, edited JPG:","your best edited version of your third portrait, exported at full resolution.")])
        en+=spooky_settings(False)
        en+=safety_card(False)
        en+=card("CAPTURE / ONE PORTRAIT AT A TIME","Your Workflow for Each Portrait",
            steps([
                ("Look at your plan:","check your journal page and your inspiration image."),
                ("Set up the lights:","place the lights, set the colors, and set the heights from your diagram."),
                ("Take a test frame:","check the mood, the sharpness, and the exposure. Fix the white balance if the color is off."),
                ("Change one thing:","for the next portrait, change the light position, height, or color, and note it in your journal."),
                ("Capture and confirm:","make sure the eyes are sharp before you move on."),
            ])
            + note("Capture in RAW so you have room to protect the colors you planned when you edit."))
        en+=card("SHARE &amp; EDIT / DELIVER YOUR THREE","Share, Cull, Edit, and Export",
            para("One person operates the camera for each portrait, but all three of you edit and turn in your own work. So everyone needs the files.")
            + steps([
                ("Share the files:","share the memory card, or put the RAW files in a shared OneDrive folder, so all three group members get the three portraits."),
                ("Import to Lightroom:","move the RAW files into your RAW_Images folder and import them into Lightroom Classic."),
                ("Cull your best:","choose your best version of each of the three portraits."),
                ("Edit in Lightroom:","protect the colors you planned, fix the exposure, and keep the eyes sharp."),
                ("Export 3 JPGs:","go to File &rsaquo; Export and export your three portraits as full-resolution JPGs, then upload them here."),
            ]))
        en+=next_up("UP NEXT &middot; STEP 04 - Reflection","Tell what you planned, what you changed between portraits, and how your group worked.")

        es=banner("M&oacute;dulo 11 &bull; Paso 03","Captura y Entrega",
            "Roten los roles, capturen sus tres retratos, luego selecciona, edita y exporta tus JPG.","#top","Back to English")
        es+=card("EN EL ESTUDIO / TOMEN TURNOS","Roten y Capturen Tres Retratos",
            para("Monten sus luces desde el plan de tu diario. Tu grupo de tres rota los roles: <strong>sujeto</strong>, <strong>asistente de iluminaci&oacute;n</strong> y <strong>operador de c&aacute;mara</strong>. Despu&eacute;s de cada retrato, cambien de rol, para que cada quien opere la c&aacute;mara una vez y tu grupo haga tres retratos.")
            + (float_right(CAP_FLOAT,"Un retrato de terror de ejemplo iluminado desde abajo, el look cl&aacute;sico de luz inferior","Luz inferior: la luz viene desde abajo, as&iacute; que las sombras suben para un look espeluznante.") if HAVE_CAP_FLOAT else "")
            + bullets([
                ("Tres retratos:","uno por rotaci&oacute;n. Cada uno es un look nuevo."),
                ("Cambia una cosa:","cambia al menos una cosa entre retratos: posici&oacute;n de la luz, altura de la luz o color."),
                ("Sigue tu plan:","arma cada montaje desde el diagrama de tu diario para que sea f&aacute;cil de repetir."),
            ]))
        es+=deliverables_box(True,
            [("Retrato 1, JPG editado:","tu mejor versi&oacute;n editada de tu primer retrato, exportada a resoluci&oacute;n completa."),
             ("Retrato 2, JPG editado:","tu mejor versi&oacute;n editada de tu segundo retrato, exportada a resoluci&oacute;n completa."),
             ("Retrato 3, JPG editado:","tu mejor versi&oacute;n editada de tu tercer retrato, exportada a resoluci&oacute;n completa.")])
        es+=spooky_settings(True)
        es+=safety_card(True)
        es+=card("CAPTURA / UN RETRATO A LA VEZ","Tu Flujo para Cada Retrato",
            steps([
                ("Mira tu plan:","revisa la p&aacute;gina de tu diario y tu imagen de inspiraci&oacute;n."),
                ("Monta las luces:","coloca las luces, pon los colores y las alturas desde tu diagrama."),
                ("Toma una prueba:","revisa el ambiente, la nitidez y la exposici&oacute;n. Corrige el balance de blancos si el color no se ve bien."),
                ("Cambia una cosa:","para el siguiente retrato, cambia la posici&oacute;n, la altura o el color de la luz, y an&oacute;talo en tu diario."),
                ("Captura y confirma:","aseg&uacute;rate de que los ojos est&eacute;n n&iacute;tidos antes de seguir."),
            ])
            + note("Captura en RAW para tener espacio para proteger los colores que planeaste cuando edites."))
        es+=card("COMPARTE Y EDITA / ENTREGA TUS TRES","Comparte, Selecciona, Edita y Exporta",
            para("Una persona opera la c&aacute;mara en cada retrato, pero los tres editan y entregan su propio trabajo. As&iacute; que todos necesitan los archivos.")
            + steps([
                ("Comparte los archivos:","comparte la tarjeta de memoria, o pon los archivos RAW en una carpeta compartida de OneDrive, para que los tres del grupo tengan los tres retratos."),
                ("Importa a Lightroom:","mueve los archivos RAW a tu carpeta RAW_Images e imp&oacute;rtalos a Lightroom Classic."),
                ("Selecciona tus mejores:","elige tu mejor versi&oacute;n de cada uno de los tres retratos."),
                ("Edita en Lightroom:","protege los colores que planeaste, corrige la exposici&oacute;n y mant&eacute;n los ojos n&iacute;tidos."),
                ("Exporta 3 JPG:","ve a File &rsaquo; Export y exporta tus tres retratos como JPG a resoluci&oacute;n completa, luego s&uacute;belos aqu&iacute;."),
            ]))
        es+=next_up("SIGUIENTE &middot; PASO 04 - Reflexi&oacute;n","Cuenta qu&eacute; planeaste, qu&eacute; cambiaste entre retratos y c&oacute;mo trabaj&oacute; tu grupo.")

        stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S3}" class="silva-step-btn">Step 04 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S3}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
        return wrap_page(f"Step 3: Capture and Deliver | Spooky Portraits | {CT} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

    # ========================= CONTACT STRUCT (Photo 1, 1st-year) =========================
    def capture_contact():
        en=banner("Module 11 &bull; Step 02","Capture &amp; Contact Sheet",
            "Gather your inspiration, capture your three portraits, and build a contact sheet.","#espanol","Clic para Espa&ntilde;ol")
        en+=card("FIND YOUR INSPIRATION","Start with 5 to 8 Horror-Lighting Images",
            para("Good spooky portraits start with good ideas. Before you light anyone, gather a folder of horror-lighting images you want your look to feel like. Your project folder already has a <strong>Reference_Images</strong> folder waiting for them.")
            + bullets([
                ("Save 5 to 8 images:","search horror movie lighting, old or new, any style. Pick images that show where the light is, what color it is, and how it feels, and save them into your <strong>Reference_Images</strong> folder."),
                ("Be ready to say:","for each image, where is the light, what color is it, and what mood does it make?"),
                ("Turn it in:","take a screen capture of your <strong>Reference_Images</strong> folder showing your 5 to 8 images, and upload it here."),
            ])
            + note("These images are for your private study. Do not repost them or turn them in as your own work. You turn in a screen capture of your folder, not the images."))
        en+=deliverables_box(False,
            [("Reference folder:","1 screen capture of your Reference_Images folder, showing your 5 to 8 inspiration images."),
             ("Contact sheet:","1 contact sheet of your three portraits, built in Lightroom and turned in as a high-resolution JPG.")])
        en+=spooky_settings(False)
        en+=safety_card(False)
        en+=card("CAPTURE / THREE PORTRAITS","Rotate Roles and Make Three Looks",
            para("Set up your lights for the look you want. Your group of three rotates roles: <strong>subject</strong>, <strong>lighting assistant</strong>, and <strong>camera operator</strong>. After each portrait, switch roles, so everyone operates the camera once.")
            + (float_right(CAP_FLOAT,"An example spooky portrait lit from below, the classic underlighting look","Underlighting: the light comes from below, so the shadows climb upward for an eerie look.") if HAVE_CAP_FLOAT else "")
            + steps([
                ("Look at your inspiration:","check your reference images and the look you want."),
                ("Set up the lights:","place the lights, set the colors, and set the heights."),
                ("Take a test frame:","check the mood, the sharpness, and the exposure. Fix the white balance if the color is off."),
                ("Change one thing:","for the next portrait, change the light position, height, or color."),
                ("Capture and confirm:","make sure the eyes are sharp before you move on."),
            ])
            + note("Three portraits in all, one per rotation. Change at least one thing between each: light position, height, or color."))
        en+=card("SHARE &amp; CONTACT SHEET","Share the Files, Then Build Your Contact Sheet",
            para("One person operates the camera for each portrait, but all three of you edit and turn in your own work. So everyone needs the files.")
            + steps([
                ("Share the files:","share the memory card, or put the RAW files in a shared OneDrive folder, so all three group members get the three portraits."),
                ("Import to Lightroom:","move the RAW files into your RAW_Images folder and import them into Lightroom Classic."),
                ("Build the contact sheet:","in the Print module, use the contact-sheet template with your three portraits loaded."),
                ("Print to JPG:","use Print to File so it saves as a high-resolution JPG, then upload it here."),
            ])
            + note("Contact sheets are always turned in as a high-resolution JPG."))
        en+=next_up("UP NEXT &middot; STEP 03 - Cull, Edit &amp; Deliver","Choose your best version of each portrait, edit it, and export your three JPGs.")

        es=banner("M&oacute;dulo 11 &bull; Paso 02","Captura y Hoja de Contactos",
            "Junta tu inspiraci&oacute;n, captura tus tres retratos y arma una hoja de contactos.","#top","Back to English")
        es+=card("ENCUENTRA TU INSPIRACI&Oacute;N","Empieza con 5 a 8 Im&aacute;genes de Iluminaci&oacute;n de Terror",
            para("Los buenos retratos de terror empiezan con buenas ideas. Antes de iluminar a nadie, junta una carpeta de im&aacute;genes de iluminaci&oacute;n de terror con el look que quieres lograr. Tu carpeta del proyecto ya tiene una carpeta <strong>Reference_Images</strong> lista para ellas.")
            + bullets([
                ("Guarda 5 a 8 im&aacute;genes:","busca iluminaci&oacute;n de pel&iacute;culas de terror, vieja o nueva, cualquier estilo. Elige im&aacute;genes que muestren d&oacute;nde est&aacute; la luz, de qu&eacute; color es y c&oacute;mo se siente, y gu&aacute;rdalas en tu carpeta <strong>Reference_Images</strong>."),
                ("Prep&aacute;rate para decir:","de cada imagen, &iquest;d&oacute;nde est&aacute; la luz, de qu&eacute; color es y qu&eacute; ambiente crea?"),
                ("Entr&eacute;gala:","toma una captura de pantalla de tu carpeta <strong>Reference_Images</strong> mostrando tus 5 a 8 im&aacute;genes, y s&uacute;bela aqu&iacute;."),
            ])
            + note("Estas im&aacute;genes son para tu estudio privado. No las vuelvas a publicar ni las entregues como tu propio trabajo. Entregas una captura de pantalla de tu carpeta, no las im&aacute;genes."))
        es+=deliverables_box(True,
            [("Carpeta de referencia:","1 captura de pantalla de tu carpeta Reference_Images, mostrando tus 5 a 8 im&aacute;genes de inspiraci&oacute;n."),
             ("Hoja de contactos:","1 hoja de contactos de tus tres retratos, armada en Lightroom y entregada como un JPG de alta resoluci&oacute;n.")])
        es+=spooky_settings(True)
        es+=safety_card(True)
        es+=card("CAPTURA / TRES RETRATOS","Roten los Roles y Hagan Tres Looks",
            para("Monten sus luces para el look que quieren. Tu grupo de tres rota los roles: <strong>sujeto</strong>, <strong>asistente de iluminaci&oacute;n</strong> y <strong>operador de c&aacute;mara</strong>. Despu&eacute;s de cada retrato, cambien de rol, para que cada quien opere la c&aacute;mara una vez.")
            + (float_right(CAP_FLOAT,"Un retrato de terror de ejemplo iluminado desde abajo, el look cl&aacute;sico de luz inferior","Luz inferior: la luz viene desde abajo, as&iacute; que las sombras suben para un look espeluznante.") if HAVE_CAP_FLOAT else "")
            + steps([
                ("Mira tu inspiraci&oacute;n:","revisa tus im&aacute;genes de referencia y el look que quieres."),
                ("Monta las luces:","coloca las luces, pon los colores y las alturas."),
                ("Toma una prueba:","revisa el ambiente, la nitidez y la exposici&oacute;n. Corrige el balance de blancos si el color no se ve bien."),
                ("Cambia una cosa:","para el siguiente retrato, cambia la posici&oacute;n, la altura o el color de la luz."),
                ("Captura y confirma:","aseg&uacute;rate de que los ojos est&eacute;n n&iacute;tidos antes de seguir."),
            ])
            + note("Tres retratos en total, uno por rotaci&oacute;n. Cambia al menos una cosa entre cada uno: posici&oacute;n, altura o color de la luz."))
        es+=card("COMPARTE Y HOJA DE CONTACTOS","Comparte los Archivos, Luego Arma Tu Hoja de Contactos",
            para("Una persona opera la c&aacute;mara en cada retrato, pero los tres editan y entregan su propio trabajo. As&iacute; que todos necesitan los archivos.")
            + steps([
                ("Comparte los archivos:","comparte la tarjeta de memoria, o pon los archivos RAW en una carpeta compartida de OneDrive, para que los tres del grupo tengan los tres retratos."),
                ("Importa a Lightroom:","mueve los archivos RAW a tu carpeta RAW_Images e imp&oacute;rtalos a Lightroom Classic."),
                ("Arma la hoja de contactos:","en el m&oacute;dulo Print, usa la plantilla de hoja de contactos con tus tres retratos cargados."),
                ("Imprime a JPG:","usa Print to File para que se guarde como un JPG de alta resoluci&oacute;n, luego s&uacute;belo aqu&iacute;."),
            ])
            + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n."))
        es+=next_up("SIGUIENTE &middot; PASO 03 - Selecciona, Edita y Entrega","Elige tu mejor versi&oacute;n de cada retrato, ed&iacute;tala y exporta tus tres JPG.")

        stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S2}" class="silva-step-btn">Step 03 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S2}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
        return wrap_page(f"Step 2: Capture and Contact Sheet | Spooky Portraits | {CT} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

    def cull_deliver():
        en=banner("Module 11 &bull; Step 03","Cull, Edit &amp; Deliver",
            "Choose your best version of each portrait, edit it, and export your three JPGs.","#espanol","Clic para Espa&ntilde;ol")
        en+=card("CULL / CHOOSE YOUR BEST","Pick the Best of Each Portrait",
            para("Open your take in Lightroom Classic and go portrait by portrait. For each of your three portraits, choose your single best version.")
            + bullets([
                ("Sharp eyes:","keep the frames where the eyes are in focus. Skip any that are soft."),
                ("The right mood:","keep the version where the light and color feel the way you wanted."),
                ("No blinks:","make sure your keeper has open eyes and a natural look."),
            ])
            + note("Call these your selections, not &ldquo;picks.&rdquo; You end with three: your best version of each portrait."))
        en+=deliverables_box(False,
            [("Portrait 1, edited JPG:","your best edited version of your first portrait, exported at full resolution."),
             ("Portrait 2, edited JPG:","your best edited version of your second portrait, exported at full resolution."),
             ("Portrait 3, edited JPG:","your best edited version of your third portrait, exported at full resolution.")])
        en+=card("EDIT / PROTECT YOUR COLORS","Make Each Portrait Its Best",
            para("These are RAW files, so you have room to edit. Bring out the mood you planned.")
            + steps([
                ("Fix the white balance:","your colored lights should read the way you set them. Fix the white balance so the color is true."),
                ("Set the exposure:","keep the face bright enough to read, but protect the dark, moody shadows."),
                ("Keep the eyes sharp:","the eyes are the heart of a portrait. Make sure they stay sharp and clear."),
                ("Light retouch only:","small, natural cleanups are fine. Do not over-smooth the skin."),
            ])
            + note("Edit on the Mac in Lightroom Classic."))
        en+=card("DELIVER / NAME AND UPLOAD","Export Your Three JPGs",
            steps([
                ("Export full-resolution JPGs:","go to File &rsaquo; Export and export your three edited portraits as full-resolution JPGs into your project folder."),
                ("Name each file:","use your last name and first name plus the portrait number, like <strong>Lee_Mia_Portrait1.jpg</strong>."),
                ("Upload here:","turn in your three edited JPGs to this Canvas assignment."),
            ]))
        en+=next_up("UP NEXT &middot; STEP 04 - Reflection","Tell what inspired you, what you changed between portraits, and how your group worked.")

        es=banner("M&oacute;dulo 11 &bull; Paso 03","Selecciona, Edita y Entrega",
            "Elige tu mejor versi&oacute;n de cada retrato, ed&iacute;tala y exporta tus tres JPG.","#top","Back to English")
        es+=card("SELECCIONA / ELIGE LAS MEJORES","Elige la Mejor de Cada Retrato",
            para("Abre tu trabajo en Lightroom Classic y ve retrato por retrato. Para cada uno de tus tres retratos, elige tu mejor versi&oacute;n.")
            + bullets([
                ("Ojos n&iacute;tidos:","guarda las im&aacute;genes donde los ojos est&aacute;n enfocados. Descarta las borrosas."),
                ("El ambiente correcto:","guarda la versi&oacute;n donde la luz y el color se sienten como los quer&iacute;as."),
                ("Sin parpadeos:","aseg&uacute;rate de que tu imagen tenga los ojos abiertos y se vea natural."),
            ])
            + note("Llama a estas tus selecciones. Terminas con tres: tu mejor versi&oacute;n de cada retrato."))
        es+=deliverables_box(True,
            [("Retrato 1, JPG editado:","tu mejor versi&oacute;n editada de tu primer retrato, exportada a resoluci&oacute;n completa."),
             ("Retrato 2, JPG editado:","tu mejor versi&oacute;n editada de tu segundo retrato, exportada a resoluci&oacute;n completa."),
             ("Retrato 3, JPG editado:","tu mejor versi&oacute;n editada de tu tercer retrato, exportada a resoluci&oacute;n completa.")])
        es+=card("EDITA / PROTEGE TUS COLORES","Haz Que Cada Retrato Sea el Mejor",
            para("Estos son archivos RAW, as&iacute; que tienes espacio para editar. Resalta el ambiente que planeaste.")
            + steps([
                ("Corrige el balance de blancos:","tus luces de color deben verse como las pusiste. Corrige el balance de blancos para que el color sea real."),
                ("Ajusta la exposici&oacute;n:","mant&eacute;n la cara lo bastante clara para verse, pero protege las sombras oscuras y con ambiente."),
                ("Mant&eacute;n los ojos n&iacute;tidos:","los ojos son el coraz&oacute;n de un retrato. Aseg&uacute;rate de que queden n&iacute;tidos y claros."),
                ("Retoque ligero:","peque&ntilde;os arreglos naturales est&aacute;n bien. No suavices mucho la piel."),
            ])
            + note("Edita en la Mac en Lightroom Classic."))
        es+=card("ENTREGA / NOMBRA Y SUBE","Exporta Tus Tres JPG",
            steps([
                ("Exporta JPG a resoluci&oacute;n completa:","ve a File &rsaquo; Export y exporta tus tres retratos editados como JPG a resoluci&oacute;n completa a la carpeta de tu proyecto."),
                ("Nombra cada archivo:","usa tu apellido y tu nombre m&aacute;s el n&uacute;mero del retrato, como <strong>Lee_Mia_Portrait1.jpg</strong>."),
                ("Sube aqu&iacute;:","entrega tus tres JPG editados a esta tarea de Canvas."),
            ]))
        es+=next_up("SIGUIENTE &middot; PASO 04 - Reflexi&oacute;n","Cuenta qu&eacute; te inspir&oacute;, qu&eacute; cambiaste entre retratos y c&oacute;mo trabaj&oacute; tu grupo.")

        stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S3}" class="silva-step-btn">Step 04 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S3}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
        return wrap_page(f"Step 3: Cull, Edit and Deliver | Spooky Portraits | {CT} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

    # ---------- STEP 04: REFLECTION (shared) ----------
    def reflection():
        lp_en = "lighting" if CONTACT else "lighting plan"
        lp_es = "iluminaci&oacute;n" if CONTACT else "plan de iluminaci&oacute;n"
        en=banner("Module 11 &bull; Step 04","Reflection",
            "Tell what inspired you, what you changed, and how your group worked.","#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
        en+=card("STEP 04 / REFLECT","Complete and Upload the Reflection",
            para(f"Finish with a short reflection about your {lp_en}, your three portraits, and your group.")
            + note("The reflection document is inside the project folder you downloaded on Step 01, the Overview. Open the <strong>Spooky_Portraits</strong> folder and find <strong>Spooky-Portraits-Reflection</strong> (English or Spanish). Type right in the document.")
            + bullets([
                ("Your inspiration:","what horror lighting look inspired you, and what did you like about it?"),
                ("Your lighting:","where was each light, what color, and what height, and why did that set the mood?"),
                ("What you changed:","what did you change between your three portraits, and how did it change the mood?"),
                ("Your group:","what role did each person play, and how did your group work together?"),
            ])
            + note("Answer honestly, in your own words, in full sentences."))
        en+=deliverables_box(False,
            [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
        en+=next_up("MODULE COMPLETE","Great work. You planned your light, made three moods, and controlled color like a real set photographer.")

        es=banner("M&oacute;dulo 11 &bull; Paso 04","Reflexi&oacute;n",
            "Cuenta qu&eacute; te inspir&oacute;, qu&eacute; cambiaste y c&oacute;mo trabaj&oacute; tu grupo.","#top","Back to English", HICON_REFLECT)
        es+=card("PASO 04 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
            para(f"Termina con una reflexi&oacute;n corta sobre tu {lp_es}, tus tres retratos y tu grupo.")
            + note("El documento de reflexi&oacute;n est&aacute; dentro de la carpeta del proyecto que descargaste en el Paso 01, el Resumen. Abre la carpeta <strong>Spooky_Portraits</strong> y busca <strong>Spooky-Portraits-Reflection</strong> (en ingl&eacute;s o en espa&ntilde;ol). Escribe directamente en el documento.")
            + bullets([
                ("Tu inspiraci&oacute;n:","&iquest;qu&eacute; estilo de iluminaci&oacute;n de terror te inspir&oacute;, y qu&eacute; te gust&oacute; de &eacute;l?"),
                ("Tu iluminaci&oacute;n:","&iquest;d&oacute;nde estaba cada luz, de qu&eacute; color y a qu&eacute; altura, y por qu&eacute; cre&oacute; el ambiente?"),
                ("Qu&eacute; cambiaste:","&iquest;qu&eacute; cambiaste entre tus tres retratos, y c&oacute;mo cambi&oacute; el ambiente?"),
                ("Tu grupo:","&iquest;qu&eacute; rol tuvo cada persona, y c&oacute;mo trabajaron juntos?"),
            ])
            + note("Contesta con honestidad, en tus propias palabras, en oraciones completas."))
        es+=deliverables_box(True,
            [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completado, subido a esta tarea de Canvas.")])
        es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Planeaste tu luz, creaste tres ambientes y controlaste el color como un fot&oacute;grafo de set de verdad.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 03</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 03</a><span></span></div>'
        return wrap_page(f"Step 4: Reflection | Spooky Portraits | {CT} | PVHS", nav("Step 04",dots_for(3),stepnav), top_wrap(en,es), bottom)

    mid = [(S1,capture_contact),(S2,cull_deliver)] if CONTACT else [(S1,plan),(S2,capture_deliver)]
    return [(OVER,overview)] + mid + [(S3,reflection)]

# ================= BUILD =================
for c in COURSES:
    for fname,gen in build_course(c):
        html=ent(gen())
        assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
        assert "–" not in html and "&ndash;" not in html, "en dash in "+fname
        ban_check(html, fname)
        open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
        print("wrote", fname, len(html), "bytes")
