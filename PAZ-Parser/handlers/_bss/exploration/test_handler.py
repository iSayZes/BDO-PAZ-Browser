from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _bss.exploration.connections import connection_fields
from _bss.exploration.parser import (
    NODE_KIND_NAMES,
    build_map_node_index,
    build_node_name_kr_index,
    build_node_parent_index,
)
from _bwp.waypoint.worldmap import WORLDMAP_FILE
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)


CASE = HandlerCase(
    handler_name="exploration.bss",
    data_file="exploration.bss",
    companion_files={"mapdata_realexplore2.bwp": "mapdata_realexplore2.bwp"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Node Name", "Connected Nodes"],
    internal_path="gamecommondata/binary/exploration.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "node_key",
                "node_name",
                "name_kr",
                "node_kind",
                "kind",
                "enabled",
                "is_sub_node",
                "main_sub",
                "contribution",
                "manager_id",
                "manager",
                "representative_id",
                "representative",
                "radius",
                "knowledge_ids",
                "knowledge_count",
                "knowledge_names",
                "knowledge_text",
                "connection_keys",
                "connection_count",
                "connection_names",
                "connection_text",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        # CppEnums.ExplorationNodeType has 16 members.
        RangeTest(col="node_kind", min_val=0, max_val=15),
        RangeTest(col="enabled", min_val=0, max_val=1),
        RangeTest(col="is_sub_node", min_val=0, max_val=1),
        RangeTest(col="radius", min_val=0.0, max_val=float("inf")),
        # Named through LOC type 29. Type 34 (knowledge) gave "Cron Castle Altar".
        TargetTest(
            col="node_key",
            value=65,
            expected={
                "node_name": "Wale Farm",
                "name_kr": "웨일 농장",
                "kind": "Normal",
                "main_sub": "Main",
                "manager_id": 40605,
                "knowledge_ids": [389],
                "knowledge_names": ["Wale"],
            },
        ),
        TargetTest(
            col="node_key",
            value=1,
            expected={
                "node_name": "Velia",
                "kind": "City",
                "manager": None,
                "representative_id": 40017,
            },
        ),
        TargetTest(
            col="node_key",
            value=3,
            expected={"node_name": "Cron Castle", "kind": "Dangerous"},
        ),
    ],
)


@pytest.fixture(scope="module")
def exploration_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_exploration_bss(
    spec: Any,
    exploration_result: HandlerResult,
) -> None:
    exploration_result.check(spec)


def _record(result: HandlerResult, node_key: int) -> dict:
    return next(record for record in result.records if record["node_key"] == node_key)


@pytest.mark.parametrize(
    ("node_key", "linked_key", "linked_name"),
    [
        (1, 21, "Bartali Farm"),  # Velia
        (2, 45, "Toscani Farm"),  # Western Guard Camp
        (65, 61, "Olvia"),  # Wale Farm
    ],
)
def test_node_lists_its_worldmap_link(
    exploration_result: HandlerResult,
    node_key: int,
    linked_key: int,
    linked_name: str,
) -> None:
    record = _record(exploration_result, node_key)
    assert linked_key in record["connection_keys"]
    assert record["connection_names"][record["connection_keys"].index(linked_key)] == linked_name


def test_connections_are_symmetric(exploration_result: HandlerResult) -> None:
    """The worldmap stores every link both ways, so each node lists the other."""
    by_key = {record["node_key"]: record for record in exploration_result.records}
    one_way = [
        (record["node_key"], key)
        for record in exploration_result.records
        for key in record["connection_keys"]
        if key in by_key and record["node_key"] not in by_key[key]["connection_keys"]
    ]
    assert one_way == []


def test_connection_fields_agree(exploration_result: HandlerResult) -> None:
    for record in exploration_result.records:
        assert record["connection_count"] == len(record["connection_keys"]) == len(record["connection_names"])
        assert record["connection_text"] == ", ".join(record["connection_names"])


def test_connection_names_fall_back_to_loc_then_the_key() -> None:
    links = {1: frozenset({4, 3, 2})}
    fields = connection_fields(1, links, {2: "Farm"}, lambda key: "Sea" if key == 3 else "")
    assert fields["connection_keys"] == [2, 3, 4]
    assert fields["connection_names"] == ["Farm", "Sea", "4"]


