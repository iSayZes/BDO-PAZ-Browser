from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CountTest,
    HandlerCase,
    HandlerResult,
    PosTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)


CASE = HandlerCase(
    handler_name="exploration.bss",
    data_file="exploration.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Knowledge Name", "Description", "Hint"],
    internal_path="gamecommondata/binary/exploration.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "slot",
                "file_offset",
                "record_size",
                "knowledge_id",
                "knowledge_name",
                "description",
                "hint",
                "group_id",
                "enabled",
                "unknown_flags",
                "anchor_id_a",
                "anchor_id_b",
                "radius",
                "radius_squared",
            ],
        ),
        CountTest(expected=1003),
        PosTest(
            pos=0,
            expected={
                "file_offset": 8,
                "knowledge_id": 65,
                "knowledge_name": "Cron Castle Altar",
                "group_id": 0,
                "enabled": 1,
                "anchor_id_a": 905,
                "anchor_id_b": 905,
                "radius": 2700.0,
            },
        ),
        TargetTest(
            col="knowledge_id",
            value=1008,
            expected={
                "slot": 1,
                "knowledge_name": "Altin",
                "group_id": 3,
                "anchor_id_a": 806,
                "anchor_id_b": 806,
                "radius": 9700.0,
            },
        ),
        TargetTest(
            col="knowledge_id",
            value=1053,
            expected={
                "slot": 2,
                "knowledge_name": "Rohu",
                "group_id": 4,
                "anchor_id_a": 829,
                "anchor_id_b": 829,
                "radius": 9700.0,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def exploration_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_exploration_bss(
    spec: Any,
    exploration_result: HandlerResult,
) -> None:
    spec.check(exploration_result.records)
