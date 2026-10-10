"use strict";

import { t } from "../core/i18n.js";

// The entry strip above the preview, and its Export menu.
export const detailsMethods = {
  _exportMenuCloser: null,

  _setDetails(meta) {
    const items = [
      ["archive", meta.archive, "detail-item-key"],
      ["path", meta.path, "detail-item-path"],
      ["compressed", meta.compressed, ""],
      ["uncompressed", meta.uncompressed, ""],
      ["offset", meta.offset, ""],
    ];
    document.getElementById("detail-grid").innerHTML = items
      .map(([key, value, extra]) => {
        const text = this._esc(value);
        return `<div class="detail-item ${extra}"><span class="detail-label">${t(`details.${key}`)}</span>`
          + `<span class="detail-value" title="${text}">${text}</span></div>`;
      })
      .join("");
  },

  toggleExportMenu() {
    if (document.getElementById("export-menu").hidden) this._openExportMenu();
    else this.closeExportMenu();
  },

  // "Table as CSV" needs the records of a parsed table (see _selectFile).
  _openExportMenu() {
    document.getElementById("export-csv").disabled = !this._canExportCsv;
    document.getElementById("export-menu").hidden = false;
    document.getElementById("btn-export").setAttribute("aria-expanded", "true");
    const wrap = document.querySelector(".export-wrap");
    const onPointer = (event) => {
      if (!wrap.contains(event.target)) this.closeExportMenu();
    };
    const onKey = (event) => {
      if (event.key === "Escape") this.closeExportMenu();
    };
    document.addEventListener("mousedown", onPointer);
    document.addEventListener("keydown", onKey);
    this._exportMenuCloser = () => {
      document.removeEventListener("mousedown", onPointer);
      document.removeEventListener("keydown", onKey);
    };
  },

  closeExportMenu() {
    document.getElementById("export-menu").hidden = true;
    document.getElementById("btn-export").setAttribute("aria-expanded", "false");
    this._exportMenuCloser?.();
    this._exportMenuCloser = null;
  },

  // `kind` is "raw" (the file's bytes) or "csv" (the parsed table).
  async exportAs(kind) {
    this.closeExportMenu();
    if (!this._selectedPath) return;
    const tab = kind === "csv" ? "parsed" : "hex";
    const result = await window.pywebview.api.export_file(this._selectedPath, tab);
    if (result?.error) {
      this.setStatus({ key: "status.exportFailed", args: { message: result.error } });
    }
  },
};
