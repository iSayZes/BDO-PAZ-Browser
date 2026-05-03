"use strict";

export const extractionMethods = {
  _toggleExtractSelect(li, path) {
    if (this._extractPaths.has(path)) {
      this._extractPaths.delete(path);
      li.classList.remove("extract-selected");
    } else {
      this._extractPaths.add(path);
      li.classList.add("extract-selected");
    }
    this._updateExtractBadge();
  },

  _clearExtractSelection() {
    document.querySelectorAll(".tree-node.extract-selected").forEach((n) => n.classList.remove("extract-selected"));
    this._extractPaths.clear();
    this._updateExtractBadge();
  },

  async _updateExtractBadge() {
    const badge = document.getElementById("extract-badge");
    if (this._extractPaths.size === 0) {
      badge.hidden = true;
      return;
    }
    const info = await window.pywebview.api.get_selection_size([...this._extractPaths]);
    if (this._extractPaths.size === 0) return;
    badge.hidden = false;
    badge.textContent = `${info.count.toLocaleString()} file${info.count !== 1 ? "s" : ""}  ·  ${this._fmtBytes(info.bytes)}`;
  },

  _fmtBytes(n) {
    if (n < 1024) return `${n} B`;
    if (n < 1024 ** 2) return `${(n / 1024).toFixed(1)} KB`;
    if (n < 1024 ** 3) return `${(n / 1024 ** 2).toFixed(1)} MB`;
    return `${(n / 1024 ** 3).toFixed(1)} GB`;
  },

  async extractSelected() {
    if (this._extractPaths.size === 0) {
      alert("Ctrl+click files or folders in the tree to select them first.");
      return;
    }
    const output = document.getElementById("output-path").value.trim();
    if (!output) {
      alert("Set an output folder first.");
      return;
    }
    await window.pywebview.api.extract_entries([...this._extractPaths], output);
  },

  async extractFolder() {
    if (!this._currentFolderPath) {
      alert("Expand a folder in the tree first.");
      return;
    }
    const output = document.getElementById("output-path").value.trim();
    if (!output) {
      alert("Set an output folder first.");
      return;
    }
    await window.pywebview.api.extract_entries([this._currentFolderPath], output);
  },

  async pickOutputFolder() {
    const path = await window.pywebview.api.pick_output_folder();
    if (path) {
      document.getElementById("output-path").value = path;
      localStorage.setItem("outputPath", path);
    }
  },

  onExtractionDone() {
    /* status updated by Python push */
  },

  async onPluginsReloaded() {
    this.setStatus({ message: "Plugins reloaded." });
    if (this._activeTab === "parsed" && this._selectedPath) {
      await this._refreshParsedView();
    }
  },

  async _refreshParsedView() {
    const result = await window.pywebview.api.load_entry(this._selectedPath);
    if (result.error && !result.hex_html) return;

    this._parsedHtml = result.has_parsed ? (result.html || "") : null;
    this._hexHtml = result.hex_html || "";
    this._hexPage = 0;
    this._hexTotalPages = result.hex_total_pages ?? 1;
    this._parsedPage = 0;
    this._parsedTotalPages = result.parsed_total_pages ?? 1;

    const tabs = document.getElementById("preview-tabs");
    tabs.hidden = !result.has_parsed;

    const content = document.getElementById("preview-content");
    content.innerHTML = this._parsedHtml || "";
    this._initTableSort(content);
    this._setPageBar(this._parsedTotalPages > 1 ? this._buildPageBar("parsed", 0, this._parsedTotalPages) : null);
  },
};
