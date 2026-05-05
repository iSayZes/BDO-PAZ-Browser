"use strict";

export const folderMethods = {
  async openFolder() {
    await this._showTreeLoading();
    const result = await window.pywebview.api.open_folder();
    if (result.ok) {
      const el = document.getElementById("folder-path");
      el.textContent = result.path;
      el.classList.remove("muted");
    } else {
      document.getElementById("tree").innerHTML = "";
    }
  },

  onFolderLoaded() {
    this._loadTreeRoot();
  },
};
