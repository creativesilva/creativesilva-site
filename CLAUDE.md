# CLAUDE.md

Project memory for Claude Code sessions working on `creativesilva-site`.

This file gets auto-loaded by Claude Code. Read it once at session start, then refer back to it (and to the docs it points to) whenever you're uncertain about conventions.

---

## What This Repo Is

`creativesilva-site` is the public GitHub Pages site at **www.creativesilva.com** owned by Chris Silva, a CTE teacher at Pioneer Valley High School (PVHS) in Santa Maria, CA. The site hosts:

- A public-facing portfolio + landing pages
- A `/curriculum.html` index of every Canvas assignment Chris has built
- Standalone Canvas assignment pages under `/curriculum/shared/` and `/curriculum/{course-slug}/` that get pasted into Canvas as HTML, OR linked from Canvas directly
- Asset library at `/assets/` (logos, mockup templates, hero images, downloadable AI/PSD files)

Domain is wired via the `CNAME` file (`www.creativesilva.com`). Deploys are pure GitHub Pages on the `main` branch. Push to `main`, wait ~60 seconds, change is live.

---

## The User (Chris)

- Teaches Digital Arts 1B, Digital Arts 2B, Photography 1, Photography 2, and Yearbook
- Bilingual classroom (Santa Maria has a large Mexican-American student population)
- Builds Canvas assignments by writing HTML pages on this site, then copying the rendered HTML into Canvas (or linking directly from Canvas)
- Works fast and expects polish: he's a designer, "good enough" is not good enough
- Trusts you to take creative control when he says so, but wants the structural conventions of the framework respected

When in doubt, ship clean, balanced, and minimal. Bloated copy and visual clutter are the two things he will push back on every time.

---

## Three Files You Must Know

1. **`CANVAS_BUILD_FRAMEWORK.md`** at the repo root. This is the single source of truth for building any new Canvas assignment page. Read it end-to-end before your first Canvas build of a session. It covers:
   - The intake questionnaire (10 questions to ask before building)
   - PVHS Stock vs Custom Client style variants with color tokens
   - **§3.5 Angular Gradient Framework (LOCKED)**: the current house style for Finals, study guides, quiz-prep, and test-intro pages. Use it verbatim.
   - Section-by-section HTML templates with placeholders
   - The required 6-vocab grid, scroll patterns, 5th grade reading rules
   - Migration guide for legacy Canvas code
   - Pre-delivery checklist and git workflow

   **`SILVA_ANGULAR_FRAMEWORK.md`** is the standalone, self-contained version of the locked angular style (same rules as §3.5, no legacy noise). It is the only doc offered on the public Build Resources card. When building in the current style, follow it.

2. **`css/silva-module.css`** — the only stylesheet the framework uses. Includes the site nav, page chrome, copy/download buttons, mobile rules, and the `silva-scroll` styled scrollbar. Edit cautiously; most pages depend on it.

3. **`js/silva-nav.js`** — site nav behavior. Every Canvas page loads it via `<script src="/js/silva-nav.js"></script>` at the bottom.

---

## Hard Rules (Apply Project-Wide, Not Just Canvas Builds)

These are non-negotiable. The user has flagged em dashes as a hard ban via global memory; the others come from accumulated feedback during builds.

