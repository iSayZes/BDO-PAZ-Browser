from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _bss.stringtable.text import STRINGTABLE_FILE
from _common.texture_string import TEXTURE_STRING_COMBINE
from .parser import FILE_NAME, TEXTURE_INFO_SLOTS, parse_journalinfostaticstatus


# Morning Land's first card tracks quest chain 8503 (its chapter key
# LUA_MORNINGLAND_QUESTBOARD_TAB1); the same card on clients 3251 and 3482.
_FIRST_MORNING_LAND_CHAIN = 8503
_MORNING_LAND_TAB1 = "LUA_MORNINGLAND_QUESTBOARD_TAB1"


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={STRINGTABLE_FILE: STRINGTABLE_FILE, TEXTURE_STRING_COMBINE: TEXTURE_STRING_COMBINE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["chapter_text", "title_text", "scenario_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "journal_list_index", "chapter_index", "ui_type", "ui_type_index", "journal_index", "quest_group_no",
                "unknown_0a", "chapter_string", "scenario_desc", "title_string", "unknown_18", "texture_normal",
                "texture_over", "unknown_22", "detail_btn_texture_ids", "detail_btn_string", "unknown_36",
                "book_quests", "ed_textures", "chapter_text", "title_text", "scenario_text", "book_quests_text",
            ],
        ),
        RangeTest(col="ui_type", min_val=0, max_val=1),
        TargetTest(
            col="quest_group_no",
            value=_FIRST_MORNING_LAND_CHAIN,
            expected={"journal_list_index": 0, "chapter_string": _MORNING_LAND_TAB1},
        ),
    ],
)


@pytest.fixture(scope="module")
def journal_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_journalinfostaticstatus_bss(spec: Any, journal_result: HandlerResult) -> None:
    journal_result.check(spec)


def test_cards_are_unique_per_board(journal_result: HandlerResult) -> None:
    cards = [
        (r["journal_list_index"], r["chapter_index"], r["ui_type_index"], r["journal_index"])
        for r in journal_result.records
    ]
    assert len(cards) == len(set(cards))


def test_every_board_has_its_texture_info() -> None:
    journals, texture_infos = parse_journalinfostaticstatus(load_binary_fixture(FILE_NAME))
    assert len(texture_infos) == len({journal["journal_list_index"] for journal in journals})
    assert all(len(slots) == TEXTURE_INFO_SLOTS for slots in texture_infos)


def test_every_card_has_a_book_quest_and_an_ed_texture(journal_result: HandlerResult) -> None:
    for record in journal_result.records:
        assert record["book_quests"], record["quest_group_no"]
        assert record["ed_textures"], record["quest_group_no"]


def test_every_game_key_has_english_text(journal_result: HandlerResult) -> None:
    """With English LOC each chapter and title key resolves to text, not the key itself."""
    unresolved = [
        key for r in journal_result.records
        for key, text in ((r["chapter_string"], r["chapter_text"]), (r["title_string"], r["title_text"]))
        if key and text == key
    ]
    assert not unresolved, unresolved
