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
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _common.equipskill_roll import read_skill_nos
from _common.pabr_offset import parse_bare_offset_rows
from _dbss.pet.parser import parse_pet_records
from .parser import FILE_NAME, OFFSET_FILE, SKILL_FIELDS, parse_petpcroom_records


_COUNT_SIZE = 4
_ROW_SIZE = 14
_CATALOG_FILE = "petequipskill.bss"


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={_CATALOG_FILE: _CATALOG_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["pet_id", *SKILL_FIELDS, "pet_name", "skill_name_0", "skill_name_1", "skill_name_2"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["pet_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="size", min_val=_ROW_SIZE, max_val=_ROW_SIZE),
    ],
)


@pytest.fixture(scope="module")
def pet_pc_room_result(request: Any) -> HandlerResult:
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
def test_petpcroom_dbss(spec: Any, pet_pc_room_result: HandlerResult) -> None:
    pet_pc_room_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_petpcroomoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_pet_ids_are_unique(pet_pc_room_result: HandlerResult) -> None:
    pet_ids = [r["pet_id"] for r in pet_pc_room_result.records]
    assert len(pet_ids) == len(set(pet_ids))


def test_offset_rows_point_at_each_row() -> None:
    """Each index row starts at its row's own pet_id and covers the whole row."""
    records = parse_petpcroom_records(load_binary_fixture(FILE_NAME))
    expected = {r["pet_id"]: (_COUNT_SIZE + index * _ROW_SIZE, _ROW_SIZE) for index, r in enumerate(records)}
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_every_pet_id_is_a_pc_room_pet() -> None:
    """Each row keys a pet.dbss record whose pc_room_type is set."""
    pets = parse_pet_records(load_binary_fixture("pet.dbss"), load_binary_fixture("petoffset.dbss"))
    pc_room_types = {pet["pet_id"]: pet["pc_room_type"] for pet in pets}
    for record in parse_petpcroom_records(load_binary_fixture(FILE_NAME)):
        assert pc_room_types.get(record["pet_id"]) == 1, record["pet_id"]


def test_every_equip_skill_id_is_in_the_catalog() -> None:
    """Each equip_skill_id_* is a Section 1 equip_skill_id of petequipskill.bss."""
    catalog_ids = set(read_skill_nos(load_binary_fixture(_CATALOG_FILE)))
    for record in parse_petpcroom_records(load_binary_fixture(FILE_NAME)):
        assert {record[field] for field in SKILL_FIELDS} <= catalog_ids, record["pet_id"]


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    data = struct.pack("<IH3I", 1, 55663, 4, 41, 9)
    assert parse_petpcroom_records(data) == [
        {"pet_id": 55663, "equip_skill_id_0": 4, "equip_skill_id_1": 41, "equip_skill_id_2": 9}
    ]
    with pytest.raises(ValueError):
        parse_petpcroom_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_petpcroom_records(data[:-1])
