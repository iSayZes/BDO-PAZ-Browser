from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.skillexperience.parser import (
    GUILD_SKILL_EXPERIENCE,
    LEVEL_TABLES,
    PRODUCT_EXPERIENCE,
    SKILL_EXPERIENCE,
    LevelTable,
    parse_level_offset_records,
    parse_level_records,
)


_U32 = struct.Struct("<I")


def _table_case(table: LevelTable) -> HandlerCase:
    exp_tests = [RangeTest(col="exp", min_val=0, max_val=2**64 - 1)] if "exp" in table.fields else []
    return HandlerCase(
        handler_name=table.file_name,
        data_file=table.file_name,
        companion_files={table.offset_file: table.offset_file},
        loc_file=None,
        uses_loc=False,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{table.file_name}",
        tests=[
            SchemaTest(required_keys=["level", *table.fields]),
            DeclaredCountTest(declared=header_count(offset=0)),
            DeclaredCountTest(declared=header_count(offset=0, companion=table.offset_file)),
            *exp_tests,
        ],
    )


def _offset_case(table: LevelTable) -> HandlerCase:
    return HandlerCase(
        handler_name=table.offset_file,
        data_file=table.offset_file,
        companion_files={},
        loc_file=None,
        uses_loc=False,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{table.offset_file}",
        tests=[
            SchemaTest(required_keys=["level", "data_offset", "data_size"]),
            DeclaredCountTest(declared=header_count(offset=0)),
            RangeTest(col="data_size", min_val=table.row.size, max_val=table.row.size),
        ],
    )


CASES = {table.file_name: _table_case(table) for table in LEVEL_TABLES}
OFFSET_CASES = {table.offset_file: _offset_case(table) for table in LEVEL_TABLES}
_RESULTS: dict[str, HandlerResult] = {}


def _result(case: HandlerCase) -> HandlerResult:
    key = str(case.handler_name)
    if key not in _RESULTS:
        _RESULTS[key] = run_case(replace(case, tests=[]))
    return _RESULTS[key]


def _specs(cases: dict[str, HandlerCase]) -> list[Any]:
    return [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in cases.items() for spec in case.tests]


@pytest.mark.parametrize(("name", "spec"), _specs(CASES))
def test_level_table(name: str, spec: Any) -> None:
    _result(CASES[name]).check(spec)


@pytest.mark.parametrize(("name", "spec"), _specs(OFFSET_CASES))
def test_level_offset_table(name: str, spec: Any) -> None:
    _result(OFFSET_CASES[name]).check(spec)


@pytest.mark.parametrize("table", LEVEL_TABLES, ids=lambda table: table.file_name)
def test_levels_run_from_zero_without_gaps(table: LevelTable) -> None:
    levels = [record["level"] for record in _result(CASES[table.file_name]).records]
    assert levels == list(range(len(levels)))


@pytest.mark.parametrize("table", (SKILL_EXPERIENCE, GUILD_SKILL_EXPERIENCE), ids=lambda table: table.file_name)
def test_exp_never_drops_from_one_level_to_the_next(table: LevelTable) -> None:
    exp = [record["exp"] for record in _result(CASES[table.file_name]).records]
    assert exp == sorted(exp)


def test_a_row_of_another_level_raises() -> None:
    source = _result(CASES[SKILL_EXPERIENCE.file_name]).source
    offset_data = source.file(SKILL_EXPERIENCE.offset_file)
    first_row = parse_level_offset_records(offset_data)[0]
    data = bytearray(source.data)
    _U32.pack_into(data, first_row["data_offset"], first_row["level"] + 1)
    with pytest.raises(ValueError, match="row holds level"):
        parse_level_records(SKILL_EXPERIENCE, bytes(data), offset_data)


def test_different_row_counts_raise() -> None:
    source = _result(CASES[PRODUCT_EXPERIENCE.file_name]).source
    data = bytearray(source.data)
    _U32.pack_into(data, 0, _U32.unpack_from(data, 0)[0] + 1)
    with pytest.raises(ValueError, match="counts"):
        parse_level_records(PRODUCT_EXPERIENCE, bytes(data), source.file(PRODUCT_EXPERIENCE.offset_file))


def test_a_row_of_another_size_raises() -> None:
    source = _result(CASES[GUILD_SKILL_EXPERIENCE.file_name]).source
    with pytest.raises(ValueError, match="row size"):
        parse_level_records(SKILL_EXPERIENCE, source.data, source.file(GUILD_SKILL_EXPERIENCE.offset_file))
