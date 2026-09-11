# Silva Angular Framework

The locked house style for Pioneer Valley High School Digital Arts and
Photography Canvas pages. Paste this whole file into a fresh agent
session to bring it up to speed on the exact build style.

Master reference page: `curriculum/shared/da-finals-quiz-prep.html`.
Generator: `tools/build-da-finals.py`.

---

## 1. Non-Negotiable Rules

- Never use em dashes. No `—`, no `&mdash;`. Use a colon, comma, or a new sentence.
- Never use the words **shoot, shooting, shot, shots** (or **screenshot**). Hard ban, as absolute as the em-dash ban: in a school these words evoke school shootings. Use capture / take photos / photograph, a session, photo / image / frame, "captured in RAW", "screen capture". Applies to EN and ES, headings, chips, alt text, comments. **Manufacturer exception (2026-09-11):** a maker's real menu/product name may contain an otherwise-banned word when accuracy requires it (e.g. Canon's **Shooting** menu). Use it only as the literal manufacturer term. The `build-image-series.py` ban-guard allowlists the exact phrases "Shooting tab" / "Shooting menu".
- No emojis in student-facing content. They read cheap. Use a text label, a colored chip, or an arrow (`&larr;` `&rarr;`) instead. (`tools/strip-emojis.py` removes them from the `#top` region.)
- Student-facing language at about a 5th grade reading level. Short, direct sentences. Active voice. Use "you" and "your".
- All Canvas assets host from `https://www.creativesilva.com/assets/...` (the ONLY district-whitelisted domain; raw GitHub / jsDelivr render as broken images in the student Canvas iOS app). No Canvas-hosted file URLs, no relative paths, no invented filenames. Spaces in paths become `%20`.
- Bilingual by default: full English block first, then a full Spanish mirror below the `#espanol` anchor. English only when explicitly requested.
- Deliverables, per step (REQUIRED, no exception): each STEP is its own separately-graded Canvas submission with its own deliverable(s), always, unless Chris says otherwise (e.g. Sketchbook step 1 = upload 2 images, step 2 = upload the reflection: two graded assignments). The compact `DELIVERABLES` / `ENTREGABLES` box lives ONLY on the step page that submits that deliverable, placed at the **TOP of the step** (right after the banner, before the content cards, LOCKED 2026-09-10, same as the Downloads section on Overviews), stating exactly what THAT step turns in with a clear file type (.docx, JPG, high-resolution JPG, .xmp). The box is **GOLD** (its own color so turn-ins are unmistakable, distinct from teal content, orange Downloads, purple Resources): a gold section box with the **combined chip header** (gold deliverables icon `deliverables-v4.png` on the LEFT, gold title `DELIVERABLES &middot; TURN IT IN` / `ENTREGABLES &middot; ENTR&Eacute;GALO`, accent rule below) exactly like every other section (see &sect;3.5), then a **forecast** line and the turn-in bullets. Forecast: &#x201C;Work through every task on this page to finish this step the right way. Each step in this module gets its own grade, so turn in the work below:&#x201D; / &#x201C;Trabaja cada tarea de esta p&aacute;gina para terminar bien este paso. Cada paso de este m&oacute;dulo tiene su propia calificaci&oacute;n, as&iacute; que entrega lo siguiente:&#x201D;. Helper `deliverables_box(es, items)`. NEVER put deliverables on the Overview. EN in `#top`, ES in `#espanol`.
- Module-type identity: the SUPERSEDED system (2026-09-11) put an assignment-type icon at the top-RIGHT of the first card&#x2019;s title (`<!--IDEYE-->`, applied by `tools/apply-id-icons.py`). The combined chip-header system (&sect;3.5) REPLACES it: type identity now lives in the section chip headers themselves (the Overview&#x2019;s first card is a &#x201C;The Module Overview&#x201D; type chip; content cards carry the step-check icon). `apply-id-icons.py` is now a graceful no-op on chip-format pages (it finds no legacy eyebrow and skips). Do NOT re-add the old top-right ID chip to a converted page. The type-icon family still lives in `assets/Icons/assignment/` (220px PNGs from SVG masters in `_src/`); its teal content-variant set feeds the chip headers. **White header icon (LOCKED 2026-09-11):** photo-walk modules and own-device modules carry a WHITE module-type icon (44px) in the banner's RIGHT cell, immediately left of the language-toggle button (a flex row, `justify-self:end`), NOT crowning the title. Pass it via `banner(..., hicon=HICON_PHOTO_WALK)` or `HICON_YOUR_DEVICE`. Photo-walk modules use the white photo-walk icon; own-device modules the white iPad/iPhone icon.
- Keep the copy/download script and `<script src="/js/silva-nav.js"></script>`. Keep the PVHS logo.

