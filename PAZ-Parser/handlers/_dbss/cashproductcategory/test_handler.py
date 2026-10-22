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

from .parser import (
    FILE_NAME,
    MAX_DEPTH,
    OFFSET_FILE,
    parse_cashproductcategory,
    parse_cashproductcategory_records,
    parse_cashproductcategoryoffset_rows,
)


# PABR magic and count before the index rows; string count, table start and zero after them.
_OFFSET_HEAD_AND_TRAILER = 8 + 12
_OFFSET_ROW_SIZE = 10
# CppEnums.CashProductCategory.eCashProductCategory_Normal: the "Function" tab,
# UniqueNo 3 in the client 1784 CouponCategory_Table sheet.
_NORMAL = 3

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
                "main_key", "middle_key", "small_key", "category_key", "depth", "name_kr", "is_useable",
                "price_type", "special_category_type", "tag_type", "tag_order", "unique_no", "child_count",
                "name", "price_type_name",
            ],
        ),
        RangeTest(col="depth", min_val=1, max_val=MAX_DEPTH),
        RangeTest(col="price_type", min_val=0, max_val=3),
        RangeTest(col="is_useable", min_val=0, max_val=1),
        TargetTest(col="unique_no", value=_NORMAL, expected={"main_key": _NORMAL, "middle_key": None, "small_key": None}),
        UserLanguageTest(fields=["name"]),
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
        SchemaTest(required_keys=["main_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_OFFSET_HEAD_AND_TRAILER)),
    ],
)


@pytest.fixture(scope="module")
def category_result(request: Any) -> HandlerResult:
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
def test_cashproductcategory_dbss(spec: Any, category_result: HandlerResult) -> None:
    category_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_cashproductcategoryoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_main_category_has_an_index_row_at_its_start() -> None:
    data = load_binary_fixture(FILE_NAME)
    head, records = parse_cashproductcategory(data)
    rows = parse_cashproductcategoryoffset_rows(load_binary_fixture(OFFSET_FILE))
    # str16 name, u32 and u8 after it, then the u32 main category count.
    rows_start = 8 + 2 * len(head["all_name_kr"]) + 5 + 4

    problems = offset_row_problems(data, rows, struct.Struct("<H"), rows_start=rows_start)

    assert not problems, problems
    assert sorted(row.entry_id for row in rows) == sorted(r["main_key"] for r in records if r["depth"] == 1)


def test_child_counts_match_the_tree() -> None:
    records = parse_cashproductcategory_records(load_binary_fixture(FILE_NAME))
    for pos, record in enumerate(records):
        children = 0
        for later in records[pos + 1 :]:
            if later["depth"] <= record["depth"]:
                break
            children += later["depth"] == record["depth"] + 1
        assert children == record["child_count"], (record["main_key"], record["middle_key"], record["small_key"])


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _category(key: int, name: str, unique_no: int, children: bytes = b"", child_count: int = 0) -> bytes:
    flags = struct.pack("<BBBBB3sII", 1, 2, 0, 1, 4, b"\0\0\0", unique_no, child_count)
    return struct.pack("<H", key) + _str16(name) + flags + children + struct.pack("<HI", 0xFFFF, 0)


def test_parse_walks_the_tree_depth_first() -> None:
    small = _category(1, "S", 30)
    middle = _category(2, "M", 20, small, 1)
    data = _str16("ALL") + struct.pack("<IBI", 0, 1, 1) + _category(9, "Main", 10, middle, 1)

    head, records = parse_cashproductcategory(data)

    assert head["all_name_kr"] == "ALL"
    assert [(r["main_key"], r["middle_key"], r["small_key"]) for r in records] == [(9, None, None), (9, 2, None), (9, 2, 1)]
    assert [r["unique_no"] for r in records] == [10, 20, 30]
    assert records[2]["tag_type"] == 1 and records[2]["tag_order"] == 4
