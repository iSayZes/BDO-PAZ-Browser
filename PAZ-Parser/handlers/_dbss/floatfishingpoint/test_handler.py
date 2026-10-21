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

from _dbss.floatfishing.parser import FILE_NAME as GROUP_FILE, parse_floatfishing_records
from .parser import FILE_NAME, OFFSET_FILE, parse_floatfishingpoint_records, parse_floatfishingpointoffset_rows


_COUNT_SIZE = 4
_ROW_SIZE = 42
_OFFSET_ROW_SIZE = 10
# Point 1 off Velia: group 1, spawns 917 Fishing Point, in the FloatFishingPoint_Table sheet of client 1784.
_VELIA_POINT = 1
_FISHING_POINT = 917

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["spawn_character_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "point_key",
                "point_size",
                "start_position_x",
                "start_position_y",
                "start_position_z",
                "end_position_x",
                "end_position_z",
                "fishing_group_key",
                "spawn_character_key",
                "spawn_action_index",
                "spawn_character_name",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(
            col="point_key",
            value=_VELIA_POINT,
            expected={"fishing_group_key": _VELIA_POINT, "spawn_character_key": _FISHING_POINT},
        ),
        UserLanguageTest(fields=["spawn_character_name"]),
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
        SchemaTest(required_keys=["point_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="point_key", value=_VELIA_POINT, expected={"data_size": _ROW_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def point_result(request: Any) -> HandlerResult:
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
def test_floatfishingpoint_dbss(spec: Any, point_result: HandlerResult) -> None:
    point_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_floatfishingpointoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_every_point_uses_a_fishing_group() -> None:
    """Each `fishing_group_key` is a row of `floatfishing.dbss`."""
    groups = {row["fishing_group_key"] for row in parse_floatfishing_records(load_binary_fixture(GROUP_FILE))}
    points = parse_floatfishingpoint_records(load_binary_fixture(FILE_NAME))
    missing = [point["point_key"] for point in points if point["fishing_group_key"] not in groups]
    assert not missing, missing


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_floatfishingpointoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"))
    assert not problems, problems
