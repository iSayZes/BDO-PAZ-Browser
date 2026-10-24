from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .parser import REWARD_SET_COUNT, ROW_REWARD_LIST, SET_REWARD_LISTS, parse_reward_rows


_U32 = struct.Struct("<I")
_ROW_COUNT_AT = 4
_ROWS_AT = 8
_TABLE_START_AT = -8
# Per row: the u16 unknown_00, a u64 count per list (five sets of four, then
# one) and the two u32 skill keys; 16 bytes per reward.
_LIST_COUNT = REWARD_SET_COUNT * len(SET_REWARD_LISTS) + 1
_ROW_FIXED_SIZE = 2 + _LIST_COUNT * 8 + 2 * 4
_REWARD_SIZE = 16
# The box of the list after the sets (LOC type 0: Waveworn Resolve Box).
_WAVEWORN_RESOLVE_BOX = 790777


def _declared_rewards(source: CaseInput) -> int:
    """The rewards the sizes leave room for: the bytes between the header and
    the string table, less the fixed part of each row, in 16-byte rewards."""
    (row_count,) = _U32.unpack_from(source.data, _ROW_COUNT_AT)
    (table_start,) = _U32.unpack_from(source.data, len(source.data) + _TABLE_START_AT)
    return (table_start - _ROWS_AT - row_count * _ROW_FIXED_SIZE) // _REWARD_SIZE


CASE = HandlerCase(
    handler_name="oceansiegereward.bss",
    data_file="oceansiegereward.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name", "skill_name_1", "skill_name_2"],
    internal_path="gamecommondata/binary/oceansiegereward.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "unknown_00",
                "reward_set",
                "reward_list",
                "reward_list_number",
                "item_id",
                "unknown_04",
                "count",
                "skill_key_1",
                "skill_key_2",
                "icon_path",
                "item_name",
                "skill_name_1",
                "skill_name_2",
            ],
        ),
        DeclaredCountTest(declared=_declared_rewards),
        RangeTest(col="reward_set", min_val=1, max_val=REWARD_SET_COUNT),
        RangeTest(col="reward_list_number", min_val=1, max_val=len(SET_REWARD_LISTS)),
        TargetTest(
            col="item_id",
            value=_WAVEWORN_RESOLVE_BOX,
            expected={"item_name": "Waveworn Resolve Box", "reward_list": ROW_REWARD_LIST, "reward_set": None},
        ),
    ],
)


@pytest.fixture(scope="module")
def reward_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_oceansiegereward_bss(spec: Any, reward_result: HandlerResult) -> None:
    reward_result.check(spec)


def test_every_item_and_skill_has_a_name(reward_result: HandlerResult) -> None:
    for record in reward_result.records:
        assert record["item_name"] and record["skill_name_1"] and record["skill_name_2"], record


def test_only_the_list_after_the_sets_has_no_set(reward_result: HandlerResult) -> None:
    for record in reward_result.records:
        assert (record["reward_set"] is None) == (record["reward_list"] == ROW_REWARD_LIST), record


def test_each_row_holds_five_sets_of_four_lists(reward_result: HandlerResult) -> None:
    rows = parse_reward_rows(reward_result.source.data)
    assert rows
    for row in rows:
        assert len(row["reward_sets"]) == REWARD_SET_COUNT
        assert all(tuple(reward_set) == SET_REWARD_LISTS for reward_set in row["reward_sets"])


def _pabr(values: bytes) -> bytes:
    table_start = _ROWS_AT - _U32.size + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def _empty_lists(count: int) -> bytes:
    return struct.pack(f"<{count}Q", *([0] * count))


def test_a_row_reads_its_sets_last_list_and_skills() -> None:
    reward = struct.pack("<I4sQ", 7, b"\xa4\x00\x00\x00", 3)
    first_set = struct.pack("<Q", 1) + reward + _empty_lists(len(SET_REWARD_LISTS) - 1)
    other_sets = _empty_lists((REWARD_SET_COUNT - 1) * len(SET_REWARD_LISTS))
    row = struct.pack("<H", 0) + first_set + other_sets + _empty_lists(1) + struct.pack("<II", 11, 12)
    (parsed,) = parse_reward_rows(_pabr(_U32.pack(1) + row))
    assert parsed["reward_sets"][0][SET_REWARD_LISTS[0]] == [{"item_id": 7, "unknown_04": "a4 00 00 00", "count": 3}]
    assert parsed[ROW_REWARD_LIST] == []
    assert (parsed["skill_key_1"], parsed["skill_key_2"]) == (11, 12)


def test_a_reward_count_past_the_string_table_raises() -> None:
    row = struct.pack("<H", 0) + struct.pack("<Q", 5) + bytes(16)
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_reward_rows(_pabr(_U32.pack(1) + row))


def test_rows_that_stop_short_of_the_string_table_raise() -> None:
    row = struct.pack("<H", 0) + _empty_lists(_LIST_COUNT) + struct.pack("<II", 0, 0) + b"\x00"
    with pytest.raises(ValueError, match="string table starts"):
        parse_reward_rows(_pabr(_U32.pack(1) + row))
