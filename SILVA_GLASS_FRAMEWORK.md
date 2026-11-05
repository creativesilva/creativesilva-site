# SILVA GLASS FRAMEWORK

The locked design system for Chris Silva's **operational teacher tools**: the iOS "liquid glass, galaxy glow" look. **AI Studio** (`build-resources.html`, formerly Prompt Studio / Build Resources; renamed 2026-11-04) is the reference implementation, applied end to end across BOTH its tabs (Prompt Builder AND Resources) plus the Reference Library: one page-wide galaxy backdrop, one glass component set, one teal rollover. Roll this out slowly to the teacher portal, Equipment Manager, and other teacher tools.

**Scope.** This is for TEACHER TOOLS only. **Canvas student pages stay angular** (see `SILVA_ANGULAR_FRAMEWORK.md`); do not glass-ify them. The red/white portfolio and lightwriterz.org are untouched.

**Status: LOCKED 2026-11-04.** Approved on AI Studio (v1.7). Maintain it without being reminded. When a decision changes, update this file in the same session.

---

## 0. The feel, in one line

Near-black teal space, lit from within. Soft frosted glass panels with a bright top edge, floating over a slow galaxy mesh. Rounded, calm, cohesive. Nothing square, nothing flat, nothing that reads "AI slop."

Three references it synthesizes: Apple iOS 26 Liquid Glass (material + rounded nav), Canva (draggable multi-detent sheets, tasteful gradients), the Alexa app (card-based, one obvious action).

---

## 1. Tokens (the single source of truth)

Copy this `:root` block into any teacher tool to adopt the system. Every value below is a LAW: use the token, never a one-off literal.

```css
:root{
  /* INK (page base) */
  --g-ink:#06100f; --g-ink-2:#041413;
  /* TEAL BRAND (the only UI hue) */
  --g-teal:#00b8b8; --g-teal-lt:#5ff0f0; --g-teal-deep:#007474;
  /* GALAXY ACCENTS (backdrop mesh + glow ONLY, never a UI fill) */
  --g-cyan:#00eee0; --g-blue:#3886f8; --g-violet:#965cf2; --g-pink:#e86ece;
  /* TEXT */
  --g-text:#eafeff; --g-muted:rgba(214,247,247,.82); --g-faint:rgba(206,244,244,.6);
  /* EDGES / LINES */
  --g-edge:rgba(112,246,246,.30); --g-edge-soft:rgba(112,246,246,.18);
  /* STATE */
  --g-warn:#f5b301; --g-ok:#3fa863; --g-danger:#ff7a7a;
  /* RADIUS (4 steps, nothing else) */
  --g-r-pill:999px;   /* pills, chips, circular buttons */
  --g-r-lg:20px;      /* cards, sheets, big panels */
  --g-r-md:14px;      /* rows, accordions, secondary panels */
  --g-r-sm:10px;      /* inputs, dropdowns, thumbnails, tool buttons */
  /* CONTROL HEIGHTS (2 steps, nothing else) */
  --g-ctrl-h:48px;    /* standard glass button / pill / input */
  --g-ctrl-h-sm:42px; /* compact row button / dense pill */
  /* GLASS MATERIAL (2 blurs, nothing in between) */
  --g-blur:blur(20px) saturate(150%);       /* panels, pills, controls */
  --g-blur-heavy:blur(28px) saturate(150%); /* the sheet, dock, overlays */
  /* FILLS */
  --g-glass:linear-gradient(145deg, rgba(0,184,184,.14), rgba(132,80,226,.07) 58%, rgba(6,16,16,.26));  /* panel */
  --g-glass-quiet:linear-gradient(145deg, rgba(0,184,184,.08), rgba(132,80,226,.04) 60%, rgba(6,16,16,.2)); /* input / calm surface */
  --g-primary:linear-gradient(135deg, var(--g-teal-lt), var(--g-teal));  /* the one bright action */
  /* SPECULAR + SHADOW (depth) */
  --g-spec:inset 0 1px 0 rgba(185,255,255,.18);
  --g-spec-strong:inset 0 2px 0 rgba(224,255,255,.6), inset 1px 0 0 rgba(185,255,255,.2), inset -1px 0 0 rgba(0,0,0,.26), inset 0 -1px 0 rgba(0,0,0,.4);
  --g-shadow-sm:0 6px 16px rgba(0,0,0,.24);
  --g-shadow:0 12px 30px rgba(0,0,0,.34);
  --g-shadow-lg:0 18px 54px rgba(0,0,0,.5);
  --g-glow:0 0 18px 2px rgba(95,240,240,.4), 0 0 30px 6px rgba(132,80,226,.22);  /* ready / active pulse */
  /* SPACING (6 steps) */
  --g-s1:4px; --g-s2:8px; --g-s3:12px; --g-s4:16px; --g-s5:22px; --g-s6:32px;
  /* TYPE */
  --g-font:'Oswald',system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif; /* heads, labels, buttons */
  --g-body:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; /* paragraphs, inputs */
}
```

