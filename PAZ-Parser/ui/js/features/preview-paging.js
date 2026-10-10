"use strict";

import { t } from "../core/i18n.js";
import { iconElement } from "../core/icons.js";

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
    prev.className = "page-btn with-icon";
    prev.append(iconElement("chevron-left"), t("pageBar.prev"));
    prev.disabled = page === 0;
    prev.onclick = () => kind === "hex" ? this._gotoHexPage(page - 1) : this._gotoParsedPage(page - 1);

    const label = document.createElement("span");
    label.className = "page-label";
    label.textContent = `${page + 1} / ${total}`;

    const next = document.createElement("button");
    next.className = "page-btn with-icon";
    next.append(t("pageBar.next"), iconElement("chevron-right"));
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

  // Returns true when the page was shown. `sort` defaults to the active one,
  // so paging keeps the current order. While the request runs the table is
  // marked busy (see .parsed-busy in 11-data-tables.css); a response that a
  // newer page request or `_cancelParsedPageRequest` has overtaken is dropped.
  async _gotoParsedPage(page, sort = this._parsedSort) {
    const seq = ++this._parsedPageSeq;
    const content = document.getElementById("preview-content");
    this._setParsedBusy(true);

    try {
      const result = await window.pywebview.api.get_parsed_page(
        this._selectedPath, page, sort?.field ?? "", sort?.dir ?? "",
      );
      if (seq !== this._parsedPageSeq) return false;
      if (result.error) {
        this.setStatus({ key: "status.pageError", args: { message: result.error } });
        return false;
      }
      this._parsedSort = sort;
      this._parsedPage = page;
      this._parsedHtml = result.html;
      // Switched to the hex tab meanwhile: keep the page for when they return.
      if (this._activeTab !== "parsed") return true;
      content.innerHTML = result.html;
      this._scrollPreviewToTop();
      this._initTableSort(content);
      this._initTableIcons(content);
      this._setPageBar(this._buildPageBar("parsed", page, this._parsedTotalPages));
      return true;
    } finally {
      if (seq === this._parsedPageSeq) this._setParsedBusy(false);
    }
  },

  _setParsedBusy(isBusy) {
    const content = document.getElementById("preview-content");
    content.classList.toggle("parsed-busy", isBusy);
    content.toggleAttribute("aria-busy", isBusy);
  },

  // Drops any parsed page request still in flight, e.g. when another file
  // opens or plugins reload.
  _cancelParsedPageRequest() {
    this._parsedPageSeq++;
    this._setParsedBusy(false);
  },

  showError(msg) {
    alert(msg);
  },
};
