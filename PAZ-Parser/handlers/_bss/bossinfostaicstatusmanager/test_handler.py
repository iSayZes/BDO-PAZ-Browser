from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _common.texture_string import TEXTURE_STRING_COMBINE, TextureRegion, parse_texture_regions
from .parser import FILE_NAME, parse_bossinfo_records


_STRINGTABLE_FILE = "stringtable.bss"
_DASTARD_BHEG = 23069
_KZARKA = 23001
_NIGHTMARISH_KZARKA = 23172
_FIELD = 1
# 0 World to 4 Event, the LUA_WORLDMAP_BOSSLIST_TOOLTIP_<n> keys.
_LAST_TAB = 4
_WORLD = 0
_BOSS_LIST_SHEET = "ui_texture/combine/etc/combine_etc_worldmap_bosslist.dds"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={
        _STRINGTABLE_FILE: _STRINGTABLE_FILE,
        TEXTURE_STRING_COMBINE: TEXTURE_STRING_COMBINE,
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "tab"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "character_id", "boss_info_type", "reward_items", "main_texture", "list_texture",
            "reinforced_character_id", "reinforced_reward_items", "x", "y", "z",
            "spawn_times", "is_event_boss", "unknown_ids", "unknown_flag",
            "name", "tab", "reinforced_name", "reward_names", "spawn_count",
            "position", "icon_path", "icon_region",
        ]),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="boss_info_type", min_val=0, max_val=_LAST_TAB),
        UserLanguageTest(fields=["name", "tab", "reinforced_name", "reward_names"]),
        TargetTest(col="character_id", value=_DASTARD_BHEG, expected={
            "name": "Dastard Bheg",
            "boss_info_type": _FIELD,
            "tab": "Field",
            "main_texture": "Combine_Etc_WorldMap_BossList_Img_Begg",
            "list_texture": "Combine_Etc_WorldMap_BossList_Begg",
            "icon_path": _BOSS_LIST_SHEET,
        }),
        TargetTest(col="character_id", value=_KZARKA, expected={
            "boss_info_type": _WORLD,
            "reinforced_character_id": _NIGHTMARISH_KZARKA,
            "reinforced_name": "Nightmarish Kzarka",
        }),
    ],
)


@pytest.fixture(scope="module")
def boss_info_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_bossinfostaicstatusmanager_bss(spec: Any, boss_info_result: HandlerResult) -> None:
    boss_info_result.check(spec)


def test_every_list_icon_resolves(boss_info_result: HandlerResult) -> None:
    for r in boss_info_result.records:
        assert r["icon_path"] and r["icon_region"]


def test_unknown_ids_pair_with_spawn_times(boss_info_result: HandlerResult) -> None:
    for r in boss_info_result.records:
        times = [(g["group"], len(g["values"])) for g in r["spawn_times"]]
        ids = [(g["group"], len(g["values"])) for g in r["unknown_ids"]]
        assert times == ids


def test_a_short_record_raises() -> None:
    # One record that holds only empty group lists, then an empty string table.
    record = struct.pack("<II", 0, 0)
    table_start = 8 + len(record)
    data = b"PABR" + struct.pack("<I", 1) + record + struct.pack("<I", 0) + struct.pack("<II", table_start, 0)
    with pytest.raises(ValueError):
        parse_bossinfo_records(data)


def test_texture_regions_read_back() -> None:
    xml = (
        b'<Table>\r\n\t\t<Texture ID="A" Size="160 75" UV="162 382 322 457" '
        b'Path="Combine/Etc/Sheet.dds"/>\r\n'
        b'\t\t<Texture ID="B" Size="1 1" UV="0 0 1" Path="Combine/Etc/Sheet.dds"/>\r\n</Table>'
    )
    assert parse_texture_regions(xml, ["A", "B", "C"]) == {
        "A": TextureRegion("ui_texture/combine/etc/sheet.dds", (162, 382, 322, 457)),
    }
    assert parse_texture_regions(None, ["A"]) == {}
