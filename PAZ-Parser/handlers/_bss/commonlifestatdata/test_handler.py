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
    run_case,
)

from _bss.commonlifestatdata.parser import parse_commonlifestat_records
from _bss.lifeexpmaxlevel.parser import parse_lifeexpmaxlevel_records


# The PABR magic in front of the values, the 4-byte value and the trailer.
_VALUES_START = 4
_VALUE_SIZE = 4
_TRAILER_SIZE = 8
# CppEnums.LifeExperienceType: the two life skills whose tab shows this mastery.
_GATHERING = 0
_PROCESSING = 5


def _values_before_string_table(source: CaseInput) -> int:
    """The f32 values between the magic and the string table the trailer points at."""
    (table_start,) = struct.unpack_from("<I", source.data, len(source.data) - _TRAILER_SIZE)
    return (table_start - _VALUES_START) // _VALUE_SIZE


CASE = HandlerCase(
    handler_name="commonlifestatdata.bss",
    data_file="commonlifestatdata.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["rank"],
    internal_path="gamecommondata/binary/commonlifestatdata.bss",
    tests=[
        SchemaTest(required_keys=["level", "rank", "mastery"]),
        DeclaredCountTest(declared=_values_before_string_table),
        TargetTest(col="level", value=1, expected={"rank": "Beginner 1"}),
        TargetTest(col="level", value=81, expected={"rank": "Guru 1"}),
    ],
)


@pytest.fixture(scope="module")
def commonlifestat_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_commonlifestatdata_bss(spec: Any, commonlifestat_result: HandlerResult) -> None:
    commonlifestat_result.check(spec)


def test_levels_run_to_the_max_gathering_and_processing_level(commonlifestat_result: HandlerResult) -> None:
    max_levels = {
        record["life_skill"]: record["max_level"]
        for record in parse_lifeexpmaxlevel_records(load_binary_fixture("lifeexpmaxlevel.bss"))
    }
    levels = [record["level"] for record in commonlifestat_result.records]

    assert levels == list(range(1, len(levels) + 1))
    assert levels[-1] == max_levels[_GATHERING] == max_levels[_PROCESSING]


def test_mastery_never_falls_as_the_level_rises(commonlifestat_result: HandlerResult) -> None:
    masteries = [record["mastery"] for record in commonlifestat_result.records]
    assert all(lower <= higher for lower, higher in zip(masteries, masteries[1:]))


def _file(values: list[float], table_start: int | None = None) -> bytes:
    body = b"PABR" + b"".join(struct.pack("<f", value) for value in values)
    start = len(body) if table_start is None else table_start
    return body + struct.pack("<III", 0, start, 0)


def test_values_map_to_levels_from_one() -> None:
    records = parse_commonlifestat_records(_file([0.0, 10.0, 15.0]))
    assert records == [
        {"level": 1, "mastery": 0.0},
        {"level": 2, "mastery": 10.0},
        {"level": 3, "mastery": 15.0},
    ]


def test_a_string_table_inside_a_value_is_rejected() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_commonlifestat_records(_file([0.0, 10.0], table_start=10))
