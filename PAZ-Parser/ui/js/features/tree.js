"use strict";

import { t } from "../core/i18n.js";
import { iconElement } from "../core/icons.js";

export const treeMethods = {
  // Also runs when the filter box is cleared, so it must not disable the
  // search input: that would blur it and drop keystrokes. It shares
  // _searchSeq with _doSearch so a filter typed during the reload wins.
  async _loadTreeRoot() {
    const seq = ++this._searchSeq;
    this._inSearch = false;
    this._clearExtractSelection();
    document.getElementById("search").value = "";
    const tree = document.getElementById("tree");
    tree.innerHTML = "";
    tree.appendChild(this._buildTreeRootLoading());
    try {
      await this._nextPaint();
      const children = await window.pywebview.api.get_children("");
      if (seq !== this._searchSeq) return;
      tree.innerHTML = "";
      for (const item of children) {
        tree.appendChild(this._buildNode(item));
      }
    } catch (err) {
      console.error("Loading the tree root failed", err);
      if (seq !== this._searchSeq) return;
      tree.innerHTML = "";
      this.setStatus({ key: "status.error", args: { message: String(err?.message ?? err) } });
    } finally {
      this._setSearchEnabled(true);
    }
  },

  _setSearchEnabled(isEnabled) {
    document.getElementById("search").disabled = !isEnabled;
    document.getElementById("btn-content-search").disabled = !isEnabled;
  },

  // A text view searches its own lines, in string mode; an image view has nothing to find.
  _syncViewSearchBar() {
    const isText = !!document.querySelector("#preview-content .text-lines");
    this.showTabSearchBar(isText);
    if (isText) this._syncSearchBarToTab("parsed");
  },

  // The whole tree is loading: the spinner row, then grey rows where names will be.
  _buildTreeRootLoading() {
    const rows = document.createDocumentFragment();
    rows.appendChild(this._buildTreeLoadingNode());
    const widths = [62, 48, 70, 55, 40, 66, 58, 45, 72, 50, 61, 38];
    for (const width of widths) {
      const row = document.createElement("li");
      row.className = "tree-node tree-skeleton";
      row.setAttribute("aria-hidden", "true");
      row.innerHTML = `<span class="tree-label"><span class="skeleton-icon"></span><span class="skeleton-bar" style="width:${width}%"></span></span>`;
      rows.appendChild(row);
    }
    return rows;
  },

  _buildTreeLoadingNode() {
    const loading = document.createElement("li");
    loading.className = "tree-node loading";
    loading.innerHTML = `<span class="tree-label"><span class="loading-spinner" aria-hidden="true"></span><span class="tree-name">${t("tree.loading")}</span></span>`;
    return loading;
  },

  // Folder loads only. Search stays off until onFolderLoaded rebuilds the
  // tree, so it cannot query the previous folder's entries meanwhile.
  _showTreeLoading() {
    this._setSearchEnabled(false);
    const tree = document.getElementById("tree");
    tree.innerHTML = "";
    tree.appendChild(this._buildTreeRootLoading());
    return this._nextPaint();
  },

  _nextPaint() {
    return new Promise((resolve) => requestAnimationFrame(resolve));
  },

  _buildNode(item) {
    const li = document.createElement("li");
    li.className = `tree-node tree-${item.type}`;
    li.dataset.id = item.id;
    li.dataset.icon = item.icon;
    // A rebuilt tree (settings saved, folder expanded again) keeps the selection marked.
    if (item.id === this._selectedPath) li.classList.add("selected");

    const label = document.createElement("span");
    label.className = "tree-label";

    if (item.type === "dir") {
      label.appendChild(iconElement("chevron-right", "icon tree-arrow"));
    }

    label.appendChild(iconElement(item.icon, "icon tree-icon"));

    const name = document.createElement("span");
    name.className = "tree-name";
    name.textContent = item.name;
    label.appendChild(name);

    if (item.type === "dir") {
      const count = document.createElement("span");
      count.className = "tree-count";
      count.textContent = (item.count || 0).toLocaleString();
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
    this._parsedSort = null;
    this._cancelParsedPageRequest();
    this._isAltView = false;
    this._tabLabels = null;
    this._canExportCsv = false;
    this._isPlainView = false;
    this._recordCount = null;
    this._byteCount = null;
    this.closeExportMenu();

    document.getElementById("preview-title").replaceChildren(iconElement(icon), document.createTextNode(name));
    this.showHandlerVersion(name);
    document.getElementById("preview-content").innerHTML = `<div class="placeholder preview-loading"><span class="loading-spinner" aria-hidden="true"></span><span>${t("preview.loading")}</span></div>`;
    document.getElementById("preview-tabs").hidden = true;
    document.getElementById("preview-tabs").classList.remove("view-first");
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
      document.getElementById("preview-content").innerHTML = `<div class="error">${this._esc(t("status.error", { message: result.error }))}</div>`;
    } else {
      this._parsedHtml = result.has_parsed ? (result.html || "") : null;
      this._hexHtml = result.hex_html || "";
      this._activeTab = "hex";
      this._hexTotalPages = result.hex_total_pages ?? 1;
      this._parsedTotalPages = result.parsed_total_pages ?? 1;
      this._parsedSort = result.sort ?? null;
      this._isAltView = !!result.tab_labels;
      this._tabLabels = result.tab_labels || null;
      this._recordCount = result.record_count ?? null;
      this._byteCount = result.byte_count ?? null;
      // Text/Rendered views have no records to write as CSV.
      this._canExportCsv = !!result.has_parsed && !this._isAltView;

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
          btn.setAttribute("aria-selected", String(btn.dataset.tab === "hex"));
        });
        content.innerHTML = this._hexHtml;
        this._setPageBar(this._hexTotalPages > 1 ? this._buildPageBar("hex", 0, this._hexTotalPages) : null);
        this.showTabSearchBar(true);
        if (this._isAltView) {
          document.getElementById("tab-search-mode-hex").hidden = true;
        }
      } else if (result.view_label && result.html) {
        // A text or image view: its own tab first, Hex next to it. The find
        // bar searches bytes, so it shows on the Hex tab only.
        this._isPlainView = true;
        this._parsedHtml = result.html;
        this._activeTab = "parsed";
        parsedTabBtn.textContent = result.view_label;
        tabs.classList.add("view-first");
        tabs.hidden = false;
        tabs.querySelectorAll(".tab-btn").forEach((btn) => {
          btn.classList.toggle("active", btn.dataset.tab === "parsed");
          btn.setAttribute("aria-selected", String(btn.dataset.tab === "parsed"));
        });
        content.innerHTML = result.html;
        this._initPreviewView(content);
        this._setPageBar(null);
        this._syncViewSearchBar();
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

  switchTab(tab) {
    if (this._hexHtml === null) return;
    this._activeTab = tab;
    this._syncSearchBarToTab(tab);
    this._resetTabSearch();
    document.getElementById("preview-tabs").querySelectorAll(".tab-btn").forEach((btn) => {
      btn.classList.toggle("active", btn.dataset.tab === tab);
      btn.setAttribute("aria-selected", String(btn.dataset.tab === tab));
    });
    const content = document.getElementById("preview-content");
    if (tab === "hex") {
      // A parsed request may still finish; it only updates state off-tab.
      this._setParsedBusy(false);
      content.innerHTML = this._hexHtml;
      this._setPageBar(this._hexTotalPages > 1 ? this._buildPageBar("hex", this._hexPage, this._hexTotalPages) : null);
      if (this._isAltView) {
        document.getElementById("tab-search-mode-hex").hidden = true;
      }
      if (this._isPlainView) this.showTabSearchBar(true);
    } else if (this._isPlainView) {
      content.innerHTML = this._parsedHtml || "";
      this._initPreviewView(content);
      this._setPageBar(null);
      this._syncViewSearchBar();
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