## 2. Canvas-Safe Constraints

The Canvas Rich Content Editor sanitizer strips a lot. Build only with what survives.

PRESERVED: inline `background` (solid color or single linear-gradient, multi-stop is fine), solid `border` / `border-top` (with a real color), `padding`, `margin`, `display:block` / `grid` / `flex`, `<img>` tags, inline `color` / `font-size`, `letter-spacing`, `text-transform`, `<strong>`, `<table>` / `<tr>` / `<td>` structure.

STRIPPED (verified the hard way, 2026-08-21): `border-image` (a `border:2px solid transparent;border-image:...` becomes an INVISIBLE border), `grid-template-columns` values containing `repeat()` (the whole declaration is dropped, collapsing the grid; explicit tracks like `minmax(0,1fr) minmax(0,1fr) ...` survive), `border-radius`, `box-shadow`, `opacity`, `position:absolute`, `<style>` blocks, `<script>` inside the copied region, `transition`, `animation`, `:hover`, pseudo-elements, `background-image: url(...)` on most elements, `filter`.

Design implication: everything is angular (zero rounded corners). Accents are drawn with borders, gradients, and CSS-border shapes, never shadows or rounded chips.

**Canvas does NOT sanitize `<iframe>` content.** The school-day countdown card renders inside an iframe, so it keeps `border-image` and anything else. Inline HTML pasted into the page IS sanitized. So a countdown card (iframe) and a nav button (inline) will NOT match if the button leans on `border-image`. Build inline elements to match iframe elements using only preserved CSS (see §7.5).

### 2.1 Multi-column layout: use a table, not grid

CSS grid columns collapse in Canvas (see `repeat()` above, and grid support is flaky generally). For a fixed N-column row (e.g. the 5 nav buttons), use a `<table role="presentation" style="width:100%;border-collapse:collapse;table-layout:fixed;"><tbody><tr>` with one `<td style="width:20%;vertical-align:top;padding:0 6px;">` per column. Table columns come from the `<td>` structure itself, so they survive even if every CSS property is stripped.

### 2.2 Gradient frame without border-image

To get a bright-teal-top-left to dim-bottom-right gradient frame (matching the countdown card) on sanitized inline HTML: wrap the element in a `<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">` (the frame) and give the inner element a body background. The 2px padding reveals the frame gradient as a border. Body colors: teal corner wedge `#094043`, dark body `#041d1c`.

**Two treatments by size (the cohesive system the home pages use):**
- **Small boxes (nav buttons, inner cards, framed images):** gradient-frame wrapper + an **opaque** body (`#094043` wedge / `#041d1c`) + 28px triangle. Opaque so the frame does not bleed.
- **Large section cards:** do NOT use the gradient-frame wrapper. Use the home-page welcome-card recipe: `background:linear-gradient(180deg,rgba(0,116,116,0.10) 0%,rgba(0,116,116,0.03) 100%);border:1px solid rgba(0,184,184,0.22);border-left:6px solid #00b8b8;`. The very faint translucent teal lets the panther watermark read through; the solid 1px border + 6px teal left accent are Canvas-safe. No wrapper, no triangle on large sections. (Forcing the small-box wrapper onto a large section and faking translucency by lowering the body opacity fights the frame and looks murky, do not do it.)

