// CreativeSilva.com — peek hero slider + justified gallery + lightbox + also-like slider

// ---------- Hero slider (peek carousel) ----------
(function () {
  var slider  = document.querySelector(".hero-slider");
  if (!slider) return;

  var track   = slider.querySelector(".hero-slides-track");
  if (!track) return;

  var slides  = Array.from(track.querySelectorAll(".hero-slide"));
  var dots    = Array.from(slider.querySelectorAll(".hero-dot"));
  var prevBtn = slider.querySelector(".hero-btn--prev");
  var nextBtn = slider.querySelector(".hero-btn--next");
  var colEl   = slider.querySelector(".hero-collection");
  var titleEl = slider.querySelector(".hero-title");
  var current = 0;
  var timer;
  var INTERVAL  = 14000;
  var SLIDE_PAD = 6; // px padding on each side of a slide (matches CSS)

  function sliderW()  { return slider.offsetWidth; }
  function slideW()   { return sliderW() * 0.8; }   // 80% of container
  function peekW()    { return sliderW() * 0.1; }   // 10% on each side

  function applyTransform(i) {
    var step   = slideW() + SLIDE_PAD * 2;
    var offset = peekW() - i * step;
    track.style.transform = "translateX(" + offset + "px)";
  }

  function goTo(i) {
    slides[current].classList.remove("active");
    dots[current].classList.remove("active");
    current = (i + slides.length) % slides.length;
    slides[current].classList.add("active");
    dots[current].classList.add("active");
    applyTransform(current);
    if (colEl)   colEl.textContent   = slides[current].dataset.collection || "";
    if (titleEl) titleEl.textContent = slides[current].dataset.title      || "";
  }

  function start()   { if (!timer) timer = setInterval(function () { goTo(current + 1); }, INTERVAL); }
  function stop()    { clearInterval(timer); timer = null; }

  // Set initial position without transition flash
  track.style.transition = "none";
  applyTransform(0);
  requestAnimationFrame(function () { track.style.transition = ""; });

  if (prevBtn) prevBtn.addEventListener("click", function () { goTo(current - 1); });
  if (nextBtn) nextBtn.addEventListener("click", function () { goTo(current + 1); });

  dots.forEach(function (dot, i) {
    dot.addEventListener("click", function () { goTo(i); });
  });

  // Touch / swipe
  var touchX = 0;
  slider.addEventListener("touchstart", function (e) {
    touchX = e.touches[0].clientX;
  }, { passive: true });
  slider.addEventListener("touchend", function (e) {
    var dx = touchX - e.changedTouches[0].clientX;
    if (Math.abs(dx) > 40) { goTo(dx > 0 ? current + 1 : current - 1); }
  });

  // Keyboard
  document.addEventListener("keydown", function (e) {
    if (lb && lb.classList.contains("open")) return; // don't hijack lightbox keys
    if (e.key === "ArrowLeft")  { goTo(current - 1); }
    if (e.key === "ArrowRight") { goTo(current + 1); }
  });

  // Recalculate on resize
  window.addEventListener("resize", function () { applyTransform(current); });

  start();
}());

// ---------- Justified gallery (Pixiset-style flush rows) ----------
(function () {
  document.querySelectorAll(".gallery-grid").forEach(function (grid) {
    grid.querySelectorAll(".gallery-item").forEach(function (item) {
      if (item.classList.contains("gallery-item--feature")) return;
      var img = item.querySelector("img");
      if (!img) return;
      function applyRatio() {
        var r = img.naturalWidth / img.naturalHeight;
        if (!r || r <= 0) r = 1.5;
        item.style.flexGrow  = r;
        item.style.flexBasis = Math.round(r * 200) + "px";
      }
      if (img.complete && img.naturalWidth > 0) {
        applyRatio();
      } else {
        img.addEventListener("load", applyRatio);
      }
    });
  });
}());

// ---------- Lightbox ----------
var lb; // shared reference so keyboard handler above can check
(function () {
  // Collect all gallery images on the page (standard gallery + magazine covers)
  const items = Array.from(document.querySelectorAll(".gallery-item img, .magazine-cover img"));
  let currentIndex = 0;

  // Build lightbox
  lb = document.createElement("div");
  lb.className = "lightbox";
  lb.innerHTML =
    '<button class="lb-close" aria-label="Close">&times;</button>' +
    '<button class="lb-prev" aria-label="Previous image">&#8592;</button>' +
    '<img alt="" />' +
    '<button class="lb-next" aria-label="Next image">&#8594;</button>' +
    '<div class="lb-caption"></div>';
  document.body.appendChild(lb);

  const lbImg   = lb.querySelector("img");
  const lbCap   = lb.querySelector(".lb-caption");
  const lbClose = lb.querySelector(".lb-close");
  const lbPrev  = lb.querySelector(".lb-prev");
  const lbNext  = lb.querySelector(".lb-next");

  function showImage(index) {
    currentIndex = (index + items.length) % items.length;
    const img    = items[currentIndex];
    const figure = img.closest("figure");
    const cap    = figure ? figure.querySelector("figcaption") : null;
    lbImg.src = img.src;
    lbImg.alt = img.alt || "";
    if (cap) {
      lbCap.textContent = cap.textContent;
    } else {
      const credit = figure ? figure.querySelector(".magazine-credit") : null;
      if (credit) {
        const name = credit.querySelector(".student-name");
        const pub  = credit.querySelector(".publication");
        lbCap.textContent = (name && pub) ? name.textContent + " \u00b7 " + pub.textContent : "";
      } else {
        lbCap.textContent = "";
      }
    }
    const show = items.length > 1 ? "" : "none";
    lbPrev.style.display = show;
    lbNext.style.display = show;
  }

  function openLightbox(index) {
    showImage(index);
    lb.classList.add("open");
    document.body.style.overflow = "hidden";
  }

  function closeLightbox() {
    lb.classList.remove("open");
    lbImg.src = "";
    document.body.style.overflow = "";
  }

  items.forEach(function (img, index) {
    img.addEventListener("click", function () { openLightbox(index); });
  });

  lb.addEventListener("click", function (e) {
    if (e.target === lb) closeLightbox();
  });

  lbClose.addEventListener("click", closeLightbox);

  lbPrev.addEventListener("click", function (e) {
    e.stopPropagation();
    showImage(currentIndex - 1);
  });

  lbNext.addEventListener("click", function (e) {
    e.stopPropagation();
    showImage(currentIndex + 1);
  });

  document.addEventListener("keydown", function (e) {
    if (!lb.classList.contains("open")) return;
    if (e.key === "Escape")     closeLightbox();
    if (e.key === "ArrowLeft")  showImage(currentIndex - 1);
    if (e.key === "ArrowRight") showImage(currentIndex + 1);
  });

  // "Also View" slider
  document.querySelectorAll(".also-like-slider-wrap").forEach(function (wrap) {
    var track   = wrap.querySelector(".also-like-track");
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
      var atEnd   = track.scrollLeft >= track.scrollWidth - track.clientWidth - 2;
      prevBtn.setAttribute("aria-hidden", atStart ? "true" : "false");
      nextBtn.setAttribute("aria-hidden", atEnd   ? "true" : "false");
    }

    prevBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      track.scrollBy({ left: -scrollAmount(), behavior: "smooth" });
    });
    nextBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      track.scrollBy({ left: scrollAmount(), behavior: "smooth" });
    });
    track.addEventListener("scroll", refresh, { passive: true });
    refresh();
  });

  // Smooth scroll for back-to-top
  document.querySelectorAll(".back-to-top").forEach(function (el) {
    el.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });
})();
