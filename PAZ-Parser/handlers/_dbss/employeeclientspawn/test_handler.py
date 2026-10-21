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
    UserLanguageTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import FILE_NAME, OFFSET_FILE


_COUNT_SIZE = 4
_ROW_SIZE = 20
_OFFSET_ROW_SIZE = 12
# Epheria Sailboat: one sailor position, index 0, in the EmployeeShipSpawnPosition_Table sheet of client 1784.
_EPHERIA_SAILBOAT = 31001

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["character_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "character_key", "index", "spawn_position_x", "spawn_position_y", "spawn_position_z",
            "spawn_direction", "character_name",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="character_key", value=_EPHERIA_SAILBOAT, expected={"index": 0}),
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
        SchemaTest(required_keys=["character_key", "index", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="character_key", value=_EPHERIA_SAILBOAT, expected={"index": 0, "data_size": _ROW_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def spawn_result(request: Any) -> HandlerResult:
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
def test_employeeclientspawn_dbss(spec: Any, spawn_result: HandlerResult) -> None:
    spawn_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_employeeclientspawnoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_rows_are_unique_per_ship_and_index(spawn_result: HandlerResult) -> None:
    keys = [(r["character_key"], r["index"]) for r in spawn_result.records]
    assert len(keys) == len(set(keys))


def test_offset_rows_point_at_their_rows() -> None:
    """The index key is the row's first u32: `index << 16 | character_key`."""
    rows = parse_bare_u32_offset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<I"))
    assert not problems, problems
