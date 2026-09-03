# Silva Angular Framework

The locked house style for Pioneer Valley High School Digital Arts and
Photography Canvas pages. Paste this whole file into a fresh agent
session to bring it up to speed on the exact build style.

Master reference page: `curriculum/shared/da-finals-quiz-prep.html`.
Generator: `tools/build-da-finals.py`.

---

## 1. Non-Negotiable Rules

- Never use em dashes. No `—`, no `&mdash;`. Use a colon, comma, or a new sentence.
- Never use the words **shoot, shooting, shot, shots** (or **screenshot**). Hard ban, as absolute as the em-dash ban: in a school these words evoke school shootings. Use capture / take photos / photograph, a session, photo / image / frame, "captured in RAW", "screen capture". Applies to EN and ES, headings, chips, alt text, comments.
- No emojis in student-facing content. They read cheap. Use a text label, a colored chip, or an arrow (`&larr;` `&rarr;`) instead. (`tools/strip-emojis.py` removes them from the `#top` region.)
- Student-facing language at about a 5th grade reading level. Short, direct sentences. Active voice. Use "you" and "your".
- All Canvas assets host from `https://www.creativesilva.com/assets/...` (the ONLY district-whitelisted domain; raw GitHub / jsDelivr render as broken images in the student Canvas iOS app). No Canvas-hosted file URLs, no relative paths, no invented filenames. Spaces in paths become `%20`.
- Bilingual by default: full English block first, then a full Spanish mirror below the `#espanol` anchor. English only when explicitly requested.
- Deliverables, per step (REQUIRED, no exception): each STEP is its own separately-graded Canvas submission with its own deliverable(s), always, unless Chris says otherwise (e.g. Sketchbook step 1 = upload 2 images, step 2 = upload the reflection: two graded assignments). The compact `DELIVERABLES` / `ENTREGABLES` box lives ONLY on the step page that submits that deliverable, placed LOW on that step (near the turn-in, not at the top), stating exactly what THAT step turns in. NEVER put deliverables on the Overview (the Overview describes the project and holds downloads). EN in `#top`, ES in `#espanol`.
- Assignment identification icon (REQUIRED where an icon exists): on every active module page the FIRST card&#x2019;s eyebrow row becomes a `space-between` flex row (`<!--IDEYE-->`). The original eyebrow/title stays on the LEFT unchanged; on the RIGHT sits a short orange description followed by the assignment icon (38px), so the icon lands at the far-right edge. The whole right group wraps below the eyebrow on narrow screens (`flex-wrap:wrap`). EN in `#top`, ES in `#espanol`. No standalone orange bar. Icon family in `assets/Icons/assignment/` with its right-side description: `overview` &rarr; &#x201C;Downloads on This Page&#x201D;; `your-device` (homework on the student&#x2019;s own phone/tablet) &rarr; &#x201C;Your Own Device Required&#x201D;; `camera-kit` (project needing a camera kit checkout) &rarr; &#x201C;Reserve a Camera Kit&#x201D;; `photo-walk` (camera kit during class) &rarr; &#x201C;In-Class Photo Walk&#x201D;; `reflection` &rarr; &#x201C;Written Reflection&#x201D;. Apply with the idempotent `tools/apply-id-icons.py` (add the page to its MAP with the type); it strips any legacy `<!--IDCHIP-->` bar and re-runs safely after regenerating any builder module. Editing, contact-sheet, research/find, worksheet, and design/build steps have no icon yet, leave them off until Chris supplies one.
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

**Resources live on the Overview only (LOCKED):** every downloadable resource (preset, template, reference file, link) goes on the module Overview page. Step pages never repeat a resource download link; they reference it in prose and point back to the Overview with a short italic line ("The X is on the Overview page." / "El X est&aacute; en la p&aacute;gina de Resumen."). One predictable place for resources builds an intuitive Canvas routine.

**Downloadable files must be zipped (LOCKED):** never link a raw non-image file (`.lrtemplate`, `.docx` presets, etc.) directly from `raw.githubusercontent.com`. Cross-origin, the browser ignores the `download` attribute and GitHub serves the file as `text/plain`, so clicking just shows the file as a wall of text instead of downloading. Put the file(s) in a `.zip` and link that (browsers always download `.zip`). Bundle related files into ONE zip and add a short note that the download contains all of them.

**Vocabulary / Key Words card (LOCKED):** the 6-term vocab grid is a `<table>` (3 columns x 2 rows). Give every term box the SAME size for uniformity: put a `min-height` on each opaque body div (e.g. `min-height:132px`) and write the 6 definitions at roughly the same length so no box towers over another. Always include a quiz-disclaimer note at the top of the card (teal note box, eyebrow "ON THE QUIZ" / "EN EL EXAMEN") telling students the words appear on the mid-semester quiz and the end-of-semester quiz before finals. Definitions stay concise (not too detailed) but clear, EN + ES at 5th grade.

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
