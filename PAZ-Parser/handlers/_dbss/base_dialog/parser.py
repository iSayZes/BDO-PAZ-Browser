"""`base_dialog.dbss`: the base record of every NPC dialog.

`base_dialogoffset.dbss` has the layout and keys of `detail_dialogoffset.dbss`
(`dialog_index << 16 | character_id`). Records tile the data file from byte 4:

    u32 key | utf16 name_kr | u32 n + n x utf16 line | u8[5] reserved

Strings are a u64 UTF-16 code-unit count plus UTF-16LE text. Full layout in
docs/file-formats/dbss/base_dialog_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.record_reader import RecordReader
from _dbss.detail_dialog.parser import split_key

_U32 = struct.Struct("<I")
_RESERVED_SIZE = 5


@dataclass(frozen=True)
class BaseDialogRecord:
    key: int
    name_kr: str
    lines: tuple[str, ...]

    @property
    def character_id(self) -> int:
        return split_key(self.key)[0]

    @property
    def dialog_index(self) -> int:
        return split_key(self.key)[1]


def parse_base_dialog_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row in file order; `entry_id` is the dialog key."""
    return parse_pabr_u32_offset_rows(data)


def parse_base_dialog_record(data: bytes, row: PabrOffsetRow) -> BaseDialogRecord:
    """Walk one record. Raises ValueError when it does not end at its index size."""
    label = f"base dialog 0x{row.entry_id:08X}"
    reader = RecordReader(data, row.offset, row.offset + row.size, label)
    (key,) = reader.unpack(_U32)
    if key != row.entry_id:
        raise ValueError(f"record at 0x{row.offset:X} holds key 0x{key:08X}, index says 0x{row.entry_id:08X}")

    name_kr = reader.text(wide=True)
    (line_count,) = reader.unpack(_U32)
    lines = tuple(reader.text(wide=True) for _ in range(line_count))
    reader.skip(_RESERVED_SIZE)
    if not reader.at_end():
        raise ValueError(f"{label} ends {reader.remaining()} bytes before its index size")
    return BaseDialogRecord(key=key, name_kr=name_kr, lines=lines)


def parse_base_dialog_records(data: bytes, offset_data: bytes) -> list[BaseDialogRecord]:
    """One record per index row, in index order.

    Raises ValueError on the first record that does not end exactly at its
    index size: the layout has changed and later fields would be misread.
    """
    return [parse_base_dialog_record(data, row) for row in parse_base_dialog_offset_rows(offset_data)]
