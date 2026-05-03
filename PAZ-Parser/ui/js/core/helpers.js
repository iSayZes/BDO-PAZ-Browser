"use strict";

export const helperMethods = {
  _esc(str) {
    const d = document.createElement("div");
    d.textContent = String(str ?? "");
    return d.innerHTML;
  },
};
