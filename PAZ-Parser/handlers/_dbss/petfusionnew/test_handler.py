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
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_u8_offset_rows
from _dbss.pet.parser import parse_pet_records
from .handler import PetFusionNewAddRateInfoHandler, PetFusionNewHandler
from .parser import (
    ADD_RATE_FIELDS,
    ADD_RATE_FILE,
    ADD_RATE_TIERS,
    FILE_NAME,
    OFFSET_FILE,
    SELECT_FIELDS,
    GOSPHY_FIELD,
    parse_add_rate_records,
    parse_petfusionnew_records,
)


_ROW_SIZE = 17
_ADD_RATE_ROW_SIZE = 16
# Rates are on the 1,000,000 = 100% scale.
_FULL_RATE = 1_000_000
_SELECT_KEYS = [field for select in SELECT_FIELDS for field in select]


def _add_rate_rows(source: CaseInput) -> int:
    """The 16-byte add rate rows: every one but the closing `gosphy_add_rate` array."""
    return fixed_rows(_ADD_RATE_ROW_SIZE)(source) - 1


def _rate_ranges(fields: list[str]) -> list[RangeTest]:
    return [RangeTest(col=field, min_val=0, max_val=_FULL_RATE) for field in fields]


def _pet_tiers() -> set[int]:
    pets = parse_pet_records(load_binary_fixture("pet.dbss"), load_binary_fixture("petoffset.dbss"))
    return {pet["tier"] for pet in pets}


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["tier", *_SELECT_KEYS]),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE)),
        DeclaredCountTest(declared=header_count(companion=OFFSET_FILE)),
        *_rate_ranges([rate for _tier, _padding, rate in SELECT_FIELDS]),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["tier", "offset", "size"]),
        DeclaredCountTest(declared=header_count()),
        RangeTest(col="size", min_val=_ROW_SIZE, max_val=_ROW_SIZE),
    ],
)

ADD_RATE_CASE = HandlerCase(
    handler_name=ADD_RATE_FILE,
    data_file=ADD_RATE_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{ADD_RATE_FILE}",
    tests=[
        SchemaTest(required_keys=["main_tier", *ADD_RATE_FIELDS, GOSPHY_FIELD]),
        DeclaredCountTest(declared=_add_rate_rows),
        RangeTest(col="main_tier", min_val=0, max_val=ADD_RATE_TIERS - 1),
        *_rate_ranges([*ADD_RATE_FIELDS, GOSPHY_FIELD]),
    ],
)

_CASES = {case.handler_name: case for case in (CASE, OFFSET_CASE, ADD_RATE_CASE)}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(_CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in _CASES.items() for spec in case.tests],
)
def test_pet_fusion_tables(name: str, spec: Any) -> None:
    _result(name).check(spec)


def test_tiers_are_pet_dbss_tiers() -> None:
    """Each main tier and result tier is a `tier` that pet.dbss stores."""
    pet_tiers = _pet_tiers()
    for record in _result(FILE_NAME).records:
        assert record["tier"] in pet_tiers
        assert {record[tier_field] for tier_field, _padding, _rate in SELECT_FIELDS} <= pet_tiers


def test_the_first_result_never_lowers_the_main_pet_tier() -> None:
    """PANEL_PETLIST_PETCOMPOSE_DESC: the new pet has the main pet's tier or a higher one."""
    for record in _result(FILE_NAME).records:
        assert record["select_tier_0"] >= record["tier"], record


def test_offset_rows_point_at_each_row() -> None:
    """Each index row starts at its row's own tier key and covers the whole row."""
    records = parse_petfusionnew_records(load_binary_fixture(FILE_NAME))
    expected = {r["tier"]: (index * _ROW_SIZE, _ROW_SIZE) for index, r in enumerate(records)}
    rows = parse_bare_u8_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_every_main_tier_has_add_rates() -> None:
    main_tiers = {record["main_tier"] for record in _result(ADD_RATE_FILE).records}
    assert {record["tier"] for record in _result(FILE_NAME).records} <= main_tiers


def test_parser_reads_a_row_and_rejects_partial_rows() -> None:
    data = struct.pack("<BB3sIB3sI", 0, 2, b"\x7f\x00\x00", 100, 1, b"\x01\x00\x00", _FULL_RATE)
    assert parse_petfusionnew_records(data) == [
        {
            "tier": 0,
            "select_tier_0": 2,
            "padding_02": "7f 00 00",
            "select_rate_0": 100,
            "select_tier_1": 1,
            "padding_0a": "01 00 00",
            "select_rate_1": _FULL_RATE,
        }
    ]
    with pytest.raises(ValueError, match="whole 17-byte rows"):
        parse_petfusionnew_records(data[:-1])


def test_add_rate_parser_splits_the_last_array_by_main_tier() -> None:
    rates = list(range(1, ADD_RATE_TIERS * ADD_RATE_TIERS + 1))
    gosphy = [100, 200, 300, 400]
    records = parse_add_rate_records(struct.pack(f"<{len(rates) + len(gosphy)}I", *rates, *gosphy))
    assert [record["main_tier"] for record in records] == list(range(ADD_RATE_TIERS))
    assert [record[GOSPHY_FIELD] for record in records] == gosphy
    assert [records[1][field] for field in ADD_RATE_FIELDS] == [5, 6, 7, 8]
    with pytest.raises(ValueError, match="expected 80"):
        parse_add_rate_records(bytes(_ADD_RATE_ROW_SIZE * ADD_RATE_TIERS))


def test_tiers_show_from_1_and_rates_as_percent() -> None:
    handler = PetFusionNewAddRateInfoHandler()
    handler.lang = "en"
    record = {"main_tier": 0, **dict(zip(ADD_RATE_FIELDS, (550_000, 0, 0, 0))), GOSPHY_FIELD: 650_000}
    html = handler.render_records_page([record], 0, 1)
    assert "Tier 1" in html and "55%" in html
    assert "Wizard Gosphy" in html and "65%" in html


def test_result_tiers_show_from_1() -> None:
    handler = PetFusionNewHandler()
    handler.lang = "en"
    record = {"tier": 2, "select_tier_0": 3, "select_rate_0": 100, "select_tier_1": 2, "select_rate_1": _FULL_RATE}
    html = handler.render_records_page([record], 0, 1)
    assert "Tier 4" in html and "0.01%" in html and "100%" in html
