from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

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

from _bss.regionmapinfo.parser import ROW_SIZE, map_images, parse_regionmapinfo_records

_FILE = "regionmapinfo.bss"
_REGION_MAP_INDEX = 1
_SIEGE_MAP_INDEX = 4

CASE = HandlerCase(
    handler_name=_FILE,
    data_file=_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_FILE}",
    tests=[
        SchemaTest(required_keys=[
            "map_index", "map_type", "map_type_name", "map_index_dup",
            "sector_start_x", "sector_end_y", "sector_end_x", "sector_start_y", "image_path",
        ]),
        DeclaredCountTest(declared=header_count(offset=4)),
        # fieldinfo.bss region_map_index: the world's region bitmap.
        TargetTest(col="map_index", value=_REGION_MAP_INDEX, expected={
            "image_path": "RegionMap_New.bmp", "map_type_name": "Region",
        }),
        # fieldinfo.bss siege_info_map_index.
        TargetTest(col="map_index", value=_SIEGE_MAP_INDEX, expected={
            "image_path": "Siegemap.bmp", "map_type_name": "Siege",
        }),
    ],
)


@pytest.fixture(scope="module")
def regionmapinfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_regionmapinfo_bss(spec: Any, regionmapinfo_result: HandlerResult) -> None:
    regionmapinfo_result.check(spec)


def test_map_indexes_are_unique(regionmapinfo_result: HandlerResult) -> None:
    keys = [r["map_index"] for r in regionmapinfo_result.records]
    assert len(keys) == len(set(keys))


def test_every_map_names_an_image_and_a_rectangle(regionmapinfo_result: HandlerResult) -> None:
    for r in regionmapinfo_result.records:
        assert r["image_path"].lower().endswith(".bmp"), r["map_index"]
        assert r["sector_start_x"] < r["sector_end_x"], r["map_index"]
        assert r["sector_start_y"] < r["sector_end_y"], r["map_index"]


def test_image_index_holds_every_map(regionmapinfo_result: HandlerResult) -> None:
    images = map_images(regionmapinfo_result.source.file(None))
    assert images == {r["map_index"]: r["image_path"] for r in regionmapinfo_result.records}


def _one_row_file(map_index: int, map_index_dup: int) -> bytes:
    """PABR with one row and a one-string table, as the client writes it."""
    row = struct.pack("<HBHiiiiI", map_index, 0, map_index_dup, -160, 160, 112, -88, 0)
    name = "A.bmp".encode("utf-16-le")
    table_start = 8 + ROW_SIZE
    strings = struct.pack("<IBI", 1, 1, len(name)) + name
    return b"PABR" + struct.pack("<I", 1) + row + strings + struct.pack("<II", table_start, 0)


def test_a_row_whose_key_copy_differs_is_rejected() -> None:
    assert parse_regionmapinfo_records(_one_row_file(1, 1))[0]["image_path"] == "A.bmp"
    with pytest.raises(ValueError, match="repeats key"):
        parse_regionmapinfo_records(_one_row_file(1, 2))
