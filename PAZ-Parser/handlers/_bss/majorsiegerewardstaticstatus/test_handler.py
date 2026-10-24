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
    SchemaTest,
    case_id,
    run_case,
)

from .parser import BOOTY_LIST, REWARD_LISTS, ROW_ITEM_FIELDS, parse_major_siege_rewards


_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
_ROW_COUNT_AT = 4
_ROWS_AT = 8
_REWARD_SIZE = 16
# u8 unknown_00 before the lists, four u32 after them.
_ROW_HEAD = 1
_ROW_TAIL = 16
_BOOTY_HEAD = struct.Struct("<HQ")


def _declared_items(source: CaseInput) -> int:
    """Every list count of every row, the three item IDs per row and every booty list count."""
    data = source.data
    (row_count,) = _U32.unpack_from(data, _ROW_COUNT_AT)
    offset = _ROWS_AT
    total = 0
    for _ in range(row_count):
        offset += _ROW_HEAD
        for _ in REWARD_LISTS:
            (count,) = _U64.unpack_from(data, offset)
            offset += _U64.size + count * _REWARD_SIZE
            total += count
        offset += _ROW_TAIL
        total += len(ROW_ITEM_FIELDS)
    (booty_count,) = _U32.unpack_from(data, offset)
    offset += _U32.size
    for _ in range(booty_count):
        _territory_key, item_count = _BOOTY_HEAD.unpack_from(data, offset)
        offset += _BOOTY_HEAD.size + item_count * _U32.size
        total += item_count
    return total


CASE = HandlerCase(
    handler_name="majorsiegerewardstaticstatus.bss",
    data_file="majorsiegerewardstaticstatus.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path="gamecommondata/binary/majorsiegerewardstaticstatus.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "unknown_00",
                "unknown_plus_item_rewards_00",
                "territory_key",
                "territory_name",
                "reward_list",
                "item_id",
                "unknown_04",
                "count",
                "reward",
                "icon_path",
                "item_name",
            ],
        ),
        DeclaredCountTest(declared=_declared_items),
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
def test_majorsiegerewardstaticstatus_bss(spec: Any, reward_result: HandlerResult) -> None:
    reward_result.check(spec)


def test_every_item_has_a_name(reward_result: HandlerResult) -> None:
    for record in reward_result.records:
        assert record["item_name"], record


def test_each_row_has_its_own_u8(reward_result: HandlerResult) -> None:
    rows, _booty = parse_major_siege_rewards(reward_result.source.data)
    keys = [row["unknown_00"] for row in rows]
    assert keys and len(keys) == len(set(keys))


def test_each_territory_has_one_booty_list(reward_result: HandlerResult) -> None:
    _rows, booty = parse_major_siege_rewards(reward_result.source.data)
    keys = [entry["territory_key"] for entry in booty]
    assert keys and len(keys) == len(set(keys))


def test_every_booty_territory_has_a_name(reward_result: HandlerResult) -> None:
    for record in reward_result.records:
        if record["reward_list"] == BOOTY_LIST:
            assert record["territory_name"], record


def test_only_booty_items_have_a_territory(reward_result: HandlerResult) -> None:
    for record in reward_result.records:
        assert (record["territory_key"] is not None) == (record["reward_list"] == BOOTY_LIST), record


def _pabr(values: bytes) -> bytes:
    table_start = _ROWS_AT - _U32.size + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def _row(first_list: bytes) -> bytes:
    empty_lists = _U64.pack(0) * (len(REWARD_LISTS) - 1)
    return struct.pack("<B", 5) + first_list + empty_lists + struct.pack("<4I", 7, 11, 12, 13)


def test_a_row_reads_its_lists_and_item_ids() -> None:
    reward = struct.pack("<I4sQ", 3, b"\xa4\x00\x00\x00", 2)
    booty = _U32.pack(1) + _BOOTY_HEAD.pack(0, 2) + struct.pack("<2I", 21, 22)
    rows, parsed_booty = parse_major_siege_rewards(_pabr(_U32.pack(1) + _row(_U64.pack(1) + reward) + booty))
    (row,) = rows
    assert row[REWARD_LISTS[0]] == [{"item_id": 3, "unknown_04": "a4 00 00 00", "count": 2}]
    assert row["unknown_plus_item_rewards_00"] == 7
    assert [row[name] for name in ROW_ITEM_FIELDS] == [11, 12, 13]
    assert parsed_booty == [{"territory_key": 0, "item_ids": [21, 22]}]


def test_a_booty_count_past_the_string_table_raises() -> None:
    booty = _U32.pack(1) + _BOOTY_HEAD.pack(0, 9)
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_major_siege_rewards(_pabr(_U32.pack(1) + _row(_U64.pack(0)) + booty))


def test_booty_lists_that_stop_short_of_the_string_table_raise() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_major_siege_rewards(_pabr(_U32.pack(1) + _row(_U64.pack(0)) + _U32.pack(0) + b"\x00"))
