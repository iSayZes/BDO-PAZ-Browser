"""The worldmap node graph, `mapdata_realexplore2.bwp`, as a companion file.

Its waypoint keys are `exploration.bss` node keys, and it stores every link
both ways. Tables under `gamecommondata/binary/` load it from the sibling
`waypoint_binary/` folder.
"""

from __future__ import annotations

from collections.abc import Mapping

from bdo_models import PazEntry

from .parser import Waypoint, is_waypoint_graph, neighbours, parse_waypoint_graph


WORLDMAP_FILE = "mapdata_realexplore2.bwp"
_WORLDMAP_FOLDER = "waypoint_binary"


def worldmap_companion(entry: PazEntry) -> str:
    """Internal path of the worldmap graph for a table in `gamecommondata/binary/`."""
    root = entry.internal_path.rsplit("/", 2)[0]
    return f"{root}/{_WORLDMAP_FOLDER}/{WORLDMAP_FILE}"


def worldmap_links(companions: Mapping[str, bytes]) -> dict[int, frozenset[int]]:
    """Node key -> every node key it links to; empty when the graph is missing or not PABR."""
    worldmap = companions.get(WORLDMAP_FILE)
    if worldmap is None or not is_waypoint_graph(worldmap):
        return {}
    return neighbours(parse_waypoint_graph(worldmap))


def build_node_link_index(worldmap: bytes) -> dict[int, tuple[int, ...]]:
    """The `NODE_LINKS` index: each node key to the node keys it links to, ascending.

    The graph stores every link both ways, so each link is in the index twice,
    once under each end. An unreadable graph yields an empty index.
    """
    if not is_waypoint_graph(worldmap):
        return {}
    return {key: tuple(sorted(keys)) for key, keys in neighbours(parse_waypoint_graph(worldmap)).items()}


def worldmap_waypoints(companions: Mapping[str, bytes]) -> tuple[Waypoint, ...]:
    """Every worldmap node with its position; empty when the graph is missing or not PABR."""
    worldmap = companions.get(WORLDMAP_FILE)
    if worldmap is None or not is_waypoint_graph(worldmap):
        return ()
    return parse_waypoint_graph(worldmap).waypoints
