"use strict";

import { iconSvg } from "../core/icons.js";
import { t } from "../core/i18n.js";

// The Map view's Filters panel:
// a node search, Hide All, a Filters card of layer chips (player, markers)
// and one card per kind of map content, each a collapsible grid of rows with
// an icon, a name and a count. A chip or row is a toggle that dims when off.
// Only the Nodes rows start on. The toggles a viewer changed, collapsed cards and whether the panel is
// open are saved in the app's config (api/bdo_config.py map_filters_setting)
// and read once per page; the search is not saved.
//
// To add a layer (trees, ores, NPCs, monsters): a chip in FILTER_LAYERS
// and/or a card in FILTER_GROUPS, with its rows and drawing in a module of
// its own, as map-nodes.js and map-pins.js do. The layer asks
// `_isMapLayerOn(id)` and `_isMapFilterShown(groupId, key)` before drawing.

// Chips: id (storage key), label and icon, whether it starts on, when it is
// disabled (nothing of it on the map), whether it turns on when it goes from
// disabled to enabled, and the redraw after a change.
const FILTER_LAYERS = [
  {
    id: "player",
    label: "map.pinTypes.player",
    icon: "navigation",
    defaultOn: false,
    onWhenEnabled: true,
    disabled: (app) => !app._mapPins.some((pin) => pin.type === "player"),
    apply: (app) => app._drawMapPins(),
  },
  {
    id: "markers",
    label: "map.filters.markers",
    icon: "map-pin",
    defaultOn: false,
    disabled: (app) => !app._mapPins.some((pin) => pin.type === "marker"),
    apply: (app) => app._drawMapPins(),
  },
];
// Cards: id (storage key), title, whether its rows start on, `rows(app)`
// listing {key, label, count, icon}, optional `options(app)` listing toggles
// of the same shape shown under the rows (the eye and the badge leave them
// out), `shown(app)` the count of things the filters let through, and the
// redraw after a change.
const FILTER_GROUPS = [
  {
    id: "nodes",
    title: "map.filters.nodes",
    defaultOn: true,
    rows: (app) => app._mapNodeFilterRows(),
    options: (app) => app._mapNodeFilterOptions(),
    shown: (app) => app._mapNodeShownCount(),
    apply: (app) => app._applyMapNodeFilter(),
  },
];
// Storage key of the chips, next to the cards' ids; the Filters card's id for collapsing.
const LAYERS_ID = "layers";

function isObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

// The panel's state from the saved config value: choices {groupId or
// LAYERS_ID: {key: on}}, only the toggles the user changed.
function fromSaved(saved) {
  const value = isObject(saved) ? saved : {};
  const choices = isObject(value.choices) ? value.choices : {};
  return {
    choices: Object.fromEntries(Object.entries(choices).filter(([, rows]) => isObject(rows))),
    collapsed: new Set(Array.isArray(value.collapsed) ? value.collapsed : []),
    open: value.open !== false,
    search: "",
  };
}

export function countBy(items, key) {
  const counts = new Map();
  items.forEach((item) => counts.set(item[key], (counts.get(item[key]) ?? 0) + 1));
  return counts;
}

