"use strict";

export const searchMethods = {
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
};
