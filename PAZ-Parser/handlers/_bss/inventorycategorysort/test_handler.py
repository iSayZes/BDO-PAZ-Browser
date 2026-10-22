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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, KEY_FIELD, parse_inventorycategorysort_records


_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
# Category 10, `가구`: LOC type 122 (17, 10) reads Furniture.
_FURNITURE = 10

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[KEY_FIELD, "name_kr", "unknown_name_kr_00", "category_key_dup", "name"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col=KEY_FIELD, value=_FURNITURE, expected={"name_kr": "가구", "name": "Furniture"}),
        UserLanguageTest(fields=["name"]),
    ],
)


@pytest.fixture(scope="module")
def category_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_inventorycategorysort_bss(spec: Any, category_result: HandlerResult) -> None:
    category_result.check(spec)


def test_each_row_repeats_its_key(category_result: HandlerResult) -> None:
    for record in category_result.records:
        assert record["category_key_dup"] == record[KEY_FIELD], record


def test_both_bytes_number_the_categories_once(category_result: HandlerResult) -> None:
    count = len(category_result.records)
    assert sorted(record[KEY_FIELD] for record in category_result.records) == list(range(count))
    assert sorted(record["unknown_name_kr_00"] for record in category_result.records) == list(range(count))


def _row(category_key: int, name: str, unknown: int) -> bytes:
    return bytes([category_key]) + _U64.pack(len(name)) + name.encode("utf-16-le") + bytes([unknown, category_key])


def test_a_row_reads_key_name_and_bytes() -> None:
    data = _U32.pack(1) + _row(10, "가구", 17)
    assert parse_inventorycategorysort_records(data) == [
        {KEY_FIELD: 10, "name_kr": "가구", "unknown_name_kr_00": 17, "category_key_dup": 10}
    ]


def test_bytes_after_the_last_row_raise() -> None:
    with pytest.raises(ValueError, match="rows end"):
        parse_inventorycategorysort_records(_U32.pack(1) + _row(1, "의뢰", 0) + b"\x00")
