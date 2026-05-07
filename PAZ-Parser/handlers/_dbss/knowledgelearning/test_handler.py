from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="knowledgelearning.dbss",
    data_file="knowledgelearning.dbss",
    companion_files={"knowledgelearningoffset.dbss": "knowledgelearningoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Knowledge Name"],
    internal_path="gamecommondata/binary/knowledgelearning.dbss",
    tests=[
        SchemaTest(required_keys=["knowledge_id", "kind", "knowledge_name", "offset"]),
        CountTest(expected=4391),
        PosTest(
            pos=0,
            expected={
                "knowledge_id": 7302,
                "kind": 13,
                "knowledge_name": "Feldspar",
                "offset": 8,
            },
        ),
        TargetTest(
            col="knowledge_id",
            value=4893,
            expected={
                "kind": 13,
                "knowledge_name": "Valencian Lion",
                "offset": 25,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def knowledgelearning_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_knowledgelearning_dbss(spec: Any, knowledgelearning_result: HandlerResult) -> None:
    spec.check(knowledgelearning_result.records)
