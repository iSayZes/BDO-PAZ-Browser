from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="planttown.bss",
    data_file="planttown.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Node Name"],
    internal_path="gamecommondata/binary/planttown.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "slot",
                "node_id",
                "node_name",
                "unknown_a",
                "unknown_b",
                "unknown_c",
                "unknown_d",
            ],
        ),
        CountTest(expected=45),
        PosTest(
            pos=0,
            expected={
                "slot": 0,
                "node_id": 1785,
                "node_name": "Nampo's Moodle Village",
                "unknown_a": 1,
                "unknown_b": 2,
                "unknown_c": 10,
                "unknown_d": 1,
            },
        ),
        PosTest(
            pos=8,
            expected={
                "slot": 8,
                "node_id": 1623,
                "node_name": "Grána",
            },
        ),
        TargetTest(
            col="node_id",
            value=1301,
            expected={
                "slot": 25,
                "node_name": "Valencia City",
                "unknown_a": 1,
                "unknown_b": 2,
                "unknown_c": 10,
                "unknown_d": 1,
            },
        ),
        PosTest(
            pos=-1,
            expected={
                "slot": 44,
                "node_id": 301,
                "node_name": "Heidel",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def planttown_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_planttown_bss(spec: Any, planttown_result: HandlerResult) -> None:
    spec.check(planttown_result.records)
