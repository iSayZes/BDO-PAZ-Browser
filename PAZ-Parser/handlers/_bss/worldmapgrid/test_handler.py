from __future__ import annotations

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
    UserLanguageTest,
    case_id,
    run_case,
)

from .parser import (
    CELL_COUNT,
    CELL_UNITS,
    CELLS_AT,
    GRID_COLUMNS,
    GRID_MIN_X,
    GRID_MIN_Z,
    GRID_ROWS,
    cell_areas,
    read_cells,
)

_U32 = struct.Struct("<I")
_TRAILER_SIZE = 8
_MAX_BYTE = 255
_REQUIRED_KEYS = [
    "value", "keys", "name", "cell_count",
    "column_min", "column_max", "row_min", "row_max",
    "x_min", "x_max", "z_min", "z_max",
]
# territoryinfo.bss keys (LOC type 12).
_BALENOS = 0
_CALPHEON = 2
_MEDIAH = 3
_VALENCIA = 4
# Waypoints of mapdata_realexplore2.bwp (world x, z) and the territory they lie in.
_TOWN_WAYPOINTS = (
    ((-250206.0, -53631.2), _CALPHEON),  # 601 town(calpheoncity)
    ((360611.0, -57959.6), _MEDIAH),  # 1101 town(altinova)
    ((1036210.0, 195632.0), _VALENCIA),  # 1301 town(valenciacity)
)
# villagesiegeinfo.bss area 1 is Cron Castle (region 15); oceansiegeinfo.bss
# area 7 is Balvege Island (region 365).
_CRON_CASTLE_AREA, _CRON_CASTLE = 1, 15
_BALVEGE_AREA, _BALVEGE_ISLAND = 7, 365


def _distinct_cells(source: CaseInput) -> int:
    """The number of distinct bytes between the magic and the string table."""
    data = source.data
    (table_start,) = _U32.unpack_from(data, len(data) - _TRAILER_SIZE)
    return len(set(data[CELLS_AT:table_start]))


def _case(file_name: str, companion: str | None, tests: list) -> HandlerCase:
    return HandlerCase(
        handler_name=file_name,
        data_file=file_name,
        companion_files={companion: companion} if companion else {},
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=["name"],
        internal_path=f"gamecommondata/binary/{file_name}",
        tests=[
            SchemaTest(required_keys=_REQUIRED_KEYS),
            DeclaredCountTest(declared=_distinct_cells),
            RangeTest(col="value", min_val=0, max_val=_MAX_BYTE),
            UserLanguageTest(fields=["name"]),
            *tests,
        ],
    )


TERRITORY_CASE = _case("worldmapterritorytypedata.bss", None, [
    TargetTest(col="value", value=_CALPHEON, expected={"keys": [_CALPHEON], "name": "Calpheon"}),
])
MAJOR_SIEGE_REGION_CASE = _case("worldmapmajorsiegeregiontypedata.bss", None, [
    TargetTest(col="value", value=_VALENCIA, expected={"keys": [_VALENCIA], "name": "Valencia"}),
    TargetTest(col="value", value=_MAX_BYTE, expected={"keys": [], "name": None}),
])
MAJOR_SIEGE_TERRITORY_CASE = _case("worldmapmajorsiegeterritorytypedata.bss", None, [
    TargetTest(col="value", value=_VALENCIA, expected={"keys": [_VALENCIA], "name": "Valencia"}),
])
CONQUEST_TERRITORY_CASE = _case("worldmapterritorytypedataforconquest.bss", None, [
    # The cell stores the territory key + 1; 0 is the frame.
    TargetTest(col="value", value=_BALENOS + 1, expected={"keys": [_BALENOS], "name": "Balenos"}),
    TargetTest(col="value", value=0, expected={"keys": [], "name": None}),
])
FIELD_TYPE_CASE = _case("worldmapfieldtypedata.bss", "regiongroupinfo.bss", [])
SIEGE_REGION_CASE = _case("worldmapsiegeregionforconquest.bss", "villagesiegeinfo.bss", [
    TargetTest(col="value", value=_CRON_CASTLE_AREA, expected={"keys": [_CRON_CASTLE]}),
])
OCEAN_SIEGE_REGION_CASE = _case("worldmapoceansiegeregionforconquest.bss", "oceansiegeinfo.bss", [
    TargetTest(col="value", value=_BALVEGE_AREA, expected={"keys": [_BALVEGE_ISLAND]}),
])

