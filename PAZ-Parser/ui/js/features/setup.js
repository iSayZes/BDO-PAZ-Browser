"use strict";

export const setupMethods = {
  _setupOutputPathSave() {
    document.getElementById("output-path").addEventListener("change", (e) => {
      localStorage.setItem("outputPath", e.target.value);
    });
  },

  _setupEscapeClear() {
    document.addEventListener("keydown", (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "f") {
        e.preventDefault();
        this.openTabSearch();
        return;
      }
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "r") {
        e.preventDefault();
        window.pywebview.api.reload_plugins();
        return;
      }
      if (e.key === "Escape" && this._extractPaths.size > 0) {
        this._clearExtractSelection();
      }
    });
  },
};
