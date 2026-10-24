from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)
from tests.offset_rows import offset_row_problems

from _common.pabr_strings import string_table_start
from .parser import (
    FILE_NAME,
    KEY_FIELD,
    OFFSET_FILE,
    ROW_SIZE,
    parse_cashitemmarketsetting_records,
    parse_cashitemmarketsettingoffset_rows,
)


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
_FIRST_ROW = 8
_KEY = struct.Struct("<I")
# Blessing of Kamasylve (15 Days); a row on clients 1784 and 3483 and in the
# client 1784 CashItemMarketSetting sheet.
_BLESSING_OF_KAMASYLVE = 17081
# The fields the row stores twice.
_COPIED_FIELDS = (
    "base_price_for_item_market",
    "maxest_percent_for_item_market",
    "minest_percent_for_item_market",
    "max_register_count_for_item_market",
)

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                KEY_FIELD, "item_name", "icon_path", *_COPIED_FIELDS,
                *(f"{field}_dup" for field in _COPIED_FIELDS), "unknown_28",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="max_register_count_for_item_market", min_val=0, max_val=1),
        TargetTest(
            col=KEY_FIELD,
            value=_BLESSING_OF_KAMASYLVE,
            expected={KEY_FIELD: _BLESSING_OF_KAMASYLVE, "item_name": "Blessing of Kamasylve (15 Days)"},
        ),
        UserLanguageTest(fields=["item_name"]),
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
        SchemaTest(required_keys=[KEY_FIELD, "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="data_size", min_val=0, max_val=0),
    ],
)


@pytest.fixture(scope="module")
def market_setting_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_cashitemmarketsetting_dbss(spec: Any, market_setting_result: HandlerResult) -> None:
    market_setting_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_cashitemmarketsettingoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_item_ids_are_unique(market_setting_result: HandlerResult) -> None:
    item_ids = [record[KEY_FIELD] for record in market_setting_result.records]
    assert len(item_ids) == len(set(item_ids))


def test_every_copy_equals_its_field(market_setting_result: HandlerResult) -> None:
    for record in market_setting_result.records:
        for field in _COPIED_FIELDS:
            assert record[f"{field}_dup"] == record[field], (record[KEY_FIELD], field)


def test_every_offset_row_points_just_past_its_rows_item_id() -> None:
    data = load_binary_fixture(FILE_NAME)
    # The index stores size 0; each row runs ROW_SIZE bytes from its item_id.
    rows = [
        replace(row, size=ROW_SIZE - _KEY.size)
        for row in parse_cashitemmarketsettingoffset_rows(load_binary_fixture(OFFSET_FILE))
    ]
    rows_data = data[: string_table_start(data)]
    assert offset_row_problems(rows_data, rows, _KEY, rows_start=_FIRST_ROW, lead=_KEY.size) == []


def _table(*rows: tuple[int, int, int, int, int]) -> bytes:
    """A PABR table of (item, price, max %, min %, register count) rows, each value stored twice."""
    body = b"".join(
        struct.pack("<IQQIIIIHH6x", item, price, price, maxest, maxest, minest, minest, count, count)
        for item, price, maxest, minest, count in rows
    )
    rows_end = _FIRST_ROW + len(body)
    return b"PABR" + struct.pack("<I", len(rows)) + body + struct.pack("<III", 0, rows_end, 0)


def test_a_small_table_reads_back() -> None:
    (record,) = parse_cashitemmarketsetting_records(_table((7, 410500, 150000, 700000, 1)))
    assert record == {
        KEY_FIELD: 7,
        "base_price_for_item_market": 410500,
        "base_price_for_item_market_dup": 410500,
        "maxest_percent_for_item_market": 150000,
        "maxest_percent_for_item_market_dup": 150000,
        "minest_percent_for_item_market": 700000,
        "minest_percent_for_item_market_dup": 700000,
        "max_register_count_for_item_market": 1,
        "max_register_count_for_item_market_dup": 1,
        "unknown_28": "000000000000",
    }


def test_a_missing_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_cashitemmarketsetting_records(b"XXXX" + _table((7, 1, 1, 1, 1))[4:])
