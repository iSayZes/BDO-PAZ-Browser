from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)


# The file declares no row count. Every record sits at the slot equal to its
# `equip_skill_id`, which checks both walks find their ends and stay aligned.
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
                "unknown_08",
                "unknown_09",
                "loc_id",
                "unknown_0c",
                "unknown_10",
            ],
        ),
        RangeTest(col="unknown_09", min_val=0, max_val=0),
        RangeTest(col="unknown_0c", min_val=0, max_val=1),
        TargetTest(
            col="loc_id",
            value=49023,
            expected={"equip_skill_id": 15, "section": "S1", "slot": 15, "skill_type": 8},
        ),
        TargetTest(
            col="loc_id",
            value=49061,
            expected={
                "equip_skill_id": 15,
                "section": "S2",
                "slot": 15,
                "skill_type": 4,
                "skill_name": "Skill EXP +1%",
                "icon_path": "ui_texture/icon/new_icon/08_servant_skill/02_pet/equipskill_00049061.dds",
            },
        ),
        # Follows equip_skill_id 65, which carries the extra u32.
        TargetTest(
            col="loc_id",
            value=49047,
            expected={"equip_skill_id": 66, "section": "S2", "slot": 66},
        ),
        TargetTest(
            col="loc_id",
            value=49162,
            expected={
                "equip_skill_id": 91,
                "section": "S2",
                "slot": 91,
                "skill_type": 18,
                "skill_name": "Barter EXP +1%",
            },
        ),
        TargetTest(
            col="loc_id",
            value=49176,
            expected={"equip_skill_id": 111, "section": "S2", "slot": 111, "skill_type": 19},
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
    petequipskill_result.check(spec)


def test_every_record_sits_at_its_own_slot(petequipskill_result: HandlerResult) -> None:
    misplaced = [
        (record["section"], record["slot"], record["equip_skill_id"])
        for record in petequipskill_result.records
        if record["slot"] != record["equip_skill_id"]
    ]

    assert misplaced == []


def test_both_sections_are_present(petequipskill_result: HandlerResult) -> None:
    assert {record["section"] for record in petequipskill_result.records} == {"S1", "S2"}
