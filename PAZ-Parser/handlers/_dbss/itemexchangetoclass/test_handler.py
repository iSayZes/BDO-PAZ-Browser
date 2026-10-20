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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, LAYOUT_CLASS_SLOTS, OFFSET_FILE, parse_itemexchangetoclass_records, row_size


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
# The index points past the row's leading key, at key_dup.
_INDEXED_KEY_SIZE = 4
# Tuvala main weapons: a season group (exchange type 1).
_TUVALA_MAIN_WEAPON = 165
_SEASON = 1
_WARRIOR = 0
_TUVALA_LONGSWORD = 695113

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_items"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "key", "key_dup", "item_keys", "exchange_type", "exchange_type_name", "class_count", "class_items",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="key", value=_TUVALA_MAIN_WEAPON, expected={"exchange_type": _SEASON}),
        UserLanguageTest(fields=["class_items"]),
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
        SchemaTest(required_keys=["key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="key", value=_TUVALA_MAIN_WEAPON, expected={"key": _TUVALA_MAIN_WEAPON}),
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
def test_itemexchangetoclass_dbss(spec: Any, exchange_result: HandlerResult) -> None:
    exchange_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemexchangetoclassoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_keys_are_unique_and_repeated(exchange_result: HandlerResult) -> None:
    keys = [r["key"] for r in exchange_result.records]
    assert len(keys) == len(set(keys))
    assert all(r["key_dup"] == r["key"] for r in exchange_result.records)


def test_item_slots_are_indexed_by_class_type(exchange_result: HandlerResult) -> None:
    """The Warrior slot (class type 0) of the Tuvala main weapon group holds the Tuvala Longsword."""
    (record,) = [r for r in exchange_result.records if r["key"] == _TUVALA_MAIN_WEAPON]
    assert record["item_keys"][_WARRIOR] == _TUVALA_LONGSWORD


def test_offset_rows_point_past_each_leading_key(offset_result: HandlerResult) -> None:
    """Each index row starts 4 bytes into the row with its key and runs to its end."""
    data = load_binary_fixture(FILE_NAME)
    records = parse_itemexchangetoclass_records(data)
    size = (len(data) - _COUNT_SIZE) // len(records)
    expected = {
        r["key"]: (_COUNT_SIZE + index * size + _INDEXED_KEY_SIZE, size - _INDEXED_KEY_SIZE)
        for index, r in enumerate(records)
    }
    actual = {r["key"]: (r["data_offset"], r["data_size"]) for r in offset_result.records}
    assert actual == expected


def _row(key: int, item_keys: list[int], exchange_type: int) -> bytes:
    return struct.pack(f"<ii{len(item_keys)}IB", key, key, *item_keys, exchange_type)


@pytest.mark.parametrize("class_slots", LAYOUT_CLASS_SLOTS)
def test_parser_reads_every_layout(class_slots: int) -> None:
    items = [_TUVALA_LONGSWORD] + [0] * (class_slots - 1)
    data = struct.pack("<I", 2) + _row(_TUVALA_MAIN_WEAPON, items, _SEASON) + _row(1, [0] * class_slots, 0)
    assert len(data) == _COUNT_SIZE + 2 * row_size(class_slots)
    records = parse_itemexchangetoclass_records(data)
    assert [(r["key"], r["item_keys"][_WARRIOR], r["exchange_type"]) for r in records] == [
        (_TUVALA_MAIN_WEAPON, _TUVALA_LONGSWORD, _SEASON),
        (1, 0, 0),
    ]
    assert all(len(r["item_keys"]) == class_slots for r in records)


def test_parser_rejects_bytes_after_the_rows() -> None:
    class_slots = LAYOUT_CLASS_SLOTS[0]
    data = struct.pack("<I", 1) + _row(_TUVALA_MAIN_WEAPON, [0] * class_slots, 0)
    with pytest.raises(ValueError):
        parse_itemexchangetoclass_records(data + b"\x00")
