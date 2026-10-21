from __future__ import annotations

from dataclasses import replace
from itertools import groupby
from typing import Any

import pytest

from _bss.barter.group_lists import GROUP_COUNT_OFFSET
from _bss.barter.sub_group import SUB_GROUP_FILE
from _bss.bartersubgroup.parser import parse_bartersubgroup_records
from _common.binary import u32
from tests.fixtures import load_binary_fixture
from tests.framework import (
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from .parser import ENTRY_SIZE, FILE_NAME, parse_barter_normal_records

_NPCLIST_FILE = "barter_npclist.bss"
# A u32 category mask; categories run 1 to 10 on client 3474.
_MAX_CATEGORY_MASK = 0xFFFFFFFF
_U32_SIZE = 4

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={_NPCLIST_FILE: _NPCLIST_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Region", "NPC", "Item Given", "Item Received", "Category"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "region_key", "is_material", "slot", "barter_region_key", "select_rate", "from_item_key",
            "from_min_count", "from_max_count", "to_item_key", "to_min_count", "to_max_count",
            "barter_need_point", "exchange_max_count", "exchange_min", "exchange_max",
            "barter_sub_group", "barter_category", "region_name", "character_id", "npc_name",
            "from_item", "to_item", "sub_group", "category_names",
        ]),
        RangeTest(col="barter_category", min_val=0, max_val=_MAX_CATEGORY_MASK),
        UserLanguageTest(fields=["region_name", "npc_name", "from_item", "to_item"]),
        # Lema Island and its barter NPC, as in barter_npclist.bss.
        TargetTest(col="region_key", value=181, expected={"region_name": "Lema Island", "character_id": 58954}),
        # Item 10 is Crow Coin.
        TargetTest(col="to_item_key", value=10, expected={"to_item": "Crow Coin"}),
    ],
)


@pytest.fixture(scope="module")
def barter_normal_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_barter_normal_bss(spec: Any, barter_normal_result: HandlerResult) -> None:
    barter_normal_result.check(spec)


def _regions_by_list(records: list[dict]) -> dict[bool, list[int]]:
    """Each list's region keys in file order, one per region."""
    return {
        is_material: [key for key, _ in groupby(record["region_key"] for record in group)]
        for is_material, group in groupby(records, key=lambda record: record["is_material"])
    }


def test_both_lists_are_present_trade_items_first(barter_normal_result: HandlerResult) -> None:
    assert list(_regions_by_list(barter_normal_result.records)) == [False, True]


def test_trade_item_regions_match_the_declared_region_count(barter_normal_result: HandlerResult) -> None:
    declared = u32(load_binary_fixture(FILE_NAME), GROUP_COUNT_OFFSET)
    assert len(_regions_by_list(barter_normal_result.records)[False]) == declared


def test_both_lists_hold_the_npc_list_regions(barter_normal_result: HandlerResult) -> None:
    for keys in _regions_by_list(barter_normal_result.records).values():
        assert len(keys) == len(set(keys))
    for record in barter_normal_result.records:
        assert record["character_id"] is not None, record["region_key"]


def test_every_entry_holds_its_region_key(barter_normal_result: HandlerResult) -> None:
    for record in barter_normal_result.records:
        assert record["barter_region_key"] == record["region_key"]


def test_slots_count_each_region_from_one(barter_normal_result: HandlerResult) -> None:
    for _, group in groupby(barter_normal_result.records, key=lambda r: (r["is_material"], r["region_key"])):
        slots = [record["slot"] for record in group]
        assert slots == list(range(1, len(slots) + 1))


def test_sub_group_entries_leave_the_exchange_empty(barter_normal_result: HandlerResult) -> None:
    for record in barter_normal_result.records:
        if record["barter_sub_group"]:
            assert record["from_item_key"] is None and record["to_item_key"] is None
        else:
            assert record["from_item_key"] and record["to_item_key"]


def test_sub_groups_name_a_group_of_the_same_list(barter_normal_result: HandlerResult) -> None:
    groups = {
        (entry["is_material"], entry["barter_sub_group"])
        for entry in parse_bartersubgroup_records(load_binary_fixture(SUB_GROUP_FILE))
    }
    for record in barter_normal_result.records:
        if record["barter_sub_group"]:
            assert (record["is_material"], record["barter_sub_group"]) in groups


def _file(*lists: list[int], table_start: int | None = None) -> bytes:
    """A file of empty entries: one list per argument, each a list of per-region entry counts."""
    body = b""
    for entry_counts in lists:
        body += len(entry_counts).to_bytes(4, "little")
        for key, count in enumerate(entry_counts, start=1):
            body += key.to_bytes(2, "little") + count.to_bytes(4, "little") + bytes(count * ENTRY_SIZE)
    start = 4 + len(body) if table_start is None else table_start
    return b"PABR" + body + (0).to_bytes(4, "little") + start.to_bytes(4, "little") + bytes(4)


def test_a_minimal_file_parses() -> None:
    records = parse_barter_normal_records(_file([2, 1], [1]))
    assert [(r["is_material"], r["region_key"], r["slot"]) for r in records] == [
        (False, 1, 1), (False, 1, 2), (False, 2, 1), (True, 1, 1),
    ]


def test_a_missing_material_list_is_rejected() -> None:
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_barter_normal_records(_file([1]))


def test_a_region_head_past_the_string_table_is_rejected() -> None:
    data = _file([0], [0])
    # Two regions declared in the first list, but no bytes for their heads.
    data = data[:4] + (2).to_bytes(4, "little") + data[8:]
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_barter_normal_records(data)


def test_lists_that_miss_the_string_table_are_rejected() -> None:
    data = _file([1], [1])
    with pytest.raises(ValueError, match="string table starts"):
        parse_barter_normal_records(_file([1], [1], table_start=len(data) - 12 + _U32_SIZE))
