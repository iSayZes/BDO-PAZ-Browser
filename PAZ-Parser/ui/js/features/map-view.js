"use strict";

import { t } from "../core/i18n.js";

// The Map view (api/bdo_api_world_map.py): a prompt until the map tiles are
// built, the build's progress, then the tiles in Leaflet. The map's CRS is in
// world units (cm), one sector (12,800) per pixel at zoom 0, so a world
// position goes on the map as L.latLng(z, x) with no conversion (world_map.py).
const SECTOR_CM = 12800;
const TILE_PX = 256;
// Panning stops this far past the map's edge, as a share of its size.
const PAN_MARGIN = 0.1;
const VIEW_PARTS = ["map-canvas", "map-message", "map-prompt", "map-progress"];

function worldCrs() {
  return L.extend({}, L.CRS.Simple, {
    transformation: new L.Transformation(1 / SECTOR_CM, 0, -1 / SECTOR_CM, 0),
  });
}

function formatCount(n) {
  return Number(n).toLocaleString();
}

export const mapViewMethods = {
  // The view's onShow (views.js).
  async _showMapView() {
    if (this._leafletMap) {
      // Leaflet measured the canvas while it was hidden.
      this._leafletMap.invalidateSize();
      return;
    }
    if (!this._isFolderLoaded) {
      this._showMapPart("map-message", t("map.noFolder"));
      return;
    }
    const seq = ++this._mapSeq;
    let state;
    try {
      state = await window.pywebview.api.get_world_map();
    } catch (ex) {
      state = { state: "prompt", tiles: 0, bytes: 0, error: String(ex) };
    }
    if (seq === this._mapSeq) this._applyMapState(state);
  },

  // The prompt's OK: turns on "Keep map updated" and starts the build.
  async buildWorldMap() {
    const seq = ++this._mapSeq;
    const state = await window.pywebview.api.build_world_map();
    if (seq === this._mapSeq) this._applyMapState(state);
  },

  // Pushed when a build starts, ends or fails.
  onMapStateChanged(state) {
    this._mapSeq++;
    if (this._activeView === "map") this._applyMapState(state);
  },

  // Pushed while a build runs: {zoom, done, total, step, steps}.
  onMapBuildProgress(progress) {
    if (this._activeView === "map" && !this._leafletMap) this._showMapProgress(progress);
  },

  // "X 13,800 · Z 76,996" for a world position, as the cursor readout shows it.
  _mapCoords(x, z) {
    return t("map.coords", { x: formatCount(Math.round(x)), z: formatCount(Math.round(z)) });
  },

  // A game icon (map_icons.py) as a Leaflet icon, `height` px tall (its own
  // size by default), on the position at its anchor or, `centered`, its middle.
  // The PNG comes from the local server, like the tiles (map_icons_build.py).
  _mapGameIcon(name, icon, { heading = 0, height = icon.size[1], centered = false } = {}) {
    const url = this._mapIconUrl.replace("{name}", encodeURIComponent(name));
    const scale = height / icon.size[1];
    const width = icon.size[0] * scale;
    const [anchorX, anchorY] = centered ? [width / 2, height / 2] : icon.anchor.map((value) => value * scale);
    const turn = icon.turns
      ? ` style="transform: rotate(${Number(heading)}deg); transform-origin: ${anchorX}px ${anchorY}px"`
      : "";
    return L.divIcon({
      className: "map-pin-icon",
      html: `<img src="${url}" width="${width}" height="${height}" alt=""${turn}>`,
      iconSize: [width, height],
      iconAnchor: [anchorX, anchorY],
    });
  },

  // A new folder: drop the old client's map, and show the new one if the view is open.
  _resetMapView() {
    this._mapSeq++;
    this._closeLeaflet();
    if (this._activeView === "map") this._showMapView();
  },

  _applyMapState(state) {
    switch (state.state) {
      case "ready":
        this._openLeaflet(state);
        break;
      case "building":
        this._closeLeaflet();
        this._showMapProgress(state.progress);
        break;
      case "prompt":
        this._closeLeaflet();
        this._showMapPrompt(state);
        break;
      case "noTiles":
        this._showMapPart("map-message", t("map.noTiles"));
        break;
      default:
        this._showMapPart("map-message", t("map.noFolder"));
    }
  },

  _showMapPart(id, message) {
    VIEW_PARTS.forEach((part) => {
      document.getElementById(part).hidden = part !== id;
    });
    if (id !== "map-canvas") document.getElementById("map-coords").hidden = true;
    document.getElementById("map-filters").hidden = id !== "map-canvas";
    if (message !== undefined) document.getElementById(id).textContent = message;
  },

  _showMapPrompt(state) {
    document.getElementById("map-prompt-text").textContent = t("map.promptText", {
      tiles: formatCount(state.tiles),
      size: this._fmtBytes(state.bytes),
    });
    const error = document.getElementById("map-prompt-error");
    error.textContent = state.error ? t("map.failed", { message: state.error }) : "";
    error.hidden = !state.error;
    this._showMapPart("map-prompt");
  },

  // `progress` is null until the first tile of the first zoom is under way.
  _showMapProgress(progress) {
    const { zoom, done, total, step, steps } = progress ?? { zoom: 0, done: 0, total: 0, step: 0, steps: 0 };
    const percent = total ? Math.floor((done * 100) / total) : 0;
    document.getElementById("map-progress-zoom").textContent = progress
      ? t("map.progressZoom", { zoom, step, steps })
      : t("map.progressStarting");
    document.getElementById("map-progress-tiles").textContent = t("map.progressTiles", {
      done: formatCount(done),
      total: formatCount(total),
      percent,
    });
    document.getElementById("map-progress-fill").style.width = `${percent}%`;
    this._showMapPart("map-progress");
  },

  _openLeaflet(state) {
    this._showMapPart("map-canvas");
    if (this._leafletMap) return;

    const b = state.bounds;
    const bounds = L.latLngBounds([b.minZ, b.minX], [b.maxZ, b.maxX]);
    const map = L.map("map-canvas", {
      crs: worldCrs(),
      minZoom: state.minZoom,
      maxZoom: state.maxZoom,
      maxBounds: bounds.pad(PAN_MARGIN),
      attributionControl: false,
    });
    L.tileLayer(state.tileUrl, {
      tileSize: TILE_PX,
      minZoom: state.minZoom,
      maxZoom: state.maxZoom,
      minNativeZoom: state.minZoom,
      maxNativeZoom: state.nativeZoom,
      bounds,
      noWrap: true,
    }).addTo(map);
    map.fitBounds(bounds);

    const coords = document.getElementById("map-coords");
    map.on("mousemove", (e) => {
      coords.textContent = this._mapCoords(e.latlng.lng, e.latlng.lat);
      coords.hidden = false;
    });
    map.on("mouseout", () => {
      coords.hidden = true;
    });
    this._leafletMap = map;
    this._mapIconUrl = state.iconUrl;
    this._addMapNodeLayer(map);
    this._mapPinLayer = L.layerGroup().addTo(map);
    this._mapPinMarkers = new Map();
    this._loadMapLayers();
  },

  // The saved filters and the icons first: the nodes and pins draw with them.
  async _loadMapLayers() {
    await this._loadMapFilter();
    try {
      this._mapIcons = await window.pywebview.api.get_map_icons();
    } catch {
      // Without icons every pin is a dot or an arrow, and there are no nodes.
    }
    await Promise.all([this._loadMapNodes(), this._loadMapPins()]);
    if (this._leafletMap) this._renderMapFilters();
  },

  // Best effort. A push can draw pins before the icons are in, so the
  // markers are made again once they are.
  async _loadMapPins() {
    try {
      this._setMapPins(await window.pywebview.api.get_map_pins());
    } catch {
      // The pushes keep the list current from here on.
    }
    if (!this._mapPinLayer) return;
    this._mapPinLayer.clearLayers();
    this._mapPinMarkers.clear();
    this._drawMapPins();
  },

  _closeLeaflet() {
    if (!this._leafletMap) return;
    this._leafletMap.remove();
    this._leafletMap = null;
    this._mapNodes = null;
    this._mapPinLayer = null;
    this._mapPinMarkers = null;
    // The next map may be another client's, with icons of its own.
    this._mapIcons = {};
    this._mapIconUrl = "";
  },
};
