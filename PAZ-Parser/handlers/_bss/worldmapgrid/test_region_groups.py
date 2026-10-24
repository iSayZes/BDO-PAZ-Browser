from __future__ import annotations

import pytest

from tests.fixtures import load_binary_fixture

from .parser import CELL_COUNT, GRID_COLUMNS, CellArea, merge_areas, read_cells, split_areas
from .region_groups import region_group_rows, split_value

_FIELD_GRID = "worldmapfieldtypedata.bss"
_GROUP_FILE = "regiongroupinfo.bss"
# regiongroupinfo.bss groups 2 (Altar of Agris) and 258 (Unjongga Street) share the value 2.
_SHARED_VALUE, _ALTAR_OF_AGRIS, _UNJONGGA_STREET = 2, 2, 258
# Territory keys (territoryinfo.bss).
_BALENOS, _SERENDIA, _VALENCIA, _MORNING_LIGHT = 0, 1, 4, 10


def _cell(column: int, row: int) -> int:
    return row * GRID_COLUMNS + column


def test_groups_in_one_territory_each_own_it() -> None:
    split = split_value([2, 258], {2: frozenset({_BALENOS}), 258: frozenset({_MORNING_LIGHT})})

    assert split.keys_in(_BALENOS) == (2,)
    assert split.keys_in(_MORNING_LIGHT) == (258,)
    # A territory neither group lies in keeps both keys.
    assert split.keys_in(_SERENDIA) == (2, 258)


def test_a_group_in_several_territories_takes_the_rest() -> None:
    split = split_value(
        [0, 256], {0: frozenset({_BALENOS, _VALENCIA, _MORNING_LIGHT}), 256: frozenset({_MORNING_LIGHT})}
    )

    assert split.keys_in(_MORNING_LIGHT) == (256,)
    assert split.keys_in(_BALENOS) == (0,)
    assert split.keys_in(_SERENDIA) == (0,)


def test_a_territory_two_groups_claim_has_no_owner() -> None:
    split = split_value([5, 261], {5: frozenset({_BALENOS}), 261: frozenset({_BALENOS})})

    assert split.keys_in(_BALENOS) == (5, 261)


def test_split_areas_give_each_value_and_territory_its_box() -> None:
    cells, territories = bytearray(CELL_COUNT), bytearray(CELL_COUNT)
    for column, row in ((5, 7), (9, 7), (6, 11)):
        cells[_cell(column, row)] = 3
    territories[_cell(6, 11)] = _MORNING_LIGHT

    areas = split_areas(bytes(cells), bytes(territories), {3})

    assert areas == {
        (3, _BALENOS): CellArea(3, 2, 5, 9, 7, 7),
        (3, _MORNING_LIGHT): CellArea(3, 1, 6, 6, 11, 11),
    }
    assert merge_areas(list(areas.values())) == CellArea(3, 3, 5, 9, 7, 11)


def test_split_areas_of_grids_of_two_sizes_raise() -> None:
    with pytest.raises(ValueError, match="split grid"):
        split_areas(bytes(CELL_COUNT), bytes(CELL_COUNT - 1), {0})


def test_without_the_territory_grid_a_shared_value_keeps_one_row() -> None:
    cells = read_cells(load_binary_fixture(_FIELD_GRID), _FIELD_GRID)
    rows = region_group_rows(cells, {_GROUP_FILE: load_binary_fixture(_GROUP_FILE)})

    values = [row.area.value for row in rows]
    assert len(values) == len(set(values))
    (shared,) = [row for row in rows if row.area.value == _SHARED_VALUE]
    assert shared.join.keys == (_ALTAR_OF_AGRIS, _UNJONGGA_STREET)
