from __future__ import annotations

import struct
from dataclasses import replace
from pathlib import Path
from typing import Any

import pytest

from bdo_preview import GRID_CELL_KEY, get_handler, is_handled_file
from tests.case_input import CaseInput
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _bss.fieldinfo.names import FIELDINFO_PATH
from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from _common.pabr_offset import PABR_MAGIC
from _common.pabr_strings import TRAILER_SIZE
from .handler import FieldGridInfoHandler, FileInfoHandler, SpawnGridCellHandler
from .parser import (
    CELL_FILE_KEY,
    FIELDGRIDINFO_FILE,
    FILEINFO_FILE,
    grid_field_no,
    parse_cell_spawns,
    parse_grid_pairs,
)

_FOLDER = "mapdata_real/spawnplacementfieldgrid/1/7"
_FIELDINFO_FILE = FIELDINFO_PATH.rsplit("/", 1)[-1]
# Two Heidel NPCs in sector (2, 19), the same since client 1784.
_SMALL_CELL = "553_364.bss"
_VILLAGER_KEY = 844433521311746
# A cell whose spawns include spawn hours (`conditions`) on client 3482.
_CONDITION_CELL = "574_266.bss"
# A cell file holds 7 x 7 grid squares from the square its name gives.
_CELL_SQUARES = 7

_SPAWN_KEYS = [
    "grid_x", "grid_z", "is_spawnable", "key_index", "key_sector_z", "key_sector_x", "key_type",
    "position_x", "position_y", "position_z", "direction", "has_character", "character_key",
    "spawn_delay_time", "action_index", "dialog_index", "territory", "team_no",
    "house_x", "waypoint_count", "waypoints", "go_home_type", "index_position_count",
    "index_positions", "condition_count", "conditions",
    "spawn_key", "type_label", "character_name", "has_character_row", "go_home_waypoint",
]


def _cell_case(file_name: str, tests: list) -> HandlerCase:
    return HandlerCase(
        handler_name=CELL_FILE_KEY,
        data_file=file_name,
        companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=["character_name"],
        internal_path=f"{_FOLDER}/{file_name}",
        tests=tests,
    )


def _pair_count(source: CaseInput) -> int:
    """The 4-byte pairs between the magic and the string table offset the trailer stores."""
    data = source.data
    (table_start,) = struct.unpack_from("<I", data, len(data) - TRAILER_SIZE)
    return (table_start - len(PABR_MAGIC)) // 4


CELL_CASE = _cell_case(
    _SMALL_CELL,
    [
        SchemaTest(required_keys=_SPAWN_KEYS),
        RangeTest(col="is_spawnable", min_val=0, max_val=1),
        RangeTest(col="has_character", min_val=0, max_val=1),
        TargetTest(
            col="spawn_key",
            value=_VILLAGER_KEY,
            expected={"key_index": 2, "key_sector_x": 2, "key_sector_z": 19, "key_type": 3, "character_key": 624},
        ),
    ],
)
CONDITION_CELL_CASE = _cell_case(_CONDITION_CELL, [SchemaTest(required_keys=_SPAWN_KEYS)])

