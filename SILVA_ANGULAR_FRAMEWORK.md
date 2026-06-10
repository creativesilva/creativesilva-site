# Silva Angular Framework

The locked house style for Pioneer Valley High School Digital Arts and
Photography Canvas pages. Paste this whole file into a fresh agent
session to bring it up to speed on the exact build style.

Master reference page: `curriculum/shared/da-finals-quiz-prep.html`.
Generator: `tools/build-da-finals.py`.

---

## 1. Non-Negotiable Rules

- Never use em dashes. No `—`, no `&mdash;`. Use a colon, comma, or a new sentence.
- No emojis in student-facing content. They read cheap. Use a text label, a colored chip, or an arrow (`&larr;` `&rarr;`) instead. (`tools/strip-emojis.py` removes them from the `#top` region.)
- Student-facing language at about a 5th grade reading level. Short, direct sentences. Active voice. Use "you" and "your".
- All Canvas assets use raw GitHub URLs (`https://raw.githubusercontent.com/...`). No Canvas-hosted file URLs, no relative paths, no invented filenames. Spaces in paths become `%20`.
- Bilingual by default: full English block first, then a full Spanish mirror below the `#espanol` anchor. English only when explicitly requested.
- Keep the copy/download script and `<script src="/js/silva-nav.js"></script>`. Keep the PVHS logo.

## 2. Canvas-Safe Constraints

The Canvas Rich Content Editor sanitizer strips a lot. Build only with what survives.

PRESERVED: inline `background` (solid color or single linear-gradient), `border` / `border-top` / `border-image`, `padding`, `margin`, `display:grid` / `flex`, `<img>` tags, inline `color` / `font-size`, `letter-spacing`, `text-transform`, `<strong>`.

STRIPPED: `border-radius`, `box-shadow`, `opacity`, `position:absolute`, `<style>` blocks, `<script>` inside the copied region, `transition`, `animation`, `:hover`, pseudo-elements, `background-image: url(...)` on most elements, `filter`.

Design implication: everything is angular (zero rounded corners). Accents are drawn with borders, gradients, and CSS-border shapes, never shadows or rounded chips.

## 3. Palette Tokens

```
Teal    solid #00b8b8   dim rgba(0,184,184,0.08)   eyebrow #80e0e0
        tint linear-gradient(180deg,rgba(0,116,116,0.10) 0%,rgba(0,116,116,0.03) 100%)
Orange  solid #FF6B1A   dim rgba(255,107,26,0.08)  eyebrow #ffb27c
        tint linear-gradient(180deg,rgba(255,107,26,0.16) 0%,rgba(255,107,26,0.04) 100%)
Cyan    solid #00c2ff   dim rgba(0,194,255,0.08)   eyebrow #7dd3fc
        tint linear-gradient(180deg,rgba(0,194,255,0.16) 0%,rgba(0,194,255,0.04) 100%)
Red     solid #E62429   dim rgba(230,36,41,0.08)   eyebrow #ffb3b6
Page background: #080808 with a teal vertical gradient overlay + PV watermark.
```

Use color by purpose: teal for content/categories, orange for format and action sections, cyan for study/info, red for rules.

## 4. Card Borders — THE CRITICAL RULE

Cards stay translucent so the PV watermark shows through. The accent frame
is a diagonal gradient on the card itself. The bright solid top stripe is a
thin child div pulled flush to the top with negative margins.

Two approaches that FAILED and must not be retried:
- A colored background wrapper to fake the frame: the bright wrapper bleeds through the translucent card and floods it.
- `border-image` slice `0 1 1 1` to keep a solid top: an active border-image suppresses the solid `border-top-color`, so the top edge renders invisible.

Outer section card (2px gradient frame, 4px solid top stripe):
```html
<div style="background:<TINT>;border:2px solid transparent;border-image:linear-gradient(135deg,<SOLID> 0%,<DIM> 100%) 1;padding:30px;margin-bottom:24px;position:relative;overflow:hidden;">
  <div style="height:4px;background:<SOLID>;margin:-30px -30px 24px -30px;"></div>
  ...content...
</div>
```

