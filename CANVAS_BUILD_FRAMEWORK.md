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
- No em dashes anywhere. Use colons, commas, or restructure the sentence.
- All images and downloadable files hosted at `raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/...` (never Canvas-hosted URLs, never relative paths).
- URL-encode spaces in asset paths as `%20`.
- Use smart quotes via HTML entities (`&#x2018;` `&#x2019;` `&#x201C;` `&#x201D;`) in copy.
- Page must include the copy/download script block AND the `<script src="/js/silva-nav.js">` tag.

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

### B. Overview Card (float-right hero image)
The hero image is the showcase. Width 52%, no max-width cap, strong shadow.

```html
<div style="background:linear-gradient(180deg,rgba(255,255,255,0.08) 0%,rgba(255,255,255,0.04) 100%);border:1px solid rgba(255,255,255,0.08);border-left:6px solid #5f8fbf;border-radius:24px;padding:30px;margin-bottom:24px;overflow:hidden;">
  <img src="https://raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/{HERO_IMAGE_FILENAME}"
       alt="{HERO_ALT_TEXT}"
       style="float:right;width:52%;min-width:220px;height:auto;border-radius:20px;margin:0 0 22px 30px;border:1px solid rgba(255,255,255,0.18);box-shadow:0 8px 40px rgba(0,0,0,0.6);" />
  <div style="margin-bottom:8px;"><span style="font-size:14pt;color:#9ecbff;"><strong>Step {NN} Overview</strong></span></div>
  <div style="margin-bottom:14px;"><span style="font-size:18pt;color:#ffffff;"><strong>What You Are Building</strong></span></div>
  <div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{OVERVIEW_PARAGRAPH_1}</span></div>
  <div style="margin-bottom:14px;line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{OVERVIEW_PARAGRAPH_2}</span></div>
  <div style="line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{OVERVIEW_PARAGRAPH_3}</span></div>
</div>
```

**Float-right rules:**
- Width as percentage (52%), `min-width:220px`, NO `max-width`. This makes it scale with the browser, never get cropped, never get tiny.
- Always add `box-shadow:0 8px 40px rgba(0,0,0,0.6)` for impact.
- Parent container needs `overflow:hidden` to clear the float.
- Margin `0 0 22px 30px` keeps body text from hugging the image.

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

```html
<div style="background:linear-gradient(180deg,rgba(255,107,26,0.22) 0%,rgba(255,107,26,0.08) 100%);border:1px solid rgba(255,107,26,0.3);border-left:6px solid #FF6B1A;border-radius:24px;padding:30px;margin-bottom:24px;">
  <div style="margin-bottom:8px;"><span style="font-size:14pt;color:#ff6b1a;"><strong>How to Complete Step {NN}</strong></span></div>
  <div style="margin-bottom:16px;"><span style="font-size:18pt;color:#ffffff;"><strong>Step-by-Step Instructions</strong></span></div>

  <div style="max-height:480px;overflow-y:auto;padding-right:6px;">

    <!-- REPEAT THIS CARD PER STEP. Update the title number and content. -->
    <div style="background:rgba(0,0,0,0.28);border:1px solid rgba(255,107,26,0.2);border-left:4px solid #FF6B1A;border-radius:18px;padding:18px 20px;margin-bottom:12px;">
      <div style="margin-bottom:8px;"><span style="font-size:14pt;color:#ff6b1a;"><strong>{NN}. {STEP_TITLE}</strong></span></div>
      <div style="line-height:1.7;"><span style="font-size:14pt;color:rgba(255,255,255,0.88);">{STEP_BODY}</span></div>
    </div>

    <!-- last card uses margin-bottom:0 instead of 12px -->

  </div><!-- /scroll -->
</div>
```

**Step card rules:**
- Number cards as `01.`, `02.`, `03.` (zero-padded).
- Keep body text under ~80 words per card; break long content into multiple cards.
- Use `<strong>` for filenames, menu commands, key actions.
- Use `<br />` only inside a single card's body when listing sub-bullets; never use `<br />` to space cards.
- Last card sets `margin-bottom:0` so the scroll box ends clean.

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
- [ ] Step section wrapped in `max-height:480px;overflow-y:auto` scroll box.
- [ ] Last step card uses `margin-bottom:0`.
- [ ] `silvaCopyHTML()` and `silvaDownloadHTML()` script block present.
- [ ] `<script src="/js/silva-nav.js"></script>` present.
- [ ] Download filename in `silvaDownloadHTML()` matches page slug (e.g., `{slug}-canvas.html`).
- [ ] If bilingual: ES block exists, anchor toggles work both directions, no English text leaked into ES.
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

## 12. Common Mistakes to Avoid

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

**End of framework. If anything in a build doesn't match this doc, fix the build, not the doc.**
