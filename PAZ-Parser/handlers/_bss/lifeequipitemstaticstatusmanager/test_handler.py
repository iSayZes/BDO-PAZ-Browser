from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.fixtures import load_binary_fixture
from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, RangeTest, SchemaTest, UserLanguageTest, case_id, run_case

from _dbss.lifeexp.labels import LIFE_SKILLS
from .parser import FILE_NAME, parse_life_equip_records, parse_life_stat_lists


_U32 = struct.Struct("<I")
_LISTS_START = 4
_TRAILER_SIZE = 8
# `__ePlayerLifeStatType_Count`, the "any tab" value of `itemenchant.dbss` `life_restrict_type`.
_LIFE_STAT_TYPE_COUNT = 15
# The Life Skill tabs `0` Collecting to `9` Sail (panel_window_equipment_all_4.luac, `_lifeSlotPerType`).
_TAB_COUNT = 10
_FISHING = 1
_SAIL = 9
# buff.dbss effect types: life EXP gain, the Life Skill mastery, Auto-fishing Time and Sailor EXP.
_EXPERIENCE_RATE = 25
_LIFE_MASTERY = 149
_AUTO_FISHING_TIME = 121
_SAILOR_EXP = 19
_MAX_EFFECT_TYPE = 0xFF


def _declared_effect_types(source: CaseInput) -> int:
    """The effect types the list counts declare between the magic and the string table."""
    data = source.data
    (table_start,) = _U32.unpack_from(data, len(data) - _TRAILER_SIZE)
    pos, total = _LISTS_START, 0
    while pos < table_start:
        (count,) = _U32.unpack_from(data, pos)
        pos += _U32.size + count
        total += count
    return total


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["life_skill_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["life_stat_type", "effect_index", "effect_type", "life_skill_name", "effect_type_name"]),
        DeclaredCountTest(declared=_declared_effect_types),
        RangeTest(col="life_stat_type", min_val=0, max_val=_LIFE_STAT_TYPE_COUNT - 1),
        RangeTest(col="effect_type", min_val=0, max_val=_MAX_EFFECT_TYPE),
        UserLanguageTest(fields=["life_skill_name"]),
    ],
)


@pytest.fixture(scope="module")
def life_equip_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_lifeequipitemstaticstatusmanager(spec: Any, life_equip_result: HandlerResult) -> None:
    life_equip_result.check(spec)


def test_there_is_a_list_for_every_life_stat_type() -> None:
    lists = parse_life_stat_lists(load_binary_fixture(FILE_NAME))
    assert len(lists) == _LIFE_STAT_TYPE_COUNT == len(LIFE_SKILLS)


def test_every_life_skill_tab_counts_exp_and_mastery() -> None:
    lists = parse_life_stat_lists(load_binary_fixture(FILE_NAME))
    for tab in range(_TAB_COUNT):
        assert {_EXPERIENCE_RATE, _LIFE_MASTERY} <= set(lists[tab]), tab
    assert all(not effect_types for effect_types in lists[_TAB_COUNT:])


def test_the_fishing_and_sail_tabs_keep_their_own_effects() -> None:
    lists = parse_life_stat_lists(load_binary_fixture(FILE_NAME))
    assert _AUTO_FISHING_TIME in lists[_FISHING]
    assert _SAILOR_EXP in lists[_SAIL]
    others = [effect_types for tab, effect_types in enumerate(lists) if tab not in (_FISHING, _SAIL)]
    assert all(_AUTO_FISHING_TIME not in effect_types and _SAILOR_EXP not in effect_types for effect_types in others)


def test_each_list_is_sorted() -> None:
    for effect_types in parse_life_stat_lists(load_binary_fixture(FILE_NAME)):
        assert effect_types == sorted(effect_types)


def _pabr(values: bytes) -> bytes:
    table_start = _LISTS_START + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_an_empty_list_keeps_the_next_life_stat_type() -> None:
    data = _pabr(_U32.pack(0) + _U32.pack(2) + bytes([_EXPERIENCE_RATE, _LIFE_MASTERY]))
    assert parse_life_equip_records(data) == [
        {"life_stat_type": 1, "effect_index": 0, "effect_type": _EXPERIENCE_RATE},
        {"life_stat_type": 1, "effect_index": 1, "effect_type": _LIFE_MASTERY},
    ]


def test_a_count_past_the_string_table_raises() -> None:
    with pytest.raises(ValueError, match="runs past"):
        parse_life_equip_records(_pabr(_U32.pack(3) + bytes([_EXPERIENCE_RATE])))
