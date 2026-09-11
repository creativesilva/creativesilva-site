#!/usr/bin/env python3
# Photography 2A - Module: Off-Camera Flash (OCF).
# A whole-class photo walk with the school camera kit: light an outdoor portrait with off-camera
# flash, build a contact sheet, edit 3, reflect. Rebuilt from the OLD hand-authored framework
# (eyebrow chips + <!--IDEYE--> right-side ID icon + orange language toggle + table vocab) onto the
# chip-header framework via silva_framework, re-chroming only. Every student sentence (EN + ES) is
# preserved verbatim from the legacy pages. Overview + 3 steps, bilingual, 5th-grade.
# Camera-kit capture (no personal camera roll to mine) so NO own-device fresh-photos note.
import os
from silva_framework import *
import silva_framework as _sf

def banner(label,title,subtitle,es_href,es_label):
    # OCF capture happens on a whole-class photo walk: crown every page with the white photo-walk icon.
    return _sf.banner(label,title,subtitle,es_href,es_label,HICON_PHOTO_WALK)

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/photo2/ocf"
HEADER=f"{IMG}/ocf-header-v4.png"
S1_FLOAT=f"{IMG}/ocf-step01-float.png"
S2_FLOAT=f"{IMG}/ocf-step02-float.png"
S3_FLOAT=f"{IMG}/ocf-step03-float.png"
REFLECT_EN=f"{SITE}/assets/course-documents/Off-Camera-Flash-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Off-Camera-Flash-Reflection-ES.docx"
AREA="Photography Folder"

# Outside-resource links on the Overview's "Go Deeper" section (same English resources in EN + ES).
VID1="https://vimeo.com/1222759721/f73154d03c?fl=pl&amp;fe=sh"
VID2="https://vimeo.com/1222759720/2219d6c39d?fl=pl&amp;fe=sh"
ART1="https://www.adorama.com/alc/overpower-sun-flash-photography"
ART2="https://digital-photography-school.com/a-beginners-guide-to-working-with-flash-off-camera/"

OVER="photo2-ocf-overview.html"
S1="photo2-ocf-step01-inspiration.html"
S2="photo2-ocf-step02-photowalk.html"
S3="photo2-ocf-step03-reflection.html"

# ---- module-local helpers (no framework equivalent; all cohesive to their section color) ----
def downloads_block(es):
    # Orange Downloads section (Overview only). OCF holds the reflection doc, same as the old page.
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

def pills(labels):
    # Teal meta pills under the Overview hero (cohesive inside the teal type card).
    r="".join('<span style="display:inline-block;background:rgba(0,116,116,0.22);border:1px solid rgba(0,184,184,0.35);'
      'color:#80e0e0;font-size:10.5pt;letter-spacing:0.06em;text-transform:uppercase;padding:6px 12px;margin:0 8px 8px 0;">'
      f'<strong>{t}</strong></span>' for t in labels)
    return f'<div style="margin:6px 0 4px;">{r}</div>'

def scroll_steps(scroll_hint, items):
    # Horizontal snap-scroll of teal step cards (the OneDrive set-up walkthrough). Cohesive teal.
    cards=""
    for stepword,title,body in items:
        cards+=('<div style="scroll-snap-align:start;">'
          '<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;height:100%;box-sizing:border-box;">'
          '<div style="background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:18px;height:100%;box-sizing:border-box;">'
          f'<div style="font-size:10pt;letter-spacing:0.12em;text-transform:uppercase;color:#80e0e0;margin-bottom:6px;"><strong>{stepword}</strong></div>'
          f'<div style="font-size:13pt;color:#ffffff;margin-bottom:6px;"><strong>{title}</strong></div>'
          f'<div style="font-size:11.5pt;line-height:1.55;color:rgba(255,255,255,0.86);">{body}</div>'
          '</div></div></div>')
    return (f'<div style="font-size:9.5pt;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.45);margin-bottom:8px;">{scroll_hint}</div>'
      '<div style="display:grid;grid-auto-flow:column;grid-auto-columns:minmax(240px,1fr);overflow-x:auto;overflow-y:hidden;gap:14px;padding-bottom:18px;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;">'
      + cards + '</div>')

