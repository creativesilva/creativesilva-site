# Curriculum Cohesion Log

A living audit + upgrade log so every Canvas-facing page shares one branded, polished
aesthetic. As we polish a page, the winning technique gets recorded here and in
`SILVA_ANGULAR_FRAMEWORK.md`, then this log tracks which other pages still need the
upgrade. When starting cohesion work, read this file first, then sweep the "Pending"
list.

Full component recipes live in `SILVA_ANGULAR_FRAMEWORK.md` (§2). This log is the
short spec + the inventory + the changelog.

---

## The universal "square" (buttons, cards, framed images, the countdown)

Every framed box on every page should read as the same object. Locked spec:

- **Gradient frame, not `border-image`.** Wrap the box in
  `<div style="background:linear-gradient(135deg,#00b8b8 0%,rgba(0,184,184,0.08) 100%);padding:2px;">`.
  The 2px padding shows the gradient as a bright-teal-top-left to dim-bottom-right frame.
  `border-image` is stripped by Canvas, so it must never be used for a frame.
- **Two treatments by size.** **Small boxes** (buttons, inner cards, framed images) use the
  gradient-frame wrapper + an **opaque** body
  `linear-gradient(135deg,#094043 0,#094043 28px,#041d1c 28px,#041d1c 100%)` + 28px triangle
  (opaque or the frame bleeds). **Large section cards** do NOT use the wrapper: they use the
  home-page welcome-card recipe, `background:linear-gradient(180deg,rgba(0,116,116,0.10) 0%,rgba(0,116,116,0.03) 100%);border:1px solid rgba(0,184,184,0.22);border-left:6px solid #00b8b8;`
  (faint translucent teal so the panther watermark reads through; solid border + teal left
  accent, Canvas-safe; no wrapper, no triangle).
- **28px triangle eyebrow.** Fixed `28px` corner wedge (never a %), so it is the same size
  on a wide box and a square box.
- **Square corners.** No `border-radius` (stripped anyway).
- **Framed images:** same gradient-frame wrapper, no triangle over the photo. Photos keep
  their aspect; size them with `width:%`.

The school-day countdown card (`assets/embeds/schoolday-card.html`) is the visual
reference; it lives in an iframe (not sanitized) and uses the same colors + 28px triangle.

## Canvas sanitizer: what is stripped (build around it)

STRIPPED: `border-image`, `grid-template-columns` with `repeat()`, `border-radius`,
`box-shadow`, `opacity`, `position:absolute`, `<style>` blocks, `<script>` in the copied
region, `transition`, `animation`, `:hover`, pseudo-elements, `background-image:url(...)`
on most elements, `filter`.

PRESERVED: single (multi-stop) `linear-gradient` `background`, solid `border`/`border-top`,
`padding`, `margin`, `display:block/grid/flex`, `<img>`, `<table>/<tr>/<td>`, inline
`color`/`font-size`/`letter-spacing`/`text-transform`, `<strong>`.

Multi-column layout: use a `<table role="presentation" table-layout:fixed>`, not grid.
Clickable buttons: `<a display:block>` wraps inline content only; block wrappers go outside
the anchor.

---

## Upgrade inventory

Status key: DONE = on the locked square spec. PENDING = still on old technique. N/A = leave.

| Page / area | Frames | Columns | Status | Notes |
|---|---|---|---|---|
| Course home nav buttons (all 8) | wrapper + triangle | table | DONE | 2026-08-21 |
| `assets/embeds/schoolday-card.html` | border-image (iframe OK) + 28px triangle | n/a | DONE | reference element |
| Course home hero images (all 8) | `border-image` | n/a | PENDING | invisible frame in Canvas; convert to wrapper |
| `curriculum/universal/about-mr-silva.html` | wrapper + triangle | grid (explicit tracks, ok) | DONE | 2026-08-21; outer cards `#041d1c`, inner cards lighter `#0f524f`; teacher image shrunk ~25% + framed; added IG + website links |
| Other `curriculum/universal/*` pages | ? | ? | PENDING | audit for border-image / repeat() |
| `curriculum/shared/*` module pages | ? | ? | PENDING | audit; da-finals uses angular already |
| `curriculum/{da1b,da2b,photo1b,photo2b}` course pages | ? | ? | PENDING | audit when built |

**Anti-patterns to grep for when auditing a page:**
`grep -oE "border-image|repeat\(|border-radius|box-shadow|position:absolute"`

---

## Changelog

- **2026-08-21** — Locked the universal square spec (gradient-frame wrapper, opaque
  `#041d1c` body, `#094043` wedge, fixed 28px triangle). Discovered Canvas strips
  `border-image` (frames go invisible) and `grid-template-columns:repeat()` (columns
  collapse; use a table). Applied to all 8 course-home nav buttons. Began upgrading
  `about-mr-silva.html`.
