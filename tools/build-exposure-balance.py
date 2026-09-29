#!/usr/bin/env python3
# Build the EXPOSURE BALANCE module (Photo 1A = Module 09, Photo 2A = Module 08).
# Frame one subject (a classmate, a thing on campus, or a provided toy figurine) at f/22, then take the
# SAME framed photo down through the range to f/1.8: six different f-stops, no repeats. Manual mode, the
# student balances shutter + ISO at each stop (ISO as low as possible, shutter never below 1/60, light
# meter between -1 and +1, eye-check the back before capturing). JPG capture, crop-only edit.
# Pages per course: Step 01 Overview (read + download) + Step 02 Capture & 12-Up + Step 03 Edit & Submit
# (6 finals + 6-Up + 6 exports = 7 files) + Step 04 Reflection. Dark teal angular framework.
import os, re
from silva_framework import *

ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
AREA="Photography Folder"
EXPOSURE_FULL=f"{SITE}/assets/images/shared/exposure-basics-v1.jpg"
EXPOSURE_THUMB=f"{SITE}/assets/images/shared/exposure-basics-thumb-v1.jpg"

# No module art yet: every image slot is gated OFF so nothing renders (a missing image shows nothing,
# never a placeholder box). Flip a HAVE_* to True and drop the file in when the art is ready.
HAVE_HEADER=True; HAVE_S1_FLOAT=False; HAVE_S2_FLOAT=False; HAVE_S3_FLOAT=False

COURSES=[
  {"prefix":"photo1","label":"Photography 1A","mod":"09","raw":False,
   "reflect_en":f"{SITE}/assets/course-documents/Exposure-Balance-Reflection-EN.docx",
   "reflect_es":f"{SITE}/assets/course-documents/Exposure-Balance-Reflection-ES.docx",
   "slide_en":f"{SITE}/assets/course-documents/Photo1-Camera-Aperture-Part1-Slides-EN-v3.pdf",
   "slide_es":f"{SITE}/assets/course-documents/Photo1-Camera-Aperture-Part1-Slides-ES-v3.pdf",
   "cover_en":f"{SITE}/assets/images/shared/aperture-part1-cover-photo1-en-v3.jpg",
   "cover_es":f"{SITE}/assets/images/shared/aperture-part1-cover-photo1-es-v3.jpg"},
  {"prefix":"photo2","label":"Photography 2A","mod":"08","raw":True,
   "reflect_en":f"{SITE}/assets/course-documents/Exposure-Balance-Photo2-Reflection-EN.docx",
   "reflect_es":f"{SITE}/assets/course-documents/Exposure-Balance-Photo2-Reflection-ES.docx",
   "slide_en":f"{SITE}/assets/course-documents/Photo2-Camera-Aperture-Part1-Slides-EN-v3.pdf",
   "slide_es":f"{SITE}/assets/course-documents/Photo2-Camera-Aperture-Part1-Slides-ES-v3.pdf",
   "cover_en":f"{SITE}/assets/images/shared/aperture-part1-cover-photo2-en-v3.jpg",
   "cover_es":f"{SITE}/assets/images/shared/aperture-part1-cover-photo2-es-v3.jpg"},
]

# Local ent: accents to entities AND en-dash to a plain hyphen (never emit &ndash;, per the hard dash ban).
def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"-","•":"&bull;","×":"&times;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

def hero_ph(label): return placeholder(label, minh=300)

EXPO_STANDARDS=[
  {"code":"SA.17.5","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Equipment &amp; Image Production","es_title":"Equipo y Producci&oacute;n de Imagen",
   "en_desc":"You use the class camera kit in Manual mode and control aperture, shutter, and ISO on purpose.",
   "es_desc":"Usas el kit de c&aacute;mara de la clase en modo Manual y controlas la apertura, el obturador y el ISO a prop&oacute;sito."},
  {"code":"SA.17.1","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Art &amp; Design Fundamentals","es_title":"Fundamentos de Arte y Dise&ntilde;o",
   "en_desc":"You balance the exposure triangle to keep every photo well exposed across the whole f-stop range.",
   "es_desc":"Equilibras el tri&aacute;ngulo de exposici&oacute;n para que cada foto quede bien expuesta en todo el rango de n&uacute;meros f."},
  {"code":"SA.17.2","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Visual Communication","es_title":"Comunicaci&oacute;n Visual",
   "en_desc":"You show how one subject changes as the aperture and depth of field change through the range.",
   "es_desc":"Muestras c&oacute;mo un mismo sujeto cambia cuando la apertura y la profundidad de campo cambian en el rango."},
  {"code":"SA.17.8","en_tier":"Studio Arts","es_tier":"Artes de Estudio",
   "en_title":"Documentation of Finished Work","es_title":"Documentaci&oacute;n del Trabajo Terminado",
   "en_desc":"You build contact sheets that present your full take and your final one-per-f-stop set clearly.",
   "es_desc":"Creas hojas de contactos que presentan todo tu trabajo y tu set final de una por n&uacute;mero f con claridad."},
]

