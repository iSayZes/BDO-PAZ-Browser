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
    SchemaTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_offset_rows
from _dbss.displayexchangeitemnpc.parser import FILE_NAME as DISPLAY_FILE, parse_displayexchangeitemnpc_records
from .parser import FILE_NAME, OFFSET_FILE, parse_itemexchangebynpc_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
_ROW_SIZE = 28
_OFFSET_ROW_SIZE = 10
# The leading index key; the offset index points past it, at the key copy.
_INDEX_KEY_SIZE = 2


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={DISPLAY_FILE: DISPLAY_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["need_item_name", "result_item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "item_exchange_key", "item_exchange_key_dup", "need_item_key", "need_item_count",
            "result_item_key", "result_item_count", "need_item_name", "result_item_name", "npc_names",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        DeclaredCountTest(declared=fixed_rows(_ROW_SIZE, header_size=_COUNT_SIZE)),
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
        SchemaTest(required_keys=["item_exchange_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
    ],
)


@pytest.fixture(scope="module")
def exchange_result(request: Any) -> HandlerResult:
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
def test_itemexchangebynpc_dbss(spec: Any, exchange_result: HandlerResult) -> None:
    exchange_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemexchangebynpcoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_key_is_stored_twice_and_unique(exchange_result: HandlerResult) -> None:
    keys = [r["item_exchange_key"] for r in exchange_result.records]
    assert len(keys) == len(set(keys))
    for r in exchange_result.records:
        assert r["item_exchange_key_dup"] == r["item_exchange_key"], r["item_exchange_key"]


def test_every_exchange_trades_items(exchange_result: HandlerResult) -> None:
    for r in exchange_result.records:
        assert r["need_item_key"] and r["result_item_key"], r["item_exchange_key"]
        assert r["need_item_count"] > 0 and r["result_item_count"] > 0, r["item_exchange_key"]


def test_listed_exchanges_name_their_npcs(exchange_result: HandlerResult) -> None:
    """A key some `displayexchangeitemnpc.dbss` dialog lists shows at least one NPC."""
    listed = {
        key
        for row in parse_displayexchangeitemnpc_records(load_binary_fixture(DISPLAY_FILE))
        for key in row["item_exchange_keys"]
    }
    for r in exchange_result.records:
        assert bool(r["npc_names"]) == (r["item_exchange_key"] in listed), r["item_exchange_key"]


def test_offset_rows_point_past_the_index_key() -> None:
    """Each index row starts at a row's key copy and covers the rest of the row."""
    records = parse_itemexchangebynpc_records(load_binary_fixture(FILE_NAME))
    expected = {
        r["item_exchange_key"]: (_COUNT_SIZE + index * _ROW_SIZE + _INDEX_KEY_SIZE, _ROW_SIZE - _INDEX_KEY_SIZE)
        for index, r in enumerate(records)
    }
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == expected


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    row = struct.pack("<HHIqIq", 7, 7, 1001, 25, 40450, 1)
    data = struct.pack("<I", 1) + row
    record = parse_itemexchangebynpc_records(data)[0]
    assert record == {
        "item_exchange_key": 7,
        "item_exchange_key_dup": 7,
        "need_item_key": 1001,
        "need_item_count": 25,
        "result_item_key": 40450,
        "result_item_count": 1,
    }
    with pytest.raises(ValueError):
        parse_itemexchangebynpc_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_itemexchangebynpc_records(data[:-1])
