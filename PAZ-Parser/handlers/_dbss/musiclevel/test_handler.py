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
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from .parser import FILE_NAME, HEADER_SIZE, KEY_FIELD, OFFSET_FILE, parse_musiclevel_records, parse_musicleveloffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 12
# The u32 key prefix in front of each row, which the index points past.
_KEY_PREFIX = struct.Struct("<I")
# Level 1 is rank F in the client 1784 MusicLevel sheet and on client 3482.
_FIRST_LEVEL = 1
_FIRST_RANK = "F"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "music_level",
                "key_prefix",
                "music_level_exp",
                "increasing_bar_number",
                "increasing_note_number",
                "music_rank",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col=KEY_FIELD, value=_FIRST_LEVEL, expected={"music_rank": _FIRST_RANK}),
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
        SchemaTest(required_keys=["music_level", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def level_result(request: Any) -> HandlerResult:
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
def test_musiclevel_dbss(spec: Any, level_result: HandlerResult) -> None:
    level_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_musicleveloffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_key_prefix_repeats_the_level(level_result: HandlerResult) -> None:
    wrong = [r[KEY_FIELD] for r in level_result.records if r["key_prefix"] != r[KEY_FIELD]]
    assert not wrong, wrong


def test_offset_rows_point_at_each_level() -> None:
    rows = parse_musicleveloffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(
        load_binary_fixture(FILE_NAME),
        rows,
        _KEY_PREFIX,
        rows_start=HEADER_SIZE,
        lead=_KEY_PREFIX.size,
    )
    assert not problems, problems


def _entry(level: int, exp: int, bars: int, notes: int, rank: str) -> bytes:
    return struct.pack("<IIQIIQ", level, level, exp, bars, notes, len(rank)) + rank.encode("utf-16-le")


def test_parse_reads_each_level() -> None:
    data = struct.pack("<II", 2, 2) + _entry(1, 72, 30, 500, "F") + _entry(2, 108, 34, 555, "D-")

    records = parse_musiclevel_records(data)

    assert records[1] == {
        "music_level": 2,
        "key_prefix": 2,
        "music_level_exp": 108,
        "increasing_bar_number": 34,
        "increasing_note_number": 555,
        "music_rank": "D-",
    }


def test_parse_rejects_bytes_after_the_last_level() -> None:
    data = struct.pack("<II", 1, 1) + _entry(1, 72, 30, 500, "F") + b"\x00"
    with pytest.raises(ValueError):
        parse_musiclevel_records(data)
