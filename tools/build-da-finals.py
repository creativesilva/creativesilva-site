#!/usr/bin/env python3
"""Generate da-finals-quiz-prep.html with new chip numbering,
gradient borders (top stripe solid, R/B/L gradient), bilingual mirror,
and merged STUDY GUIDE / 04 section."""

import os

# Repo root = parent of this tools/ directory, so the script is portable.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTFILE = f'{ROOT}/curriculum/shared/da-finals-quiz-prep.html'

# Palette
TEAL = '#00b8b8'
TEAL_DIM = 'rgba(0,184,184,0.08)'
TEAL_BG_STRONG = 'rgba(0,116,116,0.10)'
TEAL_BG_WEAK = 'rgba(0,116,116,0.03)'
TEAL_CHIP_TINT = 'rgba(0,184,184,0.18)'
TEAL_TERM_BG = 'linear-gradient(135deg,rgba(0,184,184,0.14) 0%,rgba(0,184,184,0.14) 10%,rgba(0,0,0,0.32) 10%,rgba(0,0,0,0.32) 100%)'
TEAL_EYEBROW = '#80e0e0'

ORANGE = '#FF6B1A'
ORANGE_DIM = 'rgba(255,107,26,0.08)'
ORANGE_BG_STRONG = 'rgba(255,107,26,0.16)'
ORANGE_BG_WEAK = 'rgba(255,107,26,0.04)'
ORANGE_STAT_BG = 'linear-gradient(135deg,rgba(255,107,26,0.20) 0%,rgba(255,107,26,0.20) 8%,rgba(0,0,0,0.40) 8%,rgba(0,0,0,0.40) 100%)'
ORANGE_EYEBROW = '#ffb27c'

CYAN = '#00c2ff'
CYAN_DIM = 'rgba(0,194,255,0.08)'
CYAN_BG_STRONG = 'rgba(0,194,255,0.16)'
CYAN_BG_WEAK = 'rgba(0,194,255,0.04)'
CYAN_EYEBROW = '#7dd3fc'


def outer_card(color, dim, bg_inner, inner_html, pad_t=30, pad_r=30, pad_b=30, pad_l=30, last=False):
    """Outer section card.
    The card keeps its TRANSLUCENT tinted background (so the watermark
    shows through). A 2px diagonal gradient frame is painted on all four
    sides with border-image directly on the card (no background wrapper,
    so nothing bleeds through). The thick SOLID top stripe is a thin
    child div pulled flush to the top inner edge with negative margins;
    it sits just inside the 2px gradient top border and reads as the
    bright solid top accent."""
    mb = '' if last else 'margin-bottom:24px;'
    stripe_gap = max(pad_t - 6, 12)
    stripe = (
        f'<div style="height:4px;background:{color};'
        f'margin:-{pad_t}px -{pad_r}px {stripe_gap}px -{pad_l}px;"></div>'
    )
    return (
        f'<div style="background:{bg_inner};border:2px solid transparent;'
        f'border-image:linear-gradient(135deg,{color} 0%,{dim} 100%) 1;'
        f'padding:{pad_t}px {pad_r}px {pad_b}px {pad_l}px;{mb}position:relative;overflow:hidden;">'
        f'{stripe}{inner_html}'
        f'</div>'
    )


def inner_tile(color, dim, bg_inner, inner_html, pad_t=20, pad_r=22, pad_b=24, pad_l=22):
    """Inner tile. 1px gradient frame via border-image (translucent,
    no bleed) + solid 3px top stripe child pulled flush to the top."""
    stripe_gap = max(pad_t - 8, 10)
    stripe = (
        f'<div style="height:3px;background:{color};'
        f'margin:-{pad_t}px -{pad_r}px {stripe_gap}px -{pad_l}px;"></div>'
    )
    return (
        f'<div style="background:{bg_inner};border:1px solid transparent;'
        f'border-image:linear-gradient(135deg,{color} 0%,{dim} 100%) 1;'
        f'padding:{pad_t}px {pad_r}px {pad_b}px {pad_l}px;position:relative;overflow:hidden;">'
        f'{stripe}{inner_html}'
        f'</div>'
    )


def image_border(color, dim):
    """2px gradient frame all 4 sides (border-image is fine here: no
    solid-top requirement on an image)."""
    return (
        f'border:2px solid transparent;'
        f'border-image:linear-gradient(135deg,{color} 0%,{dim} 100%) 1'
    )


def chip(label, color_solid, color_eyebrow):
    """Eyebrow chip with left stripe."""
    return (
        f'<div style="display:inline-block;background:rgba(0,0,0,0.40);'
        f'border-left:3px solid {color_solid};padding:5px 12px 5px 10px;'
        f'font-family:Arial,sans-serif;font-size:10pt;letter-spacing:0.22em;'
        f'color:{color_eyebrow};text-transform:uppercase;margin-bottom:12px;">'
        f'<strong>{label}</strong></div>'
    )


def hairline(color, width=60):
    return f'<div style="height:2px;background:{color};width:{width}px;margin-bottom:22px;"></div>'


