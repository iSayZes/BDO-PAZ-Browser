from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.item_grade import ITEM_GRADE_COLORS, item_grade_tagged
from _common.lookup_index import IndexKind
from tests.character_indexes import character_group_index
from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)


_ICON_ROOT = "ui_texture/icon/new_icon"
# Stored icon paths start with one of these, in any case.
_ICON_FOLDERS = ("new_icon", "item_icon")
# King Clam Wall Ornament: furniture, so its icon is named after the 3D asset
# and is unreachable from the item ID alone. It is the case this format solves.
_KING_CLAM = 24626
# [Event] Fence places character 2053, which has no icon of its own.
_EVENT_FENCE = 58011
_EVENT_FENCE_CHARACTER = 2053
_WEAPON = 697192
# Balacs Lunchbox, a yellow (grade 3) item (itemenchant_dbss.md).
_BALACS_LUNCHBOX = 9359
# Servant gear (servant_slots.py): a horse barding in Chest (3), a horse
# costume saddle in 15 (the client table says stirrups), a wagon cover in Body
# (25), a Caravel sail in 25, a rowboat cargo container in Boots (5), and a
# camping tent's look in 6, labelled from the camp window.
_LIGHT_LEATHER_BARDING = 52602
_ORZEKEL_SADDLE = 336046
_SHABBY_WAGON_COVER = 53501
_CARAVEL_WHITE_WIND_SAIL = 49652
_ROWBOAT_CARGO_CONTAINER = 49201
_NAPHART_CAMPING_TENT = 18881
# Kzarka Gauntlet enhances +1 to +15, then PRI to PEN: levels 1-20.
_KZARKA_GAUNTLET = 11210
# Its enchantstaticstatus.dbss key (enchantstaticstatus_dbss.md).
_KZARKA_GAUNTLET_ENCHANT_KEY = 662
_PEN = 20
# The key packs the item ID into its low 24 bits and the enchant level above them.
_MAX_ITEM_ID = 0xFFFFFF
_OFFSET_HEADER_SIZE = 8
_OFFSET_ROW_SIZE = 12
_ENCHANT_LEVEL_SHIFT = 24
_OFFSET_FILE = "itemenchantoffset.dbss"
# [Blessing] Adventure's Boon (120 min) casts skill 47683 level 1, which
# applies buffs 48723 to 48728.
_BOON_ITEM = 761880
_BOON_SKILL_KEY = 47683 << 16 | 1
_BOON_BUFFS = (48723, 48724, 48725, 48726, 48727, 48728)
# Lightstone of Fire: Twisted, a member of set 182 [The Wild: Edania].
_TWISTED_LIGHTSTONE = 758021
_EDANIA_SET = 182
# Field checks from itemenchant_dbss.md, in game or on bdocodex (2026-10-05).
_BASTEER_LONGSWORD = 10011
_KHARAZAD_NECKLACE = 11697
_YOUNG_CROW_EARRING = 964704
_DANDELION_KAMASYLVEN_SWORD = 14732
_OBSIDIAN_BLACKSTAR_ARMOR = 732052
_PUMPKIN_GHOST_SEED = 55725
_APPRENTICES_MEDICINE_BOX = 9866
# Usable only up to character level 20 (tooltip use limit).
_HP_POTION_BEGINNER = 502
_BEGINNER_MAX_LEVEL = 20
_ARSHA_PURGATUM_180_DAYS = 830533
# Enhancement types (itemenchant_dbss.md, After the Icon): ordinary weapons and
# armour 1, Blackstar 2, Kharazad 21.
_ORDINARY_GEAR = 1
_BLACKSTAR_LONGSWORD = 715001
_BLACKSTAR = 2
# Pace of Delight - 1 Square grants marblegamediceitemgroup.dbss group 1001
# (contents event 98, marblegamediceitemgroup_dbss.md).
_PACE_OF_DELIGHT_1 = 756440
_PACE_OF_DELIGHT_1_GROUP = 1001
_MARBLE_DICE = 98
# Mysterious Secret Note opens customizeditem.dbss record 497 (contents event
# 31 CustomizedItemBox, customizeditem_dbss.md).
_MYSTERIOUS_SECRET_NOTE = 66297
_SECRET_NOTE_BOX_KEY = 497
_CUSTOMIZED_ITEM_BOX = 31
# Blackstar Longsword's Warrior class entry names item mesh key 336000, the
# itemeffectchange.dbss one-handed sword mesh (itemenchant_dbss.md, Item Mesh Keys).
_BLACKSTAR_SWORD_MESH = 336000
_KHARAZAD = 21
# Equipment types the tooltip names (PaGlobalFunc_Util_ClassEquipParts):
# longsword 1 (a main-hand type), necklace 15.
_LONGSWORD = 1
_NECKLACE = 15
# A sub-weapon, named after its Central Market subcategory like main weapons.
_SOVEREIGN_KUNAI = 930007
# Life Skill gear (life_slots.py): Cooking clothes (type 12, Cooking tab 3),
# a gathering tool, a life tool, a ring, a knot and the orb (any tab, 15).
_LOGGIA_COOKS_CLOTHES = 705119
_LOGGIA_LUMBERING_AXE = 720520
_LOGGIA_FISHING_CHAIR = 705537
_LOGGIA_RING = 705503
_VENIA_KNOT = 860363
_EVERGREEN_ORB = 933601
_BLACK_STONE = 16001
# Servant gear with a non-empty `unknown_5d`, so its later header fields move.
_OQUILLA_SAIL_BALANCE = 607887
# Ancient Spirit's Crystal - Viper, in jewelgroupstaticstatus.bss group 101.
_ANCIENT_SPIRIT_VIPER = 15653
_ANCIENT_SPIRIT_GROUP = 101
_JEWEL_GROUP_FILE = "jewelgroupstaticstatus.bss"
# Marni's Stone (Bashim), a soul collector (ContentsEventType 59) counting
# the kills of characterstatic.dbss character group 70.
_MARNIS_STONE_BASHIM = 40351
_SOUL_COLLECT = 59
_BASHIM_GROUP = 70


