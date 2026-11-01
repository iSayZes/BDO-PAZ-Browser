"use strict";

export const app = {
  _selectedPath: null,
  _currentFolderPath: null,
  // Set once the backend has loaded a folder; a cancelled re-open restores it.
  _isFolderLoaded: false,
  _extractPaths: new Set(),
  _searchTimer: null,
  _searchSeq: 0,
  _selectSeq: 0,
  _inSearch: false,
  // Loads the next page of file search results on scroll (search.js).
  _searchMoreObserver: null,
  _parsedHtml: null,
  _hexHtml: null,
  // A parsed text format's source view (.ai), shown on the Text tab.
  _textHtml: null,
  _activeTab: "hex",
  _inGlobalSearch: false,
  _hexPage: 0,
  _hexTotalPages: 1,
  _parsedPage: 0,
  _parsedTotalPages: 1,
  // Active parsed-table sort, {field, dir}, or null for file order.
  _parsedSort: null,
  // Behaviors picked in the .ai behavior filter; rows of other behaviors are
  // hidden on every parsed page of the open file (preview-views.js).
  _aiFilter: new Set(),
  // Bumped per parsed page request so late responses can be dropped.
  _parsedPageSeq: 0,
  // The WebGL renderer of the open Model tab, or null (model-view.js).
  _modelRenderer: null,
  // Its rig toolbar's skeleton and clip player, or null (model-rig.js).
  _modelRig: null,
  // The open view of the toolbar rail (views.js).
  _activeView: "files",
  // Map view (map-view.js): the Leaflet map once the tiles are built, and a
  // counter that a folder load or a pushed state bumps, so a late
  // get_world_map() answer is dropped.
  _leafletMap: null,
  _mapSeq: 0,
  // The map API's pins (map_pins.py), the Leaflet layer that draws them and
  // its markers by pin id, and the game icons by name with the URL template
  // of their files (map_icons_build.py).
  _mapPins: [],
  _mapPinLayer: null,
  _mapPinMarkers: null,
  _mapIcons: {},
  _mapIconUrl: "",
  // The worldmap node layer (map-nodes.js): its layer group and {node, name,
  // marker} entries; the Filters panel's choices (map-filters.js), read from
  // the config when the first map opens.
  _mapNodes: null,
  _mapFilter: null,
};
