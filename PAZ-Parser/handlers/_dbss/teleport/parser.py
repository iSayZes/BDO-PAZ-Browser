"""`teleport.dbss` and `teleportoffset.dbss`: the destinations of teleport buffs.

    u32 section_count | section_count x (u32 count | count x 18-byte record)
    record: u32 key | u8 section | f32 x | f32 y | f32 z | u8 destination

A buff of effect type 23 names a point by section (`param_1`) and key
(`param_2`). The offset file holds the same sections without a section count,
as (index, offset, size) rows, where index is the record's position in its
section, not its key.
Full layout in docs/file-formats/dbss/teleport_dbss.md.
"""

from __future__ import annotations

import struct

from _bwp.waypoint.parser import is_waypoint_graph, parse_waypoint_graph
from _common.binary import u32
from _common.teleport import teleport_point_id
from .nearest import NamedNode, nearest_node


_RECORD = struct.Struct("<IB3fB")
_OFFSET_ROW = struct.Struct("<3I")
_COUNT_SIZE = 4


def _sections(data: bytes, pos: int, row_size: int, name: str, section_count: int | None) -> list[tuple[int, int]]:
    """(start, count) of each section from `pos`, checking they fill the file exactly.

    `teleport.dbss` declares `section_count`; `teleportoffset.dbss` does not,
    so its sections run to the end of the file (None).
    """
    sections: list[tuple[int, int]] = []
    while (section_count is None and pos < len(data)) or (
        section_count is not None and len(sections) < section_count
    ):
        if pos + _COUNT_SIZE > len(data):
            raise ValueError(f"{name} section {len(sections)} starts past the end of the file")
        count = u32(data, pos)
        start = pos + _COUNT_SIZE
        sections.append((start, count))
        pos = start + count * row_size
    if pos != len(data):
        raise ValueError(f"{name} sections end at {pos}, the file at {len(data)}")
    return sections


def parse_teleport_records(data: bytes) -> list[dict]:
    """Every point, section by section in file order.

    Raises ValueError when the sections do not fill the file exactly or a
    record names another section than the one it sits in: then the layout has
    changed and every field is suspect.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError("teleport.dbss is too short for its section count")
    sections = _sections(data, _COUNT_SIZE, _RECORD.size, "teleport.dbss", u32(data, 0))
    records: list[dict] = []
    for section, (start, count) in enumerate(sections):
        for index in range(count):
            key, stored_section, x, y, z, destination = _RECORD.unpack_from(data, start + index * _RECORD.size)
            if stored_section != section:
                raise ValueError(
                    f"teleport.dbss record {index} of section {section} names section {stored_section}"
                )
            records.append({
                "section": section,
                "key": key,
                "x": x,
                "y": y,
                "z": z,
                "destination": destination,
            })
    return records


def parse_teleport_offset_rows(data: bytes) -> list[dict]:
    """Every `teleportoffset.dbss` row, section by section in file order (a hash order)."""
    rows: list[dict] = []
    sections = _sections(data, 0, _OFFSET_ROW.size, "teleportoffset.dbss", None)
    for section, (start, count) in enumerate(sections):
        for row in range(count):
            index, offset, size = _OFFSET_ROW.unpack_from(data, start + row * _OFFSET_ROW.size)
            rows.append({"section": section, "index": index, "offset": offset, "size": size})
    return rows


def build_teleport_nearest_node_index(data: bytes, worldmap: bytes) -> dict[int, tuple[int, int]]:
    """The `TELEPORT_NEAREST_NODE` index: each point to (nearest worldmap node key, metres).

    Built without LOC over every worldmap node; that picks the same node as
    the table's named-node search on all but one point of client 3458. An
    unreadable graph yields an empty index.
    """
    if not is_waypoint_graph(worldmap):
        return {}
    nodes = [NamedNode(node.key, node.name, node.x, node.z) for node in parse_waypoint_graph(worldmap).waypoints]
    index: dict[int, tuple[int, int]] = {}
    for record in parse_teleport_records(data):
        nearest = nearest_node(record["x"], record["z"], nodes)
        if nearest is not None:
            point_id = teleport_point_id(record["section"], record["key"])
            index[point_id] = (nearest.key, round(nearest.distance_m))
    return index