> AI Studio's existing `--pbg-*` / `--pvb-*` tokens are this same system under older names; new work and the rollout use the `--g-*` names above.

---

## 2. Material laws (what makes a surface "glass")

Every panel, pill, card, control, and chip is built from the same four layers. Never skip the edge or the specular, that is what sells the glass.

1. **Fill:** `background: var(--g-glass)` (or `--g-glass-quiet` for calm/input surfaces, `--g-primary` for the one bright action).
2. **Blur:** `backdrop-filter: var(--g-blur)` (+ `-webkit-` twin). Heavy blur ONLY for the sheet/dock/overlays.
3. **Edge:** `border: 1px solid var(--g-edge)` (`--g-edge-soft` for quiet surfaces).
4. **Specular + shadow:** `box-shadow: var(--g-shadow-sm), var(--g-spec);` The inset top highlight is mandatory; depth shadow scales with elevation (`-sm` controls, base panels, `-lg` the sheet).

**Hierarchy, not uniformity.** Vary elevation so the eye reads depth: backdrop (mesh) < panel < card < pill < the one bright primary. Don't make every surface the same brightness.

**Galaxy backdrop.** A fixed `.g-bg` with a `.g-mesh` (8 soft radial blobs in teal/cyan/blue/violet/pink, `mix-blend-mode:screen`, slow drift) and a `.g-glow` (tiny star points). Accents live ONLY here, never in a button or panel fill. Paint it only while the tool is on screen.

**Fallbacks (required).** `@media (prefers-reduced-transparency:reduce)` drop blur, use a solid `--g-ink` tint. `@media (prefers-reduced-motion:reduce)` freeze the drift/glow. Reduced transparency must stay legible.

---

## 3. Radius law

Four radii, nothing else. **Zero `border-radius:0` anywhere.**

| Token | Use |
|---|---|
| `--g-r-pill` 999px | pills, chips, segmented buttons, circular icon buttons, badges |
| `--g-r-lg` 20px | the card, the sheet, top-level panels |
| `--g-r-md` 14px | list rows, accordions, nested panels, the build-order rows |
| `--g-r-sm` 10px | text inputs, dropdowns, thumbnails, small tool buttons, menu items |

---

## 4. Color law

- **Teal is the only UI hue.** `--g-teal` / `--g-teal-lt` / `--g-teal-deep` for actions, accents, active states, edges.
- **Galaxy accents** (cyan/blue/violet/pink) appear ONLY in the backdrop mesh/glow. Never a button, panel, or text color.
- **Text:** `--g-text` for primary, `--g-muted` for secondary, `--g-faint` for tertiary. Bright text on dark glass; keep contrast legible.
- **State:** amber `--g-warn` for cautions, green `--g-ok` for success, soft red `--g-danger` for errors. These are the ONLY non-teal UI colors, and only for state.
- On a bright `--g-primary` fill, text/icons are ink `#04110f`, not white.

---

## 5. Type + tracking

