from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.instancefield.parser import build_instance_field_name_index

_FILE = "instancefield.dbss"
_OFFSET_FILE = "instancefieldoffset.dbss"
# u16 key, 6 x i32 box, u32, u64 name length, u16 tail: every byte but the name.
_FIXED_SIZE = 40
_KEY = struct.Struct("<H")
_AXES = ("x", "y", "z")

INSTANCE_FIELD_CASE = HandlerCase(
    handler_name=_FILE,
    data_file=_FILE,
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_FILE}",
    tests=[
        SchemaTest(required_keys=[
            "key", "name", "min_x", "min_y", "min_z", "max_x", "max_y", "max_z",
            "unknown_1a", "unknown_tail",
        ]),
        DeclaredCountTest(declared=header_count()),
        DeclaredCountTest(declared=header_count(companion=_OFFSET_FILE)),
        # Buff type 176 test items A1_001 onwards name the field they move to.
        TargetTest(col="key", value=4001, expected={"name": "A1_001"}),
        TargetTest(col="key", value=150, expected={"name": "Atoraxion_Desert"}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["key", "offset", "size"]),
        DeclaredCountTest(declared=header_count()),
    ],
)


@pytest.fixture(scope="module")
def instance_field_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_INSTANCE_FIELD_RESULT", None)
    if result is None:
        result = run_case(replace(INSTANCE_FIELD_CASE, tests=[]))
        request.module._INSTANCE_FIELD_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", INSTANCE_FIELD_CASE.tests, ids=case_id)
def test_instancefield_dbss(spec: Any, instance_field_result: HandlerResult) -> None:
    instance_field_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_instancefieldoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_keys_are_unique(instance_field_result: HandlerResult) -> None:
    keys = [r["key"] for r in instance_field_result.records]
    assert len(keys) == len(set(keys))


def test_every_box_has_its_lower_corner_first(instance_field_result: HandlerResult) -> None:
    for r in instance_field_result.records:
        assert all(r[f"min_{axis}"] <= r[f"max_{axis}"] for axis in _AXES), r["key"]


def test_offset_rows_point_at_their_records(
    instance_field_result: HandlerResult, offset_result: HandlerResult
) -> None:
    """Each offset row starts at a record with its key and spans exactly that record."""
    data = instance_field_result.source.file(None)
    names = {r["key"]: r["name"] for r in instance_field_result.records}
    rows = offset_result.records

    assert {row["key"] for row in rows} == set(names)
    for row in rows:
        (key,) = _KEY.unpack_from(data, row["offset"])
        assert key == row["key"]
        assert row["size"] == _FIXED_SIZE + len(names[key])


def test_name_index_holds_every_field(instance_field_result: HandlerResult) -> None:
    index = build_instance_field_name_index(instance_field_result.source.file(None))
    assert index == {r["key"]: r["name"] for r in instance_field_result.records}
