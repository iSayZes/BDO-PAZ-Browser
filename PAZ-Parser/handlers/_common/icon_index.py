"""Icon lookup by entity kind and ID.

Most icons cannot be derived from an ID. They live in dozens of per-category
folders, and thousands are named after a 3D asset with no numeric part at all
(`inhouse_cultivate_sea_clam_01_wall.dds`). The tables that own those entities
store the icon path inline, so the app builds a lookup index per kind once per
PAZ folder (see `lookup_index.py`), and this module reads it by icon kind.

Each kind may also declare a derivation: the path its ID implies when the index
is unavailable or has no entry. Derivation alone reaches only ~15% of items, so
it is a fallback, never the primary source.
"""

from __future__ import annotations

import json
import re
from collections.abc import Callable
from enum import Enum
from pathlib import Path

from _common.lookup_index import IndexKind, lookup


class IconKind(Enum):
    """Entity kinds with an icon.

    Values are the keys of `icon_overrides.json`, so renaming one orphans its
    overrides.
    """

    ITEM = "item"
    QUEST = "quest"
    CHARACTER = "character"
    PET_EQUIP_SKILL = "pet_equip_skill"
    FAIRY_EQUIP_SKILL = "fairy_equip_skill"
    SKILL = "skill"
    BUFF = "buff"
    # Packed item keys (`enchant_level << 24 | item_id`), for per-level icons.
    ITEM_KEY = "item_key"
    # Kinds whose icons only their own table shows today, indexed for later use.
    QUEST_ARTWORK = "quest_artwork"
    MANOR_PART = "manor_part"
    CUTSCENE = "cutscene"
    WORLDMAP_MARKER = "worldmap_marker"
    # Sprite kinds: icon_path() gives the sheet, icon_region() the region.
    MENU = "menu"
    SUBMENU = "submenu"


# A few stored paths double a separator (`04_pc_skill//04_debuff`).
_REPEATED_SLASHES = re.compile(r"/{2,}")


def clean_stored_icon_path(stored: str) -> str:
    """A stored icon path as the PAZ index spells it: forward slashes, no
    doubled separators, lowercase. Some tables store backslashes
    (`New_Icon\\03_ETC\\00757120.dds` in itemenchant.dbss)."""
    return _REPEATED_SLASHES.sub("/", stored.strip().replace("\\", "/")).lower()


ITEM_ICON_DIR = "ui_texture/icon/new_icon/product_icon_png"


SERVANT_SKILL_ICON_DIR = "ui_texture/icon/new_icon/08_servant_skill/02_pet"


def _derive_item_icon(item_id: int) -> str:
    return f"{ITEM_ICON_DIR}/{item_id:08d}.png"


def _derive_pet_equip_skill_icon(loc_id: int) -> str:
    return f"{SERVANT_SKILL_ICON_DIR}/equipskill_{loc_id:08d}.dds"


def _derive_fairy_equip_skill_icon(loc_id: int) -> str:
    return f"{SERVANT_SKILL_ICON_DIR}/equipskill_fairy_{loc_id:08d}.dds"


# Fallback path templates, used only when the index has no entry. Kinds absent
# here have no derivation: quest and character icons are named after assets far
# more often than after their ID, so a guess would be wrong more than right.
_DERIVERS: dict[IconKind, Callable[[int], str]] = {
    IconKind.ITEM: _derive_item_icon,
    IconKind.PET_EQUIP_SKILL: _derive_pet_equip_skill_icon,
    IconKind.FAIRY_EQUIP_SKILL: _derive_fairy_equip_skill_icon,
}

# The lookup index holding each kind's stored icon paths. Kinds absent here
# have no source table and rely on derivation alone.
ICON_INDEXES: dict[IconKind, IndexKind] = {
    IconKind.ITEM: IndexKind.ITEM_ICON,
    IconKind.QUEST: IndexKind.QUEST_ICON,
    IconKind.CHARACTER: IndexKind.CHARACTER_ICON,
    IconKind.SKILL: IndexKind.SKILL_ICON,
    IconKind.BUFF: IndexKind.BUFF_ICON,
    IconKind.ITEM_KEY: IndexKind.ITEM_KEY_ICON,
    IconKind.QUEST_ARTWORK: IndexKind.QUEST_ARTWORK_ICON,
    IconKind.MANOR_PART: IndexKind.MANOR_PART_ICON,
    IconKind.CUTSCENE: IndexKind.CUTSCENE_ICON,
    IconKind.WORLDMAP_MARKER: IndexKind.WORLDMAP_MARKER_ICON,
    IconKind.MENU: IndexKind.MENU_ICON,
    IconKind.SUBMENU: IndexKind.SUBMENU_ICON,
}

# The sprite region of each sprite kind, as (x1, y1, x2, y2) pixels in the
# sheet icon_path() returns. Kinds absent here are whole-file icons.
ICON_REGION_INDEXES: dict[IconKind, IndexKind] = {
    IconKind.MENU: IndexKind.MENU_ICON_REGION,
    IconKind.SUBMENU: IndexKind.SUBMENU_ICON_REGION,
}

IconRegion = tuple[int, int, int, int]

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


def borrow_icons(
    own: dict[int, str],
    lender_icons: dict[int, str],
    lender_by_entity: dict[int, int],
    exists: Callable[[str], bool],
) -> dict[int, str]:
    """Return `own` with gaps filled from a linked entity's icon.

    For character icons the lender is the item that places or summons the
    character. An entity keeps its own icon when that file exists; a borrowed
    icon is used only when it exists, so a gap is never swapped for another
    dead path. `own` is not modified.
    """
    merged = dict(own)
    for entity_id, lender_id in lender_by_entity.items():
        if exists(merged.get(entity_id, "")):
            continue

        borrowed = lender_icons.get(lender_id, "")
        if borrowed and exists(borrowed):
            merged[entity_id] = borrowed

    return merged


def indexed_icon_path(kind: IconKind, entity_id: int) -> str:
    """Path stored in the kind's lookup index, or an empty string."""
    index_kind = ICON_INDEXES.get(kind)
    if index_kind is None:
        return ""

    stored = lookup(index_kind, entity_id)
    return stored if isinstance(stored, str) else ""


def icon_region(kind: IconKind, entity_id: int) -> IconRegion | None:
    """The sprite region of an icon, or None for whole-file icons and misses."""
    index_kind = ICON_REGION_INDEXES.get(kind)
    if index_kind is None:
        return None

    stored = lookup(index_kind, entity_id)
    if not isinstance(stored, tuple) or len(stored) != 4:
        return None
    x1, y1, x2, y2 = stored
    return x1, y1, x2, y2


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

    stored = indexed_icon_path(kind, entity_id)
    if stored:
        return stored

    return derive_icon_path(kind, entity_id)
