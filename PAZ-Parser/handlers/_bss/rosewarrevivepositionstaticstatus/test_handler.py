from __future__ import annotations

import math
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

from _bss.pabr_values.parser import parse_value_table
from _bss.pabr_values.tables import VALUE_TABLES
from .parser import parse_revive_position_records


_U32 = struct.Struct("<I")
_TEAM_COUNT_AT = 4
# u8 respawn_position_type and u32 position_count, then the positions and an f32.
_TEAM_POINT_HEAD = 5
_POSITION_SIZE = 12
_FLOAT_SIZE = 4
_MONSTER_FILE = "rosewarfiercebattlemonsterstaticstatus.bss"


def _declared_points(source: CaseInput) -> int:
    """The team count, plus the sanctum count that follows the team points."""
    data = source.data
    (team_count,) = _U32.unpack_from(data, _TEAM_COUNT_AT)
    offset = _TEAM_COUNT_AT + _U32.size
    for _ in range(team_count):
        (position_count,) = _U32.unpack_from(data, offset + 1)
        offset += _TEAM_POINT_HEAD + position_count * _POSITION_SIZE + _FLOAT_SIZE
    (sanctum_count,) = _U32.unpack_from(data, offset)
    return team_count + sanctum_count


CASE = HandlerCase(
    handler_name="rosewarrevivepositionstaticstatus.bss",
    data_file="rosewarrevivepositionstaticstatus.bss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/rosewarrevivepositionstaticstatus.bss",
    tests=[
        SchemaTest(required_keys=["respawn_position_type", "fierce_battle_key", "positions", "unknown_positions_00"]),
        DeclaredCountTest(declared=_declared_points),
    ],
)


@pytest.fixture(scope="module")
def revive_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_rosewarrevivepositionstaticstatus_bss(spec: Any, revive_result: HandlerResult) -> None:
    revive_result.check(spec)


def test_each_point_has_one_key_and_finite_positions(revive_result: HandlerResult) -> None:
    for record in revive_result.records:
        assert (record["respawn_position_type"] is None) != (record["fierce_battle_key"] is None), record
        assert record["positions"], record
        assert all(math.isfinite(value) for position in record["positions"] for value in position)


def test_every_sanctum_point_is_a_sanctum(revive_result: HandlerResult) -> None:
    (monster_table,) = [table for table in VALUE_TABLES if table.file_name == _MONSTER_FILE]
    sanctums = {row["fierce_battle_key"] for row in parse_value_table(load_binary_fixture(_MONSTER_FILE), monster_table)}
    keys = {record["fierce_battle_key"] for record in revive_result.records} - {None}
    assert keys and keys <= sanctums


def _pabr(values: bytes) -> bytes:
    table_start = _TEAM_COUNT_AT + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_team_points_come_before_sanctum_points() -> None:
    team = _U32.pack(1) + struct.pack("<BI3ff", 2, 1, 1.0, 2.0, 3.0, 500.0)
    sanctum = _U32.pack(1) + struct.pack("<HI3ff", 11, 1, 4.0, 5.0, 6.0, 400.0)
    records = parse_revive_position_records(_pabr(team + sanctum))
    assert records == [
        {"respawn_position_type": 2, "fierce_battle_key": None, "positions": [[1.0, 2.0, 3.0]], "unknown_positions_00": 500},
        {"fierce_battle_key": 11, "respawn_position_type": None, "positions": [[4.0, 5.0, 6.0]], "unknown_positions_00": 400},
    ]


def test_a_position_count_past_the_string_table_raises() -> None:
    team = _U32.pack(1) + struct.pack("<BI", 1, 9) + bytes(16)
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_revive_position_records(_pabr(team))
