from __future__ import annotations

import math
import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .parser import parse_revive_position_records


_U32 = struct.Struct("<I")
_ROW_COUNT_AT = 4
_ROWS_AT = 8
# u16 territory_key, then the u32 group count.
_ROW_HEAD = 2
# u8 unknown_00, then the u32 position count.
_GROUP_HEAD = 1
_POSITION_SIZE = 17
# CppEnums.OceanSiegeTerritoryName (global_define_cpp_enum.luac): Balenos and Calpheon.
_BALENOS = 0
_CALPHEON = 2


def _declared_positions(source: CaseInput) -> int:
    """The position counts of every group, read from each count field in turn."""
    data = source.data
    (row_count,) = _U32.unpack_from(data, _ROW_COUNT_AT)
    offset = _ROWS_AT
    total = 0
    for _ in range(row_count):
        (group_count,) = _U32.unpack_from(data, offset + _ROW_HEAD)
        offset += _ROW_HEAD + _U32.size
        for _ in range(group_count):
            (position_count,) = _U32.unpack_from(data, offset + _GROUP_HEAD)
            offset += _GROUP_HEAD + _U32.size + position_count * _POSITION_SIZE
            total += position_count
    return total


CASE = HandlerCase(
    handler_name="oceansiegereviveposition.bss",
    data_file="oceansiegereviveposition.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["territory_name"],
    internal_path="gamecommondata/binary/oceansiegereviveposition.bss",
    tests=[
        SchemaTest(
            required_keys=["territory_key", "territory_name", "unknown_00", "x", "y", "z", "unknown_0c", "unknown_10"],
        ),
        DeclaredCountTest(declared=_declared_positions),
        TargetTest(col="territory_key", value=_BALENOS, expected={"territory_name": "Balenos"}),
        TargetTest(col="territory_key", value=_CALPHEON, expected={"territory_name": "Calpheon"}),
        RangeTest(col="unknown_00", min_val=0, max_val=1),
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
def test_oceansiegereviveposition_bss(spec: Any, revive_result: HandlerResult) -> None:
    revive_result.check(spec)


def test_each_position_repeats_its_group_key(revive_result: HandlerResult) -> None:
    for record in revive_result.records:
        assert record["unknown_10"] == record["unknown_00"], record


def test_every_position_is_finite(revive_result: HandlerResult) -> None:
    for record in revive_result.records:
        assert all(math.isfinite(record[axis]) for axis in ("x", "y", "z", "unknown_0c")), record


def _pabr(values: bytes) -> bytes:
    table_start = _ROWS_AT - _U32.size + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_a_row_reads_its_groups_and_positions() -> None:
    position = struct.pack("<4fB", 1.0, -2.0, 3.0, 250.0, 1)
    row = struct.pack("<HI", _CALPHEON, 1) + struct.pack("<BI", 1, 1) + position
    (record,) = parse_revive_position_records(_pabr(_U32.pack(1) + row))
    assert record == {
        "territory_key": _CALPHEON,
        "unknown_00": 1,
        "x": 1,
        "y": -2,
        "z": 3,
        "unknown_0c": 250,
        "unknown_10": 1,
    }


def test_a_position_count_past_the_string_table_raises() -> None:
    row = struct.pack("<HI", _BALENOS, 1) + struct.pack("<BI", 0, 9)
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_revive_position_records(_pabr(_U32.pack(1) + row))


def test_rows_that_stop_short_of_the_string_table_raise() -> None:
    row = struct.pack("<HI", _BALENOS, 0) + b"\x00"
    with pytest.raises(ValueError, match="string table starts"):
        parse_revive_position_records(_pabr(_U32.pack(1) + row))
