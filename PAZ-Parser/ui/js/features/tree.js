"use strict";

import { t } from "../core/i18n.js";

export const treeMethods = {
  async _loadTreeRoot() {
    this._inSearch = false;
    this._clearExtractSelection();
    document.getElementById("search").value = "";
    const tree = document.getElementById("tree");
    tree.innerHTML = "";
    tree.appendChild(this._buildTreeLoadingNode());
    await this._nextPaint();
    const children = await window.pywebview.api.get_children("");
    tree.innerHTML = "";
    for (const item of children) {
      tree.appendChild(this._buildNode(item));
    }
  },

  _buildTreeLoadingNode() {
    const loading = document.createElement("li");
    loading.className = "tree-node loading";
    loading.innerHTML = `<span class="tree-label"><span class="loading-spinner" aria-hidden="true"></span><span class="tree-name">${t("tree.loading")}</span></span>`;
    return loading;
  },

  _showTreeLoading() {
    const tree = document.getElementById("tree");
    tree.innerHTML = "";
    tree.appendChild(this._buildTreeLoadingNode());
    return this._nextPaint();
  },

  _nextPaint() {
    return new Promise((resolve) => requestAnimationFrame(resolve));
  },

  _buildNode(item) {
    const li = document.createElement("li");
    li.className = `tree-node tree-${item.type}`;
    li.dataset.id = item.id;

    const label = document.createElement("span");
    label.className = "tree-label";

    if (item.type === "dir") {
      const arrow = document.createElement("span");
      arrow.className = "tree-arrow";
      arrow.textContent = "▶";
      label.appendChild(arrow);
    }

    const icon = document.createElement("span");
    icon.className = "tree-icon";
    icon.textContent = item.icon;
    label.appendChild(icon);

    const name = document.createElement("span");
    name.className = "tree-name";
    name.textContent = item.name;
    label.appendChild(name);

    if (item.type === "dir") {
      const count = document.createElement("span");
      count.className = "tree-count";
      count.textContent = `(${(item.count || 0).toLocaleString()})`;
      label.appendChild(count);
    }

    li.appendChild(label);

    if (item.type === "dir" && item.has_children) {
      const ul = document.createElement("ul");
      ul.className = "tree-children";
      ul.hidden = true;
      li.appendChild(ul);
      li._loaded = false;
      label.addEventListener("click", (e) => {
        if (e.ctrlKey) this._toggleExtractSelect(li, item.id);
        else this._toggleDir(li);
      });
    } else if (item.type === "file") {
      label.addEventListener("click", (e) => {
        if (e.ctrlKey) this._toggleExtractSelect(li, item.id);
        else this._selectFile(item.id, item.name, item.icon);
      });
    } else if (item.type === "dir" && !item.has_children) {
      label.addEventListener("click", (e) => {
        if (e.ctrlKey) this._toggleExtractSelect(li, item.id);
        else this._currentFolderPath = item.id;
      });
    }

    return li;
  },

  async _toggleDir(li) {
    const ul = li.querySelector(".tree-children");

    if (!ul) return;

    if (ul.hidden) {
      ul.hidden = false;
      li.classList.add("expanded");
      this._currentFolderPath = li.dataset.id;

      if (!li._loaded) {
        li._loaded = true;
        ul.appendChild(this._buildTreeLoadingNode());

        const children = await window.pywebview.api.get_children(li.dataset.id);
        ul.innerHTML = "";
        for (const child of children) {
          ul.appendChild(this._buildNode(child));
        }
      }
    } else {
      ul.hidden = true;
      li.classList.remove("expanded");
    }
  },

  async _selectFile(path, name, icon) {
    const seq = ++this._selectSeq;
    const setupStart = performance.now();
    document.querySelectorAll(".tree-node.selected").forEach((n) => n.classList.remove("selected"));
    const node = document.querySelector(`.tree-node[data-id="${CSS.escape(path)}"]`);
    if (node) node.classList.add("selected");

    document.dispatchEvent(new CustomEvent("file-selected", { detail: { path } }));

    this._selectedPath = path;
    this._parsedHtml = null;
    this._hexHtml = null;
    this._activeTab = "hex";
    this._hexPage = 0;
    this._hexTotalPages = 1;
    this._parsedPage = 0;
    this._parsedTotalPages = 1;
    this._isAltView = false;
    this._tabLabels = null;

    document.getElementById("preview-title").textContent = `${icon}  ${name}`;
    document.getElementById("preview-content").innerHTML = `<div class="placeholder preview-loading"><span class="loading-spinner" aria-hidden="true"></span><span>${t("preview.loading")}</span></div>`;
    document.getElementById("preview-tabs").hidden = true;
    document.getElementById("btn-export").hidden = true;
    this._setPageBar(null);
    window.appProfile?.record("_selectFile.setup", performance.now() - setupStart);

    const apiStart = performance.now();
    const result = await window.pywebview.api.load_entry(path);
    if (seq !== this._selectSeq) return;
    window.appProfile?.record("_selectFile.api.load_entry", performance.now() - apiStart);
    if (result.profile && window.appProfile) {
      for (const [key, value] of Object.entries(result.profile)) {
        window.appProfile.record(`_selectFile.${key}`, Number(value));
      }
    }

    const renderStart = performance.now();
    if (result.error && !result.hex_html) {
      document.getElementById("preview-content").innerHTML = `<div class="error">Error: ${this._esc(result.error)}</div>`;
    } else {
      this._parsedHtml = result.has_parsed ? (result.html || "") : null;
      this._hexHtml = result.hex_html || "";
      this._activeTab = "hex";
      this._hexTotalPages = result.hex_total_pages ?? 1;
      this._parsedTotalPages = result.parsed_total_pages ?? 1;
      this._isAltView = !!result.tab_labels;
      this._tabLabels = result.tab_labels || null;

      const tabs = document.getElementById("preview-tabs");
      const content = document.getElementById("preview-content");

      document.getElementById("btn-export").hidden = false;

      const hexTabBtn    = tabs.querySelector('[data-tab="hex"]');
      const parsedTabBtn = tabs.querySelector('[data-tab="parsed"]');
      if (this._tabLabels) {
        hexTabBtn.textContent    = this._tabLabels[0];
        parsedTabBtn.textContent = this._tabLabels[1];
      } else {
        hexTabBtn.textContent    = t("preview.tabHex");
        parsedTabBtn.textContent = t("preview.tabParsed");
      }

      if (result.has_parsed) {
        tabs.hidden = false;
        tabs.querySelectorAll(".tab-btn").forEach((btn) => {
          btn.classList.toggle("active", btn.dataset.tab === "hex");
        });
        content.innerHTML = this._hexHtml;
        this._setPageBar(this._hexTotalPages > 1 ? this._buildPageBar("hex", 0, this._hexTotalPages) : null);
        this.showTabSearchBar(true);
        if (this._isAltView) {
          document.getElementById("tab-search-mode-hex").hidden = true;
        }
      } else {
        tabs.hidden = true;
        this.showTabSearchBar(!result.stream);
        content.innerHTML = result.html ?? this._hexHtml;
        if (result.html) {
          this._initStreamThumbnails(content);
          this._initTableSort(content);
          this._initTableIcons(content);
          this._setPageBar(null);
        } else {
          this._setPageBar(this._hexTotalPages > 1 ? this._buildPageBar("hex", 0, this._hexTotalPages) : null);
        }
      }
    }
    window.appProfile?.record("_selectFile.render_result", performance.now() - renderStart);

    if (result.meta) {
      const detailsStart = performance.now();
      this._setDetails(result.meta);
      window.appProfile?.record("_selectFile.set_details", performance.now() - detailsStart);
    }
  },

  async exportFile() {
    if (!this._selectedPath) return;
    const result = await window.pywebview.api.export_file(this._selectedPath, this._activeTab);
    if (result?.error) {
      document.getElementById("status-text").textContent = `Export failed: ${result.error}`;
    }
  },

  switchTab(tab) {
    if (this._hexHtml === null) return;
    this._activeTab = tab;
    this._syncSearchBarToTab(tab);
    this._resetTabSearch();
    document.getElementById("preview-tabs").querySelectorAll(".tab-btn").forEach((btn) => {
      btn.classList.toggle("active", btn.dataset.tab === tab);
    });
    const content = document.getElementById("preview-content");
    if (tab === "hex") {
      content.innerHTML = this._hexHtml;
      this._setPageBar(this._hexTotalPages > 1 ? this._buildPageBar("hex", this._hexPage, this._hexTotalPages) : null);
      if (this._isAltView) {
        document.getElementById("tab-search-mode-hex").hidden = true;
      }
    } else {
      content.innerHTML = this._parsedHtml || "";
      this._initTableSort(content);
      this._initTableIcons(content);
      this._setPageBar(this._parsedTotalPages > 1 ? this._buildPageBar("parsed", this._parsedPage, this._parsedTotalPages) : null);
      if (this._isAltView) {
        this.showTabSearchBar(false);
      }
    }
  },
};
