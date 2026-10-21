from __future__ import annotations

from collections import defaultdict
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from .parser import FILE_NAME


_COUNT_SIZE = 4
_ROW_SIZE = 13
_HALF_BITS = 16
_HALF_MASK = 0xFFFF
# Key 0x00010001: high half 1, low half 1.
_FIRST_KEY = 0x00010001

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["key", "unknown_04", "unknown_06", "unknown_08", "unknown_0a", "unknown_0c"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
        TargetTest(col="key", value=_FIRST_KEY, expected={"unknown_04": 1, "unknown_06": 1}),
    ],
)


@pytest.fixture(scope="module")
def sequence_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_simplesequence_bss(spec: Any, sequence_result: HandlerResult) -> None:
    sequence_result.check(spec)


def test_halves_repeat_the_key(sequence_result: HandlerResult) -> None:
    for record in sequence_result.records:
        low, high = record["key"] & _HALF_MASK, record["key"] >> _HALF_BITS
        assert (record["unknown_04"], record["unknown_06"]) == (low, high)
        assert (record["unknown_08"], record["unknown_0a"]) == (high, low)


def test_low_halves_count_from_one(sequence_result: HandlerResult) -> None:
    """The keys of one high half have the low halves 1 to N with no gap."""
    lows: dict[int, list[int]] = defaultdict(list)
    for record in sequence_result.records:
        lows[record["key"] >> _HALF_BITS].append(record["key"] & _HALF_MASK)
    gaps = {high: sorted(values) for high, values in lows.items() if sorted(values) != list(range(1, len(values) + 1))}
    assert not gaps, gaps
