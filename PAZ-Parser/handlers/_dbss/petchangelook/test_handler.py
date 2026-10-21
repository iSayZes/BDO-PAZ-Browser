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
    SchemaTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _dbss.pet.joins import PET_FILE, PET_OFFSET_FILE
from _dbss.pet.parser import parse_pet_records
from .parser import (
    FILE_NAME,
    KEY_PREFIX_SIZE,
    OFFSET_FILE,
    parse_petchangelook_records,
    parse_petchangelookoffset_records,
)


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 10


def _declared_looks(source: CaseInput) -> int:
    """The look count of every record, summed over the offset table's records."""
    data = source.file(None)
    rows = parse_petchangelookoffset_records(source.file(OFFSET_FILE))
    # The payload opens with the u16 look key, then the u32 look count.
    return sum(struct.unpack_from("<I", data, row["offset"] + 2)[0] for row in rows)


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={PET_FILE: PET_FILE, PET_OFFSET_FILE: PET_OFFSET_FILE, OFFSET_FILE: OFFSET_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "change_look_key",
                "look_count",
                "look_index",
                "action_index",
                "icon_path",
                "icon_path_1",
                "icon_path_2",
                "skill_level",
                "skill_no",
                "unknown_icon_path_2_04",
                "skin_name_kr",
                "unknown_skin_name_kr_00",
                "unknown_skin_name_kr_01",
                "pet_names",
                "skill_name",
            ]
        ),
        DeclaredCountTest(declared=_declared_looks),
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
        SchemaTest(required_keys=["change_look_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)

_CASES = {case.handler_name: case for case in (CASE, OFFSET_CASE)}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(_CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in _CASES.items() for spec in case.tests],
)
def test_pet_change_look_tables(name: str, spec: Any) -> None:
    _result(name).check(spec)


def _looks() -> list[dict]:
    return parse_petchangelook_records(load_binary_fixture(FILE_NAME))


def test_offset_rows_cover_every_record() -> None:
    """The index has one row per look key, and the rows tile the main file after the count."""
    data = load_binary_fixture(FILE_NAME)
    rows = sorted(parse_petchangelookoffset_records(load_binary_fixture(OFFSET_FILE)), key=lambda row: row["offset"])
    assert len(rows) == struct.unpack_from("<I", data, 0)[0]
    position = _COUNT_SIZE
    for row in rows:
        assert struct.unpack_from("<H", data, position)[0] == row["change_look_key"], row
        assert row["offset"] == position + KEY_PREFIX_SIZE, row
        position = row["offset"] + row["size"]
    assert position == len(data)


def test_look_keys_match_the_offset_table() -> None:
    keys = {look["change_look_key"] for look in _looks()}
    rows = parse_petchangelookoffset_records(load_binary_fixture(OFFSET_FILE))
    assert keys == {row["change_look_key"] for row in rows}


def test_pet_look_keys_have_looks() -> None:
    """Most change_look_keys of pet.dbss have a row here (a patch may leave a few out)."""
    keys = {look["change_look_key"] for look in _looks()}
    pets = parse_pet_records(load_binary_fixture(PET_FILE), load_binary_fixture(PET_OFFSET_FILE))
    pet_keys = {pet["change_look_key"] for pet in pets if pet["change_look_key"]}
    assert len(pet_keys & keys) > len(pet_keys) // 2


def test_a_skill_has_a_level() -> None:
    """A look with a skill stores the gc::SkillKey level next to it; one without stores zeros."""
    for look in _looks():
        assert bool(look["skill_no"]) == bool(look["skill_level"]), look


def test_parser_reads_a_look_and_rejects_extra_or_missing_bytes() -> None:
    def text(value: str, *, wide: bool = False) -> bytes:
        raw = value.encode("utf-16-le" if wide else "ascii")
        return struct.pack("<Q", len(value)) + raw

    look = struct.pack("<I", 6) + text("a.dds") + text("b.dds") + text("c.dds")
    look += struct.pack("<HHB", 1, 49166, 1) + text("요정", wide=True) + struct.pack("<B3s", 0, b"cO7")
    data = struct.pack("<IHHI", 1, 25001, 25001, 1) + look
    assert parse_petchangelook_records(data) == [
        {
            "change_look_key": 25001,
            "look_count": 1,
            "look_index": 0,
            "action_index": 6,
            "icon_path": "a.dds",
            "icon_path_1": "b.dds",
            "icon_path_2": "c.dds",
            "skill_level": 1,
            "skill_no": 49166,
            "unknown_icon_path_2_04": 1,
            "skin_name_kr": "요정",
            "unknown_skin_name_kr_00": 0,
            "unknown_skin_name_kr_01": "63 4f 37",
        }
    ]
    with pytest.raises(ValueError):
        parse_petchangelook_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_petchangelook_records(data[:-1])
