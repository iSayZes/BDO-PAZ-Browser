from __future__ import annotations

import json
import threading
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING, Any

import webview

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from paz.bdo_thumbnail_cache import ThumbnailCache
from table_sort import TableSort

from updates.releases import Release

from .bdo_recent_tables import RecentTables
from .bdo_records_prefill import RecordsPrefill
from .bdo_records_store import DataDigests, RecordStore


class ApiState:
    """State and small helpers that `Api` and its mixins share.

    The mixins inherit this so every attribute they touch is declared in one
    place with its type.
    """

    def __init__(self, profile: bool = False, server: Any | None = None) -> None:
        self._profile = profile
        self._server = server
        self._window: webview.Window | None = None
        # The newer release the last update check found (`UpdateMixin`).
        self._app_update: Release | None = None
        # Held while a handler pack check or install runs (`HandlerUpdateMixin`).
        self._handler_update_lock = threading.Lock()
        self._paz_root: Path | None = None
        # The loaded folder's cache folder (`app_dirs.client_cache_dir`).
        self._cache_dir: Path | None = None
        self._entries: list[PazEntry] = []
        self._entry_map: dict[str, PazEntry] = {}
        # `fold_entry_map(_entry_map)`, for `_entry_ignoring_case()`.
        self._entry_map_folded: dict[str, PazEntry] = {}
        self._icon_entry_cache: dict[str, PazEntry | None] = {}
        self._icon_data_url_cache: dict[str, str] = {}
        self._icon_decode_lock = threading.Lock()
        self._icon_preview_lock = threading.Lock()
        # norm path -> (decoded image, preview data URL), oldest first.
        self._icon_preview_images: dict[str, tuple[Any, str]] = {}
        self._thumbnail_cache: ThumbnailCache | None = None
        self._tree_data: dict = {}
        # "Show only handled tables": the tree, file search, global search
        # and extraction see only the entries a binary handler reads.
        self._handled_only = False
        # (handled entries, their tree), built on first use per folder load.
        self._handled_view: tuple[list[PazEntry], dict] | None = None
        self._disk_companions: dict[str, bytes] = {}
        # The last status pushed, as setStatus() takes it, for a page that reloads.
        self._status: dict = {"key": "status.openFolder"}
        self._cached_path: str | None = None
        self._cached_data: bytes | None = None
        self._cached_handler: PreviewHandler | None = None
        self._cached_entry: PazEntry | None = None
        self._cached_companions: dict[str, bytes] = {}
        self._cached_sort: TableSort | None = None
        # Handlers whose parsed tables stay in memory (`api/bdo_recent_tables.py`).
        self._recent_tables = RecentTables()
        self._global_search_cancel: threading.Event = threading.Event()
        self._meta_version: int | None = None
        # The status `load_folder()` returned, shown again after the cache pass.
        self._folder_status: dict | None = None
        # Archive file name -> (CRC, size) from the meta file, for cache keys.
        self._archive_ids: dict[str, tuple[int, int]] = {}
        self._data_digests = DataDigests()
        self._records_store: RecordStore | None = None
        self._records_prefill: RecordsPrefill | None = None
        # When the UI last asked for something, and how many long tasks
        # (extraction, global search) run; the background fill waits for both.
        self._last_activity = 0.0
        self._busy_tasks = 0
        self._busy_lock = threading.Lock()
        # A GUI folder load shows the tree before LOC and the lookup indexes
        # are in; set while no load is between the two (`_load_entries`).
        self._folder_text_ready = threading.Event()
        self._folder_text_ready.set()
        self._folder_load_lock = threading.Lock()

    def _wait_for_folder_text(self) -> None:
        """Block until the loaded folder's LOC and lookup indexes are in.

        For the calls that render game text: run before them, a table would
        show (and cache) its Korean text and miss its icons. A no-op except
        for the second or two after a folder load shows the tree. pywebview
        runs every call on its own thread, so the window stays responsive.
        """
        self._folder_text_ready.wait()

    def _entry_ignoring_case(self, path: str) -> PazEntry | None:
        """The entry at the normalised `path` in any letter case, or None."""
        folded = path.lower()
        return self._entry_map.get(folded) or self._entry_map_folded.get(folded)

    def _mark_activity(self) -> None:
        self._last_activity = time.monotonic()

    @contextmanager
    def _busy(self) -> Iterator[None]:
        """Mark a long task, so background work waits until it ends."""
        with self._busy_lock:
            self._busy_tasks += 1
        try:
            yield
        finally:
            with self._busy_lock:
                self._busy_tasks -= 1
            self._mark_activity()

    def _ts(self) -> float:
        return time.perf_counter() if self._profile else 0.0

    def _te(self, profile: dict, key: str, start: float) -> None:
        if self._profile:
            profile[key] = (time.perf_counter() - start) * 1000

    def _push_js(self, js: str) -> None:
        if self._window is not None:
            try:
                self._window.evaluate_js(js)
            except Exception:
                pass

    def _push_status(self, msg: str | dict, progress: tuple[int, int] | None = None) -> None:
        data: dict = msg if isinstance(msg, dict) else {"message": msg}
        self._status = dict(data)
        data["progress"] = list(progress) if progress else None
        self._push_js(f"app.setStatus({json.dumps(data)})")

    if TYPE_CHECKING:
        # Implemented on Api; declared here so the mixins can call them.
        def read_entry(self, internal_path: str) -> bytes: ...

        def get_entry(self, internal_path: str) -> PazEntry | None: ...

        def stream_url(self, internal_path: str) -> str: ...

        def _visible_entries(self) -> list[PazEntry]: ...

        def _load_companions_parallel(
            self, handler: PreviewHandler, entry: PazEntry
        ) -> dict[str, bytes]: ...
