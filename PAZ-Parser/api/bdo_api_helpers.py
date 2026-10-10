from __future__ import annotations

import fnmatch
from collections.abc import Callable

from bdo_models import PazEntry

_DISK_VIRTUAL_PREFIX = "__disk__"

# Icon names of the UI sprite (ui/js/core/icons.js) by file extension.
_ICON_MAP: dict[str, str] = {
    ".dds": "image", ".png": "image", ".jpg": "image", ".jpeg": "image", ".bmp": "image", ".tga": "image",
    ".xml": "code", ".json": "code", ".yaml": "code", ".yml": "code",
    ".htm": "code", ".html": "code", ".lua": "code",
    ".txt": "text", ".log": "text", ".csv": "text", ".ini": "text", ".cfg": "text",
    ".webm": "video",
    ".pac": "archive", ".bss": "parsed", ".dbss": "parsed",
    ".loc": "loc",
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


def _file_icon(ext: str) -> str:
    return _ICON_MAP.get(ext.lower(), "file")


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
