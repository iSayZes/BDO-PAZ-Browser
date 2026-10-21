from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.pabr_offset import parse_bare_u32_offset_rows
from tests.fixtures import load_binary_fixture
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

from _bss.yachthandrank.parser import FILE_NAME as HAND_RANK_FILE
from _dbss.yachtdicepreset.parser import FILE_NAME as DICE_PRESET_FILE

from .parser import FILE_NAME


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
# Eileen (NPC 40063) and her knowledge entry 45, the first row of the
# NPC_DiceList sheet the file is compiled from.
_EILEEN_ROW = 1
_EILEEN_NPC = 40063
_EILEEN_KNOWLEDGE = 45
_DICE_PRESET_OFFSET_FILE = "yachtdicepresetoffset.dbss"
# Eileen's row 1 offers the six single-eye hands, Bit o' Ones first.
_BIT_O_ONES = "Bit o' Ones"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={HAND_RANK_FILE: HAND_RANK_FILE, DICE_PRESET_FILE: DICE_PRESET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["npc_name", "knowledge_name", "hand_rank_names"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "npc_dice_info_key", "npc_key", "npc_name", "dice_preset_key", "dice_text", "hand_rank_count",
            "hand_rank_keys", "hand_rank_names", "knowledge_key", "knowledge_name", "deck_limit", "roll_count_max",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="npc_dice_info_key",
            value=_EILEEN_ROW,
            expected={"npc_key": _EILEEN_NPC, "knowledge_key": _EILEEN_KNOWLEDGE},
        ),
        UserLanguageTest(fields=["npc_name", "knowledge_name", "hand_rank_names"]),
    ],
)


@pytest.fixture(scope="module")
def yachtnpcdiceinfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_yachtnpcdiceinfo_bss(spec: Any, yachtnpcdiceinfo_result: HandlerResult) -> None:
    yachtnpcdiceinfo_result.check(spec)


def test_row_keys_are_unique(yachtnpcdiceinfo_result: HandlerResult) -> None:
    keys = [r["npc_dice_info_key"] for r in yachtnpcdiceinfo_result.records]
    assert len(keys) == len(set(keys)), "a key has two rows"


def test_hand_rank_keys_follow_their_count(yachtnpcdiceinfo_result: HandlerResult) -> None:
    for r in yachtnpcdiceinfo_result.records:
        assert len(r["hand_rank_keys"]) == r["hand_rank_count"] == len(r["hand_rank_names"]), r["npc_dice_info_key"]


def test_hand_ranks_show_their_names(yachtnpcdiceinfo_result: HandlerResult) -> None:
    eileen = next(r for r in yachtnpcdiceinfo_result.records if r["npc_dice_info_key"] == _EILEEN_ROW)
    assert eileen["hand_rank_names"][0] == _BIT_O_ONES


def test_every_row_shows_its_preset_dice(yachtnpcdiceinfo_result: HandlerResult) -> None:
    for r in yachtnpcdiceinfo_result.records:
        assert r["dice_text"], r["npc_dice_info_key"]


def test_every_dice_preset_is_in_the_preset_table(yachtnpcdiceinfo_result: HandlerResult) -> None:
    preset_keys = {row.entry_id for row in parse_bare_u32_offset_rows(load_binary_fixture(_DICE_PRESET_OFFSET_FILE))}
    used = {r["dice_preset_key"] for r in yachtnpcdiceinfo_result.records}
    assert used <= preset_keys, f"dice presets missing from {_DICE_PRESET_OFFSET_FILE}: {sorted(used - preset_keys)}"
