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
    case_id,
    run_case,
)

from .parser import FILE_NAME, OFFSET_FILE, parse_greatseaevent_records, parse_greatseaeventoffset_records


_U32 = struct.Struct("<I")
_EVENT_HEAD = struct.Struct("<HB")
# The u32 group count before the first group.
_COUNT_SIZE = 4
# Group 1, index 0: "빛나는 산호초를 발견했습니다!" ("found a shining coral reef").
_FIRST_GROUP = 1


def _offset_row_count(source: CaseInput) -> int:
    """The index rows the offset file declares: the counts after each group key."""
    return len(parse_greatseaeventoffset_records(source.file(OFFSET_FILE)))


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "group_key", "select_index", "result_string_kr", "image_path", "unknown_image_path_00",
        ]),
        DeclaredCountTest(declared=_offset_row_count),
        TargetTest(col="group_key", value=_FIRST_GROUP, expected={"select_index": 0}),
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
        SchemaTest(required_keys=["group_key", "select_index", "data_offset", "data_size"]),
        TargetTest(col="group_key", value=_FIRST_GROUP, expected={"select_index": 0}),
    ],
)


@pytest.fixture(scope="module")
def event_result(request: Any) -> HandlerResult:
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
def test_greatseaevent_dbss(spec: Any, event_result: HandlerResult) -> None:
    event_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_greatseaeventoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_their_events() -> None:
    """Each index row starts at an event with its group key and index; the events of a group tile."""
    data = load_binary_fixture(FILE_NAME)
    rows = parse_greatseaeventoffset_records(load_binary_fixture(OFFSET_FILE))
    problems = []
    expected_offset = _COUNT_SIZE
    previous_group = None
    for row in rows:
        if row["group_key"] != previous_group:
            expected_offset += _U32.size
            previous_group = row["group_key"]
        if row["data_offset"] != expected_offset:
            problems.append(f"{row['group_key']}/{row['select_index']} starts at 0x{row['data_offset']:X}")
        if _EVENT_HEAD.unpack_from(data, row["data_offset"]) != (row["group_key"], row["select_index"]):
            problems.append(f"{row['group_key']}/{row['select_index']} points at another event")
        expected_offset = row["data_offset"] + row["data_size"]
    assert expected_offset == len(data), "the events do not end at the end of the file"
    assert not problems, problems


def test_index_keys_match_the_events() -> None:
    events = parse_greatseaevent_records(load_binary_fixture(FILE_NAME))
    rows = parse_greatseaeventoffset_records(load_binary_fixture(OFFSET_FILE))
    assert [(e["group_key"], e["select_index"]) for e in events] == [(r["group_key"], r["select_index"]) for r in rows]
