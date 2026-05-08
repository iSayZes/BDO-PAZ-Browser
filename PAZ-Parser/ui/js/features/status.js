"use strict";

import { t } from "../core/i18n.js";

export const statusMethods = {
  setStatus(data) {
    const msg = data.key ? t(data.key, data.args ?? {}) : (data.message ?? "");
    document.getElementById("status-text").textContent = msg;
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
