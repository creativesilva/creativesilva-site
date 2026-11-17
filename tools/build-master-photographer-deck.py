#!/usr/bin/env python3
# RETIRED 2026-11-16. This generated the ORIGINAL deck template. Chris now maintains the decks by
# hand in Google Drive (one per course, EN; he recolored MY WORK gray and added the PV logo), and
# the Spanish decks + both course project folders are zipped into assets/templates/master-photographer/
# by the Master Photographer workflow. The student deck ships only inside those project-folder ZIPs,
# hosted on each course Overview. Do NOT re-run this to regenerate the student deck; it would overwrite
# nothing the site uses. Kept for reference only. See the Master Photographer project memory.
# Generic 16:9 student slide-deck TEMPLATE for the Master Photographer project (Photography 1).
# A clean starting point students duplicate and customize. 8-slide spine:
#   1 Cover -> 2,3,4 Master photographer images (technique studied)
#   -> 5,6,7 My work (how I used it) -> 8 Reflection (closing slide).
# Run with the scratchpad venv python (python-pptx). Output: the .pptx under assets/templates/master-photographer/.
# No em dashes, no banned violence words (school setting). Arial, PVHS teal #007474 + red #E62429.
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

ROOT = "/Users/riva/RIVA_CODE/01_CREATIVE_Coding/creativesilva-site"
OUTDIR = os.path.join(ROOT, "assets/templates/master-photographer")
OUT = os.path.join(OUTDIR, "Master-Photographer-Slide-Template.pptx")

TEAL = RGBColor(0x00, 0x74, 0x74)
RED  = RGBColor(0xE6, 0x24, 0x29)
INK  = RGBColor(0x1A, 0x1A, 0x1A)
MUTE = RGBColor(0x8A, 0x8A, 0x8A)
HAIR = RGBColor(0xC9, 0xCF, 0xD3)
BOXF = RGBColor(0xF2, 0xF4, 0xF5)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Arial"

EW, EH = Inches(13.333), Inches(7.5)

prs = Presentation()
prs.slide_width = EW
prs.slide_height = EH
BLANK = prs.slide_layouts[6]

def _set(run, size, color, bold=False, italic=False, font=FONT):
    run.font.size = Pt(size); run.font.bold = bold; run.font.italic = italic
    run.font.name = font; run.font.color.rgb = color

def textbox(slide, x, y, w, h, lines, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    # lines: list of (text, size, color, bold, italic, space_after_pt)
    tb = slide.shapes.add_textbox(x, y, w, h); tf = tb.text_frame
    tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    for i, ln in enumerate(lines):
        text, size, color, bold, italic, sa = ln
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_before = Pt(0); p.space_after = Pt(sa)
        r = p.add_run(); r.text = text; _set(r, size, color, bold, italic)
    return tb

def rect(slide, x, y, w, h, fill, line=None, line_w=None, shape=MSO_SHAPE.RECTANGLE):
    sp = slide.shapes.add_shape(shape, x, y, w, h)
    sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line; sp.line.width = line_w or Pt(1)
    sp.shadow.inherit = False
    return sp

def line_in_rect(sp, lines, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE,
                 ml=0.18, mr=0.18, mt=0.1, mb=0.1):
    tf = sp.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = Inches(ml); tf.margin_right = Inches(mr)
    tf.margin_top = Inches(mt); tf.margin_bottom = Inches(mb)
    for i, ln in enumerate(lines):
        text, size, color, bold, italic, sa = ln
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_before = Pt(0); p.space_after = Pt(sa)
        r = p.add_run(); r.text = text; _set(r, size, color, bold, italic)

def header_bar(slide, eyebrow, big, accent):
    rect(slide, 0, 0, EW, Inches(1.18), accent)
    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.14), Inches(12.1), Inches(0.92))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    p1 = tf.paragraphs[0]; p1.space_after = Pt(2)
    r1 = p1.add_run(); r1.text = eyebrow; _set(r1, 12, WHITE, bold=True); r1.font._rPr.set("spc", "140")
    p2 = tf.add_paragraph(); p2.space_before = Pt(0)
    r2 = p2.add_run(); r2.text = big; _set(r2, 26, WHITE, bold=True)

def footer(slide):
    textbox(slide, Inches(0.6), Inches(7.04), Inches(12.1), Inches(0.34),
            [("Pioneer Valley High School  ·  CTE Photography  ·  Master Photographer Project", 9, MUTE, False, False, 0)],
            align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE)

