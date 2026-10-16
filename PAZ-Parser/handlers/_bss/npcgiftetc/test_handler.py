from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerCase, HandlerResult, SchemaTest, TargetTest, case_id, run_case


# The block is a fixed 32-byte layout with no row count, so the field list is the handler's own.
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
        TargetTest(
            col="field",
            value="unknown_04",
            expected={"notes": "Global gift-system value"},
        ),
        TargetTest(
            col="field",
            value=("unknown_10", "unknown_14", "unknown_1c"),
            expected=[{"value": 0}, {"value": 0}, {"value": 0}],
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
    npcgiftetc_result.check(spec)
