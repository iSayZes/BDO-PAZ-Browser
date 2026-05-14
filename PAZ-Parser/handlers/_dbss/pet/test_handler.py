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
                "tier",
                "grade",
                "grade_name",
                "max_level",
                "equip_skill_slots",
                "acquire_type_id",
                "equip_skill_id",
                "icon_path",
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
                "tier": 1,
                "grade": 1,
                "grade_name": "Classic",
                "max_level": 10,
                "equip_skill_slots": 2,
                "acquire_type_id": 0,
                "equip_skill_id": 21,
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
                "tier": 4,
                "acquire_type_id": 304,
                "equip_skill_id": 78,
                "grade": 2,
                "grade_name": "Rare",
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
    companion_files={"petgradeoffset.dbss": "petgradeoffset.dbss"},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petgrade.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "variant",
                "species",
                "grade",
                "grade_name",
                "data_offset",
                "data_size",
                "key_match",
            ]
        ),
        CountTest(expected=203),
        PosTest(
            pos=0,
            expected={
                "key": 262,
                "variant": 6,
                "species": 1,
                "grade": 3,
                "grade_name": "Premium",
                "data_offset": 2012,
                "data_size": 8,
                "key_match": True,
            },
        ),
        TargetTest(
            col="key",
            value=15878,
            expected={
                "variant": 6,
                "species": 62,
                "grade": 2,
                "grade_name": "Rare",
                "data_offset": 8,
                "data_size": 8,
            },
        ),
    ],
)

GRADE_OFFSET_CASE = HandlerCase(
    handler_name="petgradeoffset.dbss",
    data_file="petgradeoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petgradeoffset.dbss",
    tests=[
        SchemaTest(required_keys=["key", "variant", "species", "data_offset", "data_size"]),
        CountTest(expected=203),
        PosTest(pos=0, expected={"key": 262, "variant": 6, "species": 1, "data_offset": 2012, "data_size": 8}),
        PosTest(pos=-1, expected={"key": 9744, "variant": 16, "species": 38, "data_offset": 1064, "data_size": 8}),
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


@pytest.fixture(scope="module")
def grade_offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_GRADE_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(GRADE_OFFSET_CASE, tests=[]))
        request.module._GRADE_OFFSET_RESULT = result
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


@pytest.mark.parametrize("spec", GRADE_OFFSET_CASE.tests, ids=case_id)
def test_petgradeoffset_dbss(spec: Any, grade_offset_result: HandlerResult) -> None:
    spec.check(grade_offset_result.records)
