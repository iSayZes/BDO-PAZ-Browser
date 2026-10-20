"""`othertownnotmovableitem.bss`: items that cannot go into another town's storage.

A u32 count, then `count` u32 item IDs up to the end of the file; no magic and
no trailer. Layout in docs/file-formats/othertownnotmovableitem_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "othertownnotmovableitem.bss"

_COUNT_SIZE = 4
_ROW = struct.Struct("<I")


def parse_othertownnotmovableitem_records(data: bytes) -> list[dict]:
    """One record per item, in file order. Raises ValueError when the rows do not fill the file."""
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")
    count = u32(data, 0)
    if _COUNT_SIZE + count * _ROW.size != len(data):
        raise ValueError(f"{FILE_NAME} declares {count:,} rows but holds {len(data) - _COUNT_SIZE:,} row bytes")
    return [{"item_id": item_id} for (item_id,) in _ROW.iter_unpack(data[_COUNT_SIZE:])]
