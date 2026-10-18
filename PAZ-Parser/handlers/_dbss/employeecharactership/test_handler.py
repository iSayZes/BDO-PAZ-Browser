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
    header_count,
    run_case,
)

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from .parser import FILE_NAME, OFFSET_FILE, parse_employeecharactership_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
# character_key to manual_cannon_fire_decrease_cool_time, then the u64 count
# of the condition text.
_FIXED_ROW_SIZE = 68
_TEXT_COUNT_SIZE = 8
_FLAG_FIELDS = (
    "is_summon_full",
    "new_cannon_ship_ui",
    "ocean_ship_skill_ui",
    "manual_cannon_fire",
    "manual_cannon_fire_decrease_cool_time",
)
_EPHERIA_CARAVEL = 31048


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["character_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "character_key", "employee_max", "employee_spawn_count", "food_max",
            "ocean_ship_cannon_setup", "ship_food_recovery", "ship_cannon_recovery",
            "damage_diagram_restoration_cost", "unknown_1e", "unknown_22", *_FLAG_FIELDS,
            "new_cannon_count", "new_cannon_speed", "manual_cannon_fire_min_length",
            "manual_cannon_fire_max_length", "manual_cannon_fire_random_dist",
            "manual_cannon_fire_random_pos", "manual_cannon_fire_max_angle",
            "manual_cannon_fire_decrease_cool_time_condition", "character_name", "has_character_row",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        *(RangeTest(col=field, min_val=0, max_val=1) for field in _FLAG_FIELDS),
        TargetTest(col="character_key", value=_EPHERIA_CARAVEL, expected={"has_character_row": True}),
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
        SchemaTest(required_keys=["character_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
    ],
)


@pytest.fixture(scope="module")
def ship_result(request: Any) -> HandlerResult:
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
def test_employeecharactership_dbss(spec: Any, ship_result: HandlerResult) -> None:
    ship_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_employeecharactershipoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_character_keys_are_unique(ship_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in ship_result.records]
    assert len(keys) == len(set(keys))


def test_offset_rows_cover_each_row_exactly(offset_result: HandlerResult) -> None:
    """Each index row points at the start of the row with its key and covers all of it."""
    expected = {}
    pos = _COUNT_SIZE
    for r in parse_employeecharactership_records(load_binary_fixture(FILE_NAME)):
        size = (
            _FIXED_ROW_SIZE
            + _TEXT_COUNT_SIZE
            + 2 * len(r["manual_cannon_fire_decrease_cool_time_condition"])
        )
        expected[r["character_key"]] = (pos, size)
        pos += size
    actual = {r["character_key"]: (r["data_offset"], r["data_size"]) for r in offset_result.records}
    assert actual == expected


def _row(character_key: int, condition: str) -> bytes:
    fixed = struct.pack(
        "<HIIIIfffIIBBBfBBffffIB",
        character_key, 30, 3, 1100000, 300, 0.6, 1000.0, 1000000.0, 0, 0,
        0, 1, 4, 13.0, 1, 1, 3000.0, 15000.0, 300.0, 100.0, 10, 1,
    )
    text = condition.encode("utf-16-le")
    return fixed + struct.pack("<Q", len(condition)) + text


def test_parser_reads_a_row_and_rejects_bytes_after_the_rows() -> None:
    condition = "getlifelevel(9)>80;"
    data = struct.pack("<I", 1) + _row(_EPHERIA_CARAVEL, condition)
    record = parse_employeecharactership_records(data)[0]
    assert record["character_key"] == _EPHERIA_CARAVEL
    assert record["ship_food_recovery"] == 0.6
    assert record["new_cannon_count"] == 4
    assert record["manual_cannon_fire_max_angle"] == 10
    assert record["manual_cannon_fire_decrease_cool_time_condition"] == condition
    with pytest.raises(ValueError):
        parse_employeecharactership_records(data + b"\x00")


def test_parser_rejects_a_row_cut_short() -> None:
    data = struct.pack("<I", 1) + _row(_EPHERIA_CARAVEL, "")[:-1]
    with pytest.raises(ValueError):
        parse_employeecharactership_records(data)
