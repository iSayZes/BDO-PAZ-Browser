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
    UserLanguageTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _dbss.cashproductcategory.parser import FILE_NAME as CATEGORY_FILE, parse_cashproductcategory_records
from .parser import FILE_NAME, NO_CATEGORY, OFFSET_FILE, parse_coupon_records, parse_couponoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# 1,000,000 = 100%.
_FULL_RATE = 1_000_000
# "할인 쿠폰 10%": key 1 of the client 1784 Coupon_Table sheet, valid in every category.
_FIRST_COUPON = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "category"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "coupon_key", "unknown_02", "max_discount_pearl", "min_product_pearl", "name_kr",
                "expiration_days", "discount_rate", "discount_pearl", "icon_path", "category_expression_kr",
                "category_main", "category_middle", "category_small", "unknown_category_expression_kr_06",
                "name", "category",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="discount_rate", min_val=0, max_val=_FULL_RATE),
        TargetTest(col="coupon_key", value=_FIRST_COUPON, expected={"category_main": NO_CATEGORY}),
        UserLanguageTest(fields=["name", "category"]),
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
        SchemaTest(required_keys=["coupon_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def coupon_result(request: Any) -> HandlerResult:
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
def test_coupon_dbss(spec: Any, coupon_result: HandlerResult) -> None:
    coupon_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_couponoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_each_coupon() -> None:
    rows = parse_couponoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"))
    assert not problems, problems


def _path(main: int, middle: int, small: int) -> tuple[int | None, ...]:
    return tuple(None if key == NO_CATEGORY else key for key in (main, middle, small))


def test_every_coupon_category_is_a_shop_category() -> None:
    categories = {
        (r["main_key"], r["middle_key"], r["small_key"])
        for r in parse_cashproductcategory_records(load_binary_fixture(CATEGORY_FILE))
    }
    missing = [
        (r["coupon_key"], path)
        for r in parse_coupon_records(load_binary_fixture(FILE_NAME))
        if (path := _path(r["category_main"], r["category_middle"], r["category_small"]))[0] is not None
        and path not in categories
    ]
    assert not missing, missing


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def test_parse_reads_one_coupon() -> None:
    row = (
        struct.pack("<HBqq", 7, 2, 1000, 0)
        + _str16("Coupon")
        + struct.pack("<IIq", 14, 300_000, 0)
        + _str16("New_Icon/x.dds")
        + _str16("Cat")
        + struct.pack("<HHHI", 4, 1, NO_CATEGORY, 0)
    )

    (record,) = parse_coupon_records(struct.pack("<I", 1) + row)

    assert record["coupon_key"] == 7
    assert record["max_discount_pearl"] == 1000
    assert record["expiration_days"] == 14
    assert record["discount_rate"] == 300_000
    assert record["icon_path"] == "New_Icon/x.dds"
    assert (record["category_main"], record["category_middle"], record["category_small"]) == (4, 1, NO_CATEGORY)
