"""Icon lookup by entity kind and ID.

Most icons cannot be derived from an ID. They live in dozens of per-category
folders, and thousands are named after a 3D asset with no numeric part at all
(`inhouse_cultivate_sea_clam_01_wall.dds`). The tables that own those entities
store the icon path inline, so the app builds an index per kind once per PAZ
folder and injects it here, the same way `loc.py` receives LOC data.

Each kind may also declare a derivation: the path its ID implies when the index
is unavailable or has no entry. Derivation alone reaches only ~15% of items, so
it is a fallback, never the primary source.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from enum import Enum
from pathlib import Path


class IconKind(Enum):
    """Entity kinds that have an icon index.

    Values double as disk-cache keys, so renaming one orphans its cached data.
    """

    ITEM = "item"
    QUEST = "quest"
    CHARACTER = "character"


ITEM_ICON_DIR = "ui_texture/icon/new_icon/product_icon_png"


def _derive_item_icon(item_id: int) -> str:
    return f"{ITEM_ICON_DIR}/{item_id:08d}.png"


# Fallback path templates, used only when the index has no entry. Kinds absent
# here have no derivation: quest and character icons are named after assets far
# more often than after their ID, so a guess would be wrong more than right.
_DERIVERS: dict[IconKind, Callable[[int], str]] = {
    IconKind.ITEM: _derive_item_icon,
}

# kind -> {entity_id: PAZ icon path}
_INDEXES: dict[IconKind, dict[int, str]] = {}

# Hand-curated fixes, checked into the repo rather than built from the PAZ.
# They win over the index, because they exist precisely to correct it.
OVERRIDES_FILE = Path(__file__).parent / "icon_overrides.json"

_OVERRIDES: dict[IconKind, dict[int, str]] | None = None
_OVERRIDE_ERROR: str = ""


def _read_overrides() -> dict[IconKind, dict[int, str]]:
    """Parse the override file. A bad file is reported, never fatal."""
    global _OVERRIDE_ERROR
    _OVERRIDE_ERROR = ""

    if not OVERRIDES_FILE.is_file():
        return {}

    try:
        raw = json.loads(OVERRIDES_FILE.read_text(encoding="utf-8"))
        by_value = {kind.value: kind for kind in IconKind}
        parsed: dict[IconKind, dict[int, str]] = {}
        for name, entries in raw.items():
            kind = by_value.get(name)
            if kind is None:
                continue
            parsed[kind] = {int(key): str(path) for key, path in entries.items()}
        return parsed
    except Exception as ex:
        _OVERRIDE_ERROR = f"{OVERRIDES_FILE.name}: {ex}"
        return {}


def _overrides() -> dict[IconKind, dict[int, str]]:
    global _OVERRIDES
    if _OVERRIDES is None:
        _OVERRIDES = _read_overrides()
    return _OVERRIDES


def reload_icon_overrides() -> None:
    """Re-read the override file, for tooling that edits it in place."""
    global _OVERRIDES
    _OVERRIDES = None
    _overrides()


def icon_override_error() -> str:
    """Why the override file was ignored, or an empty string."""
    _overrides()
    return _OVERRIDE_ERROR


def icon_override_count(kind: IconKind) -> int:
    return len(_overrides().get(kind, ()))


def init_icon_index(kind: IconKind, mapping: dict[int, str] | None) -> None:
    """Install the index for one kind. Pass None to clear just that kind."""
    if mapping is None:
        _INDEXES.pop(kind, None)
        return

    _INDEXES[kind] = mapping


def clear_icon_indexes() -> None:
    """Drop every loaded index, for a folder switch or a failed load."""
    _INDEXES.clear()


def is_icon_index_loaded(kind: IconKind) -> bool:
    return kind in _INDEXES


def icon_index_size(kind: IconKind) -> int:
    return len(_INDEXES.get(kind, ()))


def derive_icon_path(kind: IconKind, entity_id: int) -> str:
    """Path implied by the ID alone, ignoring the index."""
    deriver = _DERIVERS.get(kind)
    return deriver(entity_id) if deriver else ""


def icon_path(kind: IconKind, entity_id: int) -> str:
    """Best known icon path.

    Three tiers, in order: a hand-curated override, the built index, then the
    kind's derivation. An override set to an empty string means "this entity has
    no icon", which suppresses a wrong derived guess.
    """
    override = _overrides().get(kind, {}).get(entity_id)
    if override is not None:
        return override

    stored = _INDEXES.get(kind, {}).get(entity_id)
    if stored:
        return stored

    return derive_icon_path(kind, entity_id)
