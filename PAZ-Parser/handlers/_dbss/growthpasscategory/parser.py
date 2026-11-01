"""`growthpasscategory.dbss`: the tabs of the Growth Pass window.

    u32 record_count | record_count x (u32 category_key | record body)

    record body: u32 category_key | name (UTF-16) | icon texture key (ASCII)
                 | u16 quest_chain_id | 20 zero bytes

Both strings carry a u64 length prefix (`RecordReader.text`).
`growthpasscategoryoffset.dbss` (no magic, u32 keys) points at each body.
Full layout in docs/file-formats/dbss/growthpasscategory_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader


_KEY_SIZE = 4
_U32 = struct.Struct("<I")
_U16 = struct.Struct("<H")
_TAIL_SIZE = 20


@dataclass(frozen=True)
class GrowthPassCategory:
    category_key: int
    name_kr: str
    icon_texture: str
    quest_chain_id: int


def parse_growthpasscategory_records(data: bytes, offset_data: bytes) -> list[GrowthPassCategory]:
    """Every category in offset table order.

    Raises ValueError when a record does not match its offset row.
    """
    return [_read_category(data, row) for row in parse_bare_u32_offset_rows(offset_data)]


def _read_category(data: bytes, row: PabrOffsetRow) -> GrowthPassCategory:
    start, end = row.offset, row.offset + row.size
    if start < _KEY_SIZE or end > len(data):
        raise ValueError(f"category {row.entry_id} runs past the file")

    if u32(data, start - _KEY_SIZE) != row.entry_id:
        raise ValueError(f"category {row.entry_id}: key copy before 0x{start:X} does not match")

    reader = RecordReader(data, start, end, f"category {row.entry_id}")
    (key,) = reader.unpack(_U32)
    if key != row.entry_id:
        raise ValueError(f"category {row.entry_id}: record key {key} does not match")
    name_kr = reader.text(wide=True)
    icon_texture = reader.text(wide=False)
    (quest_chain_id,) = reader.unpack(_U16)
    reader.skip(_TAIL_SIZE)
    if not reader.at_end():
        raise ValueError(f"category {row.entry_id}: {reader.remaining()} bytes left after the record")

    return GrowthPassCategory(row.entry_id, name_kr, icon_texture, quest_chain_id)
