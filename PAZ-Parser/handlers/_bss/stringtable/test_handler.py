from __future__ import annotations

import struct
from collections import defaultdict
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _bss.stringtable.parser import SHEET_LOC_ID2, parse_sheet_hashes
from _common.pabr_strings import string_table_start
from _common.string_hash import key_hash


_SHEET_HEADER_SIZE = 12
_ROW_SIZE = 16
# PABR magic and the u32 sheet count.
_FILE_HEADER_SIZE = 8


def _sheet_rows(source: CaseInput) -> int:
    """String rows between the sheet headers and the string table the trailer points at."""
    (sheet_count,) = struct.unpack_from("<I", source.data, 4)
    rows_size = string_table_start(source.data) - _FILE_HEADER_SIZE - sheet_count * _SHEET_HEADER_SIZE
    if rows_size < 0 or rows_size % _ROW_SIZE:
        raise AssertionError(f"{rows_size} bytes of sheet rows are not whole {_ROW_SIZE}-byte rows")
    return rows_size // _ROW_SIZE


CASE = HandlerCase(
    handler_name="stringtable.bss",
    data_file="stringtable.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["text"],
    internal_path="gamecommondata/binary/stringtable.bss",
    tests=[
        SchemaTest(required_keys=["sheet", "key_hash", "key", "korean", "text"]),
        DeclaredCountTest(declared=_sheet_rows),
        # UI strings colour names and values, in LOC and in the Korean fallback.
        PaFieldTest(field="text"),
        # The Storage town NPC navigation label (stringtable_bss.md).
        TargetTest(
            col="key",
            value="LUA_WIDGET_TOWNNPCNAVI_NPCTYPETEXT_6",
            expected={"sheet": "GAME", "key_hash": 0x4D282741, "text": "Storage"},
        ),
        # Only has the LOC str_id3 = 1 variant.
        TargetTest(
            col="key",
            value="LUA_LIFEEQUIPMENT_TOOLTIP_MARBLE",
            expected={"sheet": "GAME", "text": "Orb"},
        ),
    ],
)


@pytest.fixture(scope="module")
def stringtable_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_stringtable_bss(spec: Any, stringtable_result: HandlerResult) -> None:
    stringtable_result.check(spec)


def test_every_sheet_has_a_loc_id2(stringtable_result: HandlerResult) -> None:
    sheets = {record["sheet"] for record in stringtable_result.records}

    assert sheets <= SHEET_LOC_ID2.keys(), sheets - SHEET_LOC_ID2.keys()


def test_keys_are_unique_per_sheet_and_hash_alike_across_sheets(
    stringtable_result: HandlerResult,
) -> None:
    hashes_by_key: dict[str, set[int]] = defaultdict(set)
    seen: set[tuple[str, str]] = set()
    for record in stringtable_result.records:
        sheet_key = (record["sheet"], record["key"])
        assert sheet_key not in seen, sheet_key
        seen.add(sheet_key)
        hashes_by_key[record["key"]].add(record["key_hash"])

    assert not {key for key, hashes in hashes_by_key.items() if len(hashes) > 1}


def test_records_follow_the_hash_order(stringtable_result: HandlerResult) -> None:
    hashes = [record["key_hash"] for record in stringtable_result.records]

    assert hashes == sorted(hashes)


def test_every_row_has_a_key(stringtable_result: HandlerResult) -> None:
    assert all(record["key"] for record in stringtable_result.records)


def test_every_key_hash_is_the_key_hash_of_its_key(stringtable_result: HandlerResult) -> None:
    """lookup3 over the UTF-16LE key with seed 0xC5EDE (`_common/string_hash.py`)."""
    for record in stringtable_result.records:
        assert key_hash(record["key"]) == record["key_hash"], record["key"]


def test_every_sheet_hash_is_the_key_hash_of_its_name(stringtable_result: HandlerResult) -> None:
    for name, sheet_hash in parse_sheet_hashes(stringtable_result.source.data).items():
        assert key_hash(name) == sheet_hash, name
