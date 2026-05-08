"use strict";

import { t } from "../core/i18n.js";

export const tableMethods = {
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
      this.setStatus({ key: "status.copiedRow" });
    });
  },
};
