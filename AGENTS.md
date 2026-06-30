# AGENTS.md

# PVHS Canvas Curriculum Builder for Codex Web

This repository powers Creative Silva curriculum pages and Canvas-ready assignment HTML. Codex must act as a careful curriculum production assistant, not just a code editor.

Codex should create, revise, translate, validate, and link assignment pages using the established Silva module framework.

## 1. Primary Mission

When the user asks for a new assignment, module page, design revision, translation, or migration:

1. Read this file first.
2. Read `CANVAS_BUILD_FRAMEWORK.md`.
3. Inspect the closest existing finished page before editing.
4. Create or update the correct HTML file.
5. Keep the work Canvas-safe.
6. Validate the page before finishing.
7. Summarize exactly what changed.

Do not invent a new design system. Match the existing PVHS and Creative Silva curriculum framework.

## 2. Files Codex Must Treat as Source of Truth

Always prefer repo files over assumptions.

Required reference files:

- `CANVAS_BUILD_FRAMEWORK.md` (see §3.5 for the LOCKED Angular Gradient Framework)
- `curriculum/shared/da-finals-quiz-prep.html` (master reference for the Angular Gradient / Finals style)
- `tools/build-da-finals.py` (generator that emits the master page; encodes the locked card/button/chip rules)
- `curriculum/shared/jimenez-step05-mockups.html`
- `curriculum/shared/jimenez-spring-final.html`
- `curriculum.html`
- `css/silva-module.css`
- `js/silva-nav.js`
- Existing assignment pages in `curriculum/shared/`

If files disagree, follow this order:

1. Current user request
2. This `AGENTS.md`
3. `CANVAS_BUILD_FRAMEWORK.md`
4. Closest finished assignment example
5. Older legacy pages

## 3. Critical Non-Negotiable Rules

These rules apply to every build and edit.

- Do not use em dashes. Never use `—` or `&mdash;`.
- Use student-facing language at about 5th grade reading level.
- Keep sentences short and direct.
- Use active voice.
- Use "you" and "your" for student directions.
- Keep each card under about 60 words.
- Split long content into smaller cards.
- Every Overview section must include exactly 6 vocabulary words.
- Vocabulary definitions must be kid-friendly and under 15 words.
- Long step sections must use a visible scroll box.
- Step scroll boxes must include a scroll hint and bottom fade.
- All Canvas assets must use raw GitHub URLs.
- Do not use Canvas-hosted file URLs.
- Do not use relative image or download paths inside Canvas copy content.
- Do not invent asset filenames or image URLs.
- Do not rename user assets unless asked.
- Do not remove the copy/download script.
- Do not remove `<script src="/js/silva-nav.js"></script>`.
- Do not remove the PVHS logo.
- Do not push directly to `main` unless the user explicitly asks.
- Prefer a branch or pull request workflow when available.

## 4. Canonical Asset Rules

All images and downloadable files should live in:

```text
assets/
```

All Canvas-facing image and download URLs must use this pattern:

```text
https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/{URL_ENCODED_FILENAME}
```

The PVHS logo must use this exact URL:

```text
https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/PV%20LOGO%20NEW.png
```

Filename rules:

- Spaces are allowed in the repo, but must become `%20` in URLs.
- Do not use filenames that contain `copy`.
- Prefer clear filenames that describe the assignment or asset.
- If the asset does not exist in the repo, stop and report it as missing.
- If the user gives a Canvas, Google Drive, Dropbox, or other external asset link, ask for the file to be added to `assets/` unless the user explicitly says otherwise.

## 5. Default Build Locations

New Canvas assignment pages normally go here:

```text
curriculum/shared/{slug}.html
```

Published pages normally need an entry in:

```text
curriculum.html
```

Course slugs:

```text
Digital Arts 1B: da1b
Digital Arts 2B: da2b
Photo 1: photo1
Photo 2: photo2
Yearbook: yearbook
```

Live page pattern:

```text
https://www.creativesilva.com/curriculum/shared/{slug}.html
```

## 6. Codex Task Modes

Use the correct mode based on the user request.

### Mode A: New Assignment Build

Use when the user asks for a new assignment or module.

Required minimum intake:

- Assignment title
- Course or courses
- Style variant: PVHS Stock or Custom Client
- Bilingual choice: English only or English plus Spanish
- Hero image filename or confirmation that no hero image is ready yet
- Step count or rough task flow
- Submission format
- Any downloadable project file

If information is missing:

- Ask one short batched clarification question.
- If only non-critical details are missing, use safe defaults and list assumptions.
- Never invent image filenames, download filenames, or client brand colors.

Safe defaults when user does not specify:

- Bilingual: English plus Spanish
- Style: PVHS Stock
- Step count: 6 to 8 concise steps
- Reading level: 5th grade
- Output file: `curriculum/shared/{slug}.html`
- Add to `curriculum.html`: yes, when course is known
- Vocabulary: choose 6 terms from the actual assignment content

### Mode B: Design or Layout Revision

Use when the user asks to adjust an existing page design.

Workflow:

