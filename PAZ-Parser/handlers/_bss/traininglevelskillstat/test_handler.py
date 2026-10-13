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
    TargetTest,
    case_id,
    run_case,
)

from _bss.traininglevelskillstat.handler import rate_text
from _bss.traininglevelskillstat.parser import parse_traininglevelskillstat_records


# The PABR magic in front of the entries, the 8-byte entry and the trailer.
_ENTRIES_START = 4
_ENTRY_SIZE = 8
_TRAILER_SIZE = 8
_FULL_RATE = 1_000_000


def _entries_before_string_table(source: CaseInput) -> int:
    """The entries between the magic and the string table the trailer points at."""
    (table_start,) = struct.unpack_from("<I", source.data, len(source.data) - _TRAILER_SIZE)
    return (table_start - _ENTRIES_START) // _ENTRY_SIZE


CASE = HandlerCase(
    handler_name="traininglevelskillstat.bss",
    data_file="traininglevelskillstat.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["rank"],
    internal_path="gamecommondata/binary/traininglevelskillstat.bss",
    tests=[
        SchemaTest(required_keys=["level", "rank", "add_vehicle_skill_owner_rate", "add_servant_stat_rate"]),
        DeclaredCountTest(declared=_entries_before_string_table),
        RangeTest(col="add_vehicle_skill_owner_rate", min_val=0, max_val=_FULL_RATE),
        RangeTest(col="add_servant_stat_rate", min_val=0, max_val=_FULL_RATE),
        TargetTest(col="level", value=1, expected={"rank": "Beginner 1"}),
        TargetTest(col="level", value=81, expected={"rank": "Guru 1"}),
    ],
)


@pytest.fixture(scope="module")
def traininglevelskillstat_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_traininglevelskillstat_bss(spec: Any, traininglevelskillstat_result: HandlerResult) -> None:
    traininglevelskillstat_result.check(spec)


def test_levels_run_from_one(traininglevelskillstat_result: HandlerResult) -> None:
    levels = [record["level"] for record in traininglevelskillstat_result.records]
    assert levels == list(range(1, len(levels) + 1))


def test_rates_never_fall_as_the_level_rises(traininglevelskillstat_result: HandlerResult) -> None:
    for field in ("add_vehicle_skill_owner_rate", "add_servant_stat_rate"):
        rates = [record[field] for record in traininglevelskillstat_result.records]
        assert all(lower <= higher for lower, higher in zip(rates, rates[1:])), field


def _file(entries: list[tuple[int, int]], table_start: int | None = None) -> bytes:
    body = b"PABR" + b"".join(struct.pack("<II", *entry) for entry in entries)
    start = len(body) if table_start is None else table_start
    return body + struct.pack("<III", 0, start, 0)


def test_entries_map_to_levels_from_one_skill_rate_first() -> None:
    records = parse_traininglevelskillstat_records(_file([(0, 0), (10_000, 20_000)]))
    assert records == [
        {"level": 1, "add_vehicle_skill_owner_rate": 0, "add_servant_stat_rate": 0},
        {"level": 2, "add_vehicle_skill_owner_rate": 10_000, "add_servant_stat_rate": 20_000},
    ]


def test_a_string_table_inside_an_entry_is_rejected() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_traininglevelskillstat_records(_file([(0, 0), (1, 1)], table_start=10))


def test_rates_show_one_decimal_like_the_tooltip() -> None:
    assert rate_text(217_000) == "21.7%"
    assert rate_text(_FULL_RATE) == "100.0%"
