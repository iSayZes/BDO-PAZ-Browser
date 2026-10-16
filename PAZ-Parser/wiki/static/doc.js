// A doc page: the format list in the sidebar, the layout tabs and the byte map hover.
// The page content itself is static HTML; CURRENT_PAGE names this page's file.
(function () {
  "use strict";
  var W = PazWiki;

  function renderFormats() {
    var sorted = FORMATS.slice().sort(function (a, b) { return W.sortName(a).localeCompare(W.sortName(b)); });
    var items = sorted.map(function (f) {
      var active = f.page === CURRENT_PAGE;
      var search = (f.name + " " + f.others.join(" ")).toLowerCase();
      var meter = f.converted
        ? '<span class="fmt-pct" style="color:' + W.doneColor(W.share(f)) + '">' + Math.round(W.share(f) * 100) + "%</span>" + W.bar(f.known, f.unknown)
        : '<span class="fmt-pct muted">-</span>';
      return '<li data-name="' + W.esc(search) + '"><a class="fmt' + (active ? " active" : "") + '" href="' + W.esc(f.page) + '"' +
        (active ? ' aria-current="page"' : "") + '><span class="fmt-name">' + W.esc(f.name) + "</span>" + meter +
        '<span class="fmt-counts">' + W.countChip(f.oq, "q", "?", "open question", "open questions") +
        W.countChip(f.ig, "ig", "⌖", "in-game check", "in-game checks") + "</span></a></li>";
    });
    var list = document.getElementById("fmtList");
    list.innerHTML = items.join("");
    var current = list.querySelector(".fmt.active");
    if (current) list.scrollTop = current.parentElement.offsetTop - list.clientHeight / 2;
    document.getElementById("fmtFilter").addEventListener("input", function (ev) {
      var q = ev.target.value.trim().toLowerCase();
      var shown = 0;
      document.querySelectorAll("#fmtList li").forEach(function (li) {
        var match = li.dataset.name.indexOf(q) !== -1;
        li.hidden = !match;
        if (match) shown++;
      });
      document.getElementById("fmtEmpty").hidden = shown > 0;
    });
  }

  function showLayout(n) {
    document.querySelectorAll("#layoutTabs button").forEach(function (b) {
      var on = b.dataset.layout === String(n);
      b.classList.toggle("active", on);
      b.setAttribute("aria-selected", on ? "true" : "false");
    });
    document.querySelectorAll(".layout-panel").forEach(function (p) {
      p.hidden = p.dataset.layout !== String(n);
    });
    try { localStorage.setItem("pazdocs-layout-" + CURRENT_PAGE, String(n)); } catch (e) { /* storage blocked */ }
  }

  function initLayoutTabs() {
    var tabs = document.getElementById("layoutTabs");
    if (!tabs) return;
    var saved = null;
    try { saved = localStorage.getItem("pazdocs-layout-" + CURRENT_PAGE); } catch (e) { saved = null; }
    var valid = saved !== null && document.querySelector('#layoutTabs button[data-layout="' + saved + '"]');
    showLayout(valid ? saved : tabs.querySelector("button").dataset.layout);
    tabs.addEventListener("click", function (ev) {
      var btn = ev.target.closest("button[data-layout]");
      if (btn) showLayout(btn.dataset.layout);
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
        readout.innerHTML = "<b>" + W.esc(cells[0].textContent) + "</b>  " + W.esc(cells[1].textContent) + "  <b>" +
          W.esc(cells[2].textContent) + "</b>  " + W.esc(name ? name.title : "");
      }
    });
    panels.addEventListener("mouseleave", function () {
      panels.querySelectorAll("[data-struct]").forEach(clear);
    });
  }

  renderFormats();
  initLayoutTabs();
  initHover();
})();
