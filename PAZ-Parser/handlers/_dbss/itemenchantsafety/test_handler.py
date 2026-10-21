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

from .parser import FILE_NAME, OFFSET_FILE, parse_itemenchantsafetyoffset_rows


_COUNT_SIZE = 4
_ROW_SIZE = 15
_OFFSET_ROW_SIZE = 12
# Type 2 is accessories in the Enchant_Safetymode sheet comment of client 1784.
_ACCESSORIES = 2

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
            required_keys=["type", "gear", "min_level", "max_level", "stack", "caution_stack", "caution_rate"]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="type", value=_ACCESSORIES, expected={"gear": "Accessories"}),
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
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="type", value=_ACCESSORIES, expected={"data_size": _ROW_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def safety_result(request: Any) -> HandlerResult:
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
def test_itemenchantsafety_dbss(spec: Any, safety_result: HandlerResult) -> None:
    safety_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemenchantsafetyoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_types_are_unique(safety_result: HandlerResult) -> None:
    types = [r["type"] for r in safety_result.records]
    assert len(types) == len(set(types)), types


def test_level_ranges_are_ordered(safety_result: HandlerResult) -> None:
    bad = [r["type"] for r in safety_result.records if r["min_level"] > r["max_level"]]
    assert not bad, bad


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_itemenchantsafetyoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<B"))
    assert not problems, problems
