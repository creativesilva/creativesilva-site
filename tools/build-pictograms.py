#!/usr/bin/env python3
# Digital Arts 1A - Module: Pictograms.
# Find and save real pictograms, then reimagine 3 by hand in the sketchbook and reflect.
# No camera, no own-device capture (students collect existing pictograms online), so no
# fresh-photos note and no header module-type icon. Chip-header framework via silva_framework.
# Overview + 2 steps, bilingual EN/ES, 5th-grade. No downloadable resources (handwritten work).
import os
from silva_framework import *

ROOT=os.path.join(os.path.dirname(__file__),"..")
IMG=f"{SITE}/assets/images/digarts1/pictograms"
HERO=f"{IMG}/pictograms-hero-v2.png"
HAZARD=f"{IMG}/hazard-pictograms-transparent.png"
FIND_FLOAT=f"{IMG}/pictograms-step01-float-v2.png"
SKETCH_FLOAT=f"{IMG}/pictograms-sketch-float-v1.png"

OVER="digarts1-pictograms-overview.html"
S1="digarts1-pictograms-step01-find-save.html"
S2="digarts1-pictograms-step02-sketch-reflect.html"

# ---- module-local helpers (cohesive teal, no framework equivalent) ----
def examples(items):
    # row of sign examples on a white cell so the dark/transparent signs read; teal frame + caption.
    cells=""
    for src,label in items:
        cells+=('<div style="flex:1 1 140px;min-width:0;">'
          '<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">'
          f'<div style="background:#ffffff;padding:10px;"><img src="{src}" alt="{label}" style="display:block;width:100%;height:auto;" /></div></div>'
          f'<div style="text-align:center;font-size:10.5pt;color:#80e0e0;margin-top:6px;"><strong>{label}</strong></div></div>')
    return f'<div style="display:flex;flex-wrap:wrap;gap:12px;margin:8px 0 4px;">{cells}</div>'

def pills(labels):
    r="".join('<span style="display:inline-block;background:rgba(0,116,116,0.22);border:1px solid rgba(0,184,184,0.35);'
      'color:#80e0e0;font-size:10.5pt;letter-spacing:0.06em;text-transform:uppercase;padding:6px 12px;margin:0 8px 8px 0;">'
      f'<strong>{t}</strong></span>' for t in labels)
    return f'<div style="margin:6px 0 4px;">{r}</div>'

def hazard_img(alt,cap):
    return ('<div style="margin:10px 0 4px;text-align:center;">'
      f'<img src="{HAZARD}" alt="{alt}" style="display:block;width:100%;height:auto;margin:0 auto;" />'
      f'<div style="font-size:10.5pt;color:#80e0e0;margin-top:10px;"><strong>{cap}</strong></div></div>')

def teal_callout(label,body):
    # labeled teal callout, cohesive inside a teal content card (was a red box in the old page).
    return ('<div style="background:rgba(0,184,184,0.10);border:1px solid rgba(0,184,184,0.30);border-left:4px solid #00b8b8;padding:14px 16px;margin:4px 0 16px;">'
      f'<div style="font-size:9.5pt;letter-spacing:0.2em;text-transform:uppercase;color:#80e0e0;margin-bottom:5px;"><strong>{label}</strong></div>'
      f'<div style="font-size:13pt;color:rgba(255,255,255,0.92);line-height:1.5;">{body}</div></div>')

def subcols(pairs):
    # full-width flex row of teal sub-panels (title + bullet list); wraps to stack when narrow.
    cells=""
    for title,its in pairs:
        lis="".join('<div style="margin-bottom:6px;line-height:1.45;"><span style="color:#00b8b8;">&bull;</span> '
          f'<span style="font-size:11.5pt;color:rgba(255,255,255,0.84);">{it}</span></div>' for it in its)
        cells+=('<div style="flex:1 1 260px;min-width:0;background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">'
          '<div style="background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:18px;height:100%;box-sizing:border-box;">'
          f'<div style="font-size:12pt;letter-spacing:0.04em;color:#5eead4;margin:2px 0 10px;"><strong>{title}</strong></div>{lis}</div></div>')
    return f'<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:6px;">{cells}</div>'

