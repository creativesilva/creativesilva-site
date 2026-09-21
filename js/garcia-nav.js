/* ============================================================================
   garcia-nav.js : Mrs. Garcia's scoped module header + pager.
   A trimmed fork of silva-nav.js: SAME header/framework (CS logo, Catalog
   dropdown, Calendar, Search, countdown, Copy URL / Copy HTML, pager), but it
   ONLY knows Mrs. Garcia's own modules and never links back to the main catalog.
   To add a module: add it to MENU and MODULES (host the copied pages under
   /curriculum/garcia/), keeping the two in sync.
   ========================================================================== */
(function () {
  var HOME = '/curriculum/garcia/index.html';   // Mrs. Garcia's portal (her "catalog")

  // Catalog dropdown: her course -> her modules -> the module's OVERVIEW url.
  var MENU = [
    { course: 'Photography 1A', modules: [
      { name: 'Tiny Things', url: '/curriculum/garcia/tiny-things-overview.html' }
    ]}
  ];

  // Each inner array is one module's ordered page URLs (drives the prev/next pager).
  var MODULES = [
    ['/curriculum/garcia/tiny-things-overview.html',
     '/curriculum/garcia/tiny-things-step01-capture.html',
     '/curriculum/garcia/tiny-things-step02-reflection.html']
  ];

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
  function groupIndexOf(url) {
    for (var i = 0; i < MODULES.length; i++) {
      for (var j = 0; j < MODULES[i].length; j++) {
        if (samePath(MODULES[i][j], url)) { return i; }
      }
    }
    return -1;
  }
  // Her whole set is the active span (prev/next may chain across her modules).
  var ACTIVE_FIRST = 0;
  var ACTIVE_LAST = MODULES.length - 1;
  function inActive(g) { return g >= ACTIVE_FIRST && g <= ACTIVE_LAST; }

  function pageWindow(total, cur) {
    var out = [];
    if (total <= 7) { for (var i = 0; i < total; i++) { out.push(i); } return out; }
    var keep = {};
    [0, total - 1, cur - 1, cur, cur + 1].forEach(function (n) { if (n >= 0 && n < total) { keep[n] = true; } });
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

    var prevHref = null, prevLabel = '&#8249;&nbsp; Previous';
    if (at.p > 0) { prevHref = mod[at.p - 1]; }
    else if (inActive(at.g) && at.g > ACTIVE_FIRST) {
      var pmod = MODULES[at.g - 1]; prevHref = pmod[pmod.length - 1]; prevLabel = '&#8249;&nbsp; Previous Module';
    }
    var prev = document.createElement(prevHref ? 'a' : 'span');
    prev.className = 'pg-edge pg-prev' + (prevHref ? '' : ' pg-disabled');
    if (prevHref) { prev.href = prevHref; }
    prev.innerHTML = prevLabel;
    pager.appendChild(prev);

    if (mod.length > 1) {
      pageWindow(mod.length, at.p).forEach(function (n) {
        if (n === 'gap') { var dots = document.createElement('span'); dots.className = 'pg-ellipsis'; dots.textContent = '…'; pager.appendChild(dots); return; }
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

    var atLast = at.p >= mod.length - 1;
    var nextHref = null, nextLabel = 'Next &nbsp;&#8250;';
    if (!atLast) { nextHref = mod[at.p + 1]; }
    else if (inActive(at.g) && at.g < ACTIVE_LAST) { nextHref = MODULES[at.g + 1][0]; nextLabel = 'Next Module &nbsp;&#8250;'; }
    var next = document.createElement(nextHref ? 'a' : 'span');
    next.className = 'pg-edge pg-next' + (nextHref ? '' : ' pg-disabled');
    if (nextHref) { next.href = nextHref; }
    next.innerHTML = nextLabel;
    pager.appendChild(next);

    pager.appendChild(makeUrlBtn());
    pager.appendChild(makeCopyBtn());
    return pager;
  }

  function makeCopyBtn() {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'pg-copy'; b.textContent = 'COPY HTML';
    b.addEventListener('click', function () {
      var el = document.getElementById('top'); if (!el) { return; }
      navigator.clipboard.writeText(el.outerHTML).then(function () {
        b.textContent = '✓ Copied!'; b.classList.add('copied');
        setTimeout(function () { b.textContent = 'COPY HTML'; b.classList.remove('copied'); }, 2500);
      }).catch(function () { alert('Copy failed. Try selecting the page source manually.'); });
    });
    return b;
  }
  function makeUrlBtn() {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'pg-copy'; b.textContent = 'COPY URL';
    b.addEventListener('click', function () {
      navigator.clipboard.writeText(location.href).then(function () {
        b.textContent = '✓ Copied!'; b.classList.add('copied');
        setTimeout(function () { b.textContent = 'COPY URL'; b.classList.remove('copied'); }, 2500);
      }).catch(function () { alert('Copy failed. Copy the address bar manually.'); });
    });
    return b;
  }

  // Row 1: title (links to her module overview / her portal) + Calendar + Search (her portal) + countdown.
  function buildTitlebar() {
    var bar = document.createElement('div');
    bar.className = 'silva-uni-titlebar';

    var title = document.createElement('a');
    title.className = 'silva-uni-title';
    var at = locate();
    title.href = at ? ('/' + MODULES[at.g][0].replace(/^\//, '')) : HOME;
    var docTitle = (document.title || '').split('|')[0].trim();
    title.textContent = docTitle || 'Photography 1A';
    bar.appendChild(title);

    var cal = document.createElement('a');
    cal.className = 'silva-uni-cal';
    cal.href = '/calendar.html';
    cal.textContent = 'Calendar';
    bar.appendChild(cal);

    // Search: opens Mrs. Garcia's portal with its module search open (scoped to her modules only).
    var searchBtn = document.createElement('a');
    searchBtn.className = 'silva-uni-searchbtn';
    searchBtn.href = HOME + '?search=1';
    searchBtn.textContent = 'Search';
    searchBtn.setAttribute('aria-label', 'Search Mrs. Garcia’s modules');
    bar.appendChild(searchBtn);

    var clock = document.createElement('iframe');
    clock.className = 'silva-uni-clock';
    clock.src = '/assets/embeds/period-clock.html';
    clock.title = 'Class period countdown';
    clock.setAttribute('scrolling', 'no');
    clock.setAttribute('loading', 'lazy');
    bar.appendChild(clock);
    return bar;
  }

  // Row 2: CS logo (-> her portal) + Catalog dropdown (her modules only) + pager. No Teacher/Build links.
  function buildCatalogRow() {
    var bar = document.createElement('div');
    bar.className = 'silva-uni-bar';

    var logo = document.createElement('a');
    logo.className = 'silva-uni-logo';
    logo.href = HOME;
    logo.setAttribute('aria-label', 'Mrs. Garcia, Photography 1A');
    logo.innerHTML = '<img src="/assets/garcia/lg-logo-mrs-garcia-v1.svg" alt="Mrs. Garcia" />';
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
    // Only her pages: a Home link to her portal, then her modules. No links back to the main catalog.
    var catHome = document.createElement('a');
    catHome.href = HOME;
    catHome.className = 'silva-uni-catmod silva-uni-catmain';
    catHome.innerHTML = '&#8592;&nbsp; Photography 1A Home';
    menu.appendChild(catHome);
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

    var host = document.querySelector('.silva-page');
    var bottom = buildPager();
    if (host && bottom) { bottom.classList.add('pg-bottom'); host.appendChild(bottom); }

    var oldInner = nav.querySelector('.silva-nav-inner');
    if (oldInner) { oldInner.parentNode.removeChild(oldInner); }

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
  } else { init(); }
})();
