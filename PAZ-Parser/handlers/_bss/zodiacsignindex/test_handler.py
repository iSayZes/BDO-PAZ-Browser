from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="zodiacsignindex.bss",
    data_file="zodiacsignindex.bss",
    companion_files={"zodiacsign.dbss": "zodiacsign.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name"],
    internal_path="gamecommondata/customization/zodiacsignindex.bss",
    tests=[
        SchemaTest(required_keys=["slot", "zodiac_id", "name", "known"]),
        CountTest(expected=12),
        PosTest(
            pos=0,
            expected={
                "slot": 0,
                "zodiac_id": 1,
                "name": "Hammer",
                "known": True,
            },
        ),
        TargetTest(
            col="zodiac_id",
            value=12,
            expected={
                "slot": 11,
                "name": "Goblin",
                "known": True,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def zodiacsignindex_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_zodiacsignindex_bss(spec: Any, zodiacsignindex_result: HandlerResult) -> None:
    spec.check(zodiacsignindex_result.records)
