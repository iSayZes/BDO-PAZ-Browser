"""Map pin icons as files: built into a client's map folder next to the tiles.

The map build (`api/bdo_api_world_map.py`) cuts the icons (`map_icons.py`)
after the tiles, into `<map folder>/icons/`: one `<name>.png` per icon at
RENDER_SCALE and `icons.json` with each icon's size, anchor and whether it
turns. The local server serves the PNGs; the page reads the index through
`get_map_icons()`. A map built before the icons, or with another
ICON_FORMAT, gets them on the Map view's first open.

The icons go with the map: "Keep map updated" builds them again after a
patch, and "Delete all caches" removes them with the tiles.
"""

from __future__ import annotations

import json
import logging
import shutil
from collections.abc import Callable
from pathlib import Path

from map_icons import ICON_NAMES, cut_icons

ICONS_FOLDER = "icons"
INDEX_NAME = "icons.json"
# Raise when LAYOUT_ICONS or the cutting changes, so built icons are cut again.
ICON_FORMAT = 1
_BUILDING_SUFFIX = ".building"


def icons_folder(map_folder: Path) -> Path:
    return map_folder / ICONS_FOLDER


def icon_file(map_folder: Path, name: str) -> Path | None:
    """The PNG of icon `name` in `map_folder`, or None for an unknown name or a missing file."""
    if name not in ICON_NAMES:
        return None
    path = icons_folder(map_folder) / f"{name}.png"
    return path if path.is_file() else None


def read_icon_index(map_folder: Path) -> dict[str, dict] | None:
    """Icon name -> {"size", "anchor", "turns"} of the built icons; None when not built in ICON_FORMAT."""
    path = icons_folder(map_folder) / INDEX_NAME
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, ValueError):
        logging.warning("Ignoring unreadable %s", path, exc_info=True)
        return None
    if not isinstance(data, dict) or data.get("format") != ICON_FORMAT or not isinstance(data.get("icons"), dict):
        return None
    return data["icons"]


def build_icons(read: Callable[[str], bytes | None], map_folder: Path) -> dict[str, dict]:
    """Cut every icon the client has into `map_folder`, replacing icons built before; returns the index.

    `read` returns a file of the PAZ archives by path in any letter case, or
    None. Written to a side folder first, so a failed build leaves the old
    icons. Raises OSError when the files cannot be written.
    """
    target = icons_folder(map_folder)
    building = target.with_name(target.name + _BUILDING_SUFFIX)
    shutil.rmtree(building, ignore_errors=True)
    building.mkdir(parents=True)
    index: dict[str, dict] = {}
    try:
        for name, icon in cut_icons(read).items():
            icon.image.save(building / f"{name}.png", format="PNG")
            index[name] = {"size": list(icon.size), "anchor": list(icon.anchor), "turns": icon.turns}
        (building / INDEX_NAME).write_text(json.dumps({"format": ICON_FORMAT, "icons": index}), encoding="utf-8")
        shutil.rmtree(target, ignore_errors=True)
        building.rename(target)
    except BaseException:
        shutil.rmtree(building, ignore_errors=True)
        raise
    return index
