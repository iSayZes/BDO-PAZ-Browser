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
    case_id,
    run_case,
)

from _bss.skillexperiencemaxlevel.parser import parse_skillexperiencemaxlevel_records
from _dbss.skillexperience.parser import GUILD_SKILL_EXPERIENCE, SKILL_EXPERIENCE, LevelTable, parse_level_records


_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
_MAGIC_SIZE = 4
_TRAILER_END_AT = -8
# Each max level file and the EXP table whose top level it holds.
_TABLES: dict[str, LevelTable] = {
    "skillexperiencemaxlevel.bss": SKILL_EXPERIENCE,
    "guildskillexperiencemaxlevel.bss": GUILD_SKILL_EXPERIENCE,
}


def _array_length(source: CaseInput) -> int:
    """The u16 count between the magic and the trailer's `end_of_data`."""
    (end_of_data,) = _U32.unpack_from(source.file(None), _TRAILER_END_AT)
    return (end_of_data - _MAGIC_SIZE) // _U16.size


def _case(name: str) -> HandlerCase:
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file=None,
        uses_loc=False,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{name}",
        tests=[
            SchemaTest(required_keys=["max_level"]),
            DeclaredCountTest(declared=_array_length),
        ],
    )


CASES = {name: _case(name) for name in _TABLES}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in CASES.items() for spec in case.tests],
)
def test_skillexperiencemaxlevel_bss(name: str, spec: Any) -> None:
    _result(name).check(spec)


@pytest.mark.parametrize("name", list(_TABLES))
def test_the_max_level_is_the_top_row_of_its_exp_table(name: str) -> None:
    table = _TABLES[name]
    rows = parse_level_records(table, load_binary_fixture(table.file_name), load_binary_fixture(table.offset_file))
    assert [record["max_level"] for record in _result(name).records] == [max(row["level"] for row in rows)]


def test_a_trailer_that_misses_the_array_end_raises() -> None:
    with pytest.raises(ValueError, match="does not close"):
        parse_skillexperiencemaxlevel_records(b"PABR" + bytes(2) + _U32.pack(0) + _U32.pack(5) + _U32.pack(0), "x.bss")


def test_a_missing_magic_raises() -> None:
    with pytest.raises(ValueError, match="PABR"):
        parse_skillexperiencemaxlevel_records(bytes(18), "x.bss")
