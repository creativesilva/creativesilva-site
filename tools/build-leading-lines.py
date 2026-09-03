#!/usr/bin/env python3
# Photography 1A - Module 03: Leading Lines Photo Walk.
# Followup to Composition Concepts. In-class photo walk, shared class cameras (2 per camera),
# each partner takes 3 leading-line examples, swap, cull to best 6 (3 own + 3 partner), JPG only.
# Dark teal angular framework. Overview + 2 steps, bilingual EN/ES, 5th-grade.
# Header + Step 01 float are PLACEHOLDERS (art dropped in later).
import os, re
SITE="https://www.creativesilva.com"
ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
IMG=f"{SITE}/assets/images/photo1/leading-lines"
HEADER=f"{IMG}/leading-lines-header-v1.jpg"
FLOAT=f"{IMG}/leading-lines-step01-float-v1.jpg"
ARTICLE="https://digital-photography-school.com/how-to-use-leading-lines-for-better-compositions/"
REFLECT_EN=f"{SITE}/assets/course-documents/Leading-Lines-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Leading-Lines-Reflection-ES.docx"

OVER="photo1-leading-lines-overview.html"
S1="photo1-leading-lines-step01-capture.html"
S2="photo1-leading-lines-step02-reflection.html"

def ent(s):
    m={"á":"&aacute;","é":"&eacute;","í":"&iacute;","ó":"&oacute;","ú":"&uacute;",
       "Á":"&Aacute;","É":"&Eacute;","Í":"&Iacute;","Ó":"&Oacute;","Ú":"&Uacute;",
       "ñ":"&ntilde;","Ñ":"&Ntilde;","ü":"&uuml;","¿":"&iquest;","¡":"&iexcl;",
       "“":"&ldquo;","”":"&rdquo;","‘":"&lsquo;","’":"&rsquo;","–":"&ndash;","•":"&bull;","×":"&times;"}
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

def placeholder(label, minh, mw=None):
    # dashed placeholder box for art dropped in later (header / float). Chris fills these.
    style=f'width:{mw};' if mw else ''
    return (f'<div style="{style}min-height:{minh}px;border:2px dashed rgba(0,184,184,0.45);background:rgba(0,184,184,0.06);'
      'display:flex;align-items:center;justify-content:center;text-align:center;padding:18px;margin:6px 0 4px;box-sizing:border-box;">'
      f'<span style="font-size:11pt;letter-spacing:0.16em;text-transform:uppercase;color:#80e0e0;line-height:1.5;">{label}</span></div>')

def float_placeholder(label):
    return ('<div style="float:right;width:40%;min-width:230px;margin:0 0 14px 22px;">'
      + placeholder(label, 220) + '</div>')

def framed(src,alt):
    return (f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;margin:6px 0 4px;">'
      f'<img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>')

