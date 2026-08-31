// Photography 1A - Composition Concepts reflection (Word .docx), worksheet/text-box style.
// Builds TWO separate documents: one English, one Spanish (never bilingual).
// Each question has a bordered answer box that grows as the student types.
// Run: NODE_PATH=$(npm root -g) node tools/build-composition-reflection.js
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle,
  Table, TableRow, TableCell, WidthType, HeightRule, ShadingType,
} = require('docx');

const TEAL = '007474';
const DARK = '10302F';
const CONTENT_W = 9360; // Letter minus 1in left/right margins
const root = path.join(__dirname, '..');
const logo = fs.readFileSync(path.join(root, 'assets/PV LOGO NEW.png'));

// a bordered answer box that grows as the student types
function answerBox() {
  const b = { style: BorderStyle.SINGLE, size: 8, color: '888888' };
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    rows: [new TableRow({
      height: { value: 1300, rule: HeightRule.ATLEAST },
      children: [new TableCell({
        width: { size: CONTENT_W, type: WidthType.DXA },
        borders: { top: b, bottom: b, left: b, right: b },
        shading: { fill: 'FAFAFA', type: ShadingType.CLEAR },
        margins: { top: 100, bottom: 100, left: 140, right: 140 },
        children: [new Paragraph({ children: [new TextRun('')] })],
      })],
    })],
  });
}

function question(n, text) {
  return [
    new Paragraph({
      spacing: { before: 320, after: 100 },
      children: [
        new TextRun({ text: `${n}.  `, bold: true, color: TEAL, size: 24, font: 'Arial' }),
        new TextRun({ text, bold: true, color: DARK, size: 24, font: 'Arial' }),
      ],
    }),
    answerBox(),
  ];
}

function buildDoc(cfg) {
  const doc = new Document({
    styles: { default: { document: { run: { font: 'Arial', size: 22, color: '1A1A1A' } } } },
    sections: [{
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, right: 1440, bottom: 1080, left: 1440 } } },
      children: [
        new Paragraph({
          alignment: AlignmentType.LEFT, spacing: { after: 60 },
          children: [new ImageRun({ type: 'png', data: logo, transformation: { width: 132, height: 132 },
            altText: { title: 'PVHS', description: 'Pioneer Valley High School', name: 'PVHS' } })],
        }),
        new Paragraph({
          spacing: { after: 0 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: TEAL, space: 4 } },
          children: [new TextRun({ text: cfg.title, bold: true, color: TEAL, size: 36, font: 'Arial' })],
        }),
        new Paragraph({
          spacing: { before: 60, after: 220 },
          children: [new TextRun({ text: cfg.subtitle, color: '777777', size: 18, font: 'Arial' })],
        }),
        new Paragraph({
          spacing: { after: 60 },
          children: [
            new TextRun({ text: cfg.nameLabel + ': ', bold: true, size: 22 }),
            new TextRun({ text: '________________________________', color: '888888' }),
            new TextRun({ text: '     ' + cfg.dateLabel + ': ', bold: true, size: 22 }),
            new TextRun({ text: '__________________', color: '888888' }),
          ],
        }),
        new Paragraph({
          spacing: { after: 200 },
          children: [
            new TextRun({ text: cfg.deviceLabel + ': ', bold: true, size: 22 }),
            new TextRun({ text: '________________________________________________________', color: '888888' }),
          ],
        }),
        new Paragraph({
          spacing: { after: 60 },
          children: [new TextRun({ text: cfg.instructions, italics: true, size: 22, color: '555555' })],
        }),
        ...cfg.questions.flatMap((q, i) => question(i + 1, q)),
        new Paragraph({ children: [new TextRun('')] }),
      ],
    }],
  });
  return Packer.toBuffer(doc).then((buf) => {
    const out = path.join(root, 'assets/course-documents', cfg.outfile);
    fs.writeFileSync(out, buf);
    console.log('wrote', cfg.outfile, (buf.length / 1024).toFixed(0) + ' KB');
  });
}

const EN = {
  outfile: 'Composition-Concepts-Reflection-EN.docx',
  title: 'Composition Concepts Reflection',
  subtitle: 'PHOTOGRAPHY 1A  •  PIONEER VALLEY HIGH SCHOOL  •  MR. SILVA',
  nameLabel: 'Name', dateLabel: 'Date', deviceLabel: 'Device you used (phone or school iPad)',
  instructions: 'Answer each question in complete sentences. The box grows as you type.',
  questions: [
    'Which 3 composition concepts did you choose?',
    'For each of your 3 photos, describe how you showed the concept.',
    'Which concept was the hardest to capture? Why?',
    'Which photo is your favorite? Why?',
    'What did you learn about composition from this project?',
  ],
};
const ES = {
  outfile: 'Composition-Concepts-Reflection-ES.docx',
  title: 'Reflexión de Conceptos de Composición',
  subtitle: 'FOTOGRAFÍA 1A  •  PIONEER VALLEY HIGH SCHOOL  •  SR. SILVA',
  nameLabel: 'Nombre', dateLabel: 'Fecha', deviceLabel: 'Dispositivo que usaste (teléfono o iPad de la escuela)',
  instructions: 'Responde cada pregunta en oraciones completas. El cuadro crece mientras escribes.',
  questions: [
    '¿Cuáles 3 conceptos de composición elegiste?',
    'Para cada una de tus 3 fotos, describe cómo mostraste el concepto.',
    '¿Cuál concepto fue el más difícil de capturar? ¿Por qué?',
    '¿Cuál foto es tu favorita? ¿Por qué?',
    '¿Qué aprendiste sobre la composición en este proyecto?',
  ],
};

(async () => { await buildDoc(EN); await buildDoc(ES); })();
