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
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, parse_petdetectposition_records


_COUNT_SIZE = 4
_ROW_SIZE = 15
# gc::PetDetectPositionType has only ePetDetectPositionType_None (0) before its Count marker.
_TYPE_NONE = 0


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["pet_detect_position_key", "pos_x", "pos_y", "pos_z", "pet_detect_position_type"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        RangeTest(col="pet_detect_position_type", min_val=_TYPE_NONE, max_val=_TYPE_NONE),
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
        SchemaTest(required_keys=["pet_detect_position_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="size", min_val=_ROW_SIZE, max_val=_ROW_SIZE),
    ],
)


@pytest.fixture(scope="module")
def pet_detect_position_result(request: Any) -> HandlerResult:
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
def test_petdetectposition_dbss(spec: Any, pet_detect_position_result: HandlerResult) -> None:
    pet_detect_position_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_petdetectpositionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_position_keys_are_unique(pet_detect_position_result: HandlerResult) -> None:
    keys = [r["pet_detect_position_key"] for r in pet_detect_position_result.records]
    assert len(keys) == len(set(keys))


def test_offset_rows_point_at_each_row() -> None:
    """Each index row starts at its row's own key and covers the whole row."""
    records = parse_petdetectposition_records(load_binary_fixture(FILE_NAME))
    expected = {
        r["pet_detect_position_key"]: (_COUNT_SIZE + index * _ROW_SIZE, _ROW_SIZE) for index, r in enumerate(records)
    }
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<IHfffB", 1, 3, 1500.0, -250.0, 3200.5, _TYPE_NONE)
    assert parse_petdetectposition_records(data) == [
        {
            "pet_detect_position_key": 3,
            "pos_x": 1500.0,
            "pos_y": -250.0,
            "pos_z": 3200.5,
            "pet_detect_position_type": _TYPE_NONE,
        }
    ]
    with pytest.raises(ValueError):
        parse_petdetectposition_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_petdetectposition_records(data[:-1])
