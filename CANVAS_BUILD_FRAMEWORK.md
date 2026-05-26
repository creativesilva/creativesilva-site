# Canvas Build Framework

A repeatable, foolproof spec for building Silva-module Canvas assignment pages on `creativesilva-site`. Any AI agent (or human) following this doc should be able to ship a new, polished, bilingual-ready assignment page from a 60-second intake.

**Author:** Chris Silva
**Last updated:** 2026-05-26
**Reference build:** `curriculum/shared/jimenez-step05-mockups.html`

---

## 0. How to Use This Doc

When the user says "build a new Canvas assignment" (or similar):

1. **Read this doc end-to-end first.**
2. **Ask the intake questions in §1.** Do NOT start building until all answers are collected.
3. **Pick the style variant** (§2: PVHS Stock or §3: Custom Client) from the answers.
4. **Build the page** following the section templates in §4 in the exact order listed.
5. **Run the pre-delivery checklist in §7** before committing.
6. **Commit and push** following §8.

**Hard rules** (apply to every build, no exceptions):
- **Every page that uses AI-generated imagery includes the AI Image Disclaimer footer** at the bottom of both EN and ES language sections (see §16).
- No em dashes anywhere. Use colons, commas, or restructure the sentence.
- All images and downloadable files hosted at `raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/...` (never Canvas-hosted URLs, never relative paths).
- URL-encode spaces in asset paths as `%20`.
- Use smart quotes via HTML entities (`&#x2018;` `&#x2019;` `&#x201C;` `&#x201D;`) in copy.
- Page must include the copy/download script block AND the `<script src="/js/silva-nav.js">` tag.
- **All student-facing copy written at 5th grade reading level** in both English and Spanish (see §12).
- **Every Overview card includes exactly 6 vocabulary words** as a responsive grid (3 across × 2 rows on wide, collapses on narrow), with kid-friendly definitions (see §5.B).
- **Long sections must have a visible scroll affordance** (vertical scroll box with "scroll for more" hint and bottom fade, OR horizontal scroll with swipe hint, depending on content type — see §13).
- **Cards stay under ~60 words.** If longer, split into two cards. Anti-bloat is a hard rule.

---

## 1. Intake Questionnaire (Ask Before Building)

Always ask these as a single batched `AskUserQuestion` call when possible. Skip a question only if the answer is unambiguous from the user's opening message.

**Q1. Assignment title and project context.**
What's the assignment called and what project/client does it belong to?
*Example: "Step 05: Brand Mockups for Jimenez Mobile Detailing Spring Final"*

**Q2. Course(s) it belongs to.**
Which course(s) on `curriculum.html` should link to this page?
Options: Digital Arts 1B, Digital Arts 2B, Photo 1, Photo 2, Yearbook, Other.

**Q3. Style variant.**
Stock PVHS theme (clean white/green/teal school colors) or Custom Client theme (dark + brand accent colors)?

**Q4. (If Custom) Brand color palette.**
Provide three hex codes: primary background tone, accent color, secondary accent. *Example for Jimenez: bg `#080808` + navy `#0b2948`, accent `#5f8fbf`, label `#9ecbff`.*

**Q5. Bilingual?**
English only, or English + Spanish (mirrored sections with anchor toggle)?

**Q6. Hero / overview float-right image.**
Filename in `/assets/` (or will the user provide one)? This is the wide image that sits to the right of the "What You Are Building" overview text.

**Q7. Step card count and titles.**
Roughly how many step-by-step cards? List rough titles if known (typical range: 6 to 12). Cards live in a scroll box so quantity doesn't bloat the page.

**Q8. Downloadable project file?**
Is there an `.ai`, `.psd`, `.pdf`, or template file students need to download? If yes, the file must be hosted under `/assets/` (no spaces, no "copy" in filename).

**Q9. Submission format.**
What does the student submit to Canvas? *Example: "5-page PDF (one per artboard)", "PSD file + JPG export", "Link to Behance post".*

**Q10. Previous/next step reference?**
Does this assignment reference a previous step (e.g., "In Step 04 you built...") or set up a next step (e.g., "In Step 06 you will...")? Capture both if applicable.

**Optional Q11.** Any special sub-sections to include? (e.g., Google Image Search tips, video embeds, rubric table, glossary). Default = none.

---

## 2. Style Variant A: PVHS Stock

Use when the assignment is generic school content (not tied to a specific client brand).

### Color tokens
```
--page-bg:        #ffffff
--page-text:      #0e2a30
--header-grad:    linear-gradient(135deg, #003e3e 0%, #007474 50%, #1f7a5a 100%)
--header-text:    #ffffff
--accent-primary: #007474   /* dark teal — PVHS brand */
--accent-soft:    #c8e6e0   /* light teal wash */
--card-bg:        #f5fbfa
--card-border:    #cfe6df
--orange-steps:   #007474   /* keep teal for steps too; or use #b97a00 amber */
--meta-label:     #007474
```

### Header look
- Solid teal gradient bar with white text.
- PV logo on left at `min(90px,15vw)`.
- Centered breadcrumb in white at 14pt bold: `Course · Project · Step XX`.
- Title in white at 22pt bold below the breadcrumb.
- Language toggle (if bilingual) right side as a white pill.

### Section accents
- Use teal `#007474` for left-borders and label text everywhere the Jimenez build uses `#5f8fbf` / `#FF6B1A`.

---

## 3. Style Variant B: Custom Client Brand

Use when the assignment is tied to a specific client mockup project (Jimenez Mobile Detailing, Estrella Boutique, etc.). This is the **dark theme** pattern proven in `jimenez-step05-mockups.html`.

