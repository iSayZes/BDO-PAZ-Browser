from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _bss.houseinfo.parser import FILE_NAME as HOUSEINFO_FILE
from _common.pabr_offset import parse_bare_offset_rows
from _common.pabr_strings import HEADER_SIZE as PABR_HEADER_SIZE
from _dbss.guildhouseinfo.house_rows import GUILDHOUSEINFO_PATH, HOUSEINFO_PATH
from _dbss.guildhouseinfo.parser import FILE_NAME as GUILDHOUSEINFO_FILE
from .parser import FILE_NAME, OFFSET_FILE, parse_innstaticstatus_records, parse_innstaticstatusoffset_rows


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10
# The index points past the u16 inn key, at the room count.
_KEY_SIZE = 2
_ROOM_KEY_SIZE = 2
_HOUSEHOLD_LIST = "householdlist.bss"
# Velia 3-2, 2F (a node house) and Velia Guild House.
_VELIA_2F = 2109
_VELIA_GUILD_HOUSE = 2110


def _declared_rooms(source: CaseInput) -> int:
    """The rooms the index sizes declare: each row is the u32 room count and 2 bytes per room."""
    rows = parse_bare_offset_rows(source.file(OFFSET_FILE))
    return sum((row.size - _COUNT_SIZE) // _ROOM_KEY_SIZE for row in rows)


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={HOUSEINFO_FILE: HOUSEINFO_FILE, GUILDHOUSEINFO_FILE: GUILDHOUSEINFO_FILE, OFFSET_FILE: OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "town"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["inn_key", "room_index", "character_key", "name", "house_path", "town"]),
        DeclaredCountTest(declared=_declared_rooms),
        TargetTest(col="character_key", value=_VELIA_2F, expected={"house_path": HOUSEINFO_PATH, "town": "Velia"}),
        TargetTest(
            col="character_key",
            value=_VELIA_GUILD_HOUSE,
            expected={"name": "Velia Guild House", "house_path": GUILDHOUSEINFO_PATH, "town": "Velia"},
        ),
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
        SchemaTest(required_keys=["inn_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def inn_result(request: Any) -> HandlerResult:
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
def test_innstaticstatus_dbss(spec: Any, inn_result: HandlerResult) -> None:
    inn_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_innstaticstatusoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_the_rows_count_their_inns() -> None:
    data = load_binary_fixture(FILE_NAME)
    assert len(parse_innstaticstatus_records(data)) == struct.unpack_from("<I", data, 0)[0]


def test_the_rooms_are_the_house_characters_of_householdlist() -> None:
    """The inns' rooms and householdlist.bss hold the same house keys, each once."""
    household = load_binary_fixture(_HOUSEHOLD_LIST)
    (count,) = struct.unpack_from("<I", household, len(b"PABR"))
    houses = struct.unpack_from(f"<{count}H", household, PABR_HEADER_SIZE)
    rooms = [key for inn in parse_innstaticstatus_records(load_binary_fixture(FILE_NAME)) for key in inn["room_keys"]]

    assert len(rooms) == len(set(rooms))
    assert set(rooms) == set(houses)


def test_offset_rows_point_at_their_rows() -> None:
    rows = parse_innstaticstatusoffset_rows(load_binary_fixture(OFFSET_FILE))
    problems = offset_row_problems(load_binary_fixture(FILE_NAME), rows, struct.Struct("<H"), lead=_KEY_SIZE)
    assert not problems, problems


def test_parse_reads_each_inn_with_its_rooms() -> None:
    data = struct.pack("<I", 2) + struct.pack("<HI2H", 1, 2, 3121, 2410) + struct.pack("<HI", 2, 0)

    assert parse_innstaticstatus_records(data) == [
        {"inn_key": 1, "room_keys": [3121, 2410]},
        {"inn_key": 2, "room_keys": []},
    ]


def test_parse_rejects_a_room_list_past_the_file() -> None:
    with pytest.raises(ValueError):
        parse_innstaticstatus_records(struct.pack("<I", 1) + struct.pack("<HI", 1, 5) + struct.pack("<H", 3121))
