// MRC Camera Modes (TV & AV) reflection template (Word .docx).
// Run: NODE_PATH=$(npm root -g) node tools/build-tvav-reflection.js
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle,
} = require('docx');

const ORANGE = 'C95201';
const DARK = '4A1E02';
const root = path.join(__dirname, '..');
const logo = fs.readFileSync(path.join(root, 'assets/mrc/MRC_Logo.png'));

const QUESTIONS = [
  'Which mode did you like better, TV or AV, and why?',
  'Which photo was the hardest to get? What did you change to make it work?',
  'Pick your favorite photo. What mode and setting did you use, and why did it work?',
  'Where could you use TV or AV mode in real life? What would you shoot?',
];

function writeLine() {
  return new Paragraph({
    spacing: { before: 220, after: 0 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: 'BBBBBB', space: 1 } },
    children: [new TextRun('')],
  });
}

function question(n, text) {
  const out = [
    new Paragraph({
      spacing: { before: 300, after: 60 },
      children: [
        new TextRun({ text: `${n}.  `, bold: true, color: ORANGE, size: 24, font: 'Arial' }),
        new TextRun({ text, bold: true, color: DARK, size: 24, font: 'Arial' }),
      ],
    }),
  ];
  for (let i = 0; i < 4; i++) out.push(writeLine());
  return out;
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
        children: [new TextRun({ text: 'Camera Modes: TV & AV Reflection', bold: true, color: ORANGE, size: 36, font: 'Arial' })],
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
        children: [new TextRun({ text: 'Answer each question in complete sentences.', italics: true, size: 22, color: '555555' })],
      }),
      ...QUESTIONS.flatMap((q, i) => question(i + 1, q)),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  const out = path.join(root, 'assets/mrc/study-guides/MRC_TV_AV_Reflection.docx');
  fs.writeFileSync(out, buf);
  console.log('wrote', out, (buf.length / 1024).toFixed(0) + ' KB');
});
