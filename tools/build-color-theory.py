#!/usr/bin/env python3
# Digital Arts 1A - Module: Color Theory.
# Learn how color builds a brand in class (12 slides), then study one real brand for homework
# (Brand Color Analysis worksheet). No camera, no own-device capture, so no fresh-photos note
# and no header module-type icon. Chip-header framework via silva_framework.
# Overview + 1 step, bilingual EN/ES, 5th-grade. Regenerates the two hand-authored pages in place.
import os
from silva_framework import *

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/digarts1/color-theory"
HERO=f"{IMG}/color-theory-header-v1.png"
COLOR_WHEEL=f"{IMG}/color-wheel.png"
WORKSHEET_EN=f"{SITE}/assets/course-documents/Color-Analysis-Worksheet-EN.docx"
WORKSHEET_ES=f"{SITE}/assets/course-documents/Color-Analysis-Worksheet-ES.docx"
AREA="Digital Arts Folder"

OVER="digarts1-color-theory-overview.html"
S1="digarts1-color-theory-step01-analysis.html"

# ---- module-local helpers (no framework equivalent) ----
def orange_note(t):
    # ORANGE note box, cohesive INSIDE the orange Downloads section. (Framework note_orange is
    # reserved for the own-device fresh-photos notice, so keep a local orange note here.)
    return ('<div style="background:rgba(255,107,26,0.10);border:1px solid rgba(255,107,26,0.30);border-left:4px solid #FF6B1A;'
      f'padding:11px 14px;margin:0 0 16px;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def downloads_block(es):
    # Orange Downloads section (Overview only). Color Theory holds the Brand Color Analysis worksheet.
    heading="Descarga Tus Archivos" if es else "Download Your Files"
    body=("Despu&eacute;s de las diapositivas, tu tarea es un An&aacute;lisis de Color de una Marca. Eliges un negocio muy conocido y estudias c&oacute;mo usa el color en cada punto de contacto con el cliente: logo, tienda, empaque y ropa de los empleados. Llenas la hoja de trabajo y agregas im&aacute;genes de ejemplo. La pr&oacute;xima clase compartimos y discutimos." if es
          else "After the slides, your homework is a Brand Color Analysis. You pick one well-known business and study how it uses color at every customer touchpoint: logo, storefront, packaging, and employee outfits. You fill out the worksheet and add example images. Next class, we share and discuss.")
    notetxt=("Todos los archivos que necesitas est&aacute;n aqu&iacute; en esta p&aacute;gina de Resumen. Descarga la hoja de trabajo de abajo para empezar." if es
             else "All the files you need are right here on this Overview page. Download the worksheet below to start.")
    reflabel="Hoja de An&aacute;lisis de Color (Word)" if es else "Color Analysis Worksheet (Word)"
    ref=WORKSHEET_ES if es else WORKSHEET_EN
    return ('<div style="background:linear-gradient(180deg,rgba(255,107,26,0.12) 0%,rgba(255,107,26,0.03) 100%);border:1px solid rgba(255,107,26,0.30);border-left:6px solid #FF6B1A;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      + section_header(DL_ICON, heading, "#FF6B1A", "#ffb27c")
      + para(body)
      + orange_note(notetxt)
      + '<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;">'
      + dl_link(ref,reflabel,row=True)
      + '</div>'
      + folder_note(es, AREA) + '</div>')

def slides_section(es):
    # PURPLE Resources section: the 12 class slides in a contained scroll panel. Slide frames and the
    # scroll hint are recolored to purple so the whole section is cohesive (was teal in the old page).
    folder="slides-es" if es else "slides-en"
    prefix="es" if es else "en"
    heading="Las Diapositivas de Hoy" if es else "Today&rsquo;s Slides"
    body=("Vemos estas diapositivas juntos en clase. Las 12 diapositivas est&aacute;n abajo." if es
          else "We go through these slides together in class. All 12 slides are below.")
    hint="Desliza por las 12 diapositivas &darr;" if es else "Scroll through all 12 slides &darr;"
    altf=(lambda n: f"Diapositiva {n}") if es else (lambda n: f"Color Theory slide {n}")
    frames=""
    for n in range(1,13):
        src=f"{IMG}/{folder}/color-theory-{prefix}-slide-{n:02d}-v2.jpg"
        mb="0" if n==12 else "12px"
        frames+=(f'<div style="background:linear-gradient(135deg,#8b5cf6 0%,rgba(139,92,246,0.08) 100%);padding:2px;margin:0 0 {mb};">'
          f'<img src="{src}" alt="{altf(n)}" style="display:block;width:100%;height:auto;" /></div>')
    hintline=f'<div style="font-size:11pt;color:#c4b5fd;letter-spacing:0.04em;margin:0 0 10px;"><strong>{hint}</strong></div>'
    panel=('<div class="silva-scroll" style="max-height:520px;overflow-y:auto;-webkit-overflow-scrolling:touch;'
      'border:1px solid rgba(139,92,246,0.28);background:rgba(0,0,0,0.22);padding:12px;box-sizing:border-box;">'
      + frames + '</div>')
    return resources_card(heading, para(body) + hintline + panel, es)

def business_grid(names):
    # Teal chip grid of business choices (cohesive inside the teal content card). 4 per row.
    def cell(name):
        return ('<td style="width:25%;vertical-align:top;padding:6px;">'
          '<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;height:100%;box-sizing:border-box;">'
          '<div style="background:linear-gradient(135deg,#094043 0,#094043 20px,#041d1c 20px,#041d1c 100%);padding:14px 12px;height:100%;box-sizing:border-box;text-align:center;">'
          f'<span style="font-size:12pt;color:#ffffff;"><strong>{name}</strong></span></div></div></td>')
    rows=""
    for i in range(0,len(names),4):
        rows+='<tr>'+''.join(cell(n) for n in names[i:i+4])+'</tr>'
    return '<table role="presentation" style="width:100%;border-collapse:collapse;table-layout:fixed;"><tbody>'+rows+'</tbody></table>'

BUSINESSES=["Chick-fil-A","Target","In-N-Out Burger","McDonald&rsquo;s","Coca-Cola","Nike","Apple","Dutch Bros"]

EN_TERMS=[
  ("Color Theory","How colors work together and how they make people feel. Designers use it to choose colors on purpose, not by luck."),
  ("Hue","The name of a color, like red, blue, or green. It is the pure color before you make it lighter or darker."),
  ("Value","How light or dark a color is. Adding white makes it lighter; adding black makes it darker."),
  ("Color Palette","The small set of colors a brand or artist chooses to use together. A small set keeps the look clean."),
  ("Complementary Colors","Two colors across from each other on the color wheel, like blue and orange. Side by side they pop."),
  ("Brand Identity","The look and feel of a company: its colors, logo, and style. Strong brands keep it the same everywhere.")]

ES_TERMS=[
  ("Teor&iacute;a del Color","C&oacute;mo los colores funcionan juntos y c&oacute;mo hacen sentir a la gente. Los dise&ntilde;adores la usan para elegir colores a prop&oacute;sito."),
  ("Matiz (Hue)","El nombre de un color, como rojo, azul o verde. Es el color puro antes de hacerlo m&aacute;s claro o m&aacute;s oscuro."),
  ("Valor","Qu&eacute; tan claro u oscuro es un color. Agregar blanco lo aclara; agregar negro lo oscurece."),
  ("Paleta de Colores","El grupo peque&ntilde;o de colores que una marca o artista elige usar junto. Un grupo peque&ntilde;o mantiene el aspecto limpio."),
  ("Colores Complementarios","Dos colores opuestos en la rueda de color, como el azul y el naranja. Juntos resaltan."),
  ("Identidad de Marca","El aspecto y la sensaci&oacute;n de una empresa: sus colores, logo y estilo. Las marcas fuertes lo mantienen igual en todas partes.")]

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Color Theory</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Digital Arts 1A &bull; Color Theory","Color Theory","How color builds a brand.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Color Theory: The Look of a Brand",
        para("Color theory is how colors work together and how they make people feel. Big brands pick a small set of colors and use them everywhere: the logo, the store, the packaging, even the staff shirts. When the colors match at every step, the brand feels strong and easy to remember. Today we learn the basics, then you study a real brand.")
        + framed(HERO,"Color Theory"))
    en+=downloads_block(False)
    en+=slides_section(False)
    en+=card("","Example: Starbucks",
        para("Look at Starbucks. It uses one clear color theme in every place you see it. The green-and-white logo, the store signs, the cups and bags, and the green aprons the workers wear all match. That is not by accident. The same colors show up at every customer touchpoint, so you know it is Starbucks before you even read the name. That is the power of a cohesive color theme."))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz","Heads up: these key words will be on the quiz.", EN_TERMS), False)

    es=banner("Arte Digital 1A &bull; Teor&iacute;a del Color","Teor&iacute;a del Color","C&oacute;mo el color crea una marca.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","Teor&iacute;a del Color: El Aspecto de una Marca",
        para("La teor&iacute;a del color es c&oacute;mo los colores funcionan juntos y c&oacute;mo hacen sentir a la gente. Las marcas grandes eligen un grupo peque&ntilde;o de colores y los usan en todo: el logo, la tienda, el empaque y hasta las camisas del personal. Cuando los colores combinan en cada paso, la marca se siente fuerte y f&aacute;cil de recordar. Hoy aprendemos lo b&aacute;sico, y luego estudias una marca real.")
        + framed(HERO,"Teor&iacute;a del Color"))
    es+=downloads_block(True)
    es+=slides_section(True)
    es+=card("","Ejemplo: Starbucks",
        para("Mira a Starbucks. Usa un mismo tema de color en cada lugar donde lo ves. El logo verde y blanco, los letreros de la tienda, los vasos y las bolsas, y los delantales verdes que usan los trabajadores, todo combina. Eso no es por casualidad. Los mismos colores aparecen en cada punto de contacto con el cliente, as&iacute; sabes que es Starbucks antes de leer el nombre. Ese es el poder de un tema de color coherente."))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen","Atenci&oacute;n: estas palabras clave estar&aacute;n en el examen.", ES_TERMS), True)

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Color Theory | Digital Arts 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Digital Arts 1A &bull; Color Theory","Color Theory","Homework: study a real brand.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("Your finished Brand Color Analysis worksheet","with your example images added (Word document, .docx), uploaded to this Canvas assignment.")])
    en+=card("","Brand Color Analysis",
        float_right(COLOR_WHEEL,"Color wheel with primary, secondary, and tertiary colors","")
        + para("Your job is to pick one well-known business and show how it uses color to build a strong, cohesive brand. Look at every customer touchpoint, name the colors you see, and explain why they work together. Then fill out the worksheet and add your example images."))
    en+=card("","Pick One Business",
        para("Choose one business from the list below. Pick one you can find lots of clear photos of. We studied Starbucks together in class, so pick a different one for your project.")
        + business_grid(BUSINESSES))
    en+=card("","What to Show in Your Analysis",
        para("For your business, find and add an example image of each of these four customer touchpoints. Under each one, name the main colors and say how they match the brand.")
        + bullets([
            ("Logo:","the brand mark and its main colors."),
            ("Storefront:","the building, the sign, or the website look."),
            ("Packaging:","bags, boxes, cups, or labels."),
            ("Employee Outfits:","uniforms, aprons, or shirts the workers wear."),
        ])
        + para("Then answer these questions: What are the 3 to 5 main brand colors? Why do you think they chose them? How does the color theme make you feel? Is the color the same at every touchpoint?")
        + note("Download the worksheet from this module&rsquo;s Overview page (marked M at the top), fill it in, and add your images."))
    en+=card("","Turn It In",
        para("Finish the worksheet, add your example images, and upload it to Canvas. Next class we share our brands and talk about what makes each color theme work.")
        + note("Looking for the worksheet? It is on this module&rsquo;s Overview page, marked M at the top, not here. Open it to download the Word document."))

    es=banner("Arte Digital 1A &bull; Teor&iacute;a del Color","Teor&iacute;a del Color","Tarea: estudia una marca real.","#top","Back to English")
    es+=deliverables_box(True,
        [("Tu hoja de trabajo de An&aacute;lisis de Color de Marca terminada","con tus im&aacute;genes de ejemplo agregadas (documento de Word, .docx), subida a esta tarea de Canvas.")])
    es+=card("","An&aacute;lisis de Color de una Marca",
        float_right(COLOR_WHEEL,"Rueda de color con colores primarios, secundarios y terciarios","")
        + para("Tu trabajo es elegir un negocio muy conocido y mostrar c&oacute;mo usa el color para crear una marca fuerte y coherente. Mira cada punto de contacto con el cliente, nombra los colores que ves y explica por qu&eacute; funcionan juntos. Luego llena la hoja de trabajo y agrega tus im&aacute;genes de ejemplo."))
    es+=card("","Elige Un Negocio",
        para("Elige un negocio de la lista de abajo. Elige uno del que puedas encontrar muchas fotos claras. Estudiamos Starbucks juntos en clase, as&iacute; que elige uno diferente para tu proyecto.")
        + business_grid(BUSINESSES))
    es+=card("","Qu&eacute; Mostrar en Tu An&aacute;lisis",
        para("Para tu negocio, busca y agrega una imagen de ejemplo de cada uno de estos cuatro puntos de contacto con el cliente. Debajo de cada uno, nombra los colores principales y di c&oacute;mo combinan con la marca.")
        + bullets([
            ("Logo:","el s&iacute;mbolo de la marca y sus colores principales."),
            ("Tienda:","el edificio, el letrero o el aspecto del sitio web."),
            ("Empaque:","bolsas, cajas, vasos o etiquetas."),
            ("Ropa de los Empleados:","uniformes, delantales o camisas que usan los trabajadores."),
        ])
        + para("Luego responde estas preguntas: &iquest;Cu&aacute;les son los 3 a 5 colores principales de la marca? &iquest;Por qu&eacute; crees que los eligieron? &iquest;C&oacute;mo te hace sentir el tema de color? &iquest;Es el color igual en cada punto de contacto?")
        + note("Descarga la hoja de trabajo desde la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba), ll&eacute;nala y agrega tus im&aacute;genes."))
    es+=card("","Entr&eacute;galo",
        para("Termina la hoja de trabajo, agrega tus im&aacute;genes de ejemplo y s&uacute;bela a Canvas. La pr&oacute;xima clase compartimos nuestras marcas y hablamos de qu&eacute; hace funcionar cada tema de color.")
        + note("&iquest;Buscas la hoja de trabajo? Est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, marcada con M arriba, no aqu&iacute;. &Aacute;brela para descargar el documento de Word."))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><span></span></div>'
    return wrap_page("Color Theory: Homework | Digital Arts 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