def panels(pairs):
    # Full-width flex row of teal sub-panels (title + a paragraph body), wraps to stack when narrow.
    cells=""
    for title,body in pairs:
        cells+=('<div style="flex:1 1 260px;min-width:0;background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">'
          '<div style="background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:18px;height:100%;box-sizing:border-box;">'
          f'<div style="font-size:12pt;letter-spacing:0.04em;color:#5eead4;margin:2px 0 10px;"><strong>{title}</strong></div>'
          f'<div style="font-size:11.5pt;line-height:1.55;color:rgba(255,255,255,0.84);">{body}</div></div></div>')
    return f'<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:6px;">{cells}</div>'

def subcols(pairs):
    # Full-width flex row of teal sub-panels (title + bullet list); wraps to stack when narrow.
    cells=""
    for title,its in pairs:
        lis="".join('<div style="margin-bottom:6px;line-height:1.45;"><span style="color:#00b8b8;">&bull;</span> '
          f'<span style="font-size:11.5pt;color:rgba(255,255,255,0.84);">{it}</span></div>' for it in its)
        cells+=('<div style="flex:1 1 260px;min-width:0;background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">'
          '<div style="background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:18px;height:100%;box-sizing:border-box;">'
          f'<div style="font-size:12pt;letter-spacing:0.04em;color:#5eead4;margin:2px 0 10px;"><strong>{title}</strong></div>{lis}</div></div>')
    return f'<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:6px;">{cells}</div>'

def sublabel(t):
    # Teal sub-heading inside a content card (cohesive).
    return f'<div style="font-size:12pt;letter-spacing:0.04em;color:#5eead4;margin:2px 0 10px;"><strong>{t}</strong></div>'

def teal_callout(label,body):
    # Labeled teal callout, cohesive inside a teal content card (recolored from the old red box).
    return ('<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.30);border-left:4px solid #00b8b8;padding:14px 16px;margin:4px 0 16px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:5px;"><strong>{label}</strong></div>'
      f'<div style="font-size:13pt;color:rgba(255,255,255,0.92);line-height:1.5;">{body}</div></div>')

def teal_info(body):
    # Standalone non-bold teal info box (the Lightroom preset note). Cohesive teal.
    return ('<div style="background:rgba(0,184,184,0.08);border:1px solid rgba(0,184,184,0.30);border-left:4px solid #00b8b8;padding:14px 16px;margin:0 0 24px;">'
      f'<div style="font-size:13pt;color:rgba(255,255,255,0.90);line-height:1.6;">{body}</div></div>')

