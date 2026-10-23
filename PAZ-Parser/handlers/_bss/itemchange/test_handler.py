from __future__ import annotations

import struct
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
    header_count,
    run_case,
)

from .parser import FILE_NAME, parse_itemchange_records


# PABR magic, then the u32 row count.
_ROW_COUNT_AT = 4
_U32 = struct.Struct("<I")
_ROW = struct.Struct("<HHIIi")
# Row 1 of clients 1784 and 3482: [Warrior] Calpheon Noble Suit to its costume.
_NOBLE_SUIT_ROW = {"key_dup": 1, "from_item_key": 14201, "to_item_key": 14301}

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["from_item_name", "to_item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["key", "key_dup", "from_item_key", "to_item_key", "type", "from_item_name", "to_item_name"]),
        DeclaredCountTest(declared=header_count(offset=_ROW_COUNT_AT)),
        TargetTest(col="key", value=1, expected=_NOBLE_SUIT_ROW),
    ],
)


@pytest.fixture(scope="module")
def itemchange_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemchange_bss(spec: Any, itemchange_result: HandlerResult) -> None:
    itemchange_result.check(spec)


def test_keys_are_unique_and_stored_twice(itemchange_result: HandlerResult) -> None:
    keys = [record["key"] for record in itemchange_result.records]
    assert len(keys) == len(set(keys))
    assert all(record["key_dup"] == record["key"] for record in itemchange_result.records)


def test_every_item_has_a_name(itemchange_result: HandlerResult) -> None:
    for record in itemchange_result.records:
        assert record["from_item_name"] and record["to_item_name"], record


def _pabr(body: bytes) -> bytes:
    table_start = 4 + len(body)
    return b"PABR" + body + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_rows_read_in_member_order() -> None:
    data = _pabr(_U32.pack(1) + _ROW.pack(7, 7, 14201, 14301, 0))
    assert parse_itemchange_records(data) == [
        {"key": 7, "key_dup": 7, "from_item_key": 14201, "to_item_key": 14301, "type": 0}
    ]


def test_rows_that_stop_short_of_the_string_table_raise() -> None:
    data = _pabr(_U32.pack(1) + _ROW.pack(7, 7, 14201, 14301, 0) + bytes(4))
    with pytest.raises(ValueError, match="string table starts"):
        parse_itemchange_records(data)
