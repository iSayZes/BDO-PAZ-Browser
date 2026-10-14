from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCount,
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

from _bss.stringtable.parser import parse_key_hashes
from _common.pabr_offset import parse_bare_offset_rows
from .commerce_types import COMMERCE_TYPES, KEY_HASHES, RESOURCE_SHEET
from .parser import (
    ENTRY_SIZE,
    FILE_NAME,
    GROUP_HEADER,
    OFFSET_FILE,
    parse_itemtradegrouptonpc_records,
)


# Bahar <Trade Manager> in Velia.
_BAHAR = 40010
_MUDSKIPPER = 8201
_SEAFOOD = 8
_COUNT_OFFSET = 0


def _offset_entries(companion: str) -> DeclaredCount:
    """Item entries the offset table declares: each group's size minus its header, in entries."""

    def read(source: CaseInput) -> int:
        total = 0
        for row in parse_bare_offset_rows(source.file(companion)):
            body = row.size - GROUP_HEADER.size
            if body < 0 or body % ENTRY_SIZE:
                raise AssertionError(f"group {row.entry_id} is {row.size} bytes, not whole {ENTRY_SIZE}-byte entries")
            total += body // ENTRY_SIZE
        return total

    return read


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={OFFSET_FILE: OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "item_name", "commerce_type_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_id",
                "name",
                "item_id",
                "item_name",
                "icon_path",
                "commerce_type",
                "commerce_type_name",
                "trade_group_type",
                "unknown_37",
                "unknown_6b",
                "unknown_7c",
            ]
        ),
        DeclaredCountTest(declared=_offset_entries(OFFSET_FILE)),
        RangeTest(col="commerce_type", min_val=min(COMMERCE_TYPES), max_val=max(COMMERCE_TYPES)),
        TargetTest(col="character_id", value=_BAHAR, expected={"character_id": _BAHAR, "name": "Bahar"}),
        # A fish is Seafood in the item tooltip.
        TargetTest(
            col="item_id",
            value=_MUDSKIPPER,
            expected={"item_name": "Mudskipper", "commerce_type": _SEAFOOD, "commerce_type_name": "Seafood"},
        ),
        UserLanguageTest(fields=["name", "item_name", "commerce_type_name"]),
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
        TargetTest(col="character_id", value=_BAHAR, expected={"character_id": _BAHAR}),
    ],
)


@pytest.fixture(scope="module")
def trade_group_result(request: Any) -> HandlerResult:
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
def test_itemtradegrouptonpc_dbss(spec: Any, trade_group_result: HandlerResult) -> None:
    trade_group_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemtradegrouptonpcoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_group_count_matches_the_offset_table() -> None:
    data = load_binary_fixture(FILE_NAME)
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert struct.unpack_from("<I", data, _COUNT_OFFSET)[0] == len(rows)


def test_every_offset_row_points_at_its_group() -> None:
    data = load_binary_fixture(FILE_NAME)
    for row in parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE)):
        character_id, item_count = GROUP_HEADER.unpack_from(data, row.offset)
        assert character_id == row.entry_id
        assert row.size == GROUP_HEADER.size + item_count * ENTRY_SIZE


def test_commerce_type_hashes_match_stringtable() -> None:
    hashes = parse_key_hashes(load_binary_fixture("stringtable.bss"), RESOURCE_SHEET)
    wrong = {
        key: (key_hash, hashes.get(key))
        for key, key_hash in KEY_HASHES[RESOURCE_SHEET].items()
        if hashes.get(key) != key_hash
    }
    assert not wrong, f"category name hashes differ from stringtable.bss (stored, file): {wrong}"


def _entry(character_id: int, item_id: int, commerce_type: int) -> bytes:
    entry = bytearray(ENTRY_SIZE)
    struct.pack_into("<HI", entry, 0, character_id, item_id)
    entry[0x37] = 1
    entry[0x7D] = commerce_type
    return bytes(entry)


def _group(character_id: int, *entries: bytes) -> bytes:
    return GROUP_HEADER.pack(character_id, len(entries)) + b"".join(entries)


def _table(*groups: bytes) -> bytes:
    return struct.pack("<I", len(groups)) + b"".join(groups)


def test_a_small_table_reads_back() -> None:
    data = _table(
        _group(40010, _entry(40010, 810442, 2)),
        _group(40075, _entry(40075, 8201, 8), _entry(40075, 55001, 6)),
    )
    records = parse_itemtradegrouptonpc_records(data)
    assert [(r["character_id"], r["item_id"], r["commerce_type"], r["unknown_37"]) for r in records] == [
        (40010, 810442, 2, 1),
        (40075, 8201, 8, 1),
        (40075, 55001, 6, 1),
    ]


def test_an_empty_group_reads_back() -> None:
    assert parse_itemtradegrouptonpc_records(_table(_group(40010))) == []


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
        parse_itemtradegrouptonpc_records(data)


def test_every_trade_group_code_has_a_label(trade_group_result: HandlerResult) -> None:
    """A code the labels in `_common/lang/` lack would show as a bare number."""
    bare = {
        record["trade_group_type"]
        for record in trade_group_result.records
        if record["trade_group_text"] == str(record["trade_group_type"])
    }

    assert not bare, f"trade group codes without a label: {sorted(bare)}"
