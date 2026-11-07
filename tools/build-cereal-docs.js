// Cereal Box Group Project docs (Word .docx), DA1A Module 10. CLAUDE.md hard rule #9 template:
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
    const minH = (typeof q === 'object' && q.minH) ? q.minH : 1500;
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
// Universal module: subtitle carries the course + school, NO teacher name.
const SUB_EN = 'Digital Arts 1A · Pioneer Valley High School';
const SUB_ES = 'Arte Digital 1A · Pioneer Valley High School';

const DOCS = [
  // ---- Research ----
  { ...EN, outfile: 'Cereal-Box-Research-EN.docx', title: 'Cereal Box Project: Research', subtitle: SUB_EN,
    instructions: 'Pick one real cereal in your category. Study its box closely and answer every question in complete sentences.',
    questions: [
      'Cereal Name: What is the full name of the cereal you picked? Use the exact wording from the box.',
      { q: 'Photo of the Front: Paste a clear photo of the front of the box. The words need to be easy to read.', ph: 'Paste your photo here.', minH: 2600 },
      'Official Website: Find the brand’s official website. Paste the full link.',
      'Target Audience: Who is the cereal trying to sell to? Kids, parents, athletes, busy adults. Explain why you think so.',
      'Colors and Type: What colors and fonts does the box use, and what mood do they create?',
      'Two Competitors: Find two other cereals that compete with yours. Name them and say what they have in common.',
      'How Design Sells: How does the box’s design help the cereal sell? Use art words like contrast, typography, and layout.',
      'Your Hot Take: Would you buy it? Why or why not? What would you change to make it better?',
    ] },
  { ...ES, outfile: 'Cereal-Box-Research-ES.docx', title: 'Proyecto de Caja de Cereal: Investigación', subtitle: SUB_ES,
    instructions: 'Elige un cereal real de tu categoría. Estudia su caja con atención y responde cada pregunta con oraciones completas.',
    questions: [
      'Nombre del Cereal: ¿Cuál es el nombre completo del cereal que elegiste? Usa las palabras exactas de la caja.',
      { q: 'Foto del Frente: Pega una foto clara del frente de la caja. Las palabras deben leerse fácil.', ph: 'Pega tu foto aquí.', minH: 2600 },
      'Sitio Web Oficial: Busca el sitio web oficial de la marca. Pega el enlace completo.',
      'Público Meta: ¿A quién le quiere vender el cereal? Niños, papás, deportistas, adultos ocupados. Explica por qué.',
      'Colores y Tipografía: ¿Qué colores y fuentes usa la caja, y qué sensación crean?',
      'Dos Competidores: Busca otros dos cereales que compitan con el tuyo. Nómbralos y di qué tienen en común.',
      'Cómo Vende el Diseño: ¿Cómo ayuda el diseño de la caja a vender el cereal? Usa palabras de arte como contraste, tipografía y composición.',
      'Tu Opinión: ¿Lo comprarías? ¿Por qué sí o por qué no? ¿Qué cambiarías para mejorarlo?',
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
