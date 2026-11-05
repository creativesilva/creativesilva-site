/* Silva ALIGNMENT AUDIT (the no-wave / row-lock gate). Dev tool, never loaded by a page.
 *
 * Measures every visible multi-column row on the page and flags anything that is not on a
 * straight line. Run it on EVERY tab / pane / open accordion, at 390, 1024, 1366, 1440 and
 * 2560 widths, before calling any visual work done. Ship only at 0 flags.
 *
 * Usage (browser console or an automation runner):
 *   fetch('/tools/align-audit.js').then(r => r.text()).then(eval);
 *   silvaAlignAudit()                 -> { rows, flags: [...] }
 *   silvaAlignAudit({ outline: true }) -> also outlines offending rows in red on the page
 *
 * A row is a set of same-kind siblings sharing one top line inside a grid or wrapping flex
 * container. For every such row it checks:
 *   topDrift      item tops differ                      (staggered row)
 *   controlDrift  first control (button, field, link)   (buttons / dropdowns zig-zag)
 *   bottomDrift   last control / action pill            (pills not on one line)
 *   lineDiff      label / name line counts differ       (one label wraps, its neighbor does not)
 *   heightDiff    item heights differ                   (ragged cards in a uniform grid)
 * and for multi-row wrapping flex containers:
 *   columnDrift   item left edges do not form straight columns (use CSS grid, not flex-wrap)
 * Tolerance is 0.75px (sub-pixel rounding only).
 */
