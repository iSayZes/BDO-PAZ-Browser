from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="allquestlist.bss",
    data_file="allquestlist.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title"],
    internal_path="gamecommondata/binary/allquestlist.bss",
    tests=[
        SchemaTest(required_keys=["slot", "packed_quest_id", "quest_chain_id", "quest_id", "title"]),
        CountTest(expected=19599),
        PosTest(
            pos=0,
            expected={
                "slot": 0,
                "packed_quest_id": 1050655,
                "quest_chain_id": 2079,
                "quest_id": 16,
                "title": "[Elvia Weekly] Gigagord",
            },
        ),
        TargetTest(
            col="slot",
            value=19598,
            expected={
                "packed_quest_id": 181218,
                "quest_chain_id": 50146,
                "quest_id": 2,
                "title": "A Whole New Experience Presented by Fughar! (Black Spirit Pass)",
            },
        ),
    ],
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
    spec.check(allquestlist_result.records)
