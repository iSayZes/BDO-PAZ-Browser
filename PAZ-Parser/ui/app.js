"use strict";

const app = {
  _selectedPath: null,
  _currentFolderPath: null,
  _extractPaths: new Set(),
  _searchTimer: null,
  _searchSeq: 0,
  _inSearch: false,
  _parsedHtml: null,
  _hexHtml: null,
  _activeTab: "hex",
  _hexPage: 0,
  _hexTotalPages: 1,
  _parsedPage: 0,
  _parsedTotalPages: 1,

  // ── Init ──────────────────────────────────────────────────────────────────

  async init() {
    const saved = localStorage.getItem("outputPath");
    if (saved) document.getElementById("output-path").value = saved;

    const status = await window.pywebview.api.get_status();
    this.setStatus(status);

    this._setupDividers();
    this._setupOutputPathSave();
    this._setupPreviewTableSelection();
    this._setupEscapeClear();

    const last = await window.pywebview.api.get_last_folder();
    if (last && last.path) {
      const el = document.getElementById("folder-path");
      el.textContent = last.path;
      el.classList.remove("muted");
      window.pywebview.api.open_folder_path(last.path);
    }
  },

  // ── Folder ────────────────────────────────────────────────────────────────

  async openFolder() {
    const result = await window.pywebview.api.open_folder();
    if (result.ok) {
      const el = document.getElementById("folder-path");
      el.textContent = result.path;
      el.classList.remove("muted");
    }
  },

  onFolderLoaded() {
    this._loadTreeRoot();
  },

  // ── Tree ──────────────────────────────────────────────────────────────────

  async _loadTreeRoot() {
    this._inSearch = false;
    this._clearExtractSelection();
    document.getElementById("search").value = "";
    const tree = document.getElementById("tree");
    tree.innerHTML = "";
    const children = await window.pywebview.api.get_children("");
    for (const item of children) {
      tree.appendChild(this._buildNode(item));
    }
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
    const arrow = li.querySelector(".tree-arrow");
    const ul = li.querySelector(".tree-children");

    if (!ul) return;

    if (ul.hidden) {
      if (!li._loaded) {
        li._loaded = true;
        const loading = document.createElement("li");
        loading.className = "tree-node loading";
        loading.innerHTML = '<span class="tree-label"><span class="tree-name">Loading…</span></span>';
        ul.appendChild(loading);

        const children = await window.pywebview.api.get_children(li.dataset.id);
        ul.innerHTML = "";
        for (const child of children) {
          ul.appendChild(this._buildNode(child));
        }
      }
      ul.hidden = false;
      li.classList.add("expanded");
      this._currentFolderPath = li.dataset.id;
    } else {
      ul.hidden = true;
      li.classList.remove("expanded");
    }
  },

  async _selectFile(path, name, icon) {
    // Deselect previous
    document.querySelectorAll(".tree-node.selected").forEach((n) => n.classList.remove("selected"));
    const node = document.querySelector(`.tree-node[data-id="${CSS.escape(path)}"]`);
    if (node) node.classList.add("selected");

    this._selectedPath = path;
    this._parsedHtml = null;
    this._hexHtml = null;
    this._activeTab = "hex";
    this._hexPage = 0;
    this._hexTotalPages = 1;
    this._parsedPage = 0;
    this._parsedTotalPages = 1;

    document.getElementById("preview-title").textContent = `${icon}  ${name}`;
    document.getElementById("preview-content").innerHTML = '<div class="placeholder">Loading…</div>';
    document.getElementById("preview-tabs").hidden = true;

    const result = await window.pywebview.api.load_entry(path);

    if (result.error && !result.hex_html) {
      document.getElementById("preview-content").innerHTML = `<div class="error">Error: ${this._esc(result.error)}</div>`;
    } else {
      this._parsedHtml = result.has_parsed ? (result.html || "") : null;
      this._hexHtml = result.hex_html || "";
      this._activeTab = "hex";
      this._hexTotalPages = result.hex_total_pages ?? 1;
      this._parsedTotalPages = result.parsed_total_pages ?? 1;

      const tabs = document.getElementById("preview-tabs");
      const content = document.getElementById("preview-content");

      if (result.has_parsed) {
        tabs.hidden = false;
        tabs.querySelectorAll(".tab-btn").forEach((btn) => {
          btn.classList.toggle("active", btn.dataset.tab === "hex");
        });
        content.innerHTML = this._hexHtml;
        if (this._hexTotalPages > 1) content.appendChild(this._buildPageBar("hex", 0, this._hexTotalPages));
      } else {
        tabs.hidden = true;
        content.innerHTML = result.html ?? this._hexHtml;
        if (result.html) {
          this._initTableSort(content);
        } else if (this._hexTotalPages > 1) {
          content.appendChild(this._buildPageBar("hex", 0, this._hexTotalPages));
        }
      }
    }

    if (result.meta) this._setDetails(result.meta);
  },

  switchTab(tab) {
    if (this._hexHtml === null) return;
    this._activeTab = tab;
    document.getElementById("preview-tabs").querySelectorAll(".tab-btn").forEach((btn) => {
      btn.classList.toggle("active", btn.dataset.tab === tab);
    });
    const content = document.getElementById("preview-content");
    if (tab === "hex") {
      content.innerHTML = this._hexHtml;
      if (this._hexTotalPages > 1) content.appendChild(this._buildPageBar("hex", this._hexPage, this._hexTotalPages));
    } else {
      content.innerHTML = this._parsedHtml || "";
      this._initTableSort(content);
      if (this._parsedTotalPages > 1) content.appendChild(this._buildPageBar("parsed", this._parsedPage, this._parsedTotalPages));
    }
  },

  // ── Details ───────────────────────────────────────────────────────────────

  _setDetails(meta) {
    const grid = document.getElementById("detail-grid");
    const rows = [
      ["📦  Archive", meta.archive],
      ["📍  Path", meta.path],
      ["🗜  Compressed", meta.compressed],
      ["📄  Uncompressed", meta.uncompressed],
      ["#  Offset", meta.offset],
    ];
    grid.innerHTML = rows
      .map(([label, value]) => `<div class="detail-label">${label}</div>` + `<div class="detail-value" title="${this._esc(value)}">${this._esc(value)}</div>`)
      .join("");
  },

  // ── Search ────────────────────────────────────────────────────────────────

  scheduleSearch(query) {
    clearTimeout(this._searchTimer);
    this._searchTimer = setTimeout(() => this._doSearch(query), 600);
  },

  async _doSearch(query) {
    const seq = ++this._searchSeq;

    if (!query.trim()) {
      this._loadTreeRoot();
      return;
    }
    this._inSearch = true;

    const results = await window.pywebview.api.search(query);
    if (seq !== this._searchSeq) return;

    const tree = document.getElementById("tree");
    tree.innerHTML = "";

    for (const item of results) {
      const li = document.createElement("li");
      li.className = "tree-node tree-file search-result";
      li.dataset.id = item.id;

      const label = document.createElement("span");
      label.className = "tree-label";
      label.innerHTML =
        `<span class="tree-icon">${item.icon}</span>` +
        `<span class="tree-name">${this._esc(item.name)}</span>` +
        `<span class="tree-path">${this._esc(item.path)}</span>`;
      label.addEventListener("click", (e) => {
        if (e.ctrlKey) this._toggleExtractSelect(li, item.id);
        else this._selectFile(item.id, item.name, item.icon);
      });
      li.appendChild(label);
      tree.appendChild(li);
    }

    const cap = results.length === 500 ? "500+ " : `${results.length.toLocaleString()} `;
    this.setStatus({ message: `Found ${cap}files matching "${query}"` });
  },

  // ── Extraction ────────────────────────────────────────────────────────────

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
    if (this._extractPaths.size === 0) return; // cleared while awaiting
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
    if (this._parsedTotalPages > 1) content.appendChild(this._buildPageBar("parsed", 0, this._parsedTotalPages));
  },

  _buildPageBar(kind, page, total) {
    const bar = document.createElement("div");
    bar.className = "page-bar";
    bar.dataset.kind = kind;

    const prev = document.createElement("button");
    prev.className = "page-btn";
    prev.textContent = "◀ Prev";
    prev.disabled = page === 0;
    prev.onclick = () => kind === "hex" ? this._gotoHexPage(page - 1) : this._gotoParsedPage(page - 1);

    const label = document.createElement("span");
    label.className = "page-label";
    label.textContent = `${page + 1} / ${total}`;

    const next = document.createElement("button");
    next.className = "page-btn";
    next.textContent = "Next ▶";
    next.disabled = page >= total - 1;
    next.onclick = () => kind === "hex" ? this._gotoHexPage(page + 1) : this._gotoParsedPage(page + 1);

    bar.append(prev, label, next);
    return bar;
  },

  async _gotoHexPage(page) {
    const result = await window.pywebview.api.get_hex_page(this._selectedPath, page);
    if (result.error) return;
    this._hexPage = page;
    this._hexHtml = result.hex_html;
    const content = document.getElementById("preview-content");
    content.innerHTML = result.hex_html;
    content.appendChild(this._buildPageBar("hex", page, this._hexTotalPages));
  },

  async _gotoParsedPage(page) {
    const result = await window.pywebview.api.get_parsed_page(this._selectedPath, page);
    if (result.error) return;
    this._parsedPage = page;
    this._parsedHtml = result.html;
    const content = document.getElementById("preview-content");
    content.innerHTML = result.html;
    this._initTableSort(content);
    content.appendChild(this._buildPageBar("parsed", page, this._parsedTotalPages));
  },

  showError(msg) {
    alert(msg);
  },

  // ── Status ────────────────────────────────────────────────────────────────

  setStatus(data) {
    document.getElementById("status-text").textContent = data.message;
    const wrap = document.getElementById("progress-wrap");
    if (data.progress) {
      const [val, total] = data.progress;
      wrap.hidden = false;
      document.getElementById("progress-fill").style.width = `${Math.round((val / total) * 100)}%`;
    } else {
      wrap.hidden = true;
      document.getElementById("progress-fill").style.width = "0%";
    }
  },

  // ── Table sorting ─────────────────────────────────────────────────────────

  _initTableSort(container) {
    container.querySelectorAll(".data-table th.sortable").forEach((th, colIdx) => {
      th.addEventListener("click", () => this._sortTable(th, colIdx));
    });
  },

  _sortTable(th, colIdx) {
    const table = th.closest("table");
    const tbody = table.querySelector("tbody");
    const rows = [...tbody.querySelectorAll("tr")];
    const asc = th.dataset.sortDir !== "asc";

    th.closest("thead")
      .querySelectorAll("th")
      .forEach((h) => {
        delete h.dataset.sortDir;
        h.classList.remove("sort-asc", "sort-desc");
      });
    th.dataset.sortDir = asc ? "asc" : "desc";
    th.classList.toggle("sort-asc", asc);
    th.classList.toggle("sort-desc", !asc);

    rows.sort((a, b) => {
      const av = a.cells[colIdx]?.textContent ?? "";
      const bv = b.cells[colIdx]?.textContent ?? "";
      const na = parseFloat(av.replace(/[^0-9.-]/g, ""));
      const nb = parseFloat(bv.replace(/[^0-9.-]/g, ""));
      if (!isNaN(na) && !isNaN(nb)) return asc ? na - nb : nb - na;
      return asc ? av.localeCompare(bv) : bv.localeCompare(av);
    });

    rows.forEach((r) => tbody.appendChild(r));
  },

  // ── Table copy ───────────────────────────────────────────────

  _setupPreviewTableSelection() {
    const previewContent = document.getElementById("preview-content");

    previewContent.addEventListener("click", (event) => {
      const row = event.target.closest(".data-table tbody tr");

      if (!row || !previewContent.contains(row)) {
        return;
      }

      const table = row.closest(".data-table");

      table.querySelectorAll("tbody tr.selected-row").forEach((selectedRow) => {
        selectedRow.classList.remove("selected-row");
      });

      row.classList.add("selected-row");
    });

    document.addEventListener("keydown", async (event) => {
      if (!(event.ctrlKey || event.metaKey) || event.key.toLowerCase() !== "c") {
        return;
      }

      const selectedRow = previewContent.querySelector(".data-table tbody tr.selected-row");

      if (!selectedRow) {
        return;
      }

      const selectedText = window.getSelection().toString();

      if (selectedText) {
        return;
      }

      event.preventDefault();

      const values = Array.from(selectedRow.querySelectorAll("td"))
        .map((cell) => cell.innerText.trim())
        .join("\t");

      await navigator.clipboard.writeText(values);
      this.setStatus({ message: "Copied selected row." });
    });
  },

  // ── Dividers (resize sidebar / details panel) ─────────────────────────────

  _setupDividers() {
    const sidebar = document.getElementById("sidebar");
    const vDiv = document.getElementById("v-divider");
    let draggingV = false;

    vDiv.addEventListener("mousedown", (e) => {
      draggingV = true;
      vDiv.classList.add("dragging");
      document.body.style.cursor = "col-resize";
      document.body.style.userSelect = "none";
      e.preventDefault();
    });

    const details = document.getElementById("details-panel");
    const hDiv = document.getElementById("h-divider");
    let draggingH = false;

    hDiv.addEventListener("mousedown", (e) => {
      draggingH = true;
      hDiv.classList.add("dragging");
      document.body.style.cursor = "row-resize";
      document.body.style.userSelect = "none";
      e.preventDefault();
    });

    document.addEventListener("mousemove", (e) => {
      if (draggingV) {
        const main = document.getElementById("main");
        const rect = main.getBoundingClientRect();
        const w = Math.max(140, Math.min(600, e.clientX - rect.left));
        sidebar.style.width = w + "px";
      }
      if (draggingH) {
        const right = document.getElementById("right-panel");
        const rect = right.getBoundingClientRect();
        const h = Math.max(70, Math.min(400, e.clientY - rect.top));
        details.style.height = h + "px";
      }
    });

    document.addEventListener("mouseup", () => {
      if (draggingV) {
        draggingV = false;
        vDiv.classList.remove("dragging");
        document.body.style.cursor = "";
        document.body.style.userSelect = "";
      }
      if (draggingH) {
        draggingH = false;
        hDiv.classList.remove("dragging");
        document.body.style.cursor = "";
        document.body.style.userSelect = "";
      }
    });
  },

  _setupOutputPathSave() {
    document.getElementById("output-path").addEventListener("change", (e) => {
      localStorage.setItem("outputPath", e.target.value);
    });
  },

  _setupEscapeClear() {
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && this._extractPaths.size > 0) {
        this._clearExtractSelection();
      }
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "r") {
        e.preventDefault();
        window.pywebview.api.reload_plugins();
      }
    });
  },

  // ── Helpers ───────────────────────────────────────────────────────────────

  _esc(str) {
    const d = document.createElement("div");
    d.textContent = String(str ?? "");
    return d.innerHTML;
  },
};

window.addEventListener("pywebviewready", () => app.init());
