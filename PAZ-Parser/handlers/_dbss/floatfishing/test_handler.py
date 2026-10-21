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

from _dbss.floatfishingpoint.parser import FILE_NAME as POINT_FILE
from .parser import DROP_SLOT_COUNT, FILE_NAME, OFFSET_FILE, parse_floatfishingoffset_rows


_COUNT_SIZE = 4
_ROW_SIZE = 70
_OFFSET_ROW_SIZE = 10
# Group 1 is used by fishing point 1 (FloatFishingPoint_Table sheet, client 1784).
_GROUP_ONE = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={POINT_FILE: POINT_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["fishing_group_key", "drop_ids", "drop_rates", "drops", "point_keys", "point_count"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="fishing_group_key", value=_GROUP_ONE, expected={"point_keys": [_GROUP_ONE]}),
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
        SchemaTest(required_keys=["fishing_group_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="fishing_group_key", value=_GROUP_ONE, expected={"data_size": _ROW_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def group_result(request: Any) -> HandlerResult:
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
def test_floatfishing_dbss(spec: Any, group_result: HandlerResult) -> None:
    group_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_floatfishingoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_drop_slot_has_a_rate_only_with_a_group(group_result: HandlerResult) -> None:
    """A slot with a drop group has a rate, an empty slot has none."""
    broken = [
        record["fishing_group_key"]
        for record in group_result.records
        if len(record["drop_ids"]) != DROP_SLOT_COUNT
        or any(bool(drop_id) != bool(rate) for drop_id, rate in zip(record["drop_ids"], record["drop_rates"]))
    ]
    assert not broken, broken


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_floatfishingoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"))
    assert not problems, problems
