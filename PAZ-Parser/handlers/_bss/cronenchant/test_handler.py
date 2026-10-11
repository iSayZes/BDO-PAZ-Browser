from __future__ import annotations

import struct
from dataclasses import replace
from itertools import groupby
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .parser import parse_cronenchant_records


_STEP_SIZE = 39
_COUNT = struct.Struct("<I")
# PRI to DEC, the levels a Caphras grade block can apply to.
_FIRST_GRADE_LEVEL = 16
_LAST_GRADE_LEVEL = 25


def _declared_steps(source: CaseInput) -> int:
    """Sum of the step counts the category and grade blocks declare."""
    data = source.file(None)
    pos, total = 4, 0
    (category_count,) = _COUNT.unpack_from(data, pos)
    pos += _COUNT.size
    for _ in range(category_count):
        (grade_count,) = _COUNT.unpack_from(data, pos)
        pos += _COUNT.size
        for _ in range(grade_count):
            (step_count,) = _COUNT.unpack_from(data, pos)
            pos += _COUNT.size + step_count * _STEP_SIZE
            total += step_count
    return total


CASE = HandlerCase(
    handler_name="cronenchant.bss",
    data_file="cronenchant.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/cronenchant.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "category",
                "gear",
                "enchant_level",
                "grade",
                "caphras_level",
                "stones",
                "total_stones",
                "ap",
                "dp",
                "accuracy",
                "evasion",
                "hidden_evasion",
                "damage_reduction",
                "hidden_damage_reduction",
                "hp",
                "mp",
            ],
        ),
        DeclaredCountTest(declared=_declared_steps),
        RangeTest(col="enchant_level", min_val=_FIRST_GRADE_LEVEL, max_val=_LAST_GRADE_LEVEL),
        # Category keys named after the Caphras cost tables they match.
        TargetTest(col="category", value=1, expected={"gear": "Boss Main Weapon"}),
        TargetTest(col="category", value=2, expected={"gear": "Boss Awakening Weapon"}),
        TargetTest(col="category", value=5, expected={"gear": "Boss Sub-Weapon"}),
        TargetTest(col="category", value=8, expected={"gear": "Dim Tree Armor"}),
        TargetTest(col="category", value=10, expected={"gear": "Green Armor"}),
    ],
)


@pytest.fixture(scope="module")
def cronenchant_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_cronenchant_bss(spec: Any, cronenchant_result: HandlerResult) -> None:
    cronenchant_result.check(spec)


def _grade_runs(records: list[dict]) -> list[list[dict]]:
    return [list(run) for _, run in groupby(records, key=lambda r: (r["category"], r["enchant_level"]))]


def test_each_grade_counts_caphras_levels_from_one(cronenchant_result: HandlerResult) -> None:
    for run in _grade_runs(cronenchant_result.records):
        assert [r["caphras_level"] for r in run] == list(range(1, len(run) + 1))


def test_total_stones_rise_and_stones_are_the_steps(cronenchant_result: HandlerResult) -> None:
    for run in _grade_runs(cronenchant_result.records):
        totals = [r["total_stones"] for r in run]
        assert totals == sorted(set(totals)), f"category {run[0]['category']} level {run[0]['enchant_level']}"
        assert [r["stones"] for r in run] == [b - a for a, b in zip([0, *totals], totals)]


def test_dp_is_evasion_plus_damage_reduction(cronenchant_result: HandlerResult) -> None:
    for r in cronenchant_result.records:
        assert r["dp"] == r["evasion"] + r["damage_reduction"]


def test_every_category_and_grade_has_a_name(cronenchant_result: HandlerResult) -> None:
    unnamed = {(r["category"], r["enchant_level"]) for r in cronenchant_result.records if not (r["gear"] and r["grade"])}
    assert not unnamed, f"(category, enchant level) without a gear or grade name: {sorted(unnamed)}"


def _file(*blocks: bytes, table_start: int | None = None) -> bytes:
    """PABR, one category, the given grade blocks, then the empty string table."""
    body = b"PABR" + _COUNT.pack(1) + _COUNT.pack(len(blocks)) + b"".join(blocks)
    start = len(body) if table_start is None else table_start
    return body + _COUNT.pack(0) + _COUNT.pack(start) + bytes(4)


def _step(category: int, enchant_level: int, total: int) -> bytes:
    return struct.pack("<HBI7fI", category, enchant_level, total, *([0.0] * 7), 0)


def test_blocks_that_stop_short_of_the_string_table_are_rejected() -> None:
    # One step declared, two stored.
    data = _file(_COUNT.pack(1) + _step(1, 18, 20) + _step(1, 18, 40))
    with pytest.raises(ValueError, match="string table starts"):
        parse_cronenchant_records(data)


def test_blocks_that_run_past_the_string_table_are_rejected() -> None:
    data = _file(_COUNT.pack(1) + _step(1, 18, 20), table_start=16)
    with pytest.raises(ValueError, match="runs past"):
        parse_cronenchant_records(data)


def test_a_step_of_another_grade_is_rejected() -> None:
    data = _file(_COUNT.pack(2) + _step(1, 18, 20) + _step(1, 19, 40))
    with pytest.raises(ValueError, match="the block started with"):
        parse_cronenchant_records(data)
