// A doc page: the format list in the sidebar, the layout timeline (or tabs) and the byte map hover.
// The page content itself is static HTML; CURRENT_PAGE names this page's file.
(function () {
  "use strict";
  var W = PazWiki;

  function renderFormats() {
    var sorted = FORMATS.slice().sort(function (a, b) { return W.sortName(a).localeCompare(W.sortName(b)); });
    var items = [];
    W.groups(sorted).forEach(function (group) {
      if (group.divider) items.push('<li class="side-group' + (group.label ? "" : " blank") + '" data-group="' + group.index + '">' + W.esc(group.label) + "</li>");
      group.items.forEach(function (f) { items.push(item(f, group.index)); });
    });
    var list = document.getElementById("fmtList");
    list.innerHTML = items.join("");
    var current = list.querySelector(".fmt.active");
    if (current) list.scrollTop = current.parentElement.offsetTop - list.clientHeight / 2;
    document.getElementById("fmtFilter").addEventListener("input", function (ev) {
      var q = ev.target.value.trim().toLowerCase();
      var shown = 0;
      var visible = {};
      document.querySelectorAll("#fmtList li[data-name]").forEach(function (li) {
        var match = li.dataset.name.indexOf(q) !== -1;
        li.hidden = !match;
        if (match) { shown++; visible[li.dataset.group] = true; }
      });
      // A divider shows when its group and an earlier group both have a match.
      document.querySelectorAll("#fmtList li.side-group").forEach(function (divider) {
        var group = Number(divider.dataset.group);
        var earlier = Object.keys(visible).some(function (g) { return Number(g) < group; });
        divider.hidden = !(earlier && visible[group]);
      });
      document.getElementById("fmtEmpty").hidden = shown > 0;
    });
  }

  function item(f, group) {
    var active = f.page === CURRENT_PAGE;
    var search = (f.name + " " + f.others.join(" ")).toLowerCase();
    var meter = f.converted
      ? '<span class="fmt-pct" title="' + W.esc(W.shareTip(f)) + '" style="color:' + W.doneColor(W.share(f)) + '">' + Math.round(W.share(f) * 100) + "%</span>" + W.bar(f.known, f.unknown)
      : '<span class="fmt-pct muted">-</span>';
    return '<li data-name="' + W.esc(search) + '" data-group="' + group + '"><a class="fmt' + (active ? " active" : "") + '" href="' + W.esc(f.page) + '"' +
      (active ? ' aria-current="page"' : "") + '><span class="fmt-name">' + W.esc(f.name) + "</span>" + meter +
      '<span class="fmt-counts">' + W.countChip(f.oq, "q", "?", "open question", "open questions") +
      W.countChip(f.ig, "ig", "⌖", "in-game check", "in-game checks") + "</span></a></li>";
  }

  // Shows layout `n`: its panel, its band on the timeline (or its tab), its Versions bar, the pill and the readout.
  function showLayout(n) {
    var key = String(n);
    document.querySelectorAll("#layoutTabs button").forEach(function (b) {
      var on = b.dataset.layout === key;
      b.classList.toggle("active", on);
      b.setAttribute("aria-selected", on ? "true" : "false");
    });
    document.querySelectorAll(".tl-band[data-layout]").forEach(function (b) {
      var on = b.dataset.layout === key;
      b.classList.toggle("sel", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
    document.querySelectorAll(".ver[data-layout]").forEach(function (v) { v.classList.toggle("sel", v.dataset.layout === key); });
    document.querySelectorAll(".layout-panel").forEach(function (p) { p.hidden = p.dataset.layout !== key; });
    var source = document.querySelector('[data-layout="' + key + '"][data-pill]');
    var pill = document.getElementById("layoutPill");
    if (source && pill) pill.textContent = source.dataset.pill;
    if (source && source.dataset.read) setReadout("Layout " + key, source.dataset.read);
    try { localStorage.setItem("pazdocs-layout-" + CURRENT_PAGE, key); } catch (e) { /* storage blocked */ }
  }

  function setReadout(name, text) {
    var nameEl = document.getElementById("tlReadName");
    var textEl = document.getElementById("tlReadText");
    if (nameEl && textEl) { nameEl.textContent = name; textEl.textContent = text; }
  }

  // The layout picker is the timeline's bands, or the tabs on a doc without Versions rows.
  function initLayoutPicker() {
    var pickers = document.querySelectorAll(".tl-band[data-layout], #layoutTabs button[data-layout]");
    if (!pickers.length) return;
    var saved = null;
    try { saved = localStorage.getItem("pazdocs-layout-" + CURRENT_PAGE); } catch (e) { saved = null; }
    var valid = saved !== null && document.querySelector('.layout-panel[data-layout="' + saved + '"]');
    var initial = document.querySelector(".tl-band.sel[data-layout], #layoutTabs button.active") || pickers[0];
    showLayout(valid ? saved : initial.dataset.layout);
    document.addEventListener("click", function (ev) {
      var btn = ev.target.closest(".tl-band[data-layout], #layoutTabs button[data-layout]");
      if (btn) showLayout(btn.dataset.layout);
    });
    var track = document.querySelector(".tl-track");
    if (track) {
      thinLabels(track);
      window.addEventListener("resize", function () { thinLabels(track); });
    }
  }

  // Timeline labels that would touch: a layout label shortens to "L7", then labels and ticks thin out left to right.
  var LABEL_GAP_PX = 10;
  function thinLabels(track) {
    var ticks = Array.prototype.slice.call(track.querySelectorAll(".tl-tick"));
    var labels = Array.prototype.slice.call(track.querySelectorAll(".tl-band-label"));
    ticks.concat(labels).forEach(function (el) { el.classList.remove("thin"); });
    labels.forEach(function (el) {
      var band = el.parentElement;
      if (band.dataset.layout) el.textContent = "Layout " + band.dataset.layout;
    });
    labels.forEach(function (el) {
      var band = el.parentElement;
      if (band.dataset.layout && labels.some(function (other) { return other !== el && overlaps(el, other); })) el.textContent = "L" + band.dataset.layout;
    });
    labels.forEach(function (el) { keepInside(el, track); });
    thinRow(ticks);
    thinRow(labels);
  }

  // A label wider than a band at either end of the track aligns to that end instead of running past it.
  function keepInside(label, track) {
    label.classList.remove("to-start", "to-end");
    var box = label.getBoundingClientRect(), edges = track.getBoundingClientRect();
    if (box.right > edges.right) label.classList.add("to-end");
    else if (box.left < edges.left) label.classList.add("to-start");
  }

  function overlaps(a, b) {
    var x = a.getBoundingClientRect(), y = b.getBoundingClientRect();
    return x.left < y.right + LABEL_GAP_PX && y.left < x.right + LABEL_GAP_PX;
  }

  function thinRow(items) {
    var sorted = items.slice().sort(function (a, b) { return a.getBoundingClientRect().left - b.getBoundingClientRect().left; });
    var lastRight = -Infinity;
    sorted.forEach(function (el) {
      var box = el.getBoundingClientRect();
      var keep = el.parentElement.classList.contains("sel") || box.left - lastRight >= LABEL_GAP_PX;
      el.classList.toggle("thin", !keep);
      if (keep) lastRight = box.right;
    });
  }

  // Pointing at a byte lights up its field's bytes and table row, and the reverse.
  function initHover() {
    var panels = document.getElementById("layoutPanels");
    if (!panels) return;
    function clear(card) {
      card.querySelectorAll(".hl").forEach(function (el) { el.classList.remove("hl"); });
    }
    panels.addEventListener("mouseover", function (ev) {
      var target = ev.target.closest("[data-f]");
      var card = ev.target.closest("[data-struct]");
      if (!card) return;
      clear(card);
      var readout = card.querySelector(".readout");
      if (!target) return;
      var index = target.dataset.f;
      card.querySelectorAll('[data-f="' + index + '"]').forEach(function (el) { el.classList.add("hl"); });
      var row = card.querySelector('tr[data-f="' + index + '"]');
      if (row && readout) {
        var cells = row.querySelectorAll("td");
        var name = cells[2].querySelector(".field-name");
        // The Type cell is built from escaped tokens; a structure's link is left out.
        var type = cells[1].querySelector("a") || cells[1];
        readout.innerHTML = "<b>" + W.esc(cells[0].textContent) + "</b>  " + type.innerHTML + "  <b>" +
          W.esc(cells[2].textContent) + "</b>  " + W.esc(name ? name.title : "");
      }
    });
    panels.addEventListener("mouseleave", function () {
      panels.querySelectorAll("[data-struct]").forEach(clear);
    });
  }

  renderFormats();
  initLayoutPicker();
  initHover();
})();