Oswald for anything structural (heads, labels, buttons, eyebrows, chips). System body font for paragraphs and input text.

| Role | Size | Weight | Tracking | Case |
|---|---|---|---|---|
| hero (page/card title) | 1.32rem | 800 | .01em | none |
| title (section/panel) | 1.02rem | 700 | .02em | none |
| label (control, eyebrow-strong) | .84rem | 700 | .08em | UPPER |
| body | .8rem | 400 to 600 | .02em | none |
| micro (meta, chip) | .72rem | 700 | .06em | UPPER |
| eyebrow (kicker) | .6rem | 700 | .2em | UPPER |

Tracking tokens, pick one: tight `.02em`, normal `.04em`, wide `.08em`, eyebrow `.2em`. No in-between values.

---

## 6. Components

Build everything from these. One spec each, no one-offs.

- **Control heights (LOCKED 2026-11-04).** Every glass button / pill / input is ONE of two heights: `--g-ctrl-h` (48px) standard, `--g-ctrl-h-sm` (42px) compact rows. No one-off heights anywhere, so controls line up and read as one system.
- **Rollover (LOCKED 2026-11-04, the universal glass action).** A glass control at rest is `--g-glass`; on hover/active its face fills `--g-primary` with ink (`#04110f`) text, `transition .16s to .18s ease`. Teal is never a permanent per-control state (that reads harsh); it is the rollover. `:active` adds `filter:brightness(.94)`.
- **Primary button / pill.** `--g-primary` fill, ink text, `--g-r-pill`, `--g-ctrl-h`, `var(--g-shadow-sm), var(--g-spec)`. Hover `filter:brightness(1.07)`. The ONE bright-at-rest thing in a view (a submit/confirm), used sparingly.
- **Secondary / glass button.** `--g-glass`, `--g-text`, `--g-blur`, `--g-edge`, `--g-r-pill`, `--g-ctrl-h`, `var(--g-spec)`. Uses the universal rollover above.
- **Icon button.** Circular (`--g-r-pill`, equal w/h, 44px min on touch) OR a pill half, `--g-ctrl-h`/`-sm`. Glass at rest; the teal fill arrives on the rollover, not as a permanent state. Icon only where the meaning is obvious to the owner.
- **Split pill (LOCKED 2026-11-04).** ONE glass capsule (`--g-glass`, `--g-blur`, `--g-edge`, `--g-r-pill`, `--g-ctrl-h`/`-sm`) split by a hairline `--g-edge-soft` divider into two equal icon halves: download left, copy right. BOTH halves are glass at rest, no permanently-bright half and no harsh dark→bright break; the teal fills only the HOVERED half (the universal rollover). Success flashes `--g-primary` + a 2px inset ring (`.ok`). The SAME pill is used in the composed-prompt footer and in every build-order row, identical.
- **Segmented control / tabs.** A pill track; the active segment is a brighter inset glass pill (`--g-glass-quiet`, `--g-r-md`, teal text + `--g-spec`), NEVER a square box with an underline. Hover is a faint teal wash. The count badge is a small teal `--g-r-pill` chip.
- **Page header / top bar.** The whole top chrome is glass too (it is the first thing seen; a flat or angular header breaks the theme). The sticky bar is translucent + heavy blur so the galaxy shows through (no bright accent border). The title sits in a rounded frosted glass panel (`--g-r-lg`, `--g-glass-quiet`), NO heavy left-bar accent. Nav destinations are glass buttons (`--g-r-md`, universal teal rollover); the one primary door may be a touch teal-tinted. Scope header overrides to the tool's own page so a shared site header elsewhere (e.g. the angular catalog) is untouched. Keep only the doors the owner uses: AI Studio carries exactly two icon buttons (Catalog, and the real ChatGPT mark drawn in `currentColor` so it takes the glass style).
- **Card / panel.** `--g-glass`, `--g-r-lg`, `--g-blur`, `--g-edge`, `var(--g-shadow), var(--g-spec-strong)`. Header row stays put; only the body scrolls.
- **Row (list item).** `--g-r-md`, `--g-glass` (quiet), `--g-blur`, left controls centered to the row, variable-width content in a reserved width so columns never zig-zag (the no-wave law).
- **Input / dropdown.** `--g-r-sm`, `--g-glass-quiet`, a light `--g-blur`, `--g-edge-soft`; focus lifts the edge to `--g-edge`/teal. NEVER square, never a flat black box. Dropdown menus are glass panels with `--g-r-md`; options are `--g-r-sm` rows with a teal active state.
- **Accordion.** Glass row header (`--g-r-md`, min-height `--g-ctrl-h`), chevron rotates (45deg to -135deg), body reveals. Ships COLLAPSED; single-open where a group picker. Selected item can ride the collapsed header. Nested sub-accordions share the same glass, one step quieter. ALL accordions in one tool read identical: no heavy per-item left-bar accents, just the clean all-around glass edge.
- **Browse / media card (library + gallery).** A glass frame (`--g-r-md`, `--g-glass-quiet`, `--g-edge-soft`, flex column, uniform height in a `repeat(auto-fill, minmax(~190px, 1fr))` grid). Top = an image tile that fills LARGE (give photos an `aspect-ratio`, not a short fixed height). The image is `object-fit:contain` (never clipped); the empty space is filled by a **frosted blur of the image itself** (`::before`, the image as `cover`, `blur(22px) brightness(.66) scale(1.3)`), NEVER a white or black bar. Logos / line-art are the one exception: keep a LIGHT ground (`#f4f6f6` or a per-item inline bg) so a transparent brand mark stays visible. Then name + an uppercase micro-format label, then the action pill (below). Opens a glass lightbox (rounded frame, circular glass close + nav).
- **Card action pill.** The per-card actions (copy image / copy URL / download) are ONE connected glass icon pill (`--g-r-pill`, `--g-glass`, `--g-blur`, `--g-edge`), split into equal **icon** segments by hairline `--g-edge-soft` dividers; teal `--g-primary` fills only the hovered segment (the split-pill language). Icons, not word chips, and never mixed per-action accent colors. Copy feedback is CLASS-BASED (a teal flash + ring), never a textContent swap, so the icon is never overwritten. In a uniform grid the pill keeps ONE fixed footprint; a card with fewer actions (an `.ai` master has no copy-as-image) splits the same width. Reference-card tools in the builder are the same single connected pill (view / copy / link / download), never separate buttons.
- **Variant card (Nike-style colorway logic, LOCKED 2026-11-04).** When one asset ships in several colors, formats or versions, show ONE card with a selector, never a tile per file (redundant tiles are a self-audit FAIL; catch them without being told). Glossy circular color dots (inset highlight + soft drop; the fill IS the color); the selected dot gets an Apple-style ring with a gap (`outline` + `outline-offset:2px`), never a heavy halo. Mouse hover previews a color, moving off returns to the selection, click selects (touch = tap to select). A PNG | SVG mini segmented toggle appears ONLY when every color ships both formats; text versions (JPG | RAW, Template | Full Set) are segments that share the action pill's exact footprint. A live sub-line names the selection (`COLOR · FORMAT`). Image, download, copy, copy URL and the lightbox all follow the selection; the lightbox ground matches the tile so a white glyph never lands on white. Icon tiles: a deep radial glow ground for bright glyphs, a light ground (`.tone-light`, image `mix-blend-mode:multiply` so a white matte melts away) for dark line icons. Long families sit in collapsed sub-accordions with counts. Reference: AI Studio > Resources > Icons (`.ic-grid`).
- **Palette chip.** A compact `--g-ctrl-h` glass chip: glossy swatch circle (with a soft glow of its own color) | name + uppercase role | monospace hex chip. The whole chip copies the hex (teal flash). Auto-fill grid, one row on wide screens, one column on a phone. Never a giant color block.
- **Ingredient / export row.** A two-line glass grid: a 64px blur-filled thumbnail spanning both lines | line 1 = step number pill + label (one line, ellipsis) | line 2 = remove (left) + the action pill (right). Nothing overlaps at phone width.
- **Chip / badge.** `--g-r-pill`, teal fill or teal-tinted glass, micro type.
- **Warning strip.** Non-blocking. Amber `--g-warn` (caution) or teal (tip) tinted glass row, `--g-r-md`, a round `!` icon. Lives where the user acts (e.g., top of the build order). Never blocks.
- **Modal / pop-out.** Floats above everything incl. the nav (z-index above the sticky nav). Capped to the viewport as a flex column: header pinned, only the body scrolls. One unified window per item with its full action set. (See the locked pop-out rules in `CLAUDE.md`.)

