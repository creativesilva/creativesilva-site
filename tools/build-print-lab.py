#!/usr/bin/env python3
# PRINT LAB - a single-page, NOT-graded, reusable print-queue assignment.
# Students upload up to 3 high-resolution JPGs of their best work to the Canvas assignment
# (the submission list IS the print queue). Mr. Silva prints them 11 x 17 to take home.
# Before uploading, students crop each photo to the 11 x 17 shape in Lightroom Classic or
# Photoshop (verified Adobe steps, Mac-only). Bilingual EN/ES, 5th-grade, dark angular framework.
#
# REOPEN ANYTIME: change the three dates in the PRINT WINDOW block below and rerun. Nothing else.
# Classes: Photography 1, Photography 2, Digital Arts 1 (Mr. Silva voice). NOT graded.
# Hard rules honored: no em dashes; no banned violence words (crop/photo/image, never "shot/shoot");
# smart quotes as entities; assets on www.creativesilva.com; Mac-only how-to.
import os
from silva_framework import *      # banner, card, para, bullets, steps, note, section_header, top_wrap, wrap_page, dot, ban_check, SITE
import silva_framework as _sf

ROOT = "/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
OUT  = os.path.join(ROOT, "curriculum/shared/print-lab.html")
DELIVER_ICON = f"{SITE}/assets/Icons/assignment/deliverables-v4.png"
# 21:9 header/hero (Chris's "Print your work header v3": two students reviewing big prints by the
# wide-format printer in the photo lab). Shared page, so one hero for Photo 1 + Photo 2 + Digital Arts.
HERO = f"{SITE}/assets/images/print-lab/print-lab-hero-v1.jpg"
HAVE_HERO = True

# ============================================================================
# PRINT WINDOW  --  the ONLY thing to edit when you reopen Print Lab.
# Change these three dates (English + Spanish), then rerun the builder. Done.
# ============================================================================
OPEN_EN,  OPEN_ES  = "Tuesday, November 17",  "martes 17 de noviembre"
CLOSE_EN, CLOSE_ES = "Thursday, November 19",  "jueves 19 de noviembre"
READY_EN, READY_ES = "Friday, November 20",    "viernes 20 de noviembre"
# ============================================================================

# ---- small local helpers (single-page chrome) ----
def subhead(t):
    return (f'<div style="font-size:12.5pt;color:#80e0e0;letter-spacing:0.08em;text-transform:uppercase;'
            f'margin:18px 0 8px;"><strong>{t}</strong></div>')

def scroller(inner):
    # Compact VERTICAL scroller: a short fixed-height box so the steps scroll inside it and the
    # page stays short. Inline overflow survives Canvas (classes are stripped); the silva-scroll
    # class only prettifies the scrollbar on the live/linked page.
    return ('<div class="silva-scroll" style="max-height:270px;overflow-y:auto;overflow-x:hidden;padding:14px 16px 18px;'
            'border:1px solid rgba(0,184,184,0.30);background:linear-gradient(180deg,rgba(0,116,116,0.10) 0%,rgba(0,116,116,0.03) 100%);'
            'margin:4px 0 10px;box-sizing:border-box;">' + inner + '</div>')

