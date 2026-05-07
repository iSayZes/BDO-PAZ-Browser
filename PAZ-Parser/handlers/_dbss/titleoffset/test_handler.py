from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="titleoffset.dbss",
    data_file="titleoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/titleoffset.dbss",
    tests=[
        SchemaTest(required_keys=["title_id", "offset"]),
        CountTest(expected=3048),
        PosTest(
            pos=0,
            expected={
                "title_id": 1,
                "offset": 510,
            },
        ),
        TargetTest(
            col="title_id",
            value=3795,
            expected={"offset": 835800},
        ),
    ],
)


@pytest.fixture(scope="module")
def titleoffset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_titleoffset_dbss(spec: Any, titleoffset_result: HandlerResult) -> None:
    spec.check(titleoffset_result.records)