FIELDGRID_CASE = HandlerCase(
    handler_name=FIELDGRIDINFO_FILE,
    data_file=FIELDGRIDINFO_FILE,
    companion_files={_FIELDINFO_FILE: _FIELDINFO_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"{_FOLDER}/{FIELDGRIDINFO_FILE}",
    tests=[
        SchemaTest(required_keys=["grid_x", "grid_z", "field_no", "world_x", "world_z"]),
        DeclaredCountTest(declared=_pair_count),
    ],
)

FILEINFO_CASE = HandlerCase(
    handler_name=FILEINFO_FILE,
    data_file=FILEINFO_FILE,
    companion_files={_FIELDINFO_FILE: _FIELDINFO_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"{_FOLDER}/{FILEINFO_FILE}",
    tests=[
        SchemaTest(required_keys=["cell_x", "cell_z", "field_no", "world_x", "world_z"]),
        DeclaredCountTest(declared=_pair_count),
    ],
)

_CASES = {
    "cell": CELL_CASE,
    "condition_cell": CONDITION_CELL_CASE,
    "fieldgrid": FIELDGRID_CASE,
    "fileinfo": FILEINFO_CASE,
}


@pytest.fixture(scope="module")
def results(request: Any) -> dict[str, HandlerResult]:
    cached = getattr(request.module, "_HANDLER_RESULTS", None)
    if cached is None:
        cached = {name: run_case(replace(case, tests=[])) for name, case in _CASES.items()}
        request.module._HANDLER_RESULTS = cached
    return cached


@pytest.mark.parametrize("spec", CELL_CASE.tests, ids=case_id)
def test_cell_bss(spec: Any, results: dict[str, HandlerResult]) -> None:
    results["cell"].check(spec)


@pytest.mark.parametrize("spec", CONDITION_CELL_CASE.tests, ids=case_id)
def test_condition_cell_bss(spec: Any, results: dict[str, HandlerResult]) -> None:
    results["condition_cell"].check(spec)


@pytest.mark.parametrize("spec", FIELDGRID_CASE.tests, ids=case_id)
def test_fieldgridinfo_bss(spec: Any, results: dict[str, HandlerResult]) -> None:
    results["fieldgrid"].check(spec)


@pytest.mark.parametrize("spec", FILEINFO_CASE.tests, ids=case_id)
def test_fileinfo_bss(spec: Any, results: dict[str, HandlerResult]) -> None:
    results["fileinfo"].check(spec)


@pytest.mark.parametrize("name", ["cell", "condition_cell"])
def test_spawns_lie_in_the_squares_of_their_cell(name: str, results: dict[str, HandlerResult]) -> None:
    cell_x, cell_z = (int(v) for v in Path(_CASES[name].data_file).stem.split("_"))
    for r in results[name].records:
        assert cell_x <= r["grid_x"] < cell_x + _CELL_SQUARES
        assert cell_z <= r["grid_z"] < cell_z + _CELL_SQUARES


@pytest.mark.parametrize("name", ["cell", "condition_cell"])
def test_every_list_holds_its_count(name: str, results: dict[str, HandlerResult]) -> None:
    for r in results[name].records:
        assert len(r["waypoints"]) == r["waypoint_count"]
        assert len(r["index_positions"]) == r["index_position_count"]
        assert len(r["conditions"]) == r["condition_count"]
        assert (r["character_key"] is None) == (r["has_character"] == 0)


def test_the_world_list_names_its_field_and_world_corners(results: dict[str, HandlerResult]) -> None:
    # The fixture fetch takes the first `fieldgridinfo.bss` / `fileinfo.bss` of the
    # `.meta`, the open world's; an instance field's list would be empty.
    for name in ("fieldgrid", "fileinfo"):
        records = results[name].records
        assert records, f"the {name} fixture lists nothing; it is not the field 1 file"
        assert all(r["field_no"] == 1 and r["world_x"] is not None for r in records)


def test_fileinfo_cells_start_on_a_multiple_of_seven(results: dict[str, HandlerResult]) -> None:
    assert all(r["cell_x"] % _CELL_SQUARES == 0 and r["cell_z"] % _CELL_SQUARES == 0 for r in results["fileinfo"].records)


def test_grid_cell_names_read_under_one_key() -> None:
    assert CELL_FILE_KEY == GRID_CELL_KEY
    assert isinstance(get_handler(_SMALL_CELL, ".bss"), SpawnGridCellHandler)
    assert isinstance(get_handler(FIELDGRIDINFO_FILE, ".bss"), FieldGridInfoHandler)
    assert isinstance(get_handler(FILEINFO_FILE, ".bss"), FileInfoHandler)
    assert is_handled_file("147_567.bss")
    assert not isinstance(get_handler("147_567a.bss", ".bss"), SpawnGridCellHandler)


def test_the_field_number_comes_from_the_folder() -> None:
    assert grid_field_no("mapdata_instancedungeon/4001/spawnplacementfieldgrid/4001/7/fileinfo.bss") == 4001
    assert grid_field_no(f"{_FOLDER}/{_SMALL_CELL}") == 1
    assert grid_field_no("gamecommondata/binary/fileinfo.bss") is None


def _trailer(body: bytes) -> bytes:
    """PABR, the body, an empty string table and the trailer pointing at it."""
    table_start = len(PABR_MAGIC) + len(body)
    return PABR_MAGIC + body + struct.pack("<III", 0, table_start, 0)


def _spawn(*, character_key: int | None, waypoint_keys: tuple[int, ...], hours: tuple[int, int] | None) -> bytes:
    head = struct.pack("<BHhhBBfffHfH", 1, 7, 19, 2, 3, 0, 100.0, -5.0, 200.0, 0, 1.5, 0)
    head += struct.pack("<BH", 1, character_key) if character_key is not None else struct.pack("<B", 0)
    body = struct.pack("<iiiHH", 0, 0, 0, 0, 0) + struct.pack("<III", 1, 0, 0) + b"\x00"
    body += struct.pack("<II", 120000, 30000) + b"\x01" + bytes(3) + struct.pack("<I", 0) + b"\x00"
    body += struct.pack("<III", 0, 0, 0) + struct.pack("<hIHI", -1, 17, 5, 0) + bytes(4)
    body += struct.pack("<iifff", 0, 0, 0.0, 0.0, 0.0) + struct.pack("<I", len(waypoint_keys))
    body += b"".join(struct.pack("<Bi", slot, key) for slot, key in enumerate(waypoint_keys, 1))
    tail = struct.pack("<BBI", 2, 0, 0)
    tail += struct.pack("<B", 1) + struct.pack("<Bhh", 0, *hours) if hours else struct.pack("<B", 0)
    return head + body + tail


def test_a_cell_reads_spawns_with_and_without_a_character() -> None:
    spawns = _spawn(character_key=624, waypoint_keys=(253, -253, 0, 0, 0), hours=(2, 22))
    spawns += _spawn(character_key=None, waypoint_keys=(), hours=None)
    data = _trailer(struct.pack("<HHI", 559, 369, 2) + spawns)

    first, second = parse_cell_spawns(data, _SMALL_CELL)

    assert (first["character_key"], first["action_index"], first["dialog_index"]) == (624, 17, 5)
    assert [w["waypoint_key"] for w in first["waypoints"]][:2] == [253, -253]
    assert first["conditions"] == [{"unknown_00": 0, "spawn_start_hour": 2, "spawn_end_hour": 22}]
    assert (second["character_key"], second["waypoints"], second["go_home_type"]) == (None, [], 2)
    assert (second["grid_x"], second["grid_z"]) == (559, 369)


def test_an_empty_list_reads_as_no_pairs() -> None:
    assert parse_grid_pairs(_trailer(b""), FILEINFO_FILE) == []


@pytest.mark.parametrize(
    "data",
    [
        b"XXXX" + _trailer(struct.pack("<HH", 126, 630))[4:],
        _trailer(struct.pack("<HHB", 126, 630, 0)),
    ],
    ids=["bad_magic", "partial_pair"],
)
def test_a_changed_list_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_grid_pairs(data, FILEINFO_FILE)


def test_a_spawn_past_the_string_table_raises() -> None:
    spawn = _spawn(character_key=624, waypoint_keys=(), hours=None)
    with pytest.raises(ValueError):
        parse_cell_spawns(_trailer(struct.pack("<HHI", 559, 369, 2) + spawn), _SMALL_CELL)
