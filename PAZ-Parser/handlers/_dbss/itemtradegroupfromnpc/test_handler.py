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
    case_id,
    header_count,
    run_case,
)

from _dbss.itemtradegroupfromnpc.parser import FILE_NAME, OFFSET_FILE, parse_itemtradegroupfromnpc_records
from _dbss.itemtradegrouptonpc.parser import GROUP_HEADER

# Client 3473 ships both files as a count of 0; the Layout 1 tests below build
# client 1784 groups from the doc. The handler is the itemtradegrouptonpc one.
_RECORD_KEYS = [
    "character_id",
    "item_id",
    "condition",
    "trade_group_type",
    "commerce_type",
    "is_sell_to_npc",
    "territory_supply_no",
    "territory_trade_no",
    "is_for_magnate",
    "trade_type",
    "price_type",
    "name",
    "item_name",
    "icon_path",
    "commerce_type_name",
    "trade_group_text",
]


def _case(name: str, required_keys: list[str]) -> HandlerCase:
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file="languagedata_en.loc",
        uses_loc=False,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{name}",
        tests=[SchemaTest(required_keys=required_keys), DeclaredCountTest(declared=header_count(offset=0))],
    )


CASES = {
    FILE_NAME: _case(FILE_NAME, _RECORD_KEYS),
    OFFSET_FILE: _case(OFFSET_FILE, ["character_id", "offset", "size"]),
}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in CASES.items() for spec in case.tests],
)
def test_itemtradegroupfromnpc_dbss(name: str, spec: Any) -> None:
    _result(name).check(spec)


# Offsets after the condition string, from the Item Entry table.
_TRADE_GROUP_TYPE = 0x28
_TERRITORY_SUPPLY_NO = 0x5D
_TERRITORY_TRADE_NO = 0x5F
_IS_FOR_MAGNATE = 0x69
_TRADE_TYPE = 0x6A
_COMMERCE_TYPE = 0x6B
_TAIL_SIZE = 0x6D


def _entry(
    character_id: int,
    item_id: int,
    commerce_type: int,
    condition: str = "",
    trade_type: int = 0,
    territory_trade_no: int = 0,
) -> bytes:
    encoded = condition.encode("utf-16-le")
    tail = bytearray(_TAIL_SIZE)
    tail[_TRADE_GROUP_TYPE] = 3
    struct.pack_into("<H", tail, _TERRITORY_SUPPLY_NO, 515)
    struct.pack_into("<H", tail, _TERRITORY_TRADE_NO, territory_trade_no)
    tail[_IS_FOR_MAGNATE] = 1 if territory_trade_no else 0
    tail[_TRADE_TYPE] = trade_type
    tail[_COMMERCE_TYPE] = commerce_type
    return struct.pack("<HIQ", character_id, item_id, len(encoded) // 2) + encoded + bytes(tail)


def _group(character_id: int, *entries: bytes) -> bytes:
    return GROUP_HEADER.pack(character_id, len(entries)) + b"".join(entries)


def _table(*groups: bytes) -> bytes:
    return struct.pack("<I", len(groups)) + b"".join(groups)


def test_layout_1_entries_read_back() -> None:
    data = _table(
        _group(47092, _entry(47092, 55097, 1, "getlifeLevel(7)>41", 2)),
        _group(44020, _entry(44020, 55646, 6, territory_trade_no=301), _entry(44020, 55647, 6)),
    )
    records = parse_itemtradegroupfromnpc_records(data)
    assert [(r["character_id"], r["item_id"], r["condition"], r["commerce_type"], r["trade_type"]) for r in records] == [
        (47092, 55097, "getlifeLevel(7)>41", 1, 2),
        (44020, 55646, "", 6, 0),
        (44020, 55647, "", 6, 0),
    ]
    assert [(r["territory_trade_no"], r["is_for_magnate"]) for r in records] == [(0, 0), (301, 1), (0, 0)]
    assert {(r["trade_group_type"], r["territory_supply_no"], r["is_sell_to_npc"]) for r in records} == {(3, 515, 0)}


def test_an_empty_group_reads_back() -> None:
    assert parse_itemtradegroupfromnpc_records(_table(_group(40010))) == []


@pytest.mark.parametrize(
    "data",
    [
        b"",
        _table(_group(40010, _entry(40010, 810442, 2)))[:-1],
        _table(_group(40010, _entry(40010, 810442, 2))) + b"\x00",
        _table(_group(40010, _entry(40026, 810444, 4))),
        struct.pack("<I", 1),
    ],
    ids=["no_count", "short_entry", "trailing_bytes", "entry_of_another_character", "missing_group"],
)
def test_a_broken_table_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_itemtradegroupfromnpc_records(data)
