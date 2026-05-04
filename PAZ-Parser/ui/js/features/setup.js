"use strict";

export const setupMethods = {
  _setupOutputPathSave() {
    document.getElementById("output-path").addEventListener("change", (e) => {
      localStorage.setItem("outputPath", e.target.value);
    });
  },

  _setupImageZoom() {
    const content = document.getElementById("preview-content");
    content.addEventListener("wheel", (e) => {
      if (!e.ctrlKey) return;
      const img = content.querySelector(".img-view img");
      if (!img) return;
      e.preventDefault();
      const current = parseFloat(img.style.zoom) || 1;
      const delta = e.deltaY < 0 ? 0.1 : -0.1;
      img.style.zoom = Math.max(0.1, Math.round((current + delta) * 10) / 10);
    }, { passive: false });
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
