from __future__ import annotations

import struct
from collections.abc import Callable
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    run_case,
)

from _bwp.waypoint.parser import Waypoint
from _common.lookup_index import IndexKind
from _common.teleport import teleport_point_id
from _dbss.teleport.nearest import NamedNode, named_nodes, nearest_node
from _dbss.teleport.parser import parse_teleport_offset_rows, parse_teleport_records


_DATA_FILE = "teleport.dbss"
_OFFSET_FILE = "teleportoffset.dbss"
_WORLDMAP_FILE = "mapdata_realexplore2.bwp"
_RECORD_SIZE = 18
# Buff 47341, "Footprints: Flower-sunken Swamp", teleports to section 0 key 277.
_SWAMP_POINT = (0, 277)
_SWAMP_BUFF = 47341


def _section_starts(data: bytes) -> list[tuple[int, int]]:
    """(start, count) of each `teleport.dbss` section, from the counts it declares."""
    sections: list[tuple[int, int]] = []
    pos = 4
    for _ in range(struct.unpack_from("<I", data, 0)[0]):
        count = struct.unpack_from("<I", data, pos)[0]
        sections.append((pos + 4, count))
        pos += 4 + count * _RECORD_SIZE
    return sections


def _declared_points(companion: str | None = None) -> Callable[[CaseInput], int]:
    """The sum of the section counts `teleport.dbss` declares; `companion` names it when it is not the data file."""

    def read(source: CaseInput) -> int:
        return sum(count for _, count in _section_starts(source.file(companion)))

    return read


