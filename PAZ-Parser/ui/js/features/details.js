"use strict";

export const detailsMethods = {
  _setDetails(meta) {
    const grid = document.getElementById("detail-grid");
    const rows = [
      ["📦  Archive", meta.archive],
      ["📍  Path", meta.path],
      ["🗜  Compressed", meta.compressed],
      ["📄  Uncompressed", meta.uncompressed],
      ["#  Offset", meta.offset],
    ];
    grid.innerHTML = rows
      .map(([label, value]) => `<div class="detail-label">${label}</div>` + `<div class="detail-value" title="${this._esc(value)}">${this._esc(value)}</div>`)
      .join("");
  },
};
