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
    handler_name="petequipskill.bss",
    data_file="petequipskill.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Skill Name"],
    internal_path="gamecommondata/binary/petequipskill.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "slot",
                "section",
                "equip_skill_id",
                "skill_name",
                "icon_path",
                "skill_type",
                "tier",
                "padding",
                "loc_id",
                "extra_flag",
                "extra_value",
            ],
        ),
        CountTest(expected=116),
        PosTest(
            pos=0,
            expected={
                "slot": 0,
                "section": "S1",
                "equip_skill_id": 0,
                "skill_type": 1,
                "tier": 1,
                "padding": 0,
            },
        ),
        TargetTest(
            col="equip_skill_id",
            value=15,
            expected={
                "section": "S1",
                "skill_type": 8,
                "loc_id": 49023,
            },
        ),
        TargetTest(
            col="loc_id",
            value=49061,
            expected={
                "equip_skill_id": 15,
                "section": "S2",
                "skill_type": 4,
                "skill_name": "Skill EXP +1%",
                "icon_path": "ui_texture/icon/new_icon/08_servant_skill/02_pet/equipskill_00049061.dds",
                "extra_flag": 0,
                "extra_value": None,
            },
        ),
        TargetTest(
            col="equip_skill_id",
            value=91,
            expected={
                "section": "S2",
                "skill_type": 18,
                "loc_id": 49162,
                "skill_name": "Barter EXP +1%",
                "extra_flag": 0,
            },
        ),
        TargetTest(
            col="equip_skill_id",
            value=104,
            expected={
                "section": "S2",
                "extra_flag": 1,
                "extra_value": 1,
            },
        ),
        PosTest(
            pos=-1,
            expected={
                "section": "S2",
                "equip_skill_id": 111,
                "skill_type": 19,
                "loc_id": 49176,
                "extra_flag": 0,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def petequipskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_petequipskill_bss(
    spec: Any,
    petequipskill_result: HandlerResult,
) -> None:
    spec.check(petequipskill_result.records)
