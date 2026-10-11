"""Worldmap nodes for the Map view's node layer.

The nodes come from the `MAP_NODE` lookup index (`exploration.bss` joined with
the worldmap graph `mapdata_realexplore2.bwp` in `_bss/exploration/parser.py`):
kind, waypoint position, main or sub-node and sea node per node key. Each kind draws
its own world map icon (`map_icons.py`). Their links come from the
`NODE_LINKS` index, the graph's links between node keys.

Names follow `_common/node.py`, which the core may not import (`handler_api.py`):
LOC type 29 in the loaded language, the Korean `exploration.bss` name when LOC
has none, and a sub-node behind its parent, `Bambu Valley - Mining`.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from _common.loc import loc_text
from _common.lookup_index import IndexKind, LookupValue, index_entries, lookup

# LOC type of the node names, as `_common/node.py` LOC_NODE_NAME.
LOC_NODE_NAME = 29
# Icon of each node_kind, in the order of the client's CppEnums.ExplorationNodeType
# (`_bss/exploration/parser.py` NODE_KIND_NAMES): Normal, Viliage, City, Gate,
# Farm, Trade, Collect, Quarry, Logging, Dangerous, Finance, FishTrap,
# MinorFinance, MonopolyFarm, Craft, Excavation.
NODE_KIND_ICONS: tuple[str, ...] = (
    "node", "village", "city", "gate", "farm", "trade", "collect", "quarry", "logging",
    "dangerous", "finance", "fish_trap", "minor_finance", "monopoly_farm", "craft", "excavation",
)


@dataclass(frozen=True)
class MapNode:
    key: int
    name: str
    # None for a kind newer than NODE_KIND_ICONS: the page draws a dot.
    icon: str | None
    x: int
    z: int
    is_sub: bool
    # A node of the open sea (`_bss/exploration/parser.py` is_sea_node): its links are sea links.
    is_sea: bool = False
    # Keys of the nodes it links to with a higher key, so the page draws each link once.
    links: tuple[int, ...] = ()

    def to_dict(self) -> dict:
        return {
            "key": self.key,
            "name": self.name,
            "icon": self.icon,
            "x": self.x,
            "z": self.z,
            "sub": self.is_sub,
            "sea": self.is_sea,
            "links": list(self.links),
        }


def map_nodes() -> tuple[MapNode, ...]:
    """Every node of the loaded client with a position; empty when the index is not loaded."""
    entries = index_entries(IndexKind.MAP_NODE)
    nodes: list[MapNode] = []
    for key, value in entries.items():
        if not isinstance(value, tuple) or len(value) != 5:
            continue
        kind, x, z, is_sub, is_sea = value
        nodes.append(MapNode(
            key=key,
            name=_display_name(key, bool(is_sub)),
            icon=NODE_KIND_ICONS[kind] if 0 <= kind < len(NODE_KIND_ICONS) else None,
            x=x,
            z=z,
            is_sub=bool(is_sub),
            is_sea=bool(is_sea),
            links=_links(key, entries),
        ))
    return tuple(nodes)


def _links(key: int, nodes: Mapping[int, LookupValue]) -> tuple[int, ...]:
    """The keys of `nodes` that `key` links to and that are higher than it."""
    linked = lookup(IndexKind.NODE_LINKS, key)
    if not isinstance(linked, tuple):
        return ()
    return tuple(other for other in linked if other > key and other in nodes)


def _name(key: int) -> str:
    korean = lookup(IndexKind.NODE_NAME_KR, key)
    return loc_text(LOC_NODE_NAME, key) or (korean if isinstance(korean, str) else "")


def _display_name(key: int, is_sub: bool) -> str:
    """`Bambu Valley - Mining` for a sub-node with a named parent, else the node's own name."""
    name = _name(key)
    parent = lookup(IndexKind.NODE_PARENT, key) if is_sub else None
    parent_name = _name(parent) if isinstance(parent, int) else ""
    return f"{parent_name} - {name}" if name and parent_name else name
