/**
 * silva-nav.js
 *
 * Two responsibilities:
 *
 * 1. Auto-injects prev/next arrow buttons into .silva-nav-inner on every
 *    curriculum page. The SEQUENCE array is the authoritative order of all
 *    published module pages. Loops continuously so the last page wraps to
 *    the first.
 *
 * 2. Auto-injects a hamburger button on every page. On mobile widths
 *    (under 760px), the nav items (dots, step-nav, copy/download buttons,
 *    prev/next arrows) are hidden by CSS. Clicking the hamburger toggles
 *    a .menu-open class on .silva-nav which the CSS uses to reveal the
 *    items stacked vertically.
 *
 * To add a new page: append its path to SEQUENCE in the correct position.
 */

(function () {
  var SEQUENCE = [
    '/curriculum/universal/about-mr-silva.html',

    // Course homes
    '/curriculum/digarts1/digarts1b-home.html',
    '/curriculum/digarts2/digarts2b-home.html',
    '/curriculum/photo1/photo1b-home.html',

    // Cross-course resources
    '/curriculum/shared/photo-course-resources.html',

    // Photo 1B: Sauce Baby (commercial photography final)
    '/curriculum/photo1/sauce-baby/creative-brief.html',
    '/curriculum/photo1/sauce-baby/overview.html',
    '/curriculum/photo1/sauce-baby/step1-mood-board.html',
    '/curriculum/photo1/sauce-baby/step2-planning.html',
    '/curriculum/photo1/sauce-baby/step3-shoot-contact.html',
    '/curriculum/photo1/sauce-baby/step4-final-edits.html',
    '/curriculum/photo1/sauce-baby/step5-reflection.html',

    // Photo 1B: The Revisit Project (end-of-year)
    '/curriculum/shared/revisit-project-overview.html',
    '/curriculum/shared/revisit-step01-capture.html',
    '/curriculum/shared/revisit-step02-edit.html',
    '/curriculum/shared/revisit-step03-reflection.html',

    // Digital Arts: Jimenez Mobile Detailing (spring final)
    '/curriculum/shared/jimenez-spring-final.html',
    '/curriculum/shared/jimenez-step05-mockups.html',
    '/curriculum/shared/jimenez-step07-reflection.html'
  ];

  function injectArrows(navInner) {
    var path = window.location.pathname;
    var idx = -1;
    for (var i = 0; i < SEQUENCE.length; i++) {
      if (path === SEQUENCE[i] || path === SEQUENCE[i].replace(/^\//, '')) {
        idx = i;
        break;
      }
    }
    if (idx === -1) return;

    var n = SEQUENCE.length;
    var prevUrl = SEQUENCE[(idx - 1 + n) % n];
    var nextUrl = SEQUENCE[(idx + 1) % n];

    var prevBtn = document.createElement('a');
    prevBtn.href = prevUrl;
    prevBtn.className = 'silva-nav-arrow silva-nav-arrow-prev';
    prevBtn.setAttribute('aria-label', 'Previous module');
    prevBtn.setAttribute('title', 'Previous module');
    prevBtn.innerHTML = '&#8592;';

    var nextBtn = document.createElement('a');
    nextBtn.href = nextUrl;
    nextBtn.className = 'silva-nav-arrow silva-nav-arrow-next';
    nextBtn.setAttribute('aria-label', 'Next module');
    nextBtn.setAttribute('title', 'Next module');
    nextBtn.innerHTML = '&#8594;';

    navInner.insertBefore(prevBtn, navInner.firstChild);
    navInner.appendChild(nextBtn);
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
    if (!nav || !navInner) return;
    injectArrows(navInner);
    injectBurger(navInner, nav);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
