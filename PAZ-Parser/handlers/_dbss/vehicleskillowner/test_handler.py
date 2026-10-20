from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_pabr_offset_rows
from _dbss.vehicleskill.parser import vehicle_skill_names_kr
from _dbss.vehicleskillowner.parser import parse_vehicleskillowner_records


_OFFSET_FILE = "vehicleskillowneroffset.dbss"
# An offset row's size starts at `character_id_dup`: u16 dup, u32 rate, u32 skill_count.
_SIZED_HEAD = 10
_SKILL_SIZE = 16


def _table_rows(source: CaseInput) -> int:
    """Rows the offset table declares: one per skill, one for a servant with none."""
    total = 0
    for row in parse_pabr_offset_rows(source.file(_OFFSET_FILE)):
        body = row.size - _SIZED_HEAD
        if body < 0 or body % _SKILL_SIZE:
            raise AssertionError(f"servant {row.entry_id} is {row.size} bytes, not whole {_SKILL_SIZE}-byte skills")
        total += max(1, body // _SKILL_SIZE)
    return total


CASE = HandlerCase(
    handler_name="vehicleskillowner.dbss",
    data_file="vehicleskillowner.dbss",
    companion_files={
        _OFFSET_FILE: _OFFSET_FILE,
        "characterstaticoffset.dbss": "characterstaticoffset.dbss",
        "vehicleskill.dbss": "vehicleskill.dbss",
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "skill_name"],
    internal_path="gamecommondata/binary/vehicleskillowner.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "character_id",
                "name",
                "cant_learnable_rate",
                "has_character_row",
                "skill_key",
                "skill_name",
                "able",
                "add_exp",
                "is_learn",
                "unknown_0d",
                "unknown_0e",
            ]
        ),
        DeclaredCountTest(declared=_table_rows),
        RangeTest(col="is_learn", min_val=0, max_val=1),
        UserLanguageTest(fields=["skill_name"]),
        # The tier 8 mare checked in the Horse Growth Info window (vehicleskillowner_dbss.md).
        TargetTest(col="character_id", value=9890, expected={"skill_key": 1, "skill_name": "Hind Kick"}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["character_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=4)),
    ],
)


@pytest.fixture(scope="module")
def owner_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_vehicleskillowner_dbss(spec: Any, owner_result: HandlerResult) -> None:
    owner_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_vehicleskillowneroffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_offset_rows_point_at_each_servant(owner_result: HandlerResult) -> None:
    # Checks the index: every servant once, each row starting 2 bytes into its record.
    source = owner_result.source
    rows = parse_pabr_offset_rows(source.file(_OFFSET_FILE))
    servants = parse_vehicleskillowner_records(source.data)
    assert sorted(row.entry_id for row in rows) == sorted(servant["character_id"] for servant in servants)
    for row in rows:
        assert int.from_bytes(source.data[row.offset : row.offset + 2], "little") == row.entry_id, row


def test_every_skill_key_is_a_vehicle_skill(owner_result: HandlerResult) -> None:
    # Checks skill_key against its target table: every key is a vehicleskill.dbss key.
    skill_keys = set(vehicle_skill_names_kr(owner_result.source.file("vehicleskill.dbss")))
    used = {r["skill_key"] for r in owner_result.records if r["skill_key"] is not None}
    assert used <= skill_keys, used - skill_keys


def test_skills_are_in_key_order(owner_result: HandlerResult) -> None:
    for servant in parse_vehicleskillowner_records(owner_result.source.data):
        keys = [skill["skill_key"] for skill in servant["skills"]]
        assert keys == sorted(keys), servant["character_id"]


def test_repeated_character_id_must_match() -> None:
    # count 1, character 1 repeated as 2, rate 0, no skills.
    data = (1).to_bytes(4, "little") + b"\x01\x00\x02\x00" + bytes(8)
    with pytest.raises(ValueError, match="repeats character 2, expected 1"):
        parse_vehicleskillowner_records(data)
