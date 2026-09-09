#!/usr/bin/env python3
# Photography 2A - Module 04: Build Your Own Preset.
# Students choose a series (natural light portraits, close-ups of flowers, architecture, etc.),
# capture 12+ images that hang together as a series, cull, edit the first image and SAVE a
# Lightroom Classic preset, then sync that preset across the whole series and deliver their best 6.
# Dark teal angular framework. Overview + 4 steps, bilingual EN/ES, 5th-grade.
# Step 02 embeds the scrollable "Presets in Lightroom Classic" slide deck (12 slides + PDF).
import os, re
SITE="https://www.creativesilva.com"
ROOT="/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
IMG=f"{SITE}/assets/images/photo2/build-your-own-preset"
HEADER=f"{IMG}/overview-hero-v1.jpg"
SLIDE=IMG+"/preset-slide-{:02d}.jpg"
SLIDE_PDF=f"{SITE}/assets/course-documents/Build-Your-Own-Preset-Guide.pdf"
REFLECT_EN=f"{SITE}/assets/course-documents/Build-Your-Own-Preset-Reflection-EN.docx"
REFLECT_ES=f"{SITE}/assets/course-documents/Build-Your-Own-Preset-Reflection-ES.docx"

OVER="photo2-preset-overview.html"
S1="photo2-preset-step01-photowalk.html"
S2="photo2-preset-step02-edit-preset.html"
S3="photo2-preset-step03-deliver.html"
S4="photo2-preset-step04-reflection.html"

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

def steps(items):
    # numbered teal circles, like the slide deck's own step list
    r=""
    for i,(b,rest) in enumerate(items,1):
        r+=('<div style="display:flex;align-items:flex-start;gap:12px;margin-bottom:12px;">'
            f'<span style="flex:0 0 auto;width:26px;height:26px;border-radius:50%;background:#FF6B1A;color:#ffffff;font-size:12pt;line-height:26px;text-align:center;"><strong>{i}</strong></span>'
            f'<span style="font-size:13.5pt;color:rgba(255,255,255,0.88);line-height:1.5;"><strong>{b}</strong> {rest}</span></div>')
    return f'<div style="margin:4px 0 6px;">{r}</div>'

def note_orange(t):
    return (f'<div style="background:rgba(255,107,26,0.10);border:1px solid rgba(255,107,26,0.30);border-left:4px solid #FF6B1A;padding:11px 14px;margin:8px 0;font-size:12pt;color:rgba(255,255,255,0.90);"><strong>{t}</strong></div>')

def framed(src,alt):
    return (f'<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;margin:6px 0 4px;">'
      f'<img src="{src}" alt="{alt}" style="display:block;width:100%;height:auto;" /></div>')

DL_ICON=f"{SITE}/assets/Icons/assignment/downloads-v1.png"

def dl_link(url,label,download=True,row=False):
    if download:
        mgn='margin:0;' if row else 'margin:0 10px 8px 0;'
        return (f'<a href="{url}" download style="display:inline-block;text-decoration:none;background:#FF6B1A;color:#ffffff;padding:11px 22px;border-top:2px solid #ffb27c;font-size:11pt;letter-spacing:0.04em;{mgn}"><strong>{label}</strong></a>')
    return (f'<a href="{url}" target="_blank" rel="noopener" style="display:inline-block;text-decoration:none;background:rgba(255,255,255,0.92);color:#003838;padding:10px 20px;border-top:2px solid #00b8b8;font-size:11pt;letter-spacing:0.04em;margin:0 10px 10px 0;"><strong>{label}</strong></a>')

def dl_row(url,label):
    return ('<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:8px;">'
      f'<img src="{DL_ICON}" alt="" style="width:42px;height:42px;flex:0 0 auto;display:block;" />'
      + dl_link(url,label,row=True) + '</div>')

