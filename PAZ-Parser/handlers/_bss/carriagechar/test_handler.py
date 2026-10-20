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
    case_id,
    run_case,
)

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from _common.pabr_offset import PABR_MAGIC
from _common.pabr_strings import TRAILER_SIZE, U32_SIZE
from .parser import FILE_NAME, parse_carriagechar_records


# The Velia Freight Wagon, in the file since client 1230.
_WAGON = 59012


def _string_count(source: CaseInput) -> int:
    """The string table count at the offset the trailer stores: one string per row."""
    data = source.data
    (table_start,) = struct.unpack_from("<I", data, len(data) - TRAILER_SIZE)
    if table_start + U32_SIZE > len(data):
        raise AssertionError(f"string table offset 0x{table_start:X} is past the end of {len(data)} bytes")
    return struct.unpack_from("<I", data, table_start)[0]


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["character_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_key",
                "character_name",
                "has_character_row",
                "object_name_index",
                "object_name",
            ]
        ),
        DeclaredCountTest(declared=_string_count),
        TargetTest(
            col="character_key",
            value=_WAGON,
            expected={"has_character_row": True, "object_name": "WorldMap/WorldMap_Cart.pam"},
        ),
    ],
)


def _file(rows: tuple[tuple[int, str], ...], header_value: int, rows_end_delta: int = 0) -> bytes:
    """PABR, the header u32, the rows, their strings and the trailer pointing at the strings."""
    body = struct.pack("<I", header_value)
    body += b"".join(struct.pack("<HI", key, index) for index, (key, _) in enumerate(rows))
    strings = struct.pack("<I", len(rows)) + b"".join(
        struct.pack("<BI", 0, len(text)) + text.encode() for _, text in rows
    )
    rows_end = len(PABR_MAGIC) + len(body) + rows_end_delta
    return PABR_MAGIC + body + strings + struct.pack("<II", rows_end, 0)


@pytest.fixture(scope="module")
def carriagechar_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_carriagechar_bss(spec: Any, carriagechar_result: HandlerResult) -> None:
    carriagechar_result.check(spec)


def test_character_keys_are_unique(carriagechar_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in carriagechar_result.records]
    assert len(keys) == len(set(keys))


def test_every_row_has_a_model_path(carriagechar_result: HandlerResult) -> None:
    assert all(r["object_name"].endswith(".pam") for r in carriagechar_result.records)


def test_rows_run_to_the_string_table_whatever_the_header_says() -> None:
    rows = ((59012, "WorldMap/A.pam"), (59013, "WorldMap/B.pam"), (59014, "WorldMap/C.pam"))
    records = parse_carriagechar_records(_file(rows, header_value=len(rows) - 1))
    assert [(r["character_key"], r["object_name"]) for r in records] == list(rows)


@pytest.mark.parametrize(
    "data",
    [
        _file(((59012, "WorldMap/A.pam"),), header_value=0, rows_end_delta=2),
        b"XXXX" + _file(((59012, "WorldMap/A.pam"),), header_value=0)[4:],
    ],
    ids=["rows_end_mismatch", "bad_magic"],
)
def test_a_changed_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_carriagechar_records(data)
