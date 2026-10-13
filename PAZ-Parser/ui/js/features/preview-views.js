"use strict";

import { t } from "../core/i18n.js";

// The toolbars of the text and image views (preview_views.py builds them):
// Wrap lines, image zoom and background, and the pixel under the cursor.
// Also the links between rows of a parsed table (`goto-record`, the state
// names of an .ai script), links into another table (`open-record`, the
// characters that run an .ai script) and the .ai behavior filter (`ai-filter`).
const ZOOM_CLASSES = ["zoom-fit", "zoom-1", "zoom-2"];
const BACKGROUND_CLASSES = ["bg-checker", "bg-dark", "bg-light"];

function setPressed(button) {
  button.parentElement.querySelectorAll("button").forEach((other) => {
    const isOn = other === button;
    other.classList.toggle("active", isOn);
    other.setAttribute("aria-pressed", String(isOn));
  });
}

function hex2(value) {
  return value.toString(16).padStart(2, "0").toUpperCase();
}

export const previewViewMethods = {
  // One listener for every view the preview shows; set up once in init.
  _setupPreviewViews() {
    document.getElementById("preview-content").addEventListener("click", (event) => {
      const button = event.target.closest("button[data-action]");
      if (!button) return;
      const action = button.dataset.action;
      if (action === "toggle-wrap") this._toggleTextWrap(button);
      else if (action === "image-zoom") this._setImageZoom(button);
      else if (action === "image-background") this._setImageBackground(button);
      else if (action === "goto-record") this._showParsedRecord(Number(button.dataset.record));
      else if (action === "ai-filter") this._toggleAiFilter(button.dataset.value);
      else if (action === "open-record") this._openRecord(button.dataset);
    });
  },

  // Called after a text or image view is put into the preview.
  _initPreviewView(root) {
    const view = root.querySelector(".img-view");
    if (view) this._initImageReadout(view);
  },

  // Opens the file at `path` on its Parsed tab and pages to the first record
  // whose `field` reads `value` (Api.find_record), as Ctrl+F marks a match.
  async _openRecord({ path, field, value }) {
    await this._selectFile(path, path.slice(path.lastIndexOf("/") + 1), "parsed");
    if (this._selectedPath !== path || this._parsedHtml === null) return;
    if (this._activeTab !== "parsed") this.switchTab("parsed", { isSaved: false });
    const result = await window.pywebview.api.find_record(path, field, value);
    if (this._selectedPath !== path) return;
    if (result.error) {
      this.setStatus({ key: "status.pageError", args: { message: result.error } });
    } else if (result.position === null) {
      this.setStatus({ key: "status.recordNotFound", args: { field, value } });
    } else {
      await this._showParsedRecord(result.position);
    }
  },

  _toggleAiFilter(value) {
    if (this._aiFilter.has(value)) this._aiFilter.delete(value);
    else this._aiFilter.add(value);
    this._applyAiFilter(document.getElementById("preview-content"));
  },

  // Shows only the rows whose state name carries a picked `data-behavior`
  // (handlers/_ai/aiscript/render.py), on the page in `root`; none picked
  // shows every row. The pick holds while paging and sorting.
  _applyAiFilter(root) {
    const bar = root.querySelector(".ai-filter");
    if (!bar) return;
    bar.querySelectorAll('button[data-action="ai-filter"]').forEach((chip) => {
      const isOn = this._aiFilter.has(chip.dataset.value);
      chip.classList.toggle("active", isOn);
      chip.setAttribute("aria-pressed", String(isOn));
    });
    const rows = [...root.querySelectorAll(".data-table tbody tr")];
    let shown = 0;
    for (const row of rows) {
      const behavior = row.querySelector(".ai-name")?.dataset.behavior;
      row.hidden = this._aiFilter.size > 0 && !this._aiFilter.has(behavior);
      if (!row.hidden) shown += 1;
    }
    bar.querySelector(".ai-filter-count").textContent = this._aiFilter.size
      ? bar.dataset.shown.replace("{shown}", shown).replace("{total}", rows.length)
      : "";
  },

  // A link or a find match that lands on a row the filter hides clears the filter.
  _revealFilteredRow(row) {
    if (!row.hidden) return;
    this._aiFilter.clear();
    this._applyAiFilter(document.getElementById("preview-content"));
  },

  _toggleTextWrap(button) {
    const lines = button.closest(".text-view-wrap")?.querySelector(".text-lines");
    if (!lines) return;
    const isOn = lines.classList.toggle("wrap");
    button.setAttribute("aria-pressed", String(isOn));
    button.classList.toggle("active", isOn);
  },

  _setImageZoom(button) {
    const view = button.closest(".img-view");
    const img = view?.querySelector(".img-scroll img");
    if (!img) return;
    setPressed(button);
    view.classList.remove(...ZOOM_CLASSES);
    view.classList.add(`zoom-${button.dataset.value}`);
    // Ctrl+wheel zoom (setup.js) sets style.zoom; a button starts from scratch.
    img.style.zoom = "";
    const factor = Number(button.dataset.value);
    img.style.width = Number.isFinite(factor) ? `${img.naturalWidth * factor}px` : "";
  },

  _setImageBackground(button) {
    const scroll = button.closest(".img-view")?.querySelector(".img-scroll");
    if (!scroll) return;
    setPressed(button);
    scroll.classList.remove(...BACKGROUND_CLASSES);
    scroll.classList.add(`bg-${button.dataset.value}`);
  },

  // "x 512 · y 384" and the pixel's color, read from a canvas copy of the image.
  _initImageReadout(view) {
    const img = view.querySelector(".img-scroll img");
    const readout = view.querySelector(".img-readout");
    if (!img || !readout) return;
    let pixels = null;

    const load = () => {
      try {
        const canvas = document.createElement("canvas");
        canvas.width = img.naturalWidth;
        canvas.height = img.naturalHeight;
        const ctx = canvas.getContext("2d", { willReadFrequently: true });
        ctx.drawImage(img, 0, 0);
        pixels = ctx.getImageData(0, 0, canvas.width, canvas.height);
      } catch {
        pixels = null; // the readout stays empty, the image still shows
      }
    };
    if (img.complete) load();
    else img.addEventListener("load", load, { once: true });

    img.addEventListener("mousemove", (event) => {
      if (!pixels) return;
      const x = Math.min(pixels.width - 1, Math.floor((event.offsetX / img.clientWidth) * pixels.width));
      const y = Math.min(pixels.height - 1, Math.floor((event.offsetY / img.clientHeight) * pixels.height));
      const i = (y * pixels.width + x) * 4;
      const [r, g, b, a] = pixels.data.slice(i, i + 4);
      const color = `#${hex2(r)}${hex2(g)}${hex2(b)}`;
      readout.innerHTML =
        `<span>x ${x} · y ${y}</span>` +
        `<span class="img-swatch" style="background:${color}"></span>` +
        `<span>${color} · ${this._esc(t("preview.alpha", { value: a }))}</span>`;
    });
    img.addEventListener("mouseleave", () => {
      readout.textContent = "";
    });
  },
};
