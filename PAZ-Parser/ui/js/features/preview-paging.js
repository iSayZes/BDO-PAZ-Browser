"use strict";

import { t } from "../core/i18n.js";

export const previewPagingMethods = {
  _setPageBar(bar) {
    const area = document.getElementById("page-bar-area");
    area.innerHTML = "";
    if (bar) area.appendChild(bar);
  },

  _buildPageBar(kind, page, total) {
    const bar = document.createElement("div");
    bar.className = "page-bar";
    bar.dataset.kind = kind;

    const prev = document.createElement("button");
    prev.className = "page-btn";
    prev.textContent = t("pageBar.prev");
    prev.disabled = page === 0;
    prev.onclick = () => kind === "hex" ? this._gotoHexPage(page - 1) : this._gotoParsedPage(page - 1);

    const label = document.createElement("span");
    label.className = "page-label";
    label.textContent = `${page + 1} / ${total}`;

    const next = document.createElement("button");
    next.className = "page-btn";
    next.textContent = t("pageBar.next");
    next.disabled = page >= total - 1;
    next.onclick = () => kind === "hex" ? this._gotoHexPage(page + 1) : this._gotoParsedPage(page + 1);

    bar.append(prev, label, next);
    return bar;
  },

  _scrollPreviewToTop() {
    const content = document.getElementById("preview-content");
    content.scrollTop = 0;
    content.scrollLeft = 0;
  },

  async _gotoHexPage(page) {
    const result = await window.pywebview.api.get_hex_page(this._selectedPath, page);
    if (result.error) return;
    this._hexPage = page;
    this._hexHtml = result.hex_html;
    const content = document.getElementById("preview-content");
    content.innerHTML = result.hex_html;
    this._scrollPreviewToTop();
    this._setPageBar(this._buildPageBar("hex", page, this._hexTotalPages));
  },

  async _gotoParsedPage(page) {
    const result = await window.pywebview.api.get_parsed_page(this._selectedPath, page);
    if (result.error) return;
    this._parsedPage = page;
    this._parsedHtml = result.html;
    const content = document.getElementById("preview-content");
    content.innerHTML = result.html;
    this._scrollPreviewToTop();
    this._initTableSort(content);
    this._setPageBar(this._buildPageBar("parsed", page, this._parsedTotalPages));
  },

  showError(msg) {
    alert(msg);
  },
};