def window_box(open_d, close_d, ready_d, es=False):
    ey   = "Ventana de Impresi&oacute;n" if es else "Print Window"
    L    = (("Abre","La cola cierra","Listas para recoger") if es
            else ("Opens","Print queue closes","Prints ready"))
    SUB  = (("","&uacute;ltimo d&iacute;a para subir tus fotos","recoge con el Sr. Silva") if es
            else ("","last day to upload your photos","pick up from Mr. Silva"))
    def row(label, date, sub, strong=False):
        datesz = "16pt" if strong else "14pt"
        subdiv = (f'<div style="font-size:11pt;color:rgba(255,255,255,0.72);margin-top:2px;">{sub}</div>' if sub else '')
        return ('<div style="padding:11px 0;border-top:1px solid rgba(0,184,184,0.18);">'
                '<div style="display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 14px;">'
                f'<span style="flex:0 0 auto;min-width:168px;font-size:10.5pt;letter-spacing:0.12em;text-transform:uppercase;color:#80e0e0;"><strong>{label}</strong></span>'
                f'<span style="font-size:{datesz};color:#ffffff;"><strong>{date}</strong></span></div>'
                f'{subdiv}</div>')
    rows = (row(L[0], open_d, SUB[0])
          + row(L[1], close_d, SUB[1], strong=True)
          + row(L[2], ready_d, SUB[2]))
    return ('<div style="background:linear-gradient(180deg,rgba(0,116,116,0.16) 0%,rgba(0,116,116,0.05) 100%);'
            'border:1px solid rgba(0,184,184,0.35);border-left:6px solid #00b8b8;padding:20px 26px 10px;margin-bottom:24px;overflow:hidden;">'
            f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:4px;"><strong>{ey}</strong></div>'
            f'{rows}</div>')

def submit_box(close_d, es=False):
    title = ("ENV&Iacute;A &middot; COLA DE IMPRESI&Oacute;N" if es else "SUBMIT &middot; PRINT QUEUE")
    lead  = ("As&iacute; entras a la cola de impresi&oacute;n. Esto no tiene calificaci&oacute;n. Es solo para que se impriman tus fotos."
             if es else
             "This is how you get into the print queue. It is not graded. It is just to get your prints made.")
    if es:
        items = [
          ("Sube hasta 3 fotos", "en JPG de alta resoluci&oacute;n a esta tarea de Canvas."),
          ("Recorta cada foto a 11 x 17", "primero (mira los pasos abajo)."),
          ("Guarda cada una como JPG de alta resoluci&oacute;n,", "300 DPI (como 3300 x 5100 p&iacute;xeles)."),
          ("Sube antes de que cierre la cola:", f"{close_d}."),
        ]
    else:
        items = [
          ("Upload up to 3 photos", "as high-resolution JPGs to this Canvas assignment."),
          ("Crop each photo to 11 x 17", "first (see the steps below)."),
          ("Save each one as a high-resolution JPG,", "300 DPI (about 3300 x 5100 pixels)."),
          ("Upload before the queue closes:", f"{close_d}."),
        ]
    lis = ""
    for b, rest in items:
        lis += ('<div style="margin-bottom:6px;line-height:1.5;"><span style="color:#f5b301;">&bull;</span> '
                f'<span style="font-size:13pt;color:rgba(255,255,255,0.90);"><strong>{b}</strong> {rest}</span></div>')
    return ('<div style="background:linear-gradient(180deg,rgba(245,179,1,0.12) 0%,rgba(245,179,1,0.03) 100%);'
            'border:1px solid rgba(245,179,1,0.35);border-left:6px solid #f5b301;padding:30px;overflow:hidden;margin-bottom:24px;">'
            + section_header(DELIVER_ICON, title, "#f5b301", "#ffd166")
            + f'<div style="font-size:13pt;color:#ffffff;margin-bottom:10px;line-height:1.5;">{lead}</div>{lis}</div>')