1. **No em dashes.** Anywhere. Ever. Use colons, commas, parentheticals, or restructure the sentence. Applies to commit messages, code comments, copy, headings, everything. Before committing any file, mentally search for `—` and `&mdash;` and replace.
2. **Smart quotes via HTML entities** in long-form copy (`&#x2018;` `&#x2019;` `&#x201C;` `&#x201D;`).
3. **5th grade reading level** for all student-facing copy in both English and Spanish. See framework §12. This means short sentences, plain words, active voice, "you" not "the student".
4. **All assets hosted at `raw.githubusercontent.com/creativesilva/creativesilva-site/main/assets/...`**. Never use Canvas-hosted URLs. Never use relative paths in pages that get pasted into Canvas (the path won't resolve from inside Canvas).
5. **URL-encode spaces** in asset paths as `%20`.
6. **No filenames with "copy" in them** (e.g., `Jimenez_Mockups copy.ai`). Rename before committing.
7. **No `.env` files, no credentials, no secrets.** Standard.

---

## Canvas Build Workflow (The Common Task)

When the user asks for a new Canvas assignment page, follow this exact path. Don't improvise; the user has iterated on this pattern many times and it works.

1. **Read `CANVAS_BUILD_FRAMEWORK.md`** if you haven't already this session.
2. **Run the intake questionnaire** from framework §1. Use a single batched `AskUserQuestion` call when possible. Don't skip the 6-vocab-word question; it's required and easy to forget.
3. **Build the page** using the §4 outer scaffold and §5 section templates. Drop content into the placeholders.
4. **Run the §8 Pre-Delivery Checklist** mentally before commit.
5. **Add the page to `curriculum.html`** for each course the user named (course slugs: `da1b`, `da2b`, `photo1`, `photo2`, `yearbook`).
6. **Commit and push** per framework §9. Page is live at `https://www.creativesilva.com/curriculum/shared/{slug}.html` in ~60 seconds.

If the user pastes legacy Canvas HTML and asks you to upgrade it, follow framework §14 (rebuild, don't patch).

---

## Reference Builds (Crib From These)

When you need to see how a section actually looks in practice:

| File | Demonstrates |
|------|-------------|
| `curriculum/shared/da-finals-quiz-prep.html` | **MASTER for the current locked Angular Gradient style.** Translucent cards with gradient border-image frames + solid top-stripe children, uniform section-colored buttons, eyebrow chips, bilingual EN/ES mirror. Generated by `tools/build-da-finals.py`. Crib from this for any new Finals/study-guide/quiz page. |
| `curriculum/shared/jimenez-step05-mockups.html` | Legacy Custom Client build (older dark theme). Reference only for migration; do not copy its border/button style into new angular pages. |
| `curriculum/shared/jimenez-spring-final.html` | Earlier Jimenez build (legacy header pattern, for migration reference) |

If you're building in the current style, diff against `da-finals-quiz-prep.html` and follow `SILVA_ANGULAR_FRAMEWORK.md` / framework §3.5.

---

## Git Workflow

- Commit only when the user asks. Never auto-commit. If unclear, ask.
- Always create new commits; never `--amend` unless explicitly requested.
- Never force push.
- Never `--no-verify` on hooks unless the user asks.
- Use `HEREDOC` for commit messages so multi-line formatting survives:
  ```bash
  git commit -m "$(cat <<'EOF'
  Short subject line under 70 chars

  Optional longer body explaining the why, not just the what.

  Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
  EOF
  )"
  ```
- Co-author tag on every commit Claude makes.
- Push immediately after commit when working on Canvas pages — Chris is usually waiting to paste the code into Canvas.

---

## Common Pitfalls In This Repo Specifically

Things you'll probably get wrong on a first attempt unless warned:

1. **Forgetting the `<script>` block** at the bottom of a Canvas page. Without `silvaCopyHTML()` and `silvaDownloadHTML()` defined inline, the Copy/Download buttons silently do nothing. Always include the script block (see framework §4) AND `<script src="/js/silva-nav.js"></script>`.
2. **Capping the hero image with `max-width`.** Don't. The hero is the showcase; let it scale. Use `width:52%; min-width:220px` and no max.
3. **Forgetting `overflow:hidden`** on the parent container of a float-right image. The next section will collapse into the float and break layout.
4. **Adding the page to `curriculum.html` but forgetting to add it for the second course.** Many assignments link from both Digital Arts 1B and 2B. Check.
5. **Writing teacher-voice copy.** "Students will demonstrate..." → rewrite to "You will...". Lead with the action.
6. **Using `WidthType.PERCENTAGE` in docx-js** (if you ever build a Word doc). Always use DXA. Percentages break in Google Docs.
7. **Mixing PVHS green/teal with the dark Custom Client theme.** Pick one variant per page and commit to it.

---

## When To Push Back

The user trusts you to flag issues, not just execute orders. Push back (politely, briefly) when:

- He asks for something that would violate a hard rule (em dashes, Canvas-hosted URLs, etc.)
- A request would visibly bloat a page he just asked to tighten
- A change would break a reference build's structural pattern
- He asks you to commit something that wasn't actually verified to work

Don't push back on:
- Aesthetic preferences (he's the designer, his call)
- Reordering content
- Adding/removing sections
- Anything stylistic that doesn't violate the framework

---

## Personal Context (From Global Memory)

Chris and Laura Silva are teachers in Santa Maria. They have ongoing financial planning conversations that may surface in adjacent projects; that context belongs in the Financials directory, not here. Keep work in `creativesilva-site` focused on teaching and the public site.

Today's date and other live state come from the session injection; don't hard-code dates in code or docs.

---

## Quick Sanity Check Before Ending A Build Session

Run through this in your head:

- [ ] Did I read the framework doc?
- [ ] Did I ask the intake questions, including the 6 vocab words?
- [ ] Is the page live? Did I check the curriculum.html link?
- [ ] Did I push to main?
- [ ] Are there any em dashes in what I just wrote?
- [ ] Does the user know how to paste it into Canvas (Copy Canvas HTML button works)?

If all yes, you're done. If any no, fix it before signing off.

---

**End of Claude project memory. For Canvas-build specifics, defer to `CANVAS_BUILD_FRAMEWORK.md`.**
