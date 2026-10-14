"use strict";

// The views of the toolbar rail. Each view lists the panes it shows: parts of
// #main and the bottom bar's extract row, which only Files uses; switching
// hides every other pane. The toolbar and the bottom bar's status row stay.
// `onShow` names the method that fills the view when it opens, `settingsTab`
// the Settings tab with the view's settings (#settings-tab-<id> in index.html).
const VIEWS = {
  files: { panes: ["sidebar", "v-divider", "right-panel", "extract-row"], settingsTab: "files" },
  map: { panes: ["map-view"], onShow: "_showMapView", settingsTab: "map" },
};

const ALL_PANES = [...new Set(Object.values(VIEWS).flatMap((view) => view.panes))];

// The Settings tabs: General, then one per view that has settings. A view
// that is not in VIEWS yet, a disabled rail button, has no tab.
export const SETTINGS_TABS = ["general", ...Object.values(VIEWS).flatMap((view) => view.settingsTab ?? [])];

export const viewMethods = {
  switchView(id) {
    const view = VIEWS[id];
    if (!view || id === this._activeView) return;
    this._activeView = id;

    ALL_PANES.forEach((pane) => {
      document.getElementById(pane).hidden = !view.panes.includes(pane);
    });
    document.querySelectorAll("#view-rail .view-tab[data-view]").forEach((tab) => {
      const isActive = tab.dataset.view === id;
      tab.classList.toggle("active", isActive);
      if (isActive) tab.setAttribute("aria-current", "page");
      else tab.removeAttribute("aria-current");
    });
    if (view.onShow) this[view.onShow]();
  },

  _isFilesView() {
    return this._activeView === "files";
  },
};