POINT_CASE = HandlerCase(
    handler_name=_DATA_FILE,
    data_file=_DATA_FILE,
    companion_files={_WORLDMAP_FILE: _WORLDMAP_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["nearest_node"],
    internal_path=f"gamecommondata/binary/{_DATA_FILE}",
    lookup_indexes={IndexKind.TELEPORT_BUFFS: {teleport_point_id(*_SWAMP_POINT): (_SWAMP_BUFF,)}},
    tests=[
        SchemaTest(
            required_keys=[
                "section",
                "key",
                "x",
                "y",
                "z",
                "destination",
                "nearest_node_key",
                "nearest_node",
                "distance_m",
                "used_by_buff_ids",
                "used_by_icons",
                "used_by",
                "used_by_tooltips",
                "used_by_count",
            ],
        ),
        DeclaredCountTest(declared=_declared_points()),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={_DATA_FILE: _DATA_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["section", "index", "offset", "size"]),
        # One row per point.
        DeclaredCountTest(declared=_declared_points(_DATA_FILE)),
    ],
)


@pytest.fixture(scope="module")
def point_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_POINT_RESULT", None)
    if result is None:
        result = run_case(replace(POINT_CASE, tests=[]))
        request.module._POINT_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", POINT_CASE.tests, ids=case_id)
def test_teleport_dbss(spec: Any, point_result: HandlerResult) -> None:
    point_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_teleportoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_keys_are_unique_within_a_section(point_result: HandlerResult) -> None:
    keys = [(record["section"], record["key"]) for record in point_result.records]
    assert len(keys) == len(set(keys))


def test_buff_destination_lies_at_its_named_place(point_result: HandlerResult) -> None:
    section, key = _SWAMP_POINT
    record = next(r for r in point_result.records if (r["section"], r["key"]) == (section, key))
    assert record["nearest_node"] == "Flower-sunken Swamp"
    # Without the item link, the buff's own English text names it.
    assert record["used_by_buff_ids"] == [_SWAMP_BUFF]
    assert record["used_by"] == ["Footprints: Flower-sunken Swamp"]
    assert record["used_by_tooltips"] == [f"Buff {_SWAMP_BUFF}"]


def test_every_point_has_a_nearest_node(point_result: HandlerResult) -> None:
    for record in point_result.records:
        assert record["nearest_node"], (record["section"], record["key"])
        assert record["distance_m"] >= 0


def test_offset_rows_index_records_by_position(offset_result: HandlerResult) -> None:
    """Each row's offset is its section start plus 18 x index, not a lookup by key."""
    data = offset_result.source.file(_DATA_FILE)
    starts = [start for start, _ in _section_starts(data)]
    for row in offset_result.records:
        assert row["offset"] == starts[row["section"]] + _RECORD_SIZE * row["index"], row
        assert row["size"] == _RECORD_SIZE
        assert data[row["offset"] + 4] == row["section"], row


def _record(key: int, section: int, x: float = 0.0, z: float = 0.0) -> bytes:
    return struct.pack("<IB3fB", key, section, x, 0.0, z, 0)


def _teleport_file(*sections: list[bytes]) -> bytes:
    body = b"".join(struct.pack("<I", len(rows)) + b"".join(rows) for rows in sections)
    return struct.pack("<I", len(sections)) + body


def test_empty_sections_keep_their_place() -> None:
    data = _teleport_file([_record(7, 0)], [], [_record(3, 2)])
    assert [(r["section"], r["key"]) for r in parse_teleport_records(data)] == [(0, 7), (2, 3)]


def test_record_in_the_wrong_section_is_rejected() -> None:
    with pytest.raises(ValueError, match="names section"):
        parse_teleport_records(_teleport_file([_record(7, 1)]))


def test_truncated_file_is_rejected() -> None:
    data = _teleport_file([_record(7, 0), _record(8, 0)])
    with pytest.raises(ValueError):
        parse_teleport_records(data[:-1])


def test_offset_file_sections_run_to_the_end() -> None:
    data = struct.pack("<I3I", 1, 0, 8, 18) + struct.pack("<I", 0) + struct.pack("<I3I", 1, 0, 30, 18)
    rows = parse_teleport_offset_rows(data)
    assert [(r["section"], r["index"], r["offset"]) for r in rows] == [(0, 0, 8), (2, 0, 30)]


def _waypoint(key: int, name: str, x: float, z: float) -> Waypoint:
    return Waypoint(key, name, x, 0.0, z, 0, False, False)


def test_nearest_node_measures_metres_on_the_ground_plane() -> None:
    nodes = [NamedNode(1, "Velia", 0.0, 0.0), NamedNode(2, "Heidel", 30_000.0, 40_000.0)]
    nearest = nearest_node(20_000.0, 40_000.0, nodes)
    assert nearest is not None
    assert (nearest.name, nearest.distance_m) == ("Heidel", 100.0)


def test_nearest_node_is_none_without_nodes() -> None:
    assert nearest_node(0.0, 0.0, []) is None


def test_nodes_without_an_english_name_are_skipped() -> None:
    waypoints = [_waypoint(1, "town(velia)", 0.0, 0.0), _waypoint(2, "hidden(cave)", 1.0, 1.0)]
    nodes = named_nodes(waypoints, lambda key: "Velia" if key == 1 else "")
    assert [node.name for node in nodes] == ["Velia"]


def test_without_loc_nodes_keep_their_worldmap_names() -> None:
    nodes = named_nodes([_waypoint(1, "town(velia)", 0.0, 0.0)], lambda key: "")
    assert [node.name for node in nodes] == ["town(velia)"]


def test_point_id_keeps_section_and_key_apart() -> None:
    from _common.teleport import teleport_point_id

    assert teleport_point_id(0, 340) != teleport_point_id(5, 340)
    with pytest.raises(ValueError):
        teleport_point_id(0, 1 << 16)


def test_used_by_names_a_buff_by_item_then_text_then_korean(monkeypatch: pytest.MonkeyPatch) -> None:
    import _dbss.teleport.used_by as used_by
    from _common.lookup_index import IndexKind, clear_indexes, init_index

    monkeypatch.setattr(used_by, "item_key_text_tagged", lambda item_id: f"<PAColor0xFFF5BA3A>item {item_id}<PAOldColor>")
    monkeypatch.setattr(used_by, "item_key_icon_path", lambda item_id: "item.dds")
    monkeypatch.setattr(used_by, "buff_first_line", lambda buff_id: "Move to Velia" if buff_id == 2 else "")
    clear_indexes()
    try:
        init_index(IndexKind.BUFF_ITEMS, {1: (761880,)})
        init_index(IndexKind.TELEPORT_BUFF_NAME_KR, {3: "벨리아 귀환석"})
        entries = used_by.used_by_entries([1, 2, 3, 4])
        labels = [entry.label for entry in entries]
    finally:
        clear_indexes()
    assert labels == ["item 761880", "Move to Velia", "벨리아 귀환석", "4"]
    # The item name keeps its grade colour for the cell.
    assert entries[0].tagged_label == "<PAColor0xFFF5BA3A>item 761880<PAOldColor>"


def test_used_by_reads_buffs_of_one_item_once(monkeypatch: pytest.MonkeyPatch) -> None:
    import _dbss.teleport.used_by as used_by

    monkeypatch.setattr(used_by, "used_by_entry", lambda buff_id: ("", "Footprints"))
    entries = used_by.used_by_entries([1, 2])
    assert [(entry.label, entry.buff_ids, entry.tooltip) for entry in entries] == [
        ("Footprints", (1, 2), "Buffs 1, 2")
    ]


def test_used_by_cell_shows_buff_ids_on_hover() -> None:
    from _dbss.teleport.used_by import used_by_cell

    cell = used_by_cell(["icon.dds", ""], ["Footprints", "Move to Velia"], ["Buff 1", "Buff 2"], 3)
    assert 'title="Buff 1"' in cell and 'title="Buff 2"' in cell


def test_nearest_node_index_places_a_point_like_the_table(point_result: HandlerResult) -> None:
    from _dbss.teleport.parser import build_teleport_nearest_node_index

    source = point_result.source
    index = build_teleport_nearest_node_index(source.data, source.file(_WORLDMAP_FILE))
    record = next(r for r in point_result.records if (r["section"], r["key"]) == _SWAMP_POINT)
    node_key, metres = index[teleport_point_id(*_SWAMP_POINT)]
    assert node_key == record["nearest_node_key"]
    assert metres == record["distance_m"]
    assert build_teleport_nearest_node_index(source.data, b"not a graph") == {}


def test_point_place_reads_name_and_distance(monkeypatch: pytest.MonkeyPatch) -> None:
    import _common.teleport as teleport
    from _common.lookup_index import clear_indexes, init_index

    monkeypatch.setattr(teleport, "full_node_name", lambda key: "Altinova Gateway" if key == 1101 else "")
    clear_indexes()
    try:
        init_index(IndexKind.TELEPORT_NEAREST_NODE, {
            teleport_point_id(0, 340): (1101, 1221),
            teleport_point_id(0, 341): (4242, 5),
        })
        assert teleport.teleport_point_place(0, 340) == "Altinova Gateway (1,221 m)"
        # A node without a name, or a point without an entry, places nothing.
        assert teleport.teleport_point_place(0, 341) == ""
        assert teleport.teleport_point_place(5, 340) == ""
    finally:
        clear_indexes()
