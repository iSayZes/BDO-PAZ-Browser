from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.skillawakeningability.parser import FILE_NAME as ABILITY_FILE, parse_skillawakeningability_records
from .parser import FILE_NAME, parse_skillawakeningability2_records


# Charging Thrust, a Warrior skill with Skill Add-on options since client 1784.
_CHARGING_THRUST = 1022

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={ABILITY_FILE: ABILITY_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill", "add_ons"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["skill_no", "skill_no_dup", "ability_count", "ability_indexes", "skill", "add_ons"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="skill_no", value=_CHARGING_THRUST, expected={"skill_no_dup": _CHARGING_THRUST}),
        UserLanguageTest(fields=["skill", "add_ons"]),
    ],
)


@pytest.fixture(scope="module")
def add_on_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skillawakeningability2_bss(spec: Any, add_on_result: HandlerResult) -> None:
    add_on_result.check(spec)


def test_skill_no_dup_repeats_the_key(add_on_result: HandlerResult) -> None:
    mismatched = [r["skill_no"] for r in add_on_result.records if r["skill_no_dup"] != r["skill_no"]]
    assert not mismatched, mismatched


def test_skill_numbers_are_unique(add_on_result: HandlerResult) -> None:
    skill_nos = [r["skill_no"] for r in add_on_result.records]
    assert len(skill_nos) == len(set(skill_nos))


def test_every_row_names_a_skill(add_on_result: HandlerResult) -> None:
    unnamed = [r["skill_no"] for r in add_on_result.records if not r["skill"]]
    assert not unnamed, unnamed


def test_every_option_is_an_ability_index() -> None:
    abilities = {r["ability_index"] for r in parse_skillawakeningability_records(load_binary_fixture(ABILITY_FILE))}
    missing = [
        (record["skill_no"], index)
        for record in parse_skillawakeningability2_records(load_binary_fixture(FILE_NAME))
        for index in record["ability_indexes"]
        if index not in abilities
    ]
    assert not missing, missing[:10]


def test_parse_reads_the_u64_count_before_the_list() -> None:
    body = struct.pack("<I", 1) + struct.pack("<HHQ3I", 700, 700, 3, 2, 5, 8)
    data = b"PABR" + body + struct.pack("<III", 0, 4 + len(body), 0)

    (record,) = parse_skillawakeningability2_records(data)

    assert record == {"skill_no": 700, "skill_no_dup": 700, "ability_count": 3, "ability_indexes": [2, 5, 8]}


def test_parse_rejects_rows_that_miss_the_string_table() -> None:
    body = struct.pack("<I", 1) + struct.pack("<HHQI", 700, 700, 1, 2)
    data = b"PABR" + body + struct.pack("<I", 0) + struct.pack("<III", 0, 8 + len(body), 0)

    with pytest.raises(ValueError):
        parse_skillawakeningability2_records(data)
