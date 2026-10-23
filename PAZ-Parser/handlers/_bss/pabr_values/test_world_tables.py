"""Checks of the monster and world tables in `world_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

from tests.fixtures import load_binary_fixture

from .abyssone_tables import ABYSS_ONE_TABLES
from .parser import parse_value_table
from .world_names import item_key_entry_text, reward_entry_text
from .world_tables import WORLD_TABLES


_TABLES = {value_table.file_name: value_table for value_table in (*WORLD_TABLES, *ABYSS_ONE_TABLES)}
_MONSTER_MANAGER = "monstermanager.bss"
_MONSTER_SELF_MANAGER = "monsterselfmanager.bss"
_BATCH_SUMMON = "bdobatchsummonmonsterss.bss"
_BLOOD_ALTAR = "bloodaltar.bss"
_TREASURE = "treasureinfostaicstatusmanager.bss"
_MAGNUS_TELEPORT = "magnuseasyteleport.bss"
_MAGNUS_MOVE_COST = "abyssmovecost.bss"
_REUSE_GROUP = "reusegroup.bss"
_LEVEL_SHIFT = 24
_FLAG_VALUES = {0, 1}
_TREASURE_DESC_PREFIX = "LUA_TREASURE_GUIDEBOOK_ITEMDESC_"
# abyssmovecost.bss move entry: cost, region key 1, region key 2.
_MOVE_REGION_1 = 1
# An item ID with no LOC name.
_UNNAMED_ITEM = 16_777_215


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def _unique(values: list[object]) -> bool:
    return bool(values) and len(values) == len(set(values))


def test_every_monster_is_listed_once() -> None:
    for name in (_MONSTER_MANAGER, _MONSTER_SELF_MANAGER):
        assert _unique([record["character_key"] for record in _records(name)]), name


def test_each_summon_key_packs_its_level_and_item() -> None:
    records = _records(_BATCH_SUMMON)
    for record in records:
        assert record["summon_key"] == record["summon_level"] << _LEVEL_SHIFT | record["item_key"], record
    assert _unique([record["summon_key"] for record in records])


def test_blood_altar_stage_keys_follow_the_row_order() -> None:
    # The stage menu Lua passes index + 1 as the stage key.
    keys = [record["stage_key"] for record in _records(_BLOOD_ALTAR)]
    assert keys == list(range(1, len(keys) + 1))


def test_every_blood_altar_stage_has_both_reward_lists() -> None:
    for record in _records(_BLOOD_ALTAR):
        assert record["first_rewards"] and record["weekly_rewards"], record


def test_every_treasure_is_listed_once() -> None:
    assert _unique([record["item_enchant_key"] for record in _records(_TREASURE)])


def test_every_treasure_description_is_a_guidebook_key() -> None:
    for record in _records(_TREASURE):
        assert record["desc_key"].startswith(_TREASURE_DESC_PREFIX), record
        assert record["is_hunting"] in _FLAG_VALUES, record


def test_every_teleport_waypoint_is_listed_once() -> None:
    assert _unique([record["waypoint_key"] for record in _records(_MAGNUS_TELEPORT)])


def test_teleport_regions_are_the_magnus_move_regions() -> None:
    teleport_regions = {record["region_key"] for record in _records(_MAGNUS_TELEPORT)}
    move_regions = {record["moves"][0][_MOVE_REGION_1] for record in _records(_MAGNUS_MOVE_COST)}
    assert teleport_regions == move_regions


def test_every_reuse_group_is_listed_once_with_a_flag() -> None:
    records = _records(_REUSE_GROUP)
    assert _unique([record["reuse_group"] for record in records])
    assert {record["is_expired_in_offline"] for record in records} <= _FLAG_VALUES


def test_a_reward_entry_shows_its_count() -> None:
    assert reward_entry_text([_UNNAMED_ITEM, "f6 7f 00 00", 3]).endswith(" x3")


def test_an_unnamed_core_material_shows_its_key_once() -> None:
    assert item_key_entry_text(_UNNAMED_ITEM) == str(_UNNAMED_ITEM)