def image_slot(slide, x, y, w, h, prompt):
    box = rect(slide, x, y, w, h, BOXF, line=HAIR, line_w=Pt(1.25))
    line_in_rect(box, [("＋", 30, HAIR, True, False, 4),
                       (prompt, 12.5, MUTE, False, False, 0)],
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    return box

def note_col(slide, x, y, w, eyebrow, accent, prompt):
    textbox(slide, x, y, w, Inches(0.4),
            [(eyebrow, 12, accent, True, False, 0)], anchor=MSO_ANCHOR.TOP)
    rule = rect(slide, x, y+Inches(0.42), Inches(1.1), Pt(3), accent)
    textbox(slide, x, y+Inches(0.66), w, Inches(3.6),
            [(prompt, 13.5, MUTE, False, True, 0)], anchor=MSO_ANCHOR.TOP)

# ---------------- Slide 1: Cover ----------------
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, Inches(0.42), EH, TEAL)                       # left spine
rect(s, Inches(0.95), Inches(1.5), Inches(1.4), Pt(4), TEAL)  # top rule
textbox(s, Inches(0.95), Inches(1.72), Inches(11.4), Inches(0.4),
        [("PIONEER VALLEY HIGH SCHOOL  ·  CTE PHOTOGRAPHY", 13, TEAL, True, False, 0)])
tb = s.shapes.add_textbox(Inches(0.9), Inches(2.25), Inches(11.5), Inches(2.0))
tf = tb.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.space_after = Pt(0)
r = p.add_run(); r.text = "Master Photographer"; _set(r, 58, INK, bold=True)
textbox(s, Inches(0.95), Inches(3.62), Inches(11.4), Inches(0.5),
        [("Selected works, and my own work inspired by them", 20, MUTE, False, True, 0)])
# fields block
fx, fy = Inches(0.95), Inches(4.55)
fields = [("Master photographer:", 4.9), ("Your name:", 4.9), ("Period:", 2.2), ("Course:", 3.4)]
cy = fy
for i, (lab, uw) in enumerate(fields):
    textbox(s, fx, cy, Inches(2.6), Inches(0.4), [(lab, 15, INK, True, False, 0)], anchor=MSO_ANCHOR.MIDDLE)
    val = "Photography 1" if lab == "Course:" else ""
    if val:
        textbox(s, fx+Inches(2.7), cy, Inches(uw), Inches(0.4), [(val, 15, INK, False, False, 0)], anchor=MSO_ANCHOR.MIDDLE)
    else:
        rect(s, fx+Inches(2.7), cy+Inches(0.34), Inches(uw), Pt(1.5), HAIR)  # fill-in rule
    cy = cy + Inches(0.55)
footer(s)

# ---------------- Slides 2-4: Master images ----------------
master_prompts = [
 "Pick a strong image by your master photographer. Name the technique it shows: composition, lighting, the moment, tone, or editing. Why does it work?",
 "Choose a second image. What is different about how it was made? Point to one clear choice the photographer made.",
 "Choose a third image. What visual thread runs through all three? This is the style you will bring into your own photos.",
]
for i in range(3):
    s = prs.slides.add_slide(BLANK)
    header_bar(s, "MASTER PHOTOGRAPHER", f"Image {i+1} of 3", TEAL)
    image_slot(s, Inches(0.6), Inches(1.6), Inches(7.25), Inches(4.95),
               "Place a master photographer image here")
    note_col(s, Inches(8.2), Inches(1.75), Inches(4.55), "WHAT I STUDIED", TEAL, master_prompts[i])
    footer(s)

# ---------------- Slides 5-7: My work ----------------
mine_prompts = [
 "Place your first edited photo. How did your master photographer influence it? Name what you borrowed: composition, light, the moment, tone, or editing.",
 "Place your second edited photo. Show a different part of the style you studied. Be specific about the choice you made.",
 "Place your third edited photo. Together, how do your three photos show the style of your master photographer?",
]
for i in range(3):
    s = prs.slides.add_slide(BLANK)
    header_bar(s, "MY WORK", f"Image {i+1} of 3", RED)
    image_slot(s, Inches(0.6), Inches(1.6), Inches(7.25), Inches(4.95),
               "Place your captured and edited photo here")
    note_col(s, Inches(8.2), Inches(1.75), Inches(4.55), "HOW I USED IT", RED, mine_prompts[i])
    footer(s)

# ---------------- Slide 8: Reflection (closing) ----------------
s = prs.slides.add_slide(BLANK)
header_bar(s, "CLOSING SLIDE", "Reflection", TEAL)
textbox(s, Inches(0.6), Inches(1.6), Inches(12.1), Inches(0.5),
        [("Look back at everything you studied and made. Answer in a few honest sentences.", 17, INK, True, False, 0)])
rb = rect(s, Inches(0.6), Inches(2.35), Inches(12.13), Inches(4.25), WHITE, line=HAIR, line_w=Pt(1.25))
line_in_rect(rb, [
    ("1.  What is the most important thing you learned from your master photographer?", 15, INK, False, False, 14),
    ("2.  How did studying their work change the way you capture or edit your own photos?", 15, INK, False, False, 14),
    ("3.  What will you carry into your next photography project?", 15, INK, False, False, 14),
    ("Type your answer below each question.", 13, MUTE, False, True, 0),
], align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, ml=0.3, mr=0.3, mt=0.26, mb=0.2)
footer(s)

os.makedirs(OUTDIR, exist_ok=True)
prs.save(OUT)
print("wrote", OUT, os.path.getsize(OUT), "bytes,", len(prs.slides.__iter__.__self__._sldIdLst), "slides")
