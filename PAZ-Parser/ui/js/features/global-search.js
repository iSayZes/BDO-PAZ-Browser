"use strict";

import { t } from "../core/i18n.js";

// Module-level state
let _gsMode = "string";
let _gsRunning = false;
const _EXTENSIONS = [".bss", ".dbss"];
const _activeExts = new Set(_EXTENSIONS);

export const globalSearchMethods = {
  _initGlobalSearch() {
    const input = document.getElementById("csb-input");
    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter") { e.preventDefault(); this._runGlobalSearch(); }
      if (e.key === "Escape") { e.stopPropagation(); this._closeGlobalSearch(); }
    });
    if (_gsMode === "hex") {
      input.addEventListener("input", (e) => {
        const cleaned = e.target.value.replace(/[^0-9a-fA-F\s]/g, "").replace(/\s+/g, " ").toUpperCase();
        if (cleaned !== e.target.value) e.target.value = cleaned;
      });
    }
  },

  toggleContentSearch() {
    const bar = document.getElementById("content-search-bar");
    const btn = document.getElementById("btn-content-search");
    const hidden = bar.hidden;
    bar.hidden = !hidden;
    btn.classList.toggle("active", !hidden ? false : true);
    if (!hidden) {
      // closing — restore tree if we were showing results
      if (this._inGlobalSearch) this._exitGlobalSearchResults();
    } else {
      document.getElementById("csb-input").focus();
    }
  },

  _closeGlobalSearch() {
    const bar = document.getElementById("content-search-bar");
    bar.hidden = true;
    document.getElementById("btn-content-search").classList.remove("active");
    if (this._inGlobalSearch) this._exitGlobalSearchResults();
  },

  _setCsbMode(mode) {
    _gsMode = mode;
    document.getElementById("csb-mode-string").classList.toggle("active", mode === "string");
    document.getElementById("csb-mode-hex").classList.toggle("active", mode === "hex");
    const input = document.getElementById("csb-input");
    if (mode === "hex") {
      const cleaned = input.value.replace(/[^0-9a-fA-F\s]/g, "").replace(/\s+/g, " ").toUpperCase();
      input.value = cleaned;
    }
    input.focus();
  },

  _toggleCsbExt(ext) {
    if (_activeExts.has(ext)) {
      if (_activeExts.size > 1) _activeExts.delete(ext);
    } else {
      _activeExts.add(ext);
    }
    document.querySelectorAll(".csb-ext-chip").forEach((chip) => {
      chip.classList.toggle("active", _activeExts.has(chip.dataset.ext));
    });
  },

  async _runGlobalSearch() {
    const query = document.getElementById("csb-input").value.trim();
    if (!query || _gsRunning) return;

    _gsRunning = true;
    this._updateCsbButtons(true);

    const result = await window.pywebview.api.search_all_files(
      query, _gsMode, [..._activeExts],
    );

    if (result.error) {
      this.setStatus({ key: "status.searchError", args: { message: result.error } });
      _gsRunning = false;
      this._updateCsbButtons(false);
      return;
    }

    // Clear tree now — results will stream in via onGlobalSearchResult
    this._inGlobalSearch = true;
    document.getElementById("tree").innerHTML = "";
  },

  async cancelGlobalSearch() {
    await window.pywebview.api.cancel_global_search();
    _gsRunning = false;
    this._updateCsbButtons(false);
  },

  onGlobalSearchResult(items) {
    this._appendGlobalSearchItems(items);
  },

  onGlobalSearchDone(_summary) {
    _gsRunning = false;
    this._updateCsbButtons(false);
    const tree = document.getElementById("tree");
    if (this._inGlobalSearch && !tree.children.length) {
      const li = document.createElement("li");
      li.className = "tree-node";
      li.style.cssText = "padding:8px 12px;color:var(--fg-muted);font-size:12px";
      li.textContent = "No matches found.";
      tree.appendChild(li);
    }
  },

  _updateCsbButtons(running) {
    document.getElementById("csb-go").hidden = running;
    document.getElementById("csb-cancel").hidden = !running;
  },

  _appendGlobalSearchItems(items) {
    const tree = document.getElementById("tree");
    for (const item of items) {
      const li = document.createElement("li");
      li.className = "tree-node tree-file csb-result";

      const icon  = document.createElement("span");
      icon.className = "tree-icon";
      icon.textContent = item.icon;

      const name  = document.createElement("span");
      name.className = "csb-result-name";
      name.textContent = item.name;

      const path  = document.createElement("span");
      path.className = "csb-result-path";
      path.textContent = item.path;

      const badge = document.createElement("span");
      badge.className = "csb-result-badge";
      badge.textContent = item.count === 1 ? "1 match" : `${item.count} matches`;

      li.append(icon, name, path, badge);
      li.addEventListener("click", () => this._selectFile(item.path, item.name, item.icon));
      tree.appendChild(li);
    }
  },

  _exitGlobalSearchResults() {
    this._inGlobalSearch = false;
    if (!this._inSearch) this._loadTreeRoot();
  },
};
