"""Checks of the fishing tables in `lifeskill_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

from tests.fixtures import load_binary_fixture

from .layout import ValueTable
from .lifeskill_names import discard_grade_text, fishing_level_text
from .lifeskill_tables import LIFE_SKILL_TABLES
from .parser import parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in LIFE_SKILL_TABLES}
_ICE_FISHING = _TABLES["icefisingstaticstatus.bss"]
_DISCARD_FISH = _TABLES["discardfish.bss"]
_REGIONS = "icefisingregionstaticstatus.bss"
# The u16 mini-game group of each icefisingregionstaticstatus.bss row, after its u16 region key.
_REGION_ROW_SIZE = 4
_REGION_GROUP_AT = 2
_PABR_VALUES_START = 4
_TRAILER_SIZE = 8
# The highest discard choice of the auto-fishing window: `4` Yellow (LUA_FISHING_DISCARD_ITEM_GRADE_4).
_MAX_DISCARD_GRADE = 3


def _records(value_table: ValueTable) -> list[dict]:
    return parse_value_table(load_binary_fixture(value_table.file_name), value_table)


def _region_groups() -> set[int]:
    data = load_binary_fixture(_REGIONS)
    table_start = int.from_bytes(data[-_TRAILER_SIZE : -_TRAILER_SIZE + 4], "little")
    return {
        int.from_bytes(data[start + _REGION_GROUP_AT : start + _REGION_ROW_SIZE], "little")
        for start in range(_PABR_VALUES_START, table_start, _REGION_ROW_SIZE)
    }


def test_every_ice_fishing_group_is_unique() -> None:
    groups = [record["mini_game_group"] for record in _records(_ICE_FISHING)]
    assert groups and len(groups) == len(set(groups))


def test_every_ice_fishing_region_has_its_group() -> None:
    groups = {record["mini_game_group"] for record in _records(_ICE_FISHING)}
    assert _region_groups() <= groups


def test_the_ice_fishing_times_are_ordered() -> None:
    for record in _records(_ICE_FISHING):
        assert record["min_wait_time"] <= record["max_wait_time"], record
        assert record["game_min_time"] <= record["game_max_time"], record
        assert record["fish_hp"] > 0, record


def test_each_discard_step_opens_a_higher_grade_at_a_higher_level() -> None:
    records = _records(_DISCARD_FISH)
    assert [record["index"] for record in records] == list(range(1, len(records) + 1))
    levels = [record["fishing_level"] for record in records]
    grades = [record["grade"] for record in records]
    assert levels == sorted(levels) and len(set(levels)) == len(levels)
    assert grades == sorted(grades) and len(set(grades)) == len(grades)
    assert all(0 <= grade <= _MAX_DISCARD_GRADE for grade in grades)


def test_the_discard_cells_fall_back_to_the_number() -> None:
    """A level past the last rank and a grade past the last choice have no text of their own."""
    assert fishing_level_text(999) == "999"
    assert discard_grade_text(99) == "99"
