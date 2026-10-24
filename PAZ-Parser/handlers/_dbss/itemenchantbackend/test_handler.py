"""itemenchantbackend.dbss and its index.

The index is a 2 MB fixture and runs as a handler case. The 127 MB table
stays out of the shared fixture folder: `tests/itemenchant_split.py` cuts
the blocks of a few items from the cached itemenchant.dbss and keeps the
part the index sizes, and the tests read those. `check_docs.py` walks the
whole live file.
"""
from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from bdo_models import PazEntry
from bdo_preview import get_handler
from tests.empty_cells import assert_empty_cells_sort_last
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
from tests.itemenchant_split import ITEM_ENCHANT_OFFSET_FILE, SplitFiles, offset_rows, pabr_offset, split_files
from tests.offset_rows import offset_row_problems

from _common.pabr_offset import PabrOffsetRow
from _dbss.itemenchant.parser import parse_itemenchant_records
from .parser import FILE_NAME, KEY_FROM_END, OFFSET_FILE, parse_itemenchantbackend_records


# Kzarka Gauntlet enhances to PEN (level 20); Ancient Spirit's Crystal -
# Viper is in jewelgroupstaticstatus.bss group 101 (itemenchant_dbss.md).
_KZARKA_GAUNTLET = 11210
_PEN = 20
_ANCIENT_SPIRIT_VIPER = 15653
_ANCIENT_SPIRIT_GROUP = 101
_OQUILLA_SAIL_BALANCE = 607887
_ITEMS = (_KZARKA_GAUNTLET, _ANCIENT_SPIRIT_VIPER, _OQUILLA_SAIL_BALANCE)
# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
_KEY = struct.Struct("<I")
_ENTRY = PazEntry("", f"gamecommondata/binary/{FILE_NAME}", 0, 0, 0, 0, 0)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["key", "item_id", "enchant_level", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="key",
            value=_PEN << 24 | _KZARKA_GAUNTLET,
            expected={"item_id": _KZARKA_GAUNTLET, "enchant_level": _PEN},
        ),
    ],
)


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemenchantbackendoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_index_holds_the_keys_of_itemenchantoffset_in_its_order() -> None:
    back_keys = [row.entry_id for row in offset_rows(OFFSET_FILE)]

    assert back_keys == [row.entry_id for row in offset_rows(ITEM_ENCHANT_OFFSET_FILE)]


@pytest.fixture(scope="module")
def files() -> SplitFiles:
    return split_files(_ITEMS)


def test_blocks_tile_the_file_and_end_with_their_key(files: SplitFiles) -> None:
    assert offset_row_problems(files.back, files.back_rows, _KEY, key_from_end=KEY_FROM_END) == []


def test_records_hold_the_itemenchant_crystal_group(files: SplitFiles) -> None:
    whole = parse_itemenchant_records(files.item_enchant, files.item_enchant_offset)
    back = parse_itemenchantbackend_records(files.back, files.back_offset)

    assert [(record["item_id"], record["crystal_group"]) for record in back] == [
        (record["item_id"], record["crystal_group"]) for record in whole
    ]
    by_item = {record["item_id"]: record for record in back}
    assert by_item[_ANCIENT_SPIRIT_VIPER]["crystal_group"] == _ANCIENT_SPIRIT_GROUP
    assert by_item[_KZARKA_GAUNTLET]["max_enchant_level"] == _PEN


def test_a_block_that_ends_with_another_key_fails(files: SplitFiles) -> None:
    # The base block of Kzarka Gauntlet, one byte short.
    shifted = pabr_offset(
        PabrOffsetRow(row.entry_id, row.offset, row.size - 1) if row.entry_id == _KZARKA_GAUNTLET else row
        for row in files.back_rows
    )

    with pytest.raises(ValueError, match="ends with key"):
        parse_itemenchantbackend_records(files.back, shifted)


def test_view_shows_one_row_per_item(files: SplitFiles) -> None:
    handler = get_handler(FILE_NAME, ".dbss")
    records = handler.get_records(files.back, _ENTRY, {OFFSET_FILE: files.back_offset})

    assert f"gamecommondata/binary/{OFFSET_FILE}" in handler.companions(_ENTRY)
    assert {record["item_id"] for record in records} == set(_ITEMS)
    assert_empty_cells_sort_last(handler, records)
