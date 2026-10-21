from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from .parser import ROW_SIZE, parse_barter_special_records

# A u32 category mask; categories run 1 to 10 on client 3474.
_MAX_CATEGORY_MASK = 0xFFFFFFFF
_ITEM_ID_MASK = 0x00FFFFFF

CASE = HandlerCase(
    handler_name="barter_special.bss",
    data_file="barter_special.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Item Given", "Item Received"],
    internal_path="gamecommondata/binary/barter_special.bss",
    tests=[
        SchemaTest(required_keys=[
            "index", "barter_region_key", "select_rate", "from_item_key", "from_min_count",
            "from_max_count", "to_item_key", "to_min_count", "to_max_count", "barter_need_point",
            "exchange_max_count", "exchange_min", "exchange_max", "barter_sub_group",
            "barter_category", "from_item", "to_item", "category_names",
        ]),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="barter_category", min_val=0, max_val=_MAX_CATEGORY_MASK),
        # Item 10 is Crow Coin.
        TargetTest(col="to_item_key", value=10, expected={"to_item": "Crow Coin"}),
    ],
)


@pytest.fixture(scope="module")
def barter_special_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_barter_special_bss(spec: Any, barter_special_result: HandlerResult) -> None:
    barter_special_result.check(spec)


def test_index_counts_the_rows_from_one(barter_special_result: HandlerResult) -> None:
    indexes = [record["index"] for record in barter_special_result.records]
    assert indexes == list(range(1, len(indexes) + 1))


def test_count_ranges_run_low_to_high(barter_special_result: HandlerResult) -> None:
    for record in barter_special_result.records:
        assert record["from_min_count"] <= record["from_max_count"]
        assert record["to_min_count"] <= record["to_max_count"]


def test_items_are_item_keys(barter_special_result: HandlerResult) -> None:
    for record in barter_special_result.records:
        assert record["from_item_key"] & _ITEM_ID_MASK
        assert record["to_item_key"] & _ITEM_ID_MASK


def test_rows_that_miss_the_string_table_are_rejected() -> None:
    # PABR, 1 row declared, but the trailer puts the string table right after the header.
    data = b"PABR" + (1).to_bytes(4, "little") + bytes(ROW_SIZE) + (0).to_bytes(4, "little")
    data += (8).to_bytes(4, "little") + bytes(4)
    with pytest.raises(ValueError, match="string table starts"):
        parse_barter_special_records(data)