def button(label, href, accent, download=False):
    """Uniform button. FRAMEWORK RULE: gray base, dark-teal text, fixed
    size, and a 2px top accent bar in the color of the section it lives
    in. Use the SAME size and gray for every button on every page;
    only the top accent color changes to match the surrounding section."""
    dl = ' download=""' if download else ''
    return (
        f'<a href="{href}"{dl} style="background:rgba(255,255,255,0.92);'
        f'color:#003838;text-decoration:none;padding:7px 16px;'
        f'display:inline-block;font-size:11pt;white-space:nowrap;'
        f'border-top:2px solid {accent};"><strong>{label}</strong></a>'
    )


def triangle(color, size=20):
    return (
        f'<div style="float:left;width:0;height:0;'
        f'border-top:{size}px solid {color};'
        f'border-right:{size}px solid transparent;'
        f'margin:-30px 0 0 -30px;"></div>\n'
        f'        <div style="clear:both;"></div>'
    )


# Category data: (en_title, es_title, [(en_name, en_def, es_name, es_def), ...])
CATEGORIES = [
    (
        'The 7 Elements of Art', 'Los 7 Elementos del Arte',
        [
            ('Line', 'A path made by a moving point. Lines can be straight, curvy, thick, thin, soft, or sharp.',
             'Línea', 'Un camino hecho por un punto en movimiento. Pueden ser rectas, curvas, gruesas, delgadas, suaves o duras.'),
            ('Shape', 'A flat area with an edge around it. Two dimensions: width and height. Circle, square, star.',
             'Forma', 'Un área plana con un borde alrededor. Dos dimensiones: ancho y alto. Círculo, cuadrado, estrella.'),
            ('Form', 'A shape that looks 3D. Has width, height, and depth. A sphere is a form. A cube is a form.',
             'Volumen', 'Una forma que se ve en 3D. Tiene ancho, alto y profundidad. Una esfera es un volumen. Un cubo es un volumen.'),
            ('Color', 'What you see when light bounces off something. Color has a name (red, blue), brightness, and strength.',
             'Color', 'Lo que ves cuando la luz rebota en algo. El color tiene nombre (rojo, azul), brillo y fuerza.'),
            ('Value', 'How light or dark something is. White is lightest. Black is darkest. Everything else is a gray value.',
             'Valor', 'Qué tan claro u oscuro es algo. El blanco es lo más claro. El negro es lo más oscuro. Todo lo demás es un valor de gris.'),
            ('Texture', 'How something feels, or how it looks like it would feel. Smooth, rough, bumpy, fuzzy, sharp.',
             'Textura', 'Cómo se siente algo, o cómo parece que se sentiría. Liso, áspero, irregular, peludo, filoso.'),
            ('Space', 'The room around and between things in an artwork. Positive space is stuff. Negative space is empty.',
             'Espacio', 'El área alrededor y entre las cosas en una obra. El espacio positivo es lo que está. El negativo está vacío.'),
        ]
    ),
    (
        'Principles of Design', 'Principios de Diseño',
        [
            ('Balance', 'When the visual weight of an artwork feels even. Can be symmetrical (both sides match) or asymmetrical (sides differ but still feel balanced).',
             'Equilibrio', 'Cuando el peso visual de una obra se siente parejo. Puede ser simétrico (los dos lados son iguales) o asimétrico (los lados son distintos pero se sienten balanceados).'),
            ('Contrast', 'The difference between two things. Light vs dark, big vs small, smooth vs rough. Contrast makes things pop.',
             'Contraste', 'La diferencia entre dos cosas. Claro vs oscuro, grande vs chico, liso vs áspero. El contraste hace que las cosas resalten.'),
            ('Visual Hierarchy', 'The order in which the eye moves around a design. The biggest, boldest stuff is seen first. Less important info is smaller.',
             'Jerarquía Visual', 'El orden en que el ojo se mueve por un diseño. Lo más grande y llamativo se ve primero. Lo menos importante es más pequeño.'),
            ('Emphasis', 'Making one part of a design stand out the most. The focal point. The part your eye lands on first.',
             'Énfasis', 'Hacer que una parte del diseño resalte más que el resto. El punto focal. La parte donde tu ojo cae primero.'),
            ('Alignment', 'Lining up the parts of a design so they look connected and clean. Left-align, center-align, right-align.',
             'Alineación', 'Acomodar las partes de un diseño para que se vean conectadas y limpias. A la izquierda, al centro, a la derecha.'),
            ('Repetition', 'Using the same shape, color, or pattern over and over to tie a design together. Repetition builds rhythm.',
             'Repetición', 'Usar la misma forma, color o patrón una y otra vez para unir el diseño. La repetición construye ritmo.'),
        ]
    ),
    (
        'Typography', 'Tipografía',
        [
            ('Typography', 'The art of using type (letters and words) in a design. Picking fonts, sizing them, and arranging them on the page.',
             'Tipografía', 'El arte de usar letras y palabras en un diseño. Escoger fuentes, ajustar el tamaño y acomodarlas en la página.'),
            ('Typeface', 'The full design of a set of letters. The shapes, the curves, the style. Arial is a typeface. Helvetica is a typeface.',
             'Tipo de Letra', 'El diseño completo de un grupo de letras. Las formas, las curvas, el estilo. Arial es un tipo de letra. Helvetica es un tipo de letra.'),
            ('Font', 'A specific size and style of a typeface. Arial 12pt Bold is a font. Arial 18pt Italic is a different font.',
             'Fuente', 'Un tamaño y estilo específico de un tipo de letra. Arial 12pt Bold es una fuente. Arial 18pt Italic es otra fuente.'),
            ('Kerning', 'The space between two specific letters. Designers adjust kerning so letters look evenly spaced.',
             'Kerning', 'El espacio entre dos letras específicas. Los diseñadores ajustan el kerning para que las letras se vean parejas.'),
            ('Leading', 'The space between lines of text, top to bottom. Pronounced “LED-ding” like the metal.',
             'Interlineado', 'El espacio entre líneas de texto, de arriba a abajo. En inglés se dice “LED-ding” como el metal.'),
            ('Tracking', 'The space between letters across a whole word or sentence. Different from kerning, which is between just two letters.',
             'Tracking', 'El espacio entre todas las letras de una palabra o frase. Distinto del kerning, que es solo entre dos letras.'),
            ('Wordmark', 'A logo made of words only, no symbol. Examples: Google, Coca-Cola, Disney.',
             'Logotipo', 'Un logo hecho solo de palabras, sin símbolo. Ejemplos: Google, Coca-Cola, Disney.'),
            ('Lockup', 'The logo art and the wordmark joined as one fixed unit. Always at the same spacing. Never moved around.',
             'Lockup', 'El símbolo y el logotipo unidos como una sola pieza fija. Siempre con el mismo espacio. Nunca se mueven por separado.'),
        ]
    ),
    (
        'Color & Reproduction', 'Color y Reproducción',
        [
            ('Hex Code', 'A 6-character code that locks in an exact color, like <strong>#FF6B1A</strong> for orange. Same color on every screen and every print.',
             'Código Hex', 'Un código de 6 caracteres que define un color exacto, como <strong>#FF6B1A</strong> para naranja. El mismo color en toda pantalla e impresión.'),
            ('CMYK', 'The four ink colors used in printing: <strong>C</strong>yan, <strong>M</strong>agenta, <strong>Y</strong>ellow, blac<strong>K</strong>. Used on printed boxes, posters, magazines.',
             'CMYK', 'Los cuatro colores de tinta para imprimir: <strong>C</strong>ian, <strong>M</strong>agenta, <strong>A</strong>marillo y ne<strong>G</strong>ro. Se usan en cajas, pósters y revistas.'),
            ('RGB', 'The three light colors used on screens: <strong>R</strong>ed, <strong>G</strong>reen, <strong>B</strong>lue. Used on phones, computers, TVs.',
             'RGB', 'Los tres colores de luz para pantallas: <strong>R</strong>ojo, <strong>V</strong>erde (Green), <strong>A</strong>zul (Blue). Para celulares, computadoras y televisiones.'),
            ('Color Palette', 'The full set of colors a brand uses. Usually 2 to 5 main colors that always go together. The palette controls the brand feel.',
             'Paleta de Colores', 'El grupo completo de colores que usa una marca. Casi siempre de 2 a 5 colores principales que van juntos. La paleta controla el estilo de la marca.'),
            ('Warm Colors', 'Colors that feel hot or sunny. Red, orange, yellow. Often used to feel energetic or fun.',
             'Colores Cálidos', 'Colores que se sienten calientes o soleados. Rojo, naranja, amarillo. Se usan para sentir energía o diversión.'),
            ('Cool Colors', 'Colors that feel calm or chilly. Blue, green, purple. Often used to feel healthy, clean, or trustworthy.',
             'Colores Fríos', 'Colores que se sienten calmados o frescos. Azul, verde, morado. Se usan para sentir limpieza, salud o confianza.'),
        ]
    ),
    (
        'Branding & Identity', 'Marca e Identidad',
        [
            ('Logo', 'The symbol or wordmark that stands for a brand. The visual signature. The Apple apple. The Nike swoosh.',
             'Logo', 'El símbolo o logotipo que representa a una marca. La firma visual. La manzana de Apple. El swoosh de Nike.'),
            ('Brand', 'The whole personality of a company: how it looks, sounds, and feels to customers. More than just the logo.',
             'Marca', 'La personalidad completa de una empresa: cómo se ve, suena y se siente para los clientes. Más que solo el logo.'),
            ('Brand Identity', 'All the visual pieces of a brand together: logo, colors, fonts, photos, voice. Everything the customer sees and hears.',
             'Identidad de Marca', 'Todas las piezas visuales de la marca juntas: logo, colores, fuentes, fotos, voz. Todo lo que el cliente ve y oye.'),
            ('Brand DNA', 'What makes a brand feel like itself. The shapes, colors, and style that stay the same even when the look gets updated.',
             'ADN de la Marca', 'Lo que hace que una marca se sienta como ella misma. Las formas, colores y estilo que se quedan iguales aunque el look se actualice.'),
            ('Mascot', 'A character that shows the brand. Tony the Tiger and Cap’n Crunch are mascots. They make a brand easy to remember.',
             'Mascota', 'Un personaje que representa a la marca. Tony el Tigre y Cap’n Crunch son mascotas. Hacen que una marca sea fácil de recordar.'),
            ('Tagline', 'A short phrase that sells the product. Like “They’re great!” or “Just do it.” Short, fun, easy to say.',
             'Eslogan', 'Una frase corta que vende el producto. Como “They’re great!” o “Just do it.” Corta, divertida, fácil de decir.'),
            ('Target Audience', 'The group of people the product is made for. Kids, teens, athletes, busy adults. Every design choice should match the target.',
             'Audiencia Objetivo', 'El grupo de personas para quien se hace el producto. Niños, jóvenes, atletas, adultos ocupados. Cada decisión de diseño debe ir con la audiencia.'),
            ('Brand Refresh', 'When a designer gives a brand a new look while keeping the heart of the brand. Like updating an old logo without losing what made it famous.',
             'Renovación de Marca', 'Cuando un diseñador le da a una marca un nuevo look sin perder su esencia. Como actualizar un logo viejo sin perder lo que lo hizo famoso.'),
            ('Creative Brief', 'A written plan that tells a designer what the client needs. Includes goals, audience, deadline, and budget.',
             'Brief Creativo', 'Un plan escrito que le dice al diseñador qué necesita el cliente. Incluye metas, audiencia, fecha y presupuesto.'),
        ]
    ),
    (
        'Packaging & Production', 'Empaque y Producción',
        [
            ('Mockup', 'A real-looking picture of your design on a product. A box mockup. A t-shirt mockup. Shows how your design would look in real life.',
             'Mockup', 'Una imagen realista de tu diseño en un producto. Un mockup de caja. Un mockup de playera. Muestra cómo se vería tu diseño en la vida real.'),
            ('Dieline', 'The flat shape of a box before it gets folded. Shows where to cut, where to fold, and where the panels go.',
             'Dieline', 'La forma plana de una caja antes de doblarse. Muestra dónde cortar, dónde doblar y dónde van los paneles.'),
            ('Front Panel', 'The face of a package. The part the shopper sees first. Holds the name, the mascot, and the tagline.',
             'Panel Frontal', 'La cara de un empaque. La parte que el comprador ve primero. Lleva el nombre, la mascota y el eslogan.'),
            ('Print Template', 'A flat file with all the box panels arranged so they can be printed, cut out, and folded into a real box.',
             'Plantilla de Impresión', 'Un archivo plano con todos los paneles de la caja acomodados para imprimir, cortar y doblar en una caja real.'),
            ('Proof', 'A test version of a design before it gets printed or shared. Designers send proofs to clients to check colors, type, and spacing.',
             'Prueba (Proof)', 'Una versión de prueba de un diseño antes de imprimir o compartir. Los diseñadores mandan pruebas al cliente para revisar colores, letra y espacios.'),
            ('Thumbnail', 'A tiny rough sketch of a design idea, drawn fast. Used to test lots of ideas before picking the best one.',
             'Thumbnail', 'Un bocetito rápido de una idea de diseño. Se usa para probar varias ideas antes de escoger la mejor.'),
        ]
    ),
    (
        'Software & Graphics Types', 'Software y Tipos de Gráficos',
        [
            ('Adobe Illustrator', 'The main software designers use to build <strong>vector</strong> logos, packaging, and illustrations. Industry standard.',
             'Adobe Illustrator', 'El programa principal que usan los diseñadores para crear logos, empaques e ilustraciones <strong>vectoriales</strong>. Estándar de la industria.'),
            ('Adobe Photoshop', 'The main software designers use to edit photos and create <strong>raster</strong> artwork.',
             'Adobe Photoshop', 'El programa principal que usan los diseñadores para editar fotos y crear arte <strong>raster</strong>.'),
            ('Vector Graphics', 'Art made of math (points and lines). Scales to any size without losing quality. Logos are almost always vector.',
             'Gráficos Vectoriales', 'Arte hecho de matemáticas (puntos y líneas). Se puede agrandar a cualquier tamaño sin perder calidad. Los logos casi siempre son vectoriales.'),
            ('Raster Graphics', 'Art made of tiny squares called pixels. Photos are raster. They lose quality when stretched too big.',
             'Gráficos Raster', 'Arte hecho de cuadritos llamados píxeles. Las fotos son raster. Pierden calidad si se estiran demasiado.'),
            ('Adobe Firefly', 'Adobe’s AI tool for generating images from text prompts. Used inside Photoshop and Illustrator.',
             'Adobe Firefly', 'La herramienta de IA de Adobe que genera imágenes a partir de texto. Se usa dentro de Photoshop e Illustrator.'),
        ]
    ),
    (
        'Workflow & Process', 'Flujo de Trabajo y Proceso',
        [
            ('Concept Sketch', 'A by-hand drawing of a design idea before going to the computer. Helps plan the layout.',
             'Boceto Conceptual', 'Un dibujo a mano de una idea de diseño antes de pasarla a la computadora. Ayuda a planear el layout.'),
            ('Mood Board', 'A collection of images, colors, and fonts gathered to set the visual mood for a project. Used before designing.',
             'Mood Board', 'Una colección de imágenes, colores y fuentes que arman el ambiente visual de un proyecto. Se usa antes de diseñar.'),
            ('Reflection', 'Looking back at finished work to write about what was learned, what went well, and what to change next time.',
             'Reflexión', 'Mirar el trabajo terminado y escribir qué aprendiste, qué salió bien y qué cambiar la próxima vez.'),
        ]
    ),
]


