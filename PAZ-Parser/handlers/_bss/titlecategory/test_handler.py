from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="titlecategory.bss",
    data_file="titlecategory.bss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/customization/titlecategory.bss",
    tests=[
        SchemaTest(required_keys=["title_id", "category_id"]),
        CountTest(expected=1528),
        PosTest(
            pos=0,
            expected={
                "title_id": 1380073808,
                "category_id": 4,
            },
        ),
        TargetTest(
            col="title_id",
            value=1243,
            expected={"category_id": 211},
        ),
    ],
)


@pytest.fixture(scope="module")
def titlecategory_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_titlecategory_bss(spec: Any, titlecategory_result: HandlerResult) -> None:
    spec.check(titlecategory_result.records)
