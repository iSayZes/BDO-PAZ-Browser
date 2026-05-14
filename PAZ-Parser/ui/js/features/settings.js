"use strict";

import { loadLang, applyTranslations } from "../core/i18n.js";

export const settingsMethods = {
  _settingsEscHandler: null,

  async openSettings() {
    const s = await window.pywebview.api.get_settings();
    document.getElementById("settings-paz-path").value = s.paz_path ?? "";
    document.getElementById("settings-language").value = s.language ?? "en";
    document.getElementById("settings-table-row-height").value = s.table_row_height ?? 27;
    document.getElementById("settings-overlay").hidden = false;

    this._settingsEscHandler = (e) => {
      if (e.key === "Escape") this.closeSettings();
    };
    document.addEventListener("keydown", this._settingsEscHandler);
  },

  closeSettings() {
    document.getElementById("settings-overlay").hidden = true;
    if (this._settingsEscHandler) {
      document.removeEventListener("keydown", this._settingsEscHandler);
      this._settingsEscHandler = null;
    }
  },

  async browseSettingsPazFolder() {
    const result = await window.pywebview.api.browse_folder();
    if (result?.ok && result.path) {
      document.getElementById("settings-paz-path").value = result.path;
    }
  },

  async saveSettings() {
    const pazPath = document.getElementById("settings-paz-path").value.trim();
    const language = document.getElementById("settings-language").value;
    const tableRowHeight = Number(document.getElementById("settings-table-row-height").value);
    const result = await window.pywebview.api.save_settings(pazPath, language, tableRowHeight);
    if (!result?.ok) return;
    this._applyTableRowHeight(result.table_row_height ?? tableRowHeight);
    this.closeSettings();
    await loadLang(language);
    applyTranslations();
    if (this._selectedPath) {
      const node = document.querySelector(".tree-node.selected");
      const name = node?.querySelector(".tree-name")?.textContent ?? "";
      const icon = node?.querySelector(".tree-icon")?.textContent ?? "";
      await this._selectFile(this._selectedPath, name, icon);
    }
  },

  _applyTableRowHeight(value) {
    const height = Math.max(20, Math.min(64, Number.parseInt(value, 10) || 27));
    document.documentElement.style.setProperty("--table-row-height", `${height}px`);
  },
};