CASES = [
    TERRITORY_CASE,
    MAJOR_SIEGE_REGION_CASE,
    MAJOR_SIEGE_TERRITORY_CASE,
    CONQUEST_TERRITORY_CASE,
    FIELD_TYPE_CASE,
    SIEGE_REGION_CASE,
    OCEAN_SIEGE_REGION_CASE,
]
_RESULTS: dict[str, HandlerResult] = {}


def _result(case: HandlerCase) -> HandlerResult:
    result = _RESULTS.get(case.handler_name)
    if result is None:
        result = run_case(replace(case, tests=[]))
        _RESULTS[case.handler_name] = result
    return result


_SPECS = [(case, spec) for case in CASES for spec in case.tests]


@pytest.mark.parametrize(
    ("case", "spec"),
    _SPECS,
    ids=[f"{case.handler_name}-{case_id(spec)}" for case, spec in _SPECS],
)
def test_worldmap_grid(case: HandlerCase, spec: Any) -> None:
    _result(case).check(spec)


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_every_cell_counts_once(case: HandlerCase) -> None:
    assert sum(record["cell_count"] for record in _result(case).records) == CELL_COUNT


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_each_box_holds_its_cells(case: HandlerCase) -> None:
    for record in _result(case).records:
        width = record["column_max"] - record["column_min"] + 1
        height = record["row_max"] - record["row_min"] + 1
        assert 0 <= record["column_min"] and record["column_max"] < GRID_COLUMNS, record
        assert 0 <= record["row_min"] and record["row_max"] < GRID_ROWS, record
        assert record["cell_count"] <= width * height, record
        assert record["x_max"] - record["x_min"] == width * CELL_UNITS, record
        assert record["z_max"] - record["z_min"] == height * CELL_UNITS, record


def test_field_type_values_are_region_group_low_bytes() -> None:
    records = _result(FIELD_TYPE_CASE).records
    assert any(record["keys"] for record in records)
    for record in records:
        assert all(key & _MAX_BYTE == record["value"] for key in record["keys"]), record


def test_towns_lie_in_their_territory() -> None:
    cells = read_cells(_result(TERRITORY_CASE).source.data, "worldmapterritorytypedata.bss")
    for (x, z), territory_key in _TOWN_WAYPOINTS:
        column = int((x - GRID_MIN_X) // CELL_UNITS)
        row = int((z - GRID_MIN_Z) // CELL_UNITS)
        assert cells[row * GRID_COLUMNS + column] == territory_key, (x, z)


def _grid_file(cells: bytes, strings: bytes = _U32.pack(0)) -> bytes:
    """PABR, the cells, a string table and the trailer."""
    table_start = CELLS_AT + len(cells)
    return b"PABR" + cells + strings + _U32.pack(table_start) + _U32.pack(0)


def test_areas_give_each_value_its_count_and_box() -> None:
    cells = bytearray(CELL_COUNT)
    for column, row in ((5, 7), (9, 7), (6, 11)):
        cells[row * GRID_COLUMNS + column] = 3
    areas = cell_areas(read_cells(_grid_file(bytes(cells)), "grid.bss"))

    assert [(area.value, area.cell_count) for area in areas] == [(0, CELL_COUNT - 3), (3, 3)]
    assert (areas[1].column_min, areas[1].column_max, areas[1].row_min, areas[1].row_max) == (5, 9, 7, 11)


def test_a_grid_of_another_size_raises() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        read_cells(_grid_file(bytes(CELL_COUNT - GRID_COLUMNS)), "grid.bss")


def test_a_grid_with_strings_raises() -> None:
    strings = _U32.pack(1) + b"\x00" + _U32.pack(1) + b"a"
    with pytest.raises(ValueError, match="1 strings"):
        read_cells(_grid_file(bytes(CELL_COUNT), strings), "grid.bss")
