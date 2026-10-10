"use strict";

export const dividerMethods = {
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

    document.addEventListener("mousemove", (e) => {
      if (draggingV) {
        const main = document.getElementById("main");
        const rect = main.getBoundingClientRect();
        const w = Math.max(140, Math.min(600, e.clientX - rect.left));
        sidebar.style.width = w + "px";
      }
    });

    document.addEventListener("mouseup", () => {
      if (draggingV) {
        draggingV = false;
        vDiv.classList.remove("dragging");
        document.body.style.cursor = "";
        document.body.style.userSelect = "";
      }
    });
  },
};
