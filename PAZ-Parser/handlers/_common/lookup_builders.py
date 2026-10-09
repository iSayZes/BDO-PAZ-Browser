"""Which lookup indexes exist and how each is built.

Every index is one `IndexSpec`: the tables it reads and the function that turns
them into `{entity_id: value}`. `build_indexes` reads each table once, so specs
that share a source reuse its payload, such as the 194 MB `itemenchant.dbss`
behind both the item icons and the character-to-item links.

This lives with the handlers, not in the app core, so a new index needs no
core change: the core only calls `build_indexes()`, installs the result
(`lookup_index.py`) and caches it (`api/bdo_lookup_indexes.py`).

Builders are imported at module level so that the core's cache fingerprint,
which follows this module's imports, reaches every builder and helper that
shapes the result.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import cast

from _common.icon_index import borrow_icons
from _bss.buffsimply.parser import build_buff_icon_index
from _bss.exploration.parser import build_node_parent_index
from _bss.groupcameradata.parser import build_cutscene_icon_index
from _bss.instancefieldmapinfo.parser import build_instance_field_title_index
from _bss.lightstoneset.parser import build_lightstone_set_index
from _bss.mansionpartinfo.parser import build_manor_part_icon_index
from _bss.menu.parser import build_menu_icon_index, build_menu_icon_region_index
from _bss.plantexchangegroup.parser import build_production_item_index
from _bss.questjournalvideoinfo.parser import build_quest_artwork_index
from _bss.specialenchantitem.parser import build_item_key_icon_index
from _bss.submenu.parser import build_submenu_icon_index, build_submenu_icon_region_index
from _bwp.waypoint.worldmap import WORLDMAP_FILE
from _common.lookup_index import IndexKind, LookupValue
from _dbss.characterobject.parser import build_character_icon_index
from _dbss.characterstatic.parser import build_knowledge_character_index
from _dbss.buff.parser import build_teleport_buff_index, build_teleport_buff_name_index
from _dbss.detail_dialog.parser import build_character_lease_index
from _dbss.instancefield.parser import build_instance_field_name_index
from _dbss.itemenchant.parser import (
    build_buff_item_index,
    build_character_item_index,
    build_item_grade_index,
    build_item_icon_index,
)
from _dbss.knowledgelearning.parser import (
    build_knowledge_learning_character_index,
    build_knowledge_learning_item_index,
)
from _dbss.quest.parser import build_quest_icon_index
from _dbss.skill.parser import build_skill_buff_index
from _dbss.teleport.parser import build_teleport_nearest_node_index
from _dbss.skilltype.parser import build_skill_icon_index, build_skill_name_index
from _dbss.worldmapmonster.parser import build_worldmap_marker_icon_index

_BINARY = "gamecommondata/binary"
ITEMENCHANT = f"{_BINARY}/itemenchant.dbss"
ITEMENCHANT_OFFSET = f"{_BINARY}/itemenchantoffset.dbss"
QUEST = f"{_BINARY}/quest.dbss"
ALLQUESTLIST = f"{_BINARY}/allquestlist.bss"
CHARACTEROBJECT = f"{_BINARY}/characterobject.dbss"
CHARACTEROBJECT_OFFSET = f"{_BINARY}/characterobjectoffset.dbss"
CHARACTERSTATIC = f"{_BINARY}/characterstatic.dbss"
CHARACTERSTATIC_OFFSET = f"{_BINARY}/characterstaticoffset.dbss"
KNOWLEDGELEARNING = f"{_BINARY}/knowledgelearning.dbss"
KNOWLEDGELEARNING_OFFSET = f"{_BINARY}/knowledgelearningoffset.dbss"
DETAIL_DIALOG = f"{_BINARY}/detail_dialog.dbss"
DETAIL_DIALOG_OFFSET = f"{_BINARY}/detail_dialogoffset.dbss"
SKILL = f"{_BINARY}/skill.dbss"
SKILL_OFFSET = f"{_BINARY}/skilloffset.dbss"
SKILLTYPE = f"{_BINARY}/skilltype.dbss"
SKILLTYPE_OFFSET = f"{_BINARY}/skilltypeoffset.dbss"
BUFFSIMPLY = f"{_BINARY}/buffsimply.bss"
SPECIALENCHANTITEM = f"{_BINARY}/specialenchantitem.bss"
QUESTJOURNALVIDEOINFO = f"{_BINARY}/questjournalvideoinfo.bss"
MANSIONPARTINFO = f"{_BINARY}/mansionpartinfo.bss"
GROUPCAMERADATA = f"{_BINARY}/groupcameradata.bss"
WORLDMAPMONSTER = f"{_BINARY}/worldmapmonster.dbss"
WORLDMAPMONSTER_OFFSET = f"{_BINARY}/worldmapmonsteroffset.dbss"
MENU = f"{_BINARY}/menu.bss"
SUBMENU = f"{_BINARY}/submenu.bss"
PLANTEXCHANGEGROUP = f"{_BINARY}/plantexchangegroup.bss"
ITEMSUBGROUP = f"{_BINARY}/itemsubgroup.dbss"
ITEMSUBGROUP_OFFSET = f"{_BINARY}/itemsubgroupoffset.dbss"
EXPLORATION = f"{_BINARY}/exploration.bss"
BUFF = f"{_BINARY}/buff.dbss"
BUFF_OFFSET = f"{_BINARY}/buffoffset.dbss"
TELEPORT = f"{_BINARY}/teleport.dbss"
LIGHTSTONESET = f"{_BINARY}/lightstoneset.bss"
INSTANCEFIELD = f"{_BINARY}/instancefield.dbss"
INSTANCEFIELDMAPINFO = f"{_BINARY}/instancefieldmapinfo.bss"
STRINGTABLE = f"{_BINARY}/stringtable.bss"
WORLDMAP = f"gamecommondata/waypoint_binary/{WORLDMAP_FILE}"

# Every built index, keyed by `IndexKind.value`.
BuiltIndexes = dict[str, Mapping[int, LookupValue]]


@dataclass(frozen=True)
class IndexSpec:
    """One index: `build` receives the payloads of `sources`, in that order."""

    kind: IndexKind
    sources: tuple[str, ...]
    build: Callable[..., Mapping[int, LookupValue]]


# Adding an index is one entry here plus its `IndexKind` member.
INDEX_SPECS: tuple[IndexSpec, ...] = (
    IndexSpec(IndexKind.ITEM_ICON, (ITEMENCHANT, ITEMENCHANT_OFFSET), build_item_icon_index),
    IndexSpec(IndexKind.ITEM_GRADE, (ITEMENCHANT, ITEMENCHANT_OFFSET), build_item_grade_index),
    IndexSpec(IndexKind.QUEST_ICON, (QUEST, ALLQUESTLIST), build_quest_icon_index),
    IndexSpec(
        IndexKind.CHARACTER_ICON,
        (CHARACTEROBJECT, CHARACTEROBJECT_OFFSET),
        build_character_icon_index,
    ),
    IndexSpec(
        IndexKind.CHARACTER_ITEM,
        (ITEMENCHANT, ITEMENCHANT_OFFSET),
        build_character_item_index,
    ),
    IndexSpec(
        IndexKind.KNOWLEDGE_CHARACTERS,
        (CHARACTERSTATIC, CHARACTERSTATIC_OFFSET),
        build_knowledge_character_index,
    ),
    IndexSpec(
        IndexKind.KNOWLEDGE_LEARNING_CHARACTERS,
        (KNOWLEDGELEARNING, KNOWLEDGELEARNING_OFFSET),
        build_knowledge_learning_character_index,
    ),
    IndexSpec(
        IndexKind.KNOWLEDGE_LEARNING_ITEMS,
        (KNOWLEDGELEARNING, KNOWLEDGELEARNING_OFFSET),
        build_knowledge_learning_item_index,
    ),
    IndexSpec(
        IndexKind.CHARACTER_LEASES,
        (DETAIL_DIALOG, DETAIL_DIALOG_OFFSET),
        build_character_lease_index,
    ),
    IndexSpec(IndexKind.SKILL_ICON, (SKILLTYPE, SKILLTYPE_OFFSET), build_skill_icon_index),
    IndexSpec(IndexKind.SKILL_NAME_KR, (SKILLTYPE, SKILLTYPE_OFFSET), build_skill_name_index),
    # buffsimply.bss holds the buff.dbss icon paths in fixed rows, 1.4 MB against 12 MB.
    IndexSpec(IndexKind.BUFF_ICON, (BUFFSIMPLY,), build_buff_icon_index),
    # The per-level icons of itemenchant.dbss for the items that change icon, 175 KB.
    IndexSpec(IndexKind.ITEM_KEY_ICON, (SPECIALENCHANTITEM,), build_item_key_icon_index),
    # Icons only their own tables show today, a few KB each, indexed for later use.
    IndexSpec(IndexKind.QUEST_ARTWORK_ICON, (QUESTJOURNALVIDEOINFO,), build_quest_artwork_index),
    IndexSpec(IndexKind.MANOR_PART_ICON, (MANSIONPARTINFO,), build_manor_part_icon_index),
    IndexSpec(IndexKind.CUTSCENE_ICON, (GROUPCAMERADATA,), build_cutscene_icon_index),
    IndexSpec(
        IndexKind.WORLDMAP_MARKER_ICON,
        (WORLDMAPMONSTER, WORLDMAPMONSTER_OFFSET),
        build_worldmap_marker_icon_index,
    ),
    IndexSpec(IndexKind.MENU_ICON, (MENU,), build_menu_icon_index),
    IndexSpec(IndexKind.MENU_ICON_REGION, (MENU,), build_menu_icon_region_index),
    IndexSpec(IndexKind.SUBMENU_ICON, (SUBMENU,), build_submenu_icon_index),
    IndexSpec(IndexKind.SUBMENU_ICON_REGION, (SUBMENU,), build_submenu_icon_region_index),
    # A few hundred production subgroups out of the 13 MB itemsubgroup.dbss.
    IndexSpec(
        IndexKind.PRODUCTION_ITEMS,
        (PLANTEXCHANGEGROUP, ITEMSUBGROUP, ITEMSUBGROUP_OFFSET),
        build_production_item_index,
    ),
    IndexSpec(IndexKind.SKILL_BUFFS, (SKILL, SKILL_OFFSET), build_skill_buff_index),
    # The item to buff link: itemenchant.dbss skill keys -> skill.dbss buff_ids.
    IndexSpec(
        IndexKind.BUFF_ITEMS,
        (ITEMENCHANT, ITEMENCHANT_OFFSET, SKILL, SKILL_OFFSET),
        build_buff_item_index,
    ),
    # Sub-node -> parent node, so a sub-node reads `Bambu Valley - Mining`.
    IndexSpec(IndexKind.NODE_PARENT, (EXPLORATION, WORLDMAP), build_node_parent_index),
    # The 654 teleport buffs out of the 12 MB buff.dbss, to name teleport.dbss points.
    IndexSpec(IndexKind.TELEPORT_BUFFS, (BUFF, BUFF_OFFSET), build_teleport_buff_index),
    IndexSpec(IndexKind.TELEPORT_BUFF_NAME_KR, (BUFF, BUFF_OFFSET), build_teleport_buff_name_index),
    # Where a teleport buff goes, for its Effect text: the 11 KB teleport.dbss
    # against the worldmap graph.
    IndexSpec(IndexKind.TELEPORT_NEAREST_NODE, (TELEPORT, WORLDMAP), build_teleport_nearest_node_index),
    # Lightstone item -> its sets, for the itemenchant.dbss Lightstone Sets column.
    IndexSpec(IndexKind.LIGHTSTONE_SETS, (LIGHTSTONESET,), build_lightstone_set_index),
    # Instance field key -> name, for the buff.dbss Effect text of type 176.
    IndexSpec(IndexKind.INSTANCE_FIELD_NAME, (INSTANCEFIELD,), build_instance_field_name_index),
    # Instance field key -> GAME sheet hash of its title, read in the loaded LOC language.
    IndexSpec(
        IndexKind.INSTANCE_FIELD_TITLE,
        (INSTANCEFIELDMAPINFO, STRINGTABLE),
        build_instance_field_title_index,
    ),
)


def build_indexes(
    read: Callable[[str], bytes | None],
    exists: Callable[[str], bool],
    specs: tuple[IndexSpec, ...] = INDEX_SPECS,
) -> BuiltIndexes:
    """Build every spec whose sources are all present, keyed by kind value.

    `read` returns a PAZ payload or None; `exists` answers whether a PAZ path
    is shipped, for the character icon borrowing step.
    """
    payloads: dict[str, bytes | None] = {}

    def load(path: str) -> bytes | None:
        if path not in payloads:
            payloads[path] = read(path)
        return payloads[path]

    indexes: BuiltIndexes = {}
    for spec in specs:
        data = [load(path) for path in spec.sources]
        if any(payload is None for payload in data):
            continue
        indexes[spec.kind.value] = dict(spec.build(*data))

    return _with_borrowed_character_icons(indexes, exists)


def _with_borrowed_character_icons(
    indexes: BuiltIndexes,
    exists: Callable[[str], bool],
) -> BuiltIndexes:
    """Give characters without a working icon the icon of their item.

    Fences, crops and pets often store no icon, or one the client does not
    ship, while the item that places or summons them does.
    """
    characters = indexes.get(IndexKind.CHARACTER_ICON.value)
    items = indexes.get(IndexKind.ITEM_ICON.value)
    links = indexes.get(IndexKind.CHARACTER_ITEM.value)
    if characters is None or items is None or links is None:
        return indexes

    # The builders fix the value types: icon kinds hold paths, links hold IDs.
    merged = borrow_icons(
        cast(dict[int, str], characters),
        cast(dict[int, str], items),
        cast(dict[int, int], links),
        exists,
    )
    return {**indexes, IndexKind.CHARACTER_ICON.value: merged}
