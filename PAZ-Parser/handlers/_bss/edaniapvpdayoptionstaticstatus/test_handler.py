from __future__ import annotations

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
    case_id,
    run_case,
)

from .handler import EdaniaPvpDayOptionBssHandler
from .parser import ROW_COUNT, TIMES_PER_ENTRY, parse_pvp_day_records


_U32 = struct.Struct("<I")
_ROWS_AT = 4
_ENTRY_SIZE = 25
_DAYS_PER_WEEK = 7
_HOURS_PER_DAY = 24
_MINUTES_PER_HOUR = 60


def _declared_entries(source: CaseInput) -> int:
    """The entry counts of the three rows, read from each count field in turn."""
    offset = _ROWS_AT
    total = 0
    for _ in range(ROW_COUNT):
        (count,) = _U32.unpack_from(source.data, offset)
        offset += _U32.size + count * _ENTRY_SIZE
        total += count
    return total


CASE = HandlerCase(
    handler_name="edaniapvpdayoptionstaticstatus.bss",
    data_file="edaniapvpdayoptionstaticstatus.bss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/edaniapvpdayoptionstaticstatus.bss",
    tests=[
        SchemaTest(required_keys=["row", "unknown_00", "times", "unknown_rows_00"]),
        DeclaredCountTest(declared=_declared_entries),
        RangeTest(col="row", min_val=0, max_val=ROW_COUNT - 1),
    ],
)


@pytest.fixture(scope="module")
def pvp_day_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_edaniapvpdayoptionstaticstatus_bss(spec: Any, pvp_day_result: HandlerResult) -> None:
    pvp_day_result.check(spec)


def test_every_time_is_a_time_of_the_week(pvp_day_result: HandlerResult) -> None:
    for record in pvp_day_result.records:
        assert len(record["times"]) == TIMES_PER_ENTRY, record
        for day, hour, minute in record["times"]:
            assert 0 <= day < _DAYS_PER_WEEK and 0 <= hour < _HOURS_PER_DAY and 0 <= minute < _MINUTES_PER_HOUR, record


def _pabr(values: bytes) -> bytes:
    table_start = _ROWS_AT + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def _row(*entries: bytes) -> bytes:
    return _U32.pack(len(entries)) + b"".join(entries)


def _entry(flag: int, *times: int) -> bytes:
    return struct.pack("<B6I", flag, *times)


def test_rows_read_their_entries_and_the_closing_byte() -> None:
    first = _entry(1, 0, 22, 0, 6, 22, 0)
    data = _pabr(_row(first) + _row() + _row() + b"\x01")
    assert parse_pvp_day_records(data) == [
        {"row": 0, "unknown_00": 1, "times": [[0, 22, 0], [6, 22, 0]], "unknown_rows_00": 1},
    ]


def test_an_entry_count_past_the_string_table_raises() -> None:
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_pvp_day_records(_pabr(_U32.pack(9) + b"\x00"))


def test_values_that_stop_short_of_the_string_table_raise() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_pvp_day_records(_pabr(_row() + _row() + _row() + b"\x00\x00"))


def test_the_cells_show_each_time_as_day_and_clock() -> None:
    handler = EdaniaPvpDayOptionBssHandler()
    handler.lang = "en"
    record = {"row": 1, "unknown_00": 0, "times": [[1, 0, 10], [1, 0, 20]], "unknown_rows_00": 1}
    html = handler.render_records_page([record], 0, 1)
    assert "Monday 00:10" in html and "Monday 00:20" in html
