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
    SchemaTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_strings import fixed_row_offsets
from .parser import FILE_NAME, KEY_FIELD, parse_buffitemautouse_records


_U32 = struct.Struct("<I")
_ROW = struct.Struct("<IIB")
# autousebuffitemcategoryinfo.bss rows are (u32 category key, u32 name index).
_CATEGORY_FILE = "autousebuffitemcategoryinfo.bss"
_CATEGORY_ROW_SIZE = 8

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["category_key", KEY_FIELD, "unknown_08", "item_name"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        UserLanguageTest(fields=["item_name"]),
    ],
)


@pytest.fixture(scope="module")
def autouse_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_buffitemautousestaticstatus_bss(spec: Any, autouse_result: HandlerResult) -> None:
    autouse_result.check(spec)


def test_each_item_has_one_row(autouse_result: HandlerResult) -> None:
    items = [record[KEY_FIELD] for record in autouse_result.records]
    assert len(items) == len(set(items))


def test_every_category_is_an_auto_use_category(autouse_result: HandlerResult) -> None:
    data = load_binary_fixture(_CATEGORY_FILE)
    category_keys = {_U32.unpack_from(data, start)[0] for start in fixed_row_offsets(data, _CATEGORY_ROW_SIZE, _CATEGORY_FILE)}
    assert {record["category_key"] for record in autouse_result.records} <= category_keys


def _pabr(rows: bytes, count: int) -> bytes:
    body = _U32.pack(count) + rows
    table_start = len(b"PABR") + len(body)
    return b"PABR" + body + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_a_row_reads_category_item_and_byte() -> None:
    records = parse_buffitemautouse_records(_pabr(_ROW.pack(2, 1399, 15), 1))
    assert records == [{"category_key": 2, KEY_FIELD: 1399, "unknown_08": 15}]


def test_rows_that_stop_short_of_the_string_table_raise() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_buffitemautouse_records(_pabr(_ROW.pack(1, 9284, 1) + b"\x00", 1))
