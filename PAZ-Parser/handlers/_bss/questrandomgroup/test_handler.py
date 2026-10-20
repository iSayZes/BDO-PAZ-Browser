from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

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

from .parser import FILE_NAME


# PABR magic, then the u32 row count.
_ROW_COUNT_OFFSET = 4
# Group 1 is the one `checkRandomGroup(1, index)` names in the conditions of
# the [Academy] [Weekly ...] quests of chain 2322.
_ACADEMY_WEEKLY_GROUP = 1
_ACADEMY_WEEKLY_CHAIN = 2322


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "group_key", "quest_count", "quest_chain_id", "draw_count",
            "unknown_00", "unknown_12", "unknown_14", "unknown_18",
        ]),
        DeclaredCountTest(declared=header_count(offset=_ROW_COUNT_OFFSET)),
        TargetTest(
            col="group_key",
            value=_ACADEMY_WEEKLY_GROUP,
            expected={"quest_chain_id": _ACADEMY_WEEKLY_CHAIN},
        ),
    ],
)


@pytest.fixture(scope="module")
def questrandomgroup_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_questrandomgroup_bss(spec: Any, questrandomgroup_result: HandlerResult) -> None:
    questrandomgroup_result.check(spec)


def test_group_keys_are_unique(questrandomgroup_result: HandlerResult) -> None:
    keys = [r["group_key"] for r in questrandomgroup_result.records]
    assert len(keys) == len(set(keys)), "a group key is listed twice"


def test_every_group_has_quests(questrandomgroup_result: HandlerResult) -> None:
    empty = [r["group_key"] for r in questrandomgroup_result.records if r["quest_count"] == 0]
    assert not empty, f"groups without quest slots: {empty}"
