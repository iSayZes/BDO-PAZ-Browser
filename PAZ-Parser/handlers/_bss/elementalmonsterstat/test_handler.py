from __future__ import annotations

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

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from .parser import FILE_NAME
from .text import PART_PARTY, PART_SOLO

# Calamity 1 Golden Pig King, the first Donghae (Solo) group (client 2519 onward).
_GOLDEN_PIG_KING = 23608
# Normal Jigwi, the first Hwanghae (Party) group (client 3002 onward).
_JIGWI = 24562
_TOP_SOLO_LEVEL = 9
_ELEMENT_TYPES = (0, 2)

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "weak_aura", "part", "difficulty"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "character_key", "character_key_dup", "unlock_character_key",
            "unlock_mental_card_key", "offence_stat", "defence_stat", "element_type",
            "level", "group", "is_boss", "monster_part", "show_reward_count",
            "show_rewards", "position_x", "position_y", "position_z", "min_ap",
            "name", "has_character_row", "unlock_character_name",
            "unlock_mental_card_name", "weak_aura", "part", "difficulty",
            "show_rewards_text",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="element_type", min_val=_ELEMENT_TYPES[0], max_val=_ELEMENT_TYPES[1]),
        RangeTest(col="level", min_val=0, max_val=_TOP_SOLO_LEVEL),
        RangeTest(col="monster_part", min_val=PART_SOLO, max_val=PART_PARTY),
        UserLanguageTest(fields=["name", "weak_aura", "part", "difficulty"]),
        TargetTest(col="character_key", value=_GOLDEN_PIG_KING, expected={
            "group": 0,
            "level": 0,
            "element_type": 0,
            "is_boss": True,
            "monster_part": PART_SOLO,
            "name": "Golden Pig King",
            "part": "Donghae (Solo)",
            "difficulty": "Calamity 1",
            "weak_aura": "Sun Aura",
            "has_character_row": True,
        }),
        TargetTest(col="character_key", value=_JIGWI, expected={
            "level": 0,
            "is_boss": True,
            "monster_part": PART_PARTY,
            "name": "Jigwi",
            "part": "Hwanghae (Party)",
            "difficulty": "Normal",
        }),
    ],
)


@pytest.fixture(scope="module")
def stat_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_elementalmonsterstat_bss(spec: Any, stat_result: HandlerResult) -> None:
    stat_result.check(spec)


def test_keys_are_unique_and_repeated(stat_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in stat_result.records]
    assert len(keys) == len(set(keys))
    assert all(r["character_key_dup"] == r["character_key"] for r in stat_result.records)


def test_each_group_and_level_has_one_boss(stat_result: HandlerResult) -> None:
    bosses = [(r["group"], r["level"]) for r in stat_result.records if r["is_boss"]]
    assert bosses
    assert len(bosses) == len(set(bosses))


def test_unlock_boss_is_the_boss_one_level_lower(stat_result: HandlerResult) -> None:
    boss_at = {(r["group"], r["level"]): r["character_key"] for r in stat_result.records if r["is_boss"]}
    unlocked = [r for r in stat_result.records if r["unlock_character_key"]]
    assert unlocked
    for r in unlocked:
        assert boss_at.get((r["group"], r["level"] - 1)) == r["unlock_character_key"], r["character_key"]


def test_show_rewards_follow_their_count(stat_result: HandlerResult) -> None:
    for r in stat_result.records:
        assert len(r["show_rewards"]) == r["show_reward_count"]
        assert all(item["count"] > 0 for item in r["show_rewards"])
