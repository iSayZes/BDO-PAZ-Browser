"use strict";

import { t } from "../core/i18n.js";

// The map API's pins on the Map view (map_pins.py, docs/map-api.md): markers
// kept by pin id and updated in place, a popup with Remove, and the game icon
// of a pin or a dot or an arrow without one.

// Pin marker sizes in px; the CSS draws them (25-map-view.css, .map-pin and
// .map-pin-facing). A pin with a heading is an arrow, a bigger target.
const PIN_SIZE = 14;
const FACING_PIN_SIZE = 22;

export const mapPinMethods = {
  // Pushed on every pin change of the map API: the full list.
  onMapPinsChanged(pins) {
    this._mapPins = pins;
    this._drawMapPins();
    this._refreshMapFilters();
  },

  // Updates the markers in place, so a pin's open popup stays open while
  // another pin, such as a live player pin, moves. The Filters panel's Player
  // and Markers chips (map-filters.js) leave their pins off.
  _drawMapPins() {
    const layer = this._mapPinLayer;
    if (!layer) return;
    const markers = this._mapPinMarkers;
    const pins = this._mapPins.filter((pin) => this._isMapLayerOn(pin.type === "player" ? "player" : "markers"));
    const ids = new Set(pins.map((pin) => pin.id));
    markers.forEach((marker, id) => {
      if (ids.has(id)) return;
      layer.removeLayer(marker);
      markers.delete(id);
    });
    pins.forEach((pin) => {
      const marker = markers.get(pin.id);
      if (marker) {
        this._updateMapPinMarker(marker, pin);
      } else {
        markers.set(pin.id, this._mapPinMarker(pin).addTo(layer));
      }
    });
  },

  _mapPinMarker(pin) {
    const marker = L.marker(L.latLng(pin.z, pin.x), { icon: this._mapPinIcon(pin), keyboard: false });
    marker.pin = pin;
    marker.bindTooltip(this._mapPinTooltip(pin));
    marker.bindPopup(() => this._mapPinPopup(marker.pin), { className: "map-pin-popup" });
    return marker;
  },

  _updateMapPinMarker(marker, pin) {
    const old = marker.pin;
    marker.pin = pin;
    marker.setLatLng(L.latLng(pin.z, pin.x));
    if (old.icon !== pin.icon || old.heading !== pin.heading) marker.setIcon(this._mapPinIcon(pin));
    marker.setTooltipContent(this._mapPinTooltip(pin));
    if (marker.isPopupOpen()) marker.setPopupContent(this._mapPinPopup(pin));
  },

  _mapPinName(pin) {
    return pin.label || t(`map.pinTypes.${pin.type}`);
  },

  _mapPinTooltip(pin) {
    // Leaflet sets a string tooltip as HTML, and a label comes from another program.
    return `${this._esc(this._mapPinName(pin))} · ${this._esc(this._mapCoords(pin.x, pin.z))}`;
  },

  // A click on a pin: its name, position, whether it is saved, and Remove.
  _mapPinPopup(pin) {
    const box = document.createElement("div");
    const name = document.createElement("div");
    name.className = "map-pin-popup-name";
    name.textContent = this._mapPinName(pin);
    const coords = document.createElement("div");
    coords.className = "map-pin-popup-coords";
    coords.textContent = this._mapCoords(pin.x, pin.z);
    box.append(name, coords);
    if (pin.saved) {
      const saved = document.createElement("div");
      saved.className = "map-pin-popup-saved";
      saved.textContent = t("map.pinSaved");
      box.append(saved);
    }
    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "btn-danger map-pin-popup-remove";
    remove.textContent = t("map.removePin");
    remove.addEventListener("click", () => this._removeMapPin(pin.id));
    box.append(remove);
    return box;
  },

  // The store pushes the new list, which drops the marker.
  async _removeMapPin(id) {
    try {
      await window.pywebview.api.remove_map_pin(id);
    } catch (ex) {
      this.setStatus({ key: "status.pinRemoveFailed", args: { message: String(ex) } });
    }
  },

  // The pin's game icon (map_icons.py); without one a dot, or with a heading
  // an arrow turned that many degrees clockwise from north. North is up on
  // this map, so the CSS rotation is the heading itself. An icon that turns
  // (the player pointer) faces north without a heading.
  _mapPinIcon(pin) {
    const hasHeading = pin.heading !== null && pin.heading !== undefined;
    const icon = pin.icon ? this._mapIcons[pin.icon] : undefined;
    if (icon) return this._mapGameIcon(pin.icon, icon, { heading: hasHeading ? pin.heading : 0 });
    if (!hasHeading) {
      return L.divIcon({ className: `map-pin map-pin-${pin.type}`, iconSize: [PIN_SIZE, PIN_SIZE] });
    }
    return L.divIcon({
      className: `map-pin-facing map-pin-facing-${pin.type}`,
      html: `<div class="map-pin-arrow" style="transform: rotate(${Number(pin.heading)}deg)"></div>`,
      iconSize: [FACING_PIN_SIZE, FACING_PIN_SIZE],
    });
  },
};
