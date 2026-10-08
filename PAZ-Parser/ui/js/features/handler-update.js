"use strict";

import { t } from "../core/i18n.js";

// Handler packs in the exe: the backend installs a newer pack in the
// background on start (or on "Check now" in the settings), and this popup
// offers the restart that puts it to use. The bottom bar shows the app's
// version and, for a file a handler reads, that handler's version (its pack
// version, or from source the commit that last changed it).
export const handlerUpdateMethods = {
  // get_app_version(): label, commit, handlers (the running pack's version or null).
  _appVersion: null,
  _handlerUpdateEscHandler: null,

  async showAppVersion() {
    this._appVersion = await window.pywebview.api.get_app_version();
    this._renderAppVersion(null);
  },

  // After a file is selected: its handler's version joins the app's.
  async showHandlerVersion(name) {
    const seq = this._selectSeq;
    const handler = name ? await window.pywebview.api.get_handler_version(name) : {};
    if (seq !== this._selectSeq) return;
    this._renderAppVersion(handler?.version ? handler : null);
  },

  _renderAppVersion(handler) {
    const version = this._appVersion;
    if (!version) return;
    const label = document.getElementById("app-version");
    label.textContent = handler
      ? `${version.label} · ${t("footer.handler", { key: handler.key, version: handler.version })}`
      : version.label;
    const lines = [];
    if (version.commit) lines.push(t("footer.commit", { commit: version.commit }));
    if (version.handlers) lines.push(t("footer.handlers", { version: version.handlers }));
    label.title = lines.join("\n");
  },

  // Pushed by the backend once a newer pack is installed.
  onHandlersUpdated(info) {
    document.getElementById("handler-update-title").textContent = t("handlerUpdate.title", { version: info.version });
    document.getElementById("handler-update-current").textContent = info.current
      ? t("handlerUpdate.current", { version: info.current })
      : t("handlerUpdate.currentBundled");
    document.getElementById("handler-update-notes").innerHTML = info.notes_html ?? "";
    document.getElementById("handler-update-restart").disabled = false;
    document.getElementById("handler-update-overlay").hidden = false;
    if (!this._handlerUpdateEscHandler) {
      this._handlerUpdateEscHandler = (event) => {
        if (event.key === "Escape") this.closeHandlerUpdate();
      };
      document.addEventListener("keydown", this._handlerUpdateEscHandler);
    }
  },

  // The new pack stays installed and runs from the next start.
  closeHandlerUpdate() {
    document.getElementById("handler-update-overlay").hidden = true;
    if (this._handlerUpdateEscHandler) {
      document.removeEventListener("keydown", this._handlerUpdateEscHandler);
      this._handlerUpdateEscHandler = null;
    }
  },

  async restartForHandlers() {
    const button = document.getElementById("handler-update-restart");
    button.disabled = true;
    const result = await window.pywebview.api.restart_app();
    if (!result?.ok) {
      button.disabled = false;
      this.showError(result?.error ?? "");
    }
  },

  async checkHandlersNow() {
    const button = document.getElementById("settings-check-handlers");
    const output = document.getElementById("settings-handlers-result");
    button.disabled = true;
    output.textContent = t("handlerUpdate.checking");
    try {
      const result = await window.pywebview.api.check_handler_update();
      output.textContent = result?.message ?? "";
      if (result?.installed) {
        this.closeSettings();
        this.onHandlersUpdated(result.installed);
      }
    } finally {
      button.disabled = false;
    }
  },

  _setupHandlerUpdate() {
    // A click on the dimmed backdrop closes, a click inside the popup does not.
    document.getElementById("handler-update-overlay").addEventListener("click", (event) => {
      if (event.target.id === "handler-update-overlay") this.closeHandlerUpdate();
    });
  },
};