def slide_deck(es):
    # 16:11 scrollable viewer: a 16:9 slide fills the window and the top of the next slide
    # peeks in, so students know to scroll. Orange PDF button sits above it.
    hint=('Scroll inside the window to see all 12 slides' if not es
          else 'Despl&aacute;zate en la ventana para ver las 12 diapositivas')
    pdf_lbl=('Download the Slides (PDF)' if not es else 'Descarga las Diapositivas (PDF)')
    alt_lbl=('Presets in Lightroom Classic, slide {} of 12' if not es
             else 'Presets en Lightroom Classic, diapositiva {} de 12')
    imgs=""
    for i in range(1,13):
        imgs+=('<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;margin:0 0 12px;">'
               f'<img src="{SLIDE.format(i)}" alt="{alt_lbl.format(i)}" style="display:block;width:100%;height:auto;" /></div>')
    return ('<div style="margin-bottom:12px;">'
      f'<a href="{SLIDE_PDF}" download style="display:inline-block;background:#FF6B1A;color:#ffffff;text-decoration:none;padding:11px 22px;border-top:2px solid #ffb27c;font-size:11pt;letter-spacing:0.04em;"><strong>&#128229; {pdf_lbl}</strong></a></div>'
      f'<div style="font-size:11pt;color:#80e0e0;margin-bottom:8px;opacity:0.9;">&#8595; {hint}</div>'
      '<div class="silva-scroll" style="aspect-ratio:16/11;max-height:82vh;overflow-y:auto;-webkit-overflow-scrolling:touch;border:1px solid rgba(0,184,184,0.22);background:rgba(0,0,0,0.22);padding:8px;box-sizing:border-box;">'
      + imgs + '</div>')

def vocab_grid(quiz_label, quiz_body, terms):
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
            f'        <a href="{OVER}" class="bc-hide-sm">Build Your Own Preset</a>\n'
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

