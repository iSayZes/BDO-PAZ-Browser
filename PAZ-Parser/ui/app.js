"use strict";

import { app } from "./js/core/state.js";
import { initMethods } from "./js/features/init.js";
import { folderMethods } from "./js/features/folder.js";
import { treeMethods } from "./js/features/tree.js";
import { detailsMethods } from "./js/features/details.js";
import { searchMethods } from "./js/features/search.js";
import { extractionMethods } from "./js/features/extraction.js";
import { previewPagingMethods } from "./js/features/preview-paging.js";
import { statusMethods } from "./js/features/status.js";
import { tableMethods } from "./js/features/table.js";
import { dividerMethods } from "./js/features/dividers.js";
import { setupMethods } from "./js/features/setup.js";
import { helperMethods } from "./js/core/helpers.js";
import { tabSearchMethods } from "./js/features/tab-search.js";

Object.assign(
  app,
  initMethods,
  folderMethods,
  treeMethods,
  detailsMethods,
  searchMethods,
  extractionMethods,
  previewPagingMethods,
  statusMethods,
  tableMethods,
  dividerMethods,
  setupMethods,
  helperMethods,
  tabSearchMethods,
);

window.app = app;
window.addEventListener("pywebviewready", () => app.init());
