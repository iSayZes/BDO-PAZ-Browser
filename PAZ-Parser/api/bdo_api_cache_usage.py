"""The caches as the settings tabs list them: size and Delete per cache, Delete all, other clients.

`CACHE_KINDS` is the table of a client's caches. Each kind names the
settings tab that lists it, its files and folders in the cache folder, and
the hooks that release them before a delete and open them again after. A new
view adds its cache as one more kind.

"Delete all caches" deletes every kind with `in_delete_all`. The PAZ index is
left out of it: rebuilding it reads every archive header again, over a minute,
and only a patch makes it stale. It has a Delete of its own.

The cache folders of other PAZ folders in the Data Folder are listed too,
with the PAZ folder their marker names, so the caches of an uninstalled test
client can go.
"""

from __future__ import annotations

import shutil
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path

from app_dirs import (
    cache_root,
    client_cache_folders,
    client_paz_folder,
    data_dir,
    disk_bytes,
    is_same_folder,
    remove_client_cache,
)
from paz import bdo_cache, bdo_index_cache, bdo_records_cache, bdo_thumbnail_cache
from ui_text import ui_text
from world_map_build import MAP_FOLDER

from .bdo_api_caches import CACHE_FILES, CacheMixin

# An API call that releases or reopens a cache's files.
CacheHook = Callable[["CacheUsageMixin"], None]


@dataclass(frozen=True)
class CacheKind:
    """One cache of a client's cache folder."""

    # Key of the settings strings `settings.caches.<id>` and `delete_cache()`.
    id: str
    # The settings tab that lists it: "general" or a view's tab.
    tab: str
    files: tuple[str, ...] = ()
    folders: tuple[str, ...] = ()
    in_delete_all: bool = True
    # Run before the files are deleted, so nothing holds them open.
    close: CacheHook | None = None
    # Run after, so the loaded folder carries on with an empty cache.
    reopen: CacheHook | None = None

    def paths(self, cache_dir: Path) -> list[Path]:
        return [cache_dir / name for name in (*self.files, *self.folders)]


CACHE_KINDS = (
    # The entries in memory stay; the next start parses the meta file again.
    CacheKind("pazIndex", "general", files=(bdo_cache.CACHE_FILE,), in_delete_all=False),
    # Every view reads the lookup indexes; they are built on the next start.
    CacheKind("indexes", "general", files=(bdo_index_cache.CACHE_FILE,)),
    CacheKind(
        "thumbnails",
        "general",
        files=(bdo_thumbnail_cache.CACHE_FILE,),
        close=lambda api: api._close_thumbnail_cache(),
        reopen=lambda api: api._open_thumbnail_cache(),
    ),
    CacheKind(
        "records",
        "files",
        files=(bdo_records_cache.CACHE_FILE,),
        close=lambda api: api._close_records_cache(),
        # The "all" mode's background pass waits for the next start, so a
        # delete is not undone straight away; opened tables are still cached.
        reopen=lambda api: api._open_records_cache(fill=False),
    ),
    # The Map view shows its build prompt again.
    CacheKind("map", "map", folders=(MAP_FOLDER,), close=lambda api: api._release_world_map()),
)
_KINDS_BY_ID = {kind.id: kind for kind in CACHE_KINDS}


class CacheUsageMixin(CacheMixin):
    """Cache sizes and deletes for the settings."""

    def get_cache_usage(self) -> dict:
        """The loaded folder's caches with their size, and the other clients' cache folders.

        `caches` is empty while no folder is loaded.
        """
        caches = []
        if self._cache_dir is not None:
            caches = [
                {
                    "id": kind.id,
                    "tab": kind.tab,
                    "bytes": _kind_bytes(self._cache_dir, kind),
                    "in_delete_all": kind.in_delete_all,
                }
                for kind in CACHE_KINDS
            ]
        return {"caches": caches, "other_clients": self._other_clients()}

    def delete_cache(self, cache_id: str) -> dict:
        """Delete one cache of the loaded folder; what is loaded stays loaded."""
        kind = _KINDS_BY_ID.get(cache_id)
        if kind is None:
            return {"ok": False, "error": ui_text("errors.unknownCache", id=cache_id)}
        return self._delete_kinds((kind,))

    def delete_caches(self) -> dict:
        """Delete every cache of the loaded folder in the Delete all set."""
        return self._delete_kinds(kind for kind in CACHE_KINDS if kind.in_delete_all)

    def delete_other_client_cache(self, client_id: str) -> dict:
        """Delete the cache folder `client_id` of another PAZ folder in the Data Folder."""
        folder = self._other_client_folder(client_id)
        if folder is None:
            return {"ok": False, "error": ui_text("errors.unknownCache", id=client_id)}
        before = disk_bytes(folder)
        errors = remove_client_cache(folder, CACHE_FILES, (MAP_FOLDER,))
        return _delete_result(before - disk_bytes(folder), errors)

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _delete_kinds(self, kinds: Iterable[CacheKind]) -> dict:
        """Close, delete and reopen `kinds`, as `CacheKind` describes."""
        self._wait_for_folder_text()
        cache_dir = self._cache_dir
        if cache_dir is None:
            return {"ok": False, "error": ui_text("errors.noFolderLoaded")}

        kinds = tuple(kinds)
        was_filling = self._records_prefill is not None
        before = sum(_kind_bytes(cache_dir, kind) for kind in kinds)
        for kind in kinds:
            if kind.close is not None:
                kind.close(self)
        errors = [error for kind in kinds for error in _delete_paths(kind.paths(cache_dir))]
        # Before the reopen, which starts new, empty files.
        freed = before - sum(_kind_bytes(cache_dir, kind) for kind in kinds)
        for kind in kinds:
            if kind.reopen is not None:
                kind.reopen(self)
        if was_filling and self._records_prefill is None:
            # The stopped pass leaves its last progress on the status line.
            self._show_folder_status()
        return _delete_result(freed, errors)

    def _other_client_folders(self) -> list[Path]:
        """The client cache folders in the Data Folder but the loaded one's."""
        folders = client_cache_folders(cache_root(data_dir()))
        if self._cache_dir is None:
            return folders
        return [folder for folder in folders if not is_same_folder(folder, self._cache_dir)]

    def _other_client_folder(self, client_id: str) -> Path | None:
        return next((folder for folder in self._other_client_folders() if folder.name == client_id), None)

    def _other_clients(self) -> list[dict]:
        clients = []
        for folder in self._other_client_folders():
            paz_folder = client_paz_folder(folder)
            clients.append({
                "id": folder.name,
                "folder": "" if paz_folder is None else str(paz_folder),
                "exists": paz_folder is not None and paz_folder.is_dir(),
                "bytes": disk_bytes(folder),
            })
        return sorted(clients, key=lambda client: client["folder"].lower())


def _kind_bytes(cache_dir: Path, kind: CacheKind) -> int:
    return sum(disk_bytes(path) for path in kind.paths(cache_dir))


def _delete_paths(paths: Iterable[Path]) -> list[str]:
    """Delete each file or folder; one message per one that could not go."""
    errors: list[str] = []
    for path in paths:
        try:
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink(missing_ok=True)
        except OSError as ex:
            errors.append(f"{path.name}: {ex}")
    return errors


def _delete_result(freed: int, errors: list[str]) -> dict:
    if errors:
        return {"ok": False, "freed": freed, "error": "; ".join(errors)}
    return {"ok": True, "freed": freed}