DOTS_TITLES=[("M","Overview"),("1","Step 01"),("2","Step 02"),("3","Step 03"),("4","Step 04")]
def dots_for(active_idx):
    hrefs=[OVER,S1,S2,S3,S4]
    r=""
    for i,(lab,title) in enumerate(DOTS_TITLES):
        r+=dot("" if i==active_idx else hrefs[i], lab, title, i==active_idx, module=(i==0 and active_idx!=0))
    return r

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Photography 2A &bull; Module 04","Build Your Own Preset","Capture a series, edit one photo, and save your look as a preset.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("THE PROJECT / OVERVIEW","Make a Look, Then Save It",
        para("In this project you pick a subject you love and capture a whole series of it: natural light portraits, close-ups of flowers, buildings on campus, or your own idea. You capture at least 12 images that go together, edit the first one until it looks the way you want, and then save those edits as a preset. A preset is your look, saved once, ready to drop on every photo in the series.")
        + para("Then you sync your preset across the series so all your photos share the same feel, pick your best 6, and turn them in.")
        + framed(HEADER,"A Lightroom Classic edit of a natural light portrait, with the Develop panel sliders open on the right"))
    en+=card("THE CONCEPT / WHAT IS A PRESET","One Look, Every Photo",
        para("A preset saves all your Develop settings in one click: white balance, exposure, contrast, color, and more. Once you save it, you can add that same look to one photo or a hundred photos at the same time.")
        + para("This is how photographers keep a series looking like it belongs together. Same light, same mood, same colors. Build the look once, then let the preset do the repeat work for you.")
        + bullets([
            ("Pick a series:","one subject and one kind of light, so your photos naturally match."),
            ("Edit one photo:","get your first image looking exactly how you want."),
            ("Save it as a preset:","turn those edits into your own reusable look."),
            ("Sync the rest:","push that look onto every photo in your series at once."),
        ]))
    en+=card("HOW IT WORKS / YOUR PLAN","Your Four Steps",
        steps([
            ("Photo Walk, Capture &amp; Cull:","choose your series and capture 12 or more images that work together. Cull to your strongest, then turn in a 12-image contact sheet."),
            ("Edit &amp; Create Your Preset:","edit your first image in the Develop module, then save those settings as a preset. Turn in your preset file."),
            ("Deliver Your Series:","sync your preset across the series, fine-tune, and turn in a 6-image contact sheet plus all 6 high-resolution images."),
            ("Reflection:","tell the story of your series and your preset."),
        ])
        + note_orange("Capture your photos on purpose for this project. They must be new images you take for this assignment, not pictures already in your camera roll from before."))
    en+=card("VOCABULARY / 6 TERMS","Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words will show up on your quizzes, the mid-semester quiz and the end-of-semester quiz before finals. Learn them now, not the night before.",
          [("Preset","Saved Develop settings you can add to any photo in one click."),
           ("Sync","To push one photo&rsquo;s settings onto all the other photos you selected."),
           ("White Balance","The setting that makes the colors look warm, cool, or true to life."),
           ("Exposure","How bright or dark the whole photo is."),
           ("Contrast","The difference between the darkest darks and the brightest lights."),
           ("HSL","Hue, Saturation, Luminance: the panel that lets you change each color on its own.")]))
    en+=card("REFLECTION / DOWNLOAD","Download Reflection Document",
        para("Download the reflection here. Fill it out after you finish your series, then turn it in on Step 04.")
        + dl_row(REFLECT_EN,"Reflection Document (Word)"))

    es=banner("Fotograf&iacute;a 2A &bull; M&oacute;dulo 04","Crea Tu Propio Preset","Captura una serie, edita una foto y guarda tu estilo como preset.","#top","Back to English")
    es+=card("EL PROYECTO / RESUMEN","Crea un Estilo y Gu&aacute;rdalo",
        para("En este proyecto eliges un tema que te encante y capturas toda una serie: retratos con luz natural, primeros planos de flores, edificios de la escuela o tu propia idea. Capturas al menos 12 im&aacute;genes que van juntas, editas la primera hasta que se vea como quieres, y luego guardas esos ajustes como un preset. Un preset es tu estilo, guardado una vez, listo para poner en cada foto de la serie.")
        + para("Despu&eacute;s sincronizas tu preset en toda la serie para que todas tus fotos tengan la misma sensaci&oacute;n, eliges tus mejores 6 y las entregas.")
        + framed(HEADER,"Una edici&oacute;n en Lightroom Classic de un retrato con luz natural, con los controles del panel Revelar abiertos a la derecha"))
    es+=card("EL CONCEPTO / QU&Eacute; ES UN PRESET","Un Estilo, Todas las Fotos",
        para("Un preset guarda todos tus ajustes de Revelar con un clic: balance de blancos, exposici&oacute;n, contraste, color y m&aacute;s. Una vez que lo guardas, puedes poner ese mismo estilo en una foto o en cien fotos al mismo tiempo.")
        + para("As&iacute; es como los fot&oacute;grafos logran que una serie se vea unida. La misma luz, el mismo &aacute;nimo, los mismos colores. Crea el estilo una vez y deja que el preset haga el trabajo repetido por ti.")
        + bullets([
            ("Elige una serie:","un tema y un tipo de luz, para que tus fotos combinen de forma natural."),
            ("Edita una foto:","logra que tu primera imagen se vea justo como quieres."),
            ("Gu&aacute;rdala como preset:","convierte esos ajustes en tu propio estilo reutilizable."),
            ("Sincroniza el resto:","pon ese estilo en cada foto de tu serie de una vez."),
        ]))
    es+=card("C&Oacute;MO FUNCIONA / TU PLAN","Tus Cuatro Pasos",
        steps([
            ("Caminata, Captura y Selecci&oacute;n:","elige tu serie y captura 12 o m&aacute;s im&aacute;genes que van juntas. Selecciona (cull) tus mejores y entrega una hoja de contactos de 12 im&aacute;genes."),
            ("Edita y Crea Tu Preset:","edita tu primera imagen en el m&oacute;dulo Revelar y guarda esos ajustes como un preset. Entrega tu archivo de preset."),
            ("Entrega Tu Serie:","sincroniza tu preset en la serie, haz ajustes finos y entrega una hoja de contactos de 6 im&aacute;genes m&aacute;s las 6 im&aacute;genes en alta resoluci&oacute;n."),
            ("Reflexi&oacute;n:","cuenta la historia de tu serie y tu preset."),
        ])
        + note_orange("Captura tus fotos a prop&oacute;sito para este proyecto. Deben ser im&aacute;genes nuevas que tomes para esta tarea, no fotos que ya ten&iacute;as en tu galer&iacute;a de antes."))
    es+=card("VOCABULARIO / 6 T&Eacute;RMINOS","Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave aparecer&aacute;n en tus ex&aacute;menes, el examen de mitad de semestre y el de fin de semestre antes de los finales. Apr&eacute;ndelas ahora, no la noche anterior.",
          [("Preset","Ajustes de Revelar guardados que puedes poner en cualquier foto con un clic."),
           ("Sync (Sincronizar)","Poner los ajustes de una foto en todas las dem&aacute;s fotos que seleccionaste."),
           ("White Balance (Balance de Blancos)","El ajuste que hace que los colores se vean c&aacute;lidos, fr&iacute;os o reales."),
           ("Exposure (Exposici&oacute;n)","Qu&eacute; tan clara u oscura est&aacute; toda la foto."),
           ("Contrast (Contraste)","La diferencia entre las sombras m&aacute;s oscuras y las luces m&aacute;s brillantes."),
           ("HSL","Tono, Saturaci&oacute;n, Luminancia: el panel que te deja cambiar cada color por separado.")]))
    es+=card("REFLEXI&Oacute;N / DESCARGA","Descarga el Documento de Reflexi&oacute;n",
        para("Descarga la reflexi&oacute;n aqu&iacute;. Compl&eacute;tala despu&eacute;s de terminar tu serie y entr&eacute;gala en el Paso 04.")
        + dl_row(REFLECT_ES,"Documento de Reflexi&oacute;n (Word)"))

    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Build Your Own Preset | Photography 2A | PVHS", nav("Overview",dots_for(0),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Build Your Own Preset &bull; Step 1","Photo Walk: Capture &amp; Cull","Pick a series, capture 12 or more, then turn in a contact sheet.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("CHOOSE / YOUR SERIES","Pick One Subject and One Light",
        para("A series is a group of photos that belong together. To make that happen, pick one subject and one kind of light, then stick with it. When your photos already match, your preset will make them match even more.")
        + bullets([
            ("Pick your subject:","natural light portraits, close-ups of flowers, buildings and lines on campus, or your own idea."),
            ("Pick your light:","keep the light similar across the whole series, like soft shade or golden late-day light."),
            ("Keep the look steady:","same subject, same feel, so the photos read as one set."),
        ]))
    en+=card("CAPTURE / 12 OR MORE","Capture Your Series",
        para("Now go capture your series. Take at least 12 images that work together. Move around, try different angles, and get close, but keep the subject and the light consistent.")
        + bullets([
            ("At least 12 images:","capture more than you need so you have strong ones to choose from."),
            ("Keep them consistent:","same subject and similar light, so one preset will fit them all."),
            ("Watch your framing:","fill the frame and keep your subject sharp."),
        ])
        + note_orange("Capture your photos on purpose for this project. They must be new images you take for this assignment, not pictures already in your camera roll from before."))
    en+=card("CULL / KEEP THE STRONG ONES","Import and Cull",
        para("Bring your photos into Lightroom Classic, then cull. Culling means looking through your photos and keeping the strongest ones. Drop the blurry, the too-dark, and the repeats.")
        + bullets([
            ("Import:","bring the whole series into Lightroom Classic."),
            ("Cull:","keep at least 12 strong images that go together as a series."),
        ]))
    en+=card("CONTACT SHEET / SHOW YOUR SERIES","Make Your 12-Image Contact Sheet",
        para("A contact sheet is one page that shows all your photos as small thumbnails. Make yours with the 12-Up contact sheet layout in the Lightroom Classic Print module, then save it as a JPG or PDF.")
        + bullets([
            ("Select your 12:","pick the images from your culled series."),
            ("Use the 12-Up layout:","in the Print module, choose the 12-Up contact sheet."),
            ("Save the page:","export the contact sheet as a JPG or PDF to turn in."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 contact sheet:","your 12-image contact sheet (JPG or PDF), showing your culled series, uploaded to this Canvas assignment.")])

    es=banner("Crea Tu Propio Preset &bull; Paso 1","Caminata: Captura y Selecci&oacute;n","Elige una serie, captura 12 o m&aacute;s y entrega una hoja de contactos.","#top","Back to English")
    es+=card("ELIGE / TU SERIE","Elige un Tema y una Luz",
        para("Una serie es un grupo de fotos que van juntas. Para lograrlo, elige un tema y un tipo de luz, y qu&eacute;date con eso. Cuando tus fotos ya combinan, tu preset las har&aacute; combinar a&uacute;n m&aacute;s.")
        + bullets([
            ("Elige tu tema:","retratos con luz natural, primeros planos de flores, edificios y l&iacute;neas de la escuela, o tu propia idea."),
            ("Elige tu luz:","mant&eacute;n la luz parecida en toda la serie, como sombra suave o la luz dorada del atardecer."),
            ("Mant&eacute;n el estilo:","el mismo tema, la misma sensaci&oacute;n, para que las fotos se lean como un solo grupo."),
        ]))
    es+=card("CAPTURA / 12 O M&Aacute;S","Captura Tu Serie",
        para("Ahora ve a capturar tu serie. Toma al menos 12 im&aacute;genes que van juntas. Mu&eacute;vete, prueba diferentes &aacute;ngulos y ac&eacute;rcate, pero mant&eacute;n el tema y la luz consistentes.")
        + bullets([
            ("Al menos 12 im&aacute;genes:","captura m&aacute;s de las que necesitas para tener buenas opciones."),
            ("Mant&eacute;nlas consistentes:","mismo tema y luz parecida, para que un preset les quede a todas."),
            ("Cuida el encuadre:","llena el cuadro y mant&eacute;n tu sujeto n&iacute;tido."),
        ])
        + note_orange("Captura tus fotos a prop&oacute;sito para este proyecto. Deben ser im&aacute;genes nuevas que tomes para esta tarea, no fotos que ya ten&iacute;as en tu galer&iacute;a de antes."))
    es+=card("SELECCIONA / QU&Eacute;DATE CON LAS FUERTES","Importa y Selecciona",
        para("Lleva tus fotos a Lightroom Classic y luego selecciona (cull). Seleccionar significa revisar tus fotos y quedarte con las m&aacute;s fuertes. Descarta las borrosas, las muy oscuras y las repetidas.")
        + bullets([
            ("Importa:","lleva toda la serie a Lightroom Classic."),
            ("Selecciona:","qu&eacute;date con al menos 12 im&aacute;genes fuertes que van juntas como serie."),
        ]))
    es+=card("HOJA DE CONTACTOS / MUESTRA TU SERIE","Crea Tu Hoja de Contactos de 12 Im&aacute;genes",
        para("Una hoja de contactos es una p&aacute;gina que muestra todas tus fotos como miniaturas. Crea la tuya con el dise&ntilde;o de hoja de contactos de 12 en el m&oacute;dulo Imprimir de Lightroom Classic, y gu&aacute;rdala como JPG o PDF.")
        + bullets([
            ("Selecciona tus 12:","elige las im&aacute;genes de tu serie seleccionada."),
            ("Usa el dise&ntilde;o de 12:","en el m&oacute;dulo Imprimir, elige la hoja de contactos de 12."),
            ("Guarda la p&aacute;gina:","exporta la hoja de contactos como JPG o PDF para entregar."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 hoja de contactos:","tu hoja de contactos de 12 im&aacute;genes (JPG o PDF), que muestra tu serie seleccionada, subida a esta tarea de Canvas.")])

    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Photo Walk, Capture and Cull | Build Your Own Preset | Photography 2A | PVHS", nav("Step 01",dots_for(1),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Build Your Own Preset &bull; Step 2","Edit &amp; Create Your Preset","Edit your first image, then save your look as a preset.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("WATCH / THE SLIDE DECK","Presets in Lightroom Classic",
        para("Start here. This slide deck walks you through what a preset is, how to edit your look, and how to save it. Scroll through all 12 slides, and download the PDF if you want to keep it open while you work.")
        + slide_deck(False))
    en+=card("EDIT / YOUR FIRST IMAGE","Build Your Look on One Photo",
        para("Pick the strongest image from your series. Open it in the Develop module and edit it until it looks exactly how you want. This one photo becomes the recipe for the whole series.")
        + bullets([
            ("Open in Develop:","select your best image and press D to open the Develop module."),
            ("White Balance:","set the colors warm, cool, or true to life to match the mood you want."),
            ("Exposure and Contrast:","get the brightness right, then add or lower contrast for punch."),
            ("Color with HSL:","use the HSL panel to make each color pop or calm down."),
        ])
        + note_orange("Make real changes. Your preset is only as good as the look you build here."))
    en+=card("CREATE / SAVE YOUR PRESET","Save Your Look as a Preset",
        para("Now save those settings as your own preset so you can add them to any photo with one click.")
        + steps([
            ("Open the Presets panel:","on the left side of the Develop module, find the Presets panel."),
            ("Click the plus:","click the + at the top of the panel, then choose Create Preset."),
            ("Name it:","give your preset a clear name, like &ldquo;Golden Portraits&rdquo; or &ldquo;Flower Close-Ups.&rdquo;"),
            ("Check the settings:","keep the boxes checked for the settings you changed, then click Create."),
            ("Export the file:","right-click your preset in the panel and choose Export. Save the .xmp file so you can turn it in."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 preset file:","your exported Lightroom preset (the .xmp file), uploaded to this Canvas assignment.")])

    es=banner("Crea Tu Propio Preset &bull; Paso 2","Edita y Crea Tu Preset","Edita tu primera imagen y guarda tu estilo como preset.","#top","Back to English")
    es+=card("MIRA / LAS DIAPOSITIVAS","Presets en Lightroom Classic",
        para("Empieza aqu&iacute;. Estas diapositivas te explican qu&eacute; es un preset, c&oacute;mo editar tu estilo y c&oacute;mo guardarlo. Despl&aacute;zate por las 12 diapositivas y descarga el PDF si quieres tenerlo abierto mientras trabajas.")
        + slide_deck(True))
    es+=card("EDITA / TU PRIMERA IMAGEN","Crea Tu Estilo en Una Foto",
        para("Elige la imagen m&aacute;s fuerte de tu serie. &Aacute;brela en el m&oacute;dulo Revelar y ed&iacute;tala hasta que se vea justo como quieres. Esta foto se convierte en la receta para toda la serie.")
        + bullets([
            ("Abre en Revelar:","selecciona tu mejor imagen y presiona D para abrir el m&oacute;dulo Revelar."),
            ("Balance de Blancos:","ajusta los colores c&aacute;lidos, fr&iacute;os o reales para lograr el &aacute;nimo que quieres."),
            ("Exposici&oacute;n y Contraste:","logra el brillo correcto y luego sube o baja el contraste para dar fuerza."),
            ("Color con HSL:","usa el panel HSL para hacer que cada color resalte o se calme."),
        ])
        + note_orange("Haz cambios de verdad. Tu preset ser&aacute; tan bueno como el estilo que crees aqu&iacute;."))
    es+=card("CREA / GUARDA TU PRESET","Guarda Tu Estilo como Preset",
        para("Ahora guarda esos ajustes como tu propio preset para poder ponerlos en cualquier foto con un clic.")
        + steps([
            ("Abre el panel de Presets:","del lado izquierdo del m&oacute;dulo Revelar, busca el panel de Presets."),
            ("Haz clic en el m&aacute;s:","haz clic en el + arriba del panel y elige Crear Preset."),
            ("P&oacute;nle nombre:","dale a tu preset un nombre claro, como &ldquo;Retratos Dorados&rdquo; o &ldquo;Flores de Cerca.&rdquo;"),
            ("Revisa los ajustes:","deja marcadas las casillas de los ajustes que cambiaste y haz clic en Crear."),
            ("Exporta el archivo:","haz clic derecho en tu preset y elige Exportar. Guarda el archivo .xmp para poder entregarlo."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 archivo de preset:","tu preset de Lightroom exportado (el archivo .xmp), subido a esta tarea de Canvas.")])

    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a><a href="{S3}" class="silva-step-btn">Step 03 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><a href="{S3}" class="silva-bottom-btn">Step 03 &#8594;</a></div>'
    return wrap_page("Step 2: Edit and Create Your Preset | Build Your Own Preset | Photography 2A | PVHS", nav("Step 02",dots_for(2),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 03 ----------------
def step03():
    en=banner("Build Your Own Preset &bull; Step 3","Deliver Your Series","Sync your preset, fine-tune, and turn in your best six.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("APPLY / SYNC YOUR PRESET","Put Your Look on the Whole Series",
        para("This is where your preset saves you time. Add your look to every photo in your series at once.")
        + steps([
            ("Go to the Library:","press G for Grid view. You will see all your photos as thumbnails."),
            ("Select your series:","click the first photo, then hold Shift and click the last one to select them all."),
            ("Switch to Develop:","press D. Your first photo opens, and the rest stay selected in the filmstrip."),
            ("Apply your preset:","click your preset in the Presets panel, then click Sync at the bottom right to push it to all the selected photos."),
        ]))
    en+=card("FINE-TUNE / EACH IMAGE","Fix the Ones That Need It",
        para("Your preset gets you most of the way, but every photo is a little different. Click through the filmstrip and fix any photo that still needs work.")
        + bullets([
            ("Check each photo:","click through your series in the filmstrip."),
            ("Adjust as needed:","nudge Exposure or White Balance on any photo that looks off."),
            ("Keep the look:","small fixes only, so the series still feels like one set."),
        ]))
    en+=card("DELIVER / YOUR BEST SIX","Export and Make Your Final Contact Sheet",
        para("Now pick your 6 strongest images. Export them at high resolution, and make a 6-image contact sheet with the 6-Up contact sheet layout in the Print module.")
        + bullets([
            ("Pick your best 6:","choose the 6 strongest photos from your synced series."),
            ("Export high-resolution:","export the 6 as high-quality JPGs."),
            ("Make the 6-Up contact sheet:","use the 6-Up layout in the Print module, then save it as a JPG or PDF."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own): 7 files",
        [("1 contact sheet:","your 6-image contact sheet (JPG or PDF)."),
         ("6 high-resolution images:","your 6 best photos, exported at high resolution, uploaded to this Canvas assignment.")])

    es=banner("Crea Tu Propio Preset &bull; Paso 3","Entrega Tu Serie","Sincroniza tu preset, haz ajustes y entrega tus mejores seis.","#top","Back to English")
    es+=card("APLICA / SINCRONIZA TU PRESET","Pon Tu Estilo en Toda la Serie",
        para("Aqu&iacute; es donde tu preset te ahorra tiempo. Pon tu estilo en cada foto de tu serie de una vez.")
        + steps([
            ("Ve a la Biblioteca:","presiona G para la vista de Cuadr&iacute;cula. Ver&aacute;s todas tus fotos como miniaturas."),
            ("Selecciona tu serie:","haz clic en la primera foto, luego mant&eacute;n Shift y haz clic en la &uacute;ltima para seleccionarlas todas."),
            ("Cambia a Revelar:","presiona D. Se abre tu primera foto y las dem&aacute;s siguen seleccionadas en la tira de diapositivas."),
            ("Aplica tu preset:","haz clic en tu preset en el panel de Presets y luego en Sincronizar abajo a la derecha para ponerlo en todas las fotos seleccionadas."),
        ]))
    es+=card("AJUSTA / CADA IMAGEN","Arregla las que lo Necesiten",
        para("Tu preset te lleva casi todo el camino, pero cada foto es un poco diferente. Revisa la tira de diapositivas y arregla cualquier foto que a&uacute;n lo necesite.")
        + bullets([
            ("Revisa cada foto:","haz clic por tu serie en la tira de diapositivas."),
            ("Ajusta si hace falta:","mueve un poco la Exposici&oacute;n o el Balance de Blancos en cualquier foto que se vea mal."),
            ("Mant&eacute;n el estilo:","solo arreglos peque&ntilde;os, para que la serie siga sinti&eacute;ndose como un grupo."),
        ]))
    es+=card("ENTREGA / TUS MEJORES SEIS","Exporta y Crea Tu Hoja de Contactos Final",
        para("Ahora elige tus 6 im&aacute;genes m&aacute;s fuertes. Exp&oacute;rtalas en alta resoluci&oacute;n y crea una hoja de contactos de 6 im&aacute;genes con el dise&ntilde;o de hoja de contactos de 6 en el m&oacute;dulo Imprimir.")
        + bullets([
            ("Elige tus mejores 6:","escoge las 6 fotos m&aacute;s fuertes de tu serie sincronizada."),
            ("Exporta en alta resoluci&oacute;n:","exporta las 6 como JPG de alta calidad."),
            ("Crea la hoja de 6:","usa el dise&ntilde;o de 6 en el m&oacute;dulo Imprimir y gu&aacute;rdala como JPG o PDF."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta): 7 archivos",
        [("1 hoja de contactos:","tu hoja de contactos de 6 im&aacute;genes (JPG o PDF)."),
         ("6 im&aacute;genes en alta resoluci&oacute;n:","tus 6 mejores fotos, exportadas en alta resoluci&oacute;n, subidas a esta tarea de Canvas.")])

    stepnav=f'<a href="{S2}" class="silva-step-btn">&#8592; Step 02</a><a href="{S4}" class="silva-step-btn">Step 04 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S2}" class="silva-bottom-btn">&#8592; Step 02</a><a href="{S4}" class="silva-bottom-btn">Step 04 &#8594;</a></div>'
    return wrap_page("Step 3: Deliver Your Series | Build Your Own Preset | Photography 2A | PVHS", nav("Step 03",dots_for(3),stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 04 ----------------
def step04():
    en=banner("Build Your Own Preset &bull; Step 4","Reflection","Tell the story of your series and your preset.","#espanol","Clic para Espa&ntilde;ol")
    en+=card("STEP 04 / REFLECT","Complete and Upload the Reflection",
        para("Finish with a short reflection. It asks about the series you chose, the look you built, how your preset worked across your photos, and what you would do differently next time.")
        + note_orange("The reflection is on this module&rsquo;s Overview page: the first page of this module, marked M in the steps at the top. Open it to download the reflection.")
        + bullets([
            ("Open it:","open the reflection Word document from this module&rsquo;s Overview page (marked M at the top)."),
            ("Answer every question:","type your answers in the boxes, in full sentences."),
            ("Save and upload:","save the document and upload it to this Canvas assignment."),
        ]))
    en+=deliverables_box("DELIVERABLES &middot; TURN IT IN","Turn in for this step (graded on its own):",
        [("1 reflection:","your completed reflection Word document, uploaded to this Canvas assignment.")])
    en+=note_orange("Answer honestly, in your own words.")

    es=banner("Crea Tu Propio Preset &bull; Paso 4","Reflexi&oacute;n","Cuenta la historia de tu serie y tu preset.","#top","Back to English")
    es+=card("PASO 04 / REFLEXIONA","Completa y Sube la Reflexi&oacute;n",
        para("Termina con una reflexi&oacute;n corta. Te pregunta sobre la serie que elegiste, el estilo que creaste, c&oacute;mo funcion&oacute; tu preset en tus fotos y qu&eacute; har&iacute;as diferente la pr&oacute;xima vez.")
        + note_orange("La reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo: la primera p&aacute;gina de este m&oacute;dulo, marcada con M en los pasos de arriba. &Aacute;brela para descargar la reflexi&oacute;n.")
        + bullets([
            ("&Aacute;brelo:","abre el documento de Word de la reflexi&oacute;n desde la p&aacute;gina de Resumen de este m&oacute;dulo (marcada con M arriba)."),
            ("Contesta cada pregunta:","escribe tus respuestas en los cuadros, en oraciones completas."),
            ("Guarda y sube:","guarda el documento y s&uacute;belo a esta tarea de Canvas."),
        ]))
    es+=deliverables_box("ENTREGABLES &middot; ENTR&Eacute;GALO","Entrega en este paso (se califica por su cuenta):",
        [("1 reflexi&oacute;n:","tu documento de Word de la reflexi&oacute;n completado, subido a esta tarea de Canvas.")])
    es+=note_orange("Contesta con honestidad, en tus propias palabras.")

    stepnav=f'<a href="{S3}" class="silva-step-btn">&#8592; Step 03</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S3}" class="silva-bottom-btn">&#8592; Step 03</a><span></span></div>'
    return wrap_page("Step 4: Reflection | Build Your Own Preset | Photography 2A | PVHS", nav("Step 04",dots_for(4),stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02),(S3,step03),(S4,step04)]:
    html=ent(gen())
    assert "—" not in html and "&mdash;" not in html, "em dash in "+fname
    low=html.lower()
    for w in ["shoot","shooting","shot","shots","shoots","screenshot"]:
        assert not re.search(r'\b'+w+r'\b', low), f"banned '{w}' in {fname}"
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
