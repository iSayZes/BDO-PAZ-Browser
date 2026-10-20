from __future__ import annotations

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

from _bss.servantmating.parser import parse_servantmating_records


CASE = HandlerCase(
    handler_name="servantmating.bss",
    data_file="servantmating.bss",
    companion_files={"characterstaticoffset.dbss": "characterstaticoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["imperial_steed_name"],
    internal_path="gamecommondata/binary/servantmating.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "average_grade",
                "result_max_grade",
                "result_min_grade",
                "imperial_steed_character_id",
                "imperial_steed_name",
                "imperial_steed_rate",
                "has_character_row",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        # A chance on the 1,000,000 = 100% scale.
        RangeTest(col="imperial_steed_rate", min_val=0, max_val=1_000_000),
    ],
)


@pytest.fixture(scope="module")
def mating_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_servantmating_bss(spec: Any, mating_result: HandlerResult) -> None:
    mating_result.check(spec)


def test_foal_grade_range_is_ordered(mating_result: HandlerResult) -> None:
    # Checks the max-before-min order: the first u16 is never below the second.
    for r in mating_result.records:
        assert r["result_min_grade"] <= r["result_max_grade"], r


def test_bands_rise_with_their_key(mating_result: HandlerResult) -> None:
    # Checks key and average_grade: in key order, each band starts above the one before.
    grades = [r["average_grade"] for r in sorted(mating_result.records, key=lambda r: r["key"])]
    assert grades == sorted(set(grades))


def test_imperial_steed_is_a_character(mating_result: HandlerResult) -> None:
    assert all(r["has_character_row"] for r in mating_result.records)


def test_rows_must_end_at_eof() -> None:
    with pytest.raises(ValueError, match="declares 1 rows"):
        parse_servantmating_records((1).to_bytes(4, "little") + bytes(19))


def test_repeated_key_must_match() -> None:
    row = (1).to_bytes(4, "little") + (2).to_bytes(4, "little") + bytes(12)
    with pytest.raises(ValueError, match="repeats key 2, expected 1"):
        parse_servantmating_records((1).to_bytes(4, "little") + row)
