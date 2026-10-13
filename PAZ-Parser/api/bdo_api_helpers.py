from __future__ import annotations

import fnmatch
from collections.abc import Callable
from typing import NamedTuple

from bdo_models import PazEntry
from bdo_preview import has_preview, is_handled_file

_DISK_VIRTUAL_PREFIX = "__disk__"

# Icon names of the UI sprite (ui/js/core/icons.js) by file extension, for
# files no handler reads (_file_icon()). Covers every built-in view's extension
# (bdo_preview._REGISTRY), so a file with a preview never gets the plain icon.
_ICON_MAP: dict[str, str] = {
    ".dds": "image", ".dds1": "image", ".dds11": "image", ".png": "image", ".jpg": "image",
    ".bmp": "image", ".gif": "image", ".tga": "image", ".tif": "image", ".svg": "image",
    ".xml": "code", ".json": "code", ".yaml": "code", ".yml": "code",
    ".htm": "code", ".html": "code", ".lua": "code", ".css": "code", ".js": "code", ".h": "code",
    # XML: NPC AI state machines (.ai), class combo lists (.cl, character/pcaiscript/)
    ".ai": "code", ".cl": "code", ".mxml": "code", ".xmp": "code", ".weathercolortablexml": "code",
    ".txt": "text", ".log": "text", ".csv": "text", ".ini": "text", ".cfg": "text",
    ".srt": "text", ".ifl": "text",
    ".pa": "text", ".pc": "text", ".ph": "text", ".pm": "text", ".pami": "text",
    ".webm": "video",
    ".pac": "archive",
}
FOLDER_ICON = "folder"


def _norm(path: str) -> str:
    return path.replace("\\", "/")


def fold_entry_map(entry_map: dict[str, PazEntry]) -> dict[str, PazEntry]:
    """Lowercased path -> entry, for the paths of `entry_map` not lowercase already.

    Nearly every client path is lowercase (all but 14 of 872,774 on client
    3458), so a full lowercase copy of the map would hold about 116 MB to
    find the few others.
    """
    return {path.lower(): entry for path, entry in entry_map.items() if not path.islower()}


def _file_icon(name: str) -> str:
    """The tree icon for file `name`: `loc` or `parsed` when a handler reads it,
    else by extension, `file` for a `.bss`/`.dbss` without a handler or an
    unknown kind."""
    ext = name[name.rfind("."):].lower() if "." in name else ""
    if ext == ".loc":
        return "loc"
    if is_handled_file(name):
        return "parsed"
    return _ICON_MAP.get(ext, "file")


def file_row_fields(name: str) -> dict[str, str | bool]:
    """The icon fields of a file row in the tree or a search: its `icon` name,
    and `supported`, True when the file has a preview other than the hex view."""
    return {"icon": _file_icon(name), "supported": has_preview(name)}


class FileSearchHits(NamedTuple):
    """Every match of one file search, kept while the page scrolls through them."""

    query: str
    # The entry list searched (`Api._visible_entries()`); another list means
    # a new folder, handler set or "Show only handled tables" setting.
    entries: list[PazEntry]
    paths: tuple[str, ...]


def folder_then_name(path: str) -> tuple[str, str]:
    """Sort key for a normalised PAZ path: its folder, then its file name,
    both ignoring case, so a folder's files stay together above its subfolders."""
    folder, _, name = path.lower().rpartition("/")
    return folder, name


def search_result(path: str) -> dict:
    """The file-search row for normalised PAZ path `path`."""
    name = path.rsplit("/", 1)[-1]
    return {"id": path, "name": name, "path": path, **file_row_fields(name)}


def path_matcher(pattern: str) -> Callable[[str], bool]:
    """Test a normalised PAZ path against a search pattern, case-insensitively.

    A glob (containing *, ? or [) matches the full path or the file name
    alone; plain text matches anywhere in the path.
    """
    q = _norm(pattern).lower()
    if any(c in q for c in ("*", "?", "[")):
        def is_glob_hit(path: str) -> bool:
            path_lc = path.lower()
            name_lc = path_lc.rsplit("/", 1)[-1]
            return fnmatch.fnmatch(path_lc, q) or fnmatch.fnmatch(name_lc, q)
        return is_glob_hit

    return lambda path: q in path.lower()
