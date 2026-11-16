// Cereal Box Group Project docs (Word .docx), Digital Arts Module 10. CLAUDE.md hard rule #9 template:
// square PV logo floating behind the top-left, centered teal title + gray subtitle, teal rule,
// Name/Period/Date row, then each question as a teal bar above a bordered answer box.
// SEPARATE EN + ES docs (never bilingual). UNIVERSAL module (shared with other PVHS teachers),
// so the subtitle carries NO teacher name. Research drops the Elements of Art section.
// Run: NODE_PATH=$(npm root -g) node tools/build-cereal-docs.js
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle,
  Table, TableRow, TableCell, WidthType, HeightRule, ShadingType, TabStopType,
  HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom, TextWrappingType,
} = require('docx');

const TEAL = '007474', GRAY = '8A8A8A', BORDER = 'C4C4C4', WHITE = 'FFFFFF';
const CONTENT_W = 10800;
const root = path.join(__dirname, '..');
const logo = fs.readFileSync(path.join(root, 'assets/PV_Square_Logo.png'));

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

function answerBox(placeholder, minH) {
  const b = { style: BorderStyle.SINGLE, size: 8, color: BORDER };
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    rows: [new TableRow({
      height: { value: minH || 1500, rule: HeightRule.ATLEAST },
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
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 160, after: 20 },
      children: [headerLogo(), new TextRun({ text: cfg.title, bold: true, color: TEAL, size: 40, font: 'Arial' })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
      children: [new TextRun({ text: cfg.subtitle, color: GRAY, size: 20, font: 'Arial' })] }),
    new Paragraph({ spacing: { after: 160 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: TEAL, space: 2 } }, children: [new TextRun({ text: '', size: 2 })] }),
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
    const text = (typeof q === 'string') ? q : q.q;
    const ph = (typeof q === 'object' && q.ph) ? q.ph : cfg.placeholder;
    const minH = (typeof q === 'object' && q.minH) ? q.minH : (cfg.boxMinH || 1500);
    children.push(questionBar(i + 1, text));
    children.push(new Paragraph({ spacing: { after: 60 }, children: [new TextRun('')] }));
    children.push(answerBox(ph, minH));
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

const EN = { nameLabel: 'Name:', periodLabel: 'Period:', dateLabel: 'Date:', placeholder: 'Type your answer here.' };
const ES = { nameLabel: 'Nombre:', periodLabel: 'Periodo:', dateLabel: 'Fecha:', placeholder: 'Escribe tu respuesta aquí.' };
// Universal module (Chris 2026-11-15): subtitle is "Digital Arts" with NO course number (not 1A/2A)
// and NO teacher name, so any Digital Arts teacher can use it.
const SUB_EN = 'Digital Arts · Pioneer Valley High School';
const SUB_ES = 'Arte Digital · Pioneer Valley High School';

const DOCS = [
  // ---- Design Detective (the existing-cereal audit; replaces Research, hierarchy-forward) ----
  { ...EN, outfile: 'Cereal-Box-Design-Detective-EN.docx', title: 'Cereal Box Design Detective', subtitle: SUB_EN, boxMinH: 700,
    instructions: 'Investigate how packaging designers control attention. Work with a partner, study one real cereal box, and answer every question in complete sentences. Good packaging does not just look cool: it tells your eye where to look.',
    questions: [
      { q: 'The Cereal You Picked: Write the full name of the real cereal, then paste a clear photo of the FRONT of the box.', ph: 'Cereal name, then paste your photo here.', minH: 1600 },
      'The 3-Second Test: Have your partner show you the front for just 3 seconds, then hide it. Write what you noticed 1st, 2nd, and 3rd, in that order. This order is the visual hierarchy the designer built.',
      'Visual Hierarchy (the big one): What is the biggest, boldest element on the front? What is the smallest? Explain how size, color, and placement move your eye from the most important information to the least important.',
      'Attention Techniques: Which techniques does the designer use to catch your eye: size and scale, color, contrast, typography, imagery or mascot, placement, or spacing? List the ones you see, then name the ONE that works best and say why.',
      'Color Scheme: What is the main color, and what are the accent colors? What mood or feeling do these colors create?',
      'Typefaces: Describe the fonts. Is the title font fun, bold, or classic? Is the small text easy to read? How do the fonts fit the cereal’s personality?',
      'Who It Is For: Who is this cereal designed for: kids, teens, families, health-focused adults, or athletes? Name TWO visual clues on the box that support your answer.',
      'Think Like a Designer: Name one thing this packaging does WELL (how clearly it communicates, not whether you like it), and one thing you would IMPROVE.',
      'Compare and Apply: Switch boxes with another group. How does the new box guide your attention differently? Then name one design strategy you might use in your OWN cereal brand.',
    ] },
  { ...ES, outfile: 'Cereal-Box-Design-Detective-ES.docx', title: 'Detective del Diseño de Cajas de Cereal', subtitle: SUB_ES, boxMinH: 700,
    instructions: 'Investiga cómo los diseñadores de empaques controlan la atención. Trabaja con un compañero, estudia una caja de cereal real y responde cada pregunta en oraciones completas. Un buen empaque no solo se ve bien: le dice a tu ojo dónde mirar.',
    questions: [
      { q: 'El Cereal que Elegiste: Escribe el nombre completo del cereal real, luego pega una foto clara del FRENTE de la caja.', ph: 'Nombre del cereal, luego pega tu foto aquí.', minH: 1600 },
      'La Prueba de 3 Segundos: Pide a tu compañero que te muestre el frente por solo 3 segundos, luego que lo esconda. Escribe qué notaste 1ro, 2do y 3ro, en ese orden. Ese orden es la jerarquía visual que creó el diseñador.',
      'Jerarquía Visual (lo más importante): ¿Cuál es el elemento más grande y llamativo del frente? ¿Cuál es el más pequeño? Explica cómo el tamaño, el color y la ubicación mueven tu ojo de lo más importante a lo menos importante.',
      'Técnicas de Atención: ¿Qué técnicas usa el diseñador para atraer tu ojo: tamaño y escala, color, contraste, tipografía, imagen o mascota, ubicación o espaciado? Enumera las que ves, luego nombra la que funciona MEJOR y di por qué.',
      'Esquema de Color: ¿Cuál es el color principal y cuáles son los colores de acento? ¿Qué ánimo o sensación crean estos colores?',
      'Tipografías: Describe las fuentes. ¿La fuente del título es divertida, fuerte o clásica? ¿El texto pequeño es fácil de leer? ¿Cómo combinan las fuentes con la personalidad del cereal?',
      'Para Quién Es: ¿Para quién está diseñado este cereal: niños, adolescentes, familias, adultos enfocados en la salud o deportistas? Nombra DOS pistas visuales de la caja que apoyen tu respuesta.',
      'Piensa Como Diseñador: Nombra una cosa que este empaque hace BIEN (qué tan claro comunica, no si te gusta), y una cosa que MEJORARÍAS.',
      'Compara y Aplica: Intercambia cajas con otro grupo. ¿Cómo guía tu atención de forma diferente la caja nueva? Luego nombra una estrategia de diseño que podrías usar en TU propia marca de cereal.',
    ] },
  // ---- Design Choices ----
  { ...EN, outfile: 'Cereal-Box-Design-Choices-EN.docx', title: 'Cereal Box Project: Design Choices', subtitle: SUB_EN,
    instructions: 'Make these choices with your partner. Fill out your own copy so you both have the same plan, the same HEX codes, and the same font names.',
    questions: [
      'Cereal Name: The full name of your cereal. Short, fun, easy to say. Write it exactly how it will go on the box.',
      'Target Audience: Who is the cereal for? Write the age group and the lifestyle.',
      { q: 'Mascot: Describe or sketch your mascot. Animal, monster, person, or food character. Give it a name.', ph: 'Describe or paste your mascot sketch here.', minH: 2400 },
      'Color Palette: Pick 3 to 5 colors. Write the HEX code for each one. Everyone in your group uses the same codes.',
      'Three Fonts: Pick three fonts: one fun title font, one accent font, and one easy-to-read font for small text.',
      'Tagline: A short phrase that sells your cereal. Short, fun, easy to say. Goes on the front of the box.',
    ] },
  { ...ES, outfile: 'Cereal-Box-Design-Choices-ES.docx', title: 'Proyecto de Caja de Cereal: Decisiones de Diseño', subtitle: SUB_ES,
    instructions: 'Toma estas decisiones con tu compañero. Llena tu propia copia para que ambos tengan el mismo plan, los mismos códigos HEX y los mismos nombres de fuentes.',
    questions: [
      'Nombre del Cereal: El nombre completo de tu cereal. Corto, divertido, fácil de decir. Escríbelo tal como irá en la caja.',
      'Público Meta: ¿Para quién es el cereal? Escribe la edad y el estilo de vida.',
      { q: 'Mascota: Describe o dibuja tu mascota. Animal, monstruo, persona o personaje de comida. Ponle un nombre.', ph: 'Describe o pega el dibujo de tu mascota aquí.', minH: 2400 },
      'Paleta de Colores: Elige de 3 a 5 colores. Escribe el código HEX de cada uno. Todos en tu grupo usan los mismos códigos.',
      'Tres Fuentes: Elige tres fuentes: una divertida para el título, una de acento, y una fácil de leer para texto pequeño.',
      'Eslogan: Una frase corta que vende tu cereal. Corta, divertida, fácil de decir. Va en el frente de la caja.',
    ] },
  // ---- Reflection ----
  { ...EN, outfile: 'Cereal-Box-Reflection-EN.docx', title: 'Cereal Box Project: Reflection', subtitle: SUB_EN,
    instructions: 'Answer every prompt in complete sentences. Be honest and specific about your own work.',
    questions: [
      'My Design Choices: What design choices did you make on your panels? Why those colors, fonts, or images?',
      'What Went Right: What part of the project went the best? Why do you think it worked?',
      'What I Would Change: If you could redo one thing on your box, what would it be and why?',
      'Partner Wins: What did you and your partner do really well together? Name something specific.',
      'What Was Hard: What was the hardest part of the project? How did you handle it?',
      'Real-World Connect: How is what you did the same as what a real package designer does on the job?',
    ] },
  { ...ES, outfile: 'Cereal-Box-Reflection-ES.docx', title: 'Proyecto de Caja de Cereal: Reflexión', subtitle: SUB_ES,
    instructions: 'Responde cada pregunta en oraciones completas. Sé honesto y específico sobre tu propio trabajo.',
    questions: [
      'Mis Decisiones de Diseño: ¿Qué decisiones de diseño tomaste en tus paneles? ¿Por qué esos colores, fuentes o imágenes?',
      'Qué Salió Bien: ¿Qué parte del proyecto salió mejor? ¿Por qué crees que funcionó?',
      'Qué Cambiaría: Si pudieras rehacer una cosa de tu caja, ¿qué sería y por qué?',
      'Logros con Tu Compañero: ¿Qué hicieron muy bien juntos tú y tu compañero? Nombra algo específico.',
      'Qué Fue Difícil: ¿Cuál fue la parte más difícil del proyecto? ¿Cómo la resolviste?',
      'Conexión Real: ¿En qué se parece lo que hiciste a lo que hace un diseñador de empaques en su trabajo?',
    ] },
];

Promise.all(DOCS.map(buildDoc)).then(() => console.log('done:', DOCS.length, 'docs')).catch((e) => { console.error(e); process.exit(1); });
