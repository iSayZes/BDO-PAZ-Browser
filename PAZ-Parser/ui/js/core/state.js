"use strict";

export const app = {
  _selectedPath: null,
  _currentFolderPath: null,
  _extractPaths: new Set(),
  _searchTimer: null,
  _searchSeq: 0,
  _inSearch: false,
  _parsedHtml: null,
  _hexHtml: null,
  _activeTab: "hex",
  _hexPage: 0,
  _hexTotalPages: 1,
  _parsedPage: 0,
  _parsedTotalPages: 1,
};
