from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _dbss.minigamefindpattern.parser import FILE_NAME as PATTERN_FILE, parse_minigamefindpattern
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, parse_minigamefind


_TYPE_COUNT_AT = 4
_MAX_DEPTH = 5
# The first chain: game type 1 leads to 2 (the 1784 sheet and client 3482).
_FIRST_GAME_TYPE = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["tool_names", "reward_names", "lakiaro_names"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "game_type",
                "game_type_dup",
                "next_game",
                "min_damage_rate",
                "next_rate",
                "life_type",
                "life_rate",
                "tool_item_keys",
                "tool_rate",
                "stone_rate",
                "stone_drop_item_key",
                "col",
                "row",
                "start_pos",
                "min_root_count",
                "begin_root_count",
                "use_slot_indexes",
                "reward_item_keys",
                "lakiaros",
                "lakiaro_names",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_TYPE_COUNT_AT)),
        TargetTest(col="game_type", value=_FIRST_GAME_TYPE, expected={"game_type_dup": _FIRST_GAME_TYPE, "next_game": 2}),
    ],
)


@pytest.fixture(scope="module")
def find_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_minigamefind_bss(spec: Any, find_result: HandlerResult) -> None:
    find_result.check(spec)


def test_each_row_repeats_its_key(find_result: HandlerResult) -> None:
    assert all(r["game_type"] == r["game_type_dup"] for r in find_result.records)


def test_next_games_are_game_types(find_result: HandlerResult) -> None:
    game_types = {r["game_type"] for r in find_result.records}
    assert all(r["next_game"] in game_types for r in find_result.records if r["next_game"] is not None)


def test_every_lakiaro_row_joins_a_game_type(find_result: HandlerResult) -> None:
    tables = parse_minigamefind(load_binary_fixture(FILE_NAME))
    joined = sum(len(r["lakiaros"]) for r in find_result.records)
    assert tables.collect_rates
    assert joined == len(tables.collect_rates)


def test_lakiaro_rows_name_an_image_and_a_depth() -> None:
    for rate in parse_minigamefind(load_binary_fixture(FILE_NAME)).collect_rates:
        assert rate["image_file"].lower().endswith(".dds"), rate
        assert 1 <= rate["depth"] <= _MAX_DEPTH, rate


def test_slot_groups_exist_in_the_pattern_table(find_result: HandlerResult) -> None:
    slots = {row["slot_index"] for row in parse_minigamefindpattern(load_binary_fixture(PATTERN_FILE))}
    used = {slot for r in find_result.records for slot in r["use_slot_indexes"] if slot}
    assert used
    assert used <= slots, used - slots


@pytest.mark.parametrize("field", ["start_pos", "min_root_count", "begin_root_count"])
def test_grid_counts_fit_the_grid(field: str, find_result: HandlerResult) -> None:
    for r in find_result.records:
        assert all(0 <= value <= max(r["col"], r["row"]) for value in r[field]), r
