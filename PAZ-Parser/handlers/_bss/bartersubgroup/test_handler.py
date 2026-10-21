from __future__ import annotations

from dataclasses import replace
from itertools import groupby
from typing import Any

import pytest

from _common.binary import u32
from tests.fixtures import load_binary_fixture
from tests.framework import (
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _bss.barter.group_lists import GROUP_COUNT_OFFSET
from .parser import ENTRY_SIZE, FILE_NAME, parse_bartersubgroup_records

# A u32 category mask; categories run 1 to 10 on client 3474.
_MAX_CATEGORY_MASK = 0xFFFFFFFF
_U32_SIZE = 4

CASE = HandlerCase(
    handler_name="bartersubgroup.bss",
    data_file="bartersubgroup.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Item Given", "Item Received", "Category"],
    internal_path="gamecommondata/binary/bartersubgroup.bss",
    tests=[
        SchemaTest(required_keys=[
            "barter_sub_group", "is_material", "select_rate", "barter_cost", "from_item_key",
            "from_min_count", "from_max_count", "to_item_key", "to_min_count", "to_max_count",
            "barter_need_point", "exchange_max_count", "exchange_min", "exchange_max",
            "barter_category", "from_item", "to_item", "category_names", "sub_group_ref",
        ]),
        RangeTest(col="barter_category", min_val=0, max_val=_MAX_CATEGORY_MASK),
        # Item 10 is Crow Coin.
        TargetTest(col="to_item_key", value=10, expected={"to_item": "Crow Coin"}),
    ],
)


@pytest.fixture(scope="module")
def bartersubgroup_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_bartersubgroup_bss(spec: Any, bartersubgroup_result: HandlerResult) -> None:
    bartersubgroup_result.check(spec)


def _keys_by_list(records: list[dict]) -> dict[bool, list[int]]:
    return {
        is_material: [record["barter_sub_group"] for record in group]
        for is_material, group in groupby(records, key=lambda record: record["is_material"])
    }


def test_both_lists_are_present_trade_items_first(bartersubgroup_result: HandlerResult) -> None:
    assert list(_keys_by_list(bartersubgroup_result.records)) == [False, True]


def test_group_keys_count_the_groups_from_one(bartersubgroup_result: HandlerResult) -> None:
    """Each list's entries carry their group's place in the list, so the keys run 1, 1, 2, ... without gaps."""
    for keys in _keys_by_list(bartersubgroup_result.records).values():
        assert keys[0] == 1
        assert all(later - earlier in (0, 1) for earlier, later in zip(keys, keys[1:]))


def test_trade_item_groups_match_the_declared_group_count(bartersubgroup_result: HandlerResult) -> None:
    declared = u32(load_binary_fixture(FILE_NAME), GROUP_COUNT_OFFSET)
    trade_keys = _keys_by_list(bartersubgroup_result.records)[False]
    assert len(set(trade_keys)) == declared


def test_count_ranges_run_low_to_high(bartersubgroup_result: HandlerResult) -> None:
    for record in bartersubgroup_result.records:
        assert record["from_min_count"] <= record["from_max_count"]
        assert record["to_min_count"] <= record["to_max_count"]


def _file(*lists: list[int], table_start: int | None = None) -> bytes:
    """A file of empty entries: one list per argument, each a list of entry counts."""
    body = b""
    for entry_counts in lists:
        body += len(entry_counts).to_bytes(4, "little")
        for count in entry_counts:
            body += count.to_bytes(4, "little") + bytes(count * ENTRY_SIZE)
    start = 4 + len(body) if table_start is None else table_start
    return b"PABR" + body + (0).to_bytes(4, "little") + start.to_bytes(4, "little") + bytes(4)


def test_a_minimal_file_parses() -> None:
    records = parse_bartersubgroup_records(_file([2], [1]))
    assert [record["is_material"] for record in records] == [False, False, True]


def test_a_missing_material_list_is_rejected() -> None:
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_bartersubgroup_records(_file([1]))


def test_lists_that_miss_the_string_table_are_rejected() -> None:
    data = _file([1], [1])
    with pytest.raises(ValueError, match="string table starts"):
        parse_bartersubgroup_records(_file([1], [1], table_start=len(data) - 12 + _U32_SIZE))
