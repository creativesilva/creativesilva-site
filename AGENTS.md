# AGENTS.md

Agent instructions for any AI coding assistant (Codex, Cursor, Aider, etc.) working on `creativesilva-site`. Filename follows the OpenAI Codex convention.

This is the directive/rule-based companion to `CLAUDE.md`. Read both if you're a multi-tool agent; read only this if you're Codex.

---

## REPO IDENTITY

```
Name:       creativesilva-site
Owner:      creativesilva (GitHub) / Chris Silva (human)
Domain:     www.creativesilva.com (CNAME, GitHub Pages)
Branch:     main (deploys on push, ~60s latency)
Stack:      Static HTML/CSS/JS. No build step. No framework.
Purpose:    Public portfolio + Canvas assignment page host for PVHS CTE classes
```

---

## DO

- [x] Read `CANVAS_BUILD_FRAMEWORK.md` before any Canvas page work
- [x] Use absolute `raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/...` URLs for all image and file references in Canvas pages
- [x] URL-encode spaces as `%20` in asset paths
- [x] Write all student copy at 5th grade reading level (EN and ES)
- [x] Include exactly 6 vocabulary cards in every Canvas page Overview section
- [x] Use HTML entities for accented characters: `&aacute;` `&eacute;` `&ntilde;` etc.
- [x] Use HTML entities for smart quotes: `&#x2018;` `&#x2019;` `&#x201C;` `&#x201D;`
- [x] Add `class="silva-scroll"` to any vertical scroll container
- [x] Pair every scroll container with a visible affordance: text hint + bottom-fade gradient
- [x] Keep cards under 60 words; split if longer
- [x] Add new Canvas pages to `curriculum.html` for every course they belong to
- [x] Use HEREDOC for multi-line `git commit -m` messages
- [x] Include `Co-Authored-By: <agent-name> <noreply@...>` trailer on commits
- [x] Push to `main` immediately after commit when the user is waiting to paste HTML into Canvas

## DO NOT

- [ ] Em dashes (`—`, `&mdash;`). Anywhere. Hard ban. Use `:`, `,`, or restructure.
- [ ] Canvas-hosted URLs (`canvas.instructure.com/files/...`) in any page
- [ ] Relative image paths in pages that get pasted into Canvas
- [ ] Filenames containing "copy" (rename before committing)
- [ ] `max-width` cap on hero/showcase images (let them scale)
- [ ] `WidthType.PERCENTAGE` in docx-js (use DXA; percentages break in Google Docs)
- [ ] `--amend` git commits unless explicitly asked
- [ ] `--no-verify` to skip hooks unless explicitly asked
- [ ] Force push to `main`
- [ ] Commit without an explicit user request
- [ ] Commit `.env`, credentials, or secrets
- [ ] Use `git add -A` or `git add .`; stage files by name
- [ ] Edit `silva-module.css` or `silva-nav.js` unless framework requires it
- [ ] Skip the 6-vocab-words intake question
- [ ] Try to surgically patch legacy Canvas HTML; rebuild from framework templates instead

---

## FILE LAYOUT

```
.
├── CANVAS_BUILD_FRAMEWORK.md   ← single source of truth for assignment page builds
├── CLAUDE.md                   ← project memory (narrative, for Claude)
├── AGENTS.md                   ← this file (directive, for Codex)
├── CNAME                       ← www.creativesilva.com
├── index.html                  ← public landing
├── curriculum.html             ← index of every assignment, links to pages
├── assets/                     ← all images, AI/PSD files, logos. Public via raw.github URL
│   ├── PV LOGO NEW.png        ← canonical PVHS logo (URL-encode space as %20)
│   ├── Jimenez_Mockups.ai     ← example downloadable template
│   └── ...
├── css/
│   └── silva-module.css        ← all .silva-* classes used by Canvas pages
├── js/
│   └── silva-nav.js            ← site nav behavior, loaded by every Canvas page
├── curriculum/
│   └── shared/                 ← cross-course assignment pages (most live here)
│       ├── jimenez-step05-mockups.html  ← canonical reference build
│       └── jimenez-spring-final.html
└── (legacy course-specific dirs: digarts1/, photo1/, etc.)
```

---

## CANONICAL URLs

```
Site:              https://www.creativesilva.com
GitHub:            https://github.com/creativesilva/creativesilva-site
Asset base:        https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/
PVHS Logo:         https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/PV%20LOGO%20NEW.png
Live page format:  https://www.creativesilva.com/curriculum/shared/{slug}.html
```

---

## CANVAS BUILD: MINIMUM VIABLE STEPS

