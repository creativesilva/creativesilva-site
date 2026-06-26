// MRC Movie Poster reflection template (Word .docx).
// Run: NODE_PATH=$(npm root -g) node tools/build-movieposter-reflection.js
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
  'Which concept did you choose or pitch, and what makes it scary?',
  'This was your first project working with a partner. How did putting your heads together on the concept help you? What was tricky about working together, and how did you handle it?',
  'This was your first time using off-camera flash (the Godox) to light your shot. How did the artificial light change your photo and its mood? What did you learn about lighting?',
  'How did you turn your daytime photo into a scary night scene in Photoshop? Think about the sky, the color, the shadows, and the vignette.',
  'If your movie were real, what would the trailer show? Would you watch it?',
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
      spacing: { before: 280, after: 60 },
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
        children: [new TextRun({ text: 'Movie Poster Reflection', bold: true, color: ORANGE, size: 36, font: 'Arial' })],
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
  const out = path.join(root, 'assets/mrc/study-guides/MRC_Movie_Poster_Reflection.docx');
  fs.writeFileSync(out, buf);
  console.log('wrote', out, (buf.length / 1024).toFixed(0) + ' KB');
});