Inner tile (1px gradient frame, 3px solid top stripe):
```html
<div style="background:<WEDGE-OR-TINT>;border:1px solid transparent;border-image:linear-gradient(135deg,<SOLID> 0%,<DIM> 100%) 1;padding:20px 22px 24px;position:relative;overflow:hidden;">
  <div style="height:3px;background:<SOLID>;margin:-20px -22px 12px -22px;"></div>
  ...content...
</div>
```

The stripe child's negative margins must equal the card's top/left/right padding so it sits flush to the inner border edge. Optional inner-tile wedge background for extra accent: `linear-gradient(135deg,<accent 0.14> 0%,<accent 0.14> 10%,rgba(0,0,0,0.32) 10%,rgba(0,0,0,0.32) 100%)`. No corner triangles.

## 5. Buttons — THE FRAMEWORK RULE

Every button on every page is identical except the top accent color.
```html
<a href="<URL>" style="background:rgba(255,255,255,0.92);color:#003838;text-decoration:none;padding:7px 16px;display:inline-block;font-size:11pt;white-space:nowrap;border-top:2px solid <SECTION-ACCENT>;"><strong><LABEL></strong></a>
```
- Gray base `rgba(255,255,255,0.92)`, text `#003838`, padding `7px 16px`, `11pt`.
- The 2px top accent bar is the SOLID color of the section the button sits in. Toggle in the teal banner gets a teal bar; download in an orange section gets an orange bar.
- Add `download=""` for file downloads.

## 6. Eyebrow Chip, Hairline, Numbering

Eyebrow chip (the small label above each card title):
```html
<div style="display:inline-block;background:rgba(0,0,0,0.40);border-left:3px solid <SOLID>;padding:5px 12px 5px 10px;font-family:Arial,sans-serif;font-size:10pt;letter-spacing:0.22em;color:<EYEBROW>;text-transform:uppercase;margin-bottom:12px;"><strong>LABEL / NN</strong></div>
```

Hairline divider under each card title:
```html
<div style="height:2px;background:<SOLID>;width:60px;margin-bottom:22px;"></div>
```
(32px wide on inner tiles.)

Chip numbering (LOCKED): every main section chip reads `LABEL / NN / TT`, where NN is the section number and TT is the total number of main sections on the page, so a student sees where they are and how long the page is (e.g. `STUDY / 03 / 07`). The English block and the Spanish mirror are each their own series and BOTH restart at `01` (the Spanish first section is `01 / TT`, never continued from English). Grouped repeating sub-sections keep their own two-number sub-series and are NOT counted in the main total: categories run `CATEGORY 01 / 08` through `CATEGORY 08 / 08`, term tiles run `TERM 01 / 50`, etc. `tools/number-sections.py` applies and re-locks this; it is idempotent.

## 7. Page Structure

```
nav.silva-nav (breadcrumb + copy/download buttons)   <- stays outside the Canvas copy region
div.silva-page > div#silva-module-content
  div#top  (this is the Canvas copy root: page background + watermark)
    ENGLISH block: banner, then section cards in order
    div#espanol  SPANISH mirror: banner, then the same section cards translated
  copy/download <script>
  <script src="/js/silva-nav.js"></script>
```

Banner: teal gradient bar, PV logo left, centered eyebrow + title + hairline + tagline, language toggle button on the right (the only button in the banner). The single document download button lives at the END of the page in the closing card, not in the banner.

## 8. Horizontal Scroll Rows

Term tiles and stat tiles sit in a horizontal scroll row:
```html
<div style="display:grid;grid-auto-flow:column;grid-auto-columns:minmax(260px,1fr);overflow-x:auto;gap:14px;padding-bottom:8px;-webkit-overflow-scrolling:touch;">
  ...tiles...
</div>
<div class="scroll-hint" style="text-align:center;font-size:8pt;color:rgba(0,184,184,0.55);letter-spacing:0.22em;text-transform:uppercase;margin-top:14px;font-family:Arial,sans-serif;"><strong>« drag or swipe for more »</strong></div>
```

## 9. Build Checklist

- Zero rounded corners anywhere.
- Every card: translucent tint background, gradient border-image frame, solid top-stripe child. Watermark visible through cards.
- Every button: gray base, fixed size, section-colored 2px top bar.
- Bilingual EN block then ES mirror, unless English-only was requested.
- All asset URLs are raw GitHub, spaces as `%20`.
- No em dashes. 5th grade reading level. Active voice.
- Div opens equal div closes.
