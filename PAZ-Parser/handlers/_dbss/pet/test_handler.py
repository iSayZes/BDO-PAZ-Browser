from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


PET_CASE = HandlerCase(
    handler_name="pet.dbss",
    data_file="pet.dbss",
    companion_files={"petoffset.dbss": "petoffset.dbss", "petgrade.dbss": "petgrade.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["pet_name", "display_name"],
    internal_path="gamecommondata/binary/pet.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "pet_id",
                "variant",
                "species",
                "grade",
                "max_level",
                "equip_skill_slots",
                "acquire_type_id",
                "equip_skill_id",
                "icon_path",
                "grade_count",
                "pet_id_match",
            ]
        ),
        CountTest(expected=1782),
        PosTest(
            pos=0,
            expected={
                "pet_id": 9101,
                "pet_name": "Cat",
                "display_name": "Cat",
                "variant": 2,
                "species": 1,
                "grade": 1,
                "max_level": 10,
                "equip_skill_slots": 2,
                "acquire_type_id": 0,
                "equip_skill_id": 21,
                "grade_count": 1,
                "icon_path": "New_UI_Common_forLua\\Window\\Stable\\Pet\\Pet_Cat_0991.dds",
                "pet_id_match": True,
            },
        ),
        TargetTest(
            col="pet_id",
            value=64517,
            expected={
                "pet_name": "Golden Star",
                "display_name": "Golden Star",
                "variant": 1,
                "grade": 4,
                "acquire_type_id": 304,
                "equip_skill_id": 78,
                "grade_count": 2,
                "icon_path": "New_UI_Common_forLua\\Window\\Stable\\Pet\\GoldStar_Pet_0004.dds",
            },
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="petoffset.dbss",
    data_file="petoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petoffset.dbss",
    tests=[
        SchemaTest(required_keys=["pet_id", "data_offset", "data_size"]),
        CountTest(expected=1782),
        PosTest(pos=0, expected={"pet_id": 56325, "data_offset": 45819, "data_size": 181}),
        PosTest(pos=-1, expected={"pet_id": 9501, "data_offset": 330592, "data_size": 181}),
    ],
)

GRADE_CASE = HandlerCase(
    handler_name="petgrade.dbss",
    data_file="petgrade.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petgrade.dbss",
    tests=[
        SchemaTest(required_keys=["variant", "species", "grade_count"]),
        CountTest(expected=203),
        PosTest(pos=0, expected={"key": 15878, "variant": 6, "species": 62, "grade_count": 2}),
        PosTest(pos=-1, expected={"key": 16641, "variant": 1, "species": 65, "grade_count": 2}),
    ],
)


@pytest.fixture(scope="module")
def pet_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PET_RESULT", None)
    if result is None:
        result = run_case(replace(PET_CASE, tests=[]))
        request.module._PET_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.fixture(scope="module")
def grade_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_GRADE_RESULT", None)
    if result is None:
        result = run_case(replace(GRADE_CASE, tests=[]))
        request.module._GRADE_RESULT = result
    return result


@pytest.mark.parametrize("spec", PET_CASE.tests, ids=case_id)
def test_pet_dbss(spec: Any, pet_result: HandlerResult) -> None:
    spec.check(pet_result.records)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_petoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    spec.check(offset_result.records)


@pytest.mark.parametrize("spec", GRADE_CASE.tests, ids=case_id)
def test_petgrade_dbss(spec: Any, grade_result: HandlerResult) -> None:
    spec.check(grade_result.records)