function element(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

export const mapFilterMethods = {
  // The saved choices, read once per page; the search starts empty.
  // The saved choices, read from the config once per page before the map
  // draws (map-view.js _loadMapLayers). Defaults until then.
  async _loadMapFilter() {
    if (this._mapFilter) return;
    let saved = {};
    try {
      saved = await window.pywebview.api.get_map_filters();
    } catch {
      // The defaults, until the next save writes the config.
    }
    this._mapFilter ??= fromSaved(saved);
  },

  _mapFilterState() {
    if (!this._mapFilter) this._mapFilter = fromSaved({});
    return this._mapFilter;
  },

  _setMapFilterChoice(groupId, key, on) {
    const { choices } = this._mapFilterState();
    choices[groupId] = { ...choices[groupId], [key]: on };
  },

  // Writes the choices to the config; a failure leaves them for this run only.
  async _saveMapFilter() {
    const { choices, collapsed, open } = this._mapFilterState();
    try {
      await window.pywebview.api.save_map_filters({ choices, collapsed: [...collapsed], open });
    } catch (ex) {
      this.setStatus({ key: "status.mapFiltersSaveFailed", args: { message: String(ex) } });
    }
  },

  // Whether chip `id` is on: the viewer's choice, else its default.
  _isMapLayerOn(id) {
    const choice = this._mapFilterState().choices[LAYERS_ID]?.[id];
    if (typeof choice === "boolean") return choice;
    return FILTER_LAYERS.find((layer) => layer.id === id)?.defaultOn ?? false;
  },

  // Whether row `key` of card `groupId` is on: the viewer's choice, else the card's default.
  _isMapFilterShown(groupId, key) {
    const choice = this._mapFilterState().choices[groupId]?.[key];
    if (typeof choice === "boolean") return choice;
    return FILTER_GROUPS.find((group) => group.id === groupId)?.defaultOn ?? false;
  },

  toggleMapFilters() {
    const state = this._mapFilterState();
    state.open = !state.open;
    this._saveMapFilter();
    this._showMapFiltersOpen();
  },

  onMapFilterSearch(value) {
    this._mapFilterState().search = value.trim().toLocaleLowerCase();
    this._applyMapNodeFilter();
  },

  _showMapFiltersOpen() {
    const { open } = this._mapFilterState();
    document.getElementById("map-filters-panel").hidden = !open;
    document.getElementById("map-filters-toggle").setAttribute("aria-expanded", String(open));
  },

  // Turns every chip and row off.
  hideAllMapFilters() {
    FILTER_LAYERS.forEach((layer) => this._setMapFilterChoice(LAYERS_ID, layer.id, false));
    FILTER_GROUPS.forEach((group) =>
      [...group.rows(this), ...(group.options?.(this) ?? [])].forEach((row) =>
        this._setMapFilterChoice(group.id, row.key, false),
      ),
    );
    this._mapFiltersChanged([...FILTER_LAYERS, ...FILTER_GROUPS]);
  },

  // After a toggle: save, redraw the layers `changed` names, rebuild the
  // panel when a map is open.
  _mapFiltersChanged(changed) {
    this._saveMapFilter();
    new Set(changed.map((entry) => entry.apply)).forEach((apply) => apply(this));
    if (this._mapNodes) this._renderMapFilters();
  },

  // Built when a map opens and after every toggle; the scroll position stays.
  _renderMapFilters() {
    const groups = document.getElementById("map-filters-groups");
    groups.replaceChildren(this._mapLayerCard(), ...FILTER_GROUPS.map((group) => this._mapFilterCard(group)));
    this._mapFilterSignature = this._mapFilterSignatureNow();
    document.getElementById("map-filters-search").value = this._mapFilterState().search;
    this._showMapFiltersOpen();
  },

  // A live player pin pushes twice a second: the panel is built again only
  // when a chip turns enabled or disabled, so a click on it is not lost.
  _refreshMapFilters() {
    if (!this._mapNodes || this._mapFilterSignature === this._mapFilterSignatureNow()) return;
    this._renderMapFilters();
  },

  _mapFilterSignatureNow() {
    return FILTER_LAYERS.map((layer) => Boolean(layer.disabled?.(this))).join();
  },

  _disabledMapLayers() {
    return FILTER_LAYERS.filter((layer) => layer.disabled?.(this));
  },

  // After a pin change: turns on the `onWhenEnabled` chips of `wasDisabled`
  // that are enabled now, so the first player pin shows. The saved choices
  // load first, or the save would write the defaults over them.
  async _turnOnEnabledMapLayers(wasDisabled) {
    const enabled = wasDisabled.filter((layer) => layer.onWhenEnabled && !layer.disabled?.(this));
    if (!enabled.length) return;
    await this._loadMapFilter();
    enabled.forEach((layer) => this._setMapFilterChoice(LAYERS_ID, layer.id, true));
    this._mapFiltersChanged(enabled);
  },

  // The Filters card: one chip per layer.
  _mapLayerCard() {
    const grid = element("div", "map-filter-chips");
    FILTER_LAYERS.forEach((layer) => {
      const disabled = Boolean(layer.disabled?.(this));
      const on = !disabled && this._isMapLayerOn(layer.id);
      const chip = this._mapFilterToggle("map-filter-chip", on, disabled);
      chip.innerHTML = iconSvg(layer.icon);
      chip.append(element("span", "map-filter-name", t(layer.label)));
      chip.addEventListener("click", () => {
        this._setMapFilterChoice(LAYERS_ID, layer.id, !on);
        this._mapFiltersChanged([layer]);
      });
      grid.append(chip);
    });
    const head = element("div", "map-filter-card-head");
    head.innerHTML = iconSvg("filter");
    head.append(element("span", "map-filter-card-title", t("map.filters.title")));
    return this._mapFilterCardFrame(LAYERS_ID, head, grid);
  },

  // A card: title, "shown / total" badge, an eye button for all its rows and
  // a collapse button, then its rows in a two-column grid and its options
  // under them.
  _mapFilterCard(group) {
    const rows = group.rows(this);
    const body = element("div", "map-filter-card-body");
    const grid = element("div", "map-filter-grid");
    grid.append(...rows.map((row) => this._mapFilterRowButton(group, row)));
    body.append(grid);
    const options = group.options?.(this) ?? [];
    if (options.length) {
      const optionGrid = element("div", "map-filter-grid map-filter-options");
      optionGrid.append(...options.map((option) => this._mapFilterRowButton(group, option)));
      body.append(optionGrid);
    }

    const total = rows.reduce((sum, row) => sum + row.count, 0);
    const anyOn = rows.some((row) => this._isMapFilterShown(group.id, row.key));
    const head = element("div", "map-filter-card-head");
    head.append(
      element("span", "map-filter-card-title", t(group.title)),
      element("span", "map-filter-badge", `${group.shown(this).toLocaleString()} / ${total.toLocaleString()}`),
    );
    const eye = element("button", "map-filter-icon-button");
    eye.type = "button";
    eye.title = t("map.filters.toggleGroup");
    eye.setAttribute("aria-label", eye.title);
    eye.innerHTML = iconSvg(anyOn ? "eye" : "eye-off");
    eye.addEventListener("click", () => {
      rows.forEach((row) => this._setMapFilterChoice(group.id, row.key, !anyOn));
      this._mapFiltersChanged([group]);
    });
    head.append(eye);
    return this._mapFilterCardFrame(group.id, head, body);
  },

  // One toggle of a card: icon, name and count, dimmed when off.
  _mapFilterRowButton(group, row) {
    const on = this._isMapFilterShown(group.id, row.key);
    const button = this._mapFilterToggle("map-filter-row", on, false);
    button.append(row.icon, element("span", "map-filter-name", row.label), element("span", "map-filter-count", row.count.toLocaleString()));
    button.title = row.label;
    button.addEventListener("click", () => {
      this._setMapFilterChoice(group.id, row.key, !on);
      this._mapFiltersChanged([group]);
    });
    return button;
  },

  // A card's frame: `head` with the collapse button added, and `body`.
  _mapFilterCardFrame(id, head, body) {
    const card = element("section", "map-filter-card");
    card.dataset.card = id;
    body.hidden = this._mapFilterState().collapsed.has(id);
    const collapse = element("button", "map-filter-icon-button");
    collapse.type = "button";
    collapse.title = t("map.filters.collapse");
    collapse.setAttribute("aria-label", collapse.title);
    collapse.setAttribute("aria-expanded", String(!body.hidden));
    collapse.innerHTML = iconSvg(body.hidden ? "chevron-down" : "chevron-up");
    collapse.addEventListener("click", () => {
      const { collapsed } = this._mapFilterState();
      if (collapsed.has(id)) collapsed.delete(id);
      else collapsed.add(id);
      this._saveMapFilter();
      this._renderMapFilters();
    });
    head.append(collapse);
    card.append(head, body);
    return card;
  },

  _mapFilterToggle(className, on, disabled) {
    const button = element("button", className);
    button.type = "button";
    button.disabled = disabled;
    button.setAttribute("aria-pressed", String(on));
    button.classList.toggle("on", on);
    return button;
  },

  // A row icon from the app's icon sprite (icons.js), for a toggle with no game icon.
  _mapFilterSymbol(name) {
    const holder = element("span", "map-filter-icon map-filter-symbol");
    holder.innerHTML = iconSvg(name);
    return holder;
  },

  // A row icon: the game icon `name` from the map's icon files.
  _mapFilterIcon(name) {
    const img = element("img", "map-filter-icon");
    img.alt = "";
    if (this._mapIcons[name]) img.src = this._mapIconUrl.replace("{name}", encodeURIComponent(name));
    return img;
  },
};
