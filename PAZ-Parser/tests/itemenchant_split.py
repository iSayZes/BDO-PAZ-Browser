"""Small itemenchant.dbss, itemenchantbackendtest.dbss and itemenchantbackend.dbss files cut from the fixtures.

The two split files are 76 MB and 127 MB, too big for the shared fixture
folder. Every itemenchant.dbss block is the itemenchantbackendtest.dbss block
of its key followed by the itemenchantbackend.dbss block
(itemenchantbackendtest_dbss.md), and the 2 MB itemenchantbackendoffset.dbss
gives the size of the second part. So the tests read the blocks of a few
items from the cached itemenchant.dbss, by seek, and split them by that size.
Load these inside a test or fixture: fetching a fixture can skip the test.
"""
from __future__ import annotations

import struct
from collections.abc import Collection, Iterable
from dataclasses import dataclass

from _common.item_key import split_item_key
from _common.pabr_offset import PABR_MAGIC, PabrOffsetRow, parse_pabr_u32_offset_rows

from .fixtures import FIXTURES_DIR, fetch_missing

ITEM_ENCHANT_FILE = "itemenchant.dbss"
ITEM_ENCHANT_OFFSET_FILE = "itemenchantoffset.dbss"
BACKEND_OFFSET_FILE = "itemenchantbackendoffset.dbss"

_COUNT = struct.Struct("<I")
_ROW = struct.Struct("<III")
# The PABR string table after the rows: no strings, the rows end, then 0.
_TRAILER = struct.Struct("<III")


@dataclass(frozen=True)
class SplitFiles:
    """The blocks of some items, as each of the three files stores them."""

    item_enchant: bytes
    item_enchant_offset: bytes
    front: bytes
    back: bytes
    back_offset: bytes
    # The itemenchantoffset.dbss and itemenchantbackendoffset.dbss sizes of each block, in file order.
    whole_rows: list[PabrOffsetRow]
    back_rows: list[PabrOffsetRow]


def offset_rows(name: str) -> list[PabrOffsetRow]:
    """The rows of a cached `*offset.dbss` fixture."""
    fetch_missing([name])
    return parse_pabr_u32_offset_rows((FIXTURES_DIR / name).read_bytes())


def pabr_offset(rows: Iterable[PabrOffsetRow]) -> bytes:
    """An `*offset.dbss` file holding `rows`."""
    body = b"".join(_ROW.pack(row.entry_id, row.offset, row.size) for row in rows)
    count = len(body) // _ROW.size
    rows_end = len(PABR_MAGIC) + _COUNT.size + len(body)
    return PABR_MAGIC + _COUNT.pack(count) + body + _TRAILER.pack(0, rows_end, 0)


def _counted(blocks: list[bytes]) -> tuple[bytes, list[int]]:
    """A u32 count and the blocks back to back, with where each block starts."""
    starts: list[int] = []
    pos = _COUNT.size
    for block in blocks:
        starts.append(pos)
        pos += len(block)
    return _COUNT.pack(len(blocks)) + b"".join(blocks), starts


def split_files(item_ids: Collection[int]) -> SplitFiles:
    """Every block of `item_ids`, in itemenchant.dbss order, as the three files store them."""
    fetch_missing([ITEM_ENCHANT_FILE])
    back_sizes = {row.entry_id: row.size for row in offset_rows(BACKEND_OFFSET_FILE)}
    rows = [row for row in offset_rows(ITEM_ENCHANT_OFFSET_FILE) if split_item_key(row.entry_id)[0] in item_ids]

    with (FIXTURES_DIR / ITEM_ENCHANT_FILE).open("rb") as source:
        blocks = []
        for row in rows:
            source.seek(row.offset)
            blocks.append(source.read(row.size))

    fronts = [block[: len(block) - back_sizes[row.entry_id]] for row, block in zip(rows, blocks)]
    backs = [block[len(block) - back_sizes[row.entry_id] :] for row, block in zip(rows, blocks)]
    whole, whole_starts = _counted(blocks)
    back, back_starts = _counted(backs)
    whole_rows = [PabrOffsetRow(row.entry_id, start, row.size) for row, start in zip(rows, whole_starts)]
    back_rows = [
        PabrOffsetRow(row.entry_id, start, len(block)) for row, start, block in zip(rows, back_starts, backs)
    ]
    return SplitFiles(
        item_enchant=whole,
        item_enchant_offset=pabr_offset(whole_rows),
        front=_counted(fronts)[0],
        back=back,
        back_offset=pabr_offset(back_rows),
        whole_rows=whole_rows,
        back_rows=back_rows,
    )
