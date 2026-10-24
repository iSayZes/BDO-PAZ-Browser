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

from .parser import FILE_NAME, OFFSET_FILE, parse_blackspirit_records, parse_blackspiritoffset_rows


_COUNT_SIZE = 4
# u8 index, u32 offset, u32 size.
_OFFSET_ROW_SIZE = 9
# The first form, which every character has from the start.
_DEFAULT_FORM = 0

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["index", "condition"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="index", value=_DEFAULT_FORM, expected={"condition": ""}),
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
        SchemaTest(required_keys=["index", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="index", value=_DEFAULT_FORM, expected={"index": _DEFAULT_FORM}),
    ],
)


@pytest.fixture(scope="module")
def black_spirit_result(request: Any) -> HandlerResult:
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
def test_blackspirit_dbss(spec: Any, black_spirit_result: HandlerResult) -> None:
    black_spirit_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_blackspiritoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_indexes_are_unique(black_spirit_result: HandlerResult) -> None:
    indexes = [record["index"] for record in black_spirit_result.records]
    assert len(indexes) == len(set(indexes))


def test_every_other_form_has_a_condition(black_spirit_result: HandlerResult) -> None:
    assert all(r["condition"] for r in black_spirit_result.records if r["index"] != _DEFAULT_FORM)


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_blackspiritoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<B"))
    assert not problems, problems


def _row(index: int, condition: str) -> bytes:
    return struct.pack("<BQ", index, len(condition)) + condition.encode("utf-16-le")


def test_parse_reads_the_index_and_condition() -> None:
    data = struct.pack("<I", 2) + _row(0, "") + _row(5, "clearQuest(122,5);")

    records = parse_blackspirit_records(data)

    assert records == [{"index": 0, "condition": ""}, {"index": 5, "condition": "clearQuest(122,5);"}]


def test_parse_rejects_a_condition_past_the_file() -> None:
    with pytest.raises(ValueError):
        parse_blackspirit_records(struct.pack("<I", 1) + struct.pack("<BQ", 1, 50))
