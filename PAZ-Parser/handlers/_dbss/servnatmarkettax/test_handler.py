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

from .parser import FILE_NAME, OFFSET_FILE, parse_servnatmarkettaxoffset_rows


_COUNT_SIZE = 4
_ROW_SIZE = 8
_OFFSET_ROW_SIZE = 12

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["life_level", "horse_market_tax_percent", "rank"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="life_level", value=1, expected={"rank": "Beginner 1"}),
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
        SchemaTest(required_keys=["life_level", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="life_level", value=1, expected={"data_offset": _COUNT_SIZE, "data_size": _ROW_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def tax_result(request: Any) -> HandlerResult:
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
def test_servnatmarkettax_dbss(spec: Any, tax_result: HandlerResult) -> None:
    tax_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_servnatmarkettaxoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_levels_run_from_one_in_order(tax_result: HandlerResult) -> None:
    levels = [r["life_level"] for r in tax_result.records]
    assert levels == list(range(1, len(levels) + 1))


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_servnatmarkettaxoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<I"))
    assert not problems, problems
