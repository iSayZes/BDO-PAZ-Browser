from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.item_grade import ITEM_GRADE_COLORS, item_grade_tagged
from _common.lookup_index import IndexKind
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
# King Clam Wall Ornament: furniture, so its icon is named after the 3D asset
# and is unreachable from the item ID alone. It is the case this format solves.
_KING_CLAM = 24626
# [Event] Fence places character 2053, which has no icon of its own.
_EVENT_FENCE = 58011
_EVENT_FENCE_CHARACTER = 2053
_WEAPON = 697192
# Balacs Lunchbox, a yellow (grade 3) item (itemenchant_dbss.md).
_BALACS_LUNCHBOX = 9359
# Kzarka Gauntlet enhances +1 to +15, then PRI to PEN: levels 1-20.
_KZARKA_GAUNTLET = 11210
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
_ARSHA_PURGATUM_180_DAYS = 830533


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
    companion_files={"itemenchantoffset.dbss": "itemenchantoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Item"],
    internal_path="gamecommondata/binary/itemenchant.dbss",
    lookup_indexes={
        IndexKind.SKILL_BUFFS: {_BOON_SKILL_KEY: _BOON_BUFFS},
        IndexKind.LIGHTSTONE_SETS: {_TWISTED_LIGHTSTONE: (_EDANIA_SET,)},
    },
    tests=[
        SchemaTest(
            required_keys=[
                "item_id",
                "name_kr",
                "max_enchant_level",
                "required_level",
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
            expected={"max_enchant_level": _PEN, "item_name": "Kzarka Gauntlet", "name_kr": "크자카 권갑"},
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
        TargetTest(
            col="item_id",
            value=_DANDELION_KAMASYLVEN_SWORD,
            expected={"required_level": 56},
        ),
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


def test_item_grade_index_matches_the_grade_column(itemenchant_result: HandlerResult) -> None:
    from _dbss.itemenchant.parser import build_item_grade_index

    source = itemenchant_result.source
    index = build_item_grade_index(source.data, source.file(_OFFSET_FILE))

    assert index == {r["item_id"]: r["grade"] for r in itemenchant_result.records}


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
    # Named by 120 unrelated items, so it is not a link and is left out.
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
