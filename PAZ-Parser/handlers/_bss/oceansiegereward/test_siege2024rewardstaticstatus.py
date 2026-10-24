"""`siege2024rewardstaticstatus.bss`: the land siege table with the rows of `oceansiegereward.bss`."""

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
    case_id,
    run_case,
)

from .parser import REWARD_SET_COUNT, SET_REWARD_LISTS, parse_reward_rows
from .test_handler import _declared_rewards


_FILE_NAME = "siege2024rewardstaticstatus.bss"

CASE = HandlerCase(
    handler_name=_FILE_NAME,
    data_file=_FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name", "skill_name_1", "skill_name_2"],
    internal_path=f"gamecommondata/binary/{_FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "unknown_00",
                "reward_set",
                "reward_list",
                "reward_list_number",
                "item_id",
                "unknown_04",
                "count",
                "skill_key_1",
                "skill_key_2",
                "icon_path",
                "item_name",
                "skill_name_1",
                "skill_name_2",
            ],
        ),
        DeclaredCountTest(declared=_declared_rewards),
        RangeTest(col="reward_set", min_val=1, max_val=REWARD_SET_COUNT),
        RangeTest(col="reward_list_number", min_val=1, max_val=len(SET_REWARD_LISTS)),
    ],
)


@pytest.fixture(scope="module")
def siege_reward_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_siege2024rewardstaticstatus_bss(spec: Any, siege_reward_result: HandlerResult) -> None:
    siege_reward_result.check(spec)


def test_every_item_and_skill_has_a_name(siege_reward_result: HandlerResult) -> None:
    for record in siege_reward_result.records:
        assert record["item_name"] and record["skill_name_1"] and record["skill_name_2"], record


def test_each_row_has_its_own_u16(siege_reward_result: HandlerResult) -> None:
    keys = [row["unknown_00"] for row in parse_reward_rows(siege_reward_result.source.data, _FILE_NAME)]
    assert keys and len(keys) == len(set(keys))


def test_errors_name_the_land_siege_file() -> None:
    with pytest.raises(ValueError, match=_FILE_NAME):
        parse_reward_rows(b"PABR", _FILE_NAME)