1. Find and read the existing page.
2. Identify the exact section to modify.
3. Preserve all required scripts, anchors, image paths, and Canvas copy root.
4. Make the smallest safe edit that solves the request.
5. Re-run the validation checklist.
6. Summarize before and after.

Never redesign the whole page unless the user asks for a full rebuild.

### Mode C: English and Spanish Copy Revision

Use when the user asks for better wording, translation, or simpler student directions.

Rules:

- Preserve structure unless the user asks for layout changes.
- Use short English sentences.
- Use `tú` voice in Spanish.
- Use neutral Mexican-American classroom Spanish.
- Use HTML entities for Spanish punctuation and accents.
- Do not leave English text inside the Spanish section.
- Do not translate filenames, app names, menu labels, or required submission file types unless helpful.

Spanish entity examples:

```text
&aacute; &eacute; &iacute; &oacute; &uacute; &ntilde; &iexcl; &iquest;
```

### Mode D: Legacy Canvas Migration

Use when the user pastes old Canvas HTML or asks to modernize an old assignment.

Do not patch the old layout. Rebuild fresh using the framework.

Migration workflow:

1. Extract title, course, project, steps, assets, downloads, and submission requirements.
2. Replace old layout with the current Silva module framework.
3. Replace Canvas-hosted assets with raw GitHub asset URLs.
4. Add the title card, overview, 6 vocabulary cards, scroll-boxed steps, and submit card.
5. Add Spanish if requested or if the page is intended to be bilingual.
6. Keep the copy/download buttons and nav script.
7. Validate before finishing.

### Mode E: Curriculum Index Update

Use when adding a page to `curriculum.html`.

Add the new page to each requested course array using this shape:

```javascript
{ course: "{course-slug}",
  name: "{Step NN}: {Short Title}",
  pages: 1,
  status: "published",
  url: "curriculum/shared/{slug}.html"
},
```

Make sure:

- The course slug is correct.
- The title is short enough for the curriculum page.
- The URL matches the created file.
- The page is not duplicated in the same course list.

## 7. Required Page Structure

Every assignment page must preserve this outer pattern:

```text
Full HTML document
Site nav
silva-page wrapper
silva-module-content wrapper
#top Canvas copy root
English section
Spanish section, if bilingual
copy/download script
/js/silva-nav.js script
```

Inside each language section, use this order:

1. Title Card
2. Overview Card with hero image and 6 vocabulary cards
3. Project File Download Card, only if needed
4. Tips or Resources Card, only if needed
5. How to Complete Card with scroll-boxed step cards
6. What to Submit Card

## 8. Title Card Requirements

The title card must include:

- PVHS logo on the left
- Centered breadcrumb
- Assignment title
- Language toggle if bilingual
- Compact wide layout
- No wasted vertical space

For bilingual pages:

- English toggle links to `#espanol`
- Spanish toggle links to `#top`
- English label: `Clic para Espa&ntilde;ol`
- Spanish label: `Back to English`

## 9. Overview Requirements

Every Overview card must include:

- A float-right hero image when an image is available
- Hero image width near 52 percent
- No max-width cap on the hero image
- `min-width:220px`
- Border radius and shadow
- Parent container with `overflow:hidden`
- Clear float before vocabulary grid
- Exactly 6 vocabulary cards

If the hero image is missing, do not invent one. Build the page with a clear placeholder note in the Codex summary, not in the student-facing HTML, unless the user asks for a placeholder.

## 10. Step Section Requirements

Step sections must use the orange treatment.

Required scroll hint:

```html
<div style="font-size:11pt;color:#ffb27c;margin-bottom:8px;opacity:0.85;">&#8595; Scroll inside the box to see all {N} steps</div>
```

Required scroll container traits:

- `class="silva-scroll"`
- `max-height:480px`
- `overflow-y:auto`
- visible border
- bottom-fade gradient
- step cards inside the scroll box

Step card rules:

- Use `01.`, `02.`, `03.` numbering.
- Keep body text under about 60 words.
- Use strong tags for file names, menu commands, and key actions.
- Last card must use `margin-bottom:0`.
- Do not use line breaks to space cards.

## 11. Writing Rules

English:

- Use direct student voice.
- Use plain words.
- Avoid teacher voice.
- Say "You will..." instead of "Students will be expected to..."
- Start with the action.
- Avoid filler phrases.
- Avoid long paragraphs.

Spanish:

- Use `tú`, not `usted`.
- Use clear classroom Spanish.
- Use common verbs: abrir, guardar, usar, hacer, poner, ver, escoger.
- Keep sentences short.
- Use HTML entities for accents.
- Avoid Castilian or Argentine regional forms.
- Do not leave English copy in Spanish sections.

## 12. Style Variants

### PVHS Stock

Use for general school assignments.

Preferred tokens:

```text
page background: #ffffff
page text: #0e2a30
header gradient: #003e3e to #007474 to #1f7a5a
accent: #007474
soft accent: #c8e6e0
card background: #f5fbfa
card border: #cfe6df
```

### Custom Client

Use for client projects, mockups, brand work, or when the assignment has a special brand identity.

