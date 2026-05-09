from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="newquest.bss",
    data_file="newquest.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title"],
    internal_path="gamecommondata/binary/newquest.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "group",
                "row",
                "flags",
                "quest_chain_id",
                "quest_id",
                "packed_quest_id",
                "title",
                "sequence_a",
                "sequence_b",
                "sequence_c",
            ],
        ),
        CountTest(expected=1255),
        PosTest(
            pos=0,
            expected={
                "group": 0,
                "row": 0,
                "flags": 0,
                "quest_chain_id": 11059,
                "quest_id": 9,
                "packed_quest_id": 600883,
                "title": "[Event] Love for Pets",
                "sequence_a": 1,
                "sequence_b": 2,
                "sequence_c": 2,
            },
        ),
        PosTest(
            pos=1,
            expected={
                "group": 0,
                "row": 1,
                "quest_chain_id": 11059,
                "quest_id": 10,
                "title": "[Event] Savory Good Feed",
            },
        ),
        TargetTest(
            col="packed_quest_id",
            value=77129,
            expected={
                "group": 223,
                "quest_chain_id": 11593,
                "quest_id": 1,
                "sequence_a": 899,
                "sequence_b": 2,
                "sequence_c": 2,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def newquest_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_newquest_bss(spec: Any, newquest_result: HandlerResult) -> None:
    spec.check(newquest_result.records)