def build_course(C):
    OVER=f"{C['prefix']}-exposure-balance-overview.html"
    S1=f"{C['prefix']}-exposure-balance-step01-capture-contact.html"
    S2=f"{C['prefix']}-exposure-balance-step02-edit-submit.html"
    S3=f"{C['prefix']}-exposure-balance-step03-reflection.html"
    MOD=C['mod']; LABEL=C['label']; RAW=C['raw']

    def nav(current,dots,stepnav):
        return ('      <div class="silva-breadcrumb">\n'
                '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
                '        <span class="bc-sep">&rsaquo;</span>\n'
                f'        <a href="{OVER}" class="bc-hide-sm">Exposure Balance</a>\n'
                '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
                f'        <span class="bc-current">{current}</span>\n'
                '      </div>\n'
                '      <div class="silva-nav-spacer"></div>\n'
                f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
                f'      <div class="silva-step-nav">{stepnav}</div>')
    DOTS_TITLES=[("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04")]
    def dots_for(active_idx):
        hrefs=[OVER,S1,S2,S3]; r=""
        for i,(lab,title) in enumerate(DOTS_TITLES):
            r+=dot("" if i==active_idx else hrefs[i], lab, title, i==active_idx, module=False)
        return r

    def downloads_block(es):
        heading="Descarga Tus Archivos" if es else "Download Your Files"
        lead=("Descarga el documento de reflexi&oacute;n de este m&oacute;dulo. Tus ajustes de hoja de contactos ya est&aacute;n instalados en Lightroom; si alguna vez los necesitas otra vez, est&aacute;n en la p&aacute;gina de Resumen del curso." if es
              else "Download this module&rsquo;s reflection document. Your contact sheet presets are already installed in Lightroom; if you ever need them again, they are on the Course Overview page.")
        reflabel="Documento de Reflexi&oacute;n (Word)" if es else "Reflection Document (Word)"
        ref=C['reflect_es'] if es else C['reflect_en']
        return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
          + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
          + para(lead)
          + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
          + dl_link(ref,reflabel,row=True)
          + '</div>'
          + folder_note(es, AREA) + '</div>')

    def exposure_poster(es):
        if es:
            heading="P&oacute;ster de Conceptos de Exposici&oacute;n"
            body=para("Este p&oacute;ster repasa lo b&aacute;sico de la exposici&oacute;n: la apertura, la velocidad del obturador y el ISO, y c&oacute;mo cada n&uacute;mero cambia la luz, el movimiento, la profundidad de campo y el grano. &Uacute;salo como referencia mientras equilibras tu exposici&oacute;n.")
            alt="P&oacute;ster de Conceptos de Exposici&oacute;n: apertura, velocidad del obturador e ISO"
            cap="Toca para abrirlo en grande en una pesta&ntilde;a nueva."
        else:
            heading="Exposure Basics Poster"
            body=para("This poster covers the basics of exposure: aperture, shutter speed, and ISO, and how each number changes light, motion, depth of field, and grain. Use it as a reference while you balance your exposure.")
            alt="Exposure Basics poster: aperture, shutter speed, and ISO"
            cap="Tap to open it full size in a new tab."
        return resources_card(heading, body, es, floatimg=purple_thumb(EXPOSURE_FULL, EXPOSURE_THUMB, alt, cap))

    # ---- study materials: ONE purple resources card holding both the aperture concept deck (PDF)
    #      and the exposure basics poster, side by side (stacks on narrow). ----
    def study_resources(es):
        if es:
            heading="Diapositivas de Apertura y P&oacute;ster"
            intro="Est&uacute;dialos antes de capturar. Las diapositivas muestran c&oacute;mo funcionan la apertura y los n&uacute;meros f; el p&oacute;ster cubre todo el tri&aacute;ngulo de exposici&oacute;n."
            scap="Diapositivas de apertura (PDF). Toca para abrir en una pesta&ntilde;a nueva."
            pcap="P&oacute;ster de conceptos de exposici&oacute;n. Toca para abrir en grande."
            palt="P&oacute;ster de Conceptos de Exposici&oacute;n: apertura, velocidad del obturador e ISO"
        else:
            heading="Aperture Slides &amp; Poster"
            intro="Study these before you capture. The slides show how aperture and f-stops work; the poster covers the whole exposure triangle."
            scap="Aperture slides (PDF). Tap to open in a new tab."
            pcap="Exposure basics poster. Tap to open full size."
            palt="Exposure Basics poster: aperture, shutter speed, and ISO"
        pdf=C['slide_es'] if es else C['slide_en']
        cover=C['cover_es'] if es else C['cover_en']
        two=('<div style="display:flex;flex-wrap:wrap;gap:20px 26px;align-items:flex-start;margin-top:8px;">'
             + f'<div style="flex:1 1 280px;min-width:0;">{slide_deck_thumb(pdf, es, thumb=cover, cap=scap)}</div>'
             + f'<div style="flex:1 1 280px;min-width:0;">{purple_thumb(EXPOSURE_FULL, EXPOSURE_THUMB, palt, pcap)}</div>'
             + '</div>')
        return resources_card(heading, para(intro)+two, es)

    # ---- custom red camera-settings section: aperture steps the range; shutter + ISO balance ----
    def exposure_settings_section(es, quality="JPG"):
        red="#f90101"
        if es:
            title="Ajustes de C&aacute;mara"
            lead=("Trabaja en modo Manual (M). T&uacute; controlas los tres ajustes: apertura, obturador e ISO. Encuadra tu sujeto y toma tu primera foto en <strong>f/22</strong>. "
                  "Luego toma la MISMA foto en cinco n&uacute;meros f m&aacute;s, hasta <strong>f/1.8</strong>: seis n&uacute;meros f distintos en total, sin repetir ninguno.")
            note_t=("En cada n&uacute;mero f, equilibra tu exposici&oacute;n: mant&eacute;n el expos&iacute;metro entre <strong>-1 y +1</strong>. Mant&eacute;n tu ISO lo m&aacute;s bajo posible y nunca dejes que el obturador baje de <strong>1/60</strong>. "
                    "Si en f/22 est&aacute; muy oscuro para mantener 1/60, sube un poco el ISO. Al abrir hacia f/1.8 entra m&aacute;s luz, as&iacute; que acelera el obturador y baja el ISO otra vez. Revisa la parte de atr&aacute;s de la c&aacute;mara antes de cada captura.")
        else:
            title="Camera Settings"
            lead=("Work in Manual mode (M). You control all three settings: aperture, shutter, and ISO. Frame your subject and take your first photo at <strong>f/22</strong>. "
                  "Then take the SAME photo at five more f-stops, all the way down to <strong>f/1.8</strong>: six different f-stops in all, with no repeats.")
            note_t=("At each f-stop, balance your exposure: keep the light meter between <strong>-1 and +1</strong>. Keep your ISO as low as it will go, and never let the shutter drop below <strong>1/60</strong>. "
                    "If f/22 is too dark to keep 1/60, raise your ISO a little. As you open up toward f/1.8, more light comes in, so speed up the shutter and drop the ISO back down. Check the back of the camera before every capture.")
        lead_html=f'<div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{lead}</span></div>'
        note_box=(f'<div style="background:rgba(249,1,1,0.10);border:1px solid rgba(249,1,1,0.30);border-left:4px solid {red};padding:11px 14px;margin:0;overflow:hidden;font-size:12pt;color:rgba(255,255,255,0.92);line-height:1.55;">{note_t}</div>')
        return (f'<div style="background:linear-gradient(180deg,rgba(249,1,1,0.06) 0%,rgba(249,1,1,0.02) 100%);border:1px solid rgba(249,1,1,0.26);border-left:6px solid {red};padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
          + section_header(CAMSET_ICON, title, "#f90101", "#ff8f8f")
          + f'<div class="silva-cfloat" style="float:right;width:50%;min-width:400px;margin:2px 0 16px 30px;">{capture_panel(quality, "1/60+", "f/22", "LOW", "shutter")}</div>'
          + lead_html + note_box + '</div>')

    # ================= OVERVIEW (Step 01) =================
    def overview():
        en=banner(f"Module {MOD} &bull; Step 01","Exposure Balance: Start Here","Read this page and download your files, then go to Step 02 to capture. This module is about balancing your exposure across the whole aperture range.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
        en+=type_card("overview","Step 01 &middot; Overview &amp; Download","One Subject, Six F-Stops",
            para("This module is about <strong>balancing your exposure</strong>. You pick one subject, frame it once, and take the same photo at six different f-stops from <strong>f/22</strong> all the way down to <strong>f/1.8</strong>. At every f-stop you do the math to keep your photo well exposed.")
            + para("Pick your subject: a <strong>classmate</strong>, a thing you find on campus (like a flower), or one of the <strong>toy figurines</strong> Mr. Silva provides. Frame your first photo at f/22, then work down through the range to f/1.8, six different f-stops with no repeats, keeping the same frame the whole time.")
            + (framed(f"{SITE}/assets/images/{C['prefix']}/exposure-balance/header-v1.jpg","Exposure Balance module header") if HAVE_HEADER else ""))
        en+=standards_box(False, EXPO_STANDARDS)
        en+=downloads_block(False)
        en+=study_resources(False)
        en+=card("THE CONCEPT / THE EXPOSURE TRIANGLE","Aperture, Shutter, and ISO Work Together",
            para("Three settings make your exposure: <strong>aperture</strong> (how wide the lens opens), <strong>shutter speed</strong> (how long the light comes in), and <strong>ISO</strong> (how much the camera boosts the light). Together they are the <strong>exposure triangle</strong>. When you change one, you balance another to keep the light right.")
            + bullets([
                ("f/22 (small opening):","very little light comes in, and almost everything is sharp front to back (deep depth of field)."),
                ("f/1.8 (wide opening):","a lot of light comes in, and only your subject is sharp while the background goes soft (shallow depth of field)."),
                ("Every stop you open:","doubles the light. So as you go from f/22 toward f/1.8, you must take light back out with a faster shutter or a lower ISO."),
            ])
            + note("Same subject, same frame, six f-stops. The look changes because of depth of field, but every photo stays well exposed because you balanced it."))
        en+=card("BALANCE YOUR EXPOSURE / THE RULES","Keep It Between -1 and +1",
            para("At each f-stop you are aiming for a good in-camera exposure. Follow these rules and use your eyes.")
            + bullets([
                ("Light meter -1 to +1:","set your shutter and ISO so the light meter sits between -1 and +1. That is a good exposure."),
                ("ISO as low as possible:","keep your ISO at its lowest (base ISO, like 100) for the cleanest photo. Only raise it if you have to."),
                ("Shutter never below 1/60:","do not let your shutter drop under 1/60 of a second, or your handheld photo will be blurry. If it wants to go lower, raise your ISO instead."),
                ("Eye-check the back:","look at the photo on the back of the camera before you move on. If it is too dark or too bright, fix it and capture again."),
            ]))
        en+=card("HOW IT WORKS / YOUR PLAN","Your Next Three Steps",
            para("You are on Step 01 now: read this page and download your files below. Here are the three steps that follow.")
            + bullets([
                ("Step 02 &middot; Capture &amp; Contact Sheet:","frame your subject, start at f/22, and work down to f/1.8. Take at least two photos at each of your six f-stops (twelve or more), then turn in a 12-Up contact sheet of your whole take."),
                ("Step 03 &middot; Edit &amp; Submit:",("develop each one fully in Lightroom, fine-tune your preset, crop, and turn in a 6-Up contact sheet plus the six edited JPGs (seven files)." if RAW else "pick your best one at each f-stop (six finals, each a different f-stop), crop them, and turn in a 6-Up contact sheet plus the six final JPGs (seven files).")),
                ("Step 04 &middot; Reflection:","tell what you learned about balancing your exposure."),
            ])
            + note("This is a RAW capture. In Step 03 you develop each photo fully: a detailed edit, your own preset, and a crop." if RAW else "This is a JPG capture. Get your exposure right in the camera so it looks good straight out of the camera. The only edit you need is a crop."))
        en+=resources_card("Key Words",
            vocab_grid("On the Quiz",
              "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
              [("Aperture","How wide the lens opens, written as an f-stop like f/22 or f/1.8. A big number (f/22) is a small opening; a small number (f/1.8) is wide open."),
               ("Exposure Triangle","The three settings that make your exposure and work together: aperture, shutter speed, and ISO. Change one and you balance another."),
               ("Stop","One step of light. Each f-stop is about one stop: it doubles the light or cuts it in half. Shutter and ISO steps work the same way."),
               ("Equivalent Exposure","Different settings can give the same brightness. Open the aperture one stop and speed the shutter one stop, and the exposure stays the same. Same light, different look."),
               ("Base ISO","The lowest, cleanest ISO your camera has (like ISO 100). Keep your ISO as low as you can for the least grain."),
               ("Light Meter","The scale in your camera that shows if your photo is too dark or too bright. Keep it between -1 and +1.")]))
        en+=next_up("UP NEXT &middot; STEP 02 - Capture &amp; Contact Sheet","Frame your subject, start at f/22, work down to f/1.8, and build your 12-Up contact sheet.")

        es=banner(f"M&oacute;dulo {MOD} &bull; Paso 01","Balance de Exposici&oacute;n: Empieza Aqu&iacute;","Lee esta p&aacute;gina y descarga tus archivos, luego ve al Paso 02 para capturar. Este m&oacute;dulo trata de equilibrar tu exposici&oacute;n en todo el rango de apertura.","#top","Back to English", HICON_PHOTO_WALK)
        es+=type_card("overview","Paso 01 &middot; Resumen y Descarga","Un Sujeto, Seis N&uacute;meros F",
            para("Este m&oacute;dulo trata de <strong>equilibrar tu exposici&oacute;n</strong>. Eliges un sujeto, lo encuadras una vez y tomas la misma foto en seis n&uacute;meros f distintos, desde <strong>f/22</strong> hasta <strong>f/1.8</strong>. En cada n&uacute;mero f haces la cuenta para que tu foto quede bien expuesta.")
            + para("Elige tu sujeto: un <strong>compa&ntilde;ero</strong>, algo que encuentres en la escuela (como una flor) o una de las <strong>figuras de juguete</strong> que Mr. Silva presta. Encuadra tu primera foto en f/22, luego baja por el rango hasta f/1.8, seis n&uacute;meros f distintos sin repetir, manteniendo el mismo encuadre todo el tiempo.")
            + (framed(f"{SITE}/assets/images/{C['prefix']}/exposure-balance/header-v1.jpg","Encabezado del m&oacute;dulo Balance de Exposici&oacute;n") if HAVE_HEADER else ""))
        es+=standards_box(True, EXPO_STANDARDS)
        es+=downloads_block(True)
        es+=study_resources(True)
        es+=card("EL CONCEPTO / EL TRI&Aacute;NGULO DE EXPOSICI&Oacute;N","Apertura, Obturador e ISO Trabajan Juntos",
            para("Tres ajustes hacen tu exposici&oacute;n: la <strong>apertura</strong> (qu&eacute; tan abierto est&aacute; el lente), la <strong>velocidad del obturador</strong> (cu&aacute;nto tiempo entra la luz) y el <strong>ISO</strong> (cu&aacute;nto sube la luz la c&aacute;mara). Juntos son el <strong>tri&aacute;ngulo de exposici&oacute;n</strong>. Cuando cambias uno, equilibras otro para mantener la luz correcta.")
            + bullets([
                ("f/22 (abertura peque&ntilde;a):","entra muy poca luz y casi todo queda n&iacute;tido de adelante hacia atr&aacute;s (mucha profundidad de campo)."),
                ("f/1.8 (abertura amplia):","entra mucha luz y solo tu sujeto queda n&iacute;tido mientras el fondo se pone suave (poca profundidad de campo)."),
                ("Cada paso que abres:","duplica la luz. As&iacute; que al ir de f/22 hacia f/1.8, debes quitar luz con un obturador m&aacute;s r&aacute;pido o un ISO m&aacute;s bajo."),
            ])
            + note("El mismo sujeto, el mismo encuadre, seis n&uacute;meros f. El estilo cambia por la profundidad de campo, pero cada foto queda bien expuesta porque la equilibraste."))
        es+=card("EQUILIBRA TU EXPOSICI&Oacute;N / LAS REGLAS","Mant&eacute;nla Entre -1 y +1",
            para("En cada n&uacute;mero f buscas una buena exposici&oacute;n en la c&aacute;mara. Sigue estas reglas y usa tus ojos.")
            + bullets([
                ("Expos&iacute;metro -1 a +1:","ajusta el obturador y el ISO para que el expos&iacute;metro quede entre -1 y +1. Esa es una buena exposici&oacute;n."),
                ("ISO lo m&aacute;s bajo posible:","mant&eacute;n tu ISO en lo m&aacute;s bajo (ISO base, como 100) para la foto m&aacute;s limpia. S&oacute;lo s&uacute;belo si es necesario."),
                ("Obturador nunca bajo 1/60:","no dejes que el obturador baje de 1/60 de segundo, o tu foto a pulso saldr&aacute; borrosa. Si quiere bajar m&aacute;s, mejor sube el ISO."),
                ("Revisa la pantalla de atr&aacute;s:","mira la foto en la parte de atr&aacute;s de la c&aacute;mara antes de seguir. Si est&aacute; muy oscura o muy brillante, arr&eacute;glala y captura de nuevo."),
            ]))
        es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Siguientes Tres Pasos",
            para("Ahora est&aacute;s en el Paso 01: lee esta p&aacute;gina y descarga tus archivos abajo. Aqu&iacute; est&aacute;n los tres pasos que siguen.")
            + bullets([
                ("Paso 02 &middot; Captura y Hoja de Contactos:","encuadra tu sujeto, empieza en f/22 y baja hasta f/1.8. Toma al menos dos fotos en cada uno de tus seis n&uacute;meros f (doce o m&aacute;s), luego entrega una hoja de contactos de 12 im&aacute;genes de todo tu trabajo."),
                ("Paso 03 &middot; Edita y Entrega:",("revela cada una por completo en Lightroom, ajusta tu preset, recorta y entrega una hoja de contactos de 6 m&aacute;s las seis im&aacute;genes editadas en JPG (siete archivos)." if RAW else "elige tu mejor foto en cada n&uacute;mero f (seis finales, cada una un n&uacute;mero f distinto), rec&oacute;rtalas y entrega una hoja de contactos de 6 m&aacute;s las seis im&aacute;genes finales en JPG (siete archivos).")),
                ("Paso 04 &middot; Reflexi&oacute;n:","cuenta qu&eacute; aprendiste sobre equilibrar tu exposici&oacute;n."),
            ])
            + note("Esta es una captura en RAW. En el Paso 03 revelas cada foto por completo: una edici&oacute;n detallada, tu propio preset y un recorte." if RAW else "Esta es una captura en JPG. Deja bien tu exposici&oacute;n en la c&aacute;mara para que se vea bien tal como sale. La &uacute;nica edici&oacute;n que necesitas es un recorte."))
        es+=resources_card("Palabras Clave",
            vocab_grid("En el Examen",
              "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el de mitad de semestre y el del final. Apr&eacute;ndelas ahora, no la noche anterior.",
              [("Aperture (Apertura)","Qu&eacute; tan abierto est&aacute; el lente, escrito como n&uacute;mero f, como f/22 o f/1.8. Un n&uacute;mero grande (f/22) es una abertura peque&ntilde;a; uno peque&ntilde;o (f/1.8) es bien abierta."),
               ("Exposure Triangle (Tri&aacute;ngulo de Exposici&oacute;n)","Los tres ajustes que hacen tu exposici&oacute;n y trabajan juntos: apertura, velocidad del obturador e ISO. Cambia uno y equilibra otro."),
               ("Stop (Paso de luz)","Un paso de luz. Cada n&uacute;mero f es como un paso: duplica la luz o la reduce a la mitad. El obturador y el ISO funcionan igual."),
               ("Equivalent Exposure (Exposici&oacute;n Equivalente)","Ajustes distintos pueden dar el mismo brillo. Abre la apertura un paso y acelera el obturador un paso, y la exposici&oacute;n se queda igual. La misma luz, distinto estilo."),
               ("Base ISO (ISO Base)","El ISO m&aacute;s bajo y limpio de tu c&aacute;mara (como ISO 100). Mant&eacute;n tu ISO lo m&aacute;s bajo posible para el menor grano."),
               ("Light Meter (Expos&iacute;metro)","La escala en tu c&aacute;mara que muestra si tu foto est&aacute; muy oscura o muy brillante. Mant&eacute;nla entre -1 y +1.")]))
        es+=next_up("SIGUIENTE &middot; PASO 02 - Captura y Hoja de Contactos","Encuadra tu sujeto, empieza en f/22, baja hasta f/1.8 y arma tu hoja de contactos de 12.")

        stepnav=f'<a href="{S1}" class="silva-step-btn">Step 02 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
        return wrap_page(f"Exposure Balance: Start Here | {LABEL} | PVHS", nav("Step 01",dots_for(0),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 02: Capture & 12-Up =================
    def step_capture():
        en=banner(f"Module {MOD} &bull; Step 02","Capture &amp; Contact Sheet","Frame one subject, work from f/22 down to f/1.8, then build a 12-Up contact sheet.","#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
        en+=type_card("photo-walk","Step 02 &middot; Capture","Pick Your Subject and Frame It",
            para("Take out the camera kit and choose your subject. This time you can photograph <strong>anything you want</strong>: a classmate, something you find on campus (like a flower), or one of the toy figurines Mr. Silva provides. Frame it once and keep that same frame for your whole take.")
            + bullets([
                ("Pick one subject:","a classmate, a campus object, or a toy figurine. Something that holds still so your six photos match."),
                ("Frame it at f/22:","set up your composition and take your first photo at f/22. Do not move the camera or the subject after this."),
                ("Keep the same frame:","take the same photo at each f-stop. Only your settings change, not your framing."),
            ]))
        en+=deliverables_box(False,
            [("1 contact sheet:","a 12-Up contact sheet of your entire take, turned in as a high-resolution JPG.")])
        en+=exposure_settings_section(False, "RAW" if RAW else "JPG")
        en+=exposure_poster(False)
        en+=card("WORK THE RANGE / SIX F-STOPS","f/22 Down to f/1.8, No Repeats",
            para("Start at f/22 and work your way down to f/1.8. Choose <strong>six different f-stops</strong> along the way (you pick them), and do not repeat the same f-stop twice. Take at least <strong>two photos at each f-stop</strong>, so your whole take is twelve photos or more.")
            + steps([
                ("Set Manual mode:","turn the Mode dial to <strong>M</strong>."),
                ("Set your aperture:","press the <strong>up arrow (Up key)</strong>, then turn the <strong>Main Dial</strong> to your f-stop. Start at f/22."),
                ("Balance the meter:","turn the <strong>Main Dial</strong> to set your shutter (keep it 1/60 or faster). If f/22 is too dark, press the <strong>ISO button</strong> and raise the ISO until the meter sits between -1 and +1."),
                ("Eye-check and capture:","look at the back of the camera. Too dark or too bright? Fix it, then take two good photos."),
                ("Open one f-stop:","move to your next f-stop toward f/1.8. More light comes in, so speed up your shutter (and drop the ISO back toward its lowest). Balance the meter again and capture."),
                ("Finish at f/1.8:","keep going until you reach f/1.8, six different f-stops in all, two photos at each."),
            ], accent="#f90101")
            + note("Keep your ISO as low as the light lets you, and never let the shutter go below 1/60. Same frame, six f-stops, every one well exposed."))
        en+=card("BUILD IT / CONTACT SHEET","Turn In a 12-Up Contact Sheet",
            para(("Bring your RAW files into Lightroom Classic and build a 12-Up contact sheet of your whole take, then print it to a high-resolution JPG." if RAW else "Bring your JPGs into Lightroom Classic and build a 12-Up contact sheet of your whole take, then print it to a high-resolution JPG."))
            + steps([
                (("Import your RAW files:" if RAW else "Import your JPGs:"),"offload from the camera kit to OneDrive, then import into Lightroom Classic."),
                ("Use the 12-Up preset:","in the Print module, choose the 12-Up contact sheet preset (you installed it in Image Series)."),
                ("Print to JPG:","use Print to File so it saves as a high-resolution JPG, then upload it here."),
            ])
            + note("Contact sheets are always turned in as a high-resolution JPG."))
        en+=next_up("UP NEXT &middot; STEP 03 - Edit &amp; Submit",("Develop each photo, fine-tune your preset, crop, and turn in a 6-Up plus six edited JPGs." if RAW else "Pick your best one at each f-stop, crop, and turn in a 6-Up plus six final JPGs."))

        es=banner(f"M&oacute;dulo {MOD} &bull; Paso 02","Captura y Hoja de Contactos","Encuadra un sujeto, ve de f/22 hasta f/1.8, y arma una hoja de contactos de 12.","#top","Back to English", HICON_PHOTO_WALK)
        es+=type_card("photo-walk","Paso 02 &middot; Captura","Elige Tu Sujeto y Encu&aacute;dralo",
            para("Saca el kit de c&aacute;mara y elige tu sujeto. Esta vez puedes fotografiar <strong>lo que quieras</strong>: un compa&ntilde;ero, algo que encuentres en la escuela (como una flor) o una de las figuras de juguete que Mr. Silva presta. Encu&aacute;dralo una vez y mant&eacute;n ese mismo encuadre en todo tu trabajo.")
            + bullets([
                ("Elige un sujeto:","un compa&ntilde;ero, un objeto de la escuela o una figura de juguete. Algo que se quede quieto para que tus seis fotos coincidan."),
                ("Encu&aacute;dralo en f/22:","arma tu toma y captura tu primera foto en f/22. No muevas la c&aacute;mara ni el sujeto despu&eacute;s de esto."),
                ("Mant&eacute;n el mismo encuadre:","toma la misma foto en cada n&uacute;mero f. Solo cambian tus ajustes, no tu encuadre."),
            ]))
        es+=deliverables_box(True,
            [("1 hoja de contactos:","una hoja de contactos de 12 im&aacute;genes de todo tu trabajo, entregada como un JPG de alta resoluci&oacute;n.")])
        es+=exposure_settings_section(True, "RAW" if RAW else "JPG")
        es+=exposure_poster(True)
        es+=card("TRABAJA EL RANGO / SEIS N&Uacute;MEROS F","de f/22 a f/1.8, Sin Repetir",
            para("Empieza en f/22 y baja hasta f/1.8. Elige <strong>seis n&uacute;meros f distintos</strong> en el camino (t&uacute; los eliges) y no repitas el mismo n&uacute;mero f. Toma al menos <strong>dos fotos en cada n&uacute;mero f</strong>, para que todo tu trabajo sea doce fotos o m&aacute;s.")
            + steps([
                ("Pon el modo Manual:","gira el dial de modo a <strong>M</strong>."),
                ("Pon tu apertura:","presiona la <strong>flecha hacia arriba</strong>, luego gira el <strong>dial principal</strong> a tu n&uacute;mero f. Empieza en f/22."),
                ("Equilibra el expos&iacute;metro:","gira el <strong>dial principal</strong> para ajustar el obturador (mant&eacute;nlo en 1/60 o m&aacute;s r&aacute;pido). Si f/22 est&aacute; muy oscuro, presiona el <strong>bot&oacute;n ISO</strong> y s&uacute;belo hasta que el expos&iacute;metro quede entre -1 y +1."),
                ("Revisa y captura:","mira la parte de atr&aacute;s de la c&aacute;mara. &iquest;Muy oscura o muy brillante? Arr&eacute;glala y toma dos buenas fotos."),
                ("Abre un n&uacute;mero f:","pasa a tu siguiente n&uacute;mero f hacia f/1.8. Entra m&aacute;s luz, as&iacute; que acelera el obturador (y baja el ISO hacia su m&iacute;nimo). Equilibra el expos&iacute;metro otra vez y captura."),
                ("Termina en f/1.8:","sigue hasta llegar a f/1.8, seis n&uacute;meros f distintos en total, dos fotos en cada uno."),
            ], accent="#f90101")
            + note("Mant&eacute;n tu ISO lo m&aacute;s bajo que la luz permita, y nunca dejes que el obturador baje de 1/60. El mismo encuadre, seis n&uacute;meros f, cada uno bien expuesto."))
        es+=card("&Aacute;RMALA / HOJA DE CONTACTOS","Entrega una Hoja de Contactos de 12",
            para(("Lleva tus archivos RAW a Lightroom Classic y arma una hoja de contactos de 12 im&aacute;genes de todo tu trabajo, luego impr&iacute;mela como un JPG de alta resoluci&oacute;n." if RAW else "Lleva tus JPG a Lightroom Classic y arma una hoja de contactos de 12 im&aacute;genes de todo tu trabajo, luego impr&iacute;mela como un JPG de alta resoluci&oacute;n."))
            + steps([
                (("Importa tus archivos RAW:" if RAW else "Importa tus JPG:"),"descarga del kit de c&aacute;mara a OneDrive, luego importa a Lightroom Classic."),
                ("Usa el ajuste de 12:","en el m&oacute;dulo Print, elige el ajuste de hoja de contactos de 12 (lo instalaste en Serie de Im&aacute;genes)."),
                ("Imprime a JPG:","usa Print to File para que se guarde como un JPG de alta resoluci&oacute;n, luego s&uacute;belo aqu&iacute;."),
            ])
            + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n."))
        es+=next_up("SIGUIENTE &middot; PASO 03 - Edita y Entrega",("Revela cada foto, ajusta tu preset, recorta y entrega una hoja de 6 m&aacute;s seis JPG editados." if RAW else "Elige tu mejor foto en cada n&uacute;mero f, recorta y entrega una hoja de 6 m&aacute;s seis JPG finales."))

        stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Step 01</a> <a href="{S2}" class="silva-step-btn">Step 03 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S2}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
        return wrap_page(f"Step 2: Capture and Contact Sheet | Exposure Balance | {LABEL} | PVHS", nav("Step 02",dots_for(1),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 03: Edit & Submit =================
    def step_edit():
        en=banner(f"Module {MOD} &bull; Step 03","Edit &amp; Submit",("Develop each photo, fine-tune your preset, crop, and turn in a 6-Up plus six edited JPGs." if RAW else "Pick your best one at each f-stop, crop, and turn in a 6-Up plus six final JPGs."),"#espanol","Clic para Espa&ntilde;ol", HICON_PHOTO_WALK)
        en+=type_card("edit","Step 03 &middot; Select","Choose Your Six Finals",
            para("Look through your take and choose your <strong>six strongest photos, one at each f-stop</strong>. Each final must be a different f-stop, from f/22 to f/1.8, and each must be properly exposed. Keeping one at each f-stop shows the full range and sets up your reflection.")
            + bullets([
                ("One per f-stop:","your best photo at each of your six f-stops. Six finals, six different f-stops."),
                ("Properly exposed:","keep the ones that are balanced, not too dark and not too bright."),
                ("Sharp where it counts:","the part of the subject you focused on should be sharp."),
            ])
            + note("Call these your final selections, not &ldquo;picks.&rdquo; Choose on purpose."))
        en+=deliverables_box(False,
            [("1 contact sheet:",("a 6-Up contact sheet with your six edited images loaded, as a high-resolution JPG." if RAW else "a 6-Up contact sheet with your six final images loaded, as a high-resolution JPG.")),
             (("6 edited photos:" if RAW else "6 final photos:"),("your six developed finals, one per f-stop, exported individually as high-resolution JPGs." if RAW else "your six selections, one per f-stop, exported individually as high-resolution JPGs.")),
             ("7 files total:",("the 6-Up contact sheet plus the six edited JPGs." if RAW else "the 6-Up contact sheet plus the six final JPGs."))])
        if RAW:
            en+=card("FULL EDIT / DEVELOP, PRESET &amp; CROP","Develop Each RAW File",
                para("This is a RAW capture, so you develop each photo in the Lightroom <strong>Develop</strong> module. Make a detailed, thorough edit: set the white balance, exposure, contrast, highlights and shadows, and color until each photo looks its best.")
                + bullets([
                    ("Develop fully:","adjust white balance, exposure, contrast, tone, and color. Bring out the detail that RAW gives you."),
                    ("Use and fine-tune your preset:","apply the preset you built earlier, then fine-tune it for this set. Keep exploring: adjust the settings and update your preset as you improve it."),
                    ("Crop for the frame:","straighten and tidy the edges so each photo reads clean."),
                    ("Keep the set consistent:","aim for a matching look across all six so the f-stop range is easy to compare."),
                ]))
        else:
            en+=card("LIGHT EDIT / CROP ONLY","Get It Right in Camera, Then Crop",
                para("This is a JPG capture, so you got your exposure right in the camera. The only edit you need is a <strong>crop</strong>: tidy the framing so each photo reads clean.")
                + bullets([
                    ("Crop for the frame:","straighten and tidy the edges. Keep the same look across all six so the range is easy to compare."),
                    ("Do not over-edit:","no heavy color or filters. The photo should already look good out of the camera."),
                ]))
        en+=card("BUILD IT / CONTACT SHEET + EXPORTS","Turn In a 6-Up Plus Six JPGs",
            steps([
                ("Load your 6 finals:","in Lightroom Classic, select your six final photos, one at each f-stop."),
                ("Build the 6-Up:","in the Print module, use the 6-Up contact sheet preset with your six finals loaded, and print it to a high-resolution JPG."),
                ("Export the 6 JPGs:","go to File &rsaquo; Export and export your six finals as high-resolution JPGs into your project folder."),
                ("Upload 7 files:","turn in the 6-Up contact sheet plus the six final JPGs."),
            ])
            + note("Contact sheets are always turned in as a high-resolution JPG."))
        en+=next_up("UP NEXT &middot; STEP 04 - Reflection","Tell what you learned about balancing your exposure across the range.")

        es=banner(f"M&oacute;dulo {MOD} &bull; Paso 03","Edita y Entrega",("Revela cada foto, ajusta tu preset, recorta y entrega una hoja de 6 m&aacute;s seis JPG editados." if RAW else "Elige tu mejor foto en cada n&uacute;mero f, recorta y entrega una hoja de 6 m&aacute;s seis JPG finales."),"#top","Back to English", HICON_PHOTO_WALK)
        es+=type_card("edit","Paso 03 &middot; Selecciona","Elige Tus Seis Finales",
            para("Revisa tu trabajo y elige tus <strong>seis fotos m&aacute;s fuertes, una en cada n&uacute;mero f</strong>. Cada final debe ser un n&uacute;mero f distinto, de f/22 a f/1.8, y cada una bien expuesta. Guardar una en cada n&uacute;mero f muestra todo el rango y prepara tu reflexi&oacute;n.")
            + bullets([
                ("Una por n&uacute;mero f:","tu mejor foto en cada uno de tus seis n&uacute;meros f. Seis finales, seis n&uacute;meros f distintos."),
                ("Bien expuestas:","guarda las que est&eacute;n equilibradas, ni muy oscuras ni muy brillantes."),
                ("N&iacute;tida donde importa:","la parte del sujeto que enfocaste debe estar n&iacute;tida."),
            ])
            + note("Llama a estas tus selecciones finales. Elige a prop&oacute;sito."))
        es+=deliverables_box(True,
            [("1 hoja de contactos:",("una hoja de contactos de 6 con tus seis im&aacute;genes editadas cargadas, como un JPG de alta resoluci&oacute;n." if RAW else "una hoja de contactos de 6 con tus seis im&aacute;genes finales cargadas, como un JPG de alta resoluci&oacute;n.")),
             (("6 fotos editadas:" if RAW else "6 fotos finales:"),("tus seis finales reveladas, una por n&uacute;mero f, exportadas por separado como JPG de alta resoluci&oacute;n." if RAW else "tus seis selecciones, una por n&uacute;mero f, exportadas por separado como JPG de alta resoluci&oacute;n.")),
             ("7 archivos en total:",("la hoja de contactos de 6 m&aacute;s las seis im&aacute;genes editadas en JPG." if RAW else "la hoja de contactos de 6 m&aacute;s las seis im&aacute;genes finales en JPG."))])
        if RAW:
            es+=card("EDICI&Oacute;N COMPLETA / REVELA, PRESET Y RECORTE","Revela Cada Archivo RAW",
                para("Esta es una captura en RAW, as&iacute; que revelas cada foto en el m&oacute;dulo <strong>Develop</strong> de Lightroom. Haz una edici&oacute;n detallada y completa: ajusta el balance de blancos, la exposici&oacute;n, el contraste, las luces y sombras, y el color hasta que cada foto se vea lo mejor posible.")
                + bullets([
                    ("Revela por completo:","ajusta el balance de blancos, la exposici&oacute;n, el contraste, el tono y el color. Saca el detalle que te da el RAW."),
                    ("Usa y ajusta tu preset:","aplica el preset que creaste antes, luego aj&uacute;stalo para este set. Sigue explorando: modifica los ajustes y actualiza tu preset conforme lo mejoras."),
                    ("Recorta el encuadre:","endereza y ordena los bordes para que cada foto se vea limpia."),
                    ("Mant&eacute;n el set consistente:","busca un estilo que combine en las seis para que el rango de n&uacute;meros f sea f&aacute;cil de comparar."),
                ]))
        else:
            es+=card("EDICI&Oacute;N LIGERA / SOLO RECORTE","Deja Bien la C&aacute;mara, Luego Recorta",
                para("Esta es una captura en JPG, as&iacute; que dejaste bien tu exposici&oacute;n en la c&aacute;mara. La &uacute;nica edici&oacute;n que necesitas es un <strong>recorte</strong>: ordena el encuadre para que cada foto se vea limpia.")
                + bullets([
                    ("Recorta el encuadre:","endereza y ordena los bordes. Mant&eacute;n el mismo estilo en las seis para que el rango sea f&aacute;cil de comparar."),
                    ("No edites de m&aacute;s:","sin color pesado ni filtros. La foto ya debe verse bien tal como sale de la c&aacute;mara."),
                ]))
        es+=card("&Aacute;RMALA / HOJA DE CONTACTOS + EXPORTES","Entrega una Hoja de 6 M&aacute;s Seis JPG",
            steps([
                ("Carga tus 6 finales:","en Lightroom Classic, selecciona tus seis fotos finales, una en cada n&uacute;mero f."),
                ("Arma la hoja de 6:","en el m&oacute;dulo Print, usa el ajuste de hoja de contactos de 6 con tus seis finales cargadas, e impr&iacute;mela como un JPG de alta resoluci&oacute;n."),
                ("Exporta los 6 JPG:","ve a File &rsaquo; Export y exporta tus seis finales como JPG de alta resoluci&oacute;n a la carpeta de tu proyecto."),
                ("Sube 7 archivos:","entrega la hoja de contactos de 6 m&aacute;s los seis JPG finales."),
            ])
            + note("Las hojas de contactos siempre se entregan como un JPG de alta resoluci&oacute;n."))
        es+=next_up("SIGUIENTE &middot; PASO 04 - Reflexi&oacute;n","Cuenta qu&eacute; aprendiste sobre equilibrar tu exposici&oacute;n en el rango.")

        stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 02</a> <a href="{S3}" class="silva-step-btn">Step 04 &#8594;</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S3}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
        return wrap_page(f"Step 3: Edit and Submit | Exposure Balance | {LABEL} | PVHS", nav("Step 03",dots_for(2),stepnav), top_wrap(en,es), bottom)

    # ================= STEP 04: Reflection =================
    def step_reflect():
        en=banner(f"Module {MOD} &bull; Step 04","Reflection","Tell what you learned about balancing your exposure.","#espanol","Clic para Espa&ntilde;ol", HICON_REFLECT)
        en+=card("STEP 04 / REFLECT","Complete and Upload the Reflection",
            para("Finish with a short reflection. It asks how you balanced your exposure across the range, what was hardest, and which f-stop look you liked best.")
            + note("The reflection document is on Step 01 (the Overview), the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
            + bullets([
                ("Balancing your exposure:","tell how you used your shutter and ISO to keep the light meter between -1 and +1 at each f-stop."),
                ("Keeping ISO low:","when did you have to raise your ISO, and why? When could you keep it at its lowest?"),
                ("Your favorite look:","which f-stop gave you the look you liked best, and why? Think about depth of field."),
            ])
            + note("Answer honestly, in your own words, in full sentences."))
        en+=deliverables_box(False,
            [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
        en+=next_up("MODULE COMPLETE","Great work. You balanced the exposure triangle across the whole aperture range, from f/22 to f/1.8.")

        es=banner(f"M&oacute;dulo {MOD} &bull; Paso 04","Reflexi&oacute;n","Cuenta qu&eacute; aprendiste sobre equilibrar tu exposici&oacute;n.","#top","Back to English", HICON_REFLECT)
        es+=card("PASO 04 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
            para("Termina con una reflexi&oacute;n corta. Te pregunta c&oacute;mo equilibraste tu exposici&oacute;n en el rango, qu&eacute; fue lo m&aacute;s dif&iacute;cil y qu&eacute; estilo de n&uacute;mero f te gust&oacute; m&aacute;s.")
            + note("El documento de reflexi&oacute;n est&aacute; en el Paso 01 (el Resumen), la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
            + bullets([
                ("Equilibrar tu exposici&oacute;n:","cuenta c&oacute;mo usaste el obturador y el ISO para mantener el expos&iacute;metro entre -1 y +1 en cada n&uacute;mero f."),
                ("Mantener el ISO bajo:","&iquest;cu&aacute;ndo tuviste que subir el ISO y por qu&eacute;? &iquest;Cu&aacute;ndo pudiste dejarlo en lo m&aacute;s bajo?"),
                ("Tu estilo favorito:","&iquest;qu&eacute; n&uacute;mero f te dio el estilo que m&aacute;s te gust&oacute; y por qu&eacute;? Piensa en la profundidad de campo."),
            ])
            + note("Contesta con honestidad, en tus propias palabras, en oraciones completas."))
        es+=deliverables_box(True,
            [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completado, subido a esta tarea de Canvas.")])
        es+=next_up("M&Oacute;DULO COMPLETO","Buen trabajo. Equilibraste el tri&aacute;ngulo de exposici&oacute;n en todo el rango de apertura, de f/22 a f/1.8.")

        stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 03</a>'
        bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 03</a><span></span></div>'
        return wrap_page(f"Step 4: Reflection | Exposure Balance | {LABEL} | PVHS", nav("Step 04",dots_for(3),stepnav), top_wrap(en,es), bottom)

    for fname,gen in [(OVER,overview),(S1,step_capture),(S2,step_edit),(S3,step_reflect)]:
        html=ent(gen())
        assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
        assert "–" not in html and "&ndash;" not in html, "en dash in "+fname
        low=html.lower()
        for allow in ["shooting tab","shooting menu"]:
            low=low.replace(allow,"")
        for w in ["shoot","shooting","shot","shots","shoots","screenshot"]:
            assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
        open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
        print("wrote", fname, len(html), "bytes")

for C in COURSES:
    build_course(C)
