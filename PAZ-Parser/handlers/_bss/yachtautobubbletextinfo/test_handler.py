from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _bss.yachthandrank.parser import FILE_NAME as HAND_RANK_FILE, parse_yachthandrank_records
from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from .parser import FILE_NAME, NPC_GROUP, PC_GROUP, TEXT_SLOTS


# PABR magic, then the player rows' u32 count.
_PC_COUNT_OFFSET = 4
_COUNT_SIZE = 4
_ROW_SIZE = 36
# Eileen (NPC 40063) speaks key 6, her first row (the YachtBubbleText sheet of client 1784).
_EILEEN_FIRST_ROW = 6
_EILEEN = 40063
_MAX_CONDITION = 7


def _declared_rows(source: CaseInput) -> int:
    """The player count plus the NPC count that follows the player rows."""
    pc_count = struct.unpack_from("<I", source.data, _PC_COUNT_OFFSET)[0]
    npc_count_offset = _PC_COUNT_OFFSET + _COUNT_SIZE + pc_count * _ROW_SIZE
    return pc_count + struct.unpack_from("<I", source.data, npc_count_offset)[0]


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={HAND_RANK_FILE: HAND_RANK_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["speaker", "hand_rank_name", "lines"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "bubble_text_key", "group", "character_key", "hand_rank_key", "text_kr_indexes", "texts_kr",
            "condition", "unknown_23", "npc_key", "speaker", "condition_name", "hand_rank_key_shown",
            "hand_rank_name", "lines",
        ]),
        DeclaredCountTest(declared=_declared_rows),
        RangeTest(col="condition", min_val=0, max_val=_MAX_CONDITION),
        TargetTest(
            col="bubble_text_key",
            value=_EILEEN_FIRST_ROW,
            expected={"group": NPC_GROUP, "character_key": _EILEEN, "speaker": "Eileen"},
        ),
        UserLanguageTest(fields=["speaker", "hand_rank_name", "lines"]),
    ],
)


@pytest.fixture(scope="module")
def yachtautobubbletextinfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_yachtautobubbletextinfo_bss(spec: Any, yachtautobubbletextinfo_result: HandlerResult) -> None:
    yachtautobubbletextinfo_result.check(spec)


def test_keys_are_unique_over_both_groups(yachtautobubbletextinfo_result: HandlerResult) -> None:
    keys = [r["bubble_text_key"] for r in yachtautobubbletextinfo_result.records]
    assert len(keys) == len(set(keys)), "a key has two rows"


def test_player_rows_have_no_npc_and_npc_rows_have_one(yachtautobubbletextinfo_result: HandlerResult) -> None:
    for r in yachtautobubbletextinfo_result.records:
        has_npc = r["character_key"] != 0
        assert has_npc == (r["group"] == NPC_GROUP), r["bubble_text_key"]
        assert r["group"] in (PC_GROUP, NPC_GROUP), r["bubble_text_key"]


def test_every_row_has_a_trigger_and_a_line(yachtautobubbletextinfo_result: HandlerResult) -> None:
    for r in yachtautobubbletextinfo_result.records:
        assert r["condition"] or r["hand_rank_key"], r["bubble_text_key"]
        assert len(r["texts_kr"]) == TEXT_SLOTS and r["texts_kr"][0], r["bubble_text_key"]


def test_every_hand_rank_is_in_the_hand_rank_table(yachtautobubbletextinfo_result: HandlerResult) -> None:
    keys = {record["hand_rank_key"] for record in parse_yachthandrank_records(load_binary_fixture(HAND_RANK_FILE))}
    used = {r["hand_rank_key"] for r in yachtautobubbletextinfo_result.records if r["hand_rank_key"]}
    assert used <= keys, f"hand ranks missing from {HAND_RANK_FILE}: {sorted(used - keys)}"
