"""itemenchantbackendtest.dbss, tested on blocks cut from the itemenchant.dbss fixture.

The 76 MB file stays out of the shared fixture folder: `tests/itemenchant_split.py`
cuts the blocks of a few items from the cached itemenchant.dbss and splits
them by the itemenchantbackendoffset.dbss sizes. The walk here finds each
block's end from its own lists and strings, so it checks the split point
against that index. `check_docs.py` walks the whole live file.
"""
from __future__ import annotations

import pytest

from bdo_models import PazEntry
from bdo_preview import get_handler
from tests.empty_cells import assert_empty_cells_sort_last
from tests.itemenchant_split import SplitFiles, split_files

from _dbss.itemenchant.parser import parse_itemenchant_records
from .parser import FILE_NAME, front_block_rows, parse_itemenchantbackendtest_records


# Kzarka Gauntlet (levels 0 to 20), an Oquilla sail with a non-empty
# `unknown_5d`, a crystal, Balacs Lunchbox (a skill key) and Marni's Stone
# (Bashim), a soul collector: the cases itemenchant_dbss.md documents.
_KZARKA_GAUNTLET = 11210
_OQUILLA_SAIL_BALANCE = 607887
_ANCIENT_SPIRIT_VIPER = 15653
_BALACS_LUNCHBOX = 9359
_MARNIS_STONE_BASHIM = 40351
_ITEMS = (_KZARKA_GAUNTLET, _OQUILLA_SAIL_BALANCE, _ANCIENT_SPIRIT_VIPER, _BALACS_LUNCHBOX, _MARNIS_STONE_BASHIM)
_PEN = 20
# Fields of the part of the block this file leaves out.
_BACK_FIELDS = ("crystal_group", "second_string", "block_size")
_ENTRY = PazEntry("", f"gamecommondata/binary/{FILE_NAME}", 0, 0, 0, 0, 0)


@pytest.fixture(scope="module")
def files() -> SplitFiles:
    return split_files(_ITEMS)


def test_walk_ends_each_block_where_the_backend_part_starts(files: SplitFiles) -> None:
    rows = front_block_rows(files.front)

    assert [row["key"] for row in rows] == [row.entry_id for row in files.whole_rows]
    assert [row["data_size"] for row in rows] == [
        whole.size - back.size for whole, back in zip(files.whole_rows, files.back_rows)
    ]


def test_records_are_the_itemenchant_records_without_the_back_part(files: SplitFiles) -> None:
    whole = parse_itemenchant_records(files.item_enchant, files.item_enchant_offset)
    front = parse_itemenchantbackendtest_records(files.front)

    assert {record["item_id"] for record in front} == set(_ITEMS)
    assert [{key: value for key, value in record.items() if key != "block_size"} for record in front] == [
        {key: value for key, value in record.items() if key not in _BACK_FIELDS} for record in whole
    ]
    gauntlet = next(record for record in front if record["item_id"] == _KZARKA_GAUNTLET)
    assert gauntlet["max_enchant_level"] == _PEN


@pytest.mark.parametrize("cut", [-1, 1], ids=["one byte short", "one byte over"])
def test_walk_fails_when_the_blocks_do_not_end_at_the_file_end(files: SplitFiles, cut: int) -> None:
    data = files.front[:cut] if cut < 0 else files.front + bytes(cut)

    with pytest.raises(ValueError, match=FILE_NAME):
        front_block_rows(data)


def test_view_is_the_itemenchant_view_without_the_crystal_group(files: SplitFiles) -> None:
    handler = get_handler(FILE_NAME, ".dbss")
    records = handler.get_records(files.front, _ENTRY, {})

    assert handler.companions(_ENTRY) == []
    assert "crystal_group_label" not in handler.sortable_fields()
    assert {record["item_id"] for record in records} == set(_ITEMS)
    assert_empty_cells_sort_last(handler, records)
