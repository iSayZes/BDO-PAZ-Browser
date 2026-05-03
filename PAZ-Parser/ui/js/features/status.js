"use strict";

export const statusMethods = {
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
};