# ---- crop how-to (verified Adobe steps, Mac-only) ----
def crop_card(es=False):
    if es:
        intro = (para("Antes de subir, recorta cada foto a la forma de 11 por 17 para que llene la impresi&oacute;n. "
                      "H&aacute;zlo en una Mac de la clase con <strong>Lightroom Classic</strong> o <strong>Photoshop</strong>. Usa el que ya conoces.")
                 + note("&iquest;Foto vertical? Usa <strong>11 x 17</strong>. &iquest;Foto horizontal? Usa <strong>17 x 11</strong>. "
                        "Recorta para que tu mejor parte quede dentro del recuadro."))
        lr = steps([
          ("", "Abre tu foto y ve al m&oacute;dulo <strong>Revelar (Develop).</strong>"),
          ("", "Presiona <strong>R</strong> para abrir la herramienta Recortar."),
          ("", "Abre el men&uacute; <strong>Proporci&oacute;n (Aspect)</strong> y elige <strong>Introducir personalizada (Enter Custom).</strong>"),
          ("", "Escribe <strong>11 x 17</strong> para una foto vertical, o <strong>17 x 11</strong> para una horizontal. Presiona <strong>X</strong> para voltear vertical u horizontal."),
          ("", "Arrastra la foto dentro del recuadro para que se vea tu mejor parte."),
          ("", "Presiona <strong>R</strong> otra vez para fijar el recorte."),
          ("", "Ve a <strong>Archivo &rarr; Exportar.</strong> Elige <strong>JPEG</strong>, Calidad <strong>100</strong>, Resoluci&oacute;n <strong>300</strong> p&iacute;xeles por pulgada. Haz clic en Exportar."),
          ("", "Sube ese JPG a esta tarea de Canvas."),
        ])
        ps = steps([
          ("", "Abre tu foto en Photoshop."),
          ("", "Presiona <strong>C</strong> para la herramienta Recortar."),
          ("", "En la barra de arriba, abre el men&uacute; que dice <strong>Proporci&oacute;n (Ratio)</strong> y elige <strong>An x Al x Resoluci&oacute;n (W x H x Resolution).</strong>"),
          ("", "Escribe <strong>11 in</strong>, <strong>17 in</strong> y <strong>300 px/in</strong> para una foto vertical (o <strong>17 in</strong>, <strong>11 in</strong> para una horizontal)."),
          ("", "Arrastra el recuadro para que se vea tu mejor parte."),
          ("", "Presiona <strong>Return</strong> para recortar."),
          ("", "Ve a <strong>Archivo &rarr; Guardar una copia (Save a Copy).</strong> Elige <strong>JPG</strong> y la calidad m&aacute;s alta. Guarda."),
          ("", "Sube ese JPG a esta tarea de Canvas."),
        ])
        inner = (intro + subhead("En Lightroom Classic") + scroller(lr)
                 + subhead("En Photoshop") + scroller(ps))
        return card("Recorta", "Recorta a 11 x 17", inner)
    intro = (para("Before you upload, crop each photo to the 11 by 17 shape so it fills the print. "
                  "Do this on a class Mac in <strong>Lightroom Classic</strong> or <strong>Photoshop</strong>. Use the one you know.")
             + note("Tall photo? Use <strong>11 x 17</strong>. Wide photo? Use <strong>17 x 11</strong>. "
                    "Crop so your best part fits inside the box."))
    lr = steps([
      ("", "Open your photo and go to the <strong>Develop</strong> module."),
      ("", "Press <strong>R</strong> to open the Crop tool."),
      ("", "Open the <strong>Aspect</strong> menu (it says &#x201C;Original&#x201D;) and choose <strong>Enter Custom.</strong>"),
      ("", "Type <strong>11 x 17</strong> for a tall photo, or <strong>17 x 11</strong> for a wide photo. Press <strong>X</strong> to flip tall or wide."),
      ("", "Drag the photo inside the box so your best part shows."),
      ("", "Press <strong>R</strong> again to set the crop."),
      ("", "Go to <strong>File &rarr; Export.</strong> Choose <strong>JPEG</strong>, Quality <strong>100</strong>, Resolution <strong>300</strong> pixels per inch. Click Export."),
      ("", "Upload that JPG to this Canvas assignment."),
    ])
    ps = steps([
      ("", "Open your photo in Photoshop."),
      ("", "Press <strong>C</strong> for the Crop tool."),
      ("", "In the bar at the top, open the menu that says <strong>Ratio</strong> and choose <strong>W x H x Resolution.</strong>"),
      ("", "Type <strong>11 in</strong>, <strong>17 in</strong>, and <strong>300 px/in</strong> for a tall photo (or <strong>17 in</strong>, <strong>11 in</strong> for a wide photo)."),
      ("", "Drag the box so your best part shows."),
      ("", "Press <strong>Return</strong> to crop."),
      ("", "Go to <strong>File &rarr; Save a Copy.</strong> Choose <strong>JPG</strong> and the highest quality. Save."),
      ("", "Upload that JPG to this Canvas assignment."),
    ])
    inner = (intro + subhead("In Lightroom Classic") + scroller(lr)
             + subhead("In Photoshop") + scroller(ps))
    return card("Crop", "Crop to 11 x 17", inner)

