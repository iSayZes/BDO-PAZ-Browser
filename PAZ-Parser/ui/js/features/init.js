"use strict";

export const initMethods = {
  async init() {
    const saved = localStorage.getItem("outputPath");
    if (saved) document.getElementById("output-path").value = saved;

    const status = await window.pywebview.api.get_status();
    this.setStatus(status);

    this._setupDividers();
    this._setupOutputPathSave();
    this._setupPreviewTableSelection();
    this._setupEscapeClear();
    this._setupImageZoom();
    this._initTabSearch();

    const last = await window.pywebview.api.get_last_folder();
    if (last && last.path) {
      const el = document.getElementById("folder-path");
      el.textContent = last.path;
      el.classList.remove("muted");
      await this._showTreeLoading();
      window.pywebview.api.open_folder_path(last.path);
    }
  },
};
