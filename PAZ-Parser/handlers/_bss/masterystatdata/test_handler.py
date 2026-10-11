from __future__ import annotations

import json
import struct
from dataclasses import replace
from pathlib import Path
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from .alchemy import extra_item_rates
from .display import rate_text
from .parser import parse_mastery_records
from .spec import ALCHEMY, COOKING, FISHING, HUNTING, MASTERY_TABLES, SAIL, TRAINING, CellFormat, MasteryTable


_LANG_DIR = Path(__file__).parent / "lang"
_DERIVED_ALCHEMY_FIELDS = ["extra_basic_item_rate", "extra_special_item_rate", "extra_rare_item_rate"]
# CppEnums.ServantStatType has eight entries, Type_Acceleration to Type_MaxAngle.
_SERVANT_STAT_TYPES = 8


def _case(spec: MasteryTable, extra_keys: list[str], tests: list) -> HandlerCase:
    return HandlerCase(
        handler_name=spec.file_name,
        data_file=spec.file_name,
        companion_files={},
        loc_file="languagedata_en.loc",
        uses_loc=False,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{spec.file_name}",
        tests=[
            SchemaTest(required_keys=["mastery", *spec.fields, *extra_keys]),
            DeclaredCountTest(declared=header_count(offset=4)),
            # Every table ends on mastery 0.
            TargetTest(col="mastery", value=0, expected={"mastery": 0}),
            *tests,
        ],
    )


FISHING_CASE = _case(FISHING, [], [])
COOKING_CASE = _case(COOKING, [], [])
HUNTING_CASE = _case(HUNTING, [], [])
ALCHEMY_CASE = _case(ALCHEMY, _DERIVED_ALCHEMY_FIELDS, [])
SAIL_CASE = _case(SAIL, [], [
    RangeTest(col="unknown_08", min_val=_SERVANT_STAT_TYPES, max_val=_SERVANT_STAT_TYPES),
])
TRAINING_CASE = _case(TRAINING, [], [])

CASES = [FISHING_CASE, COOKING_CASE, HUNTING_CASE, ALCHEMY_CASE, SAIL_CASE, TRAINING_CASE]
_RESULTS: dict[str, HandlerResult] = {}


def _result(case: HandlerCase) -> HandlerResult:
    result = _RESULTS.get(case.handler_name)
    if result is None:
        result = run_case(replace(case, tests=[]))
        _RESULTS[case.handler_name] = result
    return result


_SPECS = [(case, spec) for case in CASES for spec in case.tests]


@pytest.mark.parametrize(
    ("case", "spec"),
    _SPECS,
    ids=[f"{case.handler_name}-{case_id(spec)}" for case, spec in _SPECS],
)
def test_mastery_table(case: HandlerCase, spec: Any) -> None:
    _result(case).check(spec)


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_mastery_falls_in_whole_steps(case: HandlerCase) -> None:
    """Rows run from the highest mastery down to 0, each a whole number below the one before."""
    masteries = [record["mastery"] for record in _result(case).records]

    assert all(mastery.is_integer() for mastery in masteries)
    assert all(higher > lower for higher, lower in zip(masteries, masteries[1:]))


def test_every_column_has_an_english_label() -> None:
    labels = json.loads((_LANG_DIR / "en.json").read_text(encoding="utf-8"))["columns"]
    for spec in MASTERY_TABLES:
        for column in spec.columns:
            assert column.label_key in labels, (spec.file_name, column.label_key)


def test_shown_columns_are_record_fields() -> None:
    derived = set(_DERIVED_ALCHEMY_FIELDS)
    for spec in MASTERY_TABLES:
        fields = set(spec.fields) | (derived if spec.derive else set())
        for column in spec.columns:
            assert column.field in fields, (spec.file_name, column.field)


def _file(spec: MasteryTable, rows: list[tuple], declared: int | None = None) -> bytes:
    """PABR, the row count, the rows, an empty string table and the trailer."""
    count = len(rows) if declared is None else declared
    body = b"PABR" + struct.pack("<I", count) + b"".join(spec.row.pack(*row) for row in rows)
    return body + struct.pack("<III", 0, len(body), 0)


def test_rows_map_to_the_spec_fields() -> None:
    data = _file(COOKING, [(50.0, 1, 2, 3, 4, 5), (0.0, 0, 0, 0, 0, 0)])
    records = parse_mastery_records(data, COOKING)

    assert records[0] == {
        "mastery": 50.0,
        "speed_cook_rate": 1,
        "basic_max_drop_rate": 2,
        "add_critical_drop_rate": 3,
        "add_critical_max_drop_rate": 4,
        "add_royal_trade_bonus": 5,
    }
    assert records[1]["mastery"] == 0.0


def test_a_float_field_is_read_as_f32() -> None:
    row = (100.0, 2.0, 8, 1, 2, 3, 4, 5, 6, 7, 8)
    (record,) = parse_mastery_records(_file(SAIL, [row]), SAIL)

    assert record["unknown_04"] == 2.0
    assert record["max_angle"] == 8


def test_a_count_that_misses_the_string_table_is_rejected() -> None:
    data = _file(FISHING, [(50.0, 1), (0.0, 0)], declared=1)
    with pytest.raises(ValueError, match="string table starts"):
        parse_mastery_records(data, FISHING)


def test_rates_round_like_the_life_skill_tooltip() -> None:
    assert rate_text(764_500, CellFormat.RATE_2) == "76.45%"
    # floor((rate + 50) / 100) / 100: 49 rounds down, 50 up.
    assert rate_text(49, CellFormat.RATE_2) == "0.00%"
    assert rate_text(50, CellFormat.RATE_2) == "0.01%"
    assert rate_text(3_491.04, CellFormat.RATE_3) == "0.349%"
    assert rate_text(-1, CellFormat.RATE_2) == "0.00%"


def test_extra_item_tiers_split_the_event_drop_rate() -> None:
    rates = extra_item_rates({"event_drop_rate": 100_000, "event_drop_rate_1": 500_000, "event_drop_rate_2": 200_000})

    assert rates["extra_basic_item_rate"] == pytest.approx(40_000)
    assert rates["extra_special_item_rate"] == pytest.approx(40_000)
    assert rates["extra_rare_item_rate"] == pytest.approx(20_000)