def closing(ready_d, es=False):
    if es:
        return note(f"Listas <strong>{ready_d}.</strong> Recoge con el Sr. Silva. Env&iacute;a tu mejor trabajo: al Sr. Silva le encanta ver las fotos de las que est&aacute;s orgulloso.")
    return note(f"Prints ready <strong>{ready_d}.</strong> Pick up from Mr. Silva. Send your best work. Mr. Silva loves seeing the photos you are proud of.")

def build():
    # ---------- English ----------
    en  = banner("Print Your Best Work", "Print Lab",
                 "Send your 3 best photos. Mr. Silva prints them big, 11 by 17 inches, to take home. Free. Not graded.",
                 "#espanol", "", "")
    en += card("Print Lab", "Print Your Best Work, Big",
               para("You have made photos you are proud of. Pick your best and Mr. Silva will print them big, "
                    "<strong>11 by 17 inches</strong>, for you to take home. This is <strong>free</strong> and <strong>not graded.</strong>")
             + para("Send up to <strong>three</strong> photos before the print queue closes. First crop each one to the "
                    "11 x 17 shape, then upload it here. That is it.")
             + (framed(HERO, "Two students in the photo lab looking at large printed photos next to a wide format printer") if HAVE_HERO else ""))
    en += window_box(OPEN_EN, CLOSE_EN, READY_EN, es=False)
    en += submit_box(CLOSE_EN, es=False)
    en += crop_card(es=False)
    en += closing(READY_EN, es=False)

    # ---------- Spanish ----------
    es  = banner("Imprime Tu Mejor Trabajo", "Print Lab",
                 "Env&iacute;a tus 3 mejores fotos. El Sr. Silva las imprime grandes, 11 por 17 pulgadas, para llevar a casa. Gratis. Sin calificaci&oacute;n.",
                 "#top", "", "")
    es += card("Print Lab", "Imprime Tu Mejor Trabajo, En Grande",
               para("Has hecho fotos de las que est&aacute;s orgulloso. Elige tu mejor trabajo y el Sr. Silva lo imprime grande, "
                    "<strong>11 por 17 pulgadas</strong>, para llevar a casa. Es <strong>gratis</strong> y <strong>sin calificaci&oacute;n.</strong>")
             + para("Env&iacute;a hasta <strong>tres</strong> fotos antes de que cierre la cola de impresi&oacute;n. Primero recorta cada una a la "
                    "forma de 11 x 17 y luego s&uacute;bela aqu&iacute;. Eso es todo.")
             + (framed(HERO, "Dos estudiantes en el laboratorio de foto viendo fotos impresas grandes junto a una impresora de gran formato") if HAVE_HERO else ""))
    es += window_box(OPEN_ES, CLOSE_ES, READY_ES, es=True)
    es += submit_box(CLOSE_ES, es=True)
    es += crop_card(es=True)
    es += closing(READY_ES, es=True)

    nav_inner = ('      <div class="silva-breadcrumb">\n'
                 '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
                 '        <span class="bc-sep">&rsaquo;</span>\n'
                 '        <span class="bc-current">Print Lab</span>\n'
                 '      </div>\n'
                 '      <div class="silva-nav-spacer"></div>')

    html = wrap_page("Print Lab | PVHS Photography", nav_inner, top_wrap(en, es), "")
    ban_check(html, "print-lab.html")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", OUT, os.path.getsize(html if False else OUT), "bytes")

if __name__ == "__main__":
    build()
