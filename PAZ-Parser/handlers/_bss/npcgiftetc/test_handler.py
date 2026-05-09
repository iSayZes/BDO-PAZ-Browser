from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="npcgiftetc.bss",
    data_file="npcgiftetc.bss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/npcgiftetc.bss",
    tests=[
        SchemaTest(required_keys=["field", "value", "notes"]),
        CountTest(expected=8),
        PosTest(
            pos=0,
            expected={
                "field": "config_a",
                "value": 5,
                "notes": "Global gift-system value",
            },
        ),
        TargetTest(
            col="field",
            value="config_d",
            expected={"value": 50000000},
        ),
        TargetTest(
            col="field",
            value="config_e",
            expected={"value": 20},
        ),
    ],
)


@pytest.fixture(scope="module")
def npcgiftetc_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_npcgiftetc_bss(spec: Any, npcgiftetc_result: HandlerResult) -> None:
    spec.check(npcgiftetc_result.records)
