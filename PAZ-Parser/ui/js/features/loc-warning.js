"use strict";

import { t } from "../core/i18n.js";

// The corner warning for a language whose LOC file the client lacks: the UI
// is translated, but the tables cannot show game text in that language.
// Shown after a folder loads and after the settings are saved.
export const locWarningMethods = {
  // The language the shown warning is for. Dismissing it keeps it closed for
  // good (the backend saves it); the settings still mark the language.
  _locWarningLanguage: null,

  async checkLocWarning() {
    const warning = await window.pywebview.api.get_loc_warning();
    const box = document.getElementById("loc-warning");
    if (!warning?.file) {
      box.hidden = true;
      return;
    }
    document.getElementById("loc-warning-text").textContent = t("locWarning.missing", {
      file: warning.file,
      language: warning.name,
    });
    this._locWarningLanguage = warning.language;
    box.hidden = false;
  },

  // The toast's link: pick another language in the settings.
  openSettingsFromLocWarning() {
    document.getElementById("loc-warning").hidden = true;
    this.openSettings();
  },

  dismissLocWarning() {
    document.getElementById("loc-warning").hidden = true;
    if (this._locWarningLanguage) {
      window.pywebview.api.dismiss_loc_warning(this._locWarningLanguage);
    }
  },
};
