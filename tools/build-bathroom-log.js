// Student Bathroom Sign-Out Log (Word .docx) in the PVHS reflection-doc house style (CLAUDE.md #9):
// floating PV logo, CENTERED teal title + gray subtitle, full-width teal rule, then a sign-out table
// (Student Name / Date / Time Out / Time In) with blank rows. TWO identical pages so it prints
// double-sided (50 lines per sheet). Reusable printable form, NO student data.
// Run: NODE_PATH=$(npm root -g) node tools/build-bathroom-log.js
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle, PageBreak,
  Table, TableRow, TableCell, WidthType, ShadingType, VerticalAlign, HeightRule,
  HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom, TextWrappingType,
} = require('docx');

const TEAL = '007474', GRAY = '8A8A8A', WHITE = 'FFFFFF', GRID = 'C4C4C4';
const CONTENT_W = 10800;
const COLS = [4800, 2000, 2000, 2000]; // Student Name, Date, Time Out, Time In
const ROWS = 25;
const ROW_H = 410;
const SUBTITLE = 'Pioneer Valley High School  ·  Photography 1 & Photography 2';
const root = path.join(__dirname, '..');
const logo = fs.readFileSync(path.join(root, 'assets/PV_Square_Logo.png'));

function headerLogo() {
  return new ImageRun({
    type: 'png', data: logo, transformation: { width: 92, height: 92 },
    floating: {
      horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: 460000 },
      verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: 318000 }, // raised to match Chris's v2 (the live .docx is his exact file)
      allowOverlap: true, behindDocument: true, wrap: { type: TextWrappingType.NONE },
    },
    altText: { title: 'PVHS', description: 'Pioneer Valley High School', name: 'PVHS' },
  });
}

const bd = { style: BorderStyle.SINGLE, size: 4, color: GRID };
const cb = { top: bd, bottom: bd, left: bd, right: bd };
function hCell(text, w) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA }, shading: { fill: TEAL, type: ShadingType.CLEAR },
    borders: cb, margins: { top: 70, bottom: 70, left: 120, right: 120 }, verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text, bold: true, color: WHITE, size: 22, font: 'Arial' })] })],
  });
}
function bCell(w) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA }, borders: cb, margins: { top: 30, bottom: 30, left: 120, right: 120 },
    children: [new Paragraph({ children: [new TextRun({ text: '', size: 22, font: 'Arial' })] })],
  });
}

function buildPage() {
  const rows = [new TableRow({ tableHeader: true,
    children: [hCell('Student Name', COLS[0]), hCell('Date', COLS[1]), hCell('Time Out', COLS[2]), hCell('Time In', COLS[3])] })];
  for (let i = 0; i < ROWS; i++) rows.push(new TableRow({ height: { value: ROW_H, rule: HeightRule.ATLEAST }, children: COLS.map((w) => bCell(w)) }));
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 80, after: 10 },
      children: [headerLogo(), new TextRun({ text: 'Student Bathroom Sign-Out Log', bold: true, color: TEAL, size: 36, font: 'Arial' })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 },
      children: [new TextRun({ text: SUBTITLE, color: GRAY, size: 20, font: 'Arial' })] }),
    new Paragraph({ spacing: { after: 140 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: TEAL, space: 2 } }, children: [new TextRun({ text: '', size: 2 })] }),
    new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: COLS, rows }),
  ];
}

const children = [...buildPage(), new Paragraph({ children: [new PageBreak()] }), ...buildPage()];

const doc = new Document({
  styles: { default: { document: { run: { font: 'Arial', size: 22 } } } },
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 760, right: 720, bottom: 540, left: 720 } } }, children }],
});
Packer.toBuffer(doc).then((buf) => {
  const out = path.join(root, 'assets/course-documents', 'PVHS-Student-Bathroom-Sign-Out-Log.docx');
  fs.writeFileSync(out, buf);
  console.log('wrote', out, (buf.length / 1024).toFixed(0) + ' KB');
});
