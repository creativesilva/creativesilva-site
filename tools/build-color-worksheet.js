// Brand Color Analysis worksheet (Word .docx), SEPARATE English + Spanish docs (CLAUDE.md rule #9).
// Same polished header as the reflections (square PV logo behind the title, centered teal title +
// gray subtitle, teal rule, Name:/Period:/Date: row). Body: an intro, the business field, four
// touchpoint sections (heading bar + image-paste box + Main colors + Why it fits), a brand color
// palette box, then four analysis questions (teal bar + answer box).
// Run: NODE_PATH=$(npm root -g) node tools/build-color-worksheet.js
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
      allowOverlap: true, behindDocument: true, wrap: { type: TextWrappingType.NONE },
    },
    altText: { title: 'PVHS', description: 'Pioneer Valley High School', name: 'PVHS' },
  });
}

// teal-filled heading bar (single-cell table, white bold text); optional leading number
function bar(text) {
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE } },
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { fill: TEAL, type: ShadingType.CLEAR },
      margins: { top: 70, bottom: 70, left: 160, right: 160 },
      children: [new Paragraph({ children: [new TextRun({ text, bold: true, color: WHITE, size: 23, font: 'Arial' })] })],
    })] })],
  });
}

// bordered box with a light placeholder; minHeight in DXA controls how tall it starts
function box(placeholder, minHeight) {
  const b = { style: BorderStyle.SINGLE, size: 8, color: BORDER };
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    rows: [new TableRow({
      height: { value: minHeight, rule: HeightRule.ATLEAST },
      children: [new TableCell({
        width: { size: CONTENT_W, type: WidthType.DXA },
        borders: { top: b, bottom: b, left: b, right: b },
        margins: { top: 100, bottom: 100, left: 160, right: 160 },
        children: [new Paragraph({ children: [new TextRun({ text: placeholder, italics: true, color: GRAY, size: 22 })] })],
      })],
    })],
  });
}

function spacer(after) { return new Paragraph({ spacing: { after: after || 60 }, children: [new TextRun('')] }); }
function fieldLabel(text) {
  return new Paragraph({ spacing: { before: 80, after: 40 }, children: [new TextRun({ text, bold: true, color: TEAL, size: 22, font: 'Arial' })] });
}

function buildDoc(cfg) {
  const c = [
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
    new Paragraph({ spacing: { before: 100, after: 140 }, children: [new TextRun({ text: cfg.intro, italics: true, color: GRAY, size: 22, font: 'Arial' })] }),
    // business chosen
    fieldLabel(cfg.business), box(cfg.typeHere, 500), spacer(160),
  ];
  // four touchpoints: heading bar + image box + main colors + why it fits
  cfg.touchpoints.forEach((t) => {
    c.push(bar(t)); c.push(spacer(60));
    c.push(box(cfg.pasteHere, 2600)); c.push(spacer(20));
    c.push(fieldLabel(cfg.mainColors)); c.push(box(cfg.typeHere, 500));
    c.push(fieldLabel(cfg.whyFits)); c.push(box(cfg.typeHere, 800)); c.push(spacer(180));
  });
  // brand color palette
  c.push(bar(cfg.paletteTitle)); c.push(spacer(60));
  c.push(fieldLabel(cfg.palettePrompt)); c.push(box(cfg.typeHere, 800)); c.push(spacer(180));
  // analysis questions
  c.push(bar(cfg.analysisTitle)); c.push(spacer(80));
  cfg.questions.forEach((q, i) => {
    c.push(bar((i + 1) + '.  ' + q)); c.push(spacer(60));
    c.push(box(cfg.typeHere, 1300)); c.push(spacer(160));
  });
  const doc = new Document({
    styles: { default: { document: { run: { font: 'Arial', size: 22, color: '1A1A1A' } } } },
    sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 900, right: 720, bottom: 900, left: 720 } } }, children: c }],
  });
  return Packer.toBuffer(doc).then((buf) => {
    fs.writeFileSync(path.join(root, 'assets/course-documents', cfg.outfile), buf);
    console.log('wrote', cfg.outfile, (buf.length / 1024).toFixed(0) + ' KB');
  });
}

const EN = {
  outfile: 'Color-Analysis-Worksheet-EN.docx',
  title: 'Brand Color Analysis', subtitle: 'Digital Arts 1A · Pioneer Valley High School · Mr. Silva',
  nameLabel: 'Name:', periodLabel: 'Period:', dateLabel: 'Date:',
  intro: 'Pick one well-known business and show how it uses color at every customer touchpoint. Add an example image for each one, name the colors, and explain why they work.',
  business: 'Business you chose:', pasteHere: 'Paste your image here.', typeHere: 'Type here.',
  touchpoints: ['1.  Logo', '2.  Storefront', '3.  Packaging', '4.  Employee Outfits'],
  mainColors: 'Main colors:', whyFits: 'Why it fits the brand:',
  paletteTitle: 'Brand Color Palette', palettePrompt: 'List the 3 to 5 main brand colors:',
  analysisTitle: 'Color Analysis',
  questions: [
    'Why do you think the business chose these colors?',
    'How does the color theme make you feel?',
    'Is the color the same at every touchpoint? Give one example.',
    'What could you use from this brand in your own design work?',
  ],
};

const ES = {
  outfile: 'Color-Analysis-Worksheet-ES.docx',
  title: 'Análisis de Color de una Marca', subtitle: 'Arte Digital 1A · Pioneer Valley High School · Sr. Silva',
  nameLabel: 'Nombre:', periodLabel: 'Periodo:', dateLabel: 'Fecha:',
  intro: 'Elige un negocio muy conocido y muestra cómo usa el color en cada punto de contacto con el cliente. Agrega una imagen de ejemplo, nombra los colores y explica por qué funcionan.',
  business: 'Negocio que elegiste:', pasteHere: 'Pega tu imagen aquí.', typeHere: 'Escribe aquí.',
  touchpoints: ['1.  Logo', '2.  Tienda', '3.  Empaque', '4.  Ropa de los Empleados'],
  mainColors: 'Colores principales:', whyFits: 'Por qué combina con la marca:',
  paletteTitle: 'Paleta de Colores de la Marca', palettePrompt: 'Escribe los 3 a 5 colores principales:',
  analysisTitle: 'Análisis de Color',
  questions: [
    '¿Por qué crees que el negocio eligió estos colores?',
    '¿Cómo te hace sentir el tema de color?',
    '¿Es el color igual en cada punto de contacto? Da un ejemplo.',
    '¿Qué podrías usar de esta marca en tu propio diseño?',
  ],
};

(async () => { for (const d of [EN, ES]) await buildDoc(d); })();
