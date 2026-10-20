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
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _bss.petleaderbuff.parser import parse_petleaderbuff_records
from _dbss.pet.parser import parse_pet_records


# Stored pet tier of Tier 5, the tier an alpha pet has (petleaderbuff_bss.md).
_TIER_5 = 4
# A cooldown cut on the 1,000,000 = 100% scale.
_FULL_RATE = 1_000_000


CASE = HandlerCase(
    handler_name="petleaderbuff.bss",
    data_file="petleaderbuff.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petleaderbuff.bss",
    tests=[
        SchemaTest(required_keys=["pet_tier", "unknown_01", "leader_buff_rate"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="leader_buff_rate", min_val=0, max_val=_FULL_RATE),
        TargetTest(col="pet_tier", value=_TIER_5, expected={"pet_tier": _TIER_5}),
    ],
)


@pytest.fixture(scope="module")
def petleaderbuff_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_petleaderbuff_bss(spec: Any, petleaderbuff_result: HandlerResult) -> None:
    petleaderbuff_result.check(spec)


def test_every_pet_tier_is_a_pet_dbss_tier(petleaderbuff_result: HandlerResult) -> None:
    pets = parse_pet_records(load_binary_fixture("pet.dbss"), load_binary_fixture("petoffset.dbss"))
    pet_tiers = {pet["tier"] for pet in pets}
    assert {record["pet_tier"] for record in petleaderbuff_result.records} <= pet_tiers


def test_entries_that_do_not_fill_the_file_raise() -> None:
    data = struct.pack("<I", 2) + struct.pack("<BBI", _TIER_5, _TIER_5, 150_000)
    with pytest.raises(ValueError, match="2 entries need 16 bytes"):
        parse_petleaderbuff_records(data)


def test_a_file_shorter_than_the_count_raises() -> None:
    with pytest.raises(ValueError, match="too short"):
        parse_petleaderbuff_records(b"\x01\x00")
