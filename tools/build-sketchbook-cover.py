#!/usr/bin/env python3
# Digital Arts 1A - Module 03: Sketchbook Cover Design competition (3 pages), dark angular framework.
import os, re
SITE="https://www.creativesilva.com"
ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
IMGDIR=f"{SITE}/assets/images/digarts1/sketchbook-cover"
COOPER=f"{IMGDIR}/cooper-black-example.png"
ADOBE_ICON=f"{IMGDIR}/adobe-fonts-icon.png"
STOPWATCH=f"{IMGDIR}/stopwatch-icon.png"
HEADER_IMG=f"{IMGDIR}/sketchbook-cover-header.png"
CHICKFILA=f"{IMGDIR}/chick-fil-a-prize.jpg"
REFLECT_TYPING=f"{IMGDIR}/reflection-typing-v2.png"
ADOBE_URL="https://fonts.adobe.com"
REFLECT_EN=f"{SITE}/assets/course-documents/Sketchbook-Cover-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Sketchbook-Cover-Reflection-ES.docx"

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"&ndash;","•":"&bull;"}
    return "".join(m.get(c, c if ord(c)<128 else "&#x{:X};".format(ord(c))) for c in s)

def banner(label,title,subtitle,es_href,es_label):
    return ('<div style="background:linear-gradient(135deg,#000000 0%,#003838 40%,#007474 100%);padding:20px 28px 22px;margin:-28px -28px 24px -28px;">'
      '<div style="display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;gap:16px;">'
      f'<div style="justify-self:start;"><img src="{SITE}/assets/PV%20LOGO%20NEW.png" alt="Pioneer Valley High School Logo" style="width:min(90px,15vw);height:auto;display:block;" /></div>'
      '<div style="justify-self:center;text-align:center;">'
      f'<div style="margin-bottom:6px;"><span style="font-size:13pt;color:#80e0e0;"><strong>{label}</strong></span></div>'
      f'<div style="color:#ffffff;font-size:23pt;line-height:1.1;"><strong>{title}</strong></div>'
      f'<div style="color:rgba(255,255,255,0.82);margin-top:6px;"><span style="font-size:13pt;font-style:italic;"><strong>{subtitle}</strong></span></div></div>'
      f'<div style="justify-self:end;"><a href="{es_href}" style="background:rgba(255,255,255,0.92);color:#003838;text-decoration:none;padding:7px 16px;display:inline-block;font-size:11pt;white-space:nowrap;border-top:2px solid #ff6b1a;"><strong>{es_label}</strong></a></div>'
      '</div></div>')

def card(eyebrow,heading,inner):
    return ('<div style="background:linear-gradient(180deg,rgba(0,116,116,0.10) 0%,rgba(0,116,116,0.03) 100%);border:1px solid rgba(0,184,184,0.22);border-left:6px solid #00b8b8;padding:30px;overflow:hidden;position:relative;margin-bottom:24px;">'
      '<div style="display:inline-block;background:rgba(0,0,0,0.40);border-left:3px solid #00b8b8;padding:5px 12px 5px 10px;font-family:Arial,sans-serif;font-size:10pt;letter-spacing:0.22em;color:#80e0e0;text-transform:uppercase;margin-bottom:12px;">'
      f'<strong>{eyebrow}</strong></div>'
      f'<div style="margin-bottom:8px;"><span style="font-size:20pt;color:#ffffff;"><strong>{heading}</strong></span></div>'
      '<div style="height:2px;background:#00b8b8;width:60px;margin-bottom:18px;"></div>'
      f'{inner}</div>')

def para(t):
    return f'<div style="margin-bottom:14px;line-height:1.72;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{t}</span></div>'

def bullets(items):
    r=""
    for b,rest in items:
        inner=(f'<strong>{b}</strong> {rest}' if b else rest)
        r+=('<div style="margin-bottom:8px;line-height:1.55;"><span style="color:#00b8b8;">&bull;</span> '
            f'<span style="font-size:13.5pt;color:rgba(255,255,255,0.88);">{inner}</span></div>')
    return f'<div style="margin-bottom:6px;">{r}</div>'

