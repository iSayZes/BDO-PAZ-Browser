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
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from .parser import DISCOUNT_STEP_COUNT, FILE_NAME, OFFSET_FILE, parse_eventcategoryoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# Index 4 of the EventCategory_Table sheet of client 1784: the 2021-07-21 event.
_EVENT_4 = 4

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "index", "cash_coupon_category_main", "cash_coupon_category_middle", "cash_coupon_category_small",
            "discount_start_period", "discount_end_period", "unknown_discount_end_period_00", "discount_steps",
            "unknown_discount_end_period_a1", "max_discount_pearl", "event_type",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="index", value=_EVENT_4, expected={"discount_start_period": "2021-07-21 09:00"}),
        RangeTest(col="event_type", min_val=0, max_val=1),
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
def test_eventcategory_dbss(spec: Any, event_result: HandlerResult) -> None:
    event_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_eventcategoryoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_row_has_ten_discount_steps(event_result: HandlerResult) -> None:
    assert all(len(r["discount_steps"]) == DISCOUNT_STEP_COUNT for r in event_result.records)


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_eventcategoryoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"))
    assert not problems, problems
