// CreativeSilva.com — hero slider + lightbox + also-like slider

// ---------- Hero slider ----------
(function () {
  var slider = document.querySelector(".hero-slider");
  if (!slider) return;

  var slides   = Array.from(slider.querySelectorAll(".hero-slide"));
  var dots     = Array.from(slider.querySelectorAll(".hero-dot"));
  var prevBtn  = slider.querySelector(".hero-btn--prev");
  var nextBtn  = slider.querySelector(".hero-btn--next");
  var colEl    = slider.querySelector(".hero-collection");
  var titleEl  = slider.querySelector(".hero-title");
  var current  = 0;
  var timer;
  var INTERVAL = 5000;

  function goTo(index) {
    slides[current].classList.remove("active");
    dots[current].classList.remove("active");
    current = (index + slides.length) % slides.length;
    slides[current].classList.add("active");
    dots[current].classList.add("active");
    if (colEl)   colEl.textContent   = slides[current].dataset.collection || "";
    if (titleEl) titleEl.textContent = slides[current].dataset.title      || "";
  }

  function start()   { timer = setInterval(function () { goTo(current + 1); }, INTERVAL); }
  function stop()    { clearInterval(timer); }
  function restart() { stop(); start(); }

  if (prevBtn) prevBtn.addEventListener("click", function () { goTo(current - 1); restart(); });
  if (nextBtn) nextBtn.addEventListener("click", function () { goTo(current + 1); restart(); });

  dots.forEach(function (dot, i) {
    dot.addEventListener("click", function () { goTo(i); restart(); });
  });

  slider.addEventListener("mouseenter", stop);
  slider.addEventListener("mouseleave", start);

  // Touch / swipe
  var touchX = 0;
  slider.addEventListener("touchstart", function (e) {
    touchX = e.touches[0].clientX;
  }, { passive: true });
  slider.addEventListener("touchend", function (e) {
    var dx = touchX - e.changedTouches[0].clientX;
    if (Math.abs(dx) > 40) { goTo(dx > 0 ? current + 1 : current - 1); restart(); }
  });

  // Keyboard
  document.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft")  { goTo(current - 1); restart(); }
    if (e.key === "ArrowRight") { goTo(current + 1); restart(); }
  });

  start();
}());

// CreativeSilva.com — minimal lightbox + lazy fade-in

(function () {
  // Collect all gallery images on the page (standard gallery + magazine covers)
  const items = Array.from(document.querySelectorAll(".gallery-item img, .magazine-cover img"));
  let currentIndex = 0;

  // Build lightbox
  const lb = document.createElement("div");
  lb.className = "lightbox";
  lb.innerHTML =
    '<button class="lb-close" aria-label="Close">&times;</button>' +
    '<button class="lb-prev" aria-label="Previous image">&#8592;</button>' +
    '<img alt="" />' +
    '<button class="lb-next" aria-label="Next image">&#8594;</button>' +
    '<div class="lb-caption"></div>';
  document.body.appendChild(lb);

  const lbImg  = lb.querySelector("img");
  const lbCap  = lb.querySelector(".lb-caption");
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
      // Magazine cover credit: student name + publication
      const credit = figure ? figure.querySelector(".magazine-credit") : null;
      if (credit) {
        const name = credit.querySelector(".student-name");
        const pub  = credit.querySelector(".publication");
        lbCap.textContent = (name && pub) ? name.textContent + " \u00b7 " + pub.textContent : "";
      } else {
        lbCap.textContent = "";
      }
    }
    // Hide arrows when only one image in the gallery
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

  // Wire up each gallery image
  items.forEach(function (img, index) {
    img.addEventListener("click", function () { openLightbox(index); });
  });

  // Close on backdrop click only (not on image or arrows)
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

  // Keyboard: Escape to close, arrows to navigate
  document.addEventListener("keydown", function (e) {
    if (!lb.classList.contains("open")) return;
    if (e.key === "Escape")      closeLightbox();
    if (e.key === "ArrowLeft")   showImage(currentIndex - 1);
    if (e.key === "ArrowRight")  showImage(currentIndex + 1);
  });

  // "You may also like" slider
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
