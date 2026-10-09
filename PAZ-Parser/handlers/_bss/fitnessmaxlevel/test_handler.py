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
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _bss.fitnessmaxlevel.parser import parse_fitnessmaxlevel_records
from _dbss.fitnesslevel.parser import parse_fitnesslevel_records


_U32 = struct.Struct("<I")
_MAGIC_SIZE = 4
_TRAILER_END_AT = -8
_FITNESS_TYPES = (0, 1, 2)


def _array_length(source: CaseInput) -> int:
    """The u32 count between the magic and the trailer's `end_of_data`."""
    (end_of_data,) = _U32.unpack_from(source.file(None), _TRAILER_END_AT)
    return (end_of_data - _MAGIC_SIZE) // _U32.size


CASE = HandlerCase(
    handler_name="fitnessmaxlevel.bss",
    data_file="fitnessmaxlevel.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/fitnessmaxlevel.bss",
    tests=[
        SchemaTest(required_keys=["fitness_type", "fitness_name", "max_level"]),
        DeclaredCountTest(declared=_array_length),
        RangeTest(col="fitness_type", min_val=min(_FITNESS_TYPES), max_val=max(_FITNESS_TYPES)),
        TargetTest(col="fitness_type", value=0, expected={"fitness_name": "Breath"}),
        TargetTest(col="fitness_type", value=1, expected={"fitness_name": "Strength"}),
        TargetTest(col="fitness_type", value=2, expected={"fitness_name": "Health"}),
    ],
)


@pytest.fixture(scope="module")
def fitnessmaxlevel_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fitnessmaxlevel_bss(spec: Any, fitnessmaxlevel_result: HandlerResult) -> None:
    fitnessmaxlevel_result.check(spec)


def test_each_max_level_is_the_top_row_of_its_fitnesslevel_block(fitnessmaxlevel_result: HandlerResult) -> None:
    rows = parse_fitnesslevel_records(
        load_binary_fixture("fitnesslevel.dbss"), load_binary_fixture("fitnessleveloffset.dbss")
    )
    top_levels: dict[int, int] = {}
    for row in rows:
        top_levels[row["fitness_type"]] = max(top_levels.get(row["fitness_type"], 0), row["level"])
    max_levels = {record["fitness_type"]: record["max_level"] for record in fitnessmaxlevel_result.records}
    assert max_levels == top_levels


def test_a_missing_magic_raises() -> None:
    with pytest.raises(ValueError, match="PABR"):
        parse_fitnessmaxlevel_records(bytes(28))


def test_a_trailer_that_does_not_close_the_array_raises() -> None:
    data = b"PABR" + _U32.pack(50) * 3 + struct.pack("<III", 0, 12, 0)
    with pytest.raises(ValueError, match="trailer"):
        parse_fitnessmaxlevel_records(data)
