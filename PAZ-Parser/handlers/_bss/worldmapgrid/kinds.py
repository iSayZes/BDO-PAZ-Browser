"""What the cell values of each world map grid stand for, and their names.

Each grid stores one byte per cell; the byte joins a different table per file
(docs/file-formats/worldmapgrid_bss.md, Cell Values):

| File                                       | Cell value                                   |
| ------------------------------------------ | -------------------------------------------- |
| `worldmapterritorytypedata.bss`            | territory key                                |
| `worldmapmajorsiege{region,territory}typedata.bss` | territory key, `255` none            |
| `worldmapterritorytypedataforconquest.bss` | territory key + 1, `255` none                |
| `worldmapfieldtypedata.bss`                | low byte of a `regiongroupinfo.bss` key      |
| `worldmapsiegeregionforconquest.bss`       | `villagesiegeinfo.bss` area number           |
| `worldmapoceansiegeregionforconquest.bss`  | `oceansiegeinfo.bss` area number, `255` none |

Every grid has one row per cell value, except the region group grid, which
splits a value shared by two groups by territory (`region_groups.py`).
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from enum import Enum

from _bss.pabr_values.parser import parse_value_table
from _bss.pabr_values.tables import VALUE_TABLES
from _common.territory import territory_name
from _common.town import town_name
from .cell_join import NO_JOIN, CellJoin, GridRow, names
from .parser import cell_areas
from .region_groups import REGION_GROUP_COMPANIONS, region_group_rows

# The "no area" value of the grids that fill the map with it.
NONE_VALUE = 255
_VILLAGE_SIEGE_FILE = "villagesiegeinfo.bss"
_OCEAN_SIEGE_FILE = "oceansiegeinfo.bss"
# The siege area number of `villagesiegeinfo.bss` and `oceansiegeinfo.bss`
# (docs/file-formats/villagesiegeinfo_bss.md, Area Number): the number a grid cell holds.
_AREA_NUMBER = "area_number"


class KeyKind(Enum):
    """What the joined keys are; the value is the label key of the Keys column."""

    TERRITORY = "territoryKeys"
    REGION_GROUP = "regionGroupKeys"
    REGION = "regionKeys"


# (distinct cell values, companions by file name) -> joins by cell value.
JoinFn = Callable[[Iterable[int], Mapping[str, bytes]], dict[int, CellJoin]]
# (grid cells, companions by file name) -> the table rows.
RowsFn = Callable[[bytes, Mapping[str, bytes]], list[GridRow]]


@dataclass(frozen=True)
class GridKind:
    """One grid file: what its keys are, the companions it reads, how it builds its rows."""

    file_name: str
    key_kind: KeyKind
    rows: RowsFn
    companions: tuple[str, ...] = ()


def _value_rows(join: JoinFn) -> RowsFn:
    """One row per distinct cell value, joined by `join`."""

    def rows(cells: bytes, companions: Mapping[str, bytes]) -> list[GridRow]:
        areas = cell_areas(cells)
        joins = join([area.value for area in areas], companions)
        return [GridRow(area, joins.get(area.value, NO_JOIN)) for area in areas]

    return rows


def _territory_join(key_of: Callable[[int], int | None]) -> JoinFn:
    def join(values: Iterable[int], _companions: Mapping[str, bytes]) -> dict[int, CellJoin]:
        joins: dict[int, CellJoin] = {}
        for value in values:
            key = key_of(value)
            if key is not None:
                joins[value] = CellJoin((key,), names([territory_name(key)]))
        return joins

    return join


def _territory_key(value: int) -> int | None:
    return None if value == NONE_VALUE else value


def _conquest_territory_key(value: int) -> int | None:
    """The conquest grid stores territory key + 1; `0` is the map frame."""
    return None if value in (0, NONE_VALUE) else value - 1


def _area_join(table_file: str) -> JoinFn:
    """The region keys of the siege area row whose area number is the cell value."""
    (table,) = [table for table in VALUE_TABLES if table.file_name == table_file]

    def join(values: Iterable[int], companions: Mapping[str, bytes]) -> dict[int, CellJoin]:
        data = companions.get(table_file)
        if data is None:
            return {}
        areas = {row[_AREA_NUMBER]: tuple(row["region_keys"]) for row in parse_value_table(data, table)}
        return {
            value: CellJoin(areas[value], names([town_name(key) for key in areas[value]]))
            for value in values
            if value in areas
        }

    return join


_TERRITORY_ROWS = _value_rows(_territory_join(_territory_key))

GRID_KINDS: tuple[GridKind, ...] = (
    GridKind("worldmapterritorytypedata.bss", KeyKind.TERRITORY, _TERRITORY_ROWS),
    GridKind("worldmapmajorsiegeregiontypedata.bss", KeyKind.TERRITORY, _TERRITORY_ROWS),
    GridKind("worldmapmajorsiegeterritorytypedata.bss", KeyKind.TERRITORY, _TERRITORY_ROWS),
    GridKind(
        "worldmapterritorytypedataforconquest.bss",
        KeyKind.TERRITORY,
        _value_rows(_territory_join(_conquest_territory_key)),
    ),
    GridKind("worldmapfieldtypedata.bss", KeyKind.REGION_GROUP, region_group_rows, REGION_GROUP_COMPANIONS),
    GridKind(
        "worldmapsiegeregionforconquest.bss",
        KeyKind.REGION,
        _value_rows(_area_join(_VILLAGE_SIEGE_FILE)),
        (_VILLAGE_SIEGE_FILE,),
    ),
    GridKind(
        "worldmapoceansiegeregionforconquest.bss",
        KeyKind.REGION,
        _value_rows(_area_join(_OCEAN_SIEGE_FILE)),
        (_OCEAN_SIEGE_FILE,),
    ),
)
