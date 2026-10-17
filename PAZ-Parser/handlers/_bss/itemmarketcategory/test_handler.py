from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, LIST_FIELDS, parse_itemmarketcategory_records


_COUNT_OFFSET = 4
_MAIN_WEAPON = 1


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "main_category",
                *LIST_FIELDS,
                "unknown_filter2_values_00",
                "name",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="key", value=_MAIN_WEAPON, expected={"name": "Main Weapon"}),
    ],
)


@pytest.fixture(scope="module")
def market_category_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemmarketcategory_bss(spec: Any, market_category_result: HandlerResult) -> None:
    market_category_result.check(spec)


def test_the_key_is_the_main_category_number(market_category_result: HandlerResult) -> None:
    for r in market_category_result.records:
        assert r["key"] == r["main_category"]["category_no"]


def test_numbers_are_unique_within_each_list(market_category_result: HandlerResult) -> None:
    for r in market_category_result.records:
        for field in LIST_FIELDS:
            numbers = [value["category_no"] for value in r[field]]
            assert len(numbers) == len(set(numbers)), (r["key"], field)


def test_every_category_has_a_korean_and_a_display_name(market_category_result: HandlerResult) -> None:
    for r in market_category_result.records:
        values = [r["main_category"], *(v for field in LIST_FIELDS for v in r[field])]
        assert all(v["name_kr"] for v in values), r["key"]
        assert r["name"] and all(v["name"] for field in LIST_FIELDS for v in r[field]), r["key"]


def _file(rows: bytes, row_count: int, strings: list[str]) -> bytes:
    table = struct.pack("<I", len(strings)) + b"".join(
        struct.pack("<BI", 1, len(s.encode("utf-16-le"))) + s.encode("utf-16-le") for s in strings
    )
    head = b"PABR" + struct.pack("<I", row_count)
    return head + rows + table + struct.pack("<II", len(head) + len(rows), 0)


def test_parser_reads_lists_and_rejects_rows_that_miss_the_string_table() -> None:
    row = (
        struct.pack("<BBI", 1, 1, 0)
        + struct.pack("<I", 1) + struct.pack("<BI", 1, 1)
        + struct.pack("<I", 0)
        + struct.pack("<I", 1) + struct.pack("<BI", 2, 2)
        + struct.pack("<I", 7)
    )
    records = parse_itemmarketcategory_records(_file(row, 1, ["주 무기", "장검", "녹색"]))
    assert records == [{
        "key": 1,
        "main_category": {"category_no": 1, "name_kr": "주 무기"},
        "sub_categories": [{"category_no": 1, "name_kr": "장검"}],
        "filter1_values": [],
        "filter2_values": [{"category_no": 2, "name_kr": "녹색"}],
        "unknown_filter2_values_00": 7,
    }]
    with pytest.raises(ValueError):
        parse_itemmarketcategory_records(_file(row + b"\x00", 1, ["주 무기", "장검", "녹색"]))
