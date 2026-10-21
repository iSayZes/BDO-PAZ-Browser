from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from _bss.petequipskill.parser import parse_petequipskill_records
from _dbss.pet.joins import SKILL_CATALOG_FILE
from _dbss.pet.parser import parse_pet_records
from .parser import FILE_NAME, SECTION_LEADER_SKILL, SECTION_RESULT, parse_petupgraderesult_records


_COUNT_SIZE = 4
_RESULT_SIZE = 10
# pet.dbss stores tiers from 0: Tier 4 is 3, Tier 5 is 4.
_TIER_4 = 3
_TIER_5 = 4


def _declared_rows(source: CaseInput) -> int:
    """Both counts: the Result count at +0x00 and the Leader Skill count after its rows."""
    raw = source.file(None)
    result_count = struct.unpack_from("<I", raw, 0)[0]
    leader_count_at = _COUNT_SIZE + result_count * _RESULT_SIZE
    return result_count + struct.unpack_from("<I", raw, leader_count_at)[0]


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={SKILL_CATALOG_FILE: SKILL_CATALOG_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["leader_base_skill_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "section",
                "pet_id",
                "pet_id_dup",
                "result_pet_id",
                "leader_base_skill_id",
                "pet_name",
                "result_pet_name",
                "leader_base_skill_name",
            ]
        ),
        DeclaredCountTest(declared=_declared_rows),
        RangeTest(col="section", min_val=SECTION_RESULT, max_val=SECTION_LEADER_SKILL),
        UserLanguageTest(fields=["leader_base_skill_name"]),
    ],
)


@pytest.fixture(scope="module")
def upgrade_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_petupgraderesult_bss(spec: Any, upgrade_result: HandlerResult) -> None:
    upgrade_result.check(spec)


def _rows(section: int) -> list[dict]:
    return [r for r in parse_petupgraderesult_records(load_binary_fixture(FILE_NAME)) if r["section"] == section]


def test_results_train_a_tier_4_pet_into_a_tier_5_pet() -> None:
    pets = parse_pet_records(load_binary_fixture("pet.dbss"), load_binary_fixture("petoffset.dbss"))
    tiers = {pet["pet_id"]: pet["tier"] for pet in pets}
    for record in _rows(SECTION_RESULT):
        assert record["pet_id_dup"] == record["pet_id"], record
        assert tiers.get(record["pet_id"]) == _TIER_4, record
        assert tiers.get(record["result_pet_id"]) == _TIER_5, record


def test_leader_skill_rows_repeat_each_result_talent() -> None:
    """Each Leader Skill key is one result pet, with that Result row's talent."""
    by_result_pet = {r["result_pet_id"]: r["leader_base_skill_id"] for r in _rows(SECTION_RESULT)}
    leader_skills = {r["pet_id"]: r["leader_base_skill_id"] for r in _rows(SECTION_LEADER_SKILL)}
    assert leader_skills == by_result_pet


def test_talents_are_section_2_skills() -> None:
    catalog = parse_petequipskill_records(load_binary_fixture(SKILL_CATALOG_FILE))
    base_skill_ids = {r["equip_skill_id"] for r in catalog if r["section"] == "S2"}
    for record in parse_petupgraderesult_records(load_binary_fixture(FILE_NAME)):
        assert record["leader_base_skill_id"] in base_skill_ids, record


def test_parser_reads_both_maps_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<I3HI", 1, 9479, 9479, 56274, 100) + struct.pack("<IHI", 1, 56274, 100)
    assert parse_petupgraderesult_records(data) == [
        {"section": 1, "pet_id": 9479, "pet_id_dup": 9479, "result_pet_id": 56274, "leader_base_skill_id": 100},
        {"section": 2, "pet_id": 56274, "pet_id_dup": None, "result_pet_id": None, "leader_base_skill_id": 100},
    ]
    with pytest.raises(ValueError):
        parse_petupgraderesult_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_petupgraderesult_records(data[:-1])