def note_orange(t):
    return (f'<div style="background:rgba(255,107,26,0.10);border:1px solid rgba(255,107,26,0.30);border-left:4px solid #FF6B1A;padding:11px 14px;margin:8px 0;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def deliverables_box(title, lead, items):
    lis=""
    for b,rest in items:
        lis+=('<div style="margin-bottom:6px;line-height:1.5;"><span style="color:#00b8b8;">&bull;</span> '
              f'<span style="font-size:13pt;color:rgba(255,255,255,0.90);"><strong>{b}</strong> {rest}</span></div>')
    return ('<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.35);border-left:5px solid #00b8b8;padding:16px 18px;margin:0 0 24px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:8px;"><strong>{title}</strong></div>'
      f'<div style="font-size:13pt;color:#ffffff;margin-bottom:8px;"><strong>{lead}</strong></div>'
      f'{lis}</div>')

def datebox(label, rows_html):
    return ('<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.30);border-left:4px solid #00b8b8;padding:14px 16px;margin:6px 0 4px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:8px;"><strong>{label}</strong></div>'
      f'{rows_html}</div>')

def img_placeholder_full(label):
    return (f'<div style="width:100%;min-height:230px;display:flex;align-items:center;justify-content:center;background:rgba(0,116,116,0.08);border:2px dashed rgba(0,180,180,0.45);color:rgba(255,255,255,0.55);font-size:12pt;letter-spacing:0.14em;text-transform:uppercase;text-align:center;margin:6px 0 0;box-sizing:border-box;"><strong>{label}</strong></div>')

def float_placeholder_desc(label, desc):
    return ('<div style="float:right;width:40%;min-width:230px;margin:0 0 16px 22px;">'
      f'<div style="background:rgba(0,116,116,0.08);border:2px dashed rgba(0,180,180,0.45);min-height:210px;display:flex;align-items:center;justify-content:center;text-align:center;color:rgba(255,255,255,0.55);font-size:11pt;letter-spacing:0.1em;text-transform:uppercase;padding:20px;box-sizing:border-box;"><strong>{label}</strong></div>'
      f'<div style="font-size:10pt;color:rgba(255,255,255,0.5);margin-top:8px;line-height:1.45;font-style:italic;">{desc}</div></div>')

def cooper_float(caption):
    return ('<div style="float:right;width:40%;min-width:240px;margin:0 0 16px 22px;">'
      f'<a href="{COOPER}" target="_blank" rel="noopener" style="display:block;text-decoration:none;background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;line-height:0;">'
      f'<img src="{COOPER}" alt="Cooper Black alphabet example" style="display:block;width:100%;height:auto;" /></a>'
      f'<div style="font-size:10pt;color:#80e0e0;margin-top:8px;line-height:1.4;"><strong>{caption}</strong></div></div>')

def adobe_link(label):
    return ('<div style="margin:8px 0 4px;">'
      '<span style="display:inline-flex;align-items:center;gap:12px;flex-wrap:wrap;">'
      f'<img src="{ADOBE_ICON}" alt="Adobe Fonts icon" style="width:40px;height:40px;display:block;flex:0 0 auto;" />'
      f'<a href="{ADOBE_URL}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:10px 20px;border-top:2px solid #00b8b8;font-size:11pt;letter-spacing:0.04em;"><strong>{label}</strong></a>'
      '</span></div>')

def dl_link(url,label):
    return (f'<div style="margin-top:4px;"><a href="{url}" download style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:10px 20px;border-top:2px solid #00b8b8;font-size:11pt;letter-spacing:0.04em;margin:0 12px 12px 0;"><strong>{label}</strong></a></div>')

def framed_hero(src,alt):
    return f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;margin:6px 0 0;"><img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'

def reflect_typing_float(alt, caption):
    return ('<div style="float:right;width:40%;min-width:240px;margin:0 0 16px 22px;">'
      f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;line-height:0;"><img src="{REFLECT_TYPING}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>'
      f'<div style="font-size:10pt;color:#80e0e0;margin-top:8px;line-height:1.4;"><strong>{caption}</strong></div></div>')

def vocab_grid(terms):
    rows=[terms[i:i+3] for i in range(0,len(terms),3)]
    body=""
    for row in rows:
        tds=""
        for term,d in row:
            tds+=('<td style="width:33.33%;vertical-align:top;padding:6px;">'
                  '<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;height:100%;box-sizing:border-box;">'
                  '<div style="background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:16px;height:100%;box-sizing:border-box;">'
                  f'<div style="font-size:12pt;color:#ffffff;margin-bottom:5px;"><strong>{term}</strong></div>'
                  f'<div style="font-size:10.5pt;line-height:1.5;color:rgba(255,255,255,0.80);">{d}</div></div></div></td>')
        body+=f'<tr>{tds}</tr>'
    return f'<table role="presentation" style="width:100%;border-collapse:collapse;table-layout:fixed;"><tbody>{body}</tbody></table>'

def top_wrap(en_inner, es_inner):
    return ('<div id="top" style="width:100%;margin:0 auto;font-family:Arial,sans-serif;color:#ffffff;background-color:#080808;'
      "background-image:linear-gradient(180deg,rgba(8,8,8,0.97) 0%,rgba(0,56,56,0.94) 50%,rgba(8,8,8,0.97) 100%),"
      f"url('{SITE}/assets/PV_Panther_Watermark.png');"
      'background-position:center center,center center;background-repeat:no-repeat,no-repeat;background-attachment:fixed,fixed;overflow:hidden;">'
      '<div style="padding:28px 28px 40px;">' + en_inner + '</div>'
      '<div id="espanol" style="border-top:2px solid rgba(255,255,255,0.10);"><div style="padding:28px 28px 40px;">' + es_inner + '</div></div>'
      '</div>')

def wrap_page(title, nav_inner, top_html, bottom_nav):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="icon" type="image/svg+xml" href="https://www.creativesilva.com/logos/CS_Logo_Only.svg" />
  <style>:root {{ --course-accent: #007474; }}</style>
  <link rel="stylesheet" href="/css/silva-module.css" />
</head>
<body>
  <nav class="silva-nav" aria-label="Module navigation">
    <div class="silva-nav-inner">
{nav_inner}
      <div class="silva-nav-div"></div>
      <button class="silva-copy-btn" onclick="silvaCopyHTML()" aria-label="Copy Canvas HTML to clipboard">&#128203; Copy Canvas HTML</button>
      <button class="silva-download-btn" onclick="silvaDownloadHTML()" aria-label="Download Canvas HTML as file">&#128229; Download HTML</button>
    </div>
  </nav>
  <div class="silva-page">
  <div id="silva-module-content">
  {top_html}
  </div>
  {bottom_nav}
  </div>
  <script>
    function silvaCopyHTML() {{ var el=document.getElementById('top'); navigator.clipboard.writeText(el.outerHTML).then(function(){{var b=document.querySelector('.silva-copy-btn');b.textContent='\\u2713 Copied!';b.classList.add('copied');setTimeout(function(){{b.innerHTML='&#128203; Copy Canvas HTML';b.classList.remove('copied');}},2500);}}).catch(function(){{alert('Copy failed. Select the source manually.');}}); }}
    function silvaDownloadHTML() {{ var el=document.getElementById('top'); var blob=new Blob([el.outerHTML],{{type:'text/html'}}); var url=URL.createObjectURL(blob); var a=document.createElement('a'); a.href=url; a.download=location.pathname.split('/').pop().replace('.html','')+'-canvas.html'; document.body.appendChild(a); a.click(); document.body.removeChild(a); URL.revokeObjectURL(url); }}
  </script>
  <script src="/js/silva-nav.js"></script>
</body>
</html>
'''

OVER="digarts1-sketchbook-cover-overview.html"
S1="digarts1-sketchbook-cover-step01-design.html"
S2="digarts1-sketchbook-cover-step02-submit-reflect.html"

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

def dot(href,label,title,active,module=False):
    if active: return f'<span class="sdot sdot-active" title="{title}">{label}</span>'
    cls="sdot sdot-link sdot-module" if module else "sdot sdot-link"
    return f'<a href="{href}" class="{cls}" title="{title}">{label}</a>'

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
    HEAD_EN=banner("Digital Arts 1A &bull; Sketchbook Cover Art","Sketchbook Cover Art","Design a cover worth showing off.","#espanol","Clic para Espa&ntilde;ol")
    HEAD_ES=banner("Arte Digital 1A &bull; Arte de la Portada","Arte de la Portada","Dise&ntilde;a una portada digna de presumir.","#top","Back to English")
    en=HEAD_EN
    en+=card("THE COMPETITION / OVERVIEW","Make Your Sketchbook Your Own",
        para("Time to make your sketchbook yours. You will decorate and personalize the manila cover of your 8.5 by 11 inch sketchbook and turn it into art you are proud of. This is a friendly class competition: the best cover wins a prize. You have one week, and you may take your sketchbook home to keep working on it.")
        + framed_hero(HEADER_IMG,"Sketchbook Cover"))
    en+=card("THE PRIZE / KEY DATES","Rules and Dates",
        f'<div style="float:right;width:36%;min-width:220px;margin:0 0 14px 22px;background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;line-height:0;"><img src="{CHICKFILA}" alt="Chick-fil-A prize" style="display:block;width:100%;height:auto;" /></div>'
        + para("This is a competition, so do your very best work. Here is what you need to know:")
        + datebox("Competition",
            '<div style="font-size:13pt;color:rgba(255,255,255,0.92);line-height:1.7;">'
            '<strong style="color:#80e0e0;">Due:</strong> Friday, September 4<br>'
            '<strong style="color:#80e0e0;">Winner announced:</strong> Tuesday, September 9<br>'
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
        + note_orange("Tip: adding a pictogram that represents you or one of your words can make your cover stronger and may boost your chance of winning."))
    en+=card("VOCABULARY / 6 TERMS","Key Words",
        note_orange("Heads up: these key words will be on the quiz.")
        + vocab_grid(VOCAB_EN))
    en+=card("RESEARCH / FONTS","Fonts and Reflection",
        para("Pick your 2 typefaces on Adobe Fonts. Only this website is approved for the competition. On Adobe Fonts you can type your own word into the Sample Text box to see how it looks in any font.")
        + adobe_link("Adobe Fonts (fonts.adobe.com)")
        + para("Download the reflection here. Fill it out after your cover is done.")
        + dl_link(REFLECT_EN,"Sketchbook Cover Reflection (Word)"))

    es=HEAD_ES
    es+=card("LA COMPETENCIA / RESUMEN","Haz Tuyo Tu Cuaderno",
        para("Es hora de hacer tuyo tu cuaderno. Vas a decorar y personalizar la portada de manila de tu cuaderno de 8.5 por 11 pulgadas y convertirla en arte del que te sientas orgulloso. Esta es una competencia amistosa de la clase: la mejor portada gana un premio. Tienes una semana, y puedes llevar tu cuaderno a casa para seguir trabajando.")
        + framed_hero(HEADER_IMG,"Portada del Cuaderno"))
    es+=card("EL PREMIO / FECHAS CLAVE","Reglas y Fechas",
        f'<div style="float:right;width:36%;min-width:220px;margin:0 0 14px 22px;background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;line-height:0;"><img src="{CHICKFILA}" alt="Premio de Chick-fil-A" style="display:block;width:100%;height:auto;" /></div>'
        + para("Esta es una competencia, as&iacute; que haz tu mejor trabajo. Esto es lo que necesitas saber:")
        + datebox("Competencia",
            '<div style="font-size:13pt;color:rgba(255,255,255,0.92);line-height:1.7;">'
            '<strong style="color:#80e0e0;">Fecha de entrega:</strong> viernes 4 de septiembre<br>'
            '<strong style="color:#80e0e0;">Ganador se anuncia:</strong> martes 9 de septiembre<br>'
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
        + note_orange("Consejo: agregar un pictograma que te represente a ti o a una de tus palabras puede hacer tu portada m&aacute;s fuerte y aumentar tu oportunidad de ganar."))
    es+=card("VOCABULARIO / 6 T&Eacute;RMINOS","Palabras Clave",
        note_orange("Atenci&oacute;n: estas palabras clave estar&aacute;n en el examen.")
        + vocab_grid(VOCAB_ES))
    es+=card("INVESTIGACI&Oacute;N / FUENTES","Fuentes y Reflexi&oacute;n",
        para("Elige tus 2 tipos de letra en Adobe Fonts. Solo este sitio web est&aacute; aprobado para la competencia. En Adobe Fonts puedes escribir tu propia palabra en la casilla de Texto de Muestra para ver c&oacute;mo se ve en cualquier fuente.")
        + adobe_link("Adobe Fonts (fonts.adobe.com)")
        + para("Descarga la reflexi&oacute;n aqu&iacute;. Ll&eacute;nala cuando termines tu portada.")
        + dl_link(REFLECT_ES,"Reflexi&oacute;n de la Portada (Word)"))

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Sketchbook Cover Art | Digital Arts 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    HEAD_EN=banner("Digital Arts 1A &bull; Sketchbook Cover Art","Sketchbook Cover Art","Design your covers, then turn in two photos.","#espanol","Clic para Espa&ntilde;ol")
    HEAD_ES=banner("Arte Digital 1A &bull; Arte de la Portada","Arte de la Portada","Dise&ntilde;a tus portadas y entrega dos fotos.","#top","Back to English")
    en=HEAD_EN
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
        note_orange("Check your cover: both sides decorated, name and period in the top right corner, at least 3 words, and each word clear and easy to read."))

    en+=card("STEP 01 / TURN IT IN","Photograph and Upload Your 2 Images",
        para("When both covers are done, take a clean, clear photo of your FRONT cover and another of your BACK cover with your school iPad. Use good light, hold the iPad straight above the cover, and avoid glare. Upload both images (2 files) to this Canvas assignment.")
        + bullets([
            ("2 files:","one photo of the front cover, one photo of the back cover."),
            ("Clean and clear:","good light, straight on, the whole cover in the frame."),
        ])
        + note_orange("This is Step 1 and it is graded on its own. The reflection is turned in separately on Step 2."))

    es=HEAD_ES
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
        note_orange("Revisa tu portada: las dos caras decoradas, nombre y periodo en la esquina superior derecha, al menos 3 palabras, y cada palabra clara y f&aacute;cil de leer."))

    es+=card("PASO 01 / ENTR&Eacute;GALO","Fotograf&iacute;a y Sube Tus 2 Im&aacute;genes",
        para("Cuando las dos portadas est&eacute;n listas, toma una foto limpia y clara de tu portada del FRENTE y otra del REVERSO con tu iPad de la escuela. Usa buena luz, sostiene el iPad recto sobre la portada y evita el reflejo. Sube las dos im&aacute;genes (2 archivos) a esta tarea de Canvas.")
        + bullets([
            ("2 archivos:","una foto de la portada del frente, una del reverso."),
            ("Limpia y clara:","buena luz, de frente, con toda la portada en el encuadre."),
        ])
        + note_orange("Este es el Paso 1 y se califica por su cuenta. La reflexi&oacute;n se entrega por separado en el Paso 2."))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Sketchbook Cover Art: Design & Submit | Digital Arts 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    HEAD_EN=banner("Digital Arts 1A &bull; Sketchbook Cover Art","Sketchbook Cover Art","Complete and upload your reflection.","#espanol","Clic para Espa&ntilde;ol")
    HEAD_ES=banner("Arte Digital 1A &bull; Arte de la Portada","Arte de la Portada","Completa y sube tu reflexi&oacute;n.","#top","Back to English")
    en=HEAD_EN
    en+=card("REFLECT / STEP 02","Complete and Upload the Reflection",
        reflect_typing_float("A student typing the reflection on a computer","Type your answers right in the document.")
        + para("Finish with a short reflection. It asks about your 3 words, your Cooper Black word, and the 2 Adobe Fonts typefaces you chose, plus how you can test a font on Adobe Fonts.")
        + note_orange("The reflection Word document is on the Overview page. Open the Overview to download it.")
        + para("Type your answers, save the document, and upload it to this Canvas assignment."))
    en+=card("TURN IT IN / DELIVERABLES","What You Turn In",
        bullets([
            ("1 reflection:","your completed reflection Word document."),
        ])
        + note_orange("This step is graded on its own. Your 2 cover images were turned in on Step 1. Be honest and turn in your own work."))

    es=HEAD_ES
    es+=card("REFLEXIONA / PASO 02","Completa y Sube la Reflexi&oacute;n",
        reflect_typing_float("Un estudiante escribiendo la reflexi&oacute;n en la computadora","Escribe tus respuestas en el documento.")
        + para("Termina con una reflexi&oacute;n corta. Pregunta sobre tus 3 palabras, tu palabra en Cooper Black y los 2 tipos de letra de Adobe Fonts que elegiste, y c&oacute;mo puedes probar una fuente en Adobe Fonts.")
        + note_orange("El documento de Word de la reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen. Abre el Resumen para descargarlo.")
        + para("Escribe tus respuestas, guarda el documento y s&uacute;belo a esta tarea de Canvas."))
    es+=card("ENTR&Eacute;GALO / ENTREGABLES","Qu&eacute; Entregas",
        bullets([
            ("1 reflexi&oacute;n:","tu documento de Word de la reflexi&oacute;n completo."),
        ])
        + note_orange("Este paso se califica por su cuenta. Tus 2 im&aacute;genes de la portada se entregaron en el Paso 1. S&eacute; honesto y entrega tu propio trabajo."))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
    return wrap_page("Sketchbook Cover Art: Reflection | Digital Arts 1A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

for fname, htmlgen in [(OVER,overview),(S1,step01),(S2,step02)]:
    html=ent(htmlgen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    low=html.lower()
    for w in ["shoot","shooting","shot","shots","screenshot"]:
        assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
