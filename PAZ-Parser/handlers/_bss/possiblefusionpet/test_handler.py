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
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _dbss.pet.joins import pet_fusion_key
from _dbss.pet.parser import parse_pet_records
from .parser import FILE_NAME, parse_possiblefusionpet_records


_COUNT_SIZE = 4
_ROW_SIZE = 6

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["variant", "species", "unknown_02", "tier", "pet_id", "fusion_key", "pet_name"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def possible_fusion_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_possiblefusionpet_bss(spec: Any, possible_fusion_result: HandlerResult) -> None:
    possible_fusion_result.check(spec)


def test_each_row_holds_its_pets_fusion_key() -> None:
    """The four key bytes of a row are the fusion key of its pet in pet.dbss."""
    pets = parse_pet_records(load_binary_fixture("pet.dbss"), load_binary_fixture("petoffset.dbss"))
    keys = {pet["pet_id"]: pet_fusion_key(pet) for pet in pets}
    for record in parse_possiblefusionpet_records(load_binary_fixture(FILE_NAME)):
        assert keys.get(record["pet_id"]) == record["fusion_key"], record


def test_rows_are_sorted_by_fusion_key() -> None:
    keys = [r["fusion_key"] for r in parse_possiblefusionpet_records(load_binary_fixture(FILE_NAME))]
    assert keys == sorted(keys)


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<I4BH", 1, 1, 40, 0, 2, 9711)
    assert parse_possiblefusionpet_records(data) == [
        {"variant": 1, "species": 40, "unknown_02": 0, "tier": 2, "pet_id": 9711, "fusion_key": 0x02002801}
    ]
    with pytest.raises(ValueError):
        parse_possiblefusionpet_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_possiblefusionpet_records(data[:-1])
