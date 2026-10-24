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
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from enum import Enum

from _bss.pabr_values.parser import parse_value_table
from _bss.pabr_values.tables import VALUE_TABLES
from _bss.regiongroupinfo.parser import parse_regiongroupinfo_records
from _common.node import full_node_name
from _common.territory import territory_name
from _common.town import town_name

# The "no area" value of the grids that fill the map with it.
NONE_VALUE = 255
_LOW_BYTE = 0xFF
_REGION_GROUP_FILE = "regiongroupinfo.bss"
_VILLAGE_SIEGE_FILE = "villagesiegeinfo.bss"
_OCEAN_SIEGE_FILE = "oceansiegeinfo.bss"
# The u16 after the region list of the siege area tables: the number a grid cell holds.
_AREA_NUMBER = "area_number"


class KeyKind(Enum):
    """What the joined keys are; the value is the label key of the Keys column."""

    TERRITORY = "territoryKeys"
    REGION_GROUP = "regionGroupKeys"
    REGION = "regionKeys"


@dataclass(frozen=True)
class CellJoin:
    """The keys a cell value stands for and their names in the user's language."""

    keys: tuple[int, ...]
    names: tuple[str, ...]


# (distinct cell values, companion bytes or None) -> joins by cell value.
JoinFn = Callable[[Iterable[int], bytes | None], dict[int, CellJoin]]


@dataclass(frozen=True)
class GridKind:
    """One grid file: what its keys are, the companion it reads, how it joins."""

    file_name: str
    key_kind: KeyKind
    join: JoinFn
    companion: str | None = None


def _territory_join(key_of: Callable[[int], int | None]) -> JoinFn:
    def join(values: Iterable[int], _companion: bytes | None) -> dict[int, CellJoin]:
        joins: dict[int, CellJoin] = {}
        for value in values:
            key = key_of(value)
            if key is not None:
                joins[value] = CellJoin((key,), _names([territory_name(key)]))
        return joins

    return join


def _territory_key(value: int) -> int | None:
    return None if value == NONE_VALUE else value


def _conquest_territory_key(value: int) -> int | None:
    """The conquest grid stores territory key + 1; `0` is the map frame."""
    return None if value in (0, NONE_VALUE) else value - 1


def _region_group_join(values: Iterable[int], companion: bytes | None) -> dict[int, CellJoin]:
    """Every region group whose key has the cell value as its low byte.

    Keys from 256 on share a byte with a lower key (`2` and `258`), so a
    value can stand for two groups.
    """
    if companion is None:
        return {}
    groups: dict[int, list[dict]] = {}
    for row in parse_regiongroupinfo_records(companion):
        groups.setdefault(row["region_group_key"] & _LOW_BYTE, []).append(row)
    joins: dict[int, CellJoin] = {}
    for value in values:
        rows = sorted(groups.get(value, []), key=lambda row: row["region_group_key"])
        if rows:
            names = [full_node_name(row["node_key"]) for row in rows if row["node_key"]]
            joins[value] = CellJoin(tuple(row["region_group_key"] for row in rows), _names(names))
    return joins


def _area_join(table_file: str) -> JoinFn:
    """The region keys of the siege area row whose area number is the cell value."""
    (table,) = [table for table in VALUE_TABLES if table.file_name == table_file]

    def join(values: Iterable[int], companion: bytes | None) -> dict[int, CellJoin]:
        if companion is None:
            return {}
        areas = {row[_AREA_NUMBER]: tuple(row["region_keys"]) for row in parse_value_table(companion, table)}
        return {
            value: CellJoin(areas[value], _names([town_name(key) for key in areas[value]]))
            for value in values
            if value in areas
        }

    return join


def _names(names: list[str]) -> tuple[str, ...]:
    return tuple(name for name in names if name)


_TERRITORY = _territory_join(_territory_key)

GRID_KINDS: tuple[GridKind, ...] = (
    GridKind("worldmapterritorytypedata.bss", KeyKind.TERRITORY, _TERRITORY),
    GridKind("worldmapmajorsiegeregiontypedata.bss", KeyKind.TERRITORY, _TERRITORY),
    GridKind("worldmapmajorsiegeterritorytypedata.bss", KeyKind.TERRITORY, _TERRITORY),
    GridKind(
        "worldmapterritorytypedataforconquest.bss", KeyKind.TERRITORY, _territory_join(_conquest_territory_key)
    ),
    GridKind("worldmapfieldtypedata.bss", KeyKind.REGION_GROUP, _region_group_join, _REGION_GROUP_FILE),
    GridKind(
        "worldmapsiegeregionforconquest.bss", KeyKind.REGION, _area_join(_VILLAGE_SIEGE_FILE), _VILLAGE_SIEGE_FILE
    ),
    GridKind(
        "worldmapoceansiegeregionforconquest.bss", KeyKind.REGION, _area_join(_OCEAN_SIEGE_FILE), _OCEAN_SIEGE_FILE
    ),
)
