from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _dbss.cashproduct.parser import parse_cashproductoffset_records
from .parser import FILE_NAME, OFFSET_FILE, PRODUCT_SLOTS, parse_cashchoose_records, parse_cashchooseoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# Key 1 is the pick-3-of-6 pet pack (Desert Fox 1052, Long-tailed Rosefinch
# 1043, ...); the same row on clients 1784 and 3482 and in the client 1784
# ChooseCashProduct_Table sheet.
_PET_PACK = 1
_PET_PACK_PRODUCTS = [1052, 1043, 1031, 1033, 1030, 1029, 0, 0, 0, 0]

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["products_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "choose_key", "choose_count", "is_choose_duplicate", "include_product_no", "stack_count",
                "display_icon_path", "choose_cash_count", "icon_path", "products_text",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="is_choose_duplicate", min_val=0, max_val=1),
        RangeTest(col="choose_cash_count", min_val=0, max_val=PRODUCT_SLOTS),
        TargetTest(
            col="choose_key",
            value=_PET_PACK,
            expected={"include_product_no": _PET_PACK_PRODUCTS, "display_icon_path": ""},
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["choose_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def cashchoose_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_cashchoose_dbss(spec: Any, cashchoose_result: HandlerResult) -> None:
    cashchoose_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_cashchooseoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_each_pack() -> None:
    rows = parse_cashchooseoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"))
    assert not problems, problems


def test_products_fill_the_first_slots_and_match_the_count() -> None:
    wrong = []
    for record in parse_cashchoose_records(load_binary_fixture(FILE_NAME)):
        filled = [bool(product_no) for product_no in record["include_product_no"]]
        stacked = [bool(stack) for stack in record["stack_count"]]
        count = record["choose_cash_count"]
        if filled != stacked or filled != [slot < count for slot in range(PRODUCT_SLOTS)]:
            wrong.append(record["choose_key"])
    assert not wrong, wrong[:10]


def test_every_listed_product_is_a_cash_product() -> None:
    products = {row["product_id"] for row in parse_cashproductoffset_records(load_binary_fixture("cashproductoffset.dbss"))}
    missing = [
        (record["choose_key"], product_no)
        for record in parse_cashchoose_records(load_binary_fixture(FILE_NAME))
        for product_no in record["include_product_no"]
        if product_no and product_no not in products
    ]
    assert not missing, missing[:10]


def _row(key: int, icon: str, products: list[int]) -> bytes:
    slots = products + [0] * (PRODUCT_SLOTS - len(products))
    stacks = [1 if product_no else 0 for product_no in slots]
    return (
        struct.pack("<HIB", key, 2, 1)
        + struct.pack(f"<{PRODUCT_SLOTS}I", *slots)
        + struct.pack(f"<{PRODUCT_SLOTS}Q", *stacks)
        + struct.pack("<Q", len(icon)) + icon.encode("ascii")
        + struct.pack("<I", len(products))
    )


def test_parse_reads_two_packs() -> None:
    icon = "New_Icon/09_Cash/00021005.dds"
    data = struct.pack("<I", 2) + _row(7, "", [500, 501, 502]) + _row(8, icon, [600, 601])

    first, second = parse_cashchoose_records(data)

    assert first["choose_key"] == 7
    assert first["choose_count"] == 2
    assert first["is_choose_duplicate"] == 1
    assert first["include_product_no"][:4] == [500, 501, 502, 0]
    assert first["stack_count"][:4] == [1, 1, 1, 0]
    assert first["display_icon_path"] == ""
    assert first["choose_cash_count"] == 3
    assert second["display_icon_path"] == icon
    assert second["choose_cash_count"] == 2


def test_parse_rejects_a_truncated_row() -> None:
    data = struct.pack("<I", 1) + _row(1, "", [500])[:-2]

    with pytest.raises(ValueError):
        parse_cashchoose_records(data)
