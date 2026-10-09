from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

import _bss.instancefieldmapinfo.titles as titles
from _bss.instancefieldmapinfo.parser import build_instance_field_title_index
from _bss.stringtable.parser import GAME_SHEET, parse_sheet_key_hashes
from _common.lookup_index import IndexKind

_FILE = "instancefieldmapinfo.bss"
_STRINGTABLE_FILE = "stringtable.bss"

CASE = HandlerCase(
    handler_name=_FILE,
    data_file=_FILE,
    companion_files={_STRINGTABLE_FILE: _STRINGTABLE_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["title", "description"],
    internal_path=f"gamecommondata/binary/{_FILE}",
    lookup_indexes={IndexKind.INSTANCE_FIELD_NAME: {4001: "A1_001", 150: "Atoraxion_Desert"}},
    tests=[
        SchemaTest(required_keys=[
            "key", "title_key", "description_key", "title", "description",
            "x", "y", "z", "radius", "image_path", "image_region",
            "entry_item_id", "entry_item", "spawns", "spawn_count", "field_name",
        ]),
        DeclaredCountTest(declared=header_count(offset=4)),
        UserLanguageTest(fields=["title", "description"]),
        # The Magnus fields name themselves by GAME sheet keys after the field.
        TargetTest(col="key", value=4001, expected={
            "field_name": "A1_001",
            "title_key": "INSTANCEDUNGEONDATA_A1_001_NAME",
            "description_key": "INSTANCEDUNGEONDATA_A1_001_DESC",
        }),
        # Atoraxion's desert map takes its "Access Granted" item to enter.
        TargetTest(col="key", value=150, expected={"field_name": "Atoraxion_Desert", "entry_item_id": 65992}),
        TargetTest(col="key", value=101, expected={
            "title_key": "LUA_HORSERACING_MAP_STAGENAME00",
            "image_path": "ui_texture/combine/etc/combine_etc_horseracing.dds",
        }),
    ],
)


@pytest.fixture(scope="module")
def map_info_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_MAP_INFO_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._MAP_INFO_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_instancefieldmapinfo_bss(spec: Any, map_info_result: HandlerResult) -> None:
    map_info_result.check(spec)


def test_keys_are_unique(map_info_result: HandlerResult) -> None:
    keys = [r["key"] for r in map_info_result.records]
    assert len(keys) == len(set(keys))


def test_image_region_sits_with_an_image(map_info_result: HandlerResult) -> None:
    for r in map_info_result.records:
        assert any(r["image_region"]) == bool(r["image_path"]), r["key"]


def test_spawn_tail_follows_the_spawns(map_info_result: HandlerResult) -> None:
    for r in map_info_result.records:
        has_tail = r["unknown_spawn_f32"] is not None
        assert has_tail == bool(r["spawns"]), r["key"]


def test_title_index_holds_each_title_key_hash(map_info_result: HandlerResult) -> None:
    source = map_info_result.source
    stringtable = source.file(_STRINGTABLE_FILE)
    hashes = parse_sheet_key_hashes(stringtable, [GAME_SHEET])[GAME_SHEET]
    index = build_instance_field_title_index(source.file(None), stringtable)
    expected = {
        r["key"]: hashes[r["title_key"]] for r in map_info_result.records if r["title_key"] in hashes
    }
    assert index == expected
    assert index


@pytest.mark.parametrize(
    ("title", "name", "expected"),
    [
        ("The Magnus: The Great Single Path", "A1_001", "The Magnus: The Great Single Path (A1_001)"),
        ("", "A1_001", "A1_001"),
        ("Scarlet Thread", "", "Scarlet Thread"),
        ("", "", ""),
    ],
)
def test_instance_field_label(monkeypatch: pytest.MonkeyPatch, title: str, name: str, expected: str) -> None:
    monkeypatch.setattr(titles, "instance_field_title", lambda key: title)
    monkeypatch.setattr(titles, "instance_field_name", lambda key: name)
    assert titles.instance_field_label(4001) == expected
