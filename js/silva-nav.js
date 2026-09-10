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
      { name: 'Sketchbook Cover',    url: '/curriculum/shared/digarts1-sketchbook-cover-overview.html' },
      { name: 'Motivational Poster', url: '/curriculum/shared/digarts1-motivational-poster-overview.html' }
    ]},
    { course: 'Photography 1A', modules: [
      { name: 'Self-Portrait',            url: '/curriculum/shared/photo1-self-portrait-overview.html' },
      { name: 'Composition Concepts',     url: '/curriculum/shared/photo1-composition-concepts-overview.html' },
      { name: 'Leading Lines Photo Walk', url: '/curriculum/shared/photo1-leading-lines-overview.html' },
      { name: 'Image Series Photo Walk',  url: '/curriculum/shared/photo1-image-series-overview.html' }
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

    // MRC — Summer Digital Arts 1A (Mark Richardson Center)
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

    pager.appendChild(makeCopyBtn());
    return pager;
  }

  // The COPY HTML button that lives inside each pager, right of Next.
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

  function injectBurger(navInner, nav) {
    var burger = document.createElement('button');
    burger.type = 'button';
    burger.className = 'silva-burger';
    burger.setAttribute('aria-label', 'Toggle navigation menu');
    burger.setAttribute('aria-expanded', 'false');
    burger.innerHTML = '<span></span><span></span><span></span>';

    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    // Close menu when any link inside the open nav is clicked
    navInner.addEventListener('click', function (e) {
      var target = e.target;
      while (target && target !== navInner) {
        if (target.tagName === 'A' && nav.classList.contains('menu-open')) {
          nav.classList.remove('menu-open');
          burger.setAttribute('aria-expanded', 'false');
          break;
        }
        target = target.parentNode;
      }
    });

    navInner.appendChild(burger);
  }

  // Turn the top-left "Curriculum Catalog" breadcrumb into a click dropdown:
  // Catalog -> course list -> (click a course) its modules -> (click a module) its overview.
  // Accordion style so it works the same on iPad (touch) and desktop (mouse).
  function injectCatalogMenu() {
    var crumb = document.querySelector('.silva-breadcrumb a[href$="curriculum.html"]');
    if (!crumb || crumb.getAttribute('data-catmenu') === '1') { return; }
    crumb.setAttribute('data-catmenu', '1');

    var wrap = document.createElement('span');
    wrap.className = 'silva-catmenu';
    crumb.parentNode.insertBefore(wrap, crumb);
    wrap.appendChild(crumb);
    crumb.classList.add('silva-catmenu-trigger');
    crumb.textContent = 'Catalog';   // teacher-facing; no need for "Curriculum", no down-caret

    var panel = document.createElement('div');
    panel.className = 'silva-catmenu-panel';
    panel.setAttribute('role', 'menu');

    var full = document.createElement('a');
    full.href = '/curriculum.html';
    full.className = 'silva-catmenu-full';
    full.innerHTML = '<span class="cm-caret">&#9656;</span>Open full catalog';
    panel.appendChild(full);   // first item, before the courses

    // Build Resources: the teacher build/design tools, right below the full catalog.
    var build = document.createElement('a');
    build.href = '/curriculum.html#build-resources';
    build.className = 'silva-catmenu-full silva-catmenu-build';
    build.innerHTML = '<span class="cm-caret">&#9656;</span>Build Resources';
    panel.appendChild(build);

    // Faint divider, then the courses.
    var div = document.createElement('div');
    div.className = 'silva-catmenu-div';
    panel.appendChild(div);

    MENU.forEach(function (c) {
      var course = document.createElement('button');
      course.type = 'button';
      course.className = 'silva-catmenu-course';
      course.innerHTML = '<span class="cm-caret">&#9656;</span>' + c.course;
      var sub = document.createElement('div');
      sub.className = 'silva-catmenu-modules';
      c.modules.forEach(function (mod) {
        var a = document.createElement('a');
        a.href = mod.url;
        a.className = 'silva-catmenu-module';
        a.textContent = mod.name;
        sub.appendChild(a);
      });
      course.addEventListener('click', function (e) {
        e.stopPropagation();
        var willOpen = !course.classList.contains('open');
        panel.querySelectorAll('.silva-catmenu-course.open').forEach(function (o) { o.classList.remove('open'); });
        panel.querySelectorAll('.silva-catmenu-modules.open').forEach(function (o) { o.classList.remove('open'); });
        if (willOpen) { course.classList.add('open'); sub.classList.add('open'); }
      });
      panel.appendChild(course);
      panel.appendChild(sub);
    });

    // Leave the catalog for the portfolio site (last item, below the courses)
    var leave = document.createElement('a');
    leave.href = '/';
    leave.className = 'silva-catmenu-leave';
    leave.innerHTML = '<span class="cm-caret">&#9656;</span>creativesilva.com';
    panel.appendChild(leave);

    wrap.appendChild(panel);

    // .silva-breadcrumb has overflow:hidden (for truncation); lift it only while open
    var bc = crumb.closest('.silva-breadcrumb');
    function setOpen(open) {
      wrap.classList.toggle('open', open);
      if (bc) { bc.classList.toggle('catmenu-open', open); }
    }
    crumb.addEventListener('click', function (e) {
      e.preventDefault();
      setOpen(!wrap.classList.contains('open'));
    });
    document.addEventListener('click', function (e) {
      if (!wrap.contains(e.target)) { setOpen(false); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { setOpen(false); }
    });
  }

  function init() {
    var nav = document.querySelector('.silva-nav');
    var navInner = document.querySelector('.silva-nav-inner');

    // Bottom pager (centered) — includes its own COPY HTML at the right.
    var host = document.querySelector('.silva-page');
    var bottom = buildPager();
    if (host && bottom) { bottom.classList.add('pg-bottom'); host.appendChild(bottom); }

    if (!nav || !navInner) { return; }

    // Top pager: same pill, sits in the nav bar. Since the pager carries its
    // own COPY HTML and prev/next, drop the old toolbar buttons (Copy,
    // Download) and the now-redundant step-nav + divider.
    var top = buildPager();
    if (top) {
      var dl = navInner.querySelector('.silva-download-btn');
      if (dl) { dl.parentNode.removeChild(dl); }
      var cb = navInner.querySelector('.silva-copy-btn');
      if (cb) { cb.parentNode.removeChild(cb); }
      var sn = navInner.querySelector('.silva-step-nav');
      if (sn) { sn.style.display = 'none'; }
      var nd = navInner.querySelector('.silva-nav-div');
      if (nd) { nd.style.display = 'none'; }
      top.classList.add('pg-top');
      navInner.appendChild(top);
    }

    injectBurger(navInner, nav);
    injectCatalogMenu();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
