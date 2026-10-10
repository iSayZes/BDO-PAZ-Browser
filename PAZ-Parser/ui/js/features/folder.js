"use strict";

import { t } from "../core/i18n.js";
import { iconSvg } from "../core/icons.js";

export const folderMethods = {
  // Drops data-i18n, so applyTranslations() (on a settings save) keeps the
  // path instead of writing "No folder selected" back.
  _showFolderPath(path) {
    const el = document.getElementById("folder-path");
    el.textContent = path;
    el.classList.remove("muted");
    el.removeAttribute("data-i18n");
  },

  async openFolder() {
    await this._showTreeLoading();
    const result = await window.pywebview.api.open_folder();
    if (result.ok) {
      this._showFolderPath(result.path);
    } else if (this._isFolderLoaded) {
      // Cancelled: the backend still holds the previous folder, so bring
      // its tree and search back.
      this._loadTreeRoot();
    } else {
      document.getElementById("tree").innerHTML = "";
    }
  },

  // No PAZ folder yet: a card in the preview that says what to pick.
  _showFirstRun() {
    document.getElementById("preview-content").innerHTML =
      '<section class="first-run">' +
      `<div class="first-run-icon">${iconSvg("archive")}</div>` +
      `<h2>${this._esc(t("status.openFolder"))}</h2>` +
      `<p>${this._esc(t("firstRun.body"))}</p>` +
      '<button class="btn-primary with-icon" onclick="app.openFolder()">' +
      `${iconSvg("folder")}<span>${this._esc(t("toolbar.openFolder"))}</span></button>` +
      "</section>";
  },

  onFolderLoaded() {
    this._isFolderLoaded = true;
    const content = document.getElementById("preview-content");
    if (content.querySelector(".first-run")) {
      content.innerHTML = `<div class="placeholder">${this._esc(t("preview.selectFile"))}</div>`;
    }
    this._loadTreeRoot();
    this.checkLocWarning();
  },
};