def nav(current,dots,stepnav):
    return ('      <div class="silva-breadcrumb">\n'
            '        <a href="/curriculum.html">Curriculum Catalog</a>\n'
            '        <span class="bc-sep">&rsaquo;</span>\n'
            f'        <a href="{OVER}" class="bc-hide-sm">Pictograms</a>\n'
            '        <span class="bc-sep bc-hide-sm">&rsaquo;</span>\n'
            f'        <span class="bc-current">{current}</span>\n'
            '      </div>\n'
            '      <div class="silva-nav-spacer"></div>\n'
            f'      <div class="silva-dots" aria-label="Module progress">{dots}</div>\n'
            f'      <div class="silva-step-nav">{stepnav}</div>')

# ---------------- OVERVIEW ----------------
def overview():
    en=banner("Digital Arts 1A &bull; Pictograms","Pictograms","Simple pictures that speak with no words.","#espanol","Clic para Espa&ntilde;ol")
    en+=type_card("overview","The Module Overview","What Is a Pictogram?",
        para("A pictogram is a simple picture that stands for an idea, an object, or an action. The best part is that you understand it without reading a single word. You just look at it and know what it means.")
        + framed(HERO,"Pictograms"))
    en+=card("","Pictograms You Already Know",
        para("You already know a lot of them: a stop sign, a warning sign, a flammable symbol, or a restroom sign. They all use simple, clear shapes. That is the rule: if you can look at it and understand it with no words, it works.")
        + examples([(f"{IMG}/restroom-sign.jpg","Restroom"),(f"{IMG}/stop-sign.jpg","Stop Sign"),(f"{IMG}/flammable.png","Flammable")])
        + pills(["No Words Needed","Simple Shapes","Clear Meaning"]))
    en+=card("","Pictograms Have Been Around a Long Time",
        para("People have used pictures to share ideas for thousands of years. Long ago, before modern writing, people painted simple pictures on cave walls to show animals and daily life. Ancient Egyptians used hieroglyphs, picture-symbols that stood for words and ideas.")
        + para("We still use pictograms today because they cross languages. A visitor from any country can read a restroom sign or a warning sign without speaking the local language. The 1964 Tokyo Olympics helped make modern pictograms popular: the designers made simple picture-symbols so visitors from anywhere could find their way with no words. At the 1972 Munich Olympics, a designer named Otl Aicher pushed the idea further with clean stick-figure symbols for each sport. A lot of the signs you see at airports and schools still follow that simple style today.")
        + hazard_img("Hazard pictograms","Hazard symbols are pictograms too. They warn you fast, with no words."))
    en+=card("","What Makes a Good Pictogram",
        bullets([
            ("","It uses simple, bold shapes with no tiny details."),
            ("","It reads clearly even from far away or at a small size."),
            ("","It needs no words at all to be understood."),
            ("","It shows one clear idea."),
            ("","It works in one or two colors."),
        ]))
    en+=resources_card("Key Words",
        vocab_grid("On the Quiz",
          "Heads up: these key words can show up on a quiz. Learn what each one means now, not the night before.",
          [("Pictogram","A simple picture that stands for an idea, an object, or an action. You understand it with no words. Signs, apps, and public places use them everywhere."),
           ("Symbol","A shape or mark that carries a meaning people agree on. A heart can mean love, and a red circle with a line can mean &lsquo;do not.&rsquo;"),
           ("Icon","A small, simple picture that stands for something, often on a screen, a sign, or an app. It has to be clear even when it is tiny."),
           ("Silhouette","The solid, filled-in shape of something, with no inside detail. Just the outline filled in. Many strong pictograms are simple silhouettes."),
           ("Negative Space","The empty space around and inside a shape. Good pictograms use it on purpose so the picture stays clean and easy to read."),
           ("Reimagine","To rethink an idea and make your own new version, not a copy of what you found. You keep the meaning but change the look.")]), False)

    es=banner("Arte Digital 1A &bull; Pictogramas","Pictogramas","Dibujos simples que hablan sin palabras.","#top","Back to English")
    es+=type_card("overview","El Resumen del M&oacute;dulo","&iquest;Qu&eacute; Es Un Pictograma?",
        para("Un pictograma es un dibujo simple que representa una idea, un objeto o una acci&oacute;n. Lo mejor es que lo entiendes sin leer ni una palabra. Solo lo miras y sabes qu&eacute; significa.")
        + framed(HERO,"Pictogramas"))
    es+=card("","Pictogramas Que Ya Conoces",
        para("Ya conoces muchos: un letrero de alto, un letrero de advertencia, un s&iacute;mbolo de inflamable o un letrero de ba&ntilde;o. Todos usan formas simples y claras. Esa es la regla: si lo puedes ver y entender sin palabras, funciona.")
        + examples([(f"{IMG}/restroom-sign.jpg","Ba&ntilde;o"),(f"{IMG}/stop-sign.jpg","Alto"),(f"{IMG}/flammable.png","Inflamable")])
        + pills(["Sin Palabras","Formas Simples","Significado Claro"]))
    es+=card("","Los Pictogramas Existen Desde Hace Mucho",
        para("La gente ha usado dibujos para compartir ideas por miles de a&ntilde;os. Hace mucho, antes de la escritura moderna, la gente pintaba dibujos simples en las paredes de las cuevas para mostrar animales y la vida diaria. Los antiguos egipcios usaban jerogl&iacute;ficos, s&iacute;mbolos con dibujos que representaban palabras e ideas.")
        + para("Todav&iacute;a usamos pictogramas hoy porque cruzan los idiomas. Un visitante de cualquier pa&iacute;s puede leer un letrero de ba&ntilde;o o de advertencia sin hablar el idioma local. Los Juegos Ol&iacute;mpicos de Tokio en 1964 ayudaron a hacer populares los pictogramas modernos: los dise&ntilde;adores crearon s&iacute;mbolos con dibujos simples para que los visitantes de cualquier lugar pudieran orientarse sin palabras. En los Juegos Ol&iacute;mpicos de M&uacute;nich en 1972, un dise&ntilde;ador llamado Otl Aicher llev&oacute; la idea m&aacute;s lejos con s&iacute;mbolos limpios de figuras para cada deporte. Muchos de los letreros que ves en aeropuertos y escuelas todav&iacute;a siguen ese estilo simple hoy.")
        + hazard_img("Pictogramas de peligro","Los s&iacute;mbolos de peligro tambi&eacute;n son pictogramas. Te avisan r&aacute;pido, sin palabras."))
    es+=card("","Qu&eacute; Hace Bueno a Un Pictograma",
        bullets([
            ("","Usa formas simples y fuertes, sin detalles peque&ntilde;os."),
            ("","Se lee claro aun de lejos o en tama&ntilde;o peque&ntilde;o."),
            ("","No necesita ni una palabra para entenderse."),
            ("","Muestra una sola idea clara."),
            ("","Funciona con uno o dos colores."),
        ]))
    es+=resources_card("Palabras Clave",
        vocab_grid("En el Examen",
          "Atenci&oacute;n: estas palabras clave pueden aparecer en un examen. Aprende qu&eacute; significa cada una ahora, no la noche anterior.",
          [("Pictograma","Un dibujo simple que representa una idea, un objeto o una acci&oacute;n. Lo entiendes sin palabras. Los letreros, las apps y los lugares p&uacute;blicos los usan en todas partes."),
           ("S&iacute;mbolo","Una forma o marca que lleva un significado que la gente acuerda. Un coraz&oacute;n puede decir amor, y un c&iacute;rculo rojo con una l&iacute;nea puede decir &lsquo;no.&rsquo;"),
           ("&Iacute;cono","Un dibujo peque&ntilde;o y simple que representa algo, muchas veces en una pantalla, un letrero o una app. Debe verse claro aunque sea muy peque&ntilde;o."),
           ("Silueta","La forma s&oacute;lida y rellena de algo, sin detalle por dentro. Solo el contorno relleno. Muchos pictogramas fuertes son siluetas simples."),
           ("Espacio Negativo","El espacio vac&iacute;o alrededor y dentro de una forma. Los buenos pictogramas lo usan a prop&oacute;sito para que el dibujo se vea limpio y f&aacute;cil de leer."),
           ("Reimaginar","Repensar una idea y hacer tu propia versi&oacute;n nueva, no una copia de lo que encontraste. Guardas el significado pero cambias el aspecto.")]), True)

    dots=dot("",'M',"Overview",True)+dot(S1,'1',"Step 01",False)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{S1}" class="silva-step-btn">Step 01 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><span></span><a href="{S1}" class="silva-bottom-btn">Start: Step 01 &#8594;</a></div>'
    return wrap_page("Pictograms | Digital Arts 1A | PVHS", nav("Overview",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 01 ----------------
def step01():
    en=banner("Pictograms &bull; Step 1","Find &amp; Save","Build your pictogram folder in OneDrive.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("1 screen capture (PNG):","your &lsquo;pictogram&rsquo; folder open, showing the 6 to 10 pictograms you saved, uploaded to this Canvas assignment.")])
    en+=card("","Make Your Folder and Collect 6 to 10 Pictograms",
        float_right(FIND_FLOAT,"Student searching Google Images for pictograms to save","Search, then save the ones you like into your folder.")
        + para("In this step you will make a new folder and fill it with real pictogram examples.")
        + steps([
            ("","Open your Digital Arts folder in OneDrive."),
            ("","Make a new folder inside it and name it &lsquo;pictogram&rsquo;."),
            ("","Search Google Images for pictograms (try &lsquo;stop sign pictogram&rsquo;, &lsquo;no smoking symbol&rsquo;, &lsquo;restroom sign&rsquo;)."),
            ("","Find 6 to 10 clear pictograms you like."),
            ("","Save them into your &lsquo;pictogram&rsquo; folder. You can drag and drop straight from Google Images into the folder. That is fine."),
        ]))
    en+=card("","Set Up and Capture",
        subcols([
          ("Make the Folder",["Open your Digital Arts folder in OneDrive.","Create a new folder inside it.","Name it &lsquo;pictogram&rsquo;."]),
          ("Take the Screen Capture (F15)",["Open your &lsquo;pictogram&rsquo; folder so the images show.","Press F15 on your keyboard to take the screen capture.","The screen capture must show the folder with your 6 to 10 images inside.","F15 saves the screen capture as a PNG file on your Desktop. These are temporary files: once you turn yours in, you can move them to the Trash."]),
        ]))

    es=banner("Pictogramas &bull; Paso 1","Buscar y Guardar","Crea tu carpeta de pictogramas en OneDrive.","#top","Back to English")
    es+=deliverables_box(True,
        [("1 captura de pantalla (PNG):","tu carpeta &lsquo;pictogram&rsquo; abierta, mostrando los 6 a 10 pictogramas que guardaste, subida a esta tarea de Canvas.")])
    es+=card("","Crea Tu Carpeta y Junta 6 a 10 Pictogramas",
        float_right(FIND_FLOAT,"Estudiante buscando pictogramas en Google Im&aacute;genes para guardar","Busca y guarda los que te gusten en tu carpeta.")
        + para("En este paso vas a crear una carpeta nueva y llenarla con ejemplos reales de pictogramas.")
        + steps([
            ("","Abre tu carpeta de Arte Digital en OneDrive."),
            ("","Crea una carpeta nueva adentro y ll&aacute;mala &lsquo;pictogram&rsquo;."),
            ("","Busca pictogramas en Google Im&aacute;genes (prueba &lsquo;stop sign pictogram&rsquo;, &lsquo;no smoking symbol&rsquo;, &lsquo;restroom sign&rsquo;)."),
            ("","Encuentra 6 a 10 pictogramas claros que te gusten."),
            ("","Gu&aacute;rdalos en tu carpeta &lsquo;pictogram&rsquo;. Puedes arrastrar y soltar directo desde Google Im&aacute;genes a la carpeta. Eso est&aacute; bien."),
        ]))
    es+=card("","Prepara y Captura",
        subcols([
          ("Crea la Carpeta",["Abre tu carpeta de Arte Digital en OneDrive.","Crea una carpeta nueva adentro.","N&oacute;mbrala &lsquo;pictogram&rsquo;."]),
          ("Toma la Captura (F15)",["Abre tu carpeta &lsquo;pictogram&rsquo; para ver las im&aacute;genes.","Presiona F15 en el teclado para tomar la captura de pantalla.","La captura debe mostrar la carpeta con tus 6 a 10 im&aacute;genes adentro.","F15 guarda la captura de pantalla como un archivo PNG en tu Escritorio. Son archivos temporales: una vez que entregues la tuya, puedes moverlos a la Papelera."]),
        ]))

    dots=dot(OVER,'M',"Overview",False,True)+dot("",'1',"Step 01",True)+dot(S2,'2',"Step 02",False)
    stepnav=f'<a href="{OVER}" class="silva-step-btn">&#8592; Overview</a><a href="{S2}" class="silva-step-btn">Step 02 &#8594;</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{OVER}" class="silva-bottom-btn">&#8592; Overview</a><a href="{S2}" class="silva-bottom-btn">Step 02 &#8594;</a></div>'
    return wrap_page("Step 1: Find and Save | Pictograms | Digital Arts 1A | PVHS", nav("Step 01",dots,stepnav), top_wrap(en,es), bottom)

# ---------------- STEP 02 ----------------
def step02():
    en=banner("Pictograms &bull; Step 2","Sketch &amp; Reflect","Reimagine 3 pictograms in your sketchbook.","#espanol","Clic para Espa&ntilde;ol")
    en+=deliverables_box(False,
        [("Sketch photos (JPG):","clear pictures of your 3 finished sketches and your handwritten reflection, taken with your school iPad. If they are all on one page, turn in one picture. If they are on several pages, turn in a picture of each page.")])
    en+=card("","Redraw 3 Pictograms Your Own Way",
        float_right(SKETCH_FLOAT,"Student sketching a pictogram in a sketchbook","Reimagine each one in your own sketchbook.")
        + para("Pick 3 pictograms from the ones you saved. Make each one your own. Do not copy them exactly. Rethink each idea and draw a fresh version. Pick 3 that are different from each other, like a stop sign, a no-smoking sign, and a biohazard sign.")
        + teal_callout("The Test","I should understand each drawing with no words at all. If I can look at it and know what it means, you nailed it.")
        + para("Rules for your 3 sketches:")
        + bullets([
            ("","Choose 3 different pictograms from your saved folder."),
            ("","Reimagine each one. Make it original, not a copy."),
            ("","Add color with markers or colored pencils."),
            ("","You can put all 3 sketches on one page or one sketch per page. Your choice."),
            ("","Each drawing must read clearly with no words."),
        ]))
    en+=card("","Before You Draw, Then Reflect",
        subcols([
          ("Before You Draw",["Write your name and period in the top right of your sketchbook cover.","Have your markers or colored pencils ready.","Pick 3 different pictograms from your folder."]),
          ("Write Your Reflection (By Hand)",["When your 3 sketches are done, write a short paragraph by hand in your sketchbook.","Tell me which of your 3 sketches is your favorite and why.","Explain why it reads clearly with no words.","Tell me what was hard, and what you would do differently next time."]),
        ]))

    es=banner("Pictogramas &bull; Paso 2","Dibuja y Reflexiona","Reimagina 3 pictogramas en tu cuaderno.","#top","Back to English")
    es+=deliverables_box(True,
        [("Fotos de dibujos (JPG):","fotos claras de tus 3 dibujos terminados y tu reflexi&oacute;n escrita a mano, tomadas con tu iPad de la escuela. Si est&aacute;n todos en una p&aacute;gina, entrega una foto. Si est&aacute;n en varias p&aacute;ginas, entrega una foto de cada p&aacute;gina.")])
    es+=card("","Redibuja 3 Pictogramas a Tu Manera",
        float_right(SKETCH_FLOAT,"Estudiante dibujando un pictograma en su cuaderno","Reimagina cada uno en tu propio cuaderno.")
        + para("Elige 3 pictogramas de los que guardaste. Haz cada uno tuyo. No los copies igual. Repiensa cada idea y dibuja una versi&oacute;n nueva. Elige 3 que sean diferentes entre s&iacute;, como un letrero de alto, uno de no fumar y uno de riesgo biol&oacute;gico.")
        + teal_callout("La Prueba","Yo debo entender cada dibujo sin ninguna palabra. Si lo miro y s&eacute; qu&eacute; significa, lo lograste.")
        + para("Reglas para tus 3 dibujos:")
        + bullets([
            ("","Elige 3 pictogramas diferentes de tu carpeta guardada."),
            ("","Reimagina cada uno. H&aacute;zlo original, no una copia."),
            ("","Agrega color con marcadores o l&aacute;pices de colores."),
            ("","Puedes poner los 3 dibujos en una p&aacute;gina o uno por p&aacute;gina. T&uacute; decides."),
            ("","Cada dibujo debe entenderse claro sin palabras."),
        ]))
    es+=card("","Antes de Dibujar, Luego Reflexiona",
        subcols([
          ("Antes de Dibujar",["Escribe tu nombre y periodo arriba a la derecha en la portada de tu cuaderno de dibujo.","Ten listos tus marcadores o l&aacute;pices de colores.","Elige 3 pictogramas diferentes de tu carpeta."]),
          ("Escribe Tu Reflexi&oacute;n (a Mano)",["Cuando termines tus 3 dibujos, escribe un p&aacute;rrafo corto a mano en tu cuaderno.","Dime cu&aacute;l de tus 3 dibujos es tu favorito y por qu&eacute;.","Explica por qu&eacute; se entiende claro sin palabras.","Dime qu&eacute; fue lo dif&iacute;cil y qu&eacute; har&iacute;as diferente la pr&oacute;xima vez."]),
        ]))

    dots=dot(OVER,'M',"Overview",False,True)+dot(S1,'1',"Step 01",False)+dot("",'2',"Step 02",True)
    stepnav=f'<a href="{S1}" class="silva-step-btn">&#8592; Step 01</a>'
    bottom=f'<div class="silva-bottom-nav"><a href="{S1}" class="silva-bottom-btn">&#8592; Step 01</a><span></span></div>'
    return wrap_page("Step 2: Sketch and Reflect | Pictograms | Digital Arts 1A | PVHS", nav("Step 02",dots,stepnav), top_wrap(en,es), bottom)

for fname,gen in [(OVER,overview),(S1,step01),(S2,step02)]:
    html=ent(gen())
    ban_check(html, fname)
    open(os.path.join(ROOT,"curriculum/shared",fname),"w",encoding="utf-8").write(html)
    print("wrote", fname, len(html), "bytes")