### Color tokens (Jimenez example, swap per client)
```
--page-bg:        #080808   /* near-black canvas */
--page-text:      #ffffff
--header-grad:    linear-gradient(135deg, #000000 0%, #1c1c1c 45%, #0b2948 100%)
--header-border:  rgba(255,255,255,0.08)
--accent-primary: #5f8fbf   /* client accent — used on overview left-border */
--accent-label:   #9ecbff   /* lighter version of accent — used for small blue labels */
--orange-steps:   #FF6B1A   /* always orange for step section regardless of client */
--orange-soft:    rgba(255,107,26,0.22)
--card-bg-sub:    rgba(0,0,0,0.28)
--text-body:      rgba(255,255,255,0.88)
--text-soft:      rgba(255,255,255,0.82)
```

### Header look
- Dark gradient bar, single compact row.
- PV logo on left at `min(90px,15vw)`.
- Centered breadcrumb in `#9ecbff` 14pt bold: `Client Name · Project · Step XX`.
- Title in white at 22pt bold below the breadcrumb.
- Language toggle right as white pill.

### Section colors by purpose
| Section | Left border | Label color | Background |
|--------|------------|-------------|-----------|
| Overview / hero | `#5f8fbf` (accent) | `#9ecbff` | white wash on dark |
| How to Complete (steps) | `#FF6B1A` | `#ff6b1a` | orange wash |
| Step sub-cards | `#FF6B1A` (4px) | `#ff6b1a` | `rgba(0,0,0,0.28)` |
| Project file download | `#5f8fbf` | `#9ecbff` | white wash |
| What to Submit | `#FF6B1A` | `#ffb27c` | orange wash |
| Tips / callout boxes | `#9ecbff` | `#9ecbff` | dark navy wash |

---

## 4. Page Structure (Order Matters)

Every Canvas assignment page is built in this exact section order. The outer wrapper, nav, and script blocks are fixed. The inner section blocks repeat per language (EN, then ES if bilingual).

### Outer structure (always identical)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{Assignment Title} — {Project Name}</title>
  <style>:root { --course-accent: {ACCENT_HEX}; }</style>
  <link rel="stylesheet" href="/css/silva-module.css" />
