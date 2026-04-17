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

  // Smooth scroll for back-to-top
  document.querySelectorAll(".back-to-top").forEach(function (el) {
    el.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });
})();
