#!/usr/bin/env python3
# Digital Arts 1A - Module 03: Sketchbook Cover Art competition.
# Decorate the manila cover of the 8.5 by 11 sketchbook: name + period top right, 3 motivational
# words (1 in Cooper Black, 2 in Adobe Fonts typefaces), any medium. Friendly class competition.
# Chip-header framework via silva_framework. Overview + 2 steps, bilingual EN/ES, 5th-grade.
import os, re
from silva_framework import *

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMGDIR=f"{SITE}/assets/images/digarts1/sketchbook-cover"
COOPER=f"{IMGDIR}/cooper-black-example.png"
ADOBE_ICON=f"{IMGDIR}/adobe-fonts-icon.png"
HEADER_IMG=f"{IMGDIR}/sketchbook-cover-header-v2.jpg"
CHICKFILA=f"{IMGDIR}/chick-fil-a-prize.jpg"
REFLECT_TYPING=f"{IMGDIR}/reflection-typing-v3.jpg"
ADOBE_URL="https://fonts.adobe.com"
REFLECT_EN=f"{SITE}/assets/course-documents/Sketchbook-Cover-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Sketchbook-Cover-Reflection-ES.docx"
AREA="Digital Arts Folder"   # OneDrive top folder for this course's project folders

OVER="digarts1-sketchbook-cover-overview.html"
S1="digarts1-sketchbook-cover-step01-design.html"
S2="digarts1-sketchbook-cover-step02-submit-reflect.html"

# ---------------- module-specific content helpers ----------------
def datebox(label, rows_html):
    # Teal key-dates box for the competition (due date, winner date, prize).
    return ('<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.30);border-left:4px solid #00b8b8;padding:14px 16px;margin:6px 0 4px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:8px;"><strong>{label}</strong></div>'
      f'{rows_html}</div>')

def cooper_float(caption):
    # Clickable Cooper Black alphabet reference (opens full size). FLOAT-marked so the card hoists
    # it into the thumbnail column like framework float_right, but wrapped in a link.
    return ('<!--FLOAT-->'
      f'<a href="{COOPER}" target="_blank" rel="noopener" style="display:block;background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">'
      f'<img src="{COOPER}" alt="Cooper Black alphabet example" style="display:block;width:100%;height:auto;" /></a>'
      f'<div style="font-size:10.5pt;color:#80e0e0;text-align:center;margin-top:6px;opacity:0.9;line-height:1.4;">{caption}</div>'
      '<!--/FLOAT-->')

def adobe_link(label):
    # Adobe Fonts icon + link button (the only approved font site for this competition).
    return ('<div style="margin:8px 0 4px;">'
      '<span style="display:inline-flex;align-items:center;gap:12px;flex-wrap:wrap;">'
      f'<img src="{ADOBE_ICON}" alt="Adobe Fonts icon" style="width:40px;height:40px;display:block;flex:0 0 auto;" />'
      f'<a href="{ADOBE_URL}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:10px 20px;border-top:2px solid #00b8b8;font-size:11pt;letter-spacing:0.04em;"><strong>{label}</strong></a>'
      '</span></div>')

def downloads_block(es):
    # Orange Downloads section (Overview only). Sketchbook Cover holds the reflection doc.
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

