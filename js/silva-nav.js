/**
 * silva-nav.js
 * Auto-injects prev/next arrow buttons into .silva-nav-inner on every
 * curriculum page. The SEQUENCE array is the authoritative order of all
 * published module pages. Loops continuously — last page wraps to first.
 *
 * To add a new page: append its path to SEQUENCE in the correct position.
 */

(function () {
  var SEQUENCE = [
    '/curriculum/universal/about-mr-silva.html',
    '/curriculum/digarts1/digarts1b-home.html',
    '/curriculum/photo1/photo1b-home.html',
    '/curriculum/photo1/sauce-baby/creative-brief.html',
    '/curriculum/photo1/sauce-baby/overview.html',
    '/curriculum/photo1/sauce-baby/step1-mood-board.html',
    '/curriculum/photo1/sauce-baby/step2-planning.html',
    '/curriculum/photo1/sauce-baby/step3-shoot-contact.html',
    '/curriculum/photo1/sauce-baby/step4-final-edits.html',
    '/curriculum/photo1/sauce-baby/step5-reflection.html'
  ];

  function init() {
    var path = window.location.pathname;
    // Match with or without leading slash, with or without .html
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

    var navInner = document.querySelector('.silva-nav-inner');
    if (!navInner) return;

    var prevBtn = document.createElement('a');
    prevBtn.href = prevUrl;
    prevBtn.className = 'silva-nav-arrow';
    prevBtn.setAttribute('aria-label', 'Previous module');
    prevBtn.setAttribute('title', 'Previous module');
    prevBtn.innerHTML = '&#8592;';

    var nextBtn = document.createElement('a');
    nextBtn.href = nextUrl;
    nextBtn.className = 'silva-nav-arrow';
    nextBtn.setAttribute('aria-label', 'Next module');
    nextBtn.setAttribute('title', 'Next module');
    nextBtn.innerHTML = '&#8594;';

    navInner.insertBefore(prevBtn, navInner.firstChild);
    navInner.appendChild(nextBtn);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
