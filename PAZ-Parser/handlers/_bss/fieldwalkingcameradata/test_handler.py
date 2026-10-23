from __future__ import annotations

import math
import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _common.string_hash import key_hash
from .parser import FILE_NAME


_PABR_HEAD = struct.Struct("<4sI")
_ROW_HEAD = struct.Struct("<IIHI")
_POINT_SIZE = 38
_ROW_TAIL_SIZE = 4
# A camera walk through Velia; the source XML has it under region 5 too.
_VELIA_EVENT = "rebalenos_velia_001"
_VELIA = 5
_MAX_FOV_DEGREES = 180


def _camera_points(source: CaseInput) -> int:
    """The point counts of every row added up, walked from the row heads."""
    data = source.data
    _, row_count = _PABR_HEAD.unpack_from(data, 0)
    pos, total = _PABR_HEAD.size, 0
    for _ in range(row_count):
        *_, point_count = _ROW_HEAD.unpack_from(data, pos)
        total += point_count
        pos += _ROW_HEAD.size + point_count * _POINT_SIZE + _ROW_TAIL_SIZE
    return total


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["region_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "event_name_hash", "event_name", "region_key", "region_name", "point_count", "unknown_points_00",
            "point_index", "position", "rotation", "fov", "speed_or_time", "is_speed_mode", "is_spline",
        ]),
        DeclaredCountTest(declared=_camera_points),
        TargetTest(col="event_name", value=_VELIA_EVENT, expected={"region_key": _VELIA}),
        RangeTest(col="fov_degrees", min_val=0, max_val=_MAX_FOV_DEGREES),
        RangeTest(col="is_speed_mode", min_val=0, max_val=1),
        RangeTest(col="is_spline", min_val=0, max_val=1),
    ],
)


@pytest.fixture(scope="module")
def camera_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fieldwalkingcameradata_bss(spec: Any, camera_result: HandlerResult) -> None:
    camera_result.check(spec)


def test_event_hash_is_the_utf16_key_hash(camera_result: HandlerResult) -> None:
    """`event_name_hash` is `key_hash()` of the event name, over its UTF-16LE bytes."""
    for r in camera_result.records:
        assert r["event_name_hash"] == key_hash(r["event_name"]), r["event_name"]


def test_rotations_are_unit_quaternions(camera_result: HandlerResult) -> None:
    for r in camera_result.records:
        assert math.isclose(math.hypot(*r["rotation"]), 1, abs_tol=1e-3), (r["event_name"], r["point_index"])
