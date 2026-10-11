"use strict";

import { t } from "../core/i18n.js";
import { countBy } from "./map-filters.js";

// The worldmap nodes on the Map view (map_nodes.py): each node's game icon at
// its waypoint, under the pins, with its name as tooltip, and the worldmap
// links between them. The Filters panel (map-filters.js) turns each kind on
// and off with a row of its Nodes card, and the links with its Links option.
// Main nodes show at every zoom, sub-nodes (farms, mines, ...) from
// SUB_NODE_MIN_ZOOM, so the whole-world view stays readable. A node search
// shows every match, whatever the filters and zoom. A link shows only while
// both its nodes do: blue when either end is a sea node, orange on land.

// Node icons are this many px tall at every zoom, centred on the node, so
// links meet in their middle.
const NODE_ICON_PX = 32;
const SUB_NODE_MIN_ZOOM = 6;
// The Links option's key in the Nodes card.
const LINKS_KEY = "links";
const LINK_STYLE = { weight: 2, opacity: 0.8, interactive: false };
const LAND_LINK_COLOR = "#e0a93a";
const SEA_LINK_COLOR = "#4a90d9";
// Panes under Leaflet's marker pane (z-index 600): pins over nodes over links.
const NODE_PANE = "map-nodes";
const NODE_PANE_Z_INDEX = 590;
const LINK_PANE = "map-node-links";
const LINK_PANE_Z_INDEX = 580;

export const mapNodeMethods = {
  // Called once per Leaflet map: the node and link layers and the zoom rule.
  _addMapNodeLayer(map) {
    map.createPane(NODE_PANE).style.zIndex = String(NODE_PANE_Z_INDEX);
    map.createPane(LINK_PANE).style.zIndex = String(LINK_PANE_Z_INDEX);
    // entries: {node, marker, name} per node, name lowercased for the search;
    // links: {line, a, b} per link, a and b the entries of its two nodes.
    this._mapNodes = {
      layer: L.layerGroup().addTo(map),
      linkLayer: L.layerGroup().addTo(map),
      entries: [],
      links: [],
    };
    map.on("zoomend", () => this._applyMapNodeFilter());
  },

  async _loadMapNodes() {
    let nodes = [];
    try {
      nodes = await window.pywebview.api.get_map_nodes();
    } catch {
      // The map works without its node layer.
    }
    if (this._mapNodes) this._setMapNodes(nodes);
  },

  _setMapNodes(nodes) {
    const { layer, linkLayer } = this._mapNodes;
    layer.clearLayers();
    linkLayer.clearLayers();
    const entries = nodes
      .filter((node) => this._mapIcons[node.icon])
      .map((node) => ({
        node,
        name: node.name.toLocaleLowerCase(),
        marker: L.marker(L.latLng(node.z, node.x), {
          icon: this._mapGameIcon(node.icon, this._mapIcons[node.icon], { height: NODE_ICON_PX, centered: true }),
          pane: NODE_PANE,
          keyboard: false,
        })
          // Leaflet sets a string tooltip as HTML.
          .bindTooltip(`${this._esc(node.name)} · ${this._esc(this._mapCoords(node.x, node.z))}`),
      }));
    const byKey = new Map(entries.map((entry) => [entry.node.key, entry]));
    this._mapNodes.entries = entries;
    this._mapNodes.links = entries.flatMap((a) =>
      a.node.links
        .map((key) => byKey.get(key))
        .filter(Boolean)
        .map((b) => ({
          a,
          b,
          line: L.polyline([L.latLng(a.node.z, a.node.x), L.latLng(b.node.z, b.node.x)], {
            ...LINK_STYLE,
            color: a.node.sea || b.node.sea ? SEA_LINK_COLOR : LAND_LINK_COLOR,
            pane: LINK_PANE,
          }),
        })),
    );
    this._applyMapNodeFilter();
  },

  // The Filters panel's Nodes rows: the kinds this client has, in the order
  // of the icon list (map_icons.py LAYOUT_ICONS), with their counts.
  _mapNodeFilterRows() {
    const counts = countBy(this._mapNodes?.entries.map((entry) => entry.node) ?? [], "icon");
    return Object.keys(this._mapIcons)
      .filter((kind) => counts.has(kind))
      .map((kind) => ({
        key: kind,
        label: t(`map.nodeKinds.${kind}`),
        count: counts.get(kind),
        icon: this._mapFilterIcon(kind),
      }));
  },

  // The Nodes card's options under its kinds: the links.
  _mapNodeFilterOptions() {
    return [
      {
        key: LINKS_KEY,
        label: t("map.filters.links"),
        count: this._mapNodes?.links.length ?? 0,
        icon: this._mapFilterSymbol("route"),
      },
    ];
  },

  // Whether the Filters panel lets `node` through: its kind's row.
  _isMapNodeFiltered(node) {
    return this._isMapFilterShown("nodes", node.icon);
  },

  // The Nodes card's "shown" count: the nodes the filters let through, at any zoom.
  _mapNodeShownCount() {
    return (this._mapNodes?.entries ?? []).filter(({ node }) => this._isMapNodeFiltered(node)).length;
  },

  // Adds and removes only the markers and links whose visibility changed.
  _applyMapNodeFilter() {
    if (!this._mapNodes || !this._leafletMap) return;
    const zoom = this._leafletMap.getZoom();
    const { search } = this._mapFilterState();
    const { layer, linkLayer, entries, links } = this._mapNodes;
    entries.forEach(({ node, name, marker }) => {
      const shown = search
        ? name.includes(search)
        : this._isMapNodeFiltered(node) && (!node.sub || zoom >= SUB_NODE_MIN_ZOOM);
      toggleLayer(layer, marker, shown);
    });
    const linksOn = this._isMapFilterShown("nodes", LINKS_KEY);
    links.forEach(({ a, b, line }) => {
      toggleLayer(linkLayer, line, linksOn && layer.hasLayer(a.marker) && layer.hasLayer(b.marker));
    });
  },
};

function toggleLayer(group, item, shown) {
  if (shown === group.hasLayer(item)) return;
  if (shown) group.addLayer(item);
  else group.removeLayer(item);
}
