from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from bdo_models import PazEntry
from bdo_preview import get_handler
from _bwp.waypoint.parser import Group, Route, is_waypoint_graph, neighbours, parse_waypoint_graph
from _bwp.waypoint.worldmap import build_node_link_index
from tests.fixtures import FIXTURES_DIR, fetch_missing
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)


CASE = HandlerCase(
    handler_name="mapdata_realexplore2.bwp",
    data_file="mapdata_realexplore2.bwp",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/waypoint_binary/mapdata_realexplore2.bwp",
    tests=[
        SchemaTest(
            required_keys=[
                "key", "name", "x", "y", "z", "property", "property_name",
                "is_sub_waypoint", "is_escape", "links", "link_count",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="key", value=1, expected={"name": "town(velia)", "property_name": "ground"}),
        # A Godu Village farm links only to the village.
        TargetTest(
            col="key",
            value=1880,
            expected={"name": "hidden_field_goduvillage_2", "links": [1857], "is_sub_waypoint": False},
        ),
    ],
)


@pytest.fixture(scope="module")
def waypoint_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_mapdata_realexplore2_bwp(spec: Any, waypoint_result: HandlerResult) -> None:
    waypoint_result.check(spec)


def test_links_join_waypoints_of_the_file(waypoint_result: HandlerResult) -> None:
    keys = {record["key"] for record in waypoint_result.records}
    assert all(set(record["links"]) <= keys for record in waypoint_result.records)


def _strings(values: list[str]) -> bytes:
    body = b"".join(
        struct.pack("<BI", 1, len(value) * 2) + value.encode("utf-16-le") for value in values
    )
    return struct.pack("<I", len(values)) + body


def _graph_bytes() -> bytes:
    """Two waypoints, one link both ways, one group and one route."""
    waypoints = struct.pack("<IIfffBBB", 10, 0, 1.0, 2.0, 3.0, 0x10, 0, 0)
    waypoints += struct.pack("<IIfffBBB", 11, 1, 4.0, 5.0, 6.0, 0x40, 1, 0)
    links = struct.pack("<I", 2) + struct.pack("<IIII", 10, 11, 11, 10)
    # The group reuses waypoint 11's name: the table stores each string once.
    groups = struct.pack("<B", 1) + struct.pack("<II", 7, 1)
    routes = struct.pack("<I", 1) + struct.pack("<IIIIII", 3, 2, 2, 10, 11, 0)
    body = b"PABR" + struct.pack("<I", 2) + waypoints + links + groups + routes
    table_start = len(body)
    return body + _strings(["a", "b", "route_a"]) + struct.pack("<II", table_start, 0)


def test_parse_reads_groups_routes_and_shared_names() -> None:
    graph = parse_waypoint_graph(_graph_bytes())

    assert [(w.key, w.name, w.property, w.is_sub_waypoint) for w in graph.waypoints] == [
        (10, "a", 0x10, False),
        (11, "b", 0x40, True),
    ]
    assert graph.groups == (Group(7, "b"),)
    assert graph.routes == (Route(3, "route_a", (10, 11), 0),)
    assert neighbours(graph) == {10: frozenset({11}), 11: frozenset({10})}


def test_parse_rejects_a_walk_that_misses_the_string_table() -> None:
    data = bytearray(_graph_bytes())
    # A route count of 0 leaves the route bytes unread before the string table.
    routes_at = data.index(struct.pack("<IIIIII", 3, 2, 2, 10, 11, 0)) - 4
    data[routes_at : routes_at + 4] = struct.pack("<I", 0)
    with pytest.raises(ValueError, match="string table"):
        parse_waypoint_graph(bytes(data))


def test_parse_rejects_files_without_pabr_magic() -> None:
    with pytest.raises(ValueError, match="PABR"):
        parse_waypoint_graph(bytes(16))


# The old instance dungeon templates, which have no PABR magic and are left
# unread, with their size on client 3458. They are empty in the XML too; a
# template that grows may hold data now, so its layout needs a new look.
_OLD_TEMPLATE_SIZES = {
    "mapdata_instancedungeonauto_map.bwp": 281,
    "mapdata_instancedungeonbattlefield.bwp": 281,
    "mapdata_instancedungeoncarriage.bwp": 281,
    "mapdata_instancedungeonexplore.bwp": 13,
    "mapdata_instancedungeonexplore2.bwp": 13,
    "mapdata_instancedungeoninstance_waypoint.bwp": 728,
    "mapdata_instancedungeonmonster_patrol.bwp": 281,
    "mapdata_instancedungeonmonster_random.bwp": 281,
    "mapdata_instancedungeonnpc.bwp": 281,
    "mapdata_instancedungeonnpc_route.bwp": 281,
    "mapdata_instancedungeonoffering_carrier.bwp": 13,
    "mapdata_instancedungeonteleport.bwp": 46,
}


def _fixture_bytes(name: str) -> bytes:
    fetch_missing([name])
    return (FIXTURES_DIR / name).read_bytes()


@pytest.mark.parametrize("name", sorted(_OLD_TEMPLATE_SIZES))
def test_old_template_has_not_grown(name: str) -> None:
    data = _fixture_bytes(name)
    assert not is_waypoint_graph(data), f"{name} is a PABR graph now: drop it from _OLD_TEMPLATE_SIZES"
    assert len(data) <= _OLD_TEMPLATE_SIZES[name], (
        f"{name} grew from {_OLD_TEMPLATE_SIZES[name]} to {len(data)} bytes: check its layout again"
    )


def test_old_template_shows_notice_in_default_sort() -> None:
    name = "mapdata_instancedungeonexplore.bwp"
    data = _fixture_bytes(name)
    entry = PazEntry("", f"gamecommondata/waypoint_binary/{name}", 0, 0, 0, 0, 0)
    handler = get_handler(name, ".bwp")
    sort = handler.default_sort()

    assert sort is not None
    file_order = handler.render_data_page(data, entry, {}, 0, 50)
    assert handler.render_sorted_page(data, entry, {}, 0, 50, sort) == file_order


def test_node_link_index_lists_each_link_under_both_ends() -> None:
    assert build_node_link_index(_graph_bytes()) == {10: (11,), 11: (10,)}


def test_node_link_index_is_empty_without_a_graph() -> None:
    assert build_node_link_index(b"not a graph") == {}