def gen_term_tile(num, total, name_en_or_es, definition):
    """Inner term tile: solid 3px teal top + 1px gradient frame via wrapper."""
    inner = (
        f'<div style="font-family:Arial,sans-serif;font-size:9pt;letter-spacing:0.22em;color:{TEAL_EYEBROW};text-transform:uppercase;margin-bottom:10px;"><strong>TERM {num:02d} / {total:02d}</strong></div>'
        f'<div style="font-size:17pt;color:#ffffff;line-height:1.15;margin-bottom:8px;"><strong>{name_en_or_es}</strong></div>'
        f'<div style="height:2px;background:{TEAL};width:32px;margin-bottom:10px;"></div>'
        f'<div style="font-size:13pt;line-height:1.55;color:rgba(255,255,255,0.84);">{definition}</div>'
    )
    return '          ' + inner_tile(TEAL, TEAL_DIM, TEAL_TERM_BG, inner)


def gen_category(cat_num, total_cats, title, term_tiles_html, scroll_hint_text):
    """Outer category card containing the term grid. No triangle."""
    inner = (
        f'{chip(f"CATEGORY {cat_num:02d} / {total_cats:02d}", TEAL, TEAL_EYEBROW)}'
        f'<div style="font-size:22pt;color:#ffffff;line-height:1.15;margin-bottom:10px;"><strong>{title}</strong></div>'
        f'{hairline(TEAL)}'
        f'<div style="display:grid;grid-auto-flow:column;grid-auto-columns:minmax(260px,1fr);overflow-x:auto;gap:14px;padding-bottom:8px;-webkit-overflow-scrolling:touch;">\n'
        f'{term_tiles_html}\n'
        f'        </div>'
        f'<div class="scroll-hint" style="text-align:center;font-size:8pt;color:rgba(0,184,184,0.55);letter-spacing:0.22em;text-transform:uppercase;margin-top:14px;font-family:Arial,sans-serif;"><strong>{scroll_hint_text}</strong></div>'
    )
    return f'      <!-- CATEGORY {cat_num:02d} -->\n      ' + outer_card(TEAL, TEAL_DIM, f'linear-gradient(180deg,{TEAL_BG_STRONG} 0%,{TEAL_BG_WEAK} 100%)', inner)


