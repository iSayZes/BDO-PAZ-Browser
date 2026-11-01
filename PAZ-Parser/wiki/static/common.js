// Helpers both wiki pages use. FORMATS comes from formats.js, written by the wiki build.
var PazWiki = (function () {
  "use strict";

  function esc(text) {
    return String(text).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function inline(text) { return esc(text).replace(/`([^`]+)`/g, "<code>$1</code>"); }
  function num(n) { return n.toLocaleString("en-US"); }
  function share(f) { var total = f.known + f.unknown; return total ? f.known / total : 0; }

  // Where a known share comes from: the game files of one client, or the doc's fields alone.
  function shareTip(f) {
    var bytes = num(f.known) + " B known, " + num(f.unknown) + " B unknown";
    return f.client ? bytes + " in the client " + f.client + " files" : bytes + " over the doc's fixed-size fields, each structure once";
  }

  // The known share as a colour: red at 0%, amber at 50%, green at 100%.
  function doneColor(s) {
    var p = Math.max(0, Math.min(100, Math.round(s * 100)));
    if (p <= 50) return "color-mix(in oklab, var(--color-accent) " + p * 2 + "%, var(--color-danger))";
    return "color-mix(in oklab, var(--color-data) " + (p - 50) * 2 + "%, var(--color-accent))";
  }

  function bar(known, unknown) {
    var total = known + unknown || 1;
    return '<div class="covbar" aria-hidden="true"><span class="seg known" style="width:' + known / total * 100 +
      '%"></span><span class="seg unknown" style="width:' + unknown / total * 100 + '%"></span></div>';
  }

  function countChip(n, kind, glyph, one, many) {
    var label = n + " " + (n === 1 ? one : many);
    return '<span class="cnt ' + kind + (n ? "" : " zero") + '" title="' + label + '">' +
      '<span class="cnt-icon" aria-hidden="true">' + glyph + '</span><span aria-hidden="true">' + n + "</span>" +
      '<span class="sr">' + label + "</span></span>";
  }

  // A to Z by the shown name, ignoring leading symbols: `{alchemy,...}statdata.bss` sorts under A.
  function sortName(f) { return f.name.toLowerCase().replace(/^[^a-z0-9]+/, ""); }

  // The app's tree view order: the LOC files, the .bss / .dbss tables, every other format, then the Lua script docs.
  var GROUP_LABELS = ["", "", "Others", "Lua"];
  var EXT_GROUPS = { other: 2, lua: 3 };
  function groupOf(f) { return /_loc\.html$/.test(f.page) ? 0 : EXT_GROUPS[f.ext] || 1; }

  // The groups of `sorted` that hold a doc, each keeping its order; every group after the first gets a divider.
  function groups(sorted) {
    return GROUP_LABELS.map(function (label, index) {
      return { index: index, label: label, items: sorted.filter(function (f) { return groupOf(f) === index; }) };
    }).filter(function (group) { return group.items.length; }).map(function (group, position) {
      return { index: group.index, label: group.label, items: group.items, divider: position > 0 };
    });
  }

  return { esc: esc, inline: inline, num: num, share: share, shareTip: shareTip, doneColor: doneColor, bar: bar, countChip: countChip, sortName: sortName, groups: groups };
})();
