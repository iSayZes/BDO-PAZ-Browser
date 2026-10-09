"""Offset companions: a row count, then [id][u32 offset][u32 size] rows.

Most `*offset.dbss` companions share one layout: ASCII `PABR`, a u32 row count,
`count` rows of [u16 id][u32 offset][u32 size], then a 12-byte trailer. Some,
such as `mentalcardoffset.dbss` and `detail_dialogoffset.dbss`, store a u32 ID
instead (`parse_pabr_u32_offset_rows`). A few, such as `petexpoffset.dbss`,
store the u16 layout with no magic and no trailer, and `dialogtextoffset.dbss`
the u32 layout that way (`parse_bare_u32_offset_rows`), and
`pcgrowthoffset.dbss` a u8 ID that way (`parse_bare_u8_offset_rows`). Whether `offset`
points at an inline copy of the ID or just past it differs per table, so
callers interpret the offset themselves.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32


PABR_MAGIC = b"PABR"

_COUNT_SIZE = 4
_ROW = struct.Struct("<HII")
_U32_ROW = struct.Struct("<III")
_U8_ROW = struct.Struct("<BII")


@dataclass(frozen=True)
class PabrOffsetRow:
    entry_id: int
    offset: int
    size: int


def parse_pabr_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Return every index row of a `PABR` offset table, in file order.

    Raises ValueError on a missing magic or a count the file cannot hold.
    """
    if len(data) < len(PABR_MAGIC) + _COUNT_SIZE or data[:4] != PABR_MAGIC:
        raise ValueError("offset table does not start with PABR magic")

    return _parse_rows(data, len(PABR_MAGIC), _ROW)


def parse_pabr_u32_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Return every index row of a `PABR` offset table keyed by a u32 ID.

    Raises ValueError on a missing magic or a count the file cannot hold.
    """
    if len(data) < len(PABR_MAGIC) + _COUNT_SIZE or data[:4] != PABR_MAGIC:
        raise ValueError("offset table does not start with PABR magic")

    return _parse_rows(data, len(PABR_MAGIC), _U32_ROW)


def parse_bare_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Return every index row of an offset table that opens with its count.

    Raises ValueError on a count the file cannot hold.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError("offset table is too short to hold its row count")

    return _parse_rows(data, 0, _ROW)


def parse_bare_u32_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Return every index row of a bare offset table keyed by a u32 ID.

    Raises ValueError on a count the file cannot hold.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError("offset table is too short to hold its row count")

    return _parse_rows(data, 0, _U32_ROW)


def parse_bare_u8_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Return every index row of a bare offset table keyed by a u8 ID.

    Raises ValueError on a count the file cannot hold.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError("offset table is too short to hold its row count")

    return _parse_rows(data, 0, _U8_ROW)


def _parse_rows(data: bytes, count_at: int, row: struct.Struct) -> list[PabrOffsetRow]:
    count = u32(data, count_at)
    rows_start = count_at + _COUNT_SIZE
    rows_end = rows_start + count * row.size
    if rows_end > len(data):
        raise ValueError(
            f"offset table declares {count:,} rows but only has room for "
            f"{(len(data) - rows_start) // row.size:,}"
        )

    return [
        PabrOffsetRow(entry_id, offset, size)
        for entry_id, offset, size in row.iter_unpack(data[rows_start:rows_end])
    ]
