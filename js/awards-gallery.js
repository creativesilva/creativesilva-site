// Awards gallery lightbox + seamless cross-page carousel.
// Each of the 12 gallery pages loads this script. Clicking a thumbnail
// opens a fixed overlay viewer with prev/next arrows that cycle through
// the student's images. At the end of one student, next nav crosses to
// the first image of the next student. Same for prev at the start.
// ?img=N on page load auto-opens the lightbox at that image (used by
// cross-page hand-offs so the flow feels continuous).
(function () {
  var INVITEES = [
    { slug: "julyssa",   first: "Julyssa",   count: 3 },
    { slug: "rafael",    first: "Rafael",    count: 3 },
    { slug: "isbeth",    first: "Isbeth",    count: 3 },
    { slug: "pedro",     first: "Pedro",     count: 3 },
    { slug: "jonathan",  first: "Jonathan",  count: 3 },
    { slug: "ricardo",   first: "Ricardo",   count: 3 },
    { slug: "dennis",    first: "Dennis",    count: 4 },
    { slug: "veniece",   first: "Veniece",   count: 4 },
    { slug: "matthew",   first: "Matthew",   count: 4 },
    { slug: "davina",    first: "Davina",    count: 4 },
    { slug: "elizabeth", first: "Elizabeth", count: 4 },
    { slug: "emiliano",  first: "Emiliano",  count: 4 }
  ];

  var match = window.location.pathname.match(/\/awards\/([a-z]+)\.html/);
  if (!match) return;
  var idx = -1;
  for (var i = 0; i < INVITEES.length; i++) {
    if (INVITEES[i].slug === match[1]) { idx = i; break; }
  }
  if (idx < 0) return;

  var cur  = INVITEES[idx];
  var next = INVITEES[(idx + 1) % INVITEES.length];
  var prev = INVITEES[(idx - 1 + INVITEES.length) % INVITEES.length];

  // Build overlay
  var overlay = document.createElement("div");
  overlay.id = "awards-lightbox";
  overlay.style.cssText =
    "position:fixed;inset:0;background:rgba(0,0,0,0.94);z-index:9999;display:none;" +
    "align-items:center;justify-content:center;padding:24px;font-family:Arial,sans-serif;";
  overlay.innerHTML =
    '<div style="position:absolute;top:20px;left:24px;color:#80e0e0;font-size:12pt;letter-spacing:0.10em;text-transform:uppercase;font-weight:bold;" id="lb-counter"></div>' +
    '<button id="lb-close" aria-label="Close" style="position:absolute;top:16px;right:20px;background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.20);color:#fff;font-size:20pt;width:46px;height:46px;border-radius:50%;cursor:pointer;line-height:1;">&times;</button>' +
    '<button id="lb-prev" aria-label="Previous" style="position:absolute;left:24px;top:50%;transform:translateY(-50%);background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.20);color:#fff;font-size:22pt;width:56px;height:56px;border-radius:50%;cursor:pointer;line-height:1;">&larr;</button>' +
    '<button id="lb-next" aria-label="Next" style="position:absolute;right:24px;top:50%;transform:translateY(-50%);background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.20);color:#fff;font-size:22pt;width:56px;height:56px;border-radius:50%;cursor:pointer;line-height:1;">&rarr;</button>' +
    '<div style="display:flex;flex-direction:column;align-items:center;gap:14px;max-width:92vw;">' +
      '<img id="lb-img" src="" alt="" style="max-width:88vw;max-height:78vh;width:auto;height:auto;border-radius:14px;display:block;background:#000;" />' +
      '<div id="lb-caption" style="color:rgba(255,255,255,0.78);font-size:12pt;letter-spacing:0.06em;text-align:center;"></div>' +
    "</div>";
  document.body.appendChild(overlay);

  var imgEl    = document.getElementById("lb-img");
  var counter  = document.getElementById("lb-counter");
  var caption  = document.getElementById("lb-caption");
  var btnPrev  = document.getElementById("lb-prev");
  var btnNext  = document.getElementById("lb-next");
  var btnClose = document.getElementById("lb-close");
  var current  = 1;

  function pad(n) { return n < 10 ? "0" + n : "" + n; }

  function show(n) {
    current = n;
    imgEl.src = "/assets/awards/galleries/" + cur.slug + "/" + pad(n) + ".jpg";
    imgEl.alt = cur.first + " " + n;
    counter.textContent = cur.first + " • " + n + " of " + cur.count;
    var hint =
      n === cur.count
        ? "Last image. Next loads " + next.first + "."
        : n === 1
        ? "First image. Previous loads " + prev.first + "."
        : "Use arrows or your keyboard to flip through.";
    caption.textContent = hint;
  }

  function open(n) {
    show(n);
    overlay.style.display = "flex";
    document.body.style.overflow = "hidden";
  }

  function close() {
    overlay.style.display = "none";
    document.body.style.overflow = "";
  }

  function goPrev() {
    if (current > 1) {
      show(current - 1);
    } else {
      // hand off to previous student at their last image
      window.location.href = prev.slug + ".html?img=" + prev.count;
    }
  }

  function goNext() {
    if (current < cur.count) {
      show(current + 1);
    } else {
      // hand off to next student at image 1
      window.location.href = next.slug + ".html?img=1";
    }
  }

  btnPrev.addEventListener("click", goPrev);
  btnNext.addEventListener("click", goNext);
  btnClose.addEventListener("click", close);
  overlay.addEventListener("click", function (e) {
    if (e.target === overlay) close();
  });
  document.addEventListener("keydown", function (e) {
    if (overlay.style.display !== "flex") return;
    if (e.key === "Escape")     close();
    if (e.key === "ArrowLeft")  goPrev();
    if (e.key === "ArrowRight") goNext();
  });

  // Hook thumbnails
  var tiles = document.querySelectorAll("[data-gallery-img]");
  for (var t = 0; t < tiles.length; t++) {
    (function (el) {
      el.addEventListener("click", function (e) {
        e.preventDefault();
        open(parseInt(el.getAttribute("data-gallery-img"), 10) || 1);
      });
    })(tiles[t]);
  }

  // Auto-open via ?img=
  var params = new URLSearchParams(window.location.search);
  var imgParam = parseInt(params.get("img"), 10);
  if (imgParam >= 1 && imgParam <= cur.count) {
    open(imgParam);
  }
})();
