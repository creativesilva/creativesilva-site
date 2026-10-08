// CreativeSilva.com portfolio behavior:
// docking nav, mobile menu, home hero crossfade, justified gallery,
// Also View slider, back-to-top. (Full-screen photo viewer is lightbox.js.)
(function () {
  // ---------- Docking nav + mobile menu ----------
  var nav = document.querySelector(".mainnav");
  var toggle = document.querySelector(".navtoggle");
  var label = toggle && toggle.querySelector(".navtoggle-label");
  var head = document.querySelector(".masthead");

  if (nav && head && "IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) {
      var e = entries[0];
      nav.classList.toggle("docked", !e.isIntersecting && e.boundingClientRect.top < 0);
    }).observe(head);
  }

  function setMenu(open) {
    if (!nav) return;
    if (open) nav.style.setProperty("--menu-top", Math.max(0, nav.getBoundingClientRect().bottom) + "px");
    nav.classList.toggle("open", open);
    document.documentElement.classList.toggle("menu-open", open);
    if (toggle) {
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    }
    if (label) label.textContent = open ? "Close" : "Menu";
  }
  if (nav && toggle) {
    toggle.addEventListener("click", function () { setMenu(!nav.classList.contains("open")); });
    nav.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
    window.addEventListener("resize", function () { if (window.innerWidth > 760) setMenu(false); });
  }

  // ---------- Home hero: slow crossfade ----------
  var slides = [].slice.call(document.querySelectorAll(".hero-home .hero-slide"));
  if (slides.length > 1) {
    var sdots = [].slice.call(document.querySelectorAll(".hero-dots button"));
    var at = 0, timer = null;
    var still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var showSlide = function (i) {
      at = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle("is-active", k === at); });
      sdots.forEach(function (d, k) { d.setAttribute("aria-selected", k === at ? "true" : "false"); });
    };
    var play = function () {
      clearTimeout(timer);
      if (still) return;
      timer = setTimeout(function () { showSlide(at + 1); play(); }, +(slides[at].getAttribute("data-hold") || 7000));
    };
    sdots.forEach(function (d, k) { d.addEventListener("click", function () { slides.forEach(function (s) { s.classList.remove("pending"); }); showSlide(k); play(); }); });
    var wake = function () { slides.forEach(function (s) { s.classList.remove("pending"); }); showSlide(0); play(); };
    if (document.readyState === "complete") wake(); else window.addEventListener("load", wake);
    document.addEventListener("visibilitychange", function () { if (document.hidden) clearTimeout(timer); else play(); });
  }

  // ---------- Justified gallery (flush rows, ratio-driven) + fade-in ----------
  document.querySelectorAll(".gallery-grid").forEach(function (grid) {
    grid.querySelectorAll(".gallery-item").forEach(function (item) {
      var img = item.querySelector("img");
      if (!img) return;
      function ready() { item.classList.add("is-loaded"); }
      if (!item.classList.contains("gallery-item--feature")) {
        function applyRatio() {
          var r = img.naturalWidth / img.naturalHeight;
          if (!r || r <= 0) r = 1.5;
          item.style.flexGrow = r;
          item.style.flexBasis = Math.round(r * 220) + "px";
        }
        if (img.complete && img.naturalWidth > 0) { applyRatio(); ready(); }
        else { img.addEventListener("load", function () { applyRatio(); ready(); }); img.addEventListener("error", ready); }
      } else {
        if (img.complete && img.naturalWidth > 0) ready();
        else { img.addEventListener("load", ready); img.addEventListener("error", ready); }
      }
    });
  });

  // ---------- "Also View" slider ----------
  document.querySelectorAll(".also-like-slider-wrap").forEach(function (wrap) {
    var track = wrap.querySelector(".also-like-track");
    var prevBtn = wrap.querySelector(".slider-btn--prev");
    var nextBtn = wrap.querySelector(".slider-btn--next");
    if (!track || !prevBtn || !nextBtn) return;
    function scrollAmount() {
      var first = track.firstElementChild;
      if (!first) return 300;
      var gap = parseFloat(getComputedStyle(track).gap) || 16;
      return first.offsetWidth + gap;
    }
    function refresh() {
      var atStart = track.scrollLeft <= 2;
      var atEnd = track.scrollLeft >= track.scrollWidth - track.clientWidth - 2;
      prevBtn.setAttribute("aria-hidden", atStart ? "true" : "false");
      nextBtn.setAttribute("aria-hidden", atEnd ? "true" : "false");
    }
    prevBtn.addEventListener("click", function (e) { e.stopPropagation(); track.scrollBy({ left: -scrollAmount(), behavior: "smooth" }); });
    nextBtn.addEventListener("click", function (e) { e.stopPropagation(); track.scrollBy({ left: scrollAmount(), behavior: "smooth" }); });
    track.addEventListener("scroll", refresh, { passive: true });
    refresh();
  });

  // ---------- Back to top ----------
  document.querySelectorAll(".back-to-top").forEach(function (el) {
    el.addEventListener("click", function (e) { e.preventDefault(); window.scrollTo({ top: 0, behavior: "smooth" }); });
  });

  // ---------- Footer year ----------
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();

  // ---------- Tenure numbers (computed from start years, always current) ----------
  var curYear = new Date().getFullYear();
  document.querySelectorAll(".brand-tenure b[data-since]").forEach(function (b) {
    b.textContent = curYear - parseInt(b.getAttribute("data-since"), 10);
  });

  // ---------- Live "images made worldwide" counter ----------
  // Year-to-date images captured worldwide, at a grounded global rate (~2.1 trillion/yr).
  // The sub-count shows how few are authored photographs.
  var pcNum = document.getElementById("pc-num");
  if (pcNum) {
    var RATE = 70000;               // images per second, worldwide (~2.2 trillion/yr, 2026)
    var PHOTO_RATE = RATE / 10000;  // only about 1 in 10,000 is a true photograph
    var pcPhoto = document.getElementById("pc-photo");
    var yearStart = Date.UTC(new Date().getUTCFullYear(), 0, 1);
    var fmt = function (n) { return Math.floor(n).toLocaleString("en-US"); };
    var tickCounter = function () {
      var elapsed = (Date.now() - yearStart) / 1000;
      pcNum.textContent = fmt(elapsed * RATE);
      if (pcPhoto) pcPhoto.textContent = fmt(elapsed * PHOTO_RATE);
    };
    tickCounter();
    setInterval(tickCounter, 80);
  }
})();
