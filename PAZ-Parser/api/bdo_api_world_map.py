"""The Map view's tiles and pin icons: built once per client into the cache folder (WorldMapMixin).

The first open shows a prompt with the tile count and an estimated size; its
OK turns on the "Keep map updated" setting and starts the build. With the
setting on, a folder load whose client has no finished map (a patch) builds
it in the background. A build runs in its own thread, which drives the
process pool of `world_map_build.py` and pushes progress to the page, then
cuts the pin icons into the same folder (`map_icons_build.py`).
"""

from __future__ import annotations

import json
import logging
import shutil
import threading
import time
from pathlib import Path

from bdo_models import PazEntry
from map_icons_build import build_icons, read_icon_index
from map_nodes import map_nodes
from world_map import (
    AVERAGE_TILE_BYTES,
    MAX_ZOOM,
    MIN_ZOOM,
    Sector,
    find_sectors,
    pyramid,
    tile_count,
    visible_sectors,
)
from world_map_build import (
    BuildProgress,
    BuildStopped,
    RadarSource,
    build_map,
    map_root,
    read_manifest,
    read_radar,
    remove_other_maps,
    version_folder,
    worker_count,
)

from .bdo_api_helpers import _norm
from .bdo_api_state import ApiState
from .bdo_config import MAP_FILTERS_KEY, keep_map_updated_setting, load_config, map_filters_setting, save_config

# Progress pushes to the page at most this often, plus the first and last tile of a zoom.
_PROGRESS_INTERVAL_S = 0.2
# The page zooms in past the tiles' own scale by stretching them.
_EXTRA_ZOOM = 2


