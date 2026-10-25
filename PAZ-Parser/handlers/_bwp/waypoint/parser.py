"""`*.bwp`: waypoint graphs, the binary form of `gamecommondata/waypoint/*.xml`.

    PABR | u32 waypoint_count | waypoint_count x 23-byte waypoint
    | u32 link_count | link_count x (u32 source_key, u32 target_key)
    | u8 group_count | group_count x (u32 group_key, u32 name_ref)
    | u32 route_count | route_count x route
    | string table | u32 string_table_start | u32 0

    waypoint: u32 key | u32 index | f32 x | f32 y | f32 z | u8 property
              | u8 is_sub_waypoint | u8 is_escape
    route:    u32 route_key | u32 name_ref | u32 point_count
              | point_count x u32 waypoint_key | u32 unknown_waypoint_keys_00

Waypoint names are string `index` of the table; groups and routes point into
it by `name_ref`. Full layout in docs/file-formats/other/waypoint_bwp.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_strings import TRAILER_SIZE, check_rows_end, read_string_table, string_at, string_table_start


_MAGIC = b"PABR"
_HEADER_SIZE = 8

_WAYPOINT = struct.Struct("<IIfffBBB")
_LINK = struct.Struct("<II")
_GROUP = struct.Struct("<II")
_ROUTE_HEAD = struct.Struct("<III")
_U32 = 4

# Movement flags; "all" sets every bit.
PROPERTY_NAMES: dict[int, str] = {
    0x00: "none",
    0x01: "air",
    0x02: "wall",
    0x10: "ground",
    0x40: "water",
    0xFF: "all",
}


@dataclass(frozen=True)
class Waypoint:
    key: int
    name: str
    x: float
    y: float
    z: float
    property: int
    is_sub_waypoint: bool
    is_escape: bool


@dataclass(frozen=True)
class Group:
    key: int
    name: str


@dataclass(frozen=True)
class Route:
    key: int
    name: str
    waypoint_keys: tuple[int, ...]
    unknown_waypoint_keys_00: int


@dataclass(frozen=True)
class WaypointGraph:
    waypoints: tuple[Waypoint, ...]
    # Directed (source_key, target_key). The worldmap graph stores every link
    # both ways; patrol graphs also hold one-way links.
    links: tuple[tuple[int, int], ...]
    groups: tuple[Group, ...]
    routes: tuple[Route, ...]


def is_waypoint_graph(data: bytes) -> bool:
    """Whether `data` has the PABR layout; a few `instancedungeon*` templates do not."""
    return len(data) >= _HEADER_SIZE + TRAILER_SIZE and data[:4] == _MAGIC


def parse_waypoint_graph(data: bytes) -> WaypointGraph:
    """Every section of a waypoint graph.

    Raises ValueError on a bad magic, a waypoint whose index is not its row,
    or a walk that does not end where the string table starts: then the
    layout has changed and every later field is suspect.
    """
    if not is_waypoint_graph(data):
        raise ValueError("not a PABR waypoint graph")

    strings = read_string_table(data)
    waypoints, pos = _read_waypoints(data, strings)
    links, pos = _read_fixed(data, pos, u32(data, pos), _LINK, _U32)
    group_rows, pos = _read_fixed(data, pos, data[pos], _GROUP, 1)
    routes, pos = _read_routes(data, pos, strings)

    check_rows_end(data, pos, "waypoint graph sections")

    return WaypointGraph(
        waypoints=waypoints,
        links=tuple(links),
        groups=tuple(Group(key, string_at(strings, ref)) for key, ref in group_rows),
        routes=routes,
    )


def neighbours(graph: WaypointGraph) -> dict[int, frozenset[int]]:
    """Waypoint key -> every key it links to, in either direction."""
    linked: dict[int, set[int]] = {}
    for source, target in graph.links:
        linked.setdefault(source, set()).add(target)
        linked.setdefault(target, set()).add(source)
    return {key: frozenset(keys) for key, keys in linked.items()}


def _read_waypoints(data: bytes, strings: list[str]) -> tuple[tuple[Waypoint, ...], int]:
    count = u32(data, _HEADER_SIZE - _U32)
    pos = _HEADER_SIZE
    waypoints: list[Waypoint] = []
    for row in range(count):
        key, index, x, y, z, prop, is_sub, is_escape = _WAYPOINT.unpack_from(data, pos)
        if index != row:
            raise ValueError(f"waypoint {key} at row {row} stores index {index}")
        waypoints.append(Waypoint(key, string_at(strings, index), x, y, z, prop, bool(is_sub), bool(is_escape)))
        pos += _WAYPOINT.size
    return tuple(waypoints), pos


def _read_fixed(
    data: bytes,
    pos: int,
    count: int,
    row: struct.Struct,
    count_size: int,
) -> tuple[list[tuple[int, int]], int]:
    """`count` rows of `row` after a count field of `count_size` bytes at `pos`."""
    start = pos + count_size
    end = start + count * row.size
    if end > len(data):
        raise ValueError(f"waypoint graph declares {count:,} rows at 0x{pos:X} past the end of the file")
    return [tuple(fields) for fields in row.iter_unpack(data[start:end])], end


def _read_routes(data: bytes, pos: int, strings: list[str]) -> tuple[tuple[Route, ...], int]:
    count = u32(data, pos)
    pos += _U32
    routes: list[Route] = []
    for _ in range(count):
        key, name_ref, point_count = _ROUTE_HEAD.unpack_from(data, pos)
        pos += _ROUTE_HEAD.size
        points = struct.unpack_from(f"<{point_count}I", data, pos)
        pos += point_count * _U32
        routes.append(Route(key, string_at(strings, name_ref), points, u32(data, pos)))
        pos += _U32
    return tuple(routes), pos