def build_block(lang):
    """Build the full content block for one language (en or es)."""
    is_en = lang == 'en'

    # ---- Banner ----
    banner_eyebrow = 'DIGITAL ARTS / FINAL EXAM / STUDY GUIDE' if is_en else 'ARTES DIGITALES / EXAMEN FINAL / GUÍA DE ESTUDIO'
    banner_title = '50 Industry Terms You Must Know' if is_en else '50 Términos de la Industria que Debes Saber'
    banner_tagline = 'Real terms. Real designers use them every day. So will you.' if is_en else 'Términos reales. Los diseñadores los usan todos los días. Tú también lo harás.'
    banner_btn = 'Word Doc' if is_en else 'Documento Word'
    banner_toggle = 'Clic para Español' if is_en else 'Back to English'
    banner_toggle_href = '#espanol' if is_en else '#top'

    banner = f'''
      <!-- Banner Header -->
      <div style="background:linear-gradient(135deg,#000000 0%,#003838 40%,#007474 100%);padding:24px 28px 26px;margin:-28px -28px 24px -28px;border-bottom:3px solid {TEAL};">
        <div style="display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;gap:16px;">
          <div style="justify-self:start;">
            <img src="https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/PV%20LOGO%20NEW.png" alt="Pioneer Valley High School Logo" style="width:min(90px,15vw);height:auto;display:block;" />
          </div>
          <div style="justify-self:center;text-align:center;">
            <div style="margin-bottom:8px;font-family:Arial,sans-serif;font-size:10pt;letter-spacing:0.30em;color:{TEAL_EYEBROW};text-transform:uppercase;"><strong>{banner_eyebrow}</strong></div>
            <div style="color:#ffffff;font-size:30pt;font-weight:700;line-height:1.05;letter-spacing:-0.01em;"><strong>{banner_title}</strong></div>
            <div style="height:2px;background:{TEAL};width:80px;margin:14px auto 10px;"></div>
            <div style="color:rgba(255,255,255,0.78);"><span style="font-size:12pt;font-style:italic;">{banner_tagline}</span></div>
          </div>
          <div style="justify-self:end;">
            {button(banner_toggle, banner_toggle_href, TEAL)}
          </div>
        </div>
      </div>'''

    # ---- WELCOME / 01 ----
    welcome_chip = 'WELCOME / 01' if is_en else 'BIENVENIDA / 01'
    welcome_title = 'Lecture & Note Taking' if is_en else 'Clase y Toma de Notas'
    welcome_body1 = ('Every term below could show up on the test. Every term comes straight from the work you have done this year: the Cereal Box Group Project, Company Branding, Jimenez Mobile Detailing, and the in-class lectures.' if is_en
                     else 'Cualquier término de abajo puede salir en el examen. Cada uno viene del trabajo que hiciste este año: el Proyecto Grupal de la Caja de Cereal, Branding de Compañía, Jimenez Mobile Detailing y las clases en el salón.')
    welcome_body2 = ('Read it. Sketch the tough ones into your sketchbook. Bring the sketchbook to the test.' if is_en
                     else 'Léelo. Dibuja los difíciles en tu cuaderno de dibujo. Trae el cuaderno al examen.')

    welcome_inner = (
        f'<div style="padding:14px 14px 0;">'
        f'<img src="https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/images/da-finals/art-elements-hero.png" alt="Mr. Silva teaching the 7 Elements of Art in the PV Digital Arts Lab" style="width:100%;height:auto;display:block;{image_border(TEAL, TEAL_DIM)};box-sizing:border-box;" />'
        f'</div>'
        f'<div style="padding:26px 30px 30px;">'
        f'{chip(welcome_chip, TEAL, TEAL_EYEBROW)}'
        f'<div style="font-size:24pt;color:#ffffff;line-height:1.1;margin-bottom:10px;"><strong>{welcome_title}</strong></div>'
        f'{hairline(TEAL)}'
        f'<div style="margin-bottom:14px;line-height:1.7;font-size:14pt;color:rgba(255,255,255,0.88);">{welcome_body1}</div>'
        f'<div style="line-height:1.7;font-size:14pt;color:rgba(255,255,255,0.88);">{welcome_body2}</div>'
        f'</div>'
    )
    welcome = '\n      <!-- WELCOME / 01 -->\n      ' + outer_card(
        TEAL, TEAL_DIM, f'linear-gradient(180deg,{TEAL_BG_STRONG} 0%,{TEAL_BG_WEAK} 100%)',
        welcome_inner, pad_t=0, pad_r=0, pad_b=0, pad_l=0)

    # ---- TEST FORMAT / 02 ----
    fmt_chip = 'TEST FORMAT / 02' if is_en else 'FORMATO DEL EXAMEN / 02'
    fmt_title = 'What the Test Looks Like' if is_en else 'Cómo Se Ve el Examen'
    stat_tiles_data = [
        (('TOTAL TERMS', '50', 'Every term below could be on the test. Learn all of them.'),
         ('TOTAL TÉRMINOS', '50', 'Cualquier término de abajo puede salir en el examen. Apréndetelos todos.')),
        (('QUESTIONS', '25', 'The test pulls 25 random questions from these 50 terms.'),
         ('PREGUNTAS', '25', 'El examen escoge 25 preguntas al azar de estos 50 términos.')),
        (('CHOICES EACH', '4', 'Multiple choice. One correct answer per question.'),
         ('OPCIONES CADA UNA', '4', 'Opción múltiple. Una sola respuesta correcta por pregunta.')),
        (('OPEN BOOK', '01', 'Only resource allowed: your own sketchbook notes.'),
         ('LIBRO ABIERTO', '01', 'Único recurso permitido: tus propios apuntes en tu cuaderno.')),
    ]
    stat_tiles_html = ''
    for tile_en, tile_es in stat_tiles_data:
        label, big_num, desc = tile_en if is_en else tile_es
        tile_inner = (
            f'<div style="font-family:Arial,sans-serif;font-size:9pt;letter-spacing:0.20em;color:{ORANGE_EYEBROW};text-transform:uppercase;margin-bottom:8px;"><strong>{label}</strong></div>'
            f'<div style="font-size:40pt;color:#ffffff;line-height:1.0;font-weight:700;letter-spacing:-0.02em;margin-bottom:6px;"><strong>{big_num}</strong></div>'
            f'<div style="height:2px;background:{ORANGE};margin-bottom:10px;width:40px;"></div>'
            f'<div style="font-size:12pt;color:rgba(255,255,255,0.84);line-height:1.55;">{desc}</div>'
        )
        stat_tiles_html += '        ' + inner_tile(ORANGE, ORANGE_DIM, ORANGE_STAT_BG, tile_inner, pad_t=24, pad_r=22, pad_b=24, pad_l=22) + '\n'

    fmt_inner = (
        f'{chip(fmt_chip, ORANGE, ORANGE_EYEBROW)}'
        f'<div style="font-size:22pt;color:#ffffff;line-height:1.15;margin-bottom:10px;"><strong>{fmt_title}</strong></div>'
        f'{hairline(ORANGE)}'
        f'<div style="display:grid;grid-auto-flow:column;grid-auto-columns:minmax(200px,1fr);overflow-x:auto;gap:14px;padding-bottom:8px;-webkit-overflow-scrolling:touch;">\n'
        f'{stat_tiles_html}        </div>'
    )
    fmt = '\n      <!-- TEST FORMAT / 02 -->\n      ' + outer_card(
        ORANGE, ORANGE_DIM, f'linear-gradient(180deg,{ORANGE_BG_STRONG} 0%,{ORANGE_BG_WEAK} 100%)', fmt_inner)

    # ---- STUDY / 03 ----
    study_chip = 'STUDY / 03' if is_en else 'ESTUDIO / 03'
    study_title = 'Build Your Own Study Guide' if is_en else 'Construye Tu Propia Guía de Estudio'
    study_body1 = ('During today’s lecture session, copy the terms you do not know into your sketchbook. Write the definition in your own words. Sketch a tiny example next to each one.' if is_en
                   else 'Durante la clase de hoy, copia los términos que no sepas en tu cuaderno. Escribe la definición con tus propias palabras. Haz un dibujito al lado de cada uno.')
    study_body2 = ('Your sketchbook will be the only resource you can use on the test. The better your notes, the better your grade.' if is_en
                   else 'Tu cuaderno será el único recurso que puedes usar en el examen. Mientras mejores tus notas, mejor tu calificación.')

    study_inner = (
        f'{chip(study_chip, CYAN, CYAN_EYEBROW)}'
        f'<div style="font-size:22pt;color:#ffffff;line-height:1.15;margin-bottom:10px;"><strong>{study_title}</strong></div>'
        f'{hairline(CYAN)}'
        f'<div style="font-size:14pt;line-height:1.7;color:rgba(255,255,255,0.88);margin-bottom:12px;">{study_body1}</div>'
        f'<div style="font-size:14pt;line-height:1.7;color:rgba(255,255,255,0.88);">{study_body2}</div>'
    )
    study = '\n      <!-- STUDY / 03 -->\n      ' + outer_card(
        CYAN, CYAN_DIM, f'linear-gradient(180deg,{CYAN_BG_STRONG} 0%,{CYAN_BG_WEAK} 100%)', study_inner)

    # ---- CATEGORIES 01-08 ----
    categories_html = ''
    term_counter = 1
    total_terms = sum(len(c[2]) for c in CATEGORIES)
    scroll_hint_text = '« drag or swipe for more »' if is_en else '« arrastra o desliza para ver más »'
    for cat_idx, (en_title, es_title, terms) in enumerate(CATEGORIES, start=1):
        title = en_title if is_en else es_title
        tile_chunks = []
        for term in terms:
            en_name, en_def, es_name, es_def = term
            name = en_name if is_en else es_name
            definition = en_def if is_en else es_def
            tile_chunks.append(gen_term_tile(term_counter, total_terms, name, definition))
            term_counter += 1
        tiles_html = '\n'.join(tile_chunks)
        categories_html += gen_category(cat_idx, len(CATEGORIES), title, tiles_html, scroll_hint_text) + '\n'

    # ---- STUDY GUIDE / 04 (merged Take It With You + Study Plan + Download) ----
    sg_chip = 'STUDY GUIDE / 04' if is_en else 'GUÍA DE ESTUDIO / 04'
    sg_title = 'Bring Your Sketchbook to the Test' if is_en else 'Trae Tu Cuaderno al Examen'
    sg_steps = ('''<strong style="color:{eyebrow};">01 /</strong> Read each term out loud. Hear the word.<br />
          <strong style="color:{eyebrow};">02 /</strong> Write the ones you do not know into your sketchbook.<br />
          <strong style="color:{eyebrow};">03 /</strong> Sketch a tiny example next to each tough term.<br />
          <strong style="color:{eyebrow};">04 /</strong> Quiz yourself the night before. Then again in the morning.''' if is_en
        else '''<strong style="color:{eyebrow};">01 /</strong> Lee cada término en voz alta. Escucha la palabra.<br />
          <strong style="color:{eyebrow};">02 /</strong> Escribe los que no sepas en tu cuaderno.<br />
          <strong style="color:{eyebrow};">03 /</strong> Dibuja un ejemplo pequeño al lado de cada término difícil.<br />
          <strong style="color:{eyebrow};">04 /</strong> Hazte un examen la noche anterior. Y otra vez en la mañana.''').format(eyebrow=ORANGE_EYEBROW)
    sg_line_test_day = ('On test day, your sketchbook is your only resource. Make the notes count.' if is_en
                        else 'El día del examen, tu cuaderno es tu único recurso. Que las notas valgan.')
    sg_line_print = ('Want a printable copy? Grab the full 50-term study guide as a Word document. Open it on your phone, print it, or save it to OneDrive for offline review.' if is_en
                     else '¿Quieres una copia para imprimir? Descarga la guía completa de 50 términos como documento Word. Ábrela en tu celular, imprímela o guárdala en OneDrive para repasar sin internet.')
    sg_btn = 'Download Word Doc' if is_en else 'Descargar Documento Word'

    sg_inner = (
        f'{chip(sg_chip, ORANGE, ORANGE_EYEBROW)}'
        f'<div style="font-size:24pt;color:#ffffff;line-height:1.15;margin-bottom:10px;"><strong>{sg_title}</strong></div>'
        f'{hairline(ORANGE)}'
        f'<div style="font-size:14pt;line-height:1.8;color:rgba(255,255,255,0.88);margin-bottom:14px;">{sg_steps}</div>'
        f'<div style="font-size:14pt;line-height:1.7;color:rgba(255,255,255,0.88);margin-bottom:18px;">{sg_line_test_day}</div>'
        f'<div style="font-size:14pt;line-height:1.7;color:rgba(255,255,255,0.88);margin-bottom:22px;">{sg_line_print}</div>'
        f'<div>{button(sg_btn, "https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/study-guides/DA_Finals_Study_Guide.docx", ORANGE, download=True)}</div>'
    )
    study_guide = '\n      <!-- STUDY GUIDE / 04 -->\n      ' + outer_card(
        ORANGE, ORANGE_DIM, 'linear-gradient(180deg,rgba(255,107,26,0.18) 0%,rgba(255,107,26,0.05) 100%)',
        sg_inner, last=True)

    return banner + welcome + fmt + study + categories_html + study_guide