### 2.3 Clickable buttons in Canvas

An `<a>` that wraps block `<div>` children loses its click area in Canvas (when the anchor's display is stripped, an inline anchor around block content collapses to a zero-height sliver). Build button links as a single `<a display:block>` wrapping only **inline** content (`<img>`, `<span>`, `<br>`). Put any block wrapper (like the gradient frame `<div>`) OUTSIDE the anchor, not inside it.

### 2.4 LOCKED course-home nav button (verbatim)

This is the approved nav button, matches the countdown card, Canvas-safe, clickable. One `<td>` per button; icon + English title + Spanish subtitle live INSIDE the framed box. Do not revert to border-image, grid, or stacked-outside labels.

```html
<td style="width:20%;vertical-align:top;padding:0 6px;">
  <div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">
    <a href="COURSE_URL" style="display:block;text-decoration:none;color:inherit;background:linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%);padding:18px 10px 14px;text-align:center;">
      <img src="ICON_URL" alt="Course Overview" style="display:block;width:50%;max-width:74px;height:auto;margin:0 auto 12px;" />
      <span style="font-size:11pt;letter-spacing:0.05em;text-transform:uppercase;color:#ffffff;line-height:1.25;"><strong>Course Overview</strong></span><br />
      <span style="font-size:9pt;color:#5eead4;font-style:italic;line-height:1.3;">Resumen del Curso</span>
    </a>
  </div>
</td>
```

The countdown card (`assets/embeds/schoolday-card.html`) uses the same opaque body (`#094043` wedge / `#041d1c` at a fixed `28px` stop) and a matching gradient frame, so the two read as one system. Keep the triangle stop in **pixels** (28px), never a percentage: a percentage scales with box size, so the wedge would not match between the wide countdown and the squarer buttons.

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

## 3.5 Combined Chip Header + Accent Cohesion (LOCKED 2026-09-11)

Reference implementation: the shared `tools/silva_framework.py` module, imported by every module builder as `from silva_framework import *` (one source of truth for the chrome); `tools/build-image-series.py` is the canonical template and `tools/build-leading-lines.py` a full bilingual example. **The chip rollout is COMPLETE (2026-09-11): every live module in all three courses (Digital Arts 1A, Photography 1A, Photography 2A) is built on `silva_framework`.** This section SUPERSEDES the separate eyebrow-chip + heading + hairline pattern (§6) for module pages. Where a module needs a layout the framework has no helper for, define a small module-local helper in that builder (e.g. `examples()`, `subcols()`, `pills()`, `teal_callout()`), keeping it cohesive with the section color.

**Combined chip header.** Every section title is ONE dark rectangle ("chip") holding the section icon on the LEFT and one big color-coded title, with a short accent rule directly under it. No separate eyebrow above, no repeated heading below.
```html
<div style="display:inline-flex;align-items:center;gap:12px;background:rgba(0,0,0,0.40);border-left:5px solid <ACCENT>;padding:9px 18px 9px 12px;margin-bottom:12px;max-width:100%;box-sizing:border-box;">
  <img src="<ICON>" alt="" style="width:44px;height:44px;display:block;flex:0 0 auto;" />
  <span style="font-family:Arial,sans-serif;font-size:17pt;color:<LIGHT>;letter-spacing:0.01em;line-height:1.15;"><strong><TITLE></strong></span></div>
<div style="height:2px;background:<ACCENT>;width:60px;margin-bottom:18px;"></div>
```
Helper: `section_header(icon,title,accent,light)`. Chip icons are 44px (10% up from the original 40px, LOCKED 2026-09-11).

**Four-color accent system (LOCKED 2026-09-10).** Each section purpose has ONE color so students read the page at a glance:

| Purpose | Accent / light | Icon |
|---------|----------------|------|
| Content | `#00b8b8` / `#80e0e0` | `step-check-teal-v2.png` (or the step's type icon) |
| Downloads | `#FF6B1A` / `#ffb27c` | `downloads-v1.png` |
| Resources | `#8b5cf6` / `#c4b5fd` | `resources-v1.png` |
| Deliverables | `#f5b301` / `#ffd166` | `deliverables-v4.png` |

Section container box: `background:linear-gradient(180deg,<accent 0.10-0.12> 0%,<accent 0.03> 100%);border:1px solid <accent 0.22-0.35>;border-left:6px solid <ACCENT>;padding:30px;overflow:hidden;margin-bottom:24px;`.

**Each section is internally cohesive (LOCKED 2026-09-11).** Inside a section EVERY inline accent inherits that section's color: bullets, numbered step badges, image/thumbnail frames, captions, inline links, sub-panel borders, secondary buttons. No mixing colors inside one card. The only exceptions: a photographic image itself (only its frame/overlay/caption recolor), and the distinct semantic callout BOXES (the orange `note` alert, and the Downloads/Resources/Deliverables boxes) which read as their own boxed element, not an accent bleeding into another section.

**Content icon = step-check.** Content cards use the light-teal step-check badge (`step-check-teal-v2.png`) so working through a step reads like checking a box. Master SVG in `assets/Icons/assignment/_src/step-check.svg`; it must render with a TRANSPARENT background (the check is knocked out of a filled teal disc, everything else transparent).

**Right-hand images and thumbnails: top-align with the title, drop below when narrow (LOCKED 2026-09-11).** A card with an image/thumbnail is a wrapping flex row: `display:flex;flex-wrap:wrap;align-items:flex-start;gap:16px 26px;`, with a text column (`flex:1 1 320px;min-width:0;` holding the chip + body) and a thumbnail column (`flex:0 1 360px;`). `align-items:flex-start` top-aligns the thumbnail with the title chip; `flex-wrap` drops the thumbnail BELOW the text when the page gets too narrow (NEVER above the title, and never leaving the chip stranded beside it). Do NOT use a CSS `float` for this: module pages are pasted into Canvas, which strips `@media` queries, and a plain float can push a long title below the image. Canvas DOES preserve `display:flex`, so the flex row survives paste. All thumbnails use the same `flex:0 1 360px`, so sibling cards match in size. In the builder: `_lay()` builds the flex row; `float_right()` (teal-framed content photo) self-marks with `<!--FLOAT-->` and the card hoists it into the thumbnail column; `purple_thumb()` (purple-framed clickable Resources thumbnail: slide deck, install video) passes through the card's `floatimg` argument to the same column.

**Two thumbnail sizes (LOCKED 2026-09-11).** A generated CONTENT photo (a `float_right` Chris made and wants showcased) is shown at about HALF the card width: hoisted content photos get `flex:1 1 44%` with the text column also `flex:1 1 44%`. A resource THUMBNAIL (slide-deck cover, install video) stays COMPACT: `flex:0 1 360px` with the text column `flex:1 1 320px`. Both still top-align and drop below when narrow. `float_right(src, alt, cap="")`: the caption is optional, and a caption-less content photo emits no caption line (no empty div).

**Overview first card = "The Module Overview" type chip** (`type_card("overview",...)`) with the light-teal overview icon, then the card's own heading. Chris works in MODULES and STEPS, never "assignments".

**Header module-type icon (LOCKED 2026-09-11).** A photo-walk module or an own-device module carries a WHITE module-type icon in the banner, to the RIGHT of the title, immediately left of the language toggle (it does NOT crown the title). Photo-walk modules use `photo-walk-white-v1.png` (`HICON_PHOTO_WALK`); own-device modules use `your-device-white-v1.png` (`HICON_YOUR_DEVICE`). It appears on every page of that module. Other module types carry no header icon for now. The builder sets it with a module-local `banner()` wrapper: `import silva_framework as _sf` then `def banner(...): return _sf.banner(..., HICON_PHOTO_WALK)`.

**Deliverables box** = the gold chip header (icon on the LEFT), at the TOP of each step, opening with a forecast line, then the turn-in bullets. Helper `deliverables_box(es, items)`. Forecast:
- EN: &#x201C;Work through every task on this page to finish this step the right way. Each step in this module gets its own grade, so turn in the work below:&#x201D;
- ES: &#x201C;Trabaja cada tarea de esta p&aacute;gina para terminar bien este paso. Cada paso de este m&oacute;dulo tiene su propia calificaci&oacute;n, as&iacute; que entrega lo siguiente:&#x201D;

**Resources chip calls itself out:** the purple chip title reads &#x201C;Module Resource: &lt;title&gt;&#x201D; / &#x201C;Recurso del M&oacute;dulo: &lt;title&gt;&#x201D; so students know it is reference/how-to. Helper `resources_card(heading, inner, es)`. External reference links (a &#x201C;read this&#x201D; article, a video) are purple resources too: batch several under ONE Resources card per step with `reslink()`.

**Key Words vocab = purple collapsible accordion (LOCKED 2026-09-11).** The 6-term vocab is a purple Resources card: `resources_card("Key Words"/"Palabras Clave", vocab_grid(quiz_label, quiz_body, terms))`. `vocab_grid()` renders an always-on purple quiz note, then each term as a native `<details>` the student taps to reveal its definition, TWO columns (flex-wrap) on wide screens and one column when narrow. A collapsible CONTENT list (e.g. Composition Concepts' 20 concepts) uses the SAME `<details>` structure but themed TEAL (content), via a small module-local helper. NOTE: Canvas's paste sanitizer strips `<details>`, so accordions only work on LINKED module pages (View Page), not pasted HTML; every current module is delivered as a linked page.

**Slide decks are a click-to-open PDF cover thumbnail (LOCKED 2026-09-11).** In its purple Resources card the deck is a single cover thumbnail (`slide_deck_thumb()` &rarr; `purple_thumb()`) that links to the hosted PDF and opens it in a NEW TAB, where the browser's native PDF viewer handles full-screen reading and download. No inline scroll window, no inline PDF button. Every deck is a real PDF. The SAME PDF also downloads from the Overview Downloads section, labeled by the DECK'S TITLE then &#x201C;(Slide Deck)&#x201D;, e.g. &#x201C;Importing Photos (Slide Deck)&#x201D; / &#x201C;Importando Fotos (Presentaci&oacute;n)&#x201D;. (A few older modules still show an embedded multi-image scroll panel; they migrate to the PDF-thumbnail pattern as Chris supplies each cover image + exported PDF.)

**Teacher-facing icon library** = Build Resources &rarr; Graphics &rarr; Logos &rarr; &#x201C;Module Icons&#x201D; (renamed from &#x201C;Assignment Icons&#x201D;), holding every color variant including the teal content family on dark tiles. The five accent hexes are copy-pastable in Build Resources &rarr; Color Palette: each hex button's lettering IS its color on a contrasting chip, and a click copies the BARE number (no `#`).

**Step identity (RESOLVED 2026-09-11).** A step opens with its gold Deliverables box at the top, then plain content chips; the banner names the step and the white header module-type icon (above) carries the module identity. The old right-side ID-eye chip (the `<!--IDEYE-->` icon + label) is RETIRED and removed from every module.

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

**Overview opening sequence (LOCKED):** every overview page opens with a single **Assignment / Overview section card** whose body contains, in order: the eyebrow, the heading, ONE short intro paragraph (the quick "what this is" verbiage), and then the 21:9 hero image **framed inside that same card body**. The hero is part of the Assignment/Overview section, NOT a standalone image and NOT its own section. After that card come the remaining sections (example/sample images, history, vocab, etc.).

Rules:
- The 21:9 hero is the **FIRST image on the page** and lives **inside the Assignment/Overview card body**, directly under the intro paragraph (keep its teal gradient frame).
- It is never a standalone image block floating between sections.
- No example, sample, or gallery image ever appears above the hero.
- Build order example (Pictograms): `s1` (eyebrow + heading + one paragraph + hero, all in one `large()` card) then `ex` (examples) then the rest.

**Downloads live on the Overview; purple Resources live in the step where they are needed (UPDATED 2026-09-11).** These are two different things with two different placement rules:

- **DOWNLOADS (orange, files the student keeps: reflection doc, template/preset ZIPs, slide-deck PDFs)** are consolidated in the Overview's orange Downloads block (the 2nd card, right after the intro/header), ending with the project-folder note. Step pages never repeat a download link; they point back to THIS module's Overview (the first page of this module), so students never confuse it with the course Overview. One predictable place for files-to-keep builds an intuitive Canvas routine. **The download buttons share ONE row (LOCKED 2026-09-11):** wrap them in `display:flex;flex-wrap:wrap;gap:10px;` (each `dl_link(..., row=True)` has `margin:0`), so they sit side by side and wrap to the next line only when the page is too narrow, never permanently stacked. Saves vertical space.
- **Purple RESOURCES (how-to / reference: slide decks, install videos, step-by-step guides)** go in the STEP where they are needed, right next to the task they support. Example (Image Series): the Lightroom import slide deck AND the preset-install video both live in Step 1, where students import their photos and build the contact sheet, in that order. **Resource placement is a VARIABLE, not a fixed location:** put each resource on the page or step where it is used. Do NOT force resources onto the Overview.

**Reflection point-back wording (LOCKED 2026-09-10, use VERBATIM on every reflection step):**
- EN: &#x201C;The reflection document is on this module&rsquo;s Overview page, the first page of this module. If you have not downloaded it yet, go back and get it. Before you open it, move it from your Downloads folder into your project folder.&#x201D;
- ES: &#x201C;El documento de reflexi&oacute;n est&aacute; en la p&aacute;gina de Resumen de este m&oacute;dulo, la primera p&aacute;gina de este m&oacute;dulo. Si a&uacute;n no lo has descargado, regresa y cons&iacute;guelo. Antes de abrirlo, mu&eacute;velo de tu carpeta de Descargas a tu carpeta del proyecto.&#x201D;

It goes in the reflection step&rsquo;s orange note (`note_orange`). When a step then lists how to complete the reflection, the &#x201C;Open it&#x201D; line reads &#x201C;open the reflection Word document (.docx) from your project folder&#x201D; (it lives in the project folder now, not Downloads). This supersedes the older &#x201C;marked M at the top&#x201D; phrasing for reflections.

**Downloadable files must be zipped (LOCKED):** never link a raw non-image file (`.lrtemplate`, `.docx` presets, etc.) directly from `raw.githubusercontent.com`. Cross-origin, the browser ignores the `download` attribute and GitHub serves the file as `text/plain`, so clicking just shows the file as a wall of text instead of downloading. Put the file(s) in a `.zip` and link that (browsers always download `.zip`). Bundle related files into ONE zip and add a short note that the download contains all of them.

**Download sections are an orange card with the folder icon inside (LOCKED 2026-09-03):** a file download lives in its own ORANGE-styled card (`download_card`: `border-left:6px solid #FF6B1A`, orange eyebrow + rule, faint orange tint), NOT a teal card. Inside it, the dedicated `downloads` folder icon (`downloads-v1.png`) sits next to an official-orange `#FF6B1A` button (white bold text, `border-top:2px solid #ffb27c`) in a `dl_row`: 42px icon + button, `align-items:center`, button `margin:0` so the two center exactly. The card&#x2019;s HEADING names exactly what is downloaded there (&#x201C;Download Reflection Document&#x201D;, not a generic &#x201C;Resources&#x201D;); name every download section for the file the student needs. External read/reference links (an article, a webpage, `download=False`) keep the light cream style, so orange always means &#x201C;download a file.&#x201D; **The downloads folder icon lives ONLY in the download section, never at the top of the Overview** (the top-right carries the module&#x2019;s type icon). Applied across every module (2026-09-03 sweep): builder modules use the full orange `download_card`; the four hand-built overviews (Self-Portrait, Composition Concepts, Composition Photo Walk, OCF) carry the orange button + folder icon `dl_row` at minimum (convert them to builders to get the full orange card).

**Every Downloads section ends with a project-folder note (LOCKED 2026-09-10):** the last thing in the orange Downloads box is a `folder_note(es)` line (bold orange `#ffb27c` lead-in "Stay organized:" / "Mantente organizado:"): tell students to make a new folder named after this module and, as each file finishes downloading, move it out of Downloads into `OneDrive &rarr; {AREA} &rarr; that project folder`. `{AREA}` is course-aware (LOCKED 2026-09-11): **Photography Folder** for Photography 1A/2A, **Digital Arts Folder** for Digital Arts 1A (used verbatim, unchanged in ES). EN in `#top`, ES in `#espanol`. Present on every module Overview (all 7 builders via a `folder_note` helper; the 5 hand-built overviews inline).

**Contact-sheet templates carry an install pointer (LOCKED 2026-09-10):** wherever the contact-sheet templates ZIP is offered for download, put an `install_note` under that row: "New to these? Watch the install video (Vimeo `1164128764`), then drop them into Lightroom Classic &rarr; Print module. You only install them once." (EN + ES). Contact sheets themselves are always turned in as high-resolution JPGs, never PDF (the preset prints to file with JPG preselected).

**Resources section is PURPLE (LOCKED 2026-09-10).** The module accent system is: **teal** = lesson content, **orange** = Downloads (files to keep), **purple `#8b5cf6`** = Resources (in-depth how-to / reference: slide-deck walkthroughs, install videos, step-by-step guides), **gold `#f5b301`** = Deliverables (turn-in). A Resource is a `resources_card`: purple version of the teal `card()` (`border-left:6px solid #8b5cf6`, eyebrow chip `border-left:3px solid #8b5cf6;color:#c4b5fd`, purple heading rule) with the purple resources gear icon (`assets/Icons/assignment/resources-v1.png`, 44px) at the top-right of the title row. Use it on an Overview when the module has reference material, and on a step whose in-depth instruction set (a scrollable how-to, an embedded slide deck) is the deep guide, so students see "this is the how-to." Keep it distinct from Downloads (a file you keep) and Deliverables (turn-in). Do NOT make the FIRST card of a step a `resources_card`: the assignment-type ID icon attaches to the first teal card, so keep a teal card first, then the Resource.

**Import / slide-deck scrollable is a 16:11 window (LOCKED 2026-09-10):** when a step embeds a deck of slide JPGs (16:9 slides), stack them FLUSH inside a `.silva-scroll` div sized `aspect-ratio:16/11;overflow-y:auto;box-sizing:border-box;` with NO `max-height` clamp and NO padding, and slides at `margin:0` (a thin `border-bottom` as the only separator). The 16:11 window shows one full 16:9 slide plus a sliver of the next peeking in, which invites the student to scroll. Keep the "&#8595; Scroll..." hint above it and the orange PDF download button. Do not use `max-height:*vh` for slide decks (it clamps the ratio and breaks the peek). Long TEXT step-lists are different: those use a fixed `max-height` scrollbox, not this aspect-ratio window.

**Image-selection wording (LOCKED 2026-09-10):** chosen/culled images are **selections**, **image selections**, **selected images**, or **culled images**, NEVER the noun "picks" ("your edited picks" &rarr; "your edited selections"). Prefer the verb **select** or **cull** over "pick" when choosing images ("select your best 6"). This applies only to culling/selecting images; "pick" is fine for a tool, a font, a camera setting/mode, or a concept. EN + ES.

**Vocabulary / Key Words is a PURPLE Resource (LOCKED 2026-09-11).** Vocab is technically a reference resource, so the Key Words section is a `resources_card` titled &#x201C;Module Resource: Key Words&#x201D; / &#x201C;Recurso del M&oacute;dulo: Palabras Clave&#x201D; (purple chip + resources gear icon), and it stays on the Overview. Every accent inside it is purple (cohesion). **The terms are a COLLAPSIBLE accordion in TWO columns (LOCKED 2026-09-11):** each term is a native `<details>` (purple gradient frame over a purple-dark body wedge `#241d3a` / `#140f24`) whose `<summary>` shows a number + the term; tapping it reveals the definition. The terms sit in a `display:flex;flex-wrap:wrap;gap:10px;align-items:flex-start;` row with each `<details>` at `flex:1 1 45%;min-width:260px;`, so there are TWO columns on iPad/desktop and they collapse to one column only when the page is too narrow. No JS (native `<details>`), so it works on the linked page view. NOTE: Canvas's paste sanitizer strips `<details>` and its contents, so this interactivity only survives when the page is LINKED (View Page), not pasted into Canvas: use it on modules delivered as links. Above the accordion sits the PURPLE quiz-disclaimer note (`rgba(139,92,246,0.10)` bg, `#8b5cf6` left border, eyebrow `#c4b5fd` reading &#x201C;ON THE QUIZ&#x201D; / &#x201C;EN EL EXAMEN&#x201D;) and a one-line &#x201C;Tap a word to open its meaning.&#x201D; / &#x201C;Toca una palabra para abrir su significado.&#x201D; hint. Definitions stay concise but clear, EN + ES at 5th grade. (Reference: Composition Concepts.)

## 8. Horizontal Scroll Rows

Term tiles and stat tiles sit in a horizontal scroll row:
```html
<div style="display:grid;grid-auto-flow:column;grid-auto-columns:minmax(260px,1fr);overflow-x:auto;gap:14px;padding-bottom:8px;-webkit-overflow-scrolling:touch;">
  ...tiles...
</div>
<div class="scroll-hint" style="text-align:center;font-size:8pt;color:rgba(0,184,184,0.55);letter-spacing:0.22em;text-transform:uppercase;margin-top:14px;font-family:Arial,sans-serif;"><strong>« drag or swipe for more »</strong></div>
```

## 8.5 Image Placeholders (when no image is supplied)

When a page needs an image the user has not provided yet, do NOT leave a
gap or a broken `<img>`. Drop an on-brand placeholder box in its place:
a gradient-frame card with a dark fill, an `IMAGE PLACEHOLDER` eyebrow
label (in the page accent), and an italic, muted description of what the
image should be, written like an AI image prompt (who is in it, what
they are doing, the setting). Float it right or run it full width to
match where the real image will go. Swap the real `<img>` in (with the
standard 2px gradient frame) once the user supplies it.

```html
<div style="background:linear-gradient(135deg,rgba(R,G,B,0.12) 0%,rgba(0,0,0,0.45) 100%);border:2px solid transparent;border-image:linear-gradient(135deg,<SOLID> 0%,<DIM> 100%) 1;padding:26px 22px;text-align:center;float:right;width:42%;min-width:240px;margin:0 0 18px 26px;">
  <div style="font-size:10pt;letter-spacing:0.22em;text-transform:uppercase;color:<EYEBROW>;margin-bottom:10px;"><strong>Image Placeholder</strong></div>
  <div style="font-size:11.5pt;line-height:1.6;color:rgba(255,255,255,0.66);font-style:italic;">FLOAT-RIGHT IMAGE: who, doing what, where.</div>
</div>
```

## 9. Build Checklist

- Zero rounded corners anywhere.
- Every card: translucent tint background, gradient border-image frame, solid top-stripe child. Watermark visible through cards.
- Every button: gray base, fixed size, section-colored 2px top bar.
- Bilingual EN block then ES mirror, unless English-only was requested.
- All asset URLs host from `www.creativesilva.com`, spaces as `%20`.
- No em dashes. 5th grade reading level. Active voice.
- Div opens equal div closes.
