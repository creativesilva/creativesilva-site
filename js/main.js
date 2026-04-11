// CreativeSilva.com — minimal lightbox + lazy fade-in

(function () {
  // Lightbox
  const lb = document.createElement("div");
  lb.className = "lightbox";
  lb.innerHTML =
    '<button class="lb-close" aria-label="Close">&times;</button>' +
    '<img alt="" />' +
    '<div class="lb-caption"></div>';
  document.body.appendChild(lb);

  const lbImg = lb.querySelector("img");
  const lbCap = lb.querySelector(".lb-caption");
  const lbClose = lb.querySelector(".lb-close");

  function openLightbox(src, alt, caption) {
    lbImg.src = src;
    lbImg.alt = alt || "";
    lbCap.textContent = caption || "";
    lb.classList.add("open");
    document.body.style.overflow = "hidden";
  }
  function closeLightbox() {
    lb.classList.remove("open");
    lbImg.src = "";
    document.body.style.overflow = "";
  }

  document.querySelectorAll(".gallery-item img").forEach(function (img) {
    img.addEventListener("click", function () {
      const figure = img.closest("figure");
      const cap = figure ? figure.querySelector("figcaption") : null;
      openLightbox(img.src, img.alt, cap ? cap.textContent : "");
    });
  });

  lb.addEventListener("click", function (e) {
    if (e.target === lb || e.target === lbImg) closeLightbox();
  });
  lbClose.addEventListener("click", closeLightbox);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeLightbox();
  });

  // Smooth scroll for back-to-top
  document.querySelectorAll(".back-to-top").forEach(function (el) {
    el.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });
})();
