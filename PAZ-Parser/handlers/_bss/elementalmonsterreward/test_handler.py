from __future__ import annotations

import struct
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

from _bss.elementalmonsterstat.parser import FILE_NAME as STAT_FILE, boss_difficulties
from .parser import FILE_NAME, parse_elementalmonsterreward
from .text import rank_label

# Calamity 1 Golden Pig King, the first Donghae (Solo) group (client 2519 onward).
_GOLDEN_PIG_KING = 23608
_FIRST_RANK = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={STAT_FILE: STAT_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "part", "difficulty", "rank_label"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "character_key", "name", "is_part2", "has_stat_row", "part", "level",
            "difficulty", "rank", "rank_label", "rewards", "rewards_text",
        ]),
        UserLanguageTest(fields=["name", "part", "difficulty", "rank_label"]),
        TargetTest(col="character_key", value=_GOLDEN_PIG_KING, expected={
            "name": "Golden Pig King",
            "is_part2": False,
            "has_stat_row": True,
            "part": "Donghae (Solo)",
            "difficulty": "Calamity 1",
            "rank": _FIRST_RANK,
            "rank_label": "#1",
        }),
    ],
)


@pytest.fixture(scope="module")
def reward_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_elementalmonsterreward_bss(spec: Any, reward_result: HandlerResult) -> None:
    reward_result.check(spec)


def test_first_table_holds_the_declared_bosses() -> None:
    data = load_binary_fixture(FILE_NAME)
    (declared,) = struct.unpack_from("<I", data, 0)
    tables = parse_elementalmonsterreward(data)
    assert len(tables.records) == declared
    assert len({r["character_key"] for r in tables.records}) == declared


def test_every_boss_is_a_boss_of_elementalmonsterstat() -> None:
    tables = parse_elementalmonsterreward(load_binary_fixture(FILE_NAME))
    bosses = boss_difficulties(load_binary_fixture(STAT_FILE))
    keys = {r["character_key"] for r in tables.records + tables.part2_records}
    assert keys <= bosses.keys()


def test_rank_tiers_rise_within_a_boss() -> None:
    tables = parse_elementalmonsterreward(load_binary_fixture(FILE_NAME))
    for record in tables.records + tables.part2_records:
        ranks = [tier["rank"] for tier in record["rank_tiers"]]
        assert ranks == sorted(set(ranks)), record["character_key"]
        assert all(len(tier["rewards"]) == tier["reward_count"] for tier in record["rank_tiers"])


def test_rank_labels_follow_the_window() -> None:
    assert rank_label(1, None, "#{rank}") == "#1"
    assert rank_label(5, 1, "#{rank}") == "#2 ~ #5"
    assert rank_label(50, None, "#{rank}") == "~ #50"
