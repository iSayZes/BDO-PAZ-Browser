from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

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

from .parser import FILE_NAME, RANK_TIER_COUNT, parse_fishcompetition


# 8330 Tilefish and its title item 767766 [Title] The Biggest Tilefish (LOC type 0).
_TILEFISH = 8330
_TILEFISH_TITLE = 767766

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["fish_name", "title_item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "fish_item_key",
                "grade",
                "rank_reward_item_keys",
                "title_item_key",
                "fish_name",
                "rank_tiers",
                "rewards",
                "title_item_name",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="fish_item_key", value=_TILEFISH, expected={"title_item_key": _TILEFISH_TITLE}),
        UserLanguageTest(fields=["fish_name", "title_item_name"]),
    ],
)


@pytest.fixture(scope="module")
def competition_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fishcompetition_bss(spec: Any, competition_result: HandlerResult) -> None:
    competition_result.check(spec)


def test_rank_tiers_rise() -> None:
    """One last rank per reward tier, each past the one before."""
    tiers = parse_fishcompetition(load_binary_fixture(FILE_NAME)).rank_tiers
    assert len(tiers) == RANK_TIER_COUNT
    assert tiers[0] >= 1
    assert all(earlier < later for earlier, later in zip(tiers, tiers[1:]))


def test_every_row_has_one_reward_per_tier(competition_result: HandlerResult) -> None:
    broken = [
        record["fish_item_key"]
        for record in competition_result.records
        if len(record["rank_reward_item_keys"]) != RANK_TIER_COUNT
    ]
    assert not broken, broken