class WorldMapMixin(ApiState):
    def get_world_map(self) -> dict:
        """The Map view's state; see `_map_state()`."""
        self._mark_activity()
        with self._map_lock:
            return self._map_state()

    def get_map_icons(self) -> dict[str, dict]:
        """Icon name -> {"size", "anchor", "turns"} of the loaded client's pin icons; the files are at "iconUrl".

        Built with the map; a map built before the icons, or in an older
        icon format, gets them here. Empty while there is no finished map.
        """
        self._mark_activity()
        with self._map_lock:
            if self._cache_dir is None or self._meta_version is None or not self._is_map_current():
                return {}
            folder = version_folder(self._cache_dir, self._meta_version)
            index = read_icon_index(folder)
            return index if index is not None else self._build_map_icons(folder)

    def get_map_filters(self) -> dict:
        """The Filters panel's saved choices (`bdo_config.map_filters_setting`)."""
        return map_filters_setting(load_config())

    def save_map_filters(self, filters: object) -> dict:
        """Save the Filters panel's choices in the config; returns what was saved.

        Checked like a load, so the page cannot store anything but the panel's shape.
        """
        cleaned = map_filters_setting({MAP_FILTERS_KEY: filters})
        save_config({MAP_FILTERS_KEY: cleaned})
        return cleaned

    def get_map_nodes(self) -> list[dict]:
        """Every worldmap node with its name in the loaded language, kind icon and position (`map_nodes.py`)."""
        self._mark_activity()
        # The names need LOC, the nodes the lookup indexes.
        self._wait_for_folder_text()
        return [node.to_dict() for node in map_nodes()]

    def build_world_map(self) -> dict:
        """The prompt's OK: turn on "Keep map updated", start the build, return the new state."""
        self._mark_activity()
        save_config({"keep_map_updated": True})
        self._start_map_build()
        with self._map_lock:
            return self._map_state()

    # ── State ────────────────────────────────────────────────────────────────

    def _map_state(self) -> dict:
        """What the Map view shows; call with `_map_lock` held.

        {"state": "noFolder" | "noTiles"}, {"state": "building", "progress"},
        {"state": "ready", "tileUrl", "bounds", "minZoom", "maxZoom",
        "nativeZoom"}, or {"state": "prompt", "tiles", "bytes", "error"} where
        "error" is the message of a failed build or None. "iconUrl" is the
        URL template of the pin icons (`get_map_icons`), `{name}` for a name.
        """
        if self._cache_dir is None or self._meta_version is None:
            return {"state": "noFolder"}
        if self._map_stop is not None:
            progress = self._map_progress
            return {"state": "building", "progress": progress.to_dict() if progress else None}

        folder = version_folder(self._cache_dir, self._meta_version)
        manifest = read_manifest(folder)
        if manifest is not None and manifest.is_current(self._meta_version):
            if self._server is None:
                return {"state": "prompt", "tiles": 0, "bytes": 0, "error": "Local server not available"}
            return {
                "state": "ready",
                "tileUrl": self._server.serve_map(folder, self._meta_version),
                "iconUrl": self._server.map_icon_url(self._meta_version),
                "bounds": manifest.bounds.to_dict(),
                "minZoom": MIN_ZOOM,
                "maxZoom": MAX_ZOOM + _EXTRA_ZOOM,
                "nativeZoom": MAX_ZOOM,
            }

        sectors = self._radar_sectors()
        if not sectors:
            return {"state": "noTiles"}
        tiles = tile_count(pyramid(sectors))
        return {"state": "prompt", "tiles": tiles, "bytes": tiles * AVERAGE_TILE_BYTES, "error": self._map_error}

    def _radar_sectors(self) -> dict[Sector, PazEntry]:
        """Sector -> radar image entry of the loaded folder, hidden sectors left out; found once per folder."""
        if self._map_sectors is None:
            paths = visible_sectors(find_sectors(_norm(entry.internal_path) for entry in self._entries))
            self._map_sectors = {
                sector: entry for sector, path in paths.items() if (entry := self.get_entry(path)) is not None
            }
        return self._map_sectors

    def _is_map_current(self) -> bool:
        if self._cache_dir is None or self._meta_version is None:
            return False
        manifest = read_manifest(version_folder(self._cache_dir, self._meta_version))
        return manifest is not None and manifest.is_current(self._meta_version)

    # ── Building ─────────────────────────────────────────────────────────────

    def _keep_map_updated(self) -> None:
        """After a GUI folder load: build the map when the setting is on and it is missing or old."""
        if keep_map_updated_setting(load_config()):
            self._start_map_build()

    def _start_map_build(self) -> None:
        """Start a build in the background unless one runs, the map is current or there are no tiles."""
        with self._map_lock:
            if self._map_stop is not None or self._is_map_current():
                return
            sectors = self._radar_sectors()
            if not sectors or self._paz_root is None or self._cache_dir is None or self._meta_version is None:
                return
            sources: dict[Sector, RadarSource] = {
                sector: (self._paz_root / entry.archive_name, entry) for sector, entry in sectors.items()
            }
            stop = threading.Event()
            self._map_stop = stop
            self._map_progress = None
            self._map_error = None
            args = (sources, self._cache_dir, self._meta_version, stop)
            threading.Thread(target=self._run_map_build, args=args, daemon=True).start()
            state = self._map_state()
        self._push_js(f"app.onMapStateChanged({json.dumps(state)})")

    def _run_map_build(
        self, sources: dict[Sector, RadarSource], cache_dir: Path, version: int, stop: threading.Event
    ) -> None:
        target = version_folder(cache_dir, version)
        error: str | None = None
        was_stopped = False
        try:
            # Busy: the parsed table background fill waits for the build.
            with self._busy():
                build_map(
                    sectors=sources,
                    read=read_radar,
                    target=target,
                    version=version,
                    workers=worker_count(),
                    on_progress=self._progress_pusher(stop),
                    should_stop=stop.is_set,
                )
                # Read from the loaded folder: a folder load stops the build first.
                if not stop.is_set():
                    self._build_map_icons(target)
            remove_other_maps(cache_dir, keep=target)
        except BuildStopped:
            was_stopped = True
        except Exception as ex:
            logging.warning("Could not build the world map", exc_info=True)
            error = str(ex) or type(ex).__name__

        with self._map_lock:
            if self._map_stop is not stop:
                return  # A folder load or "Delete all caches" ended this build.
            self._map_stop = None
            self._map_error = error
            state = self._map_state()
        if not was_stopped:
            self._push_js(f"app.onMapStateChanged({json.dumps(state)})")

    def _build_map_icons(self, folder: Path) -> dict[str, dict]:
        """Cut the pin icons into the map `folder`; returns their index, empty when they fail.

        Not fatal: without icons the pins are dots and arrows.
        """
        try:
            return build_icons(self._read_any_case, folder)
        except Exception:
            logging.warning("Could not build the map pin icons in %s", folder, exc_info=True)
            return {}

    def _progress_pusher(self, stop: threading.Event):
        last_push = 0.0

        def on_progress(progress: BuildProgress) -> None:
            nonlocal last_push
            if self._map_stop is not stop:
                return
            self._map_progress = progress
            now = time.monotonic()
            if progress.done in (0, progress.total) or now - last_push >= _PROGRESS_INTERVAL_S:
                last_push = now
                self._push_js(f"app.onMapBuildProgress({json.dumps(progress.to_dict())})")

        return on_progress

    def _stop_map_build(self) -> None:
        """Stop a running build; it leaves nothing in place. Returns at once."""
        with self._map_lock:
            if self._map_stop is not None:
                self._map_stop.set()
            self._map_stop = None
            self._map_progress = None

    # ── Folder and cache changes ─────────────────────────────────────────────

    def _clear_world_map(self) -> None:
        """A new folder: stop the old folder's build and forget its radar images."""
        self._stop_map_build()
        with self._map_lock:
            self._map_sectors = None
            self._map_error = None
        if self._server is not None:
            self._server.serve_map(None, 0)

    def _world_map_bytes(self) -> int:
        """Bytes the finished maps of the loaded folder's cache take."""
        if self._cache_dir is None:
            return 0
        root = map_root(self._cache_dir)
        if not root.is_dir():
            return 0
        manifests = (read_manifest(folder) for folder in root.iterdir() if folder.is_dir())
        return sum(manifest.bytes for manifest in manifests if manifest is not None)

    def _delete_world_map(self) -> tuple[int, list[str]]:
        """Stop a build and delete every map of the loaded folder: (bytes freed, error messages)."""
        if self._cache_dir is None:
            return 0, []
        freed = self._world_map_bytes()
        self._stop_map_build()
        if self._server is not None:
            self._server.serve_map(None, 0)
        errors: list[str] = []

        def on_error(_function, path, ex) -> None:
            errors.append(f"{Path(path).name}: {ex}")

        root = map_root(self._cache_dir)
        if root.is_dir():
            shutil.rmtree(root, onexc=on_error)
        return (0 if errors else freed), errors[:1]
