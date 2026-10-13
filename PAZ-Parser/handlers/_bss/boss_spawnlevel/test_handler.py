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

from .parser import FILE_NAME, boss_characters

_FERRID_KEY = 1
_FERRID = 28856
_FERRID_SMALL_REWARD = 756210

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["boss_name", "reward_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "boss_key", "level", "character_id", "reward_item_id", "image_path",
            "boss_name", "reward_name", "unknown_05", "unknown_07", "unknown_11",
        ]),
        UserLanguageTest(fields=["boss_name", "reward_name"]),
        TargetTest(col="reward_item_id", value=_FERRID_SMALL_REWARD, expected={
            "boss_key": _FERRID_KEY,
            "character_id": _FERRID,
            "boss_name": "Ferrid",
            "image_path": "ui_texture/icon/quest/guildboss_renewal_ferrid.dds",
        }),
    ],
)


@pytest.fixture(scope="module")
def spawn_level_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_boss_spawnlevel_bss(spec: Any, spawn_level_result: HandlerResult) -> None:
    spawn_level_result.check(spec)


def test_levels_count_up_from_zero_per_boss(spawn_level_result: HandlerResult) -> None:
    levels: dict[int, list[int]] = {}
    for r in spawn_level_result.records:
        levels.setdefault(r["boss_key"], []).append(r["level"])
    for boss_levels in levels.values():
        assert boss_levels == list(range(len(boss_levels)))


def test_every_level_has_an_image(spawn_level_result: HandlerResult) -> None:
    assert all(r["image_path"].startswith("ui_texture/") for r in spawn_level_result.records)


def test_boss_characters_take_the_lowest_level() -> None:
    assert boss_characters(load_binary_fixture(FILE_NAME))[_FERRID_KEY] == _FERRID
