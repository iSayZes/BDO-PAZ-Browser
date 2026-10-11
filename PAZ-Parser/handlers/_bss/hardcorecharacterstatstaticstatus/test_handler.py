from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from _bss.experience.stat_body import STAT_BODY_SIZE, STAT_FIELDS
from .parser import FILE_NAME, FIRST_ROW, ROW_SIZE, parse_hardcore_stat_records


_COUNT = struct.Struct("<I")


def _rows_before_string_table(source: CaseInput) -> int:
    """The file stores no count; the rows fill the space up to the string table."""
    data = source.file(None)
    (table_start,) = _COUNT.unpack_from(data, len(data) - 8)
    return (table_start - FIRST_ROW) // ROW_SIZE


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["class_type", "class_name", *STAT_FIELDS]),
        DeclaredCountTest(declared=_rows_before_string_table),
        TargetTest(col="class_type", value=0, expected={"class_name": "Warrior"}),
        TargetTest(col="class_type", value=25, expected={"class_name": "Kunoichi"}),
        UserLanguageTest(fields=["class_name"]),
    ],
)


@pytest.fixture(scope="module")
def hardcore_stat_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_hardcorecharacterstatstaticstatus_bss(spec: Any, hardcore_stat_result: HandlerResult) -> None:
    hardcore_stat_result.check(spec)


def _row(class_type: int) -> bytes:
    return bytes([class_type]) + bytes(STAT_BODY_SIZE)


def _file(*rows: bytes, extra: bytes = b"") -> bytes:
    """PABR, the given rows and an empty string table."""
    body = b"PABR" + b"".join(rows) + extra
    return body + _COUNT.pack(0) + _COUNT.pack(len(body)) + bytes(4)


def test_rows_are_read_up_to_the_string_table() -> None:
    records = parse_hardcore_stat_records(_file(_row(0), _row(1), _row(2)))
    assert [r["class_type"] for r in records] == [0, 1, 2]


def test_a_partial_row_is_rejected() -> None:
    with pytest.raises(ValueError, match="not after whole 201-byte rows"):
        parse_hardcore_stat_records(_file(_row(0), extra=b"\x00"))


def test_a_row_out_of_place_is_rejected() -> None:
    with pytest.raises(ValueError, match="row 1 holds class type 2"):
        parse_hardcore_stat_records(_file(_row(0), _row(2)))
