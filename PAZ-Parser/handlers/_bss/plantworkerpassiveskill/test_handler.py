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
    handler_name="plantworkerpassiveskill.bss",
    data_file="plantworkerpassiveskill.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Description"],
    internal_path="gamecommondata/binary/plantworkerpassiveskill.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "slot",
                "skill_id",
                "duplicate_skill_id",
                "inline_name",
                "display_name",
                "icon_path",
                "inline_description",
                "display_description",
                "acquisition_weight",
                "effect_type",
                "apply_mode",
                "apply_scope",
                "effect_type_copy",
                "effect_target",
                "effect_value_a",
                "effect_value_b",
                "extra_effect_value_a",
                "extra_effect_value_b",
            ],
        ),
        CountTest(expected=72),
        PosTest(
            pos=0,
            expected={
                "skill_id": 1603,
                "duplicate_skill_id": 1603,
                "display_name": "Wings C",
                "icon_path": "/New_UI_Common_forLua/Skill/WorkerSkill/1303.dds",
                "display_description": "Movement Speed +6%",
                "acquisition_weight": 1000,
                "effect_type": 0,
                "effect_target": 0,
                "effect_value_a": 60000,
                "effect_value_b": 0,
            },
        ),
        TargetTest(
            col="skill_id",
            value=1923,
            expected={
                "display_name": "Adv. Siege Weapon Production",
                "icon_path": "/New_UI_Common_forLua/Skill/WorkerSkill/1923.dds",
                "display_description": "Extra Work (+3) Done for Siege Weapons",
                "acquisition_weight": 2500,
                "effect_type": 6,
                "effect_type_copy": 6,
                "effect_target": 5004,
                "effect_value_a": 3,
                "effect_value_b": 0,
            },
        ),
        TargetTest(
            col="skill_id",
            value=1203,
            expected={
                "display_name": "Thrifty C",
                "display_description": "5% Chance to Return 10% of 1 Crafting Material",
                "acquisition_weight": 1000,
                "effect_type": 1,
                "effect_target": 50000,
                "effect_value_a": 100000,
                "effect_value_b": 100000,
            },
        ),
        TargetTest(
            col="skill_id",
            value=1012,
            expected={
                "display_name": "Adept Worker",
                "display_description": "Work Speed +2, Movement Speed +7%",
                "effect_type": 0,
                "apply_mode": 0,
                "effect_target": 0,
                "effect_value_a": 70000,
                "effect_value_b": 0,
                "extra_zero_a": 0,
                "extra_effect_value_a": 2000000,
                "extra_effect_value_b": 1,
                "extra_zero_b": 0,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def plantworkerpassiveskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_plantworkerpassiveskill_bss(
    spec: Any,
    plantworkerpassiveskill_result: HandlerResult,
) -> None:
    spec.check(plantworkerpassiveskill_result.records)
