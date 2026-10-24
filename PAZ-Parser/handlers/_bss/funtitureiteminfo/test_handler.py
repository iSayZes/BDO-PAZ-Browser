from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, KEY_FIELD, parse_funtitureiteminfo_records


_U32 = struct.Struct("<I")
_ROW = struct.Struct("<IIB")
# CppEnums.InstallationType.TypeCount in global_define_cpp_enum.luac (client 3482).
_INSTALLATION_TYPE_COUNT = 40

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[KEY_FIELD, "item_key_dup", "installation_type", "item_name"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="installation_type", min_val=0, max_val=_INSTALLATION_TYPE_COUNT - 1),
        UserLanguageTest(fields=["item_name"]),
    ],
)


@pytest.fixture(scope="module")
def funtiture_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_funtitureiteminfo_bss(spec: Any, funtiture_result: HandlerResult) -> None:
    funtiture_result.check(spec)


def test_each_row_repeats_its_item_key(funtiture_result: HandlerResult) -> None:
    for record in funtiture_result.records:
        assert record["item_key_dup"] == record[KEY_FIELD], record


def test_each_item_has_one_row(funtiture_result: HandlerResult) -> None:
    items = [record[KEY_FIELD] for record in funtiture_result.records]
    assert len(items) == len(set(items))


def _pabr(rows: bytes, count: int) -> bytes:
    body = _U32.pack(count) + rows
    table_start = len(b"PABR") + len(body)
    return b"PABR" + body + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_a_row_reads_item_copy_and_type() -> None:
    records = parse_funtitureiteminfo_records(_pabr(_ROW.pack(47792, 47792, 35), 1))
    assert records == [{KEY_FIELD: 47792, "item_key_dup": 47792, "installation_type": 35}]


def test_rows_that_stop_short_of_the_string_table_raise() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_funtitureiteminfo_records(_pabr(_ROW.pack(3719, 3719, 4) + b"\x00", 1))
