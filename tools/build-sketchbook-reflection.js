// Digital Arts 1A - Sketchbook Cover reflection (Word .docx), text-box style.
// Builds TWO separate documents: one English, one Spanish (never bilingual). CLAUDE.md hard rule #9.
// Run: NODE_PATH=$(npm root -g) node tools/build-sketchbook-reflection.js
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle,
  Table, TableRow, TableCell, WidthType, HeightRule, ShadingType,
} = require('docx');

const TEAL = '007474';
const DARK = '10302F';
const CONTENT_W = 9360;
const root = path.join(__dirname, '..');
const logo = fs.readFileSync(path.join(root, 'assets/PV LOGO NEW.png'));

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
    new Paragraph({ spacing: { before: 320, after: 100 }, children: [
      new TextRun({ text: `${n}.  `, bold: true, color: TEAL, size: 24, font: 'Arial' }),
      new TextRun({ text, bold: true, color: DARK, size: 24, font: 'Arial' }),
    ]}),
    answerBox(),
  ];
}
function buildDoc(cfg) {
  const doc = new Document({
    styles: { default: { document: { run: { font: 'Arial', size: 22, color: '1A1A1A' } } } },
    sections: [{
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, right: 1440, bottom: 1080, left: 1440 } } },
      children: [
        new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 60 },
          children: [new ImageRun({ type: 'png', data: logo, transformation: { width: 132, height: 132 },
            altText: { title: 'PVHS', description: 'Pioneer Valley High School', name: 'PVHS' } })] }),
        new Paragraph({ spacing: { after: 0 },
          border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: TEAL, space: 4 } },
          children: [new TextRun({ text: cfg.title, bold: true, color: TEAL, size: 36, font: 'Arial' })] }),
        new Paragraph({ spacing: { before: 60, after: 220 },
          children: [new TextRun({ text: cfg.subtitle, color: '777777', size: 18, font: 'Arial' })] }),
        new Paragraph({ spacing: { after: 200 }, children: [
          new TextRun({ text: cfg.nameLabel + ': ', bold: true, size: 22 }),
          new TextRun({ text: '______________________________', color: '888888' }),
          new TextRun({ text: '   ' + cfg.periodLabel + ': ', bold: true, size: 22 }),
          new TextRun({ text: '__________', color: '888888' }),
          new TextRun({ text: '   ' + cfg.dateLabel + ': ', bold: true, size: 22 }),
          new TextRun({ text: '______________', color: '888888' }),
        ]}),
        new Paragraph({ spacing: { after: 60 },
          children: [new TextRun({ text: cfg.instructions, italics: true, size: 22, color: '555555' })] }),
        ...cfg.questions.flatMap((q, i) => question(i + 1, q)),
        new Paragraph({ children: [new TextRun('')] }),
      ],
    }],
  });
  return Packer.toBuffer(doc).then((buf) => {
    fs.writeFileSync(path.join(root, 'assets/course-documents', cfg.outfile), buf);
    console.log('wrote', cfg.outfile, (buf.length / 1024).toFixed(0) + ' KB');
  });
}

const EN = {
  outfile: 'Sketchbook-Cover-Reflection-EN.docx',
  title: 'Sketchbook Cover Reflection',
  subtitle: 'DIGITAL ARTS 1A  •  PIONEER VALLEY HIGH SCHOOL  •  MR. SILVA',
  nameLabel: 'Name', periodLabel: 'Period', dateLabel: 'Date',
  instructions: 'Answer each question in complete sentences. The box grows as you type.',
  questions: [
    'What are the 3 motivational words on your cover?',
    'Which word did you draw in Cooper Black?',
    'Name the 2 typefaces you chose from Adobe Fonts (one for each of your other 2 words).',
    'On the Adobe Fonts website, how can you test and see your own word in a font? Explain the steps.',
    'Which medium or mediums did you use, and why?',
    'What are you most proud of on your cover?',
  ],
};
const ES = {
  outfile: 'Sketchbook-Cover-Reflection-ES.docx',
  title: 'Reflexión de la Portada del Cuaderno',
  subtitle: 'ARTE DIGITAL 1A  •  PIONEER VALLEY HIGH SCHOOL  •  SR. SILVA',
  nameLabel: 'Nombre', periodLabel: 'Periodo', dateLabel: 'Fecha',
  instructions: 'Responde cada pregunta en oraciones completas. El cuadro crece mientras escribes.',
  questions: [
    '¿Cuáles son las 3 palabras motivadoras en tu portada?',
    '¿Cuál palabra dibujaste en Cooper Black?',
    'Nombra los 2 tipos de letra que elegiste de Adobe Fonts (uno para cada una de tus otras 2 palabras).',
    'En el sitio web de Adobe Fonts, ¿cómo puedes probar y ver tu propia palabra en un tipo de letra? Explica los pasos.',
    '¿Cuál medio o medios usaste, y por qué?',
    '¿De qué estás más orgulloso en tu portada?',
  ],
};

(async () => { await buildDoc(EN); await buildDoc(ES); })();
