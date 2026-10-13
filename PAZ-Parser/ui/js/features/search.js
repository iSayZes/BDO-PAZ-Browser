"use strict";

import { iconSvg } from "../core/icons.js";

// How far below the visible list the last row may be when the next page of
// results is asked for, so scrolling rarely reaches the end before it lands.
const LOAD_MORE_MARGIN_PX = 400;

export const searchMethods = {
  scheduleSearch(query) {
    clearTimeout(this._searchTimer);
    this._searchTimer = setTimeout(() => this._doSearch(query), 600);
  },

  async _doSearch(query) {
    const seq = ++this._searchSeq;
    this._searchMoreObserver?.disconnect();

    if (!query.trim()) {
      this._loadTreeRoot();
      return;
    }
    this._inSearch = true;

    const apiStart = performance.now();
    const page = await window.pywebview.api.search(query, 0);
    window.appProfile?.record("_doSearch.api.search", performance.now() - apiStart);
    if (seq !== this._searchSeq) return;

    const renderStart = performance.now();
    const tree = document.getElementById("tree");
    tree.innerHTML = "";
    document.getElementById("tree-container").scrollTop = 0;
    this._appendSearchResults(tree, page.items);
    this._loadMoreOnScroll(tree, query, seq, page.total);

    const count = page.total.toLocaleString();
    this.setStatus({ key: "status.found", args: { count, query } });
    window.appProfile?.record("_doSearch.render_results", performance.now() - renderStart);
  },

  // The server sends results a page at a time (SEARCH_PAGE_SIZE in
  // api/bdo_api_file_search.py); the next page loads when the last row nears
  // the bottom of the list, until all `total` rows are in.
  _loadMoreOnScroll(tree, query, seq, total) {
    if (tree.childElementCount >= total) return;
    const observer = new IntersectionObserver(async (entries) => {
      if (!entries.some((entry) => entry.isIntersecting)) return;
      observer.disconnect();
      const page = await window.pywebview.api.search(query, tree.childElementCount);
      if (seq !== this._searchSeq || !page.items.length) return;
      this._appendSearchResults(tree, page.items);
      this._loadMoreOnScroll(tree, query, seq, page.total);
    }, {
      root: document.getElementById("tree-container"),
      rootMargin: `${LOAD_MORE_MARGIN_PX}px`,
    });
    this._searchMoreObserver = observer;
    observer.observe(tree.lastElementChild);
  },

  _appendSearchResults(tree, items) {
    const rows = document.createDocumentFragment();
    for (const item of items) rows.appendChild(this._searchResultRow(item));
    tree.appendChild(rows);
  },

  _searchResultRow(item) {
    const li = document.createElement("li");
    li.className = "tree-node tree-file search-result";
    li.dataset.id = item.id;
    li.dataset.icon = item.icon;
    li.classList.toggle("supported", item.supported === true);

    const label = document.createElement("span");
    label.className = "tree-label";
    label.innerHTML =
      iconSvg(item.icon, "icon tree-icon") +
      `<span class="tree-name">${this._esc(item.name)}</span>` +
      `<span class="tree-path">${this._esc(item.path)}</span>`;
    label.addEventListener("click", (e) => {
      if (e.ctrlKey) this._toggleExtractSelect(li, item.id);
      else this._selectFile(item.id, item.name, item.icon);
    });
    li.appendChild(label);
    return li;
  },
};
