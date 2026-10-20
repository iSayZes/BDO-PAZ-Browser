from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerResult, TargetTest, case_id, run_case
from tests.quest_list_cases import assert_distinct_listed_quests, quest_list_case


CASE = quest_list_case(
    "doguildquestlist.bss",
    # A Very Minute Flaw: (76 << 16) | 1001.
    TargetTest(col="packed_quest_id", value=4981737, expected={"quest_chain_id": 1001, "quest_id": 76}),
)


@pytest.fixture(scope="module")
def guide_list(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_do_guide_list(spec: Any, guide_list: HandlerResult) -> None:
    guide_list.check(spec)


def test_entries_are_distinct_quests(guide_list: HandlerResult) -> None:
    assert_distinct_listed_quests(guide_list)
