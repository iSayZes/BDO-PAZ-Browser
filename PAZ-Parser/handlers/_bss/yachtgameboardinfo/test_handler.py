from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _bss.yachthandrank.parser import FILE_NAME as HAND_RANK_FILE, parse_yachthandrank_records
from tests.fixtures import load_binary_fixture
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

from .parser import FILE_NAME


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
# Board 1 is the most basic mode, one star (the PVP_GameBoard sheet of client 1784).
_BASIC_BOARD = 1
_MAX_STARS = 5
_TEXTURE_PREFIX = "Combine_ETC_MiniGame_Ya_pvp_"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={HAND_RANK_FILE: HAND_RANK_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["desc", "hand_rank_names"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "game_board_key", "hand_rank_count", "hand_rank_keys", "roll_count_max", "desc_kr_index", "desc_kr",
            "icon_texture_index", "icon_texture", "big_texture_index", "big_texture", "level", "is_use_matching",
            "desc", "hand_rank_names",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="level", min_val=1, max_val=_MAX_STARS),
        RangeTest(col="is_use_matching", min_val=0, max_val=1),
        TargetTest(col="game_board_key", value=_BASIC_BOARD, expected={"level": 1}),
        UserLanguageTest(fields=["desc", "hand_rank_names"]),
    ],
)


@pytest.fixture(scope="module")
def yachtgameboardinfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_yachtgameboardinfo_bss(spec: Any, yachtgameboardinfo_result: HandlerResult) -> None:
    yachtgameboardinfo_result.check(spec)


def test_hand_rank_keys_follow_their_count(yachtgameboardinfo_result: HandlerResult) -> None:
    for r in yachtgameboardinfo_result.records:
        assert len(r["hand_rank_keys"]) == r["hand_rank_count"] == len(r["hand_rank_names"]), r["game_board_key"]


def test_every_hand_rank_is_in_the_hand_rank_table(yachtgameboardinfo_result: HandlerResult) -> None:
    keys = {record["hand_rank_key"] for record in parse_yachthandrank_records(load_binary_fixture(HAND_RANK_FILE))}
    used = {key for r in yachtgameboardinfo_result.records for key in r["hand_rank_keys"]}
    assert used <= keys, f"hand ranks missing from {HAND_RANK_FILE}: {sorted(used - keys)}"


def test_every_row_has_its_textures(yachtgameboardinfo_result: HandlerResult) -> None:
    for r in yachtgameboardinfo_result.records:
        assert r["icon_texture"].startswith(_TEXTURE_PREFIX), r["game_board_key"]
        assert r["big_texture"].startswith(_TEXTURE_PREFIX), r["game_board_key"]
