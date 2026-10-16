// The index page: summary, filters and the sortable table of every format doc.
(function () {
  "use strict";
  var W = PazWiki;
  var state = { q: "", ext: "", onlyQ: false, onlyIg: false, sort: "name", dir: 1 };

  function renderSummary() {
    var known = 0, unknown = 0, oq = 0, ig = 0, withQ = 0, withIg = 0, full = 0;
    FORMATS.forEach(function (f) {
      oq += f.oq; ig += f.ig;
      if (f.oq) withQ++;
      if (f.ig) withIg++;
      if (!f.converted) return;
      known += f.known; unknown += f.unknown;
      if (!f.unknown) full++;
    });
    var s = W.share({ known: known, unknown: unknown });
    document.getElementById("summary").innerHTML =
      '<div class="sum overall"><span class="sum-label">Known</span>' +
      '<span class="sum-value" style="color:' + W.doneColor(s) + '">' + (s * 100).toFixed(1) + "%</span>" + W.bar(known, unknown) +
      '<span class="sum-sub">' + W.num(known) + " of " + W.num(known + unknown) + " documented bytes, converted docs only</span></div>" +
      documentedTile() +
      '<div class="sum"><span class="sum-label">Fully known</span><span class="sum-value">' + full + "</span>" +
      '<span class="sum-sub">no <code>unknown_*</code> field</span></div>' +
      '<div class="sum"><span class="sum-label">Open questions</span><span class="sum-value">' + oq + "</span>" +
      '<span class="sum-sub">in ' + withQ + " docs</span></div>" +
      '<div class="sum"><span class="sum-label">In-game checks</span><span class="sum-value">' + ig + "</span>" +
      '<span class="sum-sub">in ' + withIg + " docs</span></div>";
  }

  // How many of the game's .bss and .dbss files have a doc, by type.
  function documentedTile() {
    var documented = 0, total = 0, parts = [];
    ["bss", "dbss"].forEach(function (ext) {
      var count = SUMMARY.documented[ext] || 0;
      var all = SUMMARY.totals[ext];
      documented += count;
      total += all || 0;
      parts.push("." + ext + " " + count + (all ? "/" + all : ""));
    });
    var value = total ? documented + '<span class="sum-of"> of ' + W.num(total) + "</span>" : String(documented);
    return '<div class="sum"><span class="sum-label">Documented</span><span class="sum-value">' + value + "</span>" +
      '<span class="sum-sub">formats in the game: ' + parts.join(", ") + "</span></div>";
  }

  function matches(f) {
    if (state.ext && f.ext !== state.ext) return false;
    if (state.onlyQ && !f.oq) return false;
    if (state.onlyIg && !f.ig) return false;
    if (!state.q) return true;
    var hay = (f.name + " " + f.others.join(" ") + " " + f.desc).toLowerCase();
    return hay.indexOf(state.q) !== -1;
  }

  // Unconverted docs sort below every converted one when sorting by the known share.
  function knownKey(f) { return f.converted ? W.share(f) : -1; }

  function compare(a, b) {
    var x, y;
    if (state.sort === "known") { x = knownKey(a); y = knownKey(b); }
    else if (state.sort === "oq") { x = a.oq; y = b.oq; }
    else if (state.sort === "ig") { x = a.ig; y = b.ig; }
    else return state.dir * W.sortName(a).localeCompare(W.sortName(b));
    if (x < y) return -state.dir;
    if (x > y) return state.dir;
    return W.sortName(a).localeCompare(W.sortName(b));
  }

  function knownCell(f) {
    if (!f.converted) return '<span class="muted" title="Not in the layout format yet">not converted</span>';
    var s = W.share(f);
    var tip = W.num(f.known) + " B known, " + W.num(f.unknown) + " B unknown";
    return '<div class="known-cell" title="' + tip + '">' + W.bar(f.known, f.unknown) +
      '<span class="known-pct" style="color:' + W.doneColor(s) + '">' + Math.round(s * 100) + "%</span></div>";
  }

  function row(f) {
    var files = f.others.length
      ? '<div class="fmt-files">' + f.others.map(function (o) { return "<span>" + W.esc(o) + "</span>"; }).join("") + "</div>"
      : "";
    return '<tr><td><a class="fmt-name" href="' + W.esc(f.page) + '">' + W.esc(f.name) + "</a>" + files +
      '</td><td class="desc">' + W.inline(f.desc) + '</td><td class="num">' + knownCell(f) + "</td>" +
      '<td class="num">' + W.countChip(f.oq, "q", "?", "open question", "open questions") + "</td>" +
      '<td class="num">' + W.countChip(f.ig, "ig", "⌖", "in-game check", "in-game checks") + "</td></tr>";
  }

  function render() {
    var shown = FORMATS.filter(matches).sort(compare);
    var body = document.querySelector("#index tbody");
    body.innerHTML = shown.length
      ? shown.map(row).join("")
      : '<tr class="empty-row"><td colspan="5">No format matches these filters. Clear the search or a filter to see more.</td></tr>';
    document.getElementById("resultCount").textContent = shown.length === FORMATS.length
      ? FORMATS.length + " docs"
      : shown.length + " of " + FORMATS.length + " docs";
    document.querySelectorAll("#index th.sortable").forEach(function (th) {
      var on = th.dataset.sort === state.sort;
      th.setAttribute("aria-sort", on ? (state.dir === 1 ? "ascending" : "descending") : "none");
    });
  }

  function sortBy(key) {
    if (state.sort === key) state.dir = -state.dir;
    else { state.sort = key; state.dir = key === "name" || key === "known" ? 1 : -1; }
    render();
  }

  function init() {
    document.getElementById("q").addEventListener("input", function (ev) {
      state.q = ev.target.value.trim().toLowerCase();
      render();
    });
    document.getElementById("extFilter").addEventListener("click", function (ev) {
      var btn = ev.target.closest("button[data-ext]");
      if (!btn) return;
      state.ext = btn.dataset.ext;
      document.querySelectorAll("#extFilter button").forEach(function (b) { b.classList.toggle("active", b === btn); });
      render();
    });
    ["onlyQ", "onlyIg"].forEach(function (key) {
      var btn = document.getElementById(key);
      btn.addEventListener("click", function () {
        state[key] = !state[key];
        btn.setAttribute("aria-pressed", state[key] ? "true" : "false");
        render();
      });
    });
    var head = document.querySelector("#index thead");
    head.addEventListener("click", function (ev) {
      var th = ev.target.closest("th.sortable");
      if (th) sortBy(th.dataset.sort);
    });
    head.addEventListener("keydown", function (ev) {
      var th = ev.target.closest("th.sortable");
      if (!th || (ev.key !== "Enter" && ev.key !== " ")) return;
      ev.preventDefault();
      sortBy(th.dataset.sort);
    });
  }

  renderSummary();
  init();
  render();
})();