```
1. Read CANVAS_BUILD_FRAMEWORK.md
2. Ask intake (§1):
   - Assignment title + project context
   - Course(s) it belongs to (da1b, da2b, photo1, photo2, yearbook)
   - Style variant (Stock | Custom)
   - If Custom: 3 brand hex codes
   - Bilingual? (EN-only | EN+ES)
   - Hero image filename in /assets/
   - Step card count
   - Downloadable project file? (filename if yes)
   - Submission format
   - Prev/next step references
   - [REQUIRED] 6 vocabulary words with kid-friendly definitions
3. Create /curriculum/shared/{slug}.html using framework §4 scaffold + §5 templates
4. Add entry to curriculum.html for each course in answer 2
5. Run framework §8 pre-delivery checklist (15 items)
6. Commit and push to main
7. Confirm to user: https://www.creativesilva.com/curriculum/shared/{slug}.html
```

---

## REQUIRED PAGE STRUCTURE (Canvas Assignment)

Every Canvas assignment page MUST contain, in this order inside the `#top` div:

```
A. Title Card (wide ~16:6, single row: logo | breadcrumb+title centered | language toggle)
B. Overview Card (float-right hero image + 3 body paragraphs + 6-card vocabulary grid)
C. Project File Download Card (only if downloadable file exists)
D. Tips / Resources Card (only if relevant)
E. How to Complete (orange section, step cards inside scroll box with text hint + gradient fade)
F. What to Submit Card

[if bilingual, repeat A-F in #espanol div with Spanish translation]
```

Page MUST end with:

```html
<script>
  function silvaCopyHTML() { /* see framework §4 */ }
  function silvaDownloadHTML() { /* see framework §4 */ }
</script>
<script src="/js/silva-nav.js"></script>
```

---

## STYLE TOKENS

### PVHS Stock variant
```
page-bg:        #ffffff
header-grad:    linear-gradient(135deg,#003e3e 0%,#007474 50%,#1f7a5a 100%)
accent-primary: #007474
accent-soft:    #c8e6e0
```

### Custom Client variant (Jimenez example)
```
page-bg:        #080808
header-grad:    linear-gradient(135deg,#000000 0%,#1c1c1c 45%,#0b2948 100%)
accent-primary: #5f8fbf
accent-label:   #9ecbff
orange-steps:   #FF6B1A
text-body:      rgba(255,255,255,0.88)
card-bg-sub:    rgba(0,0,0,0.28)
```

---

## VOCABULARY GRID (REQUIRED IN EVERY OVERVIEW)

Exactly 6 words. Responsive grid via CSS Grid `repeat(auto-fit, minmax(180px, 1fr))`. 3 across desktop, 2 tablet, 1 phone. No media queries.

```html
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;">
  <!-- repeat 6 times -->
  <div style="background:rgba(0,0,0,0.32);border:1px solid rgba(95,143,191,0.28);border-left:3px solid #5f8fbf;border-radius:12px;padding:14px 16px;">
    <div style="color:#9ecbff;font-size:13pt;margin-bottom:4px;"><strong>{WORD}</strong></div>
    <div style="color:rgba(255,255,255,0.88);font-size:11pt;line-height:1.5;">{DEF_UNDER_15_WORDS}</div>
  </div>
</div>
```

Definitions: under 15 words, 5th grade language, no jargon nested inside.

---

## SCROLL PATTERNS

### Vertical (instructions, long lists)
```html
<div style="font-size:11pt;color:#ffb27c;margin-bottom:8px;opacity:0.85;">&#8595; Scroll inside the box to see all {N} steps</div>
<div class="silva-scroll" style="max-height:480px;overflow-y:auto;padding:12px 14px 18px;border:1px solid rgba(255,107,26,0.18);border-radius:14px;background:linear-gradient(to bottom,rgba(0,0,0,0.18) 0%,rgba(0,0,0,0.18) 88%,rgba(255,107,26,0.18) 100%);">
  <!-- cards -->
</div>
```

### Horizontal (galleries, comparisons)
```html
<div style="overflow-x:auto;display:flex;gap:14px;padding:6px 2px 14px;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;border:1px solid rgba(95,143,191,0.18);border-radius:14px;background:rgba(0,0,0,0.18);">
  <div style="flex:0 0 260px;scroll-snap-align:start;..."><!-- card --></div>
</div>
<div style="font-size:11pt;color:#9ecbff;opacity:0.75;text-align:center;margin-top:6px;">&#8592; Swipe or scroll to see more &#8594;</div>
```

### Decision rule
- Text content read top-to-bottom → vertical
- Visual comparison side-by-side → horizontal
- Exactly 6 items → no scroll, use the vocabulary grid pattern
- 4+ images for comparison → horizontal
- Video embed → no scroll, stack

---

## WRITING RULES (5TH GRADE, EN + ES)

### English
- Max 15 words per sentence (hard cap 20)
- Active voice always
- "Use" not "utilize". "Help" not "facilitate". "Show" not "demonstrate".
- "You" / "your", never "the student"
- One idea per sentence
- Lead with the verb. "Click Save." not "It is important that you click Save."
- No filler: cut "It is important to note that", "Please be sure to", "As mentioned previously"

### Spanish (Mexican Spanish, Santa Maria community)
- Use `tú`, never `usted`
- Present indicative over subjunctive
- Common verbs only: hacer, ver, poner, abrir, guardar, escoger, encontrar, usar
- Avoid passive `se` constructions
- HTML entities for accents and `ñ`

