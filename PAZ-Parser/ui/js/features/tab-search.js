"use strict";

// Module-level state — kept off the shared app object intentionally.
// Only tab-search.js writes these; other modules call the exported methods.
let _matches = [];
let _matchIndex = -1;
let _mode = "string";
let _seq = 0;
let _timer = null;

const HEX_BYTES_PER_PAGE = 512 * 16; // must match bdo_preview.HEX_ROWS_PER_PAGE * _ROW
const PARSED_PER_PAGE = 500;          // must match bdo_preview.PARSED_RECORDS_PER_PAGE

export const tabSearchMethods = {
  _initTabSearch() {
    document.addEventListener("file-selected", () => {
      _seq++;
      clearTimeout(_timer);
      _matches = [];
      _matchIndex = -1;
      document.getElementById("tab-search-input").value = "";
      this._updateSearchCounter();
    });
  },

  // Called by tree.js after file loads — show only when tabs are visible.
  showTabSearchBar(show) {
    const bar = document.getElementById("tab-search-bar");
    if (!bar) return;
    bar.hidden = !show;
    if (!show) {
      _matches = [];
      _matchIndex = -1;
      _mode = "string";
      this._syncModeUI();
      this._updateSearchCounter();
    } else {
      this._syncSearchBarToTab("hex"); // file load always starts on hex tab
    }
  },

  // Hide Hex mode button when on parsed tab (strings only); restore on hex tab.
  _syncSearchBarToTab(tab) {
    const hexBtn = document.getElementById("tab-search-mode-hex");
    if (!hexBtn) return;
    hexBtn.hidden = tab !== "hex";
    if (tab !== "hex" && _mode === "hex") {
      _mode = "string";
      this._syncModeUI();
    }
  },

  // Called by setup.js on Ctrl+F.
  openTabSearch() {
    const bar = document.getElementById("tab-search-bar");
    if (!bar || bar.hidden) return;
    const input = document.getElementById("tab-search-input");
    input.focus();
    input.select();
  },

  _setTabSearchMode(mode) {
    _mode = mode;
    if (mode === "hex") {
      const input = document.getElementById("tab-search-input");
      const cleaned = input.value.replace(/[^0-9a-fA-F\s]/g, "").replace(/\s+/g, " ").toUpperCase();
      if (cleaned !== input.value) input.value = cleaned;
    }
    this._syncModeUI();
    this._scheduleTabSearch();
  },

  _syncModeUI() {
    document.getElementById("tab-search-mode-hex").classList.toggle("active", _mode === "hex");
    document.getElementById("tab-search-mode-string").classList.toggle("active", _mode === "string");
    document.getElementById("tab-search-prefix").hidden = _mode !== "hex";
  },

  _onTabSearchInput(e) {
    if (_mode === "hex") {
      const raw = e.target.value;
      const cleaned = raw.replace(/[^0-9a-fA-F\s]/g, "").replace(/\s+/g, " ").toUpperCase();
      if (cleaned !== raw) e.target.value = cleaned;
    }
    this._scheduleTabSearch();
  },

  _onTabSearchKeydown(e) {
    if (e.key === "Enter") {
      e.preventDefault();
      if (e.shiftKey) this.tabSearchPrev();
      else this.tabSearchNext();
    } else if (e.key === "Escape") {
      e.stopPropagation();
      document.getElementById("tab-search-bar").hidden = true;
    }
  },

  _scheduleTabSearch() {
    clearTimeout(_timer);
    _timer = setTimeout(() => this._doTabSearch(), 300);
  },

  async _doTabSearch() {
    const query = document.getElementById("tab-search-input").value.trim();
    const seq = ++_seq;

    if (!query || !this._selectedPath) {
      _matches = [];
      _matchIndex = -1;
      this._updateSearchCounter();
      return;
    }

    const apiStart = performance.now();
    const result = await window.pywebview.api.search_content(
      this._selectedPath, query, _mode, this._activeTab,
    );
    window.appProfile?.record("_doTabSearch.api.search_content", performance.now() - apiStart);
    if (seq !== _seq) return;

    const resultStart = performance.now();
    if (result.error || result.offsets?.length === 0 || result.record_indices?.length === 0) {
      _matches = result.error ? [] : (result.offsets ?? result.record_indices ?? []);
      _matchIndex = _matches.length > 0 ? 0 : -1;
    } else {
      _matches = result.offsets ?? result.record_indices ?? [];
      _matchIndex = _matches.length > 0 ? 0 : -1;
    }

    this._updateSearchCounter();
    window.appProfile?.record("_doTabSearch.process_results", performance.now() - resultStart);
    if (_matchIndex >= 0) await this._jumpToMatch(_matchIndex);
  },

  tabSearchNext() {
    if (_matches.length === 0) return;
    _matchIndex = (_matchIndex + 1) % _matches.length;
    this._updateSearchCounter();
    this._jumpToMatch(_matchIndex);
  },

  tabSearchPrev() {
    if (_matches.length === 0) return;
    _matchIndex = (_matchIndex - 1 + _matches.length) % _matches.length;
    this._updateSearchCounter();
    this._jumpToMatch(_matchIndex);
  },

  async _jumpToMatch(index) {
    const pos = _matches[index];
    if (pos === undefined) return;

    if (this._activeTab === "hex") {
      const page = Math.floor(pos / HEX_BYTES_PER_PAGE);
      if (page !== this._hexPage) await this._gotoHexPage(page);
      this._highlightHexOffset(pos);
    } else {
      const page = Math.floor(pos / PARSED_PER_PAGE);
      if (page !== this._parsedPage) await this._gotoParsedPage(page);
      this._highlightParsedRow(pos % PARSED_PER_PAGE);
    }
  },

  _highlightHexOffset(byteOffset) {
    const rowStart = Math.floor(byteOffset / 16) * 16;
    const hex = rowStart.toString(16).toUpperCase().padStart(8, "0");
    document.querySelectorAll(".hex-row.search-match").forEach((r) => r.classList.remove("search-match"));
    for (const row of document.querySelectorAll(".hex-row")) {
      const off = row.querySelector(".hex-offset");
      if (off && off.textContent === hex) {
        row.classList.add("search-match");
        row.scrollIntoView({ block: "nearest" });
        break;
      }
    }
  },

  _highlightParsedRow(localIndex) {
    document.querySelectorAll(".search-match").forEach((r) => r.classList.remove("search-match"));
    const rows = document.querySelectorAll("table tbody tr");
    const target = rows[localIndex];
    if (!target) return;
    target.classList.add("search-match");

    // #preview-content is the scroll container; sticky thead is top:0 inside it.
    const scroller = document.getElementById("preview-content");
    if (!scroller) { target.scrollIntoView({ block: "nearest" }); return; }

    const thead = target.closest("table")?.querySelector("thead");
    const theadHeight = thead ? thead.getBoundingClientRect().height : 0;

    const scrollerRect = scroller.getBoundingClientRect();
    const rowRect = target.getBoundingClientRect();

    const rowTopRelative = rowRect.top - scrollerRect.top;
    const rowBottomRelative = rowRect.bottom - scrollerRect.top;

    if (rowTopRelative < theadHeight) {
      // Row is above (or under) sticky header — scroll it just below the header.
      scroller.scrollTop += rowTopRelative - theadHeight;
    } else if (rowBottomRelative > scroller.clientHeight) {
      // Row is below the visible area.
      scroller.scrollTop += rowBottomRelative - scroller.clientHeight;
    }
  },

  _updateSearchCounter() {
    const el = document.getElementById("tab-search-counter");
    if (!el) return;
    const query = document.getElementById("tab-search-input")?.value.trim();
    if (_matches.length === 0) {
      el.textContent = query ? "No matches" : "";
    } else {
      el.textContent = `${_matchIndex + 1} of ${_matches.length}`;
    }
  },

  // Called by switchTab so stale hex results don't persist on parsed tab and vice-versa.
  _resetTabSearch() {
    _seq++;
    clearTimeout(_timer);
    _matches = [];
    _matchIndex = -1;
    this._updateSearchCounter();
  },
};
