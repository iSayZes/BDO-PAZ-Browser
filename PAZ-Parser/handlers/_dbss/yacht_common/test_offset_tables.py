"""The `*offset.dbss` indexes of the keyed Yar! tables: their previews and where they point."""
from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.binary import u32
from _common.pabr_offset import parse_bare_u32_offset_rows
from _dbss.yachtbasecard.parser import FILE_NAME as BASE_CARD_FILE, OFFSET_FILE as BASE_CARD_OFFSET_FILE
from _dbss.yachtclasstypetextureinfo.parser import (
    FILE_NAME as CLASS_TEXTURE_FILE,
    OFFSET_FILE as CLASS_TEXTURE_OFFSET_FILE,
)
from _dbss.yachtdice.parser import FILE_NAME as DICE_FILE, OFFSET_FILE as DICE_OFFSET_FILE
from _dbss.yachtdicecard.parser import FILE_NAME as DICE_CARD_FILE, OFFSET_FILE as DICE_CARD_OFFSET_FILE
from _dbss.yachtdicepreset.parser import FILE_NAME as DICE_PRESET_FILE, OFFSET_FILE as DICE_PRESET_OFFSET_FILE
from tests.fixtures import load_binary_fixture
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

from .keyed_rows import COUNT_SIZE

# The leading key in front of the row part an index row points at.
_KEY_SIZE = 4


def _offset_row_problems(data: bytes, offset_data: bytes) -> list[str]:
    """What breaks the index: a row that does not point at both copies of its key, or rows that do not tile the file.

    Each index row points 4 bytes into its row, past the leading key, and its
    size excludes that key, so the rows plus their keys fill the file after
    the count.
    """
    rows = sorted(parse_bare_u32_offset_rows(offset_data), key=lambda row: row.offset)
    problems = [
        f"key {row.entry_id} at 0x{row.offset:X} reads {u32(data, row.offset - _KEY_SIZE)} / {u32(data, row.offset)}"
        for row in rows
        if u32(data, row.offset - _KEY_SIZE) != row.entry_id or u32(data, row.offset) != row.entry_id
    ]
    expected_offset = COUNT_SIZE + _KEY_SIZE
    for row in rows:
        if row.offset != expected_offset:
            problems.append(f"key {row.entry_id} starts at 0x{row.offset:X}, expected 0x{expected_offset:X}")
        expected_offset = row.offset + row.size + _KEY_SIZE
    if expected_offset - _KEY_SIZE != len(data):
        problems.append(f"the rows end at 0x{expected_offset - _KEY_SIZE:X}, the file at 0x{len(data):X}")
    return problems


def _offset_case(offset_file: str, key: int) -> HandlerCase:
    """The handler case of `offset_file`, with `key` one of its keys (from the client 1784 sheets)."""
    return HandlerCase(
        handler_name=offset_file,
        data_file=offset_file,
        companion_files={},
        loc_file=None,
        uses_loc=False,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{offset_file}",
        tests=[
            SchemaTest(required_keys=["key", "data_offset", "data_size"]),
            DeclaredCountTest(declared=header_count(offset=0)),
            TargetTest(col="key", value=key, expected={"key": key}),
        ],
    )


# One module-level case per file, so tests/handler_cases.py finds each.
DICE_PRESET_OFFSET_CASE = _offset_case(DICE_PRESET_OFFSET_FILE, 26)
DICE_OFFSET_CASE = _offset_case(DICE_OFFSET_FILE, 1)
DICE_CARD_OFFSET_CASE = _offset_case(DICE_CARD_OFFSET_FILE, 31)
BASE_CARD_OFFSET_CASE = _offset_case(BASE_CARD_OFFSET_FILE, 1)
CLASS_TEXTURE_OFFSET_CASE = _offset_case(CLASS_TEXTURE_OFFSET_FILE, 0)

_CASES = (
    DICE_PRESET_OFFSET_CASE,
    DICE_OFFSET_CASE,
    DICE_CARD_OFFSET_CASE,
    BASE_CARD_OFFSET_CASE,
    CLASS_TEXTURE_OFFSET_CASE,
)
# Each table and its index.
_TABLES = (
    (DICE_PRESET_FILE, DICE_PRESET_OFFSET_FILE),
    (DICE_FILE, DICE_OFFSET_FILE),
    (DICE_CARD_FILE, DICE_CARD_OFFSET_FILE),
    (BASE_CARD_FILE, BASE_CARD_OFFSET_FILE),
    (CLASS_TEXTURE_FILE, CLASS_TEXTURE_OFFSET_FILE),
)
_SPECS = [(case, spec) for case in _CASES for spec in case.tests]


def _spec_id(case_spec: tuple[HandlerCase, Any]) -> str:
    case, spec = case_spec
    return f"{case.handler_name}: {case_id(spec)}"


@pytest.fixture(scope="module")
def offset_results() -> dict[str, HandlerResult]:
    return {case.handler_name: run_case(replace(case, tests=[])) for case in _CASES}


@pytest.mark.parametrize("case_spec", _SPECS, ids=_spec_id)
def test_yacht_offset_dbss(case_spec: tuple[HandlerCase, Any], offset_results: dict[str, HandlerResult]) -> None:
    case, spec = case_spec
    offset_results[case.handler_name].check(spec)


@pytest.mark.parametrize("table", _TABLES, ids=lambda table: table[1])
def test_offset_rows_point_at_their_rows(table: tuple[str, str]) -> None:
    file_name, offset_file = table
    problems = _offset_row_problems(load_binary_fixture(file_name), load_binary_fixture(offset_file))
    assert not problems, problems