def ref_item(kind,href,title,desc):
    # Outside-resource row inside the PURPLE Resources card: purple type chip + purple-light
    # underlined title link + muted description. Recolored from the old red VIDEO / teal ARTICLE
    # chips and teal link for section cohesion.
    return ('<div style="margin-bottom:12px;line-height:1.5;">'
      f'<span style="display:inline-block;background:#8b5cf6;color:#ffffff;font-size:8.5pt;letter-spacing:0.12em;padding:2px 7px;margin-right:8px;vertical-align:middle;"><strong>{kind}</strong></span>'
      f'<a href="{href}" target="_blank" rel="noopener" style="color:#c4b5fd;font-size:13pt;text-decoration:underline;"><strong>{title}</strong></a>'
      f'<div style="font-size:11.5pt;color:rgba(255,255,255,0.72);margin-top:2px;">{desc}</div></div>')

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Off-Camera Flash</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 2A &bull; Off-Camera Flash","Off-Camera Flash","Light your subject. Balance the sky.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Outdoor Portraits with Off-Camera Flash",
        para("In this project you will light an outdoor portrait with off-camera flash (OCF). We will do this as a class. Mr. Silva will teach you how to place a flash off to the side, dial in your settings, and balance your subject with the background. We have several Canon Speedlites and a more powerful Godox portable light. Four or five flashes will be in rotation, so everyone gets hands-on practice.")
        + framed(HEADER,"Students lighting an outdoor portrait with off-camera flash at the PV Academy of Arts")
        + pills(["Off-Camera Flash","Outdoor Portraits","Class Photo Walk","Manual Settings"]))
    en+=downloads_block(False)
    en+=card("","Set Up OneDrive and Your Folders",
        para("First, make sure OneDrive is running, then build your folder structure. Scroll through the steps.")
        + scroll_steps("Scroll for all the steps &rarr;",[
            ("Step 1","Check OneDrive Is Running","Look at the top right of your Mac screen, in the row of small icons next to the time and date. Find the OneDrive cloud icon."),
            ("Step 2","Fix a Sign-In Error","If the cloud icon has an X on it, you are not signed in. Click it and log in with your school account to clear the error."),
            ("Step 3","No Icon? Open OneDrive","If you do not see the cloud icon, press Command + Spacebar, type &lsquo;OneDrive,&rsquo; and press Return to open the app. Then sign in."),
            ("Step 4","Open at Login","Right-click the OneDrive icon in the Dock at the bottom, choose Options, then click &lsquo;Open at Login&rsquo; so OneDrive starts every time."),
            ("Step 5","Go to Photography","In OneDrive, open your Photography folder."),
            ("Step 6","Make the Main Folder","Create a new folder and name it &lsquo;Off Camera Flash.&rsquo;"),
            ("Step 7","Make Two Subfolders","Inside &lsquo;Off Camera Flash,&rsquo; make two folders: &lsquo;Inspiration Images&rsquo; and &lsquo;RAW.&rsquo;"),
            ("Step 8","What They Are For","&lsquo;Inspiration Images&rsquo; holds your Step 1 examples. &lsquo;RAW&rsquo; is where you import your photo walk images in Step 2."),
        ]))
    en+=card("","Natural Light vs Off-Camera Flash",
        para("The goal is a balanced exposure: a rich, detailed background and a well-lit subject in the same frame. You control the background with your camera settings (ambient exposure) and control your subject with the flash (flash exposure).")
        + panels([
            ("Natural Light Only","When you expose for a bright sky, your subject goes dark. When you expose for your subject, the background blows out (loses all detail and turns white). Natural light alone forces you to choose one or the other."),
            ("With Off-Camera Flash","Off-camera flash lights your subject on its own. Now you can expose the background for the sky (keeping color and detail) and let the flash bring your subject up to a balanced exposure. Subject and background both look right."),
        ]))
    en+=card("","Adjust Your Settings for Outdoor Flash",
        bullets([
            ("","Work in Manual Mode so you control both exposures."),
            ("","Set your ambient exposure first: pick an aperture and ISO, then use shutter speed to darken or brighten the background."),
            ("","Turn on High-Speed Sync (HSS) on BOTH your Canon R50 and the Godox transmitter. HSS lets the flash fire at fast shutter speeds so you can use flash in bright sun."),
            ("","Set your flash to Manual power so you control it yourself, not the camera. Adjust the flash power until your subject looks right."),
            ("","Place the flash off to the side and slightly above for shape and depth."),
            ("","Overpower the sun: raise your flash power so your subject stands out against a darker, richer sky."),
        ]))
    en+=resources_card("Go Deeper (Outside Resources)",
        para("Want to push your flash further? These videos and articles show how pros use a single flash outdoors.")
        + ref_item("VIDEO",VID1,"Speedlight Basics: Outdoor Portraits with Off-Camera Flash","A step-by-step look at setting up one speedlight for an outdoor portrait.")
        + ref_item("VIDEO",VID2,"Basic One-Light Outdoor Flash (Speedlight)","How one flash can bring out color in the sky behind your subject.")
        + ref_item("ARTICLE",ART1,"How to Overpower the Sun with Flash (Adorama)","The settings and gear used to balance a bright sky with your subject.")
        + ref_item("ARTICLE",ART2,"A Beginner&rsquo;s Guide to Off-Camera Flash (DPS)","Simple steps for lighting a portrait with a flash off the camera."), False)
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Ambient Light","The light already in the scene, like the sun or the sky, before you add any flash."),
           ("Off-Camera Flash (OCF)","A flash placed away from your camera, off to the side, to light your subject from an angle."),
           ("Fill Flash","A little flash used to brighten the shadows on your subject so a bright background does not leave them dark."),
           ("High-Speed Sync (HSS)","A flash mode that lets you use fast shutter speeds with flash, so you can use flash in bright sun."),
           ("Manual Flash","You set the exact flash power yourself and keep it the same for every photo, so your light stays consistent."),
           ("Overpowering the Sun","Raising your flash power so your subject is bright and stands out against a darker, richer background.")]), False)

    es=banner("Fotograf&iacute;a 2A &bull; Flash Fuera de C&aacute;mara","Flash Fuera de C&aacute;mara","Ilumina a tu sujeto. Equilibra el cielo.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","Retratos al Aire Libre con Flash Fuera de C&aacute;mara",
        para("En este proyecto vas a iluminar un retrato al aire libre con flash fuera de c&aacute;mara (OCF). Lo haremos como clase. El Sr. Silva ense&ntilde;a c&oacute;mo colocar un flash hacia un lado, ajustar tus configuraciones y equilibrar a tu sujeto con el fondo. Tenemos varios Canon Speedlite y una luz Godox port&aacute;til m&aacute;s potente. Habr&aacute; cuatro o cinco flashes en rotaci&oacute;n para que todos practiquen.")
        + framed(HEADER,"Estudiantes iluminando un retrato al aire libre con flash fuera de c&aacute;mara en la PV Academy of Arts")
        + pills(["Flash Fuera de C&aacute;mara","Retratos al Aire Libre","Caminata de Clase","Modo Manual"]))
    es+=downloads_block(True)
    es+=card("","Configura OneDrive y Tus Carpetas",
        para("Primero, aseg&uacute;rate de que OneDrive est&eacute; activo y crea tu estructura de carpetas. Desliza para ver los pasos.")
        + scroll_steps("Desliza para ver todos los pasos &rarr;",[
            ("Paso 1","Revisa Que OneDrive Est&eacute; Activo","Mira arriba a la derecha de tu Mac, en la fila de &iacute;conos peque&ntilde;os junto a la hora y la fecha. Busca el &iacute;cono de nube de OneDrive."),
            ("Paso 2","Arregla un Error de Sesi&oacute;n","Si el &iacute;cono de nube tiene una X, no has iniciado sesi&oacute;n. Haz clic y entra con tu cuenta escolar para quitar el error."),
            ("Paso 3","&iquest;No Hay &Iacute;cono? Abre OneDrive","Si no ves el &iacute;cono de nube, presiona Command + Barra espaciadora, escribe &lsquo;OneDrive&rsquo; y presiona Return para abrir la app. Luego inicia sesi&oacute;n."),
            ("Paso 4","Abrir al Iniciar Sesi&oacute;n","Haz clic derecho en el &iacute;cono de OneDrive en el Dock de abajo, elige Opciones y marca &lsquo;Abrir al iniciar sesi&oacute;n&rsquo; para que OneDrive arranque cada vez."),
            ("Paso 5","Ve a Fotograf&iacute;a","En OneDrive, abre tu carpeta de Fotograf&iacute;a."),
            ("Paso 6","Crea la Carpeta Principal","Crea una carpeta nueva y ll&aacute;mala &lsquo;Off Camera Flash.&rsquo;"),
            ("Paso 7","Crea Dos Subcarpetas","Dentro de &lsquo;Off Camera Flash,&rsquo; crea dos carpetas: &lsquo;Inspiration Images&rsquo; y &lsquo;RAW.&rsquo;"),
            ("Paso 8","Para Qu&eacute; Sirven","&lsquo;Inspiration Images&rsquo; guarda tus ejemplos del Paso 1. &lsquo;RAW&rsquo; es donde importas tus im&aacute;genes de la caminata en el Paso 2."),
        ]))
    es+=card("","Luz Natural vs Flash Fuera de C&aacute;mara",
        para("La meta es una exposici&oacute;n equilibrada: un fondo rico y con detalle, y un sujeto bien iluminado en el mismo cuadro. T&uacute; controlas el fondo con tus configuraciones (exposici&oacute;n ambiente) y controlas a tu sujeto con el flash (exposici&oacute;n de flash).")
        + panels([
            ("Solo Luz Natural","Cuando expones para un cielo brillante, tu sujeto sale oscuro. Cuando expones para tu sujeto, el fondo se quema (pierde todo el detalle, se vuelve blanco). Con solo luz natural tienes que elegir uno o el otro."),
            ("Con Flash Fuera de C&aacute;mara","El flash ilumina a tu sujeto por su cuenta. Ahora puedes exponer el fondo para el cielo (guardando color y detalle) y dejar que el flash suba a tu sujeto a una exposici&oacute;n equilibrada. El sujeto y el fondo se ven bien."),
        ]))
    es+=card("","Ajusta Tus Configuraciones para Flash al Aire Libre",
        bullets([
            ("","Trabaja en Modo Manual para controlar las dos exposiciones."),
            ("","Ajusta primero tu exposici&oacute;n ambiente: elige una apertura y un ISO, luego usa la velocidad de obturaci&oacute;n para oscurecer o aclarar el fondo."),
            ("","Activa la Sincronizaci&oacute;n de Alta Velocidad (HSS) en tu Canon R50 Y en el transmisor Godox. La HSS deja que el flash dispare a velocidades r&aacute;pidas para usarlo bajo sol fuerte."),
            ("","Pon tu flash en potencia Manual para controlarlo t&uacute; mismo, no la c&aacute;mara. Ajusta la potencia del flash hasta que tu sujeto se vea bien."),
            ("","Coloca el flash hacia un lado y un poco arriba para dar forma y profundidad."),
            ("","Domina el sol: sube la potencia del flash para que tu sujeto resalte contra un cielo m&aacute;s oscuro y rico."),
        ]))
    es+=resources_card("Ve M&aacute;s a Fondo (Recursos Externos)",
        para("&iquest;Quieres llevar tu flash m&aacute;s lejos? Estos videos y art&iacute;culos (en ingl&eacute;s) muestran c&oacute;mo los profesionales usan un solo flash al aire libre.")
        + ref_item("VIDEO",VID1,"Speedlight Basics: Outdoor Portraits with Off-Camera Flash","A step-by-step look at setting up one speedlight for an outdoor portrait.")
        + ref_item("VIDEO",VID2,"Basic One-Light Outdoor Flash (Speedlight)","How one flash can bring out color in the sky behind your subject.")
        + ref_item("ARTICLE",ART1,"How to Overpower the Sun with Flash (Adorama)","The settings and gear used to balance a bright sky with your subject.")
        + ref_item("ARTICLE",ART2,"A Beginner&rsquo;s Guide to Off-Camera Flash (DPS)","Simple steps for lighting a portrait with a flash off the camera."), True)
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Luz Ambiente","La luz que ya est&aacute; en la escena, como el sol o el cielo, antes de agregar cualquier flash."),
           ("Flash Fuera de C&aacute;mara","Un flash colocado lejos de tu c&aacute;mara, hacia un lado, para iluminar a tu sujeto desde un &aacute;ngulo."),
           ("Flash de Relleno","Un poco de flash que aclara las sombras de tu sujeto para que un fondo brillante no lo deje oscuro."),
           ("Sincronizaci&oacute;n de Alta Velocidad (HSS)","Un modo de flash que te deja usar velocidades r&aacute;pidas con flash, para usarlo bajo sol fuerte."),
           ("Flash Manual","T&uacute; fijas la potencia exacta del flash y la mantienes igual en cada foto, para que tu luz sea consistente."),
           ("Dominar el Sol","Subir la potencia del flash para que tu sujeto se vea brillante y resalte contra un fondo m&aacute;s oscuro y rico.")]), True)

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Off-Camera Flash | Photography 2A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Photography 2A &bull; Off-Camera Flash &bull; Step 01","Find Inspiration","Gather one-strobe inspiration.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 screen capture (PNG):","your &lsquo;Inspiration Images&rsquo; folder with your saved inspiration images inside, uploaded to this Canvas assignment.")])
    en+=card("","Find Off-Camera Flash Inspiration",
        float_right(S1_FLOAT,"A Pioneer Valley student researching off-camera flash examples on a lab computer","")
        + para("Before we go out, gather inspiration. Look at how other photographers use off-camera flash outdoors. Save your examples into the &lsquo;Inspiration Images&rsquo; folder you set up on this module&rsquo;s Overview page (marked M at the top).")
        + steps([
            ("","Open your &lsquo;Off Camera Flash&rsquo; folder in OneDrive, then the &lsquo;Inspiration Images&rsquo; folder inside it."),
            ("","Search Google Images for &lsquo;outdoor portrait with one strobe&rsquo;."),
            ("","Find 6 to 10 strong examples you like."),
            ("","Save them into your &lsquo;Inspiration Images&rsquo; folder. You can drag and drop straight from Google Images."),
        ])
        + note("Set up your folders first on this module&rsquo;s Overview page (marked M at the top).")
        + subcols([
          ("Where to Save",["Open your &lsquo;Off Camera Flash&rsquo; folder in OneDrive.","Go into the &lsquo;Inspiration Images&rsquo; folder you made on this module&rsquo;s Overview page (marked M at the top).","This is where your saved examples go."]),
          ("Take the Screen Capture (F15)",["Open your &lsquo;Inspiration Images&rsquo; folder so the images show.","Press F15 on your keyboard to take the screen capture.","The screen capture must show the folder with your inspiration images inside.","F15 saves the screen capture as a PNG on your Desktop. These are temporary files: after you turn yours in, you can move them to the Trash."]),
        ]))

    es=banner("Fotograf&iacute;a 2A &bull; Flash Fuera de C&aacute;mara &bull; Paso 01","Busca Inspiraci&oacute;n","Junta inspiraci&oacute;n de un flash.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 captura de pantalla (PNG):","tu carpeta &lsquo;Inspiration Images&rsquo; con tus im&aacute;genes de inspiraci&oacute;n guardadas adentro, subida a esta tarea de Canvas.")])
    es+=card("","Busca Inspiraci&oacute;n de Flash Fuera de C&aacute;mara",
        float_right(S1_FLOAT,"Un estudiante de Pioneer Valley investigando ejemplos de flash fuera de c&aacute;mara en una computadora del laboratorio","")
        + para("Antes de salir, junta inspiraci&oacute;n. Mira c&oacute;mo otros fot&oacute;grafos usan el flash fuera de c&aacute;mara al aire libre. Guarda tus ejemplos en la carpeta &lsquo;Inspiration Images&rsquo; que preparaste en la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba).")
        + steps([
            ("","Abre tu carpeta &lsquo;Off Camera Flash&rsquo; en OneDrive y luego la carpeta &lsquo;Inspiration Images&rsquo; que est&aacute; adentro."),
            ("","Busca en Google Im&aacute;genes: &lsquo;outdoor portrait with one strobe&rsquo;."),
            ("","Encuentra de 6 a 10 buenos ejemplos que te gusten."),
            ("","Gu&aacute;rdalos en tu carpeta &lsquo;Inspiration Images&rsquo;. Puedes arrastrar y soltar directo desde Google Im&aacute;genes."),
        ])
        + note("Primero prepara tus carpetas en la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba).")
        + subcols([
          ("D&oacute;nde Guardar",["Abre tu carpeta &lsquo;Off Camera Flash&rsquo; en OneDrive.","Entra a la carpeta &lsquo;Inspiration Images&rsquo; que creaste en la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba).","Ah&iacute; van tus ejemplos guardados."]),
          ("Toma la Captura (F15)",["Abre tu carpeta &lsquo;Inspiration Images&rsquo; para ver las im&aacute;genes.","Presiona F15 en el teclado para tomar la captura de pantalla.","La captura debe mostrar la carpeta con tus im&aacute;genes de inspiraci&oacute;n adentro.","F15 guarda la captura como un PNG en tu Escritorio. Son archivos temporales: despu&eacute;s de entregar, puedes moverlos a la Papelera."]),
        ]))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Find Inspiration | Off-Camera Flash | Photography 2A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Photography 2A &bull; Off-Camera Flash &bull; Step 02","Photo Walk","Capture, contact sheet, edit 3.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 contact sheet (high-resolution JPG):","your 12-Up contact sheet (or sheets), uploaded to this Canvas assignment."),
         ("3 edited portraits (JPG):","your 3 polished, edited portraits that clearly use off-camera flash, uploaded to this Canvas assignment.")])
    en+=card("","Capture Outdoor Portraits with Off-Camera Flash",
        float_right(S2_FLOAT,"A Pioneer Valley student portrait made with off-camera flash at golden hour","")
        + para("We will do this photo walk as a class. Mr. Silva will facilitate and teach as we go. You will pair up. Each of you takes a turn as the photographer and a turn as the subject, capturing portraits with off-camera flash.")
        + para("Capture a mix: some frames in natural light only, and some with off-camera flash, so you can see the difference side by side.")
        + sublabel("Back in the Lab")
        + steps([
            ("","Import your photo walk images to Lightroom Classic, saving them into your &lsquo;Off Camera Flash &rarr; RAW&rsquo; folder."),
            ("","Build a contact sheet with the 12-Up preset for all the images you captured. Use more than one sheet if you have more than 12."),
            ("","Your contact sheet should show both your natural-light frames and your off-camera-flash frames."),
            ("","Select your 3 strongest portraits that clearly use off-camera flash and edit them to a polished finish."),
        ])
        + teal_callout("The Rule","Off-camera flash must be clearly visible in your 3 final portraits.")
        + note("The contact sheet preset is on this module&rsquo;s Overview page (marked M at the top)."))
    en+=teal_info("Use your Lightroom contact sheet presets (the saved settings that build the contact sheet for you) to make your contact sheet.")

    es=banner("Fotograf&iacute;a 2A &bull; Flash Fuera de C&aacute;mara &bull; Paso 02","Caminata","Captura, hoja de contactos, edita 3.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 hoja de contactos (JPG de alta resoluci&oacute;n):","tu hoja de contactos 12-Up (o varias hojas), subida a esta tarea de Canvas."),
         ("3 retratos editados (JPG):","tus 3 retratos pulidos y editados que usen claramente el flash fuera de c&aacute;mara, subidos a esta tarea de Canvas.")])
    es+=card("","Captura Retratos al Aire Libre con Flash Fuera de C&aacute;mara",
        float_right(S2_FLOAT,"Un retrato de una estudiante de Pioneer Valley hecho con flash fuera de c&aacute;mara en la hora dorada","")
        + para("Haremos esta caminata como clase. El Sr. Silva la gu&iacute;a y ense&ntilde;a mientras avanzamos. Vas a formar pareja. Cada uno toma un turno como fot&oacute;grafo y un turno como sujeto, capturando retratos con flash fuera de c&aacute;mara.")
        + para("Captura una mezcla: algunas tomas solo con luz natural y algunas con flash fuera de c&aacute;mara, para que veas la diferencia lado a lado.")
        + sublabel("De Vuelta en el Laboratorio")
        + steps([
            ("","Importa tus im&aacute;genes de la caminata a Lightroom Classic y gu&aacute;rdalas en tu carpeta &lsquo;Off Camera Flash &rarr; RAW&rsquo;."),
            ("","Arma una hoja de contactos con el ajuste 12-Up para todas las im&aacute;genes que capturaste. Usa m&aacute;s de una hoja si tienes m&aacute;s de 12."),
            ("","Tu hoja de contactos debe mostrar tanto tus tomas de luz natural como las de flash fuera de c&aacute;mara."),
            ("","Elige tus 3 retratos m&aacute;s fuertes que usen claramente el flash fuera de c&aacute;mara y ed&iacute;talos a un acabado pulido."),
        ])
        + teal_callout("La Regla","El flash fuera de c&aacute;mara debe verse claramente en tus 3 retratos finales.")
        + note("El ajuste de la hoja de contactos est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba)."))
    es+=teal_info("Usa tus configuraciones de hoja de contactos de Lightroom (los ajustes guardados que arman la hoja de contactos por ti) para crear tu hoja de contactos.")

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)+dot(S3,'3',"Step 03",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a><a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Photo Walk | Off-Camera Flash | Photography 2A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 03 ----------------
def step03():
    en=banner("Photography 2A &bull; Off-Camera Flash &bull; Step 03","Reflection","Your own experience, in writing.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 reflection (.docx):","your reflection document with all 4 questions answered, uploaded to this Canvas assignment.")])
    en+=card("","Reflect on Your Off-Camera Flash Experience",
        float_right(S3_FLOAT,"A Pioneer Valley student typing the Off-Camera Flash reflection on a lab computer","")
        + para("This reflection is about your own experience, not your partner&rsquo;s. Answer honestly.")
        + para("Download the reflection document, answer all 4 questions, and turn it in.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder."))

    es=banner("Fotograf&iacute;a 2A &bull; Flash Fuera de C&aacute;mara &bull; Paso 03","Reflexi&oacute;n","Tu propia experiencia, por escrito.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n (.docx):","tu documento de reflexi&oacute;n con las 4 preguntas respondidas, subido a esta tarea de Canvas.")])
    es+=card("","Reflexiona Sobre Tu Experiencia con el Flash",
        float_right(S3_FLOAT,"Un estudiante de Pioneer Valley escribiendo la reflexi&oacute;n de flash fuera de c&aacute;mara en una computadora del laboratorio","")
        + para("Esta reflexi&oacute;n es sobre tu propia experiencia, no la de tu compa&ntilde;ero. Responde con honestidad.")
        + para("Descarga el documento de reflexi&oacute;n, responde las 4 preguntas y entr&eacute;galo.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)+dot("",'3',"Step 03",True)
    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><span></span></div>'
    return wrap_page("Step 3: Reflection | Off-Camera Flash | Photography 2A | PVHS", nav("Step 03",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
