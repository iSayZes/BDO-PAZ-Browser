"""The disk caches: their folder and the parsed records cache.

Each PAZ folder has its own cache folder in the Data Folder's `cache` folder
(`app_dirs.py`). Changing the "Data Folder" setting copies the config over,
deletes the caches in the old folder and starts the loaded folder's caches in
the new one.

The "Parsed table cache" setting picks how records are cached:

- `off`: every open parses, nothing is written
- `open`: a table's records are saved the first time it is parsed (default)
- `all`: as `open`, plus a background pass that parses every table A to Z
  while the app is idle (`api/bdo_records_prefill.py`)

Sizes and deleting per cache, as the settings tabs list them, are in
`api/bdo_api_cache_usage.py`.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path

from bdo_models import MetaFile, PazEntry
from app_dirs import (
    cache_root,
    client_cache_dir,
    copy_user_files,
    data_dir,
    default_data_dir,
    move_out_of_game_folder,
    remove_cache_root,
    set_picked_data_dir,
)
from bdo_preview import PreviewHandler, get_handler, has_parsed_view, parsed_handlers, set_records_source
# The handlers folder the entry point put on the path (bdo_preview.use_handlers_dir).
from _common.loc import init_loc
from paz import bdo_cache, bdo_index_cache, bdo_records_cache, bdo_thumbnail_cache
from paz.bdo_cache import CachedEntries, save_cache
from paz.bdo_payload_reader import read_entry_payload
from paz.bdo_records_cache import RecordsCache
from paz.bdo_thumbnail_cache import ThumbnailCache
from table_sort import TableSort
from world_map_build import MAP_FOLDER

from .bdo_api_state import ApiState
from .bdo_config import load_config, peek_table_sort, records_cache_setting, table_sort_file_key
from .bdo_records_prefill import PrefillProgress, RecordsPrefill, Target
from .bdo_records_store import RecordStore, paz_entry_identity
from .bdo_tree import handled_entries

# The background fill starts a table only after the UI was quiet this long.
_IDLE_AFTER_S = 2.0


# Every file of a client's cache folder; the world map is its `MAP_FOLDER`.
CACHE_FILES = (
    bdo_cache.CACHE_FILE,
    bdo_index_cache.CACHE_FILE,
    bdo_thumbnail_cache.CACHE_FILE,
    bdo_records_cache.CACHE_FILE,
)


class CacheMixin(ApiState):
    """Cache folder, records and thumbnail cache lifecycle, the shared data digests."""

    # ── Inputs of the cache keys ─────────────────────────────────────────────

    def _set_archive_ids(self, meta: MetaFile) -> None:
        self._archive_ids = {
            f"pad{table.paz_file_id:05d}.paz": (table.crc, table.size) for table in meta.paz_files
        }

    def _paz_identity(self, entry: PazEntry) -> str | None:
        """`paz_entry_identity` of an entry read from a PAZ archive, else None."""
        archive = self._archive_ids.get(entry.archive_name.lower())
        return None if archive is None else paz_entry_identity(entry, *archive)

    def _install_loc(self, raw: bytes | None) -> None:
        """Install LOC text, or none, and record its digest for the records cache.

        When the text changed, the tables in memory were built with the old
        one, so every handler drops them.
        """
        generation = self._data_digests.generation
        init_loc(raw)
        self._data_digests.set_loc(raw)
        if self._data_digests.generation != generation:
            self._recent_tables.clear()

    # ── Cache folder ─────────────────────────────────────────────────────────

    def _open_cache_dir(self, paz_root: Path) -> None:
        """Point the caches at the cache folder of `paz_root`, moving old ones out of the game folder.

        A Data Folder whose cache folder cannot be created, such as a
        read-only one, falls back to the default for this session.
        """
        try:
            cache_dir = client_cache_dir(cache_root(data_dir()), paz_root)
        except OSError:
            logging.warning("Cannot use the Data Folder for caches, using the default one", exc_info=True)
            cache_dir = client_cache_dir(cache_root(default_data_dir()), paz_root)
        move_out_of_game_folder(paz_root, cache_dir, CACHE_FILES, (bdo_index_cache.LEGACY_CACHE_FILE,))
        self._cache_dir = cache_dir

    def _move_data_dir(self, old: Path, new: Path) -> list[str]:
        """Switch the Data Folder from `old` to `new`: copy the config and saved pins, delete `old`'s caches.

        The config and saved map pins are copied over any already in `new`;
        the ones in `old` stay. Raises OSError, before anything changed, when
        they cannot be copied.

        The loaded folder's entry list is saved again from memory, so the next
        start skips the minute-long index rebuild. The thumbnail and records
        caches start empty (the "all" mode fills the records again) and the
        lookup indexes are built on the next start. Other clients' caches in
        `old` are deleted too and rebuilt when their folder loads. Returns one
        message per old cache file that could not be deleted.
        """
        copy_user_files(old, new)
        set_picked_data_dir(new)
        self._close_records_cache()
        self._close_thumbnail_cache()
        self._stop_map_build()
        errors = remove_cache_root(cache_root(old), CACHE_FILES, (MAP_FOLDER,))
        self._cache_dir = None
        if self._paz_root is None or self._meta_version is None:
            return errors

        self._open_cache_dir(self._paz_root)
        assert self._cache_dir is not None
        try:
            save_cache(self._cache_dir, CachedEntries(self._meta_version, self._archive_files, self._entries))
        except OSError:
            # Not fatal: the next start parses the meta file again.
            logging.warning("Could not write the PAZ index cache in %s", self._cache_dir, exc_info=True)
        self._open_thumbnail_cache()
        self._open_records_cache()
        return errors

    def _open_thumbnail_cache(self) -> None:
        """Open the loaded folder's thumbnail cache; none before its PAZ index is in."""
        self._close_thumbnail_cache()
        if self._cache_dir is not None and self._meta_version is not None:
            self._thumbnail_cache = ThumbnailCache(self._cache_dir, self._meta_version)

    def _close_thumbnail_cache(self) -> None:
        if self._thumbnail_cache is not None:
            self._thumbnail_cache.close()
            self._thumbnail_cache = None

    # ── Records cache lifecycle ──────────────────────────────────────────────

    def _open_records_cache(self, *, fill: bool = True) -> None:
        """Install the records cache for the loaded folder, as the setting asks.

        `fill=False` skips the background pass of the "all" mode for this
        session; tables opened from then on are still cached.
        """
        self._close_records_cache()
        mode = records_cache_setting(load_config())
        if mode == "off" or self._cache_dir is None:
            return

        store = RecordStore(
            RecordsCache(self._cache_dir),
            self._data_digests,
            self._paz_identity,
            self.get_entry,
        )
        store.prepare(parsed_handlers())
        self._records_store = store
        set_records_source(store)
        if mode == "all" and fill:
            self._records_prefill = RecordsPrefill(
                store,
                self._prefill_targets,
                self._read_table,
                self._opening_sort,
                self._is_idle,
                self._report_prefill,
                self._show_folder_status,
            )
            self._records_prefill.start()

    def _close_records_cache(self) -> None:
        set_records_source(None)
        if self._records_prefill is not None:
            self._records_prefill.stop()
            self._records_prefill = None
        if self._records_store is not None:
            self._records_store.close()
            self._records_store = None

    def _refresh_records_cache(self) -> None:
        """After handlers or shared data changed: fingerprint new handlers, rerun the fill."""
        if self._records_store is not None:
            self._records_store.prepare(parsed_handlers())
        if self._records_prefill is not None:
            self._records_prefill.start()

    # ── Background fill ──────────────────────────────────────────────────────

    def _is_idle(self) -> bool:
        return self._busy_tasks == 0 and time.monotonic() - self._last_activity >= _IDLE_AFTER_S

    def _prefill_targets(self) -> list[Target]:
        targets: list[Target] = []
        for entry in handled_entries(self._entries):
            path = Path(entry.internal_path)
            handler = get_handler(path.name, path.suffix)
            if has_parsed_view(handler):
                targets.append((handler, entry))
        return targets

    def _read_table(self, handler: PreviewHandler, entry: PazEntry) -> tuple[bytes, dict[str, bytes]]:
        """A table and its companions, read past the payload cache.

        The fill reads every table once; through the LRU payload cache it
        would push out the payloads of the tables the user has open.
        """
        if self._paz_root is None:
            raise FileNotFoundError(entry.internal_path)
        data = read_entry_payload(self._paz_root / entry.archive_name, entry)
        companions = dict(self._disk_companions)
        for path in handler.companions(entry):
            companion = self.get_entry(path)
            if companion is None:
                continue
            try:
                companions[Path(path).name] = read_entry_payload(self._paz_root / companion.archive_name, companion)
            except Exception:
                # As in the app: a companion that cannot be read is left out.
                logging.warning("Background fill could not read companion %s", path, exc_info=True)
        return data, companions

    @staticmethod
    def _opening_sort(handler: PreviewHandler, entry: PazEntry) -> TableSort | None:
        """The sort the table opens with, as `load_entry()` picks it."""
        saved = peek_table_sort(table_sort_file_key(entry.internal_path), handler.sortable_fields())
        return saved or handler.default_sort()

    def _report_prefill(self, progress: PrefillProgress) -> None:
        counts = {"done": f"{progress.done:,}", "total": f"{progress.total:,}"}
        if progress.paused:
            message = {"key": "status.cachingTablesPaused", "args": counts}
        else:
            name = progress.path.replace("\\", "/").rsplit("/", 1)[-1]
            message = {"key": "status.cachingTables", "args": {**counts, "name": name}}
        self._push_status(message, (progress.done, progress.total))

    def _show_folder_status(self) -> None:
        """Put the folder's load message back once the pass no longer needs the line."""
        if self._folder_status is not None:
            self._push_status(dict(self._folder_status))
