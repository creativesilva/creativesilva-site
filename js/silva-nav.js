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
     '/curriculum/shared/jimenez-bonus-vote.html']
  ];

  var SEQUENCE = [];
  for (var m = 0; m < MODULES.length; m++) {
    for (var p = 0; p < MODULES[m].length; p++) { SEQUENCE.push(MODULES[m][p]); }
  }

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

    // Previous module
    var hasPrev = at.g > 0;
    var prev = document.createElement(hasPrev ? 'a' : 'span');
    prev.className = 'pg-edge pg-prev' + (hasPrev ? '' : ' pg-disabled');
    if (hasPrev) { prev.href = MODULES[at.g - 1][0]; }
    prev.innerHTML = '&#8249;&nbsp; Previous';
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

    // Next module
    var hasNext = at.g < MODULES.length - 1;
    var next = document.createElement(hasNext ? 'a' : 'span');
    next.className = 'pg-edge pg-next' + (hasNext ? '' : ' pg-disabled');
    if (hasNext) { next.href = MODULES[at.g + 1][0]; }
    next.innerHTML = 'Next &nbsp;&#8250;';
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
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
