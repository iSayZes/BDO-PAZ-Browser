from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerResult, PaFieldTest, TargetTest, case_id, run_case
from tests.quest_list_cases import quest_list_case


CASE = quest_list_case(
    "allquestlist.bss",
    # Academy and event quests carry a coloured `[Olvia Academy]` prefix.
    PaFieldTest(field="title"),
    TargetTest(
        col="packed_quest_id",
        value=1050655,
        expected={
            "quest_chain_id": 2079,
            "quest_id": 16,
            "title": "[Elvia Weekly] Gigagord",
        },
    ),
    TargetTest(
        col="packed_quest_id",
        value=181218,
        expected={
            "quest_chain_id": 50146,
            "quest_id": 2,
            "title": "A Whole New Experience Presented by Fughar! (Black Spirit Pass)",
        },
    ),
)


@pytest.fixture(scope="module")
def allquestlist_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_allquestlist_bss(spec: Any, allquestlist_result: HandlerResult) -> None:
    allquestlist_result.check(spec)