def float_right(src,alt):
    return ('<div style="float:right;width:40%;min-width:230px;margin:0 0 14px 22px;">'
      f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;"><img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div></div>')

DL_ICON=f"{SITE}/assets/Icons/assignment/downloads-v1.png"   # the "downloads" folder icon

def dl_link(url,label,download=True,row=False):
    # row=True drops the button's vertical margin so it centers cleanly beside the icon
    if download:
        # official orange (#FF6B1A) so a file download stands out for students
        mgn='margin:0;' if row else 'margin:0 10px 8px 0;'
        return (f'<a href="{url}" download style="display:inline-block;text-decoration:none;background:#FF6B1A;color:#ffffff;padding:11px 22px;border-top:2px solid #ffb27c;font-size:11pt;letter-spacing:0.04em;{mgn}"><strong>{label}</strong></a>')
    # external read / reference link keeps the light style (not a file download)
    return (f'<a href="{url}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:10px 20px;border-top:2px solid #00b8b8;font-size:11pt;letter-spacing:0.04em;margin:0 10px 10px 0;"><strong>{label}</strong></a>')

def dl_row(url,label):
    # the downloads folder icon perfectly centered beside the file's orange download button
    return ('<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:8px;">'
      f'<img src="{DL_ICON}" alt="" style="width:42px;height:42px;flex:0 0 auto;display:block;" />'
      + dl_link(url,label,row=True) + '</div>')

def vocab_grid(quiz_label, quiz_body, terms):
    # 6 uniform tiles, 3 per row, with an always-on quiz note (framework requirement)
    note=('<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.30);border-left:4px solid #00b8b8;padding:12px 16px;margin-bottom:18px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:5px;"><strong>{quiz_label}</strong></div>'
      f'<div style="font-size:12pt;color:rgba(255,255,255,0.90);line-height:1.5;">{quiz_body}</div></div>')
    cell=('<td style="width:33.33%;vertical-align:top;padding:6px;">'
      '<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;height:100%;box-sizing:border-box;">'
      '<div style="background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:16px;min-height:132px;height:100%;box-sizing:border-box;">'
      '<div style="font-size:12pt;color:#ffffff;margin-bottom:5px;"><strong>{term}</strong></div>'
      '<div style="font-size:10.5pt;line-height:1.5;color:rgba(255,255,255,0.80);">{defn}</div></div></div></td>')
    rows=""
    for i in range(0,len(terms),3):
        rows+='<tr>'+''.join(cell.format(term=t,defn=d) for t,d in terms[i:i+3])+'</tr>'
    return note+f'<table role="presentation" style="width:100%;border-collapse:collapse;table-layout:fixed;"><tbody>{rows}</tbody></table>'

def deliverables_box(title,lead,items):
    lis=""
    for b,rest in items:
        lis+=('<div style="margin-bottom:6px;line-height:1.5;"><span style="color:#00b8b8;">&bull;</span> '
              f'<span style="font-size:13pt;color:rgba(255,255,255,0.90);"><strong>{b}</strong> {rest}</span></div>')
    return ('<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.35);border-left:5px solid #00b8b8;padding:16px 18px;margin:0 0 8px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:8px;"><strong>{title}</strong></div>'
      f'<div style="font-size:13pt;color:#ffffff;margin-bottom:8px;"><strong>{lead}</strong></div>{lis}</div>')

def top_wrap(en,es):
    return ('<div id="top" style="width:100%;margin:0 auto;font-family:Arial,sans-serif;color:#ffffff;background-color:#080808;'
      "background-image:linear-gradient(180deg,rgba(8,8,8,0.97) 0%,rgba(0,56,56,0.94) 50%,rgba(8,8,8,0.97) 100%),"
      f"url('{SITE}/assets/PV_Panther_Watermark.png');"
      'background-position:center center,center center;background-repeat:no-repeat,no-repeat;background-attachment:fixed,fixed;overflow:hidden;">'
      '<div style="padding:28px 28px 40px;">'+en+'</div>'
      '<div id="espanol" style="border-top:2px solid rgba(255,255,255,0.10);"><div style="padding:28px 28px 40px;">'+es+'</div></div>'
      '</div>')

def dot(href,label,title,active,module=False):
    if active: return f'<span class="sdot sdot-active" title="{title}">{label}</span>'
    cls="sdot sdot-link sdot-module" if module else "sdot sdot-link"
    return f'<a href="{href}" class="{cls}" title="{title}">{label}</a>'

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Leading Lines</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

def wrap_page(title,nav_inner,top_html,bottom):
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
  {bottom}
  </div>
  <script>
    function silvaCopyHTML() {{ var el=document.getElementById('top'); navigator.clipboard.writeText(el.outerHTML).then(function(){{var b=document.querySelector('.silva-copy-btn');b.textContent='\\u2713 Copied!';b.classList.add('copied');setTimeout(function(){{b.innerHTML='&#128203; Copy Canvas HTML';b.classList.remove('copied');}},2500);}}).catch(function(){{alert('Copy failed. Select the source manually.');}}); }}
    function silvaDownloadHTML() {{ var el=document.getElementById('top'); var blob=new Blob([el.outerHTML],{{type:'text/html'}}); var url=URL.createObjectURL(blob); var a=document.createElement('a'); a.href=url; a.download=location.pathname.split('/').pop().replace('.html','')+'-canvas.html'; document.body.appendChild(a); a.click(); document.body.removeChild(a); URL.revokeObjectURL(url); }}
  </script>
  <script src="/js/silva-nav.js"></script>
</body>
</html>
'''

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 1A &bull; Leading Lines","Leading Lines Photo Walk","Pair up, take leading-line photos, and cull your best six.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("THE PROJECT / OVERVIEW","Leading Lines on the Walk",
        para("On this photo walk you and a partner hunt for leading lines: lines that pull your eye through a photo toward the subject. You share one class camera, two students per camera. Each of you takes 3 different examples of leading lines. Then you swap photos, cull your best, and turn in 6 photos in all.")
        + framed(HEADER,"Two Pioneer Valley students on a photo walk, one holding a Canon camera, outside the Academy of Arts building"))
    en+=card("THE CONCEPT / WHAT TO LOOK FOR","How Leading Lines Work",
        para("A leading line is any line that guides your eye through the photo. It can be a road, a fence, a hallway, a row of lockers, a shadow, or a crack in the sidewalk. Strong leading lines often run from the front of the photo toward the subject in the back.")
        + para("Sometimes the lines seem to meet at one spot far away. That spot is the vanishing point. Lines that head toward a vanishing point add depth and make a flat photo feel three-dimensional.")
        + '<div style="margin-top:6px;">' + dl_link(ARTICLE,"Read: Leading Lines Guide",download=False) + '</div>')
    en+=card("HOW IT WORKS / YOU AND YOUR PARTNER","Work as a Pair",
        bullets([
            ("Pair up:","two students share one class camera."),
            ("Take:","each person takes 3 different examples of leading lines. Different lines, different spots, not the same photo twice."),
            ("Share:","swap your photos so each partner has the other&rsquo;s 3 examples."),
            ("Cull:","pick the single best photo of each example. You keep your best 3 and your partner&rsquo;s best 3."),
            ("Submit:","turn in 6 photos in all (your 3 plus your partner&rsquo;s 3)."),
        ])
        + note_orange("You take photos as JPG. You will not edit them, so get the photo right in the camera.")
        + note_orange("Take your photos on this walk, on purpose, for this assignment. They must be new photos from today, not old ones."))
    en+=card("VOCABULARY / 6 TERMS","Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Leading Lines","Lines that guide your eye through a photo toward the subject."),
           ("Cull","To look through your photos and keep only the best ones."),
           ("Take","To capture a photo with the camera, as in &ldquo;take a photo.&rdquo;"),
           ("Composition","How you arrange everything inside the frame."),
           ("JPG","A common photo file that is ready to share without editing."),
           ("Vanishing Point","The spot far away where leading lines seem to meet.")]))
    en+=card("REFLECTION / DOWNLOAD","Download Reflection Document",
        para("Download the reflection here. Fill it out after the walk, then turn it in on Step 02. It asks you to name your partner.")
        + dl_row(REFLECT_EN,"Reflection Document (Word)"))

    es=banner("Fotograf&iacute;a 1A &bull; L&iacute;neas Gu&iacute;a","Caminata de L&iacute;neas Gu&iacute;a","Trabaja en pareja, toma fotos de l&iacute;neas gu&iacute;a y selecciona tus mejores seis.","#top","Back to English")
    es+=card("EL PROYECTO / RESUMEN","L&iacute;neas Gu&iacute;a en la Caminata",
        para("En esta caminata fotogr&aacute;fica t&uacute; y un compa&ntilde;ero buscan l&iacute;neas gu&iacute;a: l&iacute;neas que llevan tu mirada a trav&eacute;s de la foto hacia el sujeto. Comparten una c&aacute;mara de la clase, dos estudiantes por c&aacute;mara. Cada uno toma 3 ejemplos diferentes de l&iacute;neas gu&iacute;a. Luego intercambian fotos, seleccionan sus mejores y entregan 6 fotos en total.")
        + framed(HEADER,"Dos estudiantes de Pioneer Valley en una caminata fotogr&aacute;fica, uno con una c&aacute;mara Canon, afuera del edificio Academy of Arts"))
    es+=card("EL CONCEPTO / QU&Eacute; BUSCAR","C&oacute;mo Funcionan las L&iacute;neas Gu&iacute;a",
        para("Una l&iacute;nea gu&iacute;a es cualquier l&iacute;nea que lleva tu mirada a trav&eacute;s de la foto. Puede ser un camino, una reja, un pasillo, una fila de casilleros, una sombra o una grieta en la acera. Las l&iacute;neas gu&iacute;a fuertes suelen ir desde el frente de la foto hacia el sujeto al fondo.")
        + para("A veces las l&iacute;neas parecen unirse en un solo punto a lo lejos. Ese punto es el punto de fuga. Las l&iacute;neas que van hacia un punto de fuga dan profundidad y hacen que una foto plana se sienta tridimensional.")
        + '<div style="margin-top:6px;">' + dl_link(ARTICLE,"Leer: Gu&iacute;a de L&iacute;neas Gu&iacute;a",download=False) + '</div>')
    es+=card("C&Oacute;MO FUNCIONA / T&Uacute; Y TU COMPA&Ntilde;ERO","Trabaja en Pareja",
        bullets([
            ("Formen pareja:","dos estudiantes comparten una c&aacute;mara de la clase."),
            ("Toma:","cada persona toma 3 ejemplos diferentes de l&iacute;neas gu&iacute;a. L&iacute;neas distintas, lugares distintos, no la misma foto dos veces."),
            ("Comparte:","intercambien sus fotos para que cada uno tenga los 3 ejemplos del otro."),
            ("Selecciona (cull):","elige la mejor foto de cada ejemplo. Te quedas con tus mejores 3 y los mejores 3 de tu compa&ntilde;ero."),
            ("Entrega:","entrega 6 fotos en total (tus 3 m&aacute;s los 3 de tu compa&ntilde;ero)."),
        ])
        + note_orange("Tomas las fotos en JPG. No las vas a editar, as&iacute; que logra la foto bien desde la c&aacute;mara.")
        + note_orange("Toma tus fotos en esta caminata, a prop&oacute;sito, para esta tarea. Deben ser fotos nuevas de hoy, no fotos viejas."))
    es+=card("VOCABULARIO / 6 T&Eacute;RMINOS","Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Leading Lines (L&iacute;neas Gu&iacute;a)","L&iacute;neas que llevan tu mirada a trav&eacute;s de la foto hacia el sujeto."),
           ("Cull (Seleccionar)","Revisar tus fotos y quedarte solo con las mejores."),
           ("Take (Tomar)","Capturar una foto con la c&aacute;mara, como en &ldquo;tomar una foto.&rdquo;"),
           ("Composition (Composici&oacute;n)","C&oacute;mo acomodas todo dentro del encuadre."),
           ("JPG","Un archivo de foto com&uacute;n, listo para compartir sin editar."),
           ("Vanishing Point (Punto de Fuga)","El punto a lo lejos donde las l&iacute;neas gu&iacute;a parecen unirse.")]))
    es+=card("REFLEXI&Oacute;N / DESCARGA","Descarga el Documento de Reflexi&oacute;n",
        para("Descarga la reflexi&oacute;n aqu&iacute;. Compl&eacute;tala despu&eacute;s de la caminata y entr&eacute;gala en el Paso 02. Te pide el nombre de tu compa&ntilde;ero.")
        + dl_row(REFLECT_ES,"Documento de Reflexi&oacute;n (Word)"))

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Leading Lines Photo Walk | Photography 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Leading Lines &bull; Step 1","Capture, Cull &amp; Submit","Take your leading lines, then pick your best six.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("CAPTURE / ON THE WALK","Take Your Leading Lines",
        float_right(FLOAT,"A student kneeling to photograph down a long covered walkway whose columns lead the eye to a vanishing point, while a partner watches")
        + para("Pair up and share one class camera, two students per camera. Set the camera to JPG. Then walk campus and hunt for leading lines.")
        + bullets([
            ("Take 3 examples:","each of you takes 3 different examples of leading lines."),
            ("Make each different:","a different line and a different spot each time."),
            ("Get it right in camera:","you will not edit these, so frame it well and check the photo."),
            ("Take a few extra:","take a couple of extra photos of each example so you have choices when you cull."),
        ])
        + '<div style="clear:both;"></div>'
        + note_orange("Take your photos on this walk, on purpose, for this assignment. They must be new photos from today, not old ones."))
    en+=card("SHARE / WITH YOUR PARTNER","Swap Your Photos",
        para("When you both finish, share your photos so each of you has all of them: your 3 examples and your partner&rsquo;s 3 examples.")
        + bullets([
            ("Import first:","bring the camera to a computer and import the photos."),
            ("Share both sets:","give your partner your photos and get theirs, so you each have all six examples as JPGs."),
        ]))
    en+=card("CULL / PICK YOUR BEST","Cull to Your Best 6",
        para("Now cull. Culling means looking through your photos and keeping only the best. For each example, pick the single strongest photo.")
        + bullets([
            ("Your 3:","keep your best photo of each of your 3 examples."),
            ("Your partner&rsquo;s 3:","keep the best photo of each of your partner&rsquo;s 3 examples."),
            ("6 in all:","that is 6 photos, 3 of yours and 3 of your partner&rsquo;s."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own): 6 files",
        [("6 JPGs:","your best 3 leading-line photos and your partner&rsquo;s best 3, uploaded to this Canvas assignment.")])

    es=banner("L&iacute;neas Gu&iacute;a &bull; Paso 1","Captura, Selecciona y Entrega","Toma tus l&iacute;neas gu&iacute;a y luego elige tus mejores seis.","#top","Back to English")
    es+=card("CAPTURA / EN LA CAMINATA","Toma Tus L&iacute;neas Gu&iacute;a",
        float_right(FLOAT,"Un estudiante arrodillado fotografiando por un pasillo largo cuyas columnas gu&iacute;an la mirada hacia un punto de fuga, mientras un compa&ntilde;ero observa")
        + para("Formen pareja y compartan una c&aacute;mara de la clase, dos estudiantes por c&aacute;mara. Pon la c&aacute;mara en JPG. Luego caminen por la escuela y busquen l&iacute;neas gu&iacute;a.")
        + bullets([
            ("Toma 3 ejemplos:","cada uno toma 3 ejemplos diferentes de l&iacute;neas gu&iacute;a."),
            ("Haz cada uno distinto:","una l&iacute;nea distinta y un lugar distinto cada vez."),
            ("Logra la foto en la c&aacute;mara:","no vas a editarlas, as&iacute; que encuadra bien y revisa la foto."),
            ("Toma algunas de m&aacute;s:","toma un par de fotos extra de cada ejemplo para tener opciones al seleccionar."),
        ])
        + '<div style="clear:both;"></div>'
        + note_orange("Toma tus fotos en esta caminata, a prop&oacute;sito, para esta tarea. Deben ser fotos nuevas de hoy, no fotos viejas."))
    es+=card("COMPARTE / CON TU COMPA&Ntilde;ERO","Intercambien Sus Fotos",
        para("Cuando ambos terminen, compartan sus fotos para que cada uno tenga todas: tus 3 ejemplos y los 3 ejemplos de tu compa&ntilde;ero.")
        + bullets([
            ("Importa primero:","lleva la c&aacute;mara a una computadora e importa las fotos."),
            ("Compartan ambos grupos:","dale a tu compa&ntilde;ero tus fotos y recibe las suyas, para que cada uno tenga los seis ejemplos en JPG."),
        ]))
    es+=card("SELECCIONA / ELIGE TUS MEJORES","Selecciona (Cull) Tus Mejores 6",
        para("Ahora selecciona (cull). Seleccionar significa revisar tus fotos y quedarte solo con las mejores. Para cada ejemplo, elige la foto m&aacute;s fuerte.")
        + bullets([
            ("Tus 3:","qu&eacute;date con tu mejor foto de cada uno de tus 3 ejemplos."),
            ("Los 3 de tu compa&ntilde;ero:","qu&eacute;date con la mejor foto de cada uno de los 3 ejemplos de tu compa&ntilde;ero."),
            ("6 en total:","son 6 fotos, 3 tuyas y 3 de tu compa&ntilde;ero."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta): 6 archivos",
        [("6 JPG:","tus mejores 3 fotos de l&iacute;neas gu&iacute;a y las mejores 3 de tu compa&ntilde;ero, subidas a esta tarea de Canvas.")])

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Capture, Cull and Submit | Leading Lines | Photography 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Leading Lines &bull; Step 2","Turn In Your Reflection","Reflect on the walk, your partner, and your photos.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("STEP 02 / REFLECT","Complete and Upload the Reflection",
        para("Finish with a short reflection. It asks you to name your partner, explain what leading lines are, tell how you culled, and pick your favorite photo.")
        + note_orange("The reflection Word document is on the Overview page. Open the Overview to download it.")
        + bullets([
            ("Open it:","open the reflection Word document you downloaded from the Overview."),
            ("Name your partner:","write your partner&rsquo;s full name where it asks."),
            ("Answer every question:","type your answers in the boxes, in full sentences."),
            ("Save and upload:","save the document and upload it to this Canvas assignment."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 reflection:","your completed reflection Word document, with your partner named, uploaded to this Canvas assignment.")])
    en+=note_orange("Answer honestly, in your own words.")

    es=banner("L&iacute;neas Gu&iacute;a &bull; Paso 2","Entrega Tu Reflexi&oacute;n","Reflexiona sobre la caminata, tu compa&ntilde;ero y tus fotos.","#top","Back to English")
    es+=card("PASO 02 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        para("Termina con una reflexi&oacute;n corta. Te pide el nombre de tu compa&ntilde;ero, explicar qu&eacute; son las l&iacute;neas gu&iacute;a, contar c&oacute;mo seleccionaste (cull) y elegir tu foto favorita.")
        + note_orange("El documento de Word de la reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen. Abre el Resumen para descargarlo.")
        + bullets([
            ("&Aacute;brelo:","abre el documento de Word de la reflexi&oacute;n que descargaste del Resumen."),
            ("Nombra a tu compa&ntilde;ero:","escribe el nombre completo de tu compa&ntilde;ero donde lo pide."),
            ("Contesta cada pregunta:","escribe tus respuestas en los cuadros, en oraciones completas."),
            ("Guarda y sube:","guarda el documento y s&uacute;belo a esta tarea de Canvas."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 reflexi&oacute;n:","tu documento de Word de la reflexi&oacute;n, con el nombre de tu compa&ntilde;ero, subido a esta tarea de Canvas.")])
    es+=note_orange("Contesta con honestidad, en tus propias palabras.")

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
    return wrap_page("Step 2: Reflection | Leading Lines | Photography 1A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02)]:
    html=ent(gen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    low=html.lower()
    for w in ["shoot","shooting","shot","shots","shoots","screenshot"]:
        assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
