from __future__ import annotations

import re
import struct
from dataclasses import replace
from typing import Any

import pytest

from _bss.employeeexp.display import growth_text, top_levels
from _bss.employeestaticstatus.display import stat_labels
from _bss.employeeexp.parser import ABILITY_COUNT, parse_employeeexp_records
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)


# Dice notation: `1D5`, `1D5+30`.
_DICE = re.compile(r"\d+D\d+(\+\d+)?")

CASE = HandlerCase(
    handler_name="employeeexp.bss",
    data_file="employeeexp.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/employeeexp.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "employee_key",
                "level",
                "exp_to_next_level",
                "exp_raw",
                "unknown_00",
                "unknown_09",
                "growth_refs",
                "growth_dice",
                "is_max_level",
                "growth",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        # Every sailor starts at level 1.
        TargetTest(col="level", value=1, expected={"level": 1, "is_max_level": False}),
    ],
)


@pytest.fixture(scope="module")
def employeeexp_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_employeeexp_bss(spec: Any, employeeexp_result: HandlerResult) -> None:
    employeeexp_result.check(spec)


def test_each_sailor_level_is_one_row(employeeexp_result: HandlerResult) -> None:
    keys = [(record["employee_key"], record["level"]) for record in employeeexp_result.records]
    assert len(keys) == len(set(keys))


def test_each_sailor_has_levels_one_to_its_top(employeeexp_result: HandlerResult) -> None:
    records = employeeexp_result.records
    for key, top in top_levels(records).items():
        levels = sorted(record["level"] for record in records if record["employee_key"] == key)
        assert levels == list(range(1, top + 1)), key


def test_growth_refs_resolve_to_dice(employeeexp_result: HandlerResult) -> None:
    for record in employeeexp_result.records:
        assert len(record["growth_dice"]) == ABILITY_COUNT
        for ref, dice in zip(record["growth_refs"], record["growth_dice"]):
            # Ref 0 is the empty string: the ability does not grow.
            assert bool(ref) == bool(dice), record
            assert not dice or _DICE.fullmatch(dice), dice


def test_only_the_top_level_drops_its_exp(employeeexp_result: HandlerResult) -> None:
    for record in employeeexp_result.records:
        expected = None if record["is_max_level"] else record["exp_raw"]
        assert record["exp_to_next_level"] == expected, record


def test_rows_are_grouped_by_sailor(employeeexp_result: HandlerResult) -> None:
    keys = [(record["employee_key"], record["level"]) for record in employeeexp_result.records]
    assert keys == sorted(keys)


def test_growth_text_names_each_rolled_ability() -> None:
    dice = [""] * ABILITY_COUNT
    dice[6] = "1D2"
    dice[14] = "1D5+30"
    dice[17] = "1D1"
    labels = {6: "Endurance", 14: "Focus"}
    # A type without a label keeps its number.
    assert growth_text(dice, labels) == "Endurance: 1D2, Focus: 1D5+30, 17: 1D1"
    assert growth_text([""] * ABILITY_COUNT, labels) == ""


def test_every_rolled_ability_has_a_stat_name(employeeexp_result: HandlerResult) -> None:
    # Checks the shared labels: each growing type is one the sailor window names.
    named = stat_labels("en")
    for record in employeeexp_result.records:
        rolled = {ability for ability, dice in enumerate(record["growth_dice"]) if dice}
        assert rolled <= named.keys(), record


def test_rows_that_miss_the_string_table_raise(employeeexp_result: HandlerResult) -> None:
    data = bytearray(employeeexp_result.source.data)
    # One row more than the file holds: the rows now run into unknown_after_rows.
    struct.pack_into("<I", data, 4, struct.unpack_from("<I", data, 4)[0] + 1)
    with pytest.raises(ValueError, match="unknown_after_rows"):
        parse_employeeexp_records(bytes(data))


def test_bad_magic_raises() -> None:
    with pytest.raises(ValueError, match="magic"):
        parse_employeeexp_records(b"XXXX" + bytes(16))
