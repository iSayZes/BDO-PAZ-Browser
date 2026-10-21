from __future__ import annotations

from dataclasses import replace
from functools import cache
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
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

from _bss.fieldinfo.names import field_label
from _bss.fieldinfo.parser import ROW_SIZE, build_field_name_index, parse_fieldinfo_records
from _bss.instancefieldmapinfo.parser import build_instance_field_title_index
from _common.lookup_index import IndexKind, clear_indexes, init_index

_FILE = "fieldinfo.bss"
# World units per sector, the unit of `teleport.dbss` and the instancefield.dbss boxes.
_SECTOR_UNITS = 12800
# The server box counts three of its sectors per field sector.
_SERVER_SECTORS_PER_SECTOR = 3
_AXES = ("x", "y", "z")
_MAGNUS_FIELD_NO = 4001
_MAGNUS_NAME = "A1_001"
_MAGNUS_LABEL = "The Magnus: The Great Single Path (A1_001)"


@cache
def _instance_field_titles() -> dict[int, int]:
    """INSTANCE_FIELD_TITLE built from the installed tables, the way the app builds it."""
    return build_instance_field_title_index(
        load_binary_fixture("instancefieldmapinfo.bss"), load_binary_fixture("stringtable.bss")
    )


CASE = HandlerCase(
    handler_name=_FILE,
    data_file=_FILE,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["label"],
    internal_path=f"gamecommondata/binary/{_FILE}",
    lookup_indexes={
        IndexKind.INSTANCE_FIELD_NAME: {_MAGNUS_FIELD_NO: _MAGNUS_NAME},
        IndexKind.INSTANCE_FIELD_TITLE: _instance_field_titles,
    },
    tests=[
        SchemaTest(required_keys=[
            "field_no", "field_name", "resource_name", "display_name", "label",
            "spawn_x", "spawn_y", "spawn_z",
            "sector_start_x", "sector_start_y", "sector_start_z",
            "sector_end_x", "sector_end_y", "sector_end_z",
            "world_start_x", "world_end_x", "obstacle_precision",
            "server_sector_start_x", "server_sector_end_x",
            "field_type", "field_type_name", "region_map_index", "audio_map_index",
            "is_save_complete", "field_level", "is_ridable", "enter_enable_user_count",
            "use_range_spawn", "use_return_position", "item_drop_rate",
            "bank_no_music", "bank_no_environment", "great_sea_map_index",
            "horse_race_course_map_index",
        ]),
        DeclaredCountTest(declared=header_count(offset=4)),
        # Field 1 is the open world the instancefield.dbss fields copy.
        TargetTest(col="field_no", value=1, expected={
            "field_name": "월드", "resource_name": "_real", "field_type_name": "OpenField",
        }),
        # instancedungeoninfo.dbss key 2 enters the Calpheon Kzarka instance dungeon.
        TargetTest(col="field_no", value=700, expected={"field_name": "칼페온 크자카 인던"}),
        # An A1_ field reads its instancefieldmapinfo.bss title.
        TargetTest(col="field_no", value=_MAGNUS_FIELD_NO, expected={
            "field_name": _MAGNUS_NAME,
            "resource_name": f"_instancedungeon/{_MAGNUS_FIELD_NO}",
            "label": _MAGNUS_LABEL,
        }),
    ],
)


@pytest.fixture(scope="module")
def fieldinfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fieldinfo_bss(spec: Any, fieldinfo_result: HandlerResult) -> None:
    fieldinfo_result.check(spec)


def test_field_numbers_are_unique(fieldinfo_result: HandlerResult) -> None:
    numbers = [r["field_no"] for r in fieldinfo_result.records]
    assert len(numbers) == len(set(numbers))


def test_boxes_agree_in_all_three_units(fieldinfo_result: HandlerResult) -> None:
    """The world box spans whole sectors and the server box is the sector box times three."""
    for r in fieldinfo_result.records:
        for axis in _AXES:
            start, end = r[f"sector_start_{axis}"], r[f"sector_end_{axis}"]
            assert start <= end, r["field_no"]
            assert r[f"world_start_{axis}"] == start * _SECTOR_UNITS, r["field_no"]
            assert r[f"world_end_{axis}"] == (end + 1) * _SECTOR_UNITS, r["field_no"]
            assert r[f"server_sector_start_{axis}"] == start * _SERVER_SECTORS_PER_SECTOR, r["field_no"]
            assert r[f"server_sector_end_{axis}"] == end * _SERVER_SECTORS_PER_SECTOR, r["field_no"]


def test_name_index_holds_every_field(fieldinfo_result: HandlerResult) -> None:
    index = build_field_name_index(fieldinfo_result.source.file(None))
    assert index == {r["field_no"]: r["field_name"] for r in fieldinfo_result.records}


def test_label_needs_the_instance_field_with_the_same_name() -> None:
    init_index(IndexKind.INSTANCE_FIELD_NAME, {_MAGNUS_FIELD_NO: _MAGNUS_NAME, 1: "Shadow_Ser_Main"})
    try:
        # Instance field 1 is another map than field 1, the world.
        assert field_label(1, "월드") == "월드"
        # Without the title index the instance field's name stands alone.
        assert field_label(_MAGNUS_FIELD_NO, _MAGNUS_NAME) == _MAGNUS_NAME
    finally:
        clear_indexes()


def test_rows_that_miss_the_string_table_are_rejected() -> None:
    # PABR, 1 row declared, but the trailer puts the string table right after the header.
    data = b"PABR" + (1).to_bytes(4, "little") + bytes(ROW_SIZE) + (0).to_bytes(4, "little")
    data += (8).to_bytes(4, "little") + bytes(4)
    with pytest.raises(ValueError, match="string table starts"):
        parse_fieldinfo_records(data)
