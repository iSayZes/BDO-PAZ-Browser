from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.fixtures import load_binary_fixture
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

from _common.binary import u32
from .parser import FILE_NAME, OFFSET_FILE, parse_specialemployeeinfostaticstatusoffset_rows


_COUNT_SIZE = 4
# The u8 category before the u16 type a row is keyed by.
_TYPE = struct.Struct("<H")
_TYPE_AT = 1
# Arkahn (59101), hired with Proix's Old Compass (42616): type 21 of the SpecialEmployee_Table sheet of client 1784.
_ARKAHN_TYPE = 21
_ARKAHN = 59101
_OLD_COMPASS = 42616


def _offset_rows(source: CaseInput) -> int:
    """The number of rows the offset companion lists."""
    return len(parse_specialemployeeinfostaticstatusoffset_rows(source.file(OFFSET_FILE)))


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["character_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "category", "type", "character_key", "need_item_key", "need_item_count", "employ_success_rate",
            "employ_success_word_kr", "employ_fail_word_kr", "unknown_employ_fail_word_kr_00",
            "character_name", "need_item",
        ]),
        DeclaredCountTest(declared=_offset_rows),
        TargetTest(
            col="type",
            value=_ARKAHN_TYPE,
            expected={"character_key": _ARKAHN, "need_item_key": _OLD_COMPASS},
        ),
        UserLanguageTest(fields=["character_name"]),
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
        SchemaTest(required_keys=["type", "data_offset", "data_size"]),
        TargetTest(col="type", value=_ARKAHN_TYPE, expected={"data_offset": _COUNT_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def employee_result(request: Any) -> HandlerResult:
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
def test_specialemployeeinfostaticstatus_dbss(spec: Any, employee_result: HandlerResult) -> None:
    employee_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_specialemployeeinfostaticstatusoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_their_rows() -> None:
    """Each index row starts at a row with its type, and rows plus group counts fill the file."""
    data = load_binary_fixture(FILE_NAME)
    offset_data = load_binary_fixture(OFFSET_FILE)
    rows = parse_specialemployeeinfostaticstatusoffset_rows(offset_data)
    wrong_keys = [row.entry_id for row in rows if _TYPE.unpack_from(data, row.offset + _TYPE_AT)[0] != row.entry_id]
    assert not wrong_keys, wrong_keys
    group_count = u32(offset_data, 0)
    assert sum(row.size for row in rows) + group_count * _COUNT_SIZE == len(data)