---

## 7. Layout + spacing

- Spacing comes from the 6-step scale (`--g-s1`..`--g-s6`). Gutters on phone are `--g-s4` (16px) minimum, with safe-area insets.
- **Alignment / no-wave (LOCKED).** In any repeated row, items line up in straight vertical columns across rows. Vertically center a row's items; give variable-width content (a name, a date, a count) a reserved fixed width + tabular digits so nothing beside it shifts. Verify by measuring `getBoundingClientRect().left` (0px spread), not by eye.
- **Row lock (LOCKED 2026-11-04, non-negotiable).** A row can never stagger, at any width, in any state. Build it into the structure so it cannot happen, never fix it by nudging:
  - **Field grids (label over control):** each field is a CSS subgrid of the grid's rows (label / control / optional extra), so every field in a row shares ONE label track and ONE control track; labels bottom-align onto their control. Column count comes from the container's own width (container queries), so every column is about 260px or more and labels stay on ONE line. Phones get ONE column (labels never wrap beside a neighbor).
  - **Card grids:** media / name block that reserves its lines (two name lines, clamped) / selectors / action pill pinned to the bottom (`margin-top:auto`), cards stretched to one height. A pill or dot row never sits directly under text that can wrap.
  - **Action rows:** a CSS grid of equal columns (label on its own line above), never a wrapping flex row that orphans one button.
  - **Stacked controls:** controls stacked in one column share both edges (full width).
  - **The gate:** run `tools/align-audit.js` (`silvaAlignAudit()`) on every tab, pane and opened accordion at 390, 1024, 1366, 1440 and 2560 widths. It flags staggered rows, control or pill drift, mismatched label line counts, ragged card heights and wrapping rows that do not form straight columns. Ship only at 0 flags.
