"""`exploration.bss`: the worldmap node table.

    PABR | u32 count | count x (117-byte head + 7 counted u32 lists)
    | footer (u32 count + 6-byte rows) | string table | u32 string_table_start | u32 0

Records tile the file exactly, so they are walked, not searched for. Node names
come from LOC type 29 keyed by `node_key`; the string table holds the Korean
source names. Full layout in docs/file-formats/exploration_bss.md.
"""

from __future__ import annotations

import struct

from _bwp.waypoint.parser import is_waypoint_graph, neighbours, parse_waypoint_graph
from _common.binary import u16, u32
from _common.pabr_strings import TRAILER_SIZE, check_rows_end, read_string_table, string_at, string_table_start


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_HEAD_SIZE = 117
_LIST_COUNT = 7
# Lists 1 to 5 hold knowledge entry IDs; list 0 is a region hash, list 6 empty.
_KNOWLEDGE_LISTS = range(1, 6)

# Head field offsets.
_ENABLED = 0x04
_NODE_KIND = 0x05
_NAME_INDEX = 0x0A
_RADIUS = 0x1F
_MANAGER_ID = 0x2B
_REPRESENTATIVE_ID = 0x2D
_CONTRIBUTION = 0x5E
_IS_SUB_NODE = 0x74

# CppEnums.ExplorationNodeType from global_define_cpp_enum.luac, without the
# "eExplorationNodeType_" prefix and in the client's spelling.
NODE_KIND_NAMES: tuple[str, ...] = (
    "Normal", "Viliage", "City", "Gate", "Farm", "Trade", "Collect", "Quarry",
    "Logging", "Dangerous", "Finance", "FishTrap", "MinorFinance", "MonopolyFarm",
    "Craft", "Excavation",
)


def _read_lists(data: bytes, pos: int) -> tuple[list[list[int]], int]:
    lists: list[list[int]] = []
    for _ in range(_LIST_COUNT):
        count = u32(data, pos)
        end = pos + 4 + 4 * count
        if end > len(data):
            raise ValueError(f"exploration.bss list at 0x{pos:X} runs past the end of the file")
        lists.append(list(struct.unpack_from(f"<{count}I", data, pos + 4)))
        pos = end
    return lists, pos


def parse_exploration_records(data: bytes) -> list[dict]:
    """Every node in file order.

    Raises ValueError on a bad magic, or when the walk does not end where the
    string table starts: then the layout has changed and every field is suspect.
    """
    if len(data) < _HEADER_SIZE + TRAILER_SIZE or data[:4] != _MAGIC:
        raise ValueError("exploration.bss has invalid magic.")

    strings = read_string_table(data)
    count = u32(data, 4)
    pos = _HEADER_SIZE
    records: list[dict] = []

    for _ in range(count):
        head = pos
        lists, pos = _read_lists(data, head + _HEAD_SIZE)
        name_index = u16(data, head + _NAME_INDEX)
        records.append({
            "node_key": u16(data, head),
            "enabled": data[head + _ENABLED],
            "node_kind": data[head + _NODE_KIND],
            "name_kr": string_at(strings, name_index),
            "is_sub_node": data[head + _IS_SUB_NODE],
            "contribution": data[head + _CONTRIBUTION],
            "manager_id": u16(data, head + _MANAGER_ID),
            "representative_id": u16(data, head + _REPRESENTATIVE_ID),
            "radius": struct.unpack_from("<f", data, head + _RADIUS)[0],
            "knowledge_ids": [key for index in _KNOWLEDGE_LISTS for key in lists[index]],
        })

    footer_count = u32(data, pos)
    check_rows_end(data, pos + 4 + 6 * footer_count, "exploration.bss records")

    return records


def is_sea_node(record: dict) -> bool:
    """A node of the open sea: a Normal main node with no contribution cost.

    On client 3464 these are the 51 Margoria, Ross Sea, Vadabin and Juur Sea
    nodes (keys 1400 to 1452), Tiamat Sea and Oceanus Sea, and Red Battlefield
    and Pit of the Undying, which have no worldmap links.
    """
    return record["node_kind"] == 0 and not record["is_sub_node"] and record["contribution"] == 0


def build_map_node_index(exploration: bytes, worldmap: bytes) -> dict[int, tuple[int, ...]]:
    """The `MAP_NODE` index: each enabled node key to (node_kind, x, z, is_sub_node, is_sea).

    The position is the node's waypoint in `mapdata_realexplore2.bwp`, in
    whole world cm; a sub-node has its own there, while its `exploration.bss`
    position repeats its parent's. `is_sea` is `is_sea_node()`. Nodes without
    a waypoint are left out, and so are nodes with no exploration radius: the
    game cannot find them (on client 3464 only Duvencrune 1651, a second
    Duvencrune far off the map). An unreadable graph yields an empty index.
    """
    if not is_waypoint_graph(worldmap):
        return {}
    waypoints = {waypoint.key: waypoint for waypoint in parse_waypoint_graph(worldmap).waypoints}
    index: dict[int, tuple[int, ...]] = {}
    for record in parse_exploration_records(exploration):
        waypoint = waypoints.get(record["node_key"])
        if record["enabled"] and record["radius"] > 0 and waypoint is not None:
            index[record["node_key"]] = (
                record["node_kind"],
                round(waypoint.x),
                round(waypoint.z),
                record["is_sub_node"],
                int(is_sea_node(record)),
            )
    return index


def build_node_name_kr_index(exploration: bytes) -> dict[int, str]:
    """The `NODE_NAME_KR` index: each node key to its Korean source name, the fallback for LOC type 29."""
    return {
        record["node_key"]: record["name_kr"]
        for record in parse_exploration_records(exploration)
        if record["name_kr"]
    }


def build_node_parent_index(exploration: bytes, worldmap: bytes) -> dict[int, int]:
    """The `NODE_PARENT` index: each sub-node key to the node it hangs off.

    A sub-node (Mining, an investment bank, a fish drying yard) links to its
    parent alone in `mapdata_realexplore2.bwp`; sub-nodes with no link or
    several are left out. An unreadable graph yields an empty index.
    """
    if not is_waypoint_graph(worldmap):
        return {}
    links = neighbours(parse_waypoint_graph(worldmap))
    sub_nodes = [
        record["node_key"]
        for record in parse_exploration_records(exploration)
        if record["is_sub_node"]
    ]
    return {
        key: next(iter(links[key]))
        for key in sub_nodes
        if len(links.get(key, frozenset())) == 1
    }