# Build EN and ES blocks
en_block = build_block('en')
es_block = build_block('es')

# Outer wrapper
PAGE = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Digital Arts Final Exam: Study Guide</title>
  <link rel="icon" type="image/svg+xml" href="/logos/CS_Logo_Only.svg" />
  <link rel="apple-touch-icon" href="/logos/CS_Logo_Only.svg" />
  <style>:root {{ --course-accent: #007474; }}</style>
  <link rel="stylesheet" href="/css/silva-module.css" />
</head>
<body>

  <nav class="silva-nav" aria-label="Final Exam navigation">
    <div class="silva-nav-inner">
      <div class="silva-breadcrumb">
        <a href="/curriculum.html">Curriculum</a>
        <span class="bc-sep">&rsaquo;</span>
        <a href="/curriculum.html" class="bc-hide-sm">Digital Arts</a>
        <span class="bc-sep bc-hide-sm">&rsaquo;</span>
        <span class="bc-current">Final Exam Study Guide</span>
      </div>

      <div class="silva-nav-spacer"></div>

      <button class="silva-copy-btn" onclick="silvaCopyHTML()" aria-label="Copy Canvas HTML to clipboard">
        &#128203; Copy Canvas HTML
      </button>
      <button class="silva-download-btn" onclick="silvaDownloadHTML()" aria-label="Download Canvas HTML as file">
        &#128229; Download HTML
      </button>
    </div>
  </nav>

  <div class="silva-page">
  <div id="silva-module-content">

  <div id="top" style="width:100%;margin:0 auto;font-family:Arial,sans-serif;color:#ffffff;background-color:#080808;background-image:linear-gradient(180deg,rgba(8,8,8,0.97) 0%,rgba(0,56,56,0.94) 50%,rgba(8,8,8,0.97) 100%),url('https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/PV_Panther_Watermark.png');background-position:center center,center center;background-repeat:no-repeat,no-repeat;background-attachment:fixed,fixed;overflow:hidden;">

    <!-- ════════════════════════ ENGLISH ════════════════════════ -->
    <div style="padding:28px 28px 40px;">
{en_block}
    </div>

    <!-- ════════════════════════ ESPAÑOL ════════════════════════ -->
    <div id="espanol" style="border-top:2px solid rgba(255,255,255,0.10);">
    <div style="padding:28px 28px 40px;">
{es_block}
    </div>
    </div>

  </div>
  </div>
  </div>

  <script>
    function silvaCopyHTML() {{
      const el = document.getElementById('top');
      const html = el.outerHTML;
      navigator.clipboard.writeText(html).then(function() {{
        var btn = document.querySelector('.silva-copy-btn');
        btn.textContent = '✓ Copied to clipboard!';
        btn.classList.add('copied');
        setTimeout(function() {{
          btn.innerHTML = '&#128203; Copy Canvas HTML';
          btn.classList.remove('copied');
        }}, 2500);
      }}).catch(function() {{ alert('Copy failed. Try selecting the page source manually.'); }});
    }}
    function silvaDownloadHTML() {{
      var el = document.getElementById('top');
      var html = el.outerHTML;
      var blob = new Blob([html], {{ type: 'text/html' }});
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'da-finals-quiz-prep-canvas.html';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }}
  </script>

  <script src="/js/silva-nav.js"></script>
</body>
</html>
'''

with open(OUTFILE, 'w') as f:
    f.write(PAGE)

# Verify div balance
open_count = PAGE.count('<div')
close_count = PAGE.count('</div>')
print(f'Wrote {OUTFILE}')
print(f'Size: {len(PAGE):,} bytes')
print(f'<div: {open_count}, </div>: {close_count}, balanced: {open_count == close_count}')
