// MRC Panorama Project reflection template (Word .docx), worksheet style.
// Each question has a bordered answer box that grows as the student types.
// Run: NODE_PATH=$(npm root -g) node tools/build-panorama-reflection.js
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle,
  Table, TableRow, TableCell, WidthType, HeightRule, ShadingType,
} = require('docx');

const ORANGE = 'C95201';
const DARK = '4A1E02';
const CONTENT_W = 9360;
const root = path.join(__dirname, '..');
const logo = fs.readFileSync(path.join(root, 'assets/mrc/MRC_Logo.png'));

const QUESTIONS = [
  'What worked well in your panoramas? What are you proud of?',
  'What did not work, or what was tricky during shooting or merging?',
  'What would you do differently next time to make a better panorama?',
  'What did you like most about this project? And if you could shoot a panorama of anywhere in the world, where would it be, and why?',
];

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
        new TextRun({ text: `${n}.  `, bold: true, color: ORANGE, size: 24, font: 'Arial' }),
        new TextRun({ text, bold: true, color: DARK, size: 24, font: 'Arial' }),
      ],
    }),
    answerBox(),
  ];
}

const doc = new Document({
  styles: { default: { document: { run: { font: 'Arial', size: 22, color: '1A1A1A' } } } },
  sections: [{
    properties: {
      page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, right: 1440, bottom: 1080, left: 1440 } },
    },
    children: [
      new Paragraph({
        alignment: AlignmentType.LEFT,
        spacing: { after: 60 },
        children: [new ImageRun({ type: 'png', data: logo, transformation: { width: 165, height: 108 },
          altText: { title: 'MRC', description: 'Mark Richardson Center', name: 'MRC' } })],
      }),
      new Paragraph({
        spacing: { after: 0 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: ORANGE, space: 4 } },
        children: [new TextRun({ text: 'Panorama Project Reflection', bold: true, color: ORANGE, size: 36, font: 'Arial' })],
      }),
      new Paragraph({
        spacing: { before: 60, after: 220 },
        children: [new TextRun({ text: 'DIGITAL ARTS 1A  •  MARK RICHARDSON CENTER', color: '777777', size: 18, font: 'Arial' })],
      }),
      new Paragraph({
        spacing: { after: 200 },
        children: [
          new TextRun({ text: 'Name: ', bold: true, size: 22 }),
          new TextRun({ text: '___________________________________', color: '888888' }),
          new TextRun({ text: '          Date: ', bold: true, size: 22 }),
          new TextRun({ text: '____________________', color: '888888' }),
        ],
      }),
      new Paragraph({
        spacing: { after: 60 },
        children: [new TextRun({ text: 'Answer each question in complete sentences. The box grows as you type.', italics: true, size: 22, color: '555555' })],
      }),
      ...QUESTIONS.flatMap((q, i) => question(i + 1, q)),
      new Paragraph({ children: [new TextRun('')] }),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  const out = path.join(root, 'assets/mrc/study-guides/MRC_Panorama_Reflection.docx');
  fs.writeFileSync(out, buf);
  console.log('wrote', out, (buf.length / 1024).toFixed(0) + ' KB');
});
