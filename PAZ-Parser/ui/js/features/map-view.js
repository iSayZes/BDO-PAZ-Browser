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
// Pin marker sizes in px; the CSS draws them (25-map-view.css, .map-pin and
// .map-pin-facing). A pin with a heading is an arrow, a bigger target.
const PIN_SIZE = 14;
const FACING_PIN_SIZE = 22;

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

  // Pushed on every pin change of the map API: the full list.
  onMapPinsChanged(pins) {
    this._mapPins = pins;
    this._drawMapPins();
  },

  _drawMapPins() {
    const layer = this._mapPinLayer;
    if (!layer) return;
    layer.clearLayers();
    this._mapPins.forEach((pin) => {
      const label = pin.label || t(`map.pinTypes.${pin.type}`);
      L.marker(L.latLng(pin.z, pin.x), { icon: this._mapPinIcon(pin), keyboard: false })
        .bindTooltip(`${label} · ${t("map.coords", { x: formatCount(Math.round(pin.x)), z: formatCount(Math.round(pin.z)) })}`)
        .addTo(layer);
    });
  },

  // A dot, or with a heading an arrow turned that many degrees clockwise from
  // north. North is up on this map, so the CSS rotation is the heading itself.
  _mapPinIcon(pin) {
    if (pin.heading === null || pin.heading === undefined) {
      return L.divIcon({ className: `map-pin map-pin-${pin.type}`, iconSize: [PIN_SIZE, PIN_SIZE] });
    }
    return L.divIcon({
      className: `map-pin-facing map-pin-facing-${pin.type}`,
      html: `<div class="map-pin-arrow" style="transform: rotate(${Number(pin.heading)}deg)"></div>`,
      iconSize: [FACING_PIN_SIZE, FACING_PIN_SIZE],
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
      coords.textContent = t("map.coords", {
        x: formatCount(Math.round(e.latlng.lng)),
        z: formatCount(Math.round(e.latlng.lat)),
      });
      coords.hidden = false;
    });
    map.on("mouseout", () => {
      coords.hidden = true;
    });
    this._leafletMap = map;
    this._mapPinLayer = L.layerGroup().addTo(map);
    this._loadMapPins();
  },

  async _loadMapPins() {
    try {
      this._mapPins = await window.pywebview.api.get_map_pins();
    } catch {
      // The pushes keep the list current from here on.
    }
    this._drawMapPins();
  },

  _closeLeaflet() {
    if (!this._leafletMap) return;
    this._leafletMap.remove();
    this._leafletMap = null;
    this._mapPinLayer = null;
  },
};