Default custom pattern:

```text
page background: #080808
page text: #ffffff
header gradient: #000000 to #1c1c1c to brand dark tone
client accent: user-provided accent
label accent: lighter accent
steps accent: #FF6B1A
```

If brand colors are missing, ask the user for them. Do not invent custom brand colors unless asked to make a reasonable first pass.

## 13. Validation Checklist

Before finishing, Codex must check the changed files.

Content checks:

- Page title matches assignment.
- Breadcrumb matches project context.
- Copy is student-facing.
- English is simple and direct.
- Spanish uses `tú` and has no English leftovers.
- Overview has exactly 6 vocabulary cards.
- Each vocabulary definition is under 15 words.
- Step cards are concise.
- Submission instructions are clear.

HTML checks:

- PVHS logo URL is canonical.
- Asset URLs use raw GitHub.
- No Canvas-hosted asset URLs.
- No broken relative asset URLs inside `#top`.
- Hero image uses float-right pattern when present.
- Float parent uses `overflow:hidden`.
- Step section uses scroll hint.
- Scroll container uses `class="silva-scroll"`.
- Last step card has `margin-bottom:0`.
- Copy/download script exists.
- `/js/silva-nav.js` script exists.

Search checks:

Run these checks or equivalent manual searches:

```bash
grep -n "—\|&mdash;" curriculum/shared/{slug}.html
grep -n "canvas.instructure.com\|smjuhsd.instructure.com" curriculum/shared/{slug}.html
grep -n "src=\"assets/\|href=\"assets/\|src=\"/" curriculum/shared/{slug}.html
grep -n "silvaCopyHTML\|silvaDownloadHTML\|silva-nav.js" curriculum/shared/{slug}.html
```

Expected result:

- No em dash matches.
- No Canvas-hosted asset URL matches.
- No unsafe relative asset URL inside `#top`.
- Required scripts are present.

If repo scripts exist, run them too. Do not make up passing test results. If tests were not run, say so.

## 14. Commit and Pull Request Rules

Prefer pull requests for Codex Web work.

Do:

- Create or update the page file.
- Update `curriculum.html` when requested or required.
- Include new assets only when they exist in the repo or were provided by the user.
- Use a clear commit message.
- Summarize changed files.

Do not:

- Push straight to `main` unless asked.
- Commit unrelated files.
- Reformat the whole repo.
- Rewrite unrelated assignments.
- Claim the page was published unless the commit or PR was actually created.

Good commit message pattern:

```text
Add {Assignment Title} for {Course or Project}
```

Good PR summary pattern:

```text
Summary:
- Added `curriculum/shared/{slug}.html`
- Added bilingual Canvas-ready assignment content
- Added or updated curriculum link for {course}
- Verified asset URLs use raw GitHub paths

Validation:
- Checked for em dashes
- Checked for Canvas-hosted asset links
- Checked copy/download scripts
- Checked Spanish section, if bilingual
```

## 15. Standard User Prompt Template

When the user wants a new assignment, they can paste this:

```text
Build a new Canvas assignment page.

Course:
Assignment title:
Project or unit:
Style: PVHS Stock or Custom Client
Bilingual: English plus Spanish or English only
Hero image filename in assets:
Download file in assets, if any:
Submission format:
Rough steps:
Special notes:

Follow AGENTS.md and CANVAS_BUILD_FRAMEWORK.md.
Create the page in curriculum/shared/.
Update curriculum.html.
Use raw GitHub asset URLs.
Keep the writing at 5th grade level.
Validate before finishing.
```

## 16. Standard Design Revision Prompt Template

When the user wants an existing page edited, they can paste this:

```text
Revise this existing Canvas assignment page:

File:
Change needed:
Keep:
Do not change:

Follow AGENTS.md and CANVAS_BUILD_FRAMEWORK.md.
Make the smallest safe edit.
Validate before finishing.
Summarize the changed files.
```

## 17. Standard Translation Prompt Template

When the user wants bilingual cleanup, they can paste this:

```text
Revise the English and Spanish copy on this page:

File:
Goal:
Reading level: 5th grade
Spanish voice: tú, neutral Mexican-American classroom Spanish

Keep the layout.
Do not change asset paths.
Validate before finishing.
```

## 18. When Codex Is Unsure

If unsure, Codex should not guess silently.

Allowed safe assumptions:

- Use PVHS Stock style for general school content.
- Use English plus Spanish if the user mentions bilingual or Spanish.
- Use the closest existing page as the structural model.
- Create a clear slug from the assignment title.
- Choose 6 vocabulary words from the step content.

Never assume:

- Missing asset filenames
- Missing download files
- Brand colors for a custom client
- The correct course when none is stated
- That a Canvas-hosted asset is acceptable
- That a page is published before the PR or commit exists

## 19. Final Response Requirements for Codex

At the end of each Codex task, respond with:

```text
Changed files:
- ...

What I built:
- ...

Validation:
- ...

Assumptions or missing items:
- ...

Next recommended step:
- ...
```

Keep the final response short, concrete, and honest.