</head>
<body>

  <!-- SITE NAV (fixed, do not edit per assignment except breadcrumb text) -->
  <nav class="silva-nav" aria-label="Module navigation">
    <div class="silva-nav-inner">
      <div class="silva-breadcrumb">
        <a href="/curriculum.html">Curriculum</a>
        <span class="bc-sep">›</span>
        <a href="/curriculum.html" class="bc-hide-sm">{Course}</a>
        <span class="bc-sep bc-hide-sm">›</span>
        <a href="/curriculum.html" class="bc-hide-sm">{Project}</a>
        <span class="bc-sep bc-hide-sm">›</span>
        <span class="bc-current">{Step Short}</span>
      </div>
      <div class="silva-nav-spacer"></div>
      <button class="silva-copy-btn" onclick="silvaCopyHTML()">&#128203; Copy Canvas HTML</button>
      <button class="silva-download-btn" onclick="silvaDownloadHTML()">&#128229; Download HTML</button>
    </div>
  </nav>

  <div class="silva-page">
  <div id="silva-module-content">

  <!-- THIS DIV IS WHAT GETS COPIED TO CANVAS -->
  <div id="top" style="width:100%;margin:0 auto;font-family:Arial,sans-serif;color:#ffffff;background:{PAGE_BG};border-radius:30px;overflow:hidden;">

    <!-- ENGLISH SECTION -->
    <div style="padding:28px 28px 40px;">
      {SECTIONS A through F in order}
    </div><!-- /English padding -->

    <!-- SPANISH SECTION (only if bilingual) -->
    <div id="espanol" style="padding:28px 28px 40px;border-top:2px solid rgba(255,255,255,0.10);">
      {SECTIONS A through F translated, in same order}
    </div><!-- /espanol -->

  </div><!-- /top -->

  </div>
  </div>

  <!-- COPY/DOWNLOAD SCRIPT (do not modify, just change download filename) -->
  <script>
    function silvaCopyHTML() {
      const el = document.getElementById('top');
      const html = el.outerHTML;
      navigator.clipboard.writeText(html).then(function() {
        var btn = document.querySelector('.silva-copy-btn');
        btn.textContent = '✓ Copied to clipboard!';
        btn.classList.add('copied');
        setTimeout(function() {
          btn.innerHTML = '&#128203; Copy Canvas HTML';
          btn.classList.remove('copied');
        }, 2500);
      }).catch(function() {
        alert('Copy failed. Try selecting the page source manually.');
      });
    }
    function silvaDownloadHTML() {
      var el = document.getElementById('top');
      var html = el.outerHTML;
      var blob = new Blob([html], { type: 'text/html' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = '{slug}-canvas.html';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }
  </script>
  <script src="/js/silva-nav.js"></script>

</body>
</html>
```

### Sections A through F (build in this order inside each language block)

**A. Title Card (wide landscape header, ~16:6 ratio)**
**B. Overview Card (float-right hero image)**
**C. Project File Download Card (only if Q8 = yes)**
**D. Tips / Resources Card (only if Q11 includes any)**
**E. How to Complete (orange section, step cards inside scroll box)**
**F. What to Submit Card**

---

## 5. Section Templates (Copy-Paste with Substitution)

Variables in `{CURLY_BRACES}` get swapped per assignment. Hex codes shown are for the **Custom Client (Jimenez)** variant; swap to PVHS Stock tokens from §2 if that's the chosen variant.

### A. Title Card (wide landscape header)
The header is intentionally wide and shallow (roughly 16:6 proportions). One row, no wasted vertical space.

```html
<div style="background:linear-gradient(135deg,#000000 0%,#1c1c1c 45%,#0b2948 100%);border:1px solid rgba(255,255,255,0.08);border-radius:20px;padding:16px 24px;margin-bottom:24px;">
  <div style="display:flex;align-items:center;gap:16px;">
    <img src="https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/PV%20LOGO%20NEW.png"
         alt="Pioneer Valley High School Logo"
         style="width:min(90px,15vw);height:auto;flex-shrink:0;" />
    <div style="flex:1;text-align:center;">
      <div style="margin-bottom:6px;"><span style="font-size:14pt;color:#9ecbff;"><strong>{CLIENT_OR_COURSE} &nbsp;&bull;&nbsp; {PROJECT} &nbsp;&bull;&nbsp; Step {NN}</strong></span></div>
      <div style="color:#ffffff;font-size:22pt;font-weight:700;line-height:1.1;"><strong>{ASSIGNMENT_TITLE}</strong></div>
    </div>
    <div style="flex-shrink:0;">
      <a href="#espanol" style="background:rgba(255,255,255,0.92);color:#0b2948;text-decoration:none;padding:7px 16px;border-radius:999px;display:inline-block;font-size:11pt;white-space:nowrap;"><strong>Clic para Espa&ntilde;ol</strong></a>
    </div>
  </div>
</div>
```

For Spanish mirror, swap the breadcrumb text + title and change `href="#espanol"` to `href="#top"` and link label to `Back to English`.

### B. Overview Card (float-right hero image + required vocab grid)
The hero image is the showcase. Width 52%, no max-width cap, strong shadow. The Overview card MUST end with a 6-word vocabulary grid.

```html
<div style="background:linear-gradient(180deg,rgba(255,255,255,0.08) 0%,rgba(255,255,255,0.04) 100%);border:1px solid rgba(255,255,255,0.08);border-left:6px solid #5f8fbf;border-radius:24px;padding:30px;margin-bottom:24px;overflow:hidden;">
  <img src="https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/{HERO_IMAGE_FILENAME}"
       alt="{HERO_ALT_TEXT}"
       style="float:right;width:52%;min-width:220px;height:auto;border-radius:20px;margin:0 0 22px 30px;border:1px solid rgba(255,255,255,0.18);box-shadow:0 8px 40px rgba(0,0,0,0.6);" />
  <div style="margin-bottom:8px;"><span style="font-size:14pt;color:#9ecbff;"><strong>Step {NN} Overview</strong></span></div>
  <div style="margin-bottom:14px;"><span style="font-size:18pt;color:#ffffff;"><strong>What You Are Building</strong></span></div>
  <div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{OVERVIEW_PARAGRAPH_1}</span></div>
  <div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{OVERVIEW_PARAGRAPH_2}</span></div>
  <div style="margin-bottom:22px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{OVERVIEW_PARAGRAPH_3}</span></div>

  <!-- Clear the float before the vocab grid so it sits full-width below -->
  <div style="clear:both;"></div>

  <!-- VOCABULARY GRID: exactly 6 cards, 3 across on wide screens, responsive collapse -->
  <div style="margin-bottom:10px;"><span style="font-size:14pt;color:#9ecbff;"><strong>Vocabulary You Will Use</strong></span></div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;">
    <div style="background:rgba(0,0,0,0.32);border:1px solid rgba(95,143,191,0.28);border-left:3px solid #5f8fbf;border-radius:12px;padding:14px 16px;">
      <div style="color:#9ecbff;font-size:13pt;margin-bottom:4px;"><strong>{WORD_1}</strong></div>
      <div style="color:rgba(255,255,255,0.88);font-size:11pt;line-height:1.5;">{KID_FRIENDLY_DEF_1}</div>
    </div>
    <div style="background:rgba(0,0,0,0.32);border:1px solid rgba(95,143,191,0.28);border-left:3px solid #5f8fbf;border-radius:12px;padding:14px 16px;">
      <div style="color:#9ecbff;font-size:13pt;margin-bottom:4px;"><strong>{WORD_2}</strong></div>
      <div style="color:rgba(255,255,255,0.88);font-size:11pt;line-height:1.5;">{KID_FRIENDLY_DEF_2}</div>
    </div>
    <div style="background:rgba(0,0,0,0.32);border:1px solid rgba(95,143,191,0.28);border-left:3px solid #5f8fbf;border-radius:12px;padding:14px 16px;">
      <div style="color:#9ecbff;font-size:13pt;margin-bottom:4px;"><strong>{WORD_3}</strong></div>
      <div style="color:rgba(255,255,255,0.88);font-size:11pt;line-height:1.5;">{KID_FRIENDLY_DEF_3}</div>
    </div>
    <div style="background:rgba(0,0,0,0.32);border:1px solid rgba(95,143,191,0.28);border-left:3px solid #5f8fbf;border-radius:12px;padding:14px 16px;">
      <div style="color:#9ecbff;font-size:13pt;margin-bottom:4px;"><strong>{WORD_4}</strong></div>
      <div style="color:rgba(255,255,255,0.88);font-size:11pt;line-height:1.5;">{KID_FRIENDLY_DEF_4}</div>
    </div>
    <div style="background:rgba(0,0,0,0.32);border:1px solid rgba(95,143,191,0.28);border-left:3px solid #5f8fbf;border-radius:12px;padding:14px 16px;">
      <div style="color:#9ecbff;font-size:13pt;margin-bottom:4px;"><strong>{WORD_5}</strong></div>
      <div style="color:rgba(255,255,255,0.88);font-size:11pt;line-height:1.5;">{KID_FRIENDLY_DEF_5}</div>
    </div>
    <div style="background:rgba(0,0,0,0.32);border:1px solid rgba(95,143,191,0.28);border-left:3px solid #5f8fbf;border-radius:12px;padding:14px 16px;">
      <div style="color:#9ecbff;font-size:13pt;margin-bottom:4px;"><strong>{WORD_6}</strong></div>
      <div style="color:rgba(255,255,255,0.88);font-size:11pt;line-height:1.5;">{KID_FRIENDLY_DEF_6}</div>
    </div>
  </div>
</div>
```

**Float-right rules:**
- Width as percentage (52%), `min-width:220px`, NO `max-width`. This makes it scale with the browser, never get cropped, never get tiny.
- Always add `box-shadow:0 8px 40px rgba(0,0,0,0.6)` for impact.
- Parent container needs `overflow:hidden` to clear the float.
- Margin `0 0 22px 30px` keeps body text from hugging the image.
- Add `<div style="clear:both;"></div>` between body paragraphs and the vocab grid so the grid sits full-width below the image, not wrapped beside it.

**Vocabulary grid rules:**
- Exactly **6 words**. Not 4, not 8. Six fills two clean rows of three on wide screens and gracefully collapses to 2x3 or 1x6 on narrow.
- Words must be drawn from the content of this specific module (terms students will actually encounter in the steps below).
- Definitions: under 15 words, 5th grade reading level, plain English. Skip the dictionary-style "n." or pronunciation guides.
- For Spanish mirror, label becomes `Vocabulario Que Vas a Usar` and definitions translated to 5th grade Spanish (see §12).
- The `repeat(auto-fit, minmax(180px, 1fr))` grid is responsive: 3 cols on desktop, 2 cols on tablet, 1 col on phone. No media queries needed.

### C. Project File Download Card (optional)
```html
<div style="background:linear-gradient(180deg,rgba(255,255,255,0.08) 0%,rgba(255,255,255,0.04) 100%);border:1px solid rgba(255,255,255,0.08);border-left:6px solid #5f8fbf;border-radius:24px;padding:24px 30px;margin-bottom:24px;">
  <div style="margin-bottom:8px;"><span style="font-size:14pt;color:#9ecbff;"><strong>Project File</strong></span></div>
  <div style="margin-bottom:14px;"><span style="font-size:18pt;color:#ffffff;"><strong>{TEMPLATE_DISPLAY_NAME}</strong></span></div>
  <div style="margin-bottom:18px;line-height:1.7;"><span style="font-size:13pt;color:rgba(255,255,255,0.88);">{ONE_SENTENCE_DESCRIPTION}</span></div>
  <a href="https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/{TEMPLATE_FILENAME}"
     style="display:inline-block;background:#5f8fbf;color:#ffffff;text-decoration:none;padding:12px 22px;border-radius:999px;font-size:13pt;"><strong>&#11015; Download {TEMPLATE_FILENAME}</strong></a>
</div>
```

### D. Tips / Resources Card (optional)
For things like Google Image Search tips, glossary, video embed. Use the same accent treatment as the Overview card.

### E. How to Complete (orange section, scroll-boxed step cards)

Long instruction lists use the visible-affordance vertical scroll pattern from §13. The "Scroll for more" hint + bottom gradient fade work even in Canvas (where custom scrollbar styling is stripped).

```html
<div style="background:linear-gradient(180deg,rgba(255,107,26,0.22) 0%,rgba(255,107,26,0.08) 100%);border:1px solid rgba(255,107,26,0.3);border-left:6px solid #FF6B1A;border-radius:24px;padding:30px;margin-bottom:24px;">
  <div style="margin-bottom:8px;"><span style="font-size:14pt;color:#ff6b1a;"><strong>How to Complete Step {NN}</strong></span></div>
  <div style="margin-bottom:10px;"><span style="font-size:18pt;color:#ffffff;"><strong>Step-by-Step Instructions</strong></span></div>

  <!-- Scroll affordance: tells students there's more inside -->
  <div style="font-size:11pt;color:#ffb27c;margin-bottom:8px;opacity:0.85;">&#8595; Scroll inside the box to see all {N} steps</div>

  <!-- Scroll box with visible border and bottom-fade gradient for "more below" cue -->
  <div class="silva-scroll" style="max-height:480px;overflow-y:auto;padding:12px 14px 18px;border:1px solid rgba(255,107,26,0.18);border-radius:14px;background:linear-gradient(to bottom, rgba(0,0,0,0.18) 0%, rgba(0,0,0,0.18) 88%, rgba(255,107,26,0.18) 100%);">

    <!-- REPEAT THIS CARD PER STEP. Keep body under 60 words. -->
    <div style="background:rgba(0,0,0,0.32);border:1px solid rgba(255,107,26,0.2);border-left:4px solid #FF6B1A;border-radius:14px;padding:16px 18px;margin-bottom:12px;">
      <div style="margin-bottom:6px;"><span style="font-size:14pt;color:#ff6b1a;"><strong>{NN}. {STEP_TITLE}</strong></span></div>
      <div style="line-height:1.65;"><span style="font-size:13pt;color:rgba(255,255,255,0.90);">{STEP_BODY}</span></div>
    </div>

    <!-- last card uses margin-bottom:0 instead of 12px -->

  </div><!-- /silva-scroll -->
</div>
```

**Step card rules:**
- Number cards as `01.`, `02.`, `03.` (zero-padded).
- Body text under **60 words per card**. If longer, split into two cards.
- Use `<strong>` for filenames, menu commands, key actions.
- Use `<br />` only inside a single card's body when listing sub-bullets; never use `<br />` to space cards.
- Last card sets `margin-bottom:0` so the scroll box ends clean.
- Always include the `&#8595; Scroll inside the box...` hint above the scroll container so students know more content is below the fold.
- Always include the bottom-fade gradient in the scroll container background so users have a visual cue that content continues even when the OS scrollbar is hidden.
- The `silva-scroll` class hooks the styled scrollbar CSS in `silva-module.css` (visible on creativesilva.com; gracefully degrades in Canvas where custom scrollbars are stripped).

### F. What to Submit Card
```html
<div style="background:linear-gradient(180deg,rgba(255,107,26,0.22) 0%,rgba(255,107,26,0.08) 100%);border:1px solid rgba(255,107,26,0.3);border-left:6px solid #FF6B1A;border-radius:24px;padding:30px;">
  <div style="margin-bottom:8px;"><span style="font-size:14pt;color:#ffb27c;"><strong>What to Submit</strong></span></div>
  <div style="margin-bottom:14px;"><span style="font-size:18pt;color:#ffffff;"><strong>{SUBMISSION_HEADLINE}</strong></span></div>
  <div style="font-size:14pt;line-height:1.7;color:rgba(255,255,255,0.88);">{SUBMISSION_DETAILS}</div>
</div>
```

---

## 6. Asset Hosting Rules

All non-text assets must live in `/Users/riva/RIVA_CODE/creativesilva-site/assets/` and be committed to the repo.

**Naming:**
- Lowercase preferred but not required.
- No "copy" in filenames.
- Spaces are OK but must be URL-encoded as `%20` in src/href.
- Use descriptive names: `Jimenez_Mockups.ai` not `template.ai`.

**Image URLs always look like:**
```
https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/{FILENAME}
```

**PVHS logo (always use this exact URL):**
```
https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/PV%20LOGO%20NEW.png
```

**Workflow when user provides a new image:**
1. Confirm filename and that it's been added to `/assets/`.
2. Reference it via the full raw.githubusercontent URL.
3. Commit the asset together with the HTML page.

---

## 7. Bilingual Pattern

When Q5 = bilingual:
- English block has `id="top"` (which is also the Canvas-copy root).
- Spanish block has `id="espanol"` and lives **inside** the same `#top` div, separated by `border-top:2px solid rgba(255,255,255,0.10)`.
- Anchor toggles: EN header links `#espanol`, ES header links `#top`. Both update label text accordingly (`Clic para Español` vs `Back to English`).
- Spanish translations must be done with proper Spanish typography: use `&aacute;` `&eacute;` `&iacute;` `&oacute;` `&uacute;` `&ntilde;` `&iexcl;` `&iquest;`.
- Translate all section labels, titles, and body copy. Do not leave English text in the Spanish section.

---

## 8. Pre-Delivery Checklist (Run Before Committing)

Mental pass through the page. Every box must be true.

- [ ] Page title in `<head>` matches assignment.
- [ ] `--course-accent` in `:root` matches the chosen accent color.
- [ ] PVHS logo loads from the canonical raw URL.
- [ ] Hero overview image uses 52% width, no max-width cap, has shadow.
- [ ] Parent of every float-right image has `overflow:hidden`.
- [ ] Breadcrumb in title card matches the page's project context.
- [ ] No em dashes anywhere (search the file for `—` and `&mdash;`).
- [ ] All asset URLs use `raw.githubusercontent.com/creativesilva/creativesilva-site/main/...`.
- [ ] Smart quotes used in long-form copy.
- [ ] **Overview card contains exactly 6 vocabulary cards** in the responsive grid.
- [ ] **Vocabulary definitions read at 5th grade level** (under 15 words, plain language, no jargon).
- [ ] **All body copy and step instructions read at 5th grade level** (run the §12 sniff test).
- [ ] **Cards under 60 words.** If longer, split.
- [ ] Step section wrapped in scroll container with `&#8595; Scroll inside...` hint above AND bottom-fade gradient.
- [ ] Scroll container has `class="silva-scroll"` for styled scrollbar hook.
- [ ] Horizontal scroll rows (if used) have `&#8592; Swipe or scroll &#8594;` hint below.
- [ ] Last step card uses `margin-bottom:0`.
- [ ] `silvaCopyHTML()` and `silvaDownloadHTML()` script block present.
- [ ] `<script src="/js/silva-nav.js"></script>` present.
- [ ] Download filename in `silvaDownloadHTML()` matches page slug (e.g., `{slug}-canvas.html`).
- [ ] If bilingual: ES block exists, anchor toggles work both directions, **Spanish copy at 5th grade level** (use tú, simple verbs, no formal usted register), no English text leaked into ES.
- [ ] Entry added to `curriculum.html` for each course in Q2.

---

## 9. Git Workflow

```bash
cd /Users/riva/RIVA_CODE/creativesilva-site

# Stage the new page + any new assets + updated curriculum.html
git add curriculum/shared/{slug}.html \
        assets/{any-new-assets} \
        curriculum.html

# Commit with a clean message (no em dashes)
git commit -m "$(cat <<'EOF'
Add {Assignment Title} for {Project Name}

Bilingual Canvas page with {N} step cards, scroll-boxed instructions,
{HERO_IMAGE} hero, and {TEMPLATE_FILE} download. Linked from
curriculum.html for {COURSES}.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"

git push origin main
```

GitHub Pages deploy takes about 60 seconds. The page will be live at:
```
https://www.creativesilva.com/curriculum/shared/{slug}.html
```

---

## 10. Adding the Page to curriculum.html

For each course selected in Q2, add an entry to the appropriate course array in `curriculum.html`:

```javascript
{ course: "{course-slug}",
  name: "{Step NN}: {Short Title}",
  pages: 1,
  status: "published",
  url: "curriculum/shared/{slug}.html"
},
```

Course slugs in use: `da1b`, `da2b`, `photo1`, `photo2`, `yearbook`.

---

## 11. Reference Files

When in doubt, copy the structure from these proven builds:

| File | What it demonstrates |
|------|---------------------|
| `curriculum/shared/jimenez-step05-mockups.html` | Custom Client variant, bilingual, scroll-boxed steps, hero image, template download |
| `curriculum/shared/jimenez-spring-final.html` | Earlier Jimenez build (header pattern reference) |
| `css/silva-module.css` | All `.silva-*` class definitions |
| `js/silva-nav.js` | Site nav behavior (scroll, mobile menu) |

---

## 12. Writing Voice & Reading Level (5th Grade, EN + ES)

PVHS students read at a wide range of levels. Writing every assignment at a **5th grade reading level** means every student can succeed regardless of where they're at. This is not dumbing down: it's removing friction so the design challenge stays the focus.

### English: 5th grade rules

1. **Short sentences.** Aim for 12-15 words. Hard cap at 20.
2. **Plain words.** Use the everyday word, not the fancy one.
   - "use" not "utilize"
   - "help" not "facilitate"
   - "show" not "demonstrate"
   - "start" not "commence"
   - "make" not "construct"
   - "find" not "locate" or "identify"
   - "look at" not "examine"
   - "before" not "prior to"
   - "after" not "subsequent to"
   - "about" not "regarding"
3. **Active voice always.** "Open the file" not "The file should be opened."
4. **One idea per sentence.** Split compound sentences.
5. **Lead with the action.** "Click Save." not "It is important that you remember to click Save."
6. **No filler phrases.** Cut these on sight:
   - "It is important to note that..." → just say the thing
   - "In this assignment, students will..." → "You will..."
   - "Please be sure to..." → just give the instruction
   - "As mentioned previously..." → trust the reader
7. **Use "you" and "your".** Direct address. Treat the student as a person, not a category.
8. **Define jargon inline the first time.** "Embed the image (this means copy it into the file so it cannot break)."
9. **Numbers over words for steps.** "5 items" not "five items" when it's a count.
10. **Test it:** read the sentence out loud. If you stumble, rewrite it.

### Spanish: 5th grade rules (Santa Maria / Mexican Spanish register)

1. **Use tú, not usted.** Students are peers, not strangers. "Abre el archivo" not "Abra usted el archivo."
2. **Present indicative beats subjunctive.** "Necesitas hacer esto" not "Es necesario que hagas esto."
3. **Common verbs only.** hacer, ver, poner, abrir, guardar, escoger, encontrar, usar. Skip Latinate verbs.
4. **Short sentences.** Same 12-15 word target.
5. **Avoid passive constructions** with "se". "Guarda el archivo" not "El archivo se guarda."
6. **Cognates are your friend** for technical terms students already know in English: archivo, imagen, color, copia, salvar/guardar, exportar.
7. **Common kid-friendly words for definitions:**
   - "cosa" or "elemento" not "objeto"
   - "foto" not "imagen" when casual
   - "elegir" or "escoger" not "seleccionar"
   - "hacer" not "realizar" or "crear"
   - "ver" not "visualizar" or "observar"
8. **Use accents correctly.** `&aacute;` `&eacute;` `&iacute;` `&oacute;` `&uacute;` `&ntilde;` `&iexcl;` `&iquest;`.
9. **Regional flavor:** the Santa Maria community is largely Mexican-American. Lean Mexican Spanish (avoid Castilian "vosotros", avoid Argentine "vos"). When unsure, use neutral Latin American Spanish.

### Anti-bloat sniff test

Before committing, scan every card and ask:
- Could I cut this sentence and still get the point across? → Cut it.
- Does this card go over 60 words? → Split it.
- Am I explaining why before saying what to do? → Flip the order.
- Did I use a word a 5th grader wouldn't say at recess? → Swap it.
- Did I write "In this step, you will..." as a sentence opener? → Just start with the verb.

### Vocabulary words: how to pick the 6

The Overview's 6 vocab words are not a generic glossary. Each word must be:
- A term the student will actually encounter in the step cards or submission
- A word a 5th grader might not know yet
- Either a domain term (mockup, embed, vector) or a process term (preset, artboard, proof)
- Defined in under 15 words, in language that doesn't itself need definitions

Examples (Jimenez Step 05):
- **Mockup** — A fake photo of your design on a real item, like a shirt or sign.
- **Artboard** — One page inside an Illustrator file. One file can hold many.
- **Embed** — Copy an image into the file so it cannot break or go missing.
- **Vector** — A drawing made of lines and shapes, not dots, so it stays sharp at any size.
- **Preset** — A saved setup. You pick it once and it fills in all the right options.
- **Proof** — A practice version you show the client before the final.

Spanish translations should match the same plain register:
- **Mockup** — Una foto falsa de tu diseño en algo real, como una camisa o un letrero.
- **Mesa de trabajo** — Una página dentro de un archivo de Illustrator. Un archivo puede tener muchas.

---

## 13. Scroll & Overflow Patterns

Long content needs visible scroll cues. Default browser scrollbars are often invisible on dark backgrounds, and Canvas strips most custom scrollbar CSS. **Always pair scroll with a visible affordance** (hint text, gradient fade, or arrow).

### When to use vertical vs horizontal scroll

| Content type | Pattern | Why |
|--------------|---------|-----|
| Step-by-step instructions (6+ cards) | Vertical scroll box | Students read top to bottom, expect to scroll |
| FAQ / Q&A list | Vertical scroll box | Same reading flow |
| Vocabulary (exactly 6 words) | Responsive grid, NO scroll | 6 fits cleanly without overflow |
| Tips / "Did you know" | Vertical scroll if 5+ entries | Otherwise inline |
| Example image gallery (4+) | Horizontal scroll row | Visual content scans side to side |
| Comparison cards (before/after, A/B/C) | Horizontal scroll row | Side-by-side comparison is the point |
| Reference table (wide) | Horizontal scroll | Tables can't reflow narrow without breaking |
| Video embeds | NO scroll, stack vertically | Iframes don't scroll well inside scroll boxes |

### Vertical scroll box (canonical pattern)

Used in §5.E for step instructions. Repeated here for clarity.

```html
<!-- Hint above the scroll box -->
<div style="font-size:11pt;color:#ffb27c;margin-bottom:8px;opacity:0.85;">&#8595; Scroll inside the box to see all {N} steps</div>

<!-- The scroll box itself -->
<div class="silva-scroll" style="max-height:480px;overflow-y:auto;padding:12px 14px 18px;border:1px solid rgba(255,107,26,0.18);border-radius:14px;background:linear-gradient(to bottom, rgba(0,0,0,0.18) 0%, rgba(0,0,0,0.18) 88%, rgba(255,107,26,0.18) 100%);">
  <!-- cards here -->
</div>
```

Three visible affordances stacked:
1. **Text hint above** — tells students there's more inside, gives the count
2. **Bordered container** — makes the scroll boundary obvious
3. **Bottom gradient fade** — visual "more below" cue that works without scrollbar

### Horizontal scroll row (for galleries, comparison cards)

```html
<!-- Hint below the scroll row -->
<div style="overflow-x:auto;display:flex;gap:14px;padding:6px 2px 14px;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;border:1px solid rgba(95,143,191,0.18);border-radius:14px;background:rgba(0,0,0,0.18);">
  <div style="flex:0 0 260px;scroll-snap-align:start;background:rgba(0,0,0,0.32);border:1px solid rgba(95,143,191,0.22);border-radius:12px;padding:14px 16px;margin:8px 0 8px 8px;">
    <!-- card 1 content -->
  </div>
  <div style="flex:0 0 260px;scroll-snap-align:start;background:rgba(0,0,0,0.32);border:1px solid rgba(95,143,191,0.22);border-radius:12px;padding:14px 16px;margin:8px 0;">
    <!-- card 2 content -->
  </div>
  <!-- ...add gap on last card right side: margin:8px 8px 8px 0; -->
</div>
<div style="font-size:11pt;color:#9ecbff;opacity:0.75;text-align:center;margin-top:6px;">&#8592; Swipe or scroll to see more &#8594;</div>
```

Key inline styles for horizontal scroll:
- `overflow-x:auto` — enables horizontal scroll
- `display:flex; gap:14px` — lays cards in a row
- `scroll-snap-type:x mandatory` + `scroll-snap-align:start` on cards — snaps to each card
- `-webkit-overflow-scrolling:touch` — momentum scroll on iOS
- `flex:0 0 260px` on cards — fixed width per card (don't let them shrink)

### Styled scrollbar CSS (lives in `silva-module.css`)

The `silva-scroll` class hooks these styles. Visible on creativesilva.com preview; degrades gracefully in Canvas (Canvas strips custom scrollbar styles, falls back to OS default).

```css
.silva-scroll::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}
.silva-scroll::-webkit-scrollbar-track {
  background: rgba(255,255,255,0.04);
  border-radius: 5px;
}
.silva-scroll::-webkit-scrollbar-thumb {
  background: #5f8fbf;
  border-radius: 5px;
  border: 2px solid transparent;
  background-clip: padding-box;
}
.silva-scroll::-webkit-scrollbar-thumb:hover {
  background: #9ecbff;
  background-clip: padding-box;
  border: 2px solid transparent;
}
/* Firefox */
.silva-scroll {
  scrollbar-width: thin;
  scrollbar-color: #5f8fbf rgba(255,255,255,0.04);
}
```

If `silva-module.css` does not yet contain these rules, add them as part of the build.

### Rule of thumb on scroll height

- Vertical scroll: `max-height:480px` keeps about 3 cards visible at a time on desktop. Don't go over 540px (loses the "scroll me" feel).
- Horizontal scroll: don't fix height. Let cards size naturally. Cap visible width with the container.

---

## 14. Migrating Legacy Canvas Code to This Framework

When the user pastes outdated Canvas HTML and asks to upgrade it, follow this exact sequence. Do NOT try to surgically edit the old HTML. Build a fresh page using the framework and port the content in.

### Step 1: Parse the old code

Read the pasted code and extract:
- Project / client name
- Step number (if part of a series)
- Step / assignment title
- Overview paragraphs (often labeled "Description", "Introduction", or "Overview")
- Step-by-step instructions (often a `<ol>` or a series of `<h3>` blocks)
- Image references (note all `<img src="...">` URLs)
- Download links (any `<a href>` pointing to .ai, .psd, .pdf, .zip files)
- Submission requirements (often labeled "Deliverables", "Submit", "What to Turn In")
- Bilingual content (is there a `lang="es"` section, a "Español" anchor, or two separate language blocks?)

### Step 2: Run the intake questions from §1

Confirm with the user even if the old code answers most. Specifically ALWAYS ask:
- **Style variant** (Stock or Custom) — legacy code is often plain HTML with no theme; user choice matters here
- **6 vocabulary words** — almost no legacy page has these; you must collect them
- **Reading level confirmation** — legacy code is usually written for teachers, not students; confirm permission to rewrite at 5th grade level
- **Hero image** — old code may reference broken or Canvas-hosted images; confirm what to use

### Step 3: Extract and rewrite content

Pull copy from the old HTML and rewrite each chunk per §12. Do not paste old paragraphs verbatim. Mapping:

| Legacy section | New section |
|---------------|------------|
| Title / heading | §5.A Title Card |
| Overview / Description / Introduction | §5.B Overview Card body |
| (NEW — gather from user) | §5.B Vocabulary grid (6 words) |
| Downloads / Resources / Template | §5.C Project File Download |
| Tips / Notes / Hints | §5.D Tips Card |
| Instructions / Steps / Procedure | §5.E Step cards (renumber as 01., 02., 03.) |
| Deliverables / Submission / Turn In | §5.F What to Submit |

### Step 4: Migrate assets

For every image and downloadable file in the old HTML:
- If hosted at `canvas.instructure.com/files/...` or any Canvas URL, ask the user to provide the original file and add it to `/assets/`.
- If hosted at a third-party URL (Imgur, Dropbox, Google Drive), ask the user if it should be moved to `/assets/`. Default: yes.
- If already at `raw.githubusercontent.com/creativesilva/creativesilva-site/...`, keep as is.
- Rename any file containing "copy" in its name.

### Step 5: Build the new page

Create a fresh file at `curriculum/shared/{slug}.html`. Use the §4 outer scaffold. Drop the rewritten content into the §5 section templates. Do NOT try to preserve old inline styles, classes, or structure.

### Step 6: Add what was missing

Legacy pages are almost always missing all of these. Add them all:
- Title card with PV logo, breadcrumb, language toggle
- Vocabulary grid (6 cards) inside the Overview
- Scroll affordance ("Scroll inside..." hint + bottom gradient) on long instruction sections
- Spanish translation if bilingual was requested
- Copy/Download Canvas HTML buttons
- raw.githubusercontent URLs replacing all relative or Canvas-hosted image paths
- `silvaCopyHTML()` / `silvaDownloadHTML()` script block at the bottom
- `<script src="/js/silva-nav.js">` tag

### Step 7: Run the §8 Pre-Delivery Checklist

Every item must pass before commit.

### Step 8: Commit and push per §9

Use a commit message like: `Migrate {Project} {Step} from legacy Canvas HTML to framework`.

### Legacy code red flags to look for

When you see any of these in the pasted old HTML, treat it as a signal that a rewrite (not a patch) is the right move:

- `<table>` used for layout (instead of content tabular data)
- Inline `<font face="...">` or mixed font families
- Hard-coded pixel widths (`width="600"`) that won't reflow
- `<center>` or `<marquee>` tags (yes, they still show up)
- Em dashes everywhere (`—`, `&mdash;`)
- Canvas-hosted image URLs (`canvas.instructure.com/files/...`)
- Long unbroken paragraphs (over 80 words)
- Teacher-voice copy like "Students will be expected to demonstrate..."
- Passive voice throughout
- No vocabulary section
- No language toggle (even if school has bilingual students)
- Inline `style="font-family:Times..."` or other non-Arial fonts
- Buttons that link to "javascript:void(0)" or other dead handlers
- Images sized in absolute pixels with no `max-width` or `min-width`

### What NOT to do

- **Don't preserve the old layout** out of "respect" for the original. The whole point of the migration is to standardize.
- **Don't keep teacher-voice copy.** Rewrite it to student-voice at 5th grade level.
- **Don't try to make one giant Edit** to convert old HTML to new. Build fresh; port content in.
- **Don't skip the vocabulary cards** because the old code didn't have them. They are required.
- **Don't migrate without asking the user for the 6 vocab words.** You can suggest a starter set drawn from the content, but the teacher gets final say.

---

## 15. Common Mistakes to Avoid

1. **Capping the hero image with `max-width`.** Don't. It needs to scale.
2. **Forgetting `overflow:hidden` on a parent that contains a float-right image.** The next section will break layout.
3. **Putting `Step XX` twice** (once in the breadcrumb, once in the title). Pick one.
4. **Two-row headers.** Compact single-row only. Logo | breadcrumb+title centered | language toggle.
5. **Using em dashes.** Hard ban. Use colons or commas. Search `—` and `&mdash;` before commit.
6. **Forgetting the script block.** Without `silvaCopyHTML()` defined, the copy button silently fails.
7. **Linking to `/curriculum/digarts1/something.ai` instead of `/assets/something.ai`.** Canvas-pasted HTML can't resolve relative paths from a different course.
8. **Leaving "copy" in a filename** (e.g., `Jimenez_Mockups copy.ai`). Rename before committing.
9. **Skipping the Spanish translation** and just pasting English in the ES block. Either translate it properly or set Q5 = English-only.
10. **Bloated step cards.** If a card needs more than ~80 words, split it. Students will skim.

---

## 16. AI Image Disclaimer Footer (Required on Any Page Using AI Imagery)

Every page that uses AI-generated imagery must include a small disclaimer footer at the bottom of each language section. This addresses:

- Transparency about AI use (parents, students, admin)
- Known biases in AI image generators (body proportions, features, stereotypes)
- Distinguishing AI hero/staged photos from real student work on the same page
- Honest invitation for feedback

### When to include
- ✅ Any page with AI-generated photos of people (hero images, journal photos, staged scenes)
- ✅ Any page with AI-generated branding mockups, product staging, or composite imagery
- ❌ Pages that ONLY use real photos (e.g., About Mr. Silva using his actual headshot)
- ❌ Pages with no imagery at all

### Where to place
- Inside the EN language section: AFTER the last content card (typically "What to Submit" or "Begin Now"), BEFORE the closing `</div><!-- /English padding -->`
- Inside the ES language section: same position, mirrored
- Never in the title header card. Never above the fold.

### Wording (do NOT alter unless the teacher explicitly approves changes)

**English:**
```
The images on this page are AI-generated and do not show real students. AI tools can produce exaggerated body proportions, features, or other distortions that sometimes reflect biases built into the technology. All images are made to be school-appropriate. I keep working to improve the process. Questions and feedback welcome.
```

**Spanish:**
```
Las imágenes en esta página son generadas con IA y no muestran a estudiantes reales. Las herramientas de IA pueden producir proporciones del cuerpo exageradas, rasgos u otras distorsiones que a veces reflejan los sesgos de esta tecnología. Todas las imágenes son creadas para ser apropiadas para la escuela. Sigo trabajando para mejorar el proceso. Preguntas y comentarios son bienvenidos.
```

### HTML template (dark mode, swap accent color per page palette)

```html
<!-- AI Image Disclaimer -->
<div style="margin-top:24px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.10);">
  <div style="font-size:10pt;color:rgba(255,255,255,0.50);line-height:1.55;font-style:italic;">
    <span style="color:{ACCENT_LIGHT};font-style:normal;font-weight:bold;">&#9432;</span> The images on this page are AI-generated and do not show real students. AI tools can produce exaggerated body proportions, features, or other distortions that sometimes reflect biases built into the technology. All images are made to be school-appropriate. I keep working to improve the process. Questions and feedback welcome.
  </div>
</div>
```

For Spanish, swap the comment to `<!-- Aviso sobre Imágenes IA -->` and use the Spanish copy with proper HTML entities for accents.

### Accent color (the ⓘ icon)

| Page palette | `{ACCENT_LIGHT}` value |
|--------------|-----------------------|
| Photo 1B / Revisit (dark teal) | `#80e0e0` |
| Jimenez / Custom Client (dark blue) | `#9ecbff` |
| Sauce Baby (dark purple) | `#d9b3ff` |
| PVHS Stock (light teal page) | `#007474` (use solid teal, not light) |

### Styling rules

- **Tiny**: 10pt font size (smaller than body, larger than copyright fine print)
- **Subtle**: muted text color (50% opacity white on dark / 50% black on light)
- **Italic** body text to visually separate from main content
- **Bold non-italic icon** in the page's light-accent color for a small visual cue
- **Border-top divider** above to mark the boundary
- **Tucked**: never inside another card; sits as its own block at the very bottom

### Pre-commit check
Search the page for `AI Image Disclaimer` (EN comment) and `Aviso sobre Im&aacute;genes IA` (ES comment). Both must be present on AI-imagery pages. If either is missing, add it before commit.

---

**End of framework. If anything in a build doesn't match this doc, fix the build, not the doc.**
