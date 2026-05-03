"use strict";

export const folderMethods = {
  async openFolder() {
    const result = await window.pywebview.api.open_folder();
    if (result.ok) {
      const el = document.getElementById("folder-path");
      el.textContent = result.path;
      el.classList.remove("muted");
    }
  },

  onFolderLoaded() {
    this._loadTreeRoot();
  },
};