def test_node_without_links_has_no_connections() -> None:
    fields = connection_fields(1, {}, {}, lambda key: "")
    assert (fields["connection_keys"], fields["connection_count"], fields["connection_text"]) == ([], 0, "")


@pytest.mark.parametrize(
    ("sub_node", "parent"),
    [
        (209, 63),  # Elder's Bridge - Lumbering
        (401, 301),  # Luciano Pietro Investment Bank, Calpheon
        (1035, 1012),  # Taramura Island - Fish Drying Yard 1
    ],
)
def test_node_parent_index_names_the_parent_of_a_sub_node(
    exploration_result: HandlerResult,
    sub_node: int,
    parent: int,
) -> None:
    source = exploration_result.source
    index = build_node_parent_index(source.data, source.file(WORLDMAP_FILE))
    assert index[sub_node] == parent


def test_node_parent_index_holds_only_sub_nodes_and_their_links(
    exploration_result: HandlerResult,
) -> None:
    source = exploration_result.source
    index = build_node_parent_index(source.data, source.file(WORLDMAP_FILE))
    by_key = {record["node_key"]: record for record in exploration_result.records}
    for sub_node, parent in index.items():
        assert by_key[sub_node]["is_sub_node"], sub_node
        assert by_key[sub_node]["connection_keys"] == [parent], sub_node


def test_node_parent_index_is_empty_without_a_graph(exploration_result: HandlerResult) -> None:
    assert build_node_parent_index(exploration_result.source.data, b"not a graph") == {}


def test_map_node_index_places_enabled_nodes_on_their_waypoints(exploration_result: HandlerResult) -> None:
    source = exploration_result.source
    index = build_map_node_index(source.data, source.file(WORLDMAP_FILE))
    by_key = {record["node_key"]: record for record in exploration_result.records}

    assert index
    for key, (kind, x, z, is_sub, is_sea) in index.items():
        assert by_key[key]["enabled"], key
        assert by_key[key]["radius"] > 0, key
        assert 0 <= kind < len(NODE_KIND_NAMES), key
        assert (kind, is_sub) == (by_key[key]["node_kind"], by_key[key]["is_sub_node"]), key
        assert isinstance(x, int) and isinstance(z, int), key
        assert is_sea in (0, 1), key


def test_map_node_index_gives_a_sub_node_its_own_position(exploration_result: HandlerResult) -> None:
    source = exploration_result.source
    index = build_map_node_index(source.data, source.file(WORLDMAP_FILE))

    # Elder's Bridge - Lumbering (209) hangs off Elder's Bridge (63) but sits elsewhere.
    assert index[209][1:3] != index[63][1:3]


def test_map_node_index_is_empty_without_a_graph(exploration_result: HandlerResult) -> None:
    assert build_map_node_index(exploration_result.source.data, b"not a graph") == {}


def test_node_name_kr_index_holds_the_korean_names(exploration_result: HandlerResult) -> None:
    index = build_node_name_kr_index(exploration_result.source.data)

    assert index
    assert all(index[record["node_key"]] == record["name_kr"] for record in exploration_result.records if record["name_kr"])


@pytest.mark.parametrize(("node_key", "sea"), [(1409, True), (1439, True), (1, False), (63, False), (209, False)])
def test_map_node_index_marks_the_open_sea(exploration_result: HandlerResult, node_key: int, sea: bool) -> None:
    # 1409 Margoria and 1439 Juur Sea against Velia, Elder's Bridge and its Lumbering sub-node.
    source = exploration_result.source
    index = build_map_node_index(source.data, source.file(WORLDMAP_FILE))
    assert bool(index[node_key][4]) is sea


def test_map_node_index_leaves_out_the_unreachable_second_duvencrune(exploration_result: HandlerResult) -> None:
    # 1651 has no exploration radius and sits far off the map; 1649 is the town.
    source = exploration_result.source
    index = build_map_node_index(source.data, source.file(WORLDMAP_FILE))
    assert 1651 not in index
    assert 1649 in index
