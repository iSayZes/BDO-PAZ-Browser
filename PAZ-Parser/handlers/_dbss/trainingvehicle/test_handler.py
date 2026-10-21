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

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, parse_trainingvehicle_records


_COUNT_SIZE = 4
_ROW_SIZE = 8
# The offset file points past the leading character_key, at character_key_dup.
_KEY_PREFIX_SIZE = 2
# Scarecrow: a row since client 1784.
_SCARECROW = 31506
# Sandbag: a row since client 1784.
_SANDBAG = 31511


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["character_key", "character_key_dup", "grade", "name", "has_character_row"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="character_key", value=_SCARECROW, expected={"name": "Scarecrow", "has_character_row": True}),
        TargetTest(col="character_key", value=_SANDBAG, expected={"name": "Sandbag", "has_character_row": True}),
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
        SchemaTest(required_keys=["character_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="size", min_val=_ROW_SIZE - _KEY_PREFIX_SIZE, max_val=_ROW_SIZE - _KEY_PREFIX_SIZE),
    ],
)


@pytest.fixture(scope="module")
def training_vehicle_result(request: Any) -> HandlerResult:
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
def test_trainingvehicle_dbss(spec: Any, training_vehicle_result: HandlerResult) -> None:
    training_vehicle_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_trainingvehicleoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_character_keys_are_unique(training_vehicle_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in training_vehicle_result.records]
    assert len(keys) == len(set(keys))


def test_character_key_dup_repeats_the_key(training_vehicle_result: HandlerResult) -> None:
    bad = [r["character_key"] for r in training_vehicle_result.records if r["character_key_dup"] != r["character_key"]]
    assert not bad, f"rows whose character_key_dup differs: {bad[:5]}"


def test_offset_rows_point_at_each_row() -> None:
    """Each index row starts at its row's character_key_dup and covers the rest of the row."""
    records = parse_trainingvehicle_records(load_binary_fixture(FILE_NAME))
    expected = {
        r["character_key"]: (_COUNT_SIZE + index * _ROW_SIZE + _KEY_PREFIX_SIZE, _ROW_SIZE - _KEY_PREFIX_SIZE)
        for index, r in enumerate(records)
    }
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<IHHi", 1, _SCARECROW, _SCARECROW, 1)
    assert parse_trainingvehicle_records(data) == [
        {"character_key": _SCARECROW, "character_key_dup": _SCARECROW, "grade": 1}
    ]
    with pytest.raises(ValueError):
        parse_trainingvehicle_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_trainingvehicle_records(data[:-1])
