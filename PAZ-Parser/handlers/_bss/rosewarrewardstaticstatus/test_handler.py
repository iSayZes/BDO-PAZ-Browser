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

from .parser import REWARD_LISTS, parse_reward_rows


_U32 = struct.Struct("<I")
_ROW_COUNT_AT = 4
_ROWS_AT = 8
_TABLE_START_AT = -8
# Four u64 list counts and the u8 is_guild per row; 16 bytes per reward.
_ROW_FIXED_SIZE = 4 * 8 + 1
_REWARD_SIZE = 16


def _declared_rewards(source: CaseInput) -> int:
    """The rewards the sizes leave room for: the bytes between the header and
    the string table, less the fixed part of each row, in 16-byte rewards."""
    (row_count,) = _U32.unpack_from(source.data, _ROW_COUNT_AT)
    (table_start,) = _U32.unpack_from(source.data, len(source.data) + _TABLE_START_AT)
    return (table_start - _ROWS_AT - row_count * _ROW_FIXED_SIZE) // _REWARD_SIZE


CASE = HandlerCase(
    handler_name="rosewarrewardstaticstatus.bss",
    data_file="rosewarrewardstaticstatus.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path="gamecommondata/binary/rosewarrewardstaticstatus.bss",
    tests=[
        SchemaTest(
            required_keys=["is_guild", "reward_list", "item_id", "unknown_04", "count", "result", "icon_path", "item_name"],
        ),
        DeclaredCountTest(declared=_declared_rewards),
        RangeTest(col="is_guild", min_val=0, max_val=1),
        # The reward boxes name the war result and who gets them in their LOC text.
        TargetTest(
            col="item_id",
            value=790792,
            expected={"item_name": "Flourishing Victory Reward", "reward_list": "win_rewards", "is_guild": 1},
        ),
        TargetTest(
            col="item_id",
            value=790797,
            expected={"item_name": "Blossoming Resolve Reward", "reward_list": "lose_rewards", "is_guild": 0},
        ),
        TargetTest(
            col="item_id",
            value=790796,
            expected={"item_name": "Blossoming Battle Reward", "reward_list": "draw_rewards", "result": "Liberation"},
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
def test_rosewarrewardstaticstatus_bss(spec: Any, reward_result: HandlerResult) -> None:
    reward_result.check(spec)


def test_one_row_without_and_one_with_a_guild(reward_result: HandlerResult) -> None:
    rows = parse_reward_rows(reward_result.source.data)
    assert sorted(row["is_guild"] for row in rows) == [0, 1]


def test_the_fourth_list_has_no_result(reward_result: HandlerResult) -> None:
    for record in reward_result.records:
        assert (record["result"] is None) == (record["reward_list"] == REWARD_LISTS[-1])


def _pabr(values: bytes) -> bytes:
    table_start = _ROWS_AT - 4 + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_rows_read_four_lists_and_the_guild_flag() -> None:
    reward = struct.pack("<I4sQ", 7, b"\xfc\x7f\x00\x00", 3)
    row = struct.pack("<Q", 1) + reward + struct.pack("<QQQ", 0, 0, 0) + b"\x01"
    (parsed,) = parse_reward_rows(_pabr(_U32.pack(1) + row))
    assert parsed["win_rewards"] == [{"item_id": 7, "unknown_04": "fc 7f 00 00", "count": 3}]
    assert parsed["is_guild"] == 1


def test_a_reward_count_past_the_string_table_raises() -> None:
    row = struct.pack("<Q", 5) + bytes(16)
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_reward_rows(_pabr(_U32.pack(1) + row))


def test_rows_that_stop_short_of_the_string_table_raise() -> None:
    row = struct.pack("<QQQQ", 0, 0, 0, 0) + b"\x00" + b"\x00"
    with pytest.raises(ValueError, match="string table starts"):
        parse_reward_rows(_pabr(_U32.pack(1) + row))
