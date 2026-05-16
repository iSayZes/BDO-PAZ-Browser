from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


CASE = HandlerCase(
    handler_name="plantworker.bss",
    data_file="plantworker.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name"],
    internal_path="gamecommondata/binary/plantworker.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "slot",
                "worker_id",
                "next_worker_id",
                "name",
                "move_speed",
                "stamina",
                "luck",
                "icon_index",
                "icon_path",
                "base_work_speed",
            ],
        ),
        CountTest(expected=106),
        PosTest(
            pos=0,
            expected={
                "worker_id": 8047,
                "next_worker_id": 8048,
                "name": "Dokkebi Worker",
                "move_speed": 350,
                "stamina": 8,
                "luck": 50000,
                "icon_index": 0,
                "icon_path": "New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/Morning_Dokev01.dds",
                "base_work_speed": 60000000,
            },
        ),
        TargetTest(
            col="worker_id",
            value=7502,
            expected={
                "name": "Giant Worker",
                "next_worker_id": 7551,
                "move_speed": 200,
                "stamina": 25,
                "luck": 50000,
                "icon_index": 10,
                "icon_path": "New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/Worker_Giant01.dds",
                "base_work_speed": 30000000,
            },
        ),
        TargetTest(
            col="worker_id",
            value=7504,
            expected={
                "name": "Goblin Worker",
                "next_worker_id": 7552,
                "move_speed": 350,
                "stamina": 8,
                "luck": 50000,
                "icon_index": 2,
                "icon_path": "New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/Worker_Goblin01.dds",
                "base_work_speed": 60000000,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def plantworker_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_plantworker_bss(spec: Any, plantworker_result: HandlerResult) -> None:
    spec.check(plantworker_result.records)
