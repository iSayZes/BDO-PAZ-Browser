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
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, OFFSET_FILE, parse_itemtrade_records


# Bahar <Trade Manager> in Velia.
_BAHAR = 40010
_COUNT_OFFSET = 0
_FIRST_KEY = 4
_KEY_SIZE = 2


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "title"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["character_id", "name", "title"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="character_id",
            value=_BAHAR,
            expected={"character_id": _BAHAR, "name": "Bahar", "title": "<Trade Manager>"},
        ),
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
        SchemaTest(required_keys=["character_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="character_id", value=_BAHAR, expected={"character_id": _BAHAR, "size": _KEY_SIZE}),
    ],
)


@pytest.fixture(scope="module")
def item_trade_result(request: Any) -> HandlerResult:
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
def test_itemtrade_dbss(spec: Any, item_trade_result: HandlerResult) -> None:
    item_trade_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemtradeoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_character_ids_are_unique(item_trade_result: HandlerResult) -> None:
    character_ids = [r["character_id"] for r in item_trade_result.records]
    assert len(character_ids) == len(set(character_ids))


def test_every_offset_row_points_at_its_key() -> None:
    records = parse_itemtrade_records(load_binary_fixture(FILE_NAME))
    key_starts = {r["character_id"]: _FIRST_KEY + index * _KEY_SIZE for index, r in enumerate(records)}
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == {
        character_id: (start, _KEY_SIZE) for character_id, start in key_starts.items()
    }


def _table(*keys: int) -> bytes:
    return struct.pack(f"<I{len(keys)}H", len(keys), *keys)


def test_a_small_table_reads_back() -> None:
    assert parse_itemtrade_records(_table(40010, 40028)) == [
        {"character_id": 40010},
        {"character_id": 40028},
    ]


def test_an_empty_table_reads_back() -> None:
    assert parse_itemtrade_records(_table()) == []


@pytest.mark.parametrize(
    "data",
    [b"", _table(40010)[:-1], _table(40010) + b"\x00\x00"],
    ids=["no_count", "short", "trailing_bytes"],
)
def test_a_size_that_does_not_match_the_count_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_itemtrade_records(data)
