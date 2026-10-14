"use strict";

import { t } from "../core/i18n.js";
import { iconElement } from "../core/icons.js";

// The caches on the Settings tabs (`CACHE_KINDS` in api/bdo_api_cache_usage.py).
// Each tab's `.settings-cache-list[data-cache-tab]` lists its caches with size
// and Delete; General adds Delete all and the other PAZ folders' caches.
export const settingsCacheMethods = {
  // Bumped per load, so an older get_cache_usage() reply is dropped.
  _cacheUsageSeq: 0,

  async _loadCacheUsage() {
    const seq = ++this._cacheUsageSeq;
    const usage = await window.pywebview.api.get_cache_usage();
    if (seq === this._cacheUsageSeq) this._renderCacheUsage(usage ?? {});
  },

  _renderCacheUsage({ caches = [], other_clients: otherClients = [] }) {
    document.querySelectorAll(".settings-cache-list[data-cache-tab]").forEach((list) => {
      const rows = caches
        .filter((cache) => cache.tab === list.dataset.cacheTab)
        .map((cache) => this._cacheRow(cache));
      list.replaceChildren(...rows);
      list.hidden = rows.length === 0;
    });
    const total = caches.filter((cache) => cache.in_delete_all).reduce((sum, cache) => sum + cache.bytes, 0);
    this._showCacheSize(total);
    // No folder loaded: nothing of this client to delete.
    document.getElementById("settings-delete-caches").disabled = caches.length === 0;

    document.getElementById("settings-other-clients-list").replaceChildren(
      ...otherClients.map((client) => this._otherClientRow(client)),
    );
    document.getElementById("settings-other-clients").hidden = otherClients.length === 0;
  },

  _cacheRow({ id, bytes }) {
    const name = t(`settings.caches.${id}`);
    const row = this._cacheRowElement(name, bytes, (button) => this._deleteCache(id, button));
    row.dataset.cacheId = id;
    return row;
  },

  _otherClientRow({ id, folder, exists, bytes }) {
    const row = this._cacheRowElement(folder || id, bytes, (button) => this._deleteOtherClientCache(id, folder, button));
    row.dataset.clientId = id;
    row.querySelector(".settings-cache-name").classList.add("settings-cache-path");
    if (!exists) {
      const missing = document.createElement("span");
      missing.className = "settings-loc-pill";
      missing.textContent = t("settings.folderMissing");
      row.querySelector(".settings-cache-bytes").before(missing);
    }
    return row;
  },

  // Name, size and a Delete button that calls `onDelete(button)`.
  _cacheRowElement(name, bytes, onDelete) {
    const label = document.createElement("span");
    label.className = "settings-cache-name";
    label.textContent = name;
    label.title = name;
    const size = document.createElement("span");
    size.className = "settings-unit settings-cache-bytes";
    size.textContent = this._fmtBytes(bytes);
    const text = document.createElement("span");
    text.dataset.i18n = "settings.deleteCache";
    text.textContent = t("settings.deleteCache");
    const button = document.createElement("button");
    button.className = "btn-danger with-icon";
    button.append(iconElement("delete"), text);
    button.addEventListener("click", () => onDelete(button));
    const row = document.createElement("div");
    row.className = "settings-cache-item";
    row.append(label, size, button);
    return row;
  },

  async _deleteCache(id, button) {
    if (!window.confirm(t(`settings.cacheConfirm.${id}`))) return;
    const result = await this._withDisabled(button, () => window.pywebview.api.delete_cache(id));
    if (id === "map") this._resetMapView();
    await this._loadCacheUsage();
    const size = document.querySelector(`.settings-cache-item[data-cache-id="${id}"] .settings-cache-bytes`);
    if (size) size.textContent = this._deleteResultText(result);
  },

  async _deleteOtherClientCache(id, folder, button) {
    if (!window.confirm(t("settings.otherClientConfirm", { folder: folder || id }))) return;
    const result = await this._withDisabled(button, () => window.pywebview.api.delete_other_client_cache(id));
    await this._loadCacheUsage();
    // A deleted folder's row is gone; one that kept files says why.
    if (!result?.ok) this.showError(this._deleteResultText(result));
  },

  async deleteCaches() {
    if (!window.confirm(t("settings.deleteCachesConfirm"))) return;
    const button = document.getElementById("settings-delete-caches");
    const result = await this._withDisabled(button, () => window.pywebview.api.delete_caches());
    // The map tiles went with the caches.
    this._resetMapView();
    await this._loadCacheUsage();
    document.getElementById("settings-cache-size").textContent = this._deleteResultText(result);
  },

  _deleteResultText(result) {
    return result?.ok
      ? t("settings.cachesDeleted", { size: this._fmtBytes(result.freed ?? 0) })
      : t("settings.cachesDeleteFailed", { message: result?.error ?? "" });
  },

  async _withDisabled(button, call) {
    button.disabled = true;
    try {
      return await call();
    } finally {
      button.disabled = false;
    }
  },

  _showCacheSize(bytes) {
    document.getElementById("settings-cache-size").textContent = t("settings.cacheSize", { size: this._fmtBytes(bytes) });
  },
};
