// Substitute plan (Word .docx) in the PVHS reflection-doc house style (CLAUDE.md #9):
// square PV logo floating behind the top-left, CENTERED teal title + gray subtitle, full-width
// teal rule, then teal section bars. Contains NO student data (schedule + instructions only).
// Run: NODE_PATH=$(npm root -g) node tools/build-sub-plan.js
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, AlignmentType, BorderStyle,
  Table, TableRow, TableCell, WidthType, ShadingType,
  HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom, TextWrappingType,
} = require('docx');

const TEAL = '007474', GRAY = '8A8A8A', WHITE = 'FFFFFF', INK = '1A1A1A';
const CONTENT_W = 10800;
const root = path.join(__dirname, '..');
const logo = fs.readFileSync(path.join(root, 'assets/PV_Square_Logo.png'));
// Chris's full email-signature block + handwritten signature, flattened to one image (his own asset).
const sig = fs.readFileSync(path.join(root, 'assets/course-documents/silva-signature-block-v1.png'));

function headerLogo() {
  return new ImageRun({
    type: 'png', data: logo, transformation: { width: 96, height: 96 },
    floating: {
      horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: 460000 },
      verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: 430000 },
      allowOverlap: true, behindDocument: true, wrap: { type: TextWrappingType.NONE },
    },
    altText: { title: 'PVHS', description: 'Pioneer Valley High School', name: 'PVHS' },
  });
}
const NB = { style: BorderStyle.NONE };
function sectionBar(text) {
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    borders: { top: NB, bottom: NB, left: NB, right: NB },
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { fill: TEAL, type: ShadingType.CLEAR },
      margins: { top: 70, bottom: 70, left: 160, right: 160 },
      children: [new Paragraph({ children: [new TextRun({ text, bold: true, color: WHITE, size: 24, font: 'Arial' })] })],
    })] })],
  });
}
function gap(after) { return new Paragraph({ spacing: { after }, children: [new TextRun({ text: '', size: 2 })] }); }
function para(text, o = {}) {
  return new Paragraph({ spacing: { before: o.before || 0, after: o.after == null ? 120 : o.after },
    children: [new TextRun({ text, size: o.size || 22, font: 'Arial', color: o.color || INK, bold: o.bold, italics: o.italics })] });
}
// bold teal lead label + normal continuation, on one paragraph
function labeled(lead, rest, o = {}) {
  return new Paragraph({ spacing: { after: o.after == null ? 80 : o.after },
    children: [
      new TextRun({ text: lead, bold: true, color: TEAL, size: 22, font: 'Arial' }),
      new TextRun({ text: rest, size: 22, font: 'Arial', color: INK }),
    ] });
}
// one class block: bold teal period/course/room line, then the work line
function classBlock(head, work) {
  return [
    new Paragraph({ spacing: { before: 60, after: 20 }, children: [new TextRun({ text: head, bold: true, color: TEAL, size: 23, font: 'Arial' })] }),
    new Paragraph({ spacing: { after: 140 }, children: [new TextRun({ text: work, size: 22, font: 'Arial', color: INK })] }),
  ];
}

const dateStr = new Date(2026, 8, 16).toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' });

const children = [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 160, after: 20 },
    children: [headerLogo(), new TextRun({ text: 'Substitute Plan', bold: true, color: TEAL, size: 40, font: 'Arial' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
    children: [new TextRun({ text: `${dateStr}  ·  Pioneer Valley High School  ·  Mr. Silva`, color: GRAY, size: 20, font: 'Arial' })] }),
  new Paragraph({ spacing: { after: 160 }, border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: TEAL, space: 2 } }, children: [new TextRun({ text: '', size: 2 })] }),

  para('Thank you for covering my classes today. Every class is independent work: students already have everything they need in their Canvas module (software, tools, and step-by-step instructions). Please keep students working on their module for the full period.', { italics: true, color: GRAY }),
  para('This plan covers Periods 1, 2, and 4. There is no class Period 3 (prep).', { after: 160 }),

  sectionBar('Today’s Classes'),
  ...classBlock('Period 1  ·  8:30–9:20 AM  ·  Photography 1  ·  Room 322',
    'First-year photo students. They are finalizing their edits in Lightroom and turning in Module 05: Lightroom Editing on Canvas.'),
  ...classBlock('Period 2  ·  9:30–10:20 AM  ·  Digital Arts 1  ·  Room 331',
    'Students are working on Module 05: Live Stream Graphic on Canvas.'),
  ...classBlock('Period 4  ·  11:35 AM–12:25 PM  ·  Photography 2  ·  Room 322',
    'Students are working on Module 04: Build Your Own Preset on Canvas.'),

  sectionBar('Classroom Rules'),
  labeled('Phones in the wall pockets.  ', 'Students put their phones in the wall pockets at the start of class and leave them there for the whole period.'),
  labeled('No camera check-outs.  ', 'Do not let students check out any cameras today.'),
  labeled('No photo walks.  ', 'Students stay in the classroom. No going outside or around campus to take photos today.'),
  labeled('Stay on the Canvas module.  ', 'Everything students need is in Canvas. They should be working on their module the entire period.'),

  sectionBar('Attendance'),
  para('A printed seating chart for each class is on my desk. Please mark any absent or tardy students on it. If you have Aeries substitute access, you may enter attendance there instead.', { after: 160 }),

  sectionBar('If You Need Help'),
  new Paragraph({ spacing: { after: 60 }, children: [
    new TextRun({ text: 'For anything urgent, call the main office. A neighboring teacher can also help if something comes up.  ', size: 22, font: 'Arial', color: INK }),
    new TextRun({ text: 'Thank you so much!', bold: true, color: TEAL, size: 22, font: 'Arial' }),
  ] }),
  new Paragraph({ spacing: { before: 20 }, children: [new ImageRun({
    type: 'png', data: sig, transformation: { width: 341, height: 249 },
    altText: { title: 'Chris Silva', description: 'Chris Silva signature block', name: 'signature' },
  })] }),
];

const doc = new Document({
  styles: { default: { document: { run: { font: 'Arial', size: 22, color: INK } } } },
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 900, right: 720, bottom: 720, left: 720 } } }, children }],
});
Packer.toBuffer(doc).then((buf) => {
  const out = path.join(root, 'assets/course-documents', 'PVHS-Substitute-Plan-2026-09-16.docx');
  fs.writeFileSync(out, buf);
  console.log('wrote', out, (buf.length / 1024).toFixed(0) + ' KB');
});
