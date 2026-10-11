from __future__ import annotations

from collections.abc import Iterator

import pytest

from _bss.exploration.parser import NODE_KIND_NAMES
from _common.lookup_index import IndexKind, init_index
from map_icons import LAYOUT_ICONS
from map_nodes import NODE_KIND_ICONS, map_nodes

_KINDS = {name: kind for kind, name in enumerate(NODE_KIND_NAMES)}


@pytest.fixture
def indexes() -> Iterator[None]:
    kinds = (IndexKind.MAP_NODE, IndexKind.NODE_NAME_KR, IndexKind.NODE_PARENT, IndexKind.NODE_LINKS)
    yield
    for kind in kinds:
        init_index(kind, None)


def test_each_node_kind_draws_its_own_layout_control() -> None:
    # The client spells Village "Viliage" in the enum, not in the layout.
    controls = [f"Button_Node_{name.replace('Viliage', 'Village')}" for name in NODE_KIND_NAMES]

    assert [LAYOUT_ICONS[icon] for icon in NODE_KIND_ICONS] == controls


def test_nodes_come_from_the_index_with_korean_names_and_parents(indexes: None) -> None:
    # Keys no client has, so LOC never names them, loaded or not.
    init_index(IndexKind.MAP_NODE, {
        60063: (_KINDS["Normal"], 100, 200, 0, 0),
        60209: (_KINDS["Logging"], 150, 260, 1, 0),
        60999: (len(NODE_KIND_NAMES), 0, 0, 0, 0),
    })
    init_index(IndexKind.NODE_NAME_KR, {60063: "장로의 다리", 60209: "벌목"})
    init_index(IndexKind.NODE_PARENT, {60209: 60063})

    nodes = {node.key: node for node in map_nodes()}

    assert (nodes[60063].name, nodes[60063].icon, nodes[60063].x, nodes[60063].z, nodes[60063].is_sub) == ("장로의 다리", "node", 100, 200, False)
    assert (nodes[60209].name, nodes[60209].icon, nodes[60209].is_sub) == ("장로의 다리 - 벌목", "logging", True)
    assert nodes[60999].icon is None


def test_no_nodes_without_the_index(indexes: None) -> None:
    init_index(IndexKind.MAP_NODE, None)

    assert map_nodes() == ()


def test_a_node_lists_its_links_to_higher_map_nodes_once(indexes: None) -> None:
    init_index(IndexKind.MAP_NODE, {
        60001: (_KINDS["Normal"], 0, 0, 0, 1),
        60002: (_KINDS["Normal"], 1, 1, 0, 0),
        60003: (_KINDS["City"], 2, 2, 0, 0),
    })
    # 60009 is no map node (disabled or without a waypoint): no link to it.
    init_index(IndexKind.NODE_LINKS, {60001: (60002, 60003, 60009), 60002: (60001,), 60003: (60001,)})

    links = {node.key: node.links for node in map_nodes()}

    assert links == {60001: (60002, 60003), 60002: (), 60003: ()}
    assert {node.key for node in map_nodes() if node.is_sea} == {60001}
