"use strict";

import { loadLang, applyTranslations, t } from "../core/i18n.js";

// Tree id prefix of the files read from disk (`_DISK_VIRTUAL_PREFIX` in api/bdo_api_helpers.py).
const DISK_PREFIX = "__disk__";

export const settingsMethods = {
  _settingsEscHandler: null,
  // The handled-only and language settings as the modal opened, to spot a change on save.
  _savedHandledOnly: false,
  _savedLanguage: "en",
  // The "Data Folder" setting as the modal opened; "" is the default folder.
  _savedDataFolder: "",
  // UI language code -> the LOC file this client lacks for it.
  _missingLoc: {},
  // True while save_settings() runs; the modal stays open and cannot close.
  _isSavingSettings: false,

  async openSettings() {
    const s = await window.pywebview.api.get_settings();
    document.getElementById("settings-paz-path").value = s.paz_path ?? "";
    this._fillLanguages(s.languages ?? [], s.missing_loc ?? {});
    document.getElementById("settings-language").value = s.language ?? "en";
    this.showLanguageLocWarning();
    document.getElementById("settings-table-row-height").value = s.table_row_height ?? 27;
    document.getElementById("settings-show-pa-tags").checked = s.show_pa_tags === true;
    document.getElementById("settings-handled-only").checked = s.handled_only === true;
    document.getElementById("settings-check-app-updates-row").hidden = !s.app_version;
    document.getElementById("settings-check-app-updates").checked = s.check_app_updates !== false;
    document.getElementById("settings-update-handlers-row").hidden = !s.app_version;
    document.getElementById("settings-update-handlers").checked = s.update_handlers !== false;
    document.getElementById("settings-handlers-result").textContent = "";
    document.getElementById("settings-records-cache").value = s.records_cache ?? "open";
    const dataFolder = document.getElementById("settings-data-folder");
    dataFolder.value = s.data_folder ?? "";
    dataFolder.placeholder = s.default_data_folder ?? "";
    this._savedDataFolder = dataFolder.value;
    this._showCacheSize(s.cache_bytes ?? 0);
    this._savedHandledOnly = s.handled_only === true;
    this._savedLanguage = s.language ?? "en";
    document.getElementById("settings-overlay").hidden = false;

    this._settingsEscHandler = (e) => {
      if (e.key === "Escape") this.closeSettings();
    };
    document.addEventListener("keydown", this._settingsEscHandler);
  },

  _fillLanguages(languages, missingLoc) {
    this._missingLoc = missingLoc;
    const select = document.getElementById("settings-language");
    select.replaceChildren(...languages.map(({ code, name }) => new Option(name, code)));
  },

  // The warning icon next to the language list, also for a dismissed corner warning.
  showLanguageLocWarning() {
    const select = document.getElementById("settings-language");
    const file = this._missingLoc[select.value];
    const icon = document.getElementById("settings-language-warning");
    icon.hidden = !file;
    icon.title = file
      ? t("locWarning.missing", { file, language: select.selectedOptions[0]?.text ?? select.value })
      : "";
  },

  closeSettings() {
    if (this._isSavingSettings) return;
    document.getElementById("settings-overlay").hidden = true;
    if (this._settingsEscHandler) {
      document.removeEventListener("keydown", this._settingsEscHandler);
      this._settingsEscHandler = null;
    }
  },

  async browseSettingsPazFolder() {
    await this._browseInto("settings-paz-path");
  },

  async browseSettingsDataFolder() {
    await this._browseInto("settings-data-folder");
  },

  async _browseInto(inputId) {
    const result = await window.pywebview.api.browse_folder();
    if (result?.ok && result.path) {
      document.getElementById(inputId).value = result.path;
    }
  },

  async saveSettings() {
    const pazPath = document.getElementById("settings-paz-path").value.trim();
    const language = document.getElementById("settings-language").value;
    const tableRowHeight = Number(document.getElementById("settings-table-row-height").value);
    const showPaTags = document.getElementById("settings-show-pa-tags").checked;
    const handledOnly = document.getElementById("settings-handled-only").checked;
    const checkAppUpdates = document.getElementById("settings-check-app-updates").checked;
    const updateHandlers = document.getElementById("settings-update-handlers").checked;
    const recordsCache = document.getElementById("settings-records-cache").value;
    const dataFolder = document.getElementById("settings-data-folder").value.trim();
    if (this._isSavingSettings) return;
    // A new data folder deletes the caches in the old one.
    if (dataFolder !== this._savedDataFolder && !window.confirm(t("settings.dataFolderConfirm"))) return;
    // A new language rebuilds the game text index, which takes a few seconds.
    this._showSettingsSaving(true);
    let result;
    try {
      result = await window.pywebview.api.save_settings(
        pazPath, language, tableRowHeight, showPaTags, handledOnly, recordsCache, dataFolder, checkAppUpdates,
        updateHandlers,
      );
    } finally {
      this._showSettingsSaving(false);
    }
    if (!result?.ok) {
      if (result?.error) this.showError(result.error);
      return;
    }
    if (result.cache_error) this.showError(t("settings.cachesDeleteFailed", { message: result.cache_error }));
    this._applyTableRowHeight(result.table_row_height ?? tableRowHeight);
    this.closeSettings();
    await loadLang(language);
    applyTranslations();
    this.checkLocWarning();
    const languageChanged = language !== this._savedLanguage;
    if (this._selectedPath) {
      await this._reselectAfterSettings(languageChanged ? result.loc_file : undefined);
    }
    // After the reselect, which reads the selected node from the old tree.
    if ((handledOnly !== this._savedHandledOnly || languageChanged) && this._isFolderLoaded) {
      this._reloadTree();
    }
  },

  // Save shows a spinner, and the buttons that would close the modal wait for it.
  _showSettingsSaving(isSaving) {
    this._isSavingSettings = isSaving;
    const save = document.getElementById("settings-save");
    save.classList.toggle("btn-busy", isSaving);
    save.setAttribute("aria-busy", String(isSaving));
    if (isSaving) {
      save.innerHTML = `<span class="loading-spinner" aria-hidden="true"></span><span>${t("settings.saving")}</span>`;
    } else {
      save.textContent = t("settings.save");
    }
    for (const button of document.querySelectorAll("#settings-overlay .settings-footer button, #settings-overlay .settings-close")) {
      button.disabled = isSaving;
    }
  },

  // Open the selected file again, now in the new settings. After a language
  // change, `locFile` names the new language's LOC file and a selected LOC
  // file becomes that one; with none loaded, the preview says so.
  async _reselectAfterSettings(locFile) {
    const node = document.querySelector(".tree-node.selected");
    let path = this._selectedPath;
    let name = node?.querySelector(".tree-name")?.textContent ?? "";
    const icon = node?.dataset.icon ?? "file";
    if (locFile && path.startsWith(`${DISK_PREFIX}/`)) {
      path = `${DISK_PREFIX}/${locFile}`;
      name = locFile;
    }
    await this._selectFile(path, name, icon);
  },

  async deleteCaches() {
    if (!window.confirm(t("settings.deleteCachesConfirm"))) return;
    const button = document.getElementById("settings-delete-caches");
    button.disabled = true;
    try {
      const result = await window.pywebview.api.delete_caches();
      const size = document.getElementById("settings-cache-size");
      size.textContent = result?.ok
        ? t("settings.cachesDeleted", { size: this._fmtBytes(result.freed ?? 0) })
        : t("settings.cachesDeleteFailed", { message: result?.error ?? "" });
    } finally {
      button.disabled = false;
    }
  },

  _showCacheSize(bytes) {
    document.getElementById("settings-cache-size").textContent = t("settings.cacheSize", { size: this._fmtBytes(bytes) });
  },

  // The filter changes what the tree, file search and global search show, and
  // the language which LOC file sits at the root, so drop their results. A new
  // PAZ folder reloads the tree itself once loaded.
  _reloadTree() {
    if (this._inGlobalSearch) {
      this.cancelGlobalSearch();
      this._closeGlobalSearch();
    }
    this._loadTreeRoot();
  },

  _applyTableRowHeight(value) {
    const height = Math.max(20, Math.min(64, Number.parseInt(value, 10) || 27));
    document.documentElement.style.setProperty("--table-row-height", `${height}px`);
  },
};
