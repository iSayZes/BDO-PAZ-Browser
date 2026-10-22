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
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .parser import parse_revive_position_records


_U32 = struct.Struct("<I")
_ROW_HEAD = struct.Struct("<IH")
_ROW_COUNT_AT = 4
_ROWS_AT = 8
_POSITION_SIZE = 16
# territoryinfo.bss keys (LOC type 12): Balenos and Calpheon.
_BALENOS = 0
_CALPHEON = 2


def _declared_positions(source: CaseInput) -> int:
    """The position counts of every row, read from each count field in turn."""
    data = source.data
    (row_count,) = _U32.unpack_from(data, _ROW_COUNT_AT)
    offset = _ROWS_AT
    total = 0
    for _ in range(row_count):
        (position_count, _territory_key) = _ROW_HEAD.unpack_from(data, offset)
        offset += _ROW_HEAD.size + position_count * _POSITION_SIZE
        total += position_count
    return total


CASE = HandlerCase(
    handler_name="siege2024revivepositionstaticstatus.bss",
    data_file="siege2024revivepositionstaticstatus.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["territory_name"],
    internal_path="gamecommondata/binary/siege2024revivepositionstaticstatus.bss",
    tests=[
        SchemaTest(required_keys=["territory_key", "territory_name", "x", "y", "z", "unknown_0c"]),
        DeclaredCountTest(declared=_declared_positions),
        TargetTest(col="territory_key", value=_BALENOS, expected={"territory_name": "Balenos"}),
        TargetTest(col="territory_key", value=_CALPHEON, expected={"territory_name": "Calpheon"}),
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
def test_siege2024revivepositionstaticstatus_bss(spec: Any, revive_result: HandlerResult) -> None:
    revive_result.check(spec)


def test_every_territory_has_a_name(revive_result: HandlerResult) -> None:
    for record in revive_result.records:
        assert record["territory_name"], record


def test_every_position_is_finite(revive_result: HandlerResult) -> None:
    for record in revive_result.records:
        assert all(math.isfinite(record[axis]) for axis in ("x", "y", "z", "unknown_0c")), record


def _pabr(values: bytes) -> bytes:
    table_start = _ROWS_AT - _U32.size + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_the_count_comes_before_the_territory_key() -> None:
    row = _ROW_HEAD.pack(1, _CALPHEON) + struct.pack("<4f", 1.0, -2.0, 3.0, 500.0)
    (record,) = parse_revive_position_records(_pabr(_U32.pack(1) + row))
    assert record == {"territory_key": _CALPHEON, "x": 1, "y": -2, "z": 3, "unknown_0c": 500}


def test_a_position_count_past_the_string_table_raises() -> None:
    row = _ROW_HEAD.pack(9, _BALENOS)
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_revive_position_records(_pabr(_U32.pack(1) + row))


def test_rows_that_stop_short_of_the_string_table_raise() -> None:
    row = _ROW_HEAD.pack(0, _BALENOS) + b"\x00"
    with pytest.raises(ValueError, match="string table starts"):
        parse_revive_position_records(_pabr(_U32.pack(1) + row))
