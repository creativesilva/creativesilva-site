// Canonical PVHS reflection builder (Word .docx). CLAUDE.md hard rule #9.
// New polished header: square PV logo floating BEHIND text (top-left), CENTERED title + subtitle,
// full-width teal rule, Name/Period/Date row, each question a teal-filled bar (white text),
// answer box with a "Type your answer here." placeholder that grows as the student types.
// SEPARATE English and Spanish documents, never bilingual.
// Run: NODE_PATH=$(npm root -g) node tools/build-reflection.js
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle,
  Table, TableRow, TableCell, WidthType, HeightRule, ShadingType, TabStopType,
  HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom, TextWrappingType,
} = require('docx');

const TEAL = '007474', GRAY = '8A8A8A', BORDER = 'C4C4C4', WHITE = 'FFFFFF';
const CONTENT_W = 10800;              // Letter (12240) minus 0.5in L/R margins (720 each)
const root = path.join(__dirname, '..');
const logo = fs.readFileSync(path.join(root, 'assets/PV_Square_Logo.png'));

// square PV logo, ~1in, floating behind the text in the top-left corner
function headerLogo() {
  return new ImageRun({
    type: 'png', data: logo, transformation: { width: 96, height: 96 },
    floating: {
      horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: 460000 },
      verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: 430000 },
      allowOverlap: true, behindDocument: true,
      wrap: { type: TextWrappingType.NONE },
    },
    altText: { title: 'PVHS', description: 'Pioneer Valley High School', name: 'PVHS' },
  });
}

// teal-filled question bar (single-cell table, white bold text)
function questionBar(n, text) {
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { fill: TEAL, type: ShadingType.CLEAR },
      margins: { top: 70, bottom: 70, left: 160, right: 160 },
      children: [new Paragraph({ children: [
        new TextRun({ text: `${n}.  `, bold: true, color: WHITE, size: 23, font: 'Arial' }),
        new TextRun({ text, bold: true, color: WHITE, size: 23, font: 'Arial' }),
      ] })],
    })] })],
  });
}

// bordered answer box with a light placeholder that the student types over
function answerBox(placeholder) {
  const b = { style: BorderStyle.SINGLE, size: 8, color: BORDER };
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    rows: [new TableRow({
      height: { value: 1500, rule: HeightRule.ATLEAST },
      children: [new TableCell({
        width: { size: CONTENT_W, type: WidthType.DXA },
        borders: { top: b, bottom: b, left: b, right: b },
        margins: { top: 100, bottom: 100, left: 160, right: 160 },
        children: [new Paragraph({ children: [new TextRun({ text: placeholder, italics: true, color: GRAY, size: 22 })] })],
      })],
    })],
  });
}

function buildDoc(cfg) {
  const children = [
    // Title paragraph (centered) carries the floating logo
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 160, after: 20 },
      children: [headerLogo(), new TextRun({ text: cfg.title, bold: true, color: TEAL, size: 40, font: 'Arial' })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
      children: [new TextRun({ text: cfg.subtitle, color: GRAY, size: 20, font: 'Arial' })] }),
    // full-width teal rule
    new Paragraph({ spacing: { after: 160 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: TEAL, space: 2 } }, children: [new TextRun({ text: '', size: 2 })] }),
    // Name / Period / Date row (bold teal, tab stops, thin bottom rule)
    new Paragraph({
      spacing: { after: 40 },
      tabStops: [{ type: TabStopType.LEFT, position: 4200 }, { type: TabStopType.LEFT, position: 8000 }],
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: BORDER, space: 6 } },
      children: [
        new TextRun({ text: cfg.nameLabel, bold: true, color: TEAL, size: 22, font: 'Arial' }),
        new TextRun({ text: '\t' + cfg.periodLabel, bold: true, color: TEAL, size: 22, font: 'Arial' }),
        new TextRun({ text: '\t' + cfg.dateLabel, bold: true, color: TEAL, size: 22, font: 'Arial' }),
      ],
    }),
    new Paragraph({ spacing: { before: 100, after: 120 }, children: [new TextRun({ text: cfg.instructions, italics: true, color: GRAY, size: 22, font: 'Arial' })] }),
  ];
  cfg.questions.forEach((q, i) => {
    children.push(questionBar(i + 1, q));
    children.push(new Paragraph({ spacing: { after: 60 }, children: [new TextRun('')] }));
    children.push(answerBox(cfg.placeholder));
    children.push(new Paragraph({ spacing: { after: 160 }, children: [new TextRun('')] }));
  });
  const doc = new Document({
    styles: { default: { document: { run: { font: 'Arial', size: 22, color: '1A1A1A' } } } },
    sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 900, right: 720, bottom: 900, left: 720 } } }, children }],
  });
  return Packer.toBuffer(doc).then((buf) => {
    fs.writeFileSync(path.join(root, 'assets/course-documents', cfg.outfile), buf);
    console.log('wrote', cfg.outfile, (buf.length / 1024).toFixed(0) + ' KB');
  });
}