def _base_item_count(offsets: bytes) -> int:
    """Offset rows with enchant level 0: one per item."""
    (count,) = struct.unpack_from("<I", offsets, 4)
    return sum(
        1
        for row in range(count)
        if not struct.unpack_from("<I", offsets, _OFFSET_HEADER_SIZE + row * _OFFSET_ROW_SIZE)[0]
        >> _ENCHANT_LEVEL_SHIFT
    )


def _declared_items(source: CaseInput) -> int:
    return _base_item_count(source.file(_OFFSET_FILE))


CASE = HandlerCase(
    handler_name="itemenchant.dbss",
    data_file="itemenchant.dbss",
    companion_files={
        "itemenchantoffset.dbss": "itemenchantoffset.dbss",
        _JEWEL_GROUP_FILE: _JEWEL_GROUP_FILE,
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Item"],
    internal_path="gamecommondata/binary/itemenchant.dbss",
    lookup_indexes={
        IndexKind.SKILL_BUFFS: {_BOON_SKILL_KEY: _BOON_BUFFS},
        IndexKind.LIGHTSTONE_SETS: {_TWISTED_LIGHTSTONE: (_EDANIA_SET,)},
        IndexKind.CHARACTER_GROUP_MEMBERS: character_group_index,
    },
    tests=[
        SchemaTest(
            required_keys=[
                "item_id",
                "name_kr",
                "max_enchant_level",
                "enchant_key",
                "enhancement_type",
                "equip_type",
                "weapon_type",
                "equip_slot",
                "slot",
                "servant_kinds",
                "life_equip_type",
                "life_restrict_type",
                "market_category",
                "market_sub_category",
                "stackable",
                "do_apply_directly",
                "expiration_minutes",
                "time_limit",
                "required_level",
                "max_level",
                "repair_endurance_count",
                "class_mask",
                "classes",
                "vested_type",
                "family_bound",
                "binding",
                "max_durability",
                "marketable",
                "family_inventory",
                "trade_type",
                "trade",
                "dyeable",
                "icon_path",
                "second_string",
                "block_size",
                "item_name",
                "description",
                "character_id",
                "character_name",
                "skill_keys",
                "buff_ids",
                "buffs",
                "buff_count",
                "lightstone_set_ids",
                "lightstone_sets",
                "lightstone_set_count",
                "crystal_group",
                "crystal_group_label",
                "contents_event_type",
                "contents_event",
                "contents_event_param1",
                "contents_event_param2",
                "contents_event_param1_text",
            ],
        ),
        DeclaredCountTest(declared=_declared_items),
        RangeTest(col="item_id", min_val=1, max_val=_MAX_ITEM_ID),
        # A new grade needs its colour in _common/item_grade.py first.
        RangeTest(col="grade", min_val=0, max_val=len(ITEM_GRADE_COLORS) - 1),
        # Balacs Lunchbox is a yellow (grade 3) item.
        TargetTest(col="item_id", value=_BALACS_LUNCHBOX, expected={"grade": 3}),
        # Item names are drawn in their grade colour.
        PaFieldTest(field="item_name"),
        # Descriptions keep their game colours (LOC type 0 field 1).
        PaFieldTest(field="description"),
        # The furniture case: icon path comes from the block, not the item ID.
        TargetTest(
            col="item_id",
            value=_KING_CLAM,
            expected={
                "max_enchant_level": 0,
                "item_name": "King Clam Wall Ornament",
                "icon_path": (
                    f"{_ICON_ROOT}/03_etc/06_housing/"
                    "inhouse_cultivate_sea_clam_01_wall.dds"
                ),
                "second_string": "",
                "character_id": 17026,
                "character_name": "King Clam Wall Ornament",
            },
        ),
        TargetTest(
            col="item_id",
            value=_EVENT_FENCE,
            expected={
                "max_enchant_level": 0,
                "character_id": _EVENT_FENCE_CHARACTER,
                "character_name": "[Event] Fence",
            },
        ),
        # A weapon places no character; stored as None so it sorts last.
        TargetTest(
            col="item_id",
            value=_WEAPON,
            expected={"character_id": None, "character_name": ""},
        ),
        # A consumable: its skill's buffs, in slot order.
        TargetTest(
            col="item_id",
            value=_BOON_ITEM,
            expected={"skill_keys": [_BOON_SKILL_KEY], "buff_ids": list(_BOON_BUFFS), "buff_count": 6},
        ),
        # A weapon casts no skill; no buffs, None to sort last.
        TargetTest(
            col="item_id",
            value=_WEAPON,
            expected={"skill_keys": [], "buff_ids": [], "buff_count": None},
        ),
        # A Lightstone lists its sets by ID and LOC type 113 name.
        TargetTest(
            col="item_id",
            value=_TWISTED_LIGHTSTONE,
            expected={
                "lightstone_set_ids": [_EDANIA_SET],
                "lightstone_sets": [f"{_EDANIA_SET} [The Wild: Edania]"],
                "lightstone_set_count": 1,
            },
        ),
        TargetTest(
            col="item_id",
            value=_WEAPON,
            expected={"lightstone_set_ids": [], "lightstone_sets": [], "lightstone_set_count": None},
        ),
        TargetTest(
            col="item_id",
            value=_KZARKA_GAUNTLET,
            expected={
                "max_enchant_level": _PEN,
                "enchant_key": _KZARKA_GAUNTLET_ENCHANT_KEY,
                "item_name": "Kzarka Gauntlet",
                "name_kr": "크자카 권갑",
            },
        ),
        # Main weapons need no level; Kzarka is for two classes, binds never,
        # sells on the market and can be dyed.
        TargetTest(
            col="item_id",
            value=_KZARKA_GAUNTLET,
            expected={
                "required_level": None,
                "classes": "Striker, Mystic",
                "binding": "",
                "marketable": True,
                "dyeable": True,
            },
        ),
        # The enhancement type is the guaranteeenchantss.dbss group; None
        # (sorts last) on items that cannot be enhanced.
        TargetTest(col="item_id", value=_KZARKA_GAUNTLET, expected={"enhancement_type": _ORDINARY_GEAR}),
        TargetTest(col="item_id", value=_BLACKSTAR_LONGSWORD, expected={"enhancement_type": _BLACKSTAR}),
        TargetTest(col="item_id", value=_KHARAZAD_NECKLACE, expected={"enhancement_type": _KHARAZAD}),
        TargetTest(col="item_id", value=_BALACS_LUNCHBOX, expected={"enhancement_type": None}),
        # A crystal stores its jewelgroupstaticstatus.bss group; other items None.
        TargetTest(col="item_id", value=_ANCIENT_SPIRIT_VIPER, expected={"crystal_group": _ANCIENT_SPIRIT_GROUP}),
        TargetTest(col="item_id", value=_WEAPON, expected={"crystal_group": None, "crystal_group_label": ""}),
        TargetTest(
            col="item_id",
            value=_DANDELION_KAMASYLVEN_SWORD,
            expected={"required_level": 56},
        ),
        # A level cap is stored as such; items without one store None.
        TargetTest(
            col="item_id",
            value=_HP_POTION_BEGINNER,
            expected={"required_level": None, "max_level": _BEGINNER_MAX_LEVEL},
        ),
        TargetTest(col="item_id", value=_KZARKA_GAUNTLET, expected={"max_level": None}),
        # Memory Fragments repair gear only; a material has no amount.
        TargetTest(col="item_id", value=_BLACK_STONE, expected={"repair_endurance_count": None}),
        RangeTest(col="repair_endurance_count", min_val=1, max_val=0xFF),
        TargetTest(
            col="item_id",
            value=_BASTEER_LONGSWORD,
            expected={"binding": "On obtain (Family)", "classes": "Warrior, Valkyrie", "marketable": False},
        ),
        TargetTest(
            col="item_id",
            value=_ARSHA_PURGATUM_180_DAYS,
            expected={"binding": "On equip (Character)", "classes": "Seraph"},
        ),
        # All playable classes, and all but the newest one.
        TargetTest(col="item_id", value=_KHARAZAD_NECKLACE, expected={"classes": "All", "marketable": False}),
        TargetTest(col="item_id", value=_YOUNG_CROW_EARRING, expected={"classes": "All except Agent"}),
        # Food goes in the Family Inventory and has no durability.
        TargetTest(
            col="item_id",
            value=_BALACS_LUNCHBOX,
            expected={"family_inventory": True, "max_durability": None, "trade": ""},
        ),
        TargetTest(col="item_id", value=_OBSIDIAN_BLACKSTAR_ARMOR, expected={"dyeable": False}),
        TargetTest(
            col="item_id",
            value=_PUMPKIN_GHOST_SEED,
            expected={"trade_type": 1, "trade": "Trade Manager (Karma loss)"},
        ),
        TargetTest(
            col="item_id",
            value=_APPRENTICES_MEDICINE_BOX,
            expected={"trade_type": 3, "trade": "Imperial Crafting Delivery"},
        ),
        # Gear names its slot as the tooltip does and does not stack.
        TargetTest(
            col="item_id",
            value=_BASTEER_LONGSWORD,
            expected={"slot": "Main Weapon", "equip_type": _LONGSWORD, "weapon_type": "Longsword", "stackable": False},
        ),
        # Weapon types are named from their market subcategory, also when the
        # item is not listed (Basteer Longsword); other gear has its slot only.
        TargetTest(col="item_id", value=_KZARKA_GAUNTLET, expected={"weapon_type": "Gauntlet"}),
        TargetTest(col="item_id", value=_SOVEREIGN_KUNAI, expected={"slot": "Sub-weapon", "weapon_type": "Kunai"}),
        TargetTest(
            col="item_id",
            value=_KHARAZAD_NECKLACE,
            expected={"slot": "Necklace", "equip_type": _NECKLACE, "weapon_type": "", "stackable": False},
        ),
        # Items that are not equipment have no slot and type; materials and food stack.
        TargetTest(
            col="item_id",
            value=_BLACK_STONE,
            expected={"slot": "", "equip_type": None, "stackable": True},
        ),
        TargetTest(col="item_id", value=_BALACS_LUNCHBOX, expected={"slot": "", "stackable": True}),
        # Servant gear names the slot of its servant, not the character slot.
        TargetTest(col="item_id", value=_LIGHT_LEATHER_BARDING, expected={"slot": "Barding"}),
        TargetTest(col="item_id", value=_ORZEKEL_SADDLE, expected={"slot": "Saddle (Costume)"}),
        TargetTest(col="item_id", value=_SHABBY_WAGON_COVER, expected={"slot": "Cover"}),
        TargetTest(col="item_id", value=_CARAVEL_WHITE_WIND_SAIL, expected={"slot": "Sail"}),
        TargetTest(col="item_id", value=_ROWBOAT_CARGO_CONTAINER, expected={"slot": "Cargo Container"}),
        TargetTest(col="item_id", value=_NAPHART_CAMPING_TENT, expected={"slot": "Appearance"}),
        # Life Skill gear names its Life Skill tab slot.
        TargetTest(
            col="item_id",
            value=_LOGGIA_COOKS_CLOTHES,
            expected={"slot": "Armor", "life_equip_type": 12, "life_restrict_type": 3},
        ),
        TargetTest(col="item_id", value=_LOGGIA_LUMBERING_AXE, expected={"slot": "Lumbering Axe"}),
        TargetTest(col="item_id", value=_LOGGIA_FISHING_CHAIR, expected={"slot": "Tool"}),
        TargetTest(col="item_id", value=_LOGGIA_RING, expected={"slot": "Ring", "life_restrict_type": 15}),
        TargetTest(col="item_id", value=_VENIA_KNOT, expected={"slot": "Knot"}),
        TargetTest(col="item_id", value=_EVERGREEN_ORB, expected={"slot": "Orb"}),
        # A soul collector names its event and the character group it counts.
        TargetTest(
            col="item_id",
            value=_MARNIS_STONE_BASHIM,
            expected={
                "contents_event_type": _SOUL_COLLECT,
                "contents_event": "59 SoulCollect",
                "contents_event_param1": _BASHIM_GROUP,
            },
        ),
        # A weapon does nothing on use: no event, None to sort last.
        TargetTest(
            col="item_id",
            value=_WEAPON,
            expected={"contents_event_type": None, "contents_event": "", "contents_event_param1_text": ""},
        ),
        # The fields after `unknown_5d` are read past its entries: a sail
        # places no character and casts no skill.
        TargetTest(
            col="item_id",
            value=_OQUILLA_SAIL_BALANCE,
            expected={"character_id": None, "skill_keys": []},
        ),
    ],
)


@pytest.fixture(scope="module")
def itemenchant_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemenchant_dbss(
    spec: Any,
    itemenchant_result: HandlerResult,
) -> None:
    itemenchant_result.check(spec)


def test_every_item_has_a_name(itemenchant_result: HandlerResult) -> None:
    """Items without a LOC row fall back to the Korean name stored in the block."""
    records = itemenchant_result.records

    assert all(record["name_kr"] for record in records)
    assert all(record["item_name"] for record in records)


def test_soul_collectors_name_their_character_group(itemenchant_result: HandlerResult) -> None:
    """param1 of every soul collector is a character group with members; param2 is its kill count."""
    collectors = [r for r in itemenchant_result.records if r["contents_event_type"] == _SOUL_COLLECT]

    assert collectors
    for record in collectors:
        assert record["contents_event_param1_text"].startswith(f"{record['contents_event_param1']}: ")
        assert record["contents_event_param2"] is not None and record["contents_event_param2"] > 0


def test_every_block_opens_and_closes_with_its_packed_key(itemenchant_result: HandlerResult) -> None:
    """`+0x00` and end-6 repeat the offset row's packed key, enchant level included."""
    from _dbss.itemenchant.parser import parse_itemenchantoffset_records

    source = itemenchant_result.source
    data = source.data
    bad = [
        row["key"]
        for row in parse_itemenchantoffset_records(source.file(_OFFSET_FILE))
        if struct.unpack_from("<I", data, row["data_offset"])[0] != row["key"]
        or struct.unpack_from("<I", data, row["data_offset"] + row["data_size"] - 6)[0] != row["key"]
    ]

    assert not bad, f"blocks whose key copies differ from the offset row: {bad[:5]}"


def test_every_block_walks_to_its_name_and_icon(itemenchant_result: HandlerResult) -> None:
    """The counted lists lead to the Korean name and an icon path in every block, every level."""
    from _dbss.itemenchant.layout_2 import read_block_strings
    from _dbss.itemenchant.parser import parse_itemenchantoffset_records

    source = itemenchant_result.source
    data = source.data
    bad = []
    for row in parse_itemenchantoffset_records(source.file(_OFFSET_FILE)):
        start = row["data_offset"]
        strings = read_block_strings(data, start, start + row["data_size"])
        # The icon folder, not `.dds`: item 31645 stores its path without one (client 3482).
        if not strings.name_kr or not strings.icon.lower().startswith(_ICON_FOLDERS):
            bad.append(row["key"])

    assert not bad, f"blocks whose walk ends on no name or icon: {bad[:5]}"


def test_every_crystal_group_is_a_named_jewel_group(itemenchant_result: HandlerResult) -> None:
    """The crystal footer holds jewelgroupstaticstatus.bss group numbers, so
    every crystal's label names its group instead of showing the number."""
    from _bss.jewelgroupstaticstatus.parser import parse_jewel_group_records
    from tests.fixtures import load_binary_fixture

    groups = {row["group"] for row in parse_jewel_group_records(load_binary_fixture(_JEWEL_GROUP_FILE))}
    crystals = [r for r in itemenchant_result.records if r["crystal_group"] is not None]
    assert crystals, "no item stores a crystal group"
    unknown = sorted({r["crystal_group"] for r in crystals} - groups)
    assert not unknown, f"crystal groups missing from {_JEWEL_GROUP_FILE}: {unknown}"
    unnamed = [r["item_id"] for r in crystals if r["crystal_group_label"] == str(r["crystal_group"])]
    assert not unnamed, f"crystals whose label is the bare group number: {unnamed[:5]}"


def test_crystal_group_label_shows_the_limit_as_the_tooltip_does() -> None:
    from _bss.jewelgroupstaticstatus.names import NO_LIMIT, JewelGroup
    from _dbss.itemenchant.labels import crystal_group_label

    values = {"crystalGroup": "{name} (max {max_count})", "crystalGroupNoLimit": "{name} (No Limit)"}
    groups = {1: JewelGroup("Dawn", 2), 2: JewelGroup("No Group", NO_LIMIT), 3: JewelGroup("", 4)}
    assert crystal_group_label(1, groups, values) == "Dawn (max 2)"
    assert crystal_group_label(2, groups, values) == "No Group (No Limit)"
    # Unnamed, or without jewelgroupstaticstatus.bss: the number; not a crystal: ''.
    assert crystal_group_label(3, groups, values) == "3"
    assert crystal_group_label(4, {}, values) == "4"
    assert crystal_group_label(None, groups, values) == ""


def test_slot_label_hashes_match_stringtable() -> None:
    from _bss.stringtable.parser import GAME_SHEET, parse_key_hashes
    from _dbss.itemenchant.slot_labels import SLOT_LABELS
    from tests.fixtures import load_binary_fixture

    hashes = parse_key_hashes(load_binary_fixture("stringtable.bss"), GAME_SHEET)
    wrong = {
        label.key: (label.key_hash, hashes.get(label.key))
        for label in SLOT_LABELS.values()
        if hashes.get(label.key) != label.key_hash
    }
    assert not wrong, f"slot label hashes differ from stringtable.bss (stored, file): {wrong}"


def test_servant_and_life_slot_label_hashes_match_stringtable() -> None:
    from _bss.stringtable.parser import parse_sheet_key_hashes
    from _dbss.itemenchant.life_slots import LIFE_SLOT_LABELS
    from _dbss.itemenchant.servant_slots import SERVANT_SLOT_LABELS
    from tests.fixtures import load_binary_fixture

    labels = [label for group in SERVANT_SLOT_LABELS.values() for label in group.values()]
    labels += LIFE_SLOT_LABELS.values()
    hashes = parse_sheet_key_hashes(load_binary_fixture("stringtable.bss"), {label.sheet for label in labels})
    wrong = {
        label.key: (label.key_hash, hashes.get(label.sheet, {}).get(label.key))
        for label in labels
        if hashes.get(label.sheet, {}).get(label.key) != label.key_hash
    }
    assert not wrong, f"slot label hashes differ from stringtable.bss (stored, file): {wrong}"


def test_life_gear_types_have_a_label(itemenchant_result: HandlerResult) -> None:
    """A Life Skill gear type the client adds shows no slot until it gets a label."""
    from _dbss.itemenchant.life_slots import LIFE_SLOT_LABELS, NO_LIFE_EQUIP_TYPE

    stored = {record["life_equip_type"] for record in itemenchant_result.records}
    unlabelled = stored - set(LIFE_SLOT_LABELS) - {NO_LIFE_EQUIP_TYPE}
    assert not unlabelled, f"life_equip_type values without a label: {sorted(unlabelled)}"


def test_only_life_gear_has_a_life_skill_tab(itemenchant_result: HandlerResult) -> None:
    """Items that are not Life Skill gear store the "any tab" restrict type."""
    from _dbss.itemenchant.life_slots import NO_LIFE_EQUIP_TYPE

    any_tab = 15
    bad = [
        record["item_id"]
        for record in itemenchant_result.records
        if record["life_equip_type"] == NO_LIFE_EQUIP_TYPE and record["life_restrict_type"] != any_tab
    ]
    assert not bad, f"items with no life gear type but a Life Skill tab: {bad[:5]}"


def test_servant_gear_slots_have_a_label_in_their_group(itemenchant_result: HandlerResult) -> None:
    """A servant group's slot the client adds shows as a bare number until it gets a label."""
    from _dbss.itemenchant.servant_slots import SERVANT_SLOT_LABELS, servant_group
    from _dbss.itemenchant.slot_labels import NO_SLOT

    unlabelled = {
        (group, record["equip_slot"])
        for record in itemenchant_result.records
        if record["servant_kinds"] and record["equip_slot"] != NO_SLOT
        and (group := servant_group(record["servant_kinds"])) is not None
        and record["equip_slot"] not in SERVANT_SLOT_LABELS[group]
    }
    assert not unlabelled, f"servant (group, equip_slot) pairs without a label: {sorted(unlabelled)}"


def test_only_servant_gear_has_servant_kinds(itemenchant_result: HandlerResult) -> None:
    """Gear a class can wear never names a servant, and gear no class can wear always does."""
    from _dbss.itemenchant.slot_labels import NO_SLOT

    equipment = [r for r in itemenchant_result.records if r["equip_slot"] != NO_SLOT]
    both = [r["item_id"] for r in equipment if r["class_mask"] and r["servant_kinds"]]
    neither = [r["item_id"] for r in equipment if not r["class_mask"] and not r["servant_kinds"]]
    assert not both, f"gear with classes and servant kinds: {both[:5]}"
    assert not neither, f"gear with neither classes nor servant kinds: {neither[:5]}"


def test_icon_paths_use_forward_slashes(itemenchant_result: HandlerResult) -> None:
    """A few blocks store backslashes (Essence of Dawn Box); the parser turns them into slashes."""
    bad = [r["item_id"] for r in itemenchant_result.records if "\\" in r["icon_path"] or "//" in r["icon_path"]]
    assert not bad, f"icon paths with a backslash or doubled slash: {bad[:5]}"


def test_every_stored_slot_has_a_label(itemenchant_result: HandlerResult) -> None:
    """A slot the client adds shows as a bare number until it gets a label."""
    from _dbss.itemenchant.slot_labels import NO_SLOT, SLOT_LABELS

    unlabelled = {r["equip_slot"] for r in itemenchant_result.records} - set(SLOT_LABELS) - {NO_SLOT}
    assert not unlabelled, f"equip_slot values without a label: {sorted(unlabelled)}"
    assert all(record["slot"] for record in itemenchant_result.records if record["equip_slot"] != NO_SLOT)


def test_item_grade_index_matches_the_grade_column(itemenchant_result: HandlerResult) -> None:
    from _dbss.itemenchant.parser import build_item_grade_index

    source = itemenchant_result.source
    index = build_item_grade_index(source.data, source.file(_OFFSET_FILE))

    assert index == {r["item_id"]: r["grade"] for r in itemenchant_result.records}


def test_enchant_key_item_index_matches_the_enchant_key_column(itemenchant_result: HandlerResult) -> None:
    """IndexKind.ENCHANT_KEY_ITEMS is this table's Enchant Key column turned around."""
    from _dbss.itemenchant.parser import build_enchant_key_item_index

    source = itemenchant_result.source
    index = build_enchant_key_item_index(source.data, source.file(_OFFSET_FILE))
    expected: dict[int, list[int]] = {}
    for record in itemenchant_result.records:
        if record["enchant_key"]:
            expected.setdefault(record["enchant_key"], []).append(record["item_id"])

    assert index == {key: tuple(sorted(items)) for key, items in expected.items()}
    assert _KZARKA_GAUNTLET in index[_KZARKA_GAUNTLET_ENCHANT_KEY]


def test_enhancement_type_item_index_matches_the_enhancement_type_column(
    itemenchant_result: HandlerResult,
) -> None:
    """IndexKind.ENHANCEMENT_TYPE_ITEMS is this table's Enhancement Type column turned around."""
    from _dbss.itemenchant.parser import build_enhancement_type_item_index

    source = itemenchant_result.source
    index = build_enhancement_type_item_index(source.data, source.file(_OFFSET_FILE))
    expected: dict[int, list[int]] = {}
    for record in itemenchant_result.records:
        if record["enhancement_type"]:
            expected.setdefault(record["enhancement_type"], []).append(record["item_id"])

    assert index == {key: tuple(sorted(items)) for key, items in expected.items()}
    assert _BLACKSTAR_LONGSWORD in index[_BLACKSTAR]


@pytest.mark.parametrize(
    ("event_type", "builder", "item_id", "param1"),
    [
        (_MARBLE_DICE, "build_marble_dice_group_item_index", _PACE_OF_DELIGHT_1, _PACE_OF_DELIGHT_1_GROUP),
        (_CUSTOMIZED_ITEM_BOX, "build_customized_item_box_index", _MYSTERIOUS_SECRET_NOTE, _SECRET_NOTE_BOX_KEY),
    ],
    ids=["marble_dice_group_items", "customized_item_boxes"],
)
def test_contents_event_item_index_matches_the_contents_event_columns(
    itemenchant_result: HandlerResult,
    event_type: int,
    builder: str,
    item_id: int,
    param1: int,
) -> None:
    """MARBLE_DICE_GROUP_ITEMS and CUSTOMIZED_ITEM_BOXES are Event Param 1 of their event's items turned around."""
    from _dbss.itemenchant import parser

    source = itemenchant_result.source
    index = getattr(parser, builder)(source.data, source.file(_OFFSET_FILE))
    expected: dict[int, list[int]] = {}
    for record in itemenchant_result.records:
        if record["contents_event_type"] == event_type:
            # The view shows a param1 of 0 as empty (None); the index keeps the stored 0.
            expected.setdefault(record["contents_event_param1"] or 0, []).append(record["item_id"])

    assert index == {key: tuple(sorted(items)) for key, items in expected.items()}
    assert item_id in index[param1]


def test_mesh_key_item_index_links_a_mesh_to_the_items_that_wear_it(itemenchant_result: HandlerResult) -> None:
    """MESH_KEY_ITEMS turns the class entries around: Blackstar Longsword wears the itemeffectchange.dbss sword mesh."""
    from _dbss.itemeffectchange.parser import FILE_NAME as EFFECT_CHANGE_FILE, parse_itemeffectchange_records
    from _dbss.itemenchant.parser import build_mesh_key_item_index
    from tests.fixtures import load_binary_fixture

    source = itemenchant_result.source
    index = build_mesh_key_item_index(source.data, source.file(_OFFSET_FILE))
    item_ids = {r["item_id"] for r in itemenchant_result.records}
    mesh_keys = {r["mesh_key"] for r in parse_itemeffectchange_records(load_binary_fixture(EFFECT_CHANGE_FILE))}

    assert _BLACKSTAR_LONGSWORD in index[_BLACKSTAR_SWORD_MESH]
    assert mesh_keys & set(index)
    assert all(items and set(items) <= item_ids for items in index.values())


def test_customized_item_box_param1_links_to_its_record() -> None:
    """Event Param 1 of a CustomizedItemBox item opens its customizeditem.dbss row."""
    from _dbss.itemenchant.handler import _contents_event_param1_cell

    cell = _contents_event_param1_cell(
        {"contents_event_type": _CUSTOMIZED_ITEM_BOX, "contents_event_param1": _SECRET_NOTE_BOX_KEY}
    )

    assert 'data-action="open-record"' in cell
    assert 'data-path="gamecommondata/binary/customizeditem.dbss"' in cell
    assert f'data-value="{_SECRET_NOTE_BOX_KEY}"' in cell


def test_itemmaxlevel_holds_the_max_level_of_every_item_with_an_enchant_key(
    itemenchant_result: HandlerResult,
) -> None:
    """itemmaxlevel.dbss is this table's Max Level column, for the items with enhancement data."""
    from _dbss.itemmaxlevel.parser import FILE_NAME as MAX_LEVEL_FILE, parse_itemmaxlevel_records
    from tests.fixtures import load_binary_fixture

    max_levels = parse_itemmaxlevel_records(load_binary_fixture(MAX_LEVEL_FILE))
    expected = {r["item_id"]: r["max_enchant_level"] for r in itemenchant_result.records if r["enchant_key"]}

    assert {r["item_id"]: r["max_enchant_level"] for r in max_levels} == expected


def test_build_item_icon_index_covers_the_furniture_case() -> None:
    """The index is what lets an item ID reach an asset-named icon."""
    from _dbss.itemenchant.parser import build_item_icon_index
    from tests.fixtures import ensure_fixtures

    paths = ensure_fixtures(CASE)
    index = build_item_icon_index(
        paths["itemenchant.dbss"].read_bytes(),
        paths["itemenchantoffset.dbss"].read_bytes(),
    )

    # One entry per level-0 record, not one per enchant level.
    base_items = _base_item_count(paths[_OFFSET_FILE].read_bytes())
    assert len(index) == base_items
    assert index[_KING_CLAM] == (
        f"{_ICON_ROOT}/03_etc/06_housing/"
        "inhouse_cultivate_sea_clam_01_wall.dds"
    )
    # Every path stays inside the icon tree.
    assert all(p.startswith("ui_texture/icon/") for p in index.values())


def test_build_character_item_index_links_placed_objects_and_pets() -> None:
    from _dbss.itemenchant.parser import build_character_item_index
    from tests.fixtures import ensure_fixtures

    paths = ensure_fixtures(CASE)
    index = build_character_item_index(
        paths["itemenchant.dbss"].read_bytes(),
        paths["itemenchantoffset.dbss"].read_bytes(),
    )

    # A kept character is named by exactly one item, so no item appears twice.
    assert len(set(index.values())) == len(index)
    assert 0 not in index
    assert index[_EVENT_FENCE_CHARACTER] == _EVENT_FENCE
    # [Pet] Striped Cat (Tier 3) summons character 9425, "Cat".
    assert index[9425] == 860014
    # Servant gear read without its `unknown_5d` entries once named character 1.
    assert 1 not in index


def test_build_buff_item_index_links_buffs_to_their_items() -> None:
    from _dbss.itemenchant.parser import build_buff_item_index
    from tests.fixtures import ensure_fixtures

    # The index spec's sources: this table and skill.dbss.
    skill_files = {name: name for name in ("skill.dbss", "skilloffset.dbss")}
    paths = ensure_fixtures(replace(CASE, companion_files={**CASE.companion_files, **skill_files}))
    index = build_buff_item_index(
        paths["itemenchant.dbss"].read_bytes(),
        paths[_OFFSET_FILE].read_bytes(),
        paths["skill.dbss"].read_bytes(),
        paths["skilloffset.dbss"].read_bytes(),
    )

    for buff_id in _BOON_BUFFS:
        assert _BOON_ITEM in index[buff_id]
    # Item IDs are kept once each, in ascending order.
    assert all(list(items) == sorted(set(items)) for items in index.values())


def test_item_grade_tagged_wraps_the_name_in_its_grade_colour() -> None:
    assert item_grade_tagged("Kzarka Longsword", 3) == "<PAColor0xFFF5BA3A>Kzarka Longsword<PAOldColor>"
    # An unknown grade or a missing name stays plain.
    assert item_grade_tagged("Kzarka Longsword", len(ITEM_GRADE_COLORS)) == "Kzarka Longsword"
    assert item_grade_tagged("", 3) == ""


def test_time_limit_shows_only_on_items_that_expire(itemenchant_result: HandlerResult) -> None:
    from _dbss.itemenchant.handler import _time_limit_text

    # The 3-day coupon and the 180-day Arsha of itemenchant_dbss.md.
    assert (_time_limit_text(4_320), _time_limit_text(259_200), _time_limit_text(None)) == ("72h", "4320h", "")
    bad = [r["item_id"] for r in itemenchant_result.records if bool(r["time_limit"]) != (r["expiration_minutes"] is not None)]
    assert not bad, f"items whose time limit text and minutes disagree: {bad[:5]}"


def test_item_name_kr_index_matches_the_korean_name_column(itemenchant_result: HandlerResult) -> None:
    from _dbss.itemenchant.parser import build_item_name_kr_index

    source = itemenchant_result.source
    index = build_item_name_kr_index(source.data, source.file(_OFFSET_FILE))
    expected = {r["item_id"]: r["name_kr"].strip() for r in itemenchant_result.records if r["name_kr"].strip()}

    assert index == expected
