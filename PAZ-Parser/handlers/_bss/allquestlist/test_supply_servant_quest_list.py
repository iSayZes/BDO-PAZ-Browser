from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerResult, case_id, run_case
from tests.quest_list_cases import assert_distinct_listed_quests, quest_list_case


# The list holds no entries on the clients checked so far, so there is no
# stable key for a TargetTest yet.
CASE = quest_list_case("supplyservantquestlist.bss")


@pytest.fixture(scope="module")
def supply_list(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_supply_servant_quest_list(spec: Any, supply_list: HandlerResult) -> None:
    supply_list.check(spec)


def test_entries_are_distinct_quests(supply_list: HandlerResult) -> None:
    assert_distinct_listed_quests(supply_list)