def nav(current, dots, stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Sketchbook Cover Art</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

VOCAB_EN=[
 ("Typeface","A family of letters that all share one design or style. Cooper Black is a typeface."),
 ("Legible","Easy to read. Your name, period, and words must be legible so anyone can read them."),
 ("Composition","How you arrange everything on your cover so it looks balanced and planned, not random."),
 ("Medium","The tool or material you use to make art, like pencil, marker, or colored pencil."),
 ("Serif","A typeface with small feet or tails on the ends of the letters. Cooper Black is a bold serif."),
 ("Sans Serif","A typeface with no feet on the letters. Clean and simple (sans means without)."),
]
VOCAB_ES=[
 ("Tipo de Letra","Una familia de letras que comparten un mismo dise&ntilde;o o estilo. Cooper Black es un tipo de letra."),
 ("Legible","F&aacute;cil de leer. Tu nombre, periodo y palabras deben ser legibles para que cualquiera los lea."),
 ("Composici&oacute;n","C&oacute;mo acomodas todo en tu portada para que se vea equilibrada y planeada, no al azar."),
 ("Medio","La herramienta o el material que usas para hacer arte, como l&aacute;piz, marcador o l&aacute;piz de color."),
 ("Serif","Un tipo de letra con peque&ntilde;os pies o remates en las puntas de las letras. Cooper Black es un serif grueso."),
 ("Sans Serif","Un tipo de letra sin pies en las letras. Limpio y simple (sans significa sin)."),
]

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Digital Arts 1A &bull; Sketchbook Cover Art","Sketchbook Cover Art","Design a cover worth showing off.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","Make Your Sketchbook Your Own",
        para("Time to make your sketchbook yours. You will decorate and personalize the manila cover of your 8.5 by 11 inch sketchbook and turn it into art you are proud of. This is a friendly class competition: the best cover wins a prize. You have one week, and you may take your sketchbook home to keep working on it.")
        + framed(HEADER_IMG,"Sketchbook Cover"))
    en+=downloads_block(False)
    en+=card("THE PRIZE / KEY DATES","Rules and Dates",
        float_right(CHICKFILA,"Chick-fil-A prize","The prize for the best cover.")
        + para("This is a competition, so do your very best work. Here is what you need to know:")
        + datebox("Competition",
            '<div style="font-size:13pt;color:rgba(255,255,255,0.92);line-height:1.7;">'
            '<strong style="color:#80e0e0;">Due:</strong> Friday, September 4<br>'
            '<strong style="color:#80e0e0;">Winner announced:</strong> Wednesday, September 9<br>'
            '<strong style="color:#80e0e0;">Prize:</strong> a Chick-fil-A gift card for the best cover</div>'))
    en+=card("REQUIREMENTS","Your Cover Must Have",
        bullets([
            ("Both covers:","decorate the FRONT and the BACK of your sketchbook."),
            ("Name and period:","in the TOP RIGHT corner, clear and easy to read."),
            ("3 words:","at least 3 motivational or inspiring words."),
            ("Cooper Black:","draw ONE of your words in the Cooper Black typeface (example on Step 01)."),
            ("2 Adobe fonts:","draw your other 2 words in 2 clear typefaces you pick from Adobe Fonts."),
            ("Any medium (the tool or material you use, like pencil, marker, or colored pencil):","use whatever you like. Pencils, markers, and colored pencils are provided in class."),
        ]))
    en+=card("BUILDS ON MODULES 1 &amp; 2","Bring It All Together",
        para("This project puts together what you learned in Module 01 (Pictograms) and Module 02 (Color Theory), and adds a new idea: typeface. Use color on purpose, and try different typefaces for your words.")
        + note("Tip: adding a pictogram that represents you or one of your words can make your cover stronger and may boost your chance of winning."))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will be on the quiz.",
          VOCAB_EN), False)
    en+=card("RESEARCH / FONTS","Choose Your Fonts",
        para("Pick your 2 typefaces on Adobe Fonts. Only this website is approved for the competition. On Adobe Fonts you can type your own word into the Sample Text box to see how it looks in any font.")
        + adobe_link("Adobe Fonts (fonts.adobe.com)"))

    es=banner("Arte Digital 1A &bull; Arte de la Portada","Arte de la Portada","Dise&ntilde;a una portada digna de presumir.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","Haz Tuyo Tu Cuaderno",
        para("Es hora de hacer tuyo tu cuaderno. Vas a decorar y personalizar la portada de manila de tu cuaderno de 8.5 por 11 pulgadas y convertirla en arte del que te sientas orgulloso. Esta es una competencia amistosa de la clase: la mejor portada gana un premio. Tienes una semana, y puedes llevar tu cuaderno a casa para seguir trabajando.")
        + framed(HEADER_IMG,"Portada del Cuaderno"))
    es+=downloads_block(True)
    es+=card("EL PREMIO / FECHAS CLAVE","Reglas y Fechas",
        float_right(CHICKFILA,"Premio de Chick-fil-A","El premio para la mejor portada.")
        + para("Esta es una competencia, as&iacute; que haz tu mejor trabajo. Esto es lo que necesitas saber:")
        + datebox("Competencia",
            '<div style="font-size:13pt;color:rgba(255,255,255,0.92);line-height:1.7;">'
            '<strong style="color:#80e0e0;">Fecha de entrega:</strong> viernes 4 de septiembre<br>'
            '<strong style="color:#80e0e0;">Ganador se anuncia:</strong> mi&eacute;rcoles 9 de septiembre<br>'
            '<strong style="color:#80e0e0;">Premio:</strong> una tarjeta de regalo de Chick-fil-A para la mejor portada</div>'))
    es+=card("REQUISITOS","Tu Portada Debe Tener",
        bullets([
            ("Las dos portadas:","decora el FRENTE y el REVERSO de tu cuaderno."),
            ("Nombre y periodo:","en la esquina SUPERIOR DERECHA, claros y f&aacute;ciles de leer."),
            ("3 palabras:","al menos 3 palabras motivadoras o inspiradoras."),
            ("Cooper Black:","dibuja UNA de tus palabras en el tipo de letra Cooper Black (ejemplo en el Paso 01)."),
            ("2 fuentes de Adobe:","dibuja tus otras 2 palabras en 2 tipos de letra claros que elijas de Adobe Fonts."),
            ("Cualquier medio (la herramienta o el material que usas, como l&aacute;piz, marcador o l&aacute;piz de color):","usa lo que quieras. En clase se proveen l&aacute;pices, marcadores y l&aacute;pices de color."),
        ]))
    es+=card("SE BASA EN LOS M&Oacute;DULOS 1 Y 2","Junta Todo Lo Aprendido",
        para("Este proyecto junta lo que aprendiste en el M&oacute;dulo 01 (Pictogramas) y el M&oacute;dulo 02 (Teor&iacute;a del Color), y agrega una idea nueva: el tipo de letra. Usa el color a prop&oacute;sito y prueba diferentes tipos de letra para tus palabras.")
        + note("Consejo: agregar un pictograma que te represente a ti o a una de tus palabras puede hacer tu portada m&aacute;s fuerte y aumentar tu oportunidad de ganar."))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave estar&aacute;n en el examen.",
          VOCAB_ES), True)
    es+=card("INVESTIGACI&Oacute;N / FUENTES","Elige Tus Fuentes",
        para("Elige tus 2 tipos de letra en Adobe Fonts. Solo este sitio web est&aacute; aprobado para la competencia. En Adobe Fonts puedes escribir tu propia palabra en la casilla de Texto de Muestra para ver c&oacute;mo se ve en cualquier fuente.")
        + adobe_link("Adobe Fonts (fonts.adobe.com)"))

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Sketchbook Cover Art | Digital Arts 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Digital Arts 1A &bull; Sketchbook Cover Art","Sketchbook Cover Art","Design your covers, then turn in two photos.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("2 images:","a photo of your front cover and a photo of your back cover (2 JPGs), uploaded to this Canvas assignment.")])
    en+=card("STEP 01 / DESIGN &amp; CREATE","Design Your Cover",
        cooper_float("One of your 3 words must be drawn in Cooper Black. Use this alphabet as your guide. Tap the image to open it full size.")
        + para("Now design your cover. Plan where your name, period, and 3 words will go, then decorate the front and the back. Take your time and make it yours. You can work in class and take your sketchbook home for more.")
        + bullets([
            ("Plan first:","lightly sketch where everything goes before you add color."),
            ("Name and period:","top right corner, clear and easy to read."),
            ("Fill both covers:","front and back should both look finished."),
        ]))
    en+=card("YOUR 3 WORDS","Pick 3 Words and Their Fonts",
        para("Choose 3 motivational or inspiring words. Then draw them like this:")
        + bullets([
            ("1 word in Cooper Black:","use the alphabet on the right as your guide."),
            ("2 words in Adobe Fonts:","pick 2 clear typefaces from Adobe Fonts, one for each word."),
        ])
        + para("On Adobe Fonts, type your own word into the Sample Text box to see how it looks in any font before you draw it. Only this website is approved for the competition.")
        + adobe_link("Adobe Fonts (fonts.adobe.com)"))
    en+=card("REMEMBER","Before You Finish",
        note("Check your cover: both sides decorated, name and period in the top right corner, at least 3 words, and each word clear and easy to read."))
    en+=card("CAPTURE &amp; UPLOAD","Photograph and Upload Your 2 Images",
        para("When both covers are done, take a clean, clear photo of your FRONT cover and another of your BACK cover with your school iPad. Use good light, hold the iPad straight above the cover, and avoid glare. Upload both images (2 files) to this Canvas assignment.")
        + bullets([
            ("2 JPGs:","one photo of the front cover, one photo of the back cover."),
            ("Clean and clear:","good light, straight on, the whole cover in the frame."),
        ])
        + note("This is Step 1 and it is graded on its own. The reflection is turned in separately on Step 2."))

    es=banner("Arte Digital 1A &bull; Arte de la Portada","Arte de la Portada","Dise&ntilde;a tus portadas y entrega dos fotos.","#top","Back to English")
    es+=deliverables_box(True,
        [("2 im&aacute;genes:","una foto de tu portada del frente y una de tu portada del reverso (2 JPG), subidas a esta tarea de Canvas.")])
    es+=card("PASO 01 / DISE&Ntilde;A Y CREA","Dise&ntilde;a Tu Portada",
        cooper_float("Una de tus 3 palabras debe estar dibujada en Cooper Black. Usa este alfabeto como gu&iacute;a. Toca la imagen para abrirla en tama&ntilde;o completo.")
        + para("Ahora dise&ntilde;a tu portada. Planea d&oacute;nde ir&aacute;n tu nombre, tu periodo y tus 3 palabras, y luego decora el frente y el reverso. T&oacute;mate tu tiempo y hazla tuya. Puedes trabajar en clase y llevar tu cuaderno a casa para m&aacute;s.")
        + bullets([
            ("Planea primero:","dibuja suave d&oacute;nde va todo antes de agregar color."),
            ("Nombre y periodo:","esquina superior derecha, claros y f&aacute;ciles de leer."),
            ("Llena las dos portadas:","el frente y el reverso deben verse terminados."),
        ]))
    es+=card("TUS 3 PALABRAS","Elige 3 Palabras y Sus Fuentes",
        para("Elige 3 palabras motivadoras o inspiradoras. Luego dib&uacute;jalas as&iacute;:")
        + bullets([
            ("1 palabra en Cooper Black:","usa el alfabeto de la derecha como gu&iacute;a."),
            ("2 palabras en Adobe Fonts:","elige 2 tipos de letra claros de Adobe Fonts, uno para cada palabra."),
        ])
        + para("En Adobe Fonts, escribe tu propia palabra en la casilla de Texto de Muestra para ver c&oacute;mo se ve en cualquier fuente antes de dibujarla. Solo este sitio web est&aacute; aprobado para la competencia.")
        + adobe_link("Adobe Fonts (fonts.adobe.com)"))
    es+=card("RECUERDA","Antes de Terminar",
        note("Revisa tu portada: las dos caras decoradas, nombre y periodo en la esquina superior derecha, al menos 3 palabras, y cada palabra clara y f&aacute;cil de leer."))
    es+=card("CAPTURA Y SUBE","Fotograf&iacute;a y Sube Tus 2 Im&aacute;genes",
        para("Cuando las dos portadas est&eacute;n listas, toma una foto limpia y clara de tu portada del FRENTE y otra del REVERSO con tu iPad de la escuela. Usa buena luz, sostiene el iPad recto sobre la portada y evita el reflejo. Sube las dos im&aacute;genes (2 archivos) a esta tarea de Canvas.")
        + bullets([
            ("2 JPG:","una foto de la portada del frente, una del reverso."),
            ("Limpia y clara:","buena luz, de frente, con toda la portada en el encuadre."),
        ])
        + note("Este es el Paso 1 y se califica por su cuenta. La reflexi&oacute;n se entrega por separado en el Paso 2."))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Sketchbook Cover Art: Design & Submit | Digital Arts 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Digital Arts 1A &bull; Sketchbook Cover Art","Sketchbook Cover Art","Complete and upload your reflection.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 reflection:","your completed reflection Word document (.docx), uploaded to this Canvas assignment.")])
    en+=card("REFLECT / STEP 02","Complete and Upload the Reflection",
        float_right(REFLECT_TYPING,"A student typing the reflection on a computer","Type your answers right in the document.")
        + para("Finish with a short reflection. It asks about your 3 words, your Cooper Black word, and the 2 Adobe Fonts typefaces you chose, plus how you can test a font on Adobe Fonts.")
        + note("The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.")
        + para("Type your answers, save the document, and upload it to this Canvas assignment.")
        + note("Your 2 cover images were turned in on Step 1. Be honest and turn in your own work."))

    es=banner("Arte Digital 1A &bull; Arte de la Portada","Arte de la Portada","Completa y sube tu reflexi&oacute;n.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 reflexi&oacute;n:","tu documento de Word (.docx) de la reflexi&oacute;n completo, subido a esta tarea de Canvas.")])
    es+=card("REFLEXIONA / PASO 02","Completa y Sube la Reflexi&oacute;n",
        float_right(REFLECT_TYPING,"Un estudiante escribiendo la reflexi&oacute;n en la computadora","Escribe tus respuestas en el documento.")
        + para("Termina con una reflexi&oacute;n corta. Pregunta sobre tus 3 palabras, tu palabra en Cooper Black y los 2 tipos de letra de Adobe Fonts que elegiste, y c&oacute;mo puedes probar una fuente en Adobe Fonts.")
        + note("El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.")
        + para("Escribe tus respuestas, guarda el documento y s&uacute;belo a esta tarea de Canvas.")
        + note("Tus 2 im&aacute;genes de la portada se entregaron en el Paso 1. S&eacute; honesto y entrega tu propio trabajo."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
    return wrap_page("Sketchbook Cover Art: Reflection | Digital Arts 1A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