(function () {
  var TOL = 0.75;
  var CONTROL = 'button, select, textarea, input:not([type="hidden"]):not([type="checkbox"]):not([type="radio"]),'
    + ' a[download], a.cal-btn, [role="button"], .pvb-dd-btn, .logo-actions, .pvb-rtools';
  var LABEL = 'label, .ln, .nm, .logo-name, .pvb-refname, .pvb-charname, .page-name, .pvb-capt, .cap, figcaption, .pal-nm, h3, h4';

  function visible(el) {
    var r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return false;
    var cs = getComputedStyle(el);
    return cs.display !== 'none' && cs.visibility !== 'hidden' && parseFloat(cs.opacity) > 0;
  }
  function path(el) {
    var parts = [];
    while (el && el.nodeType === 1 && parts.length < 4) {
      var s = el.tagName.toLowerCase();
      if (el.id) { parts.unshift(s + '#' + el.id); break; }
      if (el.classList.length) s += '.' + Array.prototype.slice.call(el.classList, 0, 2).join('.');
      parts.unshift(s);
      el = el.parentElement;
    }
    return parts.join(' > ');
  }
  function first(el, sel) {
    if (el.matches(sel)) return el;
    var all = el.querySelectorAll(sel);
    for (var i = 0; i < all.length; i++) if (visible(all[i])) return all[i];
    return null;
  }
  // optional, state-dependent extras (an open "Other: type your own" box) are not part of the row's line
  var EXTRA = '.pvb-otherbox, [data-audit-extra]';
  // the LOWEST control on screen (visual order, so CSS `order` is respected), not the last in the DOM
  function last(el, sel) {
    var all = el.querySelectorAll(sel), best = null, bottom = -Infinity;
    for (var i = 0; i < all.length; i++) {
      if (!visible(all[i]) || all[i].matches(EXTRA)) continue;
      var b = all[i].getBoundingClientRect().bottom;
      if (b > bottom + 0.5) { bottom = b; best = all[i]; }
    }
    return best || (el.matches(sel) ? el : null);
  }
  function lines(el) {
    var cs = getComputedStyle(el);
    var lh = parseFloat(cs.lineHeight);
    if (!lh || isNaN(lh)) lh = parseFloat(cs.fontSize) * 1.25;
    // measure the first text-bearing block only (a name line, not its whole meta stack)
    var t = el.querySelector('.ln') || el;
    var h = t.getBoundingClientRect().height;
    return Math.max(1, Math.round(h / lh));
  }
  function spread(vals) {
    vals = vals.filter(function (v) { return v !== null && v !== undefined && !isNaN(v); });
    if (vals.length < 2) return 0;
    return Math.max.apply(null, vals) - Math.min.apply(null, vals);
  }
  function kind(el) { return el.tagName + '.' + (el.classList[0] || ''); }
  function txt(el) { return (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 26); }

  window.silvaAlignAudit = function (opts) {
    opts = opts || {};
    var flags = [], rowsChecked = 0, outlined = [];
    document.querySelectorAll('.silva-audit-flag').forEach(function (e) { e.classList.remove('silva-audit-flag'); e.style.outline = ''; });
    var nodes = document.querySelectorAll('body *');
    for (var n = 0; n < nodes.length; n++) {
      var c = nodes[n];
      var cs = getComputedStyle(c);
      var isGrid = cs.display === 'grid' || cs.display === 'inline-grid';
      var isWrap = (cs.display === 'flex' || cs.display === 'inline-flex') && cs.flexDirection.indexOf('row') === 0 && cs.flexWrap !== 'nowrap';
      if (!isGrid && !isWrap) continue;
      if (!visible(c)) continue;
      var kids = Array.prototype.filter.call(c.children, visible);
      if (kids.length < 2) continue;
      // a row = items whose vertical CENTERS sit inside each other's box (a centered toolbar of mixed
      // heights is one row; a wrapped item is a new row)
      var rows = [];
      kids.forEach(function (k) {
        var b = k.getBoundingClientRect(), cy = b.top + b.height / 2;
        var row = null;
        for (var i = 0; i < rows.length; i++) {
          if (Math.abs(rows[i].cy - cy) <= Math.max(6, Math.min(rows[i].h, b.height) / 2)) { row = rows[i]; break; }
        }
        if (row) row.items.push(k); else rows.push({ t: b.top, cy: cy, h: b.height, items: [k] });
      });
      rows.forEach(function (r, ri) {
        var groups = {};
        r.items.forEach(function (k) { (groups[kind(k)] = groups[kind(k)] || []).push(k); });
        Object.keys(groups).forEach(function (g) {
          var items = groups[g];
          if (items.length < 2) return;
          rowsChecked++;
          var tops = items.map(function (k) { return k.getBoundingClientRect().top; });
          // compare LIKE controls only: for every control type present in all items (a dot row, a pill),
          // its first instance per item must share one center line
          var sig = function (x) { return x.tagName + '.' + (x.classList[0] || ''); };
          var maps = items.map(function (k) {
            var m = {};
            if (k.matches(CONTROL)) m[sig(k)] = k;
            k.querySelectorAll(CONTROL).forEach(function (x) { if (!m[sig(x)] && visible(x)) m[sig(x)] = x; });
            return m;
          });
          var common = Object.keys(maps[0]).filter(function (s) { return maps.every(function (m) { return m[s]; }); });
          var c1 = common.length ? null : items.map(function () { return null; });
          var c2 = items.map(function (k) { return last(k, CONTROL); });
          var labs = items.map(function (k) { return first(k, LABEL); });
          var res = {
            topDrift: spread(tops),
            // controls are compared by their vertical CENTER (a 26px segment and a 16px dot centered in the
            // same row are aligned); a control pushed down by a wrapping label still shows up as drift
            controlDrift: common.reduce(function (worst, s) {
              return Math.max(worst, spread(maps.map(function (m) { var b = m[s].getBoundingClientRect(); return b.top + b.height / 2; })));
            }, 0),
            bottomDrift: c2.every(Boolean) ? spread(c2.map(function (x) { return x.getBoundingClientRect().bottom; })) : 0,
            lineDiff: labs.every(Boolean) ? spread(labs.map(lines)) : 0,
            heightDiff: isGrid && cs.alignItems !== 'start' && cs.alignItems !== 'flex-start' ? spread(items.map(function (k) { return k.getBoundingClientRect().height; })) : 0
          };
          var bad = res.topDrift > TOL || res.controlDrift > TOL || res.bottomDrift > TOL || res.lineDiff > 0 || res.heightDiff > TOL;
          if (bad) {
            flags.push({
              where: path(c), row: ri + 1, items: items.length,
              topDrift: +res.topDrift.toFixed(1), controlDrift: +res.controlDrift.toFixed(1),
              bottomDrift: +res.bottomDrift.toFixed(1), lineDiff: res.lineDiff, heightDiff: +res.heightDiff.toFixed(1),
              sample: items.slice(0, 3).map(txt)
            });
            if (opts.outline) items.forEach(function (k) { k.classList.add('silva-audit-flag'); k.style.outline = '2px solid #ff3b5c'; outlined.push(k); });
          }
        });
      });
      // straight columns across rows (flex-wrap only; CSS grid columns are aligned by construction)
      // (only rows holding 2+ items; a centered one-item-per-row stack is not a column layout)
      if (isWrap && rows.length > 1) {
        // a lone full-width item (flex-basis 100%: a field row under a header row) is intentional, not ragged
        var cw = c.getBoundingClientRect().width;
        rows = rows.filter(function (r) { return !(r.items.length === 1 && r.items[0].getBoundingClientRect().width >= cw * 0.9); });
        var multi = rows.filter(function (r) { return r.items.length >= 2; });
        var wide = multi.length ? multi[0].items.length : 0;
        var same = multi.filter(function (r) { return r.items.length === wide; });
        var ragged = rows.some(function (r) { return r.items.length !== rows[0].items.length; });
        var drift = 0;
        if (same.length > 1) {
          var lefts = same.map(function (r) { return r.items.map(function (k) { return Math.round(k.getBoundingClientRect().left); }); });
          for (var col = 0; col < wide; col++) drift = Math.max(drift, spread(lefts.map(function (l) { return l[col]; })));
        }
        if (drift > TOL || (multi.length && ragged)) flags.push({ where: path(c), row: 'all', items: kids.length, columnDrift: drift,
          rowsLayout: rows.map(function (r) { return r.items.length; }).join('/'),
          note: 'wrapping flex row: items do not form straight, full columns (use CSS grid with equal columns)' });
      }
    }
    return { url: location.pathname, width: innerWidth, rows: rowsChecked, flagCount: flags.length, flags: flags };
  };
})();
