"""The rows of `worldmapfieldtypedata.bss`: region groups, split by territory.

A cell holds the low byte of a `regiongroupinfo.bss` key, so a key from 256
on shares its value with the key 256 lower (`2` and `258`). The territory
grid `worldmapterritorytypedata.bss` and the regions of `regioninfo.bss` tell
the two groups apart (docs/file-formats/bss/worldmapgrid_bss.md, Shared Values):
a group whose regions all lie in one territory owns the value's cells in that
territory. The value's other cells go to the groups that own no territory
(group `0`, whose regions lie in several), or to every group of the value
when each owns one. Without the territory grid or `regioninfo.bss`, a shared
value keeps one row with every group's key.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass

from _bss.regiongroupinfo.parser import parse_regiongroupinfo_records
from _bss.regioninfo.parser import parse_regioninfo_records
from _common.node import full_node_name
from .cell_join import NO_JOIN, CellJoin, GridRow, names
from .parser import CellArea, cell_areas, merge_areas, read_cells, split_areas

_LOW_BYTE = 0xFF
_REGION_GROUP_FILE = "regiongroupinfo.bss"
_REGION_FILE = "regioninfo.bss"
_TERRITORY_GRID_FILE = "worldmapterritorytypedata.bss"
REGION_GROUP_COMPANIONS = (_REGION_GROUP_FILE, _REGION_FILE, _TERRITORY_GRID_FILE)


@dataclass(frozen=True)
class ValueSplit:
    """Which region groups of one shared cell value the cells of each territory join."""

    owners: Mapping[int, int]
    """Territory key -> the region group key that owns the value's cells there."""
    rest: tuple[int, ...]
    """The region group keys of the value's cells in a territory nobody owns."""

    def keys_in(self, territory_key: int) -> tuple[int, ...]:
        owner = self.owners.get(territory_key)
        return self.rest if owner is None else (owner,)


def split_value(group_keys: Sequence[int], territories: Mapping[int, frozenset[int]]) -> ValueSplit:
    """How the cells of a value that `group_keys` share split by territory.

    `territories` maps a region group key to the territory keys of its
    regions. A group with regions in one territory claims it; a territory
    two groups claim has no owner.
    """
    claims: dict[int, list[int]] = {}
    for key in group_keys:
        group_territories = territories.get(key, frozenset())
        if len(group_territories) == 1:
            (territory,) = group_territories
            claims.setdefault(territory, []).append(key)
    owners = {territory: keys[0] for territory, keys in claims.items() if len(keys) == 1}
    owning = set(owners.values())
    rest = tuple(key for key in group_keys if key not in owning) or tuple(group_keys)
    return ValueSplit(owners, rest)


def region_group_rows(cells: bytes, companions: Mapping[str, bytes]) -> list[GridRow]:
    """One row per cell value, and one per group (by territory) for a value groups share."""
    areas = cell_areas(cells)
    group_data = companions.get(_REGION_GROUP_FILE)
    if group_data is None:
        return [GridRow(area, NO_JOIN) for area in areas]
    groups = _groups_by_value(parse_regiongroupinfo_records(group_data))
    split = _split_rows(cells, groups, companions)
    rows: list[GridRow] = []
    for area in areas:
        rows.extend(split.get(area.value) or [GridRow(area, _join(groups.get(area.value, [])))])
    return rows


def _groups_by_value(group_rows: Iterable[dict]) -> dict[int, list[dict]]:
    """Cell value (key low byte) -> its `regiongroupinfo.bss` rows, in key order."""
    groups: dict[int, list[dict]] = {}
    for row in sorted(group_rows, key=lambda row: row["region_group_key"]):
        groups.setdefault(row["region_group_key"] & _LOW_BYTE, []).append(row)
    return groups


def _split_rows(
    cells: bytes, groups: Mapping[int, list[dict]], companions: Mapping[str, bytes]
) -> dict[int, list[GridRow]]:
    """Cell value -> its rows by group, for the values two or more groups share."""
    region_data = companions.get(_REGION_FILE)
    territory_grid = companions.get(_TERRITORY_GRID_FILE)
    shared = {value: rows for value, rows in groups.items() if len(rows) > 1}
    if not shared or region_data is None or territory_grid is None:
        return {}
    territories = _group_territories(parse_regioninfo_records(region_data))
    splits = {
        value: split_value([row["region_group_key"] for row in rows], territories) for value, rows in shared.items()
    }
    territory_cells = read_cells(territory_grid, _TERRITORY_GRID_FILE)
    by_keys: dict[int, dict[tuple[int, ...], list[CellArea]]] = {}
    for (value, territory), area in split_areas(cells, territory_cells, shared).items():
        keys = splits[value].keys_in(territory)
        by_keys.setdefault(value, {}).setdefault(keys, []).append(area)
    return {
        value: [
            GridRow(merge_areas(areas), _join([row for row in shared[value] if row["region_group_key"] in keys]))
            for keys, areas in sorted(areas_by_keys.items())
        ]
        for value, areas_by_keys in by_keys.items()
    }


def _group_territories(regions: Iterable[dict]) -> dict[int, frozenset[int]]:
    """Region group key -> the territory keys of its `regioninfo.bss` regions."""
    territories: dict[int, set[int]] = {}
    for region in regions:
        territories.setdefault(region["region_group_key"], set()).add(region["territory_key"])
    return {key: frozenset(keys) for key, keys in territories.items()}


def _join(group_rows: Sequence[dict]) -> CellJoin:
    """The group keys and the names of their worldmap nodes."""
    if not group_rows:
        return NO_JOIN
    node_names = [full_node_name(row["node_key"]) for row in group_rows if row["node_key"]]
    return CellJoin(tuple(row["region_group_key"] for row in group_rows), names(node_names))
