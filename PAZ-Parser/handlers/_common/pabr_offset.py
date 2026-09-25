"""PABR offset companions keyed by a u16 ID.

Several `*offset.dbss` companions share one layout: ASCII `PABR`, a u32 row
count, `count` rows of [u16 id][u32 offset][u32 size], then a 12-byte trailer.
Whether `offset` points at an inline copy of the ID or just past it differs per
table, so callers interpret the offset themselves.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32


PABR_MAGIC = b"PABR"

_HEADER_SIZE = 8
_ROW = struct.Struct("<HII")


@dataclass(frozen=True)
class PabrOffsetRow:
    entry_id: int
    offset: int
    size: int


def parse_pabr_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Return every index row, in file order.

    Raises ValueError on a missing magic or a count the file cannot hold.
    """
    if len(data) < _HEADER_SIZE or data[:4] != PABR_MAGIC:
        raise ValueError("offset table does not start with PABR magic")

    count = u32(data, 4)
    rows_end = _HEADER_SIZE + count * _ROW.size
    if rows_end > len(data):
        raise ValueError(
            f"offset table declares {count:,} rows but only has room for "
            f"{(len(data) - _HEADER_SIZE) // _ROW.size:,}"
        )

    return [
        PabrOffsetRow(entry_id, offset, size)
        for entry_id, offset, size in _ROW.iter_unpack(data[_HEADER_SIZE:rows_end])
    ]