### Anti-bloat sniff test (run before commit)
1. Can I cut this sentence and still get the point? → Cut.
2. Card over 60 words? → Split.
3. Explaining why before saying what? → Flip.
4. Word a 5th grader wouldn't say? → Swap.
5. Sentence opener "In this step..."? → Just start with the verb.

---

## GIT WORKFLOW

```bash
# ALWAYS stage by filename, never -A or .
cd /Users/riva/RIVA_CODE/creativesilva-site
git add curriculum/shared/{slug}.html assets/{new-assets} curriculum.html

# ALWAYS use HEREDOC for commits
git commit -m "$(cat <<'EOF'
Short subject under 70 chars (no em dashes)

Optional body explaining the why.

Co-Authored-By: <agent> <noreply@example.com>
EOF
)"

git push origin main
```

### Commit message rules
- Subject line under 70 chars
- No em dashes (yes, even in commit messages)
- Body explains "why", not "what"
- Always include Co-Authored-By trailer
- Never `--amend` unless asked
- Never `--no-verify` unless asked
- Never force push

---

## LEGACY CODE MIGRATION

When user pastes old Canvas HTML and asks for upgrade:

```
1. Parse: extract project/step/title/overview/steps/images/downloads/submission
2. Run intake §1 — ALWAYS ask for 6 vocab words (legacy code never has them)
3. Map old → new sections per framework §14 mapping table
4. Migrate assets: move Canvas-hosted images to /assets/, rename "copy" files
5. Build fresh page using framework §4 scaffold + §5 templates
   (DO NOT try to edit old HTML in place)
6. Add missing: title card, vocab grid, scroll affordances, ES translation, script block
7. Run §8 checklist
8. Commit: "Migrate {Project} {Step} from legacy Canvas HTML to framework"
```

Legacy red flags = signal to rebuild not patch:
- `<table>` for layout
- Canvas-hosted image URLs
- Em dashes throughout
- Teacher-voice copy
- No vocabulary section
- Hard-coded pixel widths
- Inline `<font>` or non-Arial font-family

---

## PRE-DELIVERY CHECKLIST (RUN BEFORE COMMIT)

Reproduced from framework §8 for quick reference. All must be true.

```
□ Page <title> matches assignment
□ --course-accent matches chosen variant
□ PVHS logo from canonical raw URL
□ Hero image: 52% width, no max-width cap, box-shadow present
□ Float-right parent has overflow:hidden
□ Breadcrumb matches project context
□ Zero em dashes (grep for — and &mdash;)
□ All asset URLs use raw.githubusercontent.com
□ Smart quote entities in long-form copy
□ Overview contains exactly 6 vocab cards
□ Vocab defs under 15 words, 5th grade level
□ All body/instruction copy at 5th grade level
□ All cards under 60 words
□ Scroll containers: text hint above + gradient fade + silva-scroll class
□ Horizontal scrolls: swipe hint below
□ Last step card uses margin-bottom:0
□ silvaCopyHTML() / silvaDownloadHTML() script block present
□ <script src="/js/silva-nav.js"></script> present
□ Download filename matches page slug
□ If bilingual: ES block present, anchors work both ways, Spanish at 5th grade level
□ Entry added to curriculum.html for each target course
```

---

## REFERENCE BUILDS

| File | Purpose |
|------|---------|
| `curriculum/shared/jimenez-step05-mockups.html` | Canonical Custom Client build. Diff against this when in doubt. |
| `curriculum/shared/jimenez-spring-final.html` | Earlier build (legacy pattern reference) |
| `css/silva-module.css` | All `.silva-*` classes |
| `js/silva-nav.js` | Site nav behavior |

---

## QUICK ANSWERS

**Q: Where do new Canvas pages go?**
A: `/curriculum/shared/{kebab-case-slug}.html`

**Q: How do I get an asset into a Canvas page?**
A: Drop it in `/assets/`, commit it, reference via `https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/{FILENAME}` with spaces URL-encoded as `%20`.

**Q: When does a page go live?**
A: ~60s after `git push origin main`. URL is `https://www.creativesilva.com/{path}`.

**Q: Should I use Markdown or HTML for Canvas pages?**
A: HTML only. Canvas pastes raw HTML, not Markdown.

**Q: Can I add a new CSS class?**
A: Avoid it. Canvas's RCE strips most classes. Use inline `style="..."`. The exception is `silva-scroll` and the site nav classes, which already exist.

**Q: User asked to ship right now. What's the fastest path?**
A: Build, push, paste live URL. No extra commentary. Confirm the Copy Canvas HTML button works.

**Q: User says "take creative control." What does that mean?**
A: Make aesthetic decisions yourself. Respect the framework structure. Keep it clean, balanced, minimal. Show the result; don't ask for color-by-color approval.

---

**END.** For deeper context see `CANVAS_BUILD_FRAMEWORK.md` (canonical) and `CLAUDE.md` (narrative).
