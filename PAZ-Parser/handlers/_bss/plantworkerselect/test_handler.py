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
    handler_name="plantworkerselect.bss",
    data_file="plantworkerselect.bss",
    companion_files={"plantworker.bss": "plantworker.bss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["SelectionName", "WorkerName"],
    internal_path="gamecommondata/binary/plantworkerselect.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "group",
                "row",
                "entry_count",
                "selection_id",
                "selection_name",
                "worker_id",
                "worker_name",
                "hire_cost",
                "worker_icon_path",
                "worker_move_speed",
                "worker_stamina",
                "worker_luck",
                "worker_base_work_speed",
                "zero_a",
                "zero_b",
            ],
        ),
        CountTest(expected=372),
        PosTest(
            pos=0,
            expected={
                "group": 0,
                "row": 0,
                "entry_count": 13,
                "selection_id": 77,
                "selection_name": "Calpheon City",
                "worker_id": 7501,
                "worker_name": "Naive Worker",
                "hire_cost": 1500,
                "worker_icon_path": "New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/Worker_Giant01.dds",
                "worker_move_speed": 150,
                "worker_stamina": 10,
                "worker_luck": 0,
                "worker_base_work_speed": 25000000,
            },
        ),
        TargetTest(
            col="worker_id",
            value=7571,
            expected={
                "group": 0,
                "selection_id": 77,
                "selection_name": "Calpheon City",
                "worker_name": "Artisan Giant Worker",
                "hire_cost": 90000,
                "worker_icon_path": "New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/Worker_Giant04.dds",
            },
        ),
        PosTest(
            pos=230,
            expected={
                "group": 18,
                "row": 1,
                "entry_count": 8,
                "selection_id": 735,
                "selection_name": "Grána",
                "worker_id": 8001,
                "worker_name": "Papu Worker",
                "hire_cost": 3500,
                "worker_icon_path": "New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/Worker_Papu01.dds",
            },
        ),
        TargetTest(
            col="worker_id",
            value=8020,
            expected={
                "group": 20,
                "entry_count": 12,
                "selection_id": 955,
                "selection_name": "O'draxxia",
                "worker_name": "Dwarf Worker",
                "hire_cost": 3500,
                "worker_icon_path": "New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/Worker_Odilita_Dwarf01.dds",
            },
        ),
        TargetTest(
            col="worker_id",
            value=8047,
            expected={
                "group": 21,
                "entry_count": 12,
                "selection_id": 1444,
                "selection_name": "Bukpo",
                "worker_name": "Dokkebi Worker",
                "hire_cost": 3500,
                "worker_icon_path": "New_UI_Common_forLua/Widget/WorldMap/WorkerIcon/Morning_Dokev01.dds",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def plantworkerselect_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_plantworkerselect_bss(
    spec: Any,
    plantworkerselect_result: HandlerResult,
) -> None:
    spec.check(plantworkerselect_result.records)
