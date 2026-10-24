from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from _common.texture_string import TEXTURE_STRING_COMBINE
from .parser import (
    FILE_NAME,
    GROUP_COUNT,
    ITEM_LIST_COUNT,
    MODE_COUNT,
    PRESET_COUNT,
    parse_solareoption_file,
)


_STRINGTABLE_FILE = "stringtable.bss"
_GROUP_SHIFT = 8
_TIER_MASK = 0xFF
# __eClassType_Count: the class type of the shared preset (solareoptionstaticstatusmanager_bss.md).
_SHARED_PRESET_CLASS = 47
# Group 1, tier 1 of game mode 0.
_GROUP_1_TIER_1 = 0x0101

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={
        _STRINGTABLE_FILE: _STRINGTABLE_FILE,
        TEXTURE_STRING_COMBINE: TEXTURE_STRING_COMBINE,
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "game_mode", "rank_group", "min_rating", "max_ranking", "rank_tier_key",
            "description", "icon_texture", "match_slot_right_frame", "match_slot_left_frame",
            "hp_widget_right_frame", "hp_widget_left_frame", "item_lists",
            "tier", "name", "item_list_texts", "icon_path", "icon_region",
        ]),
        UserLanguageTest(fields=["name"]),
        TargetTest(col="rank_tier_key", value=_GROUP_1_TIER_1, expected={
            "game_mode": 0,
            "rank_group": 1,
            "tier": 1,
            "description_key": "LUA_SOLARE_RANK_TIER_01",
            "icon_texture_key": "Solare_Tier01",
        }),
    ],
)


@pytest.fixture(scope="module")
def solare_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def solare_file() -> Any:
    return parse_solareoption_file(load_binary_fixture(FILE_NAME))


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_solareoptionstaticstatusmanager_bss(spec: Any, solare_result: HandlerResult) -> None:
    solare_result.check(spec)


def test_tier_key_holds_its_rank_group(solare_result: HandlerResult) -> None:
    for record in solare_result.records:
        assert record["rank_tier_key"] >> _GROUP_SHIFT == record["rank_group"], record
        assert record["rank_tier_key"] & _TIER_MASK == record["tier"] >= 1, record
        assert len(record["item_lists"]) == ITEM_LIST_COUNT


def test_every_string_index_names_a_string(solare_result: HandlerResult) -> None:
    for record in solare_result.records:
        assert record["description_key"].startswith("LUA_SOLARE_RANK_TIER_"), record
        assert record["icon_texture_key"].startswith("Solare_Tier"), record
        assert "_Right_" in record["match_slot_right_frame_key"]
        assert "_Left_" in record["match_slot_left_frame_key"]
        assert "_Right_" in record["hp_widget_right_frame_key"]
        assert "_Left_" in record["hp_widget_left_frame_key"]


def test_fixed_arrays(solare_file: Any) -> None:
    assert len(solare_file.modes) == MODE_COUNT
    assert all(len(mode["groups"]) == GROUP_COUNT for mode in solare_file.modes)
    groups = [group["rank_group"] for group in solare_file.modes[0]["groups"]]
    assert groups == list(range(GROUP_COUNT))
    assert len(solare_file.equip_presets) == PRESET_COUNT


def test_shared_preset_is_last_and_holds_the_jewels(solare_file: Any) -> None:
    *class_presets, shared = solare_file.equip_presets
    assert shared["class_type"] == _SHARED_PRESET_CLASS
    assert shared["jewel_items"]
    assert not any(preset["jewel_items"] for preset in class_presets)
    for preset in class_presets:
        if preset["equip_items"]:
            assert preset["class_type"] < _SHARED_PRESET_CLASS


def test_result_strings_follow_the_modes(solare_file: Any) -> None:
    common = solare_file.common
    texts = [common[f"unknown_{name}_str_ref_text"] for name in ("win", "draw", "lose")]
    assert texts == ["SOLARE_WIN", "SOLARE_DRAW", "SOLARE_LOSE"]


def test_bad_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_solareoption_file(b"XXXX" + bytes(16))
