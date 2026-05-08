"use strict";

import { t } from "../core/i18n.js";

export const detailsMethods = {
  _setDetails(meta) {
    const grid = document.getElementById("detail-grid");
    const rows = [
      [t("details.archive"), meta.archive],
      [t("details.path"), meta.path],
      [t("details.compressed"), meta.compressed],
      [t("details.uncompressed"), meta.uncompressed],
      [t("details.offset"), meta.offset],
    ];
    grid.innerHTML = rows
      .map(([label, value]) => `<div class="detail-label">${label}</div>` + `<div class="detail-value" title="${this._esc(value)}">${this._esc(value)}</div>`)
      .join("");
  },
};