// ---- shared labels ----
const EN = { nameLabel: 'Name', periodLabel: 'Period', dateLabel: 'Date',
  instructions: 'Take your time and answer in full sentences.', placeholder: 'Type your answer here.' };
const ES = { nameLabel: 'Nombre', periodLabel: 'Periodo', dateLabel: 'Fecha',
  instructions: 'Tómate tu tiempo y responde con oraciones completas.', placeholder: 'Escribe tu respuesta aquí.' };
const PVHS_EN = (course) => `${course} · Pioneer Valley High School · Mr. Silva`;
const PVHS_ES = (course) => `${course} · Pioneer Valley High School · Sr. Silva`;

const DOCS = [
  // Self-Portrait (Photography 1A)
  { ...EN, outfile: 'Self-Portrait-Reflection-EN.docx', title: 'Self-Portrait: Reflection', subtitle: PVHS_EN('Photography 1A'), questions: [
    'What was your idea for your self-portrait? What were you trying to show about yourself?',
    'How well do you think you executed your idea? What worked?',
    'What was the hardest part (lighting, framing, holding the phone, or the self-timer)?',
    'If you hid part of yourself with objects, how did you keep it recognizable as you?',
    'What would you do differently or better next time?',
  ]},
  { ...ES, outfile: 'Self-Portrait-Reflection-ES.docx', title: 'Autorretrato: Reflexión', subtitle: PVHS_ES('Fotografía 1A'), questions: [
    '¿Cuál era tu idea para tu autorretrato? ¿Qué tratabas de mostrar de ti?',
    '¿Qué tan bien crees que lograste tu idea? ¿Qué funcionó?',
    '¿Qué fue lo más difícil (la luz, el encuadre, sostener el teléfono o el temporizador)?',
    'Si tapaste parte de ti con objetos, ¿cómo lo mantuviste reconocible como tú?',
    '¿Qué harías diferente o mejor la próxima vez?',
  ]},
  // Composition Photo Walk (Photography 2A)
  { ...EN, outfile: 'Composition-Photo-Walk-Reflection-EN.docx', title: 'Composition Photo Walk: Reflection', subtitle: PVHS_EN('Photography 2A'), questions: [
    'Which composition rule was easiest for you to capture on the walk? Why?',
    'Which rule was the hardest? What made it difficult?',
    'Of your final six images, which one are you most proud of? What makes it strong?',
    'In editing, what one change made the biggest difference to an image?',
    'How did working with your partner help or challenge your process?',
    'What will you do differently on your next photo walk?',
  ]},
  { ...ES, outfile: 'Composition-Photo-Walk-Reflection-ES.docx', title: 'Caminata de Composición: Reflexión', subtitle: PVHS_ES('Fotografía 2A'), questions: [
    '¿Cuál regla de composición te fue más fácil de capturar en la caminata? ¿Por qué?',
    '¿Cuál regla fue la más difícil? ¿Qué la hizo difícil?',
    'De tus seis imágenes finales, ¿de cuál estás más orgulloso? ¿Qué la hace fuerte?',
    'En la edición, ¿qué cambio hizo la mayor diferencia en una imagen?',
    '¿Cómo te ayudó o te retó trabajar con tu compañero?',
    '¿Qué harás diferente en tu próxima caminata fotográfica?',
  ]},
  // Off-Camera Flash (Photography 2A)
  { ...EN, outfile: 'Off-Camera-Flash-Reflection-EN.docx', title: 'Off-Camera Flash: Reflection', subtitle: PVHS_EN('Photography 2A'),
    instructions: "Answer all 4 questions in complete sentences. This reflection is about your own experience, not your partner's.", questions: [
    'Compare a natural-light frame and an off-camera-flash frame from your photo walk. What looked different about the background and about your subject in each one?',
    'Walk through your settings for one off-camera-flash portrait. How did you set your ambient exposure for the background, and how did you use the flash to light your subject?',
    'What was the hardest part of using off-camera flash outdoors, and how did you work through it?',
    'Look at your 3 final portraits. Which one is your favorite, and why? What would you change next time to make your off-camera flash look even better?',
  ]},
  { ...ES, outfile: 'Off-Camera-Flash-Reflection-ES.docx', title: 'Flash Fuera de Cámara: Reflexión', subtitle: PVHS_ES('Fotografía 2A'),
    instructions: 'Responde las 4 preguntas en oraciones completas. Esta reflexión es sobre tu propia experiencia, no la de tu compañero.', questions: [
    'Compara un cuadro con luz natural y uno con flash fuera de cámara de tu caminata fotográfica. ¿Qué se veía diferente en el fondo y en tu sujeto en cada uno?',
    'Explica tus ajustes para un retrato con flash fuera de cámara. ¿Cómo ajustaste la exposición del ambiente para el fondo, y cómo usaste el flash para iluminar a tu sujeto?',
    '¿Qué fue lo más difícil de usar el flash fuera de cámara al aire libre, y cómo lo resolviste?',
    'Mira tus 3 retratos finales. ¿Cuál es tu favorito y por qué? ¿Qué cambiarías la próxima vez para que tu flash fuera de cámara se vea aún mejor?',
  ]},
  // Composition Concepts (Photography 1A)
  { ...EN, outfile: 'Composition-Concepts-Reflection-EN.docx', title: 'Composition Concepts: Reflection', subtitle: PVHS_EN('Photography 1A'), questions: [
    'Which 3 composition concepts did you choose?',
    'Which one did you enjoy the most, or find easiest to execute? Why?',
    'Which one was the hardest? Why?',
    'What would you do differently next time?',
  ]},
  { ...ES, outfile: 'Composition-Concepts-Reflection-ES.docx', title: 'Conceptos de Composición: Reflexión', subtitle: PVHS_ES('Fotografía 1A'), questions: [
    '¿Cuáles 3 conceptos de composición elegiste?',
    '¿Cuál disfrutaste más, o te resultó más fácil de hacer? ¿Por qué?',
    '¿Cuál fue el más difícil? ¿Por qué?',
    '¿Qué harías diferente la próxima vez?',
  ]},
  // Leading Lines Photo Walk (Photography 1A)
  { ...EN, outfile: 'Leading-Lines-Reflection-EN.docx', title: 'Leading Lines Photo Walk: Reflection', subtitle: PVHS_EN('Photography 1A'), questions: [
    'Who was your camera partner? Write their full name.',
    'What is a leading line, in your own words? Give one example you found on the walk.',
    'Look at your 6 photos. Which one shows leading lines the best, and what makes it strong?',
    'How did you cull your photos? How did you decide which one was the best of each example?',
    'How did working with your partner help you? Did the two of you find different kinds of lines?',
    'What would you do differently on your next photo walk to find better leading lines?',
  ]},
  { ...ES, outfile: 'Leading-Lines-Reflection-ES.docx', title: 'Caminata de Líneas Guía: Reflexión', subtitle: PVHS_ES('Fotografía 1A'), questions: [
    '¿Quién fue tu compañero de cámara? Escribe su nombre completo.',
    '¿Qué es una línea guía, en tus propias palabras? Da un ejemplo que encontraste en la caminata.',
    'Mira tus 6 fotos. ¿Cuál muestra mejor las líneas guía, y qué la hace fuerte?',
    '¿Cómo seleccionaste (cull) tus fotos? ¿Cómo decidiste cuál era la mejor de cada ejemplo?',
    '¿Cómo te ayudó trabajar con tu compañero? ¿Encontraron ustedes diferentes tipos de líneas?',
    '¿Qué harías diferente en tu próxima caminata para encontrar mejores líneas guía?',
  ]},
  // Sketchbook Cover (Digital Arts 1A) -- "medium" gets a plain-language parenthetical
  { ...EN, outfile: 'Sketchbook-Cover-Reflection-EN.docx', title: 'Sketchbook Cover Art: Reflection', subtitle: PVHS_EN('Digital Arts 1A'), questions: [
    'What are the 3 motivational words on your cover?',
    'Which word did you draw in Cooper Black?',
    'Name the 2 typefaces you chose from Adobe Fonts (one for each of your other 2 words).',
    'On the Adobe Fonts website, how can you test and see your own word in a font? Explain the steps.',
    'Which medium or mediums (the tools or materials you used, like pencil, marker, or colored pencil) did you use, and why?',
    'What are you most proud of on your cover?',
  ]},
  { ...ES, outfile: 'Sketchbook-Cover-Reflection-ES.docx', title: 'Arte de la Portada: Reflexión', subtitle: PVHS_ES('Arte Digital 1A'), questions: [
    '¿Cuáles son las 3 palabras motivadoras en tu portada?',
    '¿Cuál palabra dibujaste en Cooper Black?',
    'Nombra los 2 tipos de letra que elegiste de Adobe Fonts (uno para cada una de tus otras 2 palabras).',
    'En el sitio web de Adobe Fonts, ¿cómo puedes probar y ver tu propia palabra en un tipo de letra? Explica los pasos.',
    '¿Cuál medio o medios (las herramientas o materiales que usaste, como lápiz, marcador o lápiz de color) usaste, y por qué?',
    '¿De qué estás más orgulloso en tu portada?',
  ]},
  // Motivational Poster (Digital Arts 1A) - covers the whole process: print poster + mobile wallpaper
  { ...EN, outfile: 'Motivational-Poster-Reflection-EN.docx', title: 'Motivational Poster: Reflection', subtitle: PVHS_EN('Digital Arts 1A'), questions: [
    'Who did you choose for your poster (a real person or a fictional character), and why do they inspire you? What is the real quote you used?',
    'What is the exact name of the font (typeface) you used for your words, and why does it fit your poster?',
    'Walk through how you made the PRINT poster: cutting your subject off their background, blurring the background, and adding your words and colors.',
    'Walk through how you made the MOBILE wallpaper version: what did you change to fit the tall, narrow phone screen?',
    'What was the hardest part of the whole process, and how did you work through it?',
    'What are you most proud of, and what did you enjoy most? (If you did the extra-credit logo, tell us about it.)',
  ]},
  { ...ES, outfile: 'Motivational-Poster-Reflection-ES.docx', title: 'Póster Motivacional: Reflexión', subtitle: PVHS_ES('Arte Digital 1A'), questions: [
    '¿A quién elegiste para tu póster (una persona real o un personaje de ficción), y por qué te inspira? ¿Cuál es la frase real que usaste?',
    '¿Cuál es el nombre exacto del tipo de letra (fuente) que usaste para tus palabras, y por qué queda bien con tu póster?',
    'Explica cómo hiciste el póster para IMPRIMIR: recortar a tu sujeto de su fondo, desenfocar el fondo, y agregar tus palabras y colores.',
    'Explica cómo hiciste la versión de FONDO DE PANTALLA para el teléfono: ¿qué cambiaste para que quedara en la pantalla alta y angosta del teléfono?',
    '¿Cuál fue la parte más difícil de todo el proceso, y cómo la resolviste?',
    '¿De qué estás más orgulloso, y qué disfrutaste más? (Si hiciste el logo de crédito extra, cuéntanos sobre él.)',
  ]},
  // Studio Session / Panther of the Quarter (Photography 2A)
  { ...EN, outfile: 'Studio-Session-Reflection-EN.docx', title: 'Studio Session: Reflection', subtitle: PVHS_EN('Photography 2A'), questions: [
    'Who was in your group, and what role did each person play (Photographer, Art Director, or Lighting Assistant)? List your name and your two group members.',
    'What did you think of the studio session process, from start to finish?',
    'Would you have preferred a different role? Explain why or why not.',
    'What part of the project did you enjoy the most?',
    'What was the most challenging part, and how did you handle it?',
    'What, if anything, would you do differently next time?',
    'How did you make your editing decisions? Describe several specific changes you made to your images.',
  ]},
  { ...ES, outfile: 'Studio-Session-Reflection-ES.docx', title: 'Sesión de Estudio: Reflexión', subtitle: PVHS_ES('Fotografía 2A'), questions: [
    '¿Quiénes estaban en tu grupo y qué rol tuvo cada uno (Fotógrafo, Director de Arte o Asistente de Iluminación)? Escribe tu nombre y el de tus dos compañeros.',
    '¿Qué te pareció el proceso de la sesión de estudio, de principio a fin?',
    '¿Habrías preferido un rol diferente? Explica por qué sí o por qué no.',
    '¿Qué parte del proyecto disfrutaste más?',
    '¿Cuál fue la parte más difícil, y cómo la resolviste?',
    '¿Qué harías diferente la próxima vez, si acaso algo?',
    '¿Cómo tomaste tus decisiones de edición? Describe varios cambios específicos que hiciste a tus imágenes.',
  ]},
];

(async () => { for (const d of DOCS) await buildDoc(d); })();
