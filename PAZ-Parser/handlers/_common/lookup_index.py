"""Cached `entity ID -> value` lookups built from big source tables.

Some joins need a table far too large to open as a companion on every preview,
such as the 194 MB `itemenchant.dbss`. The app builds each lookup once per PAZ
folder, caches it on disk, and injects it here, the same way `loc.py` receives
LOC data. Handlers then read it by kind and ID and show a dash when the index is
not loaded.

`icon_index.py` layers overrides and ID derivation on top of the icon kinds.
"""

from __future__ import annotations

from collections.abc import Mapping
from enum import Enum

from _common.data_deps import index_dep, note_read

# An icon path, one linked ID, or several linked IDs.
LookupValue = int | str | tuple[int, ...]


class IndexKind(Enum):
    """Every lookup index the app can build.

    Values double as disk-cache keys, so renaming one orphans its cached data
    until the next rebuild.
    """

    ITEM_ICON = "item_icon"
    QUEST_ICON = "quest_icon"
    CHARACTER_ICON = "character_icon"
    CHARACTER_ITEM = "character_item"
    # Characters whose getknowledge() action script grants a card.
    KNOWLEDGE_CHARACTERS = "knowledge_characters"
    # Characters that teach a card through knowledgelearning.dbss (monsters, nodes).
    KNOWLEDGE_LEARNING_CHARACTERS = "knowledge_learning_characters"
    # Items that teach a card through knowledgelearning.dbss.
    KNOWLEDGE_LEARNING_ITEMS = "knowledge_learning_items"
    # Flat (item_id, cost, ...) pairs; read through _common/lease.py.
    CHARACTER_LEASES = "character_leases"
    SKILL_ICON = "skill_icon"
    # Korean skilltype.dbss names, the fallback when LOC type 10 has none.
    SKILL_NAME_KR = "skill_name_kr"
    BUFF_ICON = "buff_icon"
    # Per-level icons of the items whose icon changes with their level.
    ITEM_KEY_ICON = "item_key_icon"
    # Grade (0 to 5) of each base item ID, which colours its name.
    ITEM_GRADE = "item_grade"
    # Journal page artwork by packed quest ID, not the quest's own icon.
    QUEST_ARTWORK_ICON = "quest_artwork_icon"
    # Manor part blueprints by manor_part_key(character_id, part).
    MANOR_PART_ICON = "manor_part_icon"
    CUTSCENE_ICON = "cutscene_icon"
    WORLDMAP_MARKER_ICON = "worldmap_marker_icon"
    # Sprite sheet paths; the *_REGION kinds hold (x1, y1, x2, y2) in the sheet.
    MENU_ICON = "menu_icon"
    MENU_ICON_REGION = "menu_icon_region"
    SUBMENU_ICON = "submenu_icon"
    SUBMENU_ICON_REGION = "submenu_icon_region"
    # Packed item keys a worker production key produces.
    PRODUCTION_ITEMS = "production_items"
    # Buff IDs a skill key applies, in slot order (skill.dbss buff_ids).
    SKILL_BUFFS = "skill_buffs"
    # Base item IDs whose skills apply a buff (itemenchant.dbss -> skill.dbss).
    BUFF_ITEMS = "buff_items"
    # Parent node key of each sub-node (exploration.bss + the worldmap graph).
    NODE_PARENT = "node_parent"
    # Buff IDs that teleport to a point, by teleport_point_id(section, key).
    TELEPORT_BUFFS = "teleport_buffs"
    # Korean names of the teleport buffs, the last fallback for naming a point.
    TELEPORT_BUFF_NAME_KR = "teleport_buff_name_kr"
    # (nearest worldmap node key, metres) of each teleport point.
    TELEPORT_NEAREST_NODE = "teleport_nearest_node"
    # Set IDs each Lightstone item counts toward, as a member or substitute.
    LIGHTSTONE_SETS = "lightstone_sets"
    # Internal name of each instancefield.dbss field (`A1_001`), for buff type 176.
    INSTANCE_FIELD_NAME = "instance_field_name"


# Dependency name each read reports to `data_deps`, built once per kind.
_DEPS: dict[IndexKind, str] = {kind: index_dep(kind.value) for kind in IndexKind}

# kind -> {entity_id: value}
_INDEXES: dict[IndexKind, Mapping[int, LookupValue]] = {}


def init_index(kind: IndexKind, mapping: Mapping[int, LookupValue] | None) -> None:
    """Install the index for one kind. Pass None to clear just that kind."""
    if mapping is None:
        _INDEXES.pop(kind, None)
        return

    _INDEXES[kind] = mapping


def clear_indexes() -> None:
    """Drop every loaded index, for a folder switch or a failed load."""
    _INDEXES.clear()


def is_index_loaded(kind: IndexKind) -> bool:
    note_read(_DEPS[kind])
    return kind in _INDEXES


def index_size(kind: IndexKind) -> int:
    note_read(_DEPS[kind])
    return len(_INDEXES.get(kind, ()))


def index_entries(kind: IndexKind) -> Mapping[int, LookupValue]:
    """Every entry of one kind, empty when the index is not loaded. Read only."""
    note_read(_DEPS[kind])
    return _INDEXES.get(kind, {})


def lookup(kind: IndexKind, entity_id: int) -> LookupValue | None:
    """The stored value, or None when the index is not loaded or lacks the ID."""
    note_read(_DEPS[kind])
    return _INDEXES.get(kind, {}).get(entity_id)
