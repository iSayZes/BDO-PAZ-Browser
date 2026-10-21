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
    UserLanguageTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from .parser import BAN_FIELDS, FILE_NAME, OFFSET_FILE, parse_restrictcontentsregionoffset_rows


_COUNT_SIZE = 4
_ROW_SIZE = 13
_OFFSET_ROW_SIZE = 10
# The index points past the leading u16 region key.
_KEY_SIZE = 2
# Orze's Garden, LOC type 17.
_ORZES_GARDEN = 1550

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["region_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["region_key", "region_key_dup", *BAN_FIELDS, "unknown_0c", "region_name"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="region_key", value=_ORZES_GARDEN, expected={"region_key_dup": _ORZES_GARDEN}),
        *(RangeTest(col=field, min_val=0, max_val=1) for field in BAN_FIELDS),
        UserLanguageTest(fields=["region_name"]),
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
        SchemaTest(required_keys=["region_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="region_key", value=_ORZES_GARDEN, expected={"data_size": _ROW_SIZE - _KEY_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def region_result(request: Any) -> HandlerResult:
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
def test_restrictcontentsregion_dbss(spec: Any, region_result: HandlerResult) -> None:
    region_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_restrictcontentsregionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_key_is_a_named_region(region_result: HandlerResult) -> None:
    """Each key is a `regioninfo.bss` region with a LOC type 17 name, and repeats as `region_key_dup`."""
    unnamed = [r["region_key"] for r in region_result.records if not r["region_name"]]
    assert not unnamed, unnamed
    assert all(r["region_key"] == r["region_key_dup"] for r in region_result.records)


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_restrictcontentsregionoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"), lead=_KEY_SIZE)
    assert not problems, problems