- **One navigation at a time, never none.** On a phone exactly ONE nav shows at rest: the in-sheet tab strip at the half detent (the dock is hidden there, Chris's design) and the bottom dock at full height; they crossfade as the sheet moves. Never both at rest, never neither. The strip is equal columns that always fit the phone width (no sideways scroll, no clipped label). iPad and desktop use the in-pane tabs.
- **Scroll edge effect.** Scrolling content dissolves at a pane's edges (a soft mask), never a hard slice under a bar; the top fade appears only once the pane is scrolled.
- **Best use of space.** Design wide-first for a 27" 4K monitor and iPad Pro landscape: a responsive multi-column glass workspace, then reflow to one stacked column at phone width. A single sparse full-width column on a big screen is a FAIL.
- **Glanceable.** Compact by default, detail on interaction (expand, pop-out). Not a wall of text.
- **One edge line.** The header and the content share ONE max-width (1500px, 1760px at 4K) and the same 26px gutters, so their left and right edges sit on one line (measure: 0px drift).
- **Balanced panes (LOCKED 2026-11-04).** In the 2-column workspace both panes stretch to ONE shared height (`align-items:stretch`), capped to the viewport; each scrolls inside. Never a short pane beside a tall one with empty galaxy under it.

---

## 8. Responsive law: three tiers, mobile vertical-first

Optimize explicitly for all three. Detect the tier by capability, not width alone.

- **Mobile iPhone (vertical priority).** `@media (max-width:820px), (pointer:coarse) and (max-width:940px)`. A phone (portrait OR landscape) ALWAYS gets the vertical, single-column, thumb-reachable layout: the draggable multi-detent glass **sheet** + a bottom **dock** for navigation, content stacked top to bottom. The sheet swipes CLEAR to the top: the panel is fixed full-screen (with a scroll guard so a focused field can never scroll it), and as the sheet rises past the header it pushes the header up and away; swiping down brings the header back. Never the 2-column workspace on a phone. 44px minimum tap targets, 16px gutters, safe-area insets. The JS `isPhone()` mirrors this media query (touch + narrow), so behavior and layout agree.
- **iPad Pro / tablet.** `@media (pointer:coarse) and (min-width:821px)`. The 2-column glass workspace (controls + sticky card), tuned for touch: 44px+ tap targets, no hover-only affordances, generous spacing. Handle iPad Pro portrait (1024) and landscape (1366) both; the controls column is `clamp(360px, 33vw, 460px)`.
- **Desktop.** `@media (pointer:fine) and (min-width:821px)`. The 2-column glass workspace with hover states and mouse-scale targets. `@media (min-width:1500px)` widens the controls column. **27" 4K tier** `@media (min-width:1900px)`: max-width 1760px, the card column `clamp(440px, 26vw, 540px)`, 2-up grids become 3-up, icon/media grids auto-fill to ~9 across.

Rule of thumb: **phone = sheet + dock, one column; iPad + desktop = two-column workspace.** When in doubt on a phone, stack vertically.

---

## 9. Motion

- Sheet detents: `transform: translateY` with `cubic-bezier(.32,.72,0,1)`, ~.44s; velocity snap; position-linked dock fade.
- Micro-interactions ~.15s (`filter`, `background`, `box-shadow`). Copy/success: a brief teal `--g-glow` pulse, never a layout shift.
- Backdrop mesh drifts slowly (~34s) and the glow breathes (~6s). Everything respects `prefers-reduced-motion`.

---

## 10. Do / Don't

**Do:** use the tokens; keep teal the only UI hue; give every surface an edge + specular; vary elevation; collapse accordions by default; lead with the content, one bright action per view; measure alignment; test wide AND narrow AND a phone; keep copy plain and short.

**Don't:** `border-radius:0` or square controls; flat black input boxes; glass panels on a flat-black tab (the galaxy goes behind EVERY tab); a galaxy accent as a UI fill; mixed per-action accent colors on a card's buttons (one unified glass chip); ANY left-bar accent (a teal/gold vertical stripe-chip beside a label, or a thick colored left border on a card / row / accordion / the prompt box): the framework has no left-bars, use a clean all-around glass edge; a second bright action competing with the primary; one-off blur/gradient/radius/type values; a sparse single column on a big screen; **how-to / instructional copy on a single-user teacher tool (label it, never explain how to use it, the owner knows); emojis in student-facing copy; em dashes anywhere.**

---

## 11. Rollout checklist (per teacher tool)

1. Drop in the §1 `:root` tokens and the galaxy backdrop (`.pbg-bg` + mesh + glow) as ONE page-wide fixed layer behind EVERY tab/panel, at `z-index:-1` under all content (a child of `<body>`, never trapped inside one panel). The whole tool (every tab, every scroll region) shares the one galaxy glow; glass panels float on it, never on flat black.
2. Replace every surface with a §6 component; delete square/flat styles and every `radius:0`.
3. Collapse radii to the 4 tokens, blur to the 2 tokens, gradients to glass + primary, type to the §5 ramp.
4. Wire the §8 three tiers; confirm phone = sheet/dock vertical, iPad/desktop = 2-col.
5. Audit: glanceable, best-use-of-space, uniform, aligned (measure, 0px wave), cohesive. Run `tools/align-audit.js` on every tab, pane and opened accordion at all five widths and ship only at 0 flags. Fix before shipping.
6. Verify live on desktop, iPad Pro width, and a phone. Then push and confirm live.

Canvas student pages are out of scope. Teacher tools only.
