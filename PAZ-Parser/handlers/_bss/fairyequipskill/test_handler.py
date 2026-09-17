from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CountTest,
    HandlerCase,
    HandlerResult,
    PosTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)


_ICON_DIR = "ui_texture/icon/new_icon/08_servant_skill/02_pet"

CASE = HandlerCase(
    handler_name="fairyequipskill.bss",
    data_file="fairyequipskill.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Skill Name", "Description"],
    internal_path="gamecommondata/binary/fairyequipskill.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "equip_skill_id",
                "skill_type",
                "tier",
                "padding",
                "loc_id",
                "skill_name",
                "skill_description",
                "icon_path",
            ],
        ),
        # 35 live records; the trailing 200 null placeholders must be skipped.
        CountTest(expected=35),
        RangeTest(col="skill_type", min_val=1, max_val=8),
        RangeTest(col="equip_skill_id", min_val=0, max_val=34),
        PosTest(
            pos=0,
            expected={
                "equip_skill_id": 0,
                "skill_type": 1,
                "tier": 1,
                "padding": 0,
                "loc_id": 49096,
                "skill_name": "Tingling Breath I",
                "skill_description": "Underwater Breathing +5 sec",
                "icon_path": f"{_ICON_DIR}/equipskill_fairy_00049096.dds",
            },
        ),
        PosTest(
            pos=-1,
            expected={
                "equip_skill_id": 34,
                "skill_type": 8,
                "loc_id": 49181,
                "skill_name": "Continuous Care V",
                "skill_description": "Auto-use from 30 selected items.",
            },
        ),
        # Fairy's Tear is the one group whose loc_ids descend as ids ascend.
        TargetTest(
            col="equip_skill_id",
            value=10,
            expected={
                "skill_type": 3,
                "loc_id": 49114,
                "skill_name": "Fairy's Tear I",
            },
        ),
        TargetTest(
            col="equip_skill_id",
            value=13,
            expected={
                "skill_type": 3,
                "loc_id": 49111,
                "skill_name": "Fairy's Tear IV",
            },
        ),
        # Single-record skill groups.
        TargetTest(
            col="loc_id",
            value=49120,
            expected={
                "equip_skill_id": 19,
                "skill_type": 5,
                "skill_name": "Morning Star",
            },
        ),
        TargetTest(
            col="equip_skill_id",
            value=29,
            expected={
                "skill_type": 7,
                "loc_id": 49130,
                "skill_name": "Gift",
                "skill_description": "Luck +1",
            },
        ),
        # Legacy and current naming coexist inside skill type 6.
        TargetTest(
            col="loc_id",
            value=49121,
            expected={
                "equip_skill_id": 20,
                "skill_type": 6,
                "skill_name": "Miraculous Cheer 10 Seconds",
            },
        ),
        TargetTest(
            col="loc_id",
            value=49129,
            expected={
                "equip_skill_id": 28,
                "skill_type": 6,
                "skill_name": "Miraculous Cheer V",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def fairyequipskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fairyequipskill_bss(
    spec: Any,
    fairyequipskill_result: HandlerResult,
) -> None:
    spec.check(fairyequipskill_result.records)
