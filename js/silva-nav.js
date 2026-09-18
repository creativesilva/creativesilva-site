/**
 * silva-nav.js
 *
 * Responsibilities:
 *
 * 1. MODULES is the authoritative grouping of every published curriculum page,
 *    one inner array per module (in reading order). SEQUENCE is the flat list
 *    derived from it.
 *
 * 2. Injects an Amazon-style page pager at the bottom of every module page:
 *      < Previous   0  1  2 ... N   Next >
 *    The numbers are the pages of the CURRENT module (0 = overview/intro,
 *    1 = step one, and so on), with Amazon-style truncation when a module has
 *    many pages. Previous jumps to the module before this one, Next to the
 *    module after. Both gray out at the ends. Pager lives outside #top, so it
 *    is website-only and never copied into Canvas.
 *
 * 3. Each pager includes its own COPY HTML button at the right. The top
 *    pager replaces the old toolbar buttons (Copy, Download) and step-nav.
 *    Also injects a hamburger button for mobile.
 *
 * To add a page: drop its path into the right MODULES group, in order.
 */

(function () {
  // ===== Top-left "Curriculum Catalog" dropdown menu (teacher navigation) =====
  // Active courses -> their modules -> the module's OVERVIEW url (first page).
  // TO ADD A MODULE TO THE MENU: add a line to the right course's `modules` list.
  // This is the single source for the dropdown; keep it in sync with new modules.
  var MENU = [
    { course: 'Digital Arts 1A', modules: [
      { name: 'Pictograms',          url: '/curriculum/shared/digarts1-pictograms-overview.html' },
      { name: 'Color Theory',        url: '/curriculum/shared/digarts1-color-theory-overview.html' },
      { name: 'Sketchbook Cover Art', url: '/curriculum/shared/digarts1-sketchbook-cover-overview.html' },
      { name: 'Motivational Poster', url: '/curriculum/shared/digarts1-motivational-poster-overview.html' },
      { name: 'Live Stream Graphic',  url: '/curriculum/shared/digarts1-live-stream-graphic-overview.html' }
    ]},
    { course: 'Photography 1A', modules: [
      { name: 'Self-Portrait',            url: '/curriculum/shared/photo1-self-portrait-overview.html' },
      { name: 'Composition Concepts',     url: '/curriculum/shared/photo1-composition-concepts-overview.html' },
      { name: 'Leading Lines Photo Walk', url: '/curriculum/shared/photo1-leading-lines-overview.html' },
      { name: 'Image Series Photo Walk',  url: '/curriculum/shared/photo1-image-series-overview.html' },
      { name: 'Lightroom Editing',        url: '/curriculum/shared/photo1-lightroom-editing-overview.html' }
    ]},
    { course: 'Photography 2A', modules: [
      { name: 'Composition Photo Walk', url: '/curriculum/shared/photo2-composition-overview.html' },
      { name: 'Off-Camera Flash',       url: '/curriculum/shared/photo2-ocf-overview.html' },
      { name: 'Studio Session',         url: '/curriculum/shared/photo2-studio-session-overview.html' },
      { name: 'Build Your Own Preset',  url: '/curriculum/shared/photo2-preset-overview.html' }
    ]}
  ];

  var MODULES = [
    // Universal / shared single pages
    ['/curriculum/universal/about-mr-silva.html'],
    ['/curriculum/shared/awards-pizza-party.html'],
    ['/curriculum/shared/tech-overview.html'],

    // MRC: Summer Digital Arts 1A (Mark Richardson Center)
    ['/curriculum/mrc/digital-arts-1a-home.html'],
    ['/curriculum/mrc/about-mr-silva.html'],
    ['/curriculum/mrc/course-objectives.html'],
    ['/curriculum/mrc/athlete-poster-assignment.html',
     '/curriculum/mrc/athlete-poster-step01.html'],
    ['/curriculum/mrc/pictographs-overview.html',
     '/curriculum/mrc/pictographs-step01-capture.html',
     '/curriculum/mrc/pictographs-step02-sketch.html',
     '/curriculum/mrc/pictographs-step03-digital.html',
     '/curriculum/mrc/pictographs-step04-reflection.html'],
    ['/curriculum/mrc/logo-redesign-overview.html',
     '/curriculum/mrc/logo-redesign-step01-thumbnails.html',
     '/curriculum/mrc/logo-redesign-step02-final-sketch.html',
     '/curriculum/mrc/logo-redesign-step03-digital.html'],
    ['/curriculum/mrc/scavenger-hunt-overview.html',
     '/curriculum/mrc/scavenger-hunt-step01-hunt.html'],
    ['/curriculum/mrc/panorama-overview.html',
     '/curriculum/mrc/panorama-step01-capture.html',
     '/curriculum/mrc/panorama-step02-merge.html',
     '/curriculum/mrc/panorama-step03-reflection.html'],
    ['/curriculum/mrc/tvav-overview.html',
     '/curriculum/mrc/tvav-step01-capture.html',
     '/curriculum/mrc/tvav-step02-edit.html',
     '/curriculum/mrc/tvav-step03-reflection.html'],
    ['/curriculum/mrc/magcover-overview.html',
     '/curriculum/mrc/magcover-step01-plan.html',
     '/curriculum/mrc/magcover-step02-capture.html',
     '/curriculum/mrc/magcover-step03-design.html',
     '/curriculum/mrc/magcover-step04-reflection.html'],
    ['/curriculum/mrc/movieposter-overview.html',
     '/curriculum/mrc/movieposter-step01-plan.html',
     '/curriculum/mrc/movieposter-step02-capture.html',
     '/curriculum/mrc/movieposter-step03-design.html',
     '/curriculum/mrc/movieposter-step04-reflection.html'],
    ['/curriculum/mrc/double-exposure-overview.html',
     '/curriculum/mrc/double-exposure-step01-create.html'],
    ['/curriculum/mrc/cereal-box-introduction.html',
     '/curriculum/mrc/cereal-box-elements-of-art.html',
     '/curriculum/mrc/cereal-box-step01-research.html',
     '/curriculum/mrc/cereal-box-step02-sketchbook.html',
     '/curriculum/mrc/cereal-box-step03-design.html',
     '/curriculum/mrc/cereal-box-step04-sketch.html',
     '/curriculum/mrc/cereal-box-step05-digital.html',
     '/curriculum/mrc/cereal-box-step06-social-media.html',
     '/curriculum/mrc/cereal-box-step07-reflection.html'],

    // Course homes
    ['/curriculum/digarts1/digarts1b-home.html'],
    ['/curriculum/digarts2/digarts2b-home.html'],
    ['/curriculum/photo1/photo1b-home.html'],

    // Cross-course resources
    ['/curriculum/shared/photo-course-resources.html'],

    // Photography 1B: Final Exam Study Materials
    ['/curriculum/shared/photo1b-finals-quiz-prep.html',
     '/curriculum/shared/photo1b-spring-final-quiz-intro.html',
     '/curriculum/shared/photo1b-spring-final-silva-intro.html'],

    // Photo 1B: Sauce Baby (commercial photography final)
    ['/curriculum/photo1/sauce-baby/creative-brief.html',
     '/curriculum/photo1/sauce-baby/overview.html',
     '/curriculum/photo1/sauce-baby/step1-mood-board.html',
     '/curriculum/photo1/sauce-baby/step2-planning.html',
     '/curriculum/photo1/sauce-baby/step3-shoot-contact.html',
     '/curriculum/photo1/sauce-baby/step4-final-edits.html',
     '/curriculum/photo1/sauce-baby/step5-reflection.html',
     '/curriculum/photo1/sauce-baby/sauce-baby-bonus-vote.html'],

    // Photo 1B: The Revisit Project (end-of-year)
    ['/curriculum/shared/revisit-project-overview.html',
     '/curriculum/shared/revisit-step01-capture.html',
     '/curriculum/shared/revisit-step02-edit.html',
     '/curriculum/shared/revisit-step03-reflection.html'],

    // Digital Arts: Final Exam Study Materials
    ['/curriculum/shared/da-finals-quiz-prep.html',
     '/curriculum/shared/da-spring-final-intro.html'],

    // Digital Arts: Cereal Box Group Project
    ['/curriculum/shared/cereal-box-introduction.html',
     '/curriculum/shared/cereal-box-elements-of-art.html',
     '/curriculum/shared/cereal-box-step01-research.html',
     '/curriculum/shared/cereal-box-step02-sketchbook.html',
     '/curriculum/shared/cereal-box-step03-design.html',
     '/curriculum/shared/cereal-box-step04-sketch.html',
     '/curriculum/shared/cereal-box-step05-digital.html',
     '/curriculum/shared/cereal-box-step06-reflection.html'],

    // Digital Arts: Company Branding (prep module)
    ['/curriculum/shared/branding-introduction.html',
     '/curriculum/shared/branding-step01-research.html',
     '/curriculum/shared/branding-step02-chat.html',
     '/curriculum/shared/branding-step03-sketch.html',
     '/curriculum/shared/branding-step04-digital.html',
     '/curriculum/shared/branding-step05-mockup.html'],

    // Digital Arts: Jimenez Mobile Detailing (spring final)
    ['/curriculum/shared/jimenez-spring-final.html',
     '/curriculum/shared/jimenez-step01-research.html',
     '/curriculum/shared/jimenez-step02-sketches.html',
     '/curriculum/shared/jimenez-step03-feedback.html',
     '/curriculum/shared/jimenez-step04-illustrator.html',
     '/curriculum/shared/jimenez-step05-mockups.html',
     '/curriculum/shared/jimenez-step06-social-media.html',
     '/curriculum/shared/jimenez-step07-reflection.html',
     '/curriculum/shared/jimenez-bonus-vote.html'],

    // ── Active teaching catalog: Digital Arts 1A -> Photography 1A -> Photography 2A ──
    // Ordered to match the curriculum catalog so the pager's Prev/Next walk the whole
    // course both ways: each course opens with a "Course Pages" group (Home, Overview,
    // Syllabus, + Resources where it exists) that behaves like module 0, then its modules.
    // ACTIVE_FIRST/ACTIVE_LAST (computed below) bound this walkable span. Kept last.
    ['/curriculum/digarts1/digarts1a-home.html',
     '/curriculum/digarts1/digarts1a-course-overview.html',
     '/curriculum/digarts1/digarts1a-syllabus.html'],
    ['/curriculum/shared/digarts1-pictograms-overview.html',
     '/curriculum/shared/digarts1-pictograms-step01-find-save.html',
     '/curriculum/shared/digarts1-pictograms-step02-sketch-reflect.html'],
    ['/curriculum/shared/digarts1-color-theory-overview.html',
     '/curriculum/shared/digarts1-color-theory-step01-analysis.html'],
    ['/curriculum/shared/digarts1-sketchbook-cover-overview.html',
     '/curriculum/shared/digarts1-sketchbook-cover-step01-design.html',
     '/curriculum/shared/digarts1-sketchbook-cover-step02-submit-reflect.html'],
    ['/curriculum/shared/digarts1-motivational-poster-overview.html',
     '/curriculum/shared/digarts1-motivational-poster-step01.html',
     '/curriculum/shared/digarts1-motivational-poster-step02.html',
     '/curriculum/shared/digarts1-motivational-poster-step03.html'],
    ['/curriculum/shared/digarts1-live-stream-graphic-overview.html',
     '/curriculum/shared/digarts1-live-stream-graphic-step01.html',
     '/curriculum/shared/digarts1-live-stream-graphic-step02-inspiration.html',
     '/curriculum/shared/digarts1-live-stream-graphic-step03-design.html',
     '/curriculum/shared/digarts1-live-stream-graphic-step04-reflection.html'],
    ['/curriculum/photo1/photo1a-home.html',
     '/curriculum/photo1/photo1a-course-overview.html',
     '/curriculum/photo1/photo1a-syllabus.html',
     '/curriculum/shared/photo1a-course-resources.html'],
    ['/curriculum/shared/photo1-self-portrait-overview.html',
     '/curriculum/shared/photo1-self-portrait-step01-capture.html',
     '/curriculum/shared/photo1-self-portrait-step02-reflection.html'],
    ['/curriculum/shared/photo1-composition-concepts-overview.html',
     '/curriculum/shared/photo1-composition-concepts-step01-capture.html',
     '/curriculum/shared/photo1-composition-concepts-step02-reflection.html'],
    ['/curriculum/shared/photo1-leading-lines-overview.html',
     '/curriculum/shared/photo1-leading-lines-step01-capture.html',
     '/curriculum/shared/photo1-leading-lines-step02-reflection.html'],
    ['/curriculum/shared/photo1-image-series-overview.html',
     '/curriculum/shared/photo1-image-series-step01-capture-import.html',
     '/curriculum/shared/photo1-image-series-step02-cull-edit.html',
     '/curriculum/shared/photo1-image-series-step03-reflection.html'],
    ['/curriculum/shared/photo1-lightroom-editing-overview.html',
     '/curriculum/shared/photo1-lightroom-editing-step01-cull-export.html',
     '/curriculum/shared/photo1-lightroom-editing-step02-reflection.html'],
    ['/curriculum/photo2/photo2a-home.html',
     '/curriculum/photo2/photo2a-course-overview.html',
     '/curriculum/photo2/photo2a-syllabus.html'],
    ['/curriculum/shared/photo2-composition-overview.html',
     '/curriculum/shared/photo2-composition-step01-photowalk.html',
     '/curriculum/shared/photo2-composition-step02-cull-export.html',
     '/curriculum/shared/photo2-composition-step03-reflection.html'],
    ['/curriculum/shared/photo2-ocf-overview.html',
     '/curriculum/shared/photo2-ocf-step01-inspiration.html',
     '/curriculum/shared/photo2-ocf-step02-photowalk.html',
     '/curriculum/shared/photo2-ocf-step03-reflection.html'],
    ['/curriculum/shared/photo2-studio-session-overview.html',
     '/curriculum/shared/photo2-studio-session-step01-capture.html',
     '/curriculum/shared/photo2-studio-session-step02-cull-edit.html',
     '/curriculum/shared/photo2-studio-session-step03-reflection.html'],
    ['/curriculum/shared/photo2-preset-overview.html',
     '/curriculum/shared/photo2-preset-step01-photowalk.html',
     '/curriculum/shared/photo2-preset-step02-edit-preset.html',
     '/curriculum/shared/photo2-preset-step03-deliver.html',
     '/curriculum/shared/photo2-preset-step04-reflection.html']
  ];

  var SEQUENCE = [];
  for (var m = 0; m < MODULES.length; m++) {
    for (var p = 0; p < MODULES[m].length; p++) { SEQUENCE.push(MODULES[m][p]); }
  }

  // Expose the page grouping so other pages (the curriculum catalog) can list a
  // module's pages without duplicating the data. Read-only convenience mirror.
  try { window.SILVA_MODULES = MODULES; } catch (e) {}

  function samePath(a, b) {
    return a === b || a === b.replace(/^\//, '') || ('/' + a) === b;
  }

  function locate() {
    var path = window.location.pathname;
    for (var i = 0; i < MODULES.length; i++) {
      for (var j = 0; j < MODULES[i].length; j++) {
        if (samePath(path, MODULES[i][j])) { return { g: i, p: j }; }
      }
    }
    return null;
  }

  // The active teaching span (Digital Arts 1A Course Pages ... Photography 2A last step).
  // Inside it, Prev/Next chain across group boundaries so you can walk the whole course,
  // and course-to-course, both ways. Outside it (legacy pages), behavior is unchanged.
  function groupIndexOf(url) {
    for (var i = 0; i < MODULES.length; i++) {
      for (var j = 0; j < MODULES[i].length; j++) {
        if (samePath(MODULES[i][j], url)) { return i; }
      }
    }
    return -1;
  }
  var ACTIVE_FIRST = groupIndexOf('/curriculum/digarts1/digarts1a-home.html');
  var ACTIVE_LAST = groupIndexOf('/curriculum/shared/photo2-preset-step04-reflection.html');
  function inActive(g) { return ACTIVE_FIRST !== -1 && g >= ACTIVE_FIRST && g <= ACTIVE_LAST; }

  // Amazon-style page window: show all when small, else first/last plus a
  // 3-wide window around the current page, with ellipsis for the gaps.
  function pageWindow(total, cur) {
    var out = [];
    if (total <= 7) {
      for (var i = 0; i < total; i++) { out.push(i); }
      return out;
    }
    var keep = {};
    [0, total - 1, cur - 1, cur, cur + 1].forEach(function (n) {
      if (n >= 0 && n < total) { keep[n] = true; }
    });
    var nums = Object.keys(keep).map(Number).sort(function (a, b) { return a - b; });
    for (var k = 0; k < nums.length; k++) {
      out.push(nums[k]);
      if (k < nums.length - 1 && nums[k + 1] - nums[k] > 1) { out.push('gap'); }
    }
    return out;
  }

  function buildPager() {
    var at = locate();
    if (!at) { return null; }
    var mod = MODULES[at.g];

    var pager = document.createElement('nav');
    pager.className = 'silva-pager';
    pager.setAttribute('aria-label', 'Module page navigation');

    // Previous: the step before this one. On page 0, inside the active span, hand
    // back to the previous group's last page (previous module, or the course's
    // Course Pages, or the previous course) so you can walk the whole course back.
    var prevHref = null, prevLabel = '&#8249;&nbsp; Previous';
    if (at.p > 0) {
      prevHref = mod[at.p - 1];
    } else if (inActive(at.g) && at.g > ACTIVE_FIRST) {
      var pmod = MODULES[at.g - 1];
      prevHref = pmod[pmod.length - 1];
      prevLabel = '&#8249;&nbsp; Previous Module';
    }
    var prev = document.createElement(prevHref ? 'a' : 'span');
    prev.className = 'pg-edge pg-prev' + (prevHref ? '' : ' pg-disabled');
    if (prevHref) { prev.href = prevHref; }
    prev.innerHTML = prevLabel;
    pager.appendChild(prev);

    // Page numbers (only meaningful when the module has more than one page)
    if (mod.length > 1) {
      pageWindow(mod.length, at.p).forEach(function (n) {
        if (n === 'gap') {
          var dots = document.createElement('span');
          dots.className = 'pg-ellipsis';
          dots.textContent = '…';
          pager.appendChild(dots);
          return;
        }
        var isCur = n === at.p;
        var num = document.createElement(isCur ? 'span' : 'a');
        num.className = 'pg-num' + (isCur ? ' active' : '');
        if (!isCur) { num.href = mod[n]; }
        num.textContent = n;
        num.setAttribute('title', n === 0 ? 'Overview' : 'Step ' + n);
        if (isCur) { num.setAttribute('aria-current', 'page'); }
        pager.appendChild(num);
      });
    }

    // Next: the next step in this module. On the last step, hand off to the next
    // group's first page (labeled "Next Module"). Inside the active span this is
    // bounded by ACTIVE_LAST so the final step ends cleanly; outside, unchanged.
    var atLast = at.p >= mod.length - 1;
    var nextHref = null, nextLabel = 'Next &nbsp;&#8250;';
    if (!atLast) { nextHref = mod[at.p + 1]; }
    else if (inActive(at.g)) {
      if (at.g < ACTIVE_LAST) { nextHref = MODULES[at.g + 1][0]; nextLabel = 'Next Module &nbsp;&#8250;'; }
    } else if (at.g < MODULES.length - 1) { nextHref = MODULES[at.g + 1][0]; nextLabel = 'Next Module &nbsp;&#8250;'; }
    var next = document.createElement(nextHref ? 'a' : 'span');
    next.className = 'pg-edge pg-next' + (nextHref ? '' : ' pg-disabled');
    if (nextHref) { next.href = nextHref; }
    next.innerHTML = nextLabel;
    pager.appendChild(next);

    pager.appendChild(makeUrlBtn());
    pager.appendChild(makeCopyBtn());
    return pager;
  }

  // COPY HTML: the rightmost pager pill, sits just right of COPY URL.
  function makeCopyBtn() {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'pg-copy';
    b.textContent = 'COPY HTML';
    b.addEventListener('click', function () {
      var el = document.getElementById('top');
      if (!el) { return; }
      navigator.clipboard.writeText(el.outerHTML).then(function () {
        b.textContent = '✓ Copied!';
        b.classList.add('copied');
        setTimeout(function () { b.textContent = 'COPY HTML'; b.classList.remove('copied'); }, 2500);
      }).catch(function () { alert('Copy failed. Try selecting the page source manually.'); });
    });
    return b;
  }

  // COPY URL: same pager pill and same .pg-copy shape/style as COPY HTML, just left of it.
  function makeUrlBtn() {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'pg-copy';
    b.textContent = 'COPY URL';
    b.addEventListener('click', function () {
      navigator.clipboard.writeText(location.href).then(function () {
        b.textContent = '✓ Copied!';
        b.classList.add('copied');
        setTimeout(function () { b.textContent = 'COPY URL'; b.classList.remove('copied'); }, 2500);
      }).catch(function () { alert('Copy failed. Copy the address bar manually.'); });
    });
    return b;
  }

  // BUILD: quick jump to Build Resources in the catalog. Same accent pill as COPY URL /
  // COPY HTML, placed just left of COPY URL. Teacher-only, like the copy pills: it is
  // JS-injected, so it never lands in the HTML pasted into Canvas.
  function makeBuildBtn() {
    var a = document.createElement('a');
    a.className = 'pg-copy pg-build';
    a.textContent = 'BUILD';
    a.href = 'https://www.creativesilva.com/curriculum.html#build-resources';
    a.title = 'Go to Build Resources';
    return a;
  }

  // ===== Unified header on module pages (teacher-only, outside #top). =====
  // The SAME two-row header the catalog home shows, so there is ONE header sitewide:
  //   Row 1 (titlebar): CURRICULUM CATALOG title + CALENDAR + search.
  //   Row 2 (catbar):   CS logo + CATALOG dropdown + BUILD RESOURCES + the module
  //                     pager (Prev/Next + page numbers + BUILD / COPY URL / COPY HTML).
  // The pager and copy pills are the "internal module navigation": they only appear
  // here, on a loaded module page, never on the catalog home. Search jumps to the
  // catalog and runs there (a module page has no catalog index to search).

  // Row 1: big title (links back to the catalog), Calendar button, catalog search.
  function buildTitlebar() {
    var bar = document.createElement('div');
    bar.className = 'silva-uni-titlebar';

    // The title reflects the loaded page: the module/step title (first segment of the page
    // <title>), linked back to that module's overview. Falls back to the catalog name.
    var title = document.createElement('a');
    title.className = 'silva-uni-title';
    var at = locate();
    title.href = at ? ('/' + MODULES[at.g][0].replace(/^\//, '')) : '/curriculum.html';
    var docTitle = (document.title || '').split('|')[0].trim();
    title.textContent = docTitle || 'Curriculum Catalog';
    bar.appendChild(title);

    var cal = document.createElement('a');
    cal.className = 'silva-uni-cal';
    cal.href = '/calendar.html';
    cal.textContent = 'Calendar';
    bar.appendChild(cal);

    // Search Catalog button: module/calendar pages have no catalog index, so it opens the
    // catalog home with its search shadow-box already open (?search=1).
    var searchBtn = document.createElement('a');
    searchBtn.className = 'silva-uni-searchbtn';
    searchBtn.href = '/curriculum.html?search=1';
    searchBtn.textContent = 'Search';
    searchBtn.setAttribute('aria-label', 'Search the catalog');
    bar.appendChild(searchBtn);

    // Rolling class-period countdown (live from the pvhs_tools schedule), top-right by search.
    var clock = document.createElement('iframe');
    clock.className = 'silva-uni-clock';
    clock.src = '/assets/embeds/period-clock.html';
    clock.title = 'Class period countdown';
    clock.setAttribute('scrolling', 'no');
    clock.setAttribute('loading', 'lazy');
    bar.appendChild(clock);
    return bar;
  }

  // Row 2: CS logo + one "Catalog" dropdown (all courses -> modules) + Build Resources,
  // then the module pager pushed to the right (module pages only).
  function buildCatalogRow() {
    var bar = document.createElement('div');
    bar.className = 'silva-uni-bar';

    var logo = document.createElement('a');
    logo.className = 'silva-uni-logo';
    logo.href = '/index.html';
    logo.setAttribute('aria-label', 'creativesilva.com');
    logo.innerHTML = '<img src="/logos/CS_Logo_Only_Teal.svg" alt="Chris Silva" />';
    bar.appendChild(logo);

    var cat = document.createElement('div');
    cat.className = 'silva-uni-cat';
    var trigger = document.createElement('button');
    trigger.type = 'button';
    trigger.className = 'silva-uni-cattrigger';
    trigger.setAttribute('aria-haspopup', 'true');
    trigger.setAttribute('aria-expanded', 'false');
    trigger.innerHTML = 'Catalog <span class="silva-uni-caret">&#9662;</span>';
    var menu = document.createElement('div');
    menu.className = 'silva-uni-catmenu';
    // First item: a "Main Catalog" back-link to the master catalog (return point from any page).
    var catMain = document.createElement('a');
    catMain.href = '/curriculum.html';
    catMain.className = 'silva-uni-catmod silva-uni-catmain';
    catMain.innerHTML = '&#8592;&nbsp; Main Catalog';
    menu.appendChild(catMain);
    var catTeacher = document.createElement('a');
    catTeacher.href = 'https://www.creativesilva.com/curriculum.html#teacher-resources';
    catTeacher.className = 'silva-uni-catmod silva-uni-catteacher';
    catTeacher.textContent = 'Teacher Resources';
    menu.appendChild(catTeacher);
    var catBuildR = document.createElement('a');
    catBuildR.href = 'https://www.creativesilva.com/curriculum.html#build-resources';
    catBuildR.className = 'silva-uni-catmod';
    catBuildR.textContent = 'Build Resources';
    menu.appendChild(catBuildR);
    MENU.forEach(function (group) {
      if (!group.modules || !group.modules.length) { return; }
      var hd = document.createElement('div');
      hd.className = 'silva-uni-cathd';
      hd.textContent = group.course;
      menu.appendChild(hd);
      group.modules.forEach(function (m, mi) {
        var a = document.createElement('a');
        a.href = m.url;
        a.className = 'silva-uni-catmod';
        a.textContent = String(mi + 1).padStart(2, '0') + ' ' + m.name;
        menu.appendChild(a);
      });
    });
    trigger.addEventListener('click', function (e) {
      e.stopPropagation();
      var willOpen = !cat.classList.contains('open');
      cat.classList.toggle('open', willOpen);
      trigger.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
    });
    cat.appendChild(trigger);
    cat.appendChild(menu);
    bar.appendChild(cat);

    // (Build Resources is intentionally NOT shown on module/calendar pages: it lives on the
    // catalog home. Dropping it here keeps row 2 to one line: CS logo + Catalog + the pager.)

    // The module pager (Prev/Next + page numbers + BUILD / COPY URL / COPY HTML) is
    // the internal module navigation: it only exists on a loaded module page.
    var pager = buildPager();
    if (pager) { pager.classList.add('pg-top'); bar.appendChild(pager); }

    document.addEventListener('click', function (e) {
      if (!cat.contains(e.target)) { cat.classList.remove('open'); trigger.setAttribute('aria-expanded', 'false'); }
    });
    return bar;
  }

  function init() {
    var nav = document.querySelector('.silva-nav');
    if (!nav) { return; }

    // Bottom pager (centered) for narrow screens, appended to the page body.
    var host = document.querySelector('.silva-page');
    var bottom = buildPager();
    if (host && bottom) { bottom.classList.add('pg-bottom'); host.appendChild(bottom); }

    // Retire the legacy breadcrumb row: the unified header (Catalog dropdown + pager)
    // replaces the breadcrumb + dots + step-nav + copy/download buttons entirely.
    var oldInner = nav.querySelector('.silva-nav-inner');
    if (oldInner) { oldInner.parentNode.removeChild(oldInner); }

    // Build the one header, same as the catalog home: a centered max-width column
    // (.silva-uni-inner, mirrors .catalog-sticky-inner) holding the title row then the
    // catalog row, so every shared element lands in the exact same place on both pages.
    var inner = document.createElement('div');
    inner.className = 'silva-uni-inner';
    inner.appendChild(buildTitlebar());
    inner.appendChild(buildCatalogRow());
    nav.insertBefore(inner, nav.firstChild);

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        var open = nav.querySelectorAll('.silva-uni-cat.open');
        for (var i = 0; i < open.length; i++) { open[i].classList.remove('open'); }
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
