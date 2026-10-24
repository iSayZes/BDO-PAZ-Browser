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
    PaFieldTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.pabr_offset import parse_pabr_u32_offset_rows
from _common.string_hash import key_hash
from .parser import FILE_NAME, KEY_FIELD, OFFSET_FILE, parse_commandtooltip_records


# The PABR magic before the index's count.
_OFFSET_COUNT_AT = 4
_OFFSET_HEADER_SIZE = 8
_OFFSET_ROW_SIZE = 12
# The empty PABR string table (u32 string count) and its 8-byte trailer.
_OFFSET_TRAILER_SIZE = 12
# The first row of the Command_Tooltip_Table sheet of client 1784; the file
# stores only the key's hash.
_COMMON_01 = key_hash("COMMON_01")

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["pc_command", "console_command"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            KEY_FIELD, "pc_command_kr", "console_command_kr", "unknown_console_command_kr_00",
            "pc_command", "console_command",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col=KEY_FIELD, value=_COMMON_01, expected={KEY_FIELD: _COMMON_01}),
        RangeTest(col="unknown_console_command_kr_00", min_val=0, max_val=0),
        PaFieldTest(field="pc_command"),
        UserLanguageTest(fields=["pc_command", "console_command"]),
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
        SchemaTest(required_keys=[KEY_FIELD, "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_OFFSET_COUNT_AT)),
        TargetTest(col=KEY_FIELD, value=_COMMON_01, expected={KEY_FIELD: _COMMON_01}),
    ],
)


@pytest.fixture(scope="module")
def command_tooltip_result(request: Any) -> HandlerResult:
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
def test_commandtooltip_dbss(spec: Any, command_tooltip_result: HandlerResult) -> None:
    command_tooltip_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_commandtooltipoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_file_is_its_rows_and_an_empty_string_table() -> None:
    data = load_binary_fixture(OFFSET_FILE)
    (count,) = struct.unpack_from("<I", data, _OFFSET_COUNT_AT)
    rows_end = _OFFSET_HEADER_SIZE + count * _OFFSET_ROW_SIZE
    assert len(data) == rows_end + _OFFSET_TRAILER_SIZE
    string_count, table_start, zero = struct.unpack_from("<III", data, rows_end)
    assert (string_count, table_start, zero) == (0, rows_end, 0)


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_pabr_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<I"))
    assert not problems, problems


def test_key_hashes_are_unique(command_tooltip_result: HandlerResult) -> None:
    keys = [r[KEY_FIELD] for r in command_tooltip_result.records]
    assert len(keys) == len(set(keys))


def test_every_row_has_both_texts(command_tooltip_result: HandlerResult) -> None:
    for r in command_tooltip_result.records:
        assert r["pc_command_kr"] and r["console_command_kr"], r[KEY_FIELD]


def _row(key: int, pc: str, console: str) -> bytes:
    def str16(text: str) -> bytes:
        return struct.pack("<Q", len(text)) + text.encode("utf-16-le")

    return struct.pack("<I", key) + str16(pc) + str16(console) + struct.pack("<I", 0)


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<I", 1) + _row(7, "A", "B")
    assert parse_commandtooltip_records(data) == [{
        KEY_FIELD: 7,
        "pc_command_kr": "A",
        "console_command_kr": "B",
        "unknown_console_command_kr_00": 0,
    }]
    with pytest.raises(ValueError):
        parse_commandtooltip_records(data + b"\0")
    with pytest.raises(ValueError):
        parse_commandtooltip_records(data[:-1])
