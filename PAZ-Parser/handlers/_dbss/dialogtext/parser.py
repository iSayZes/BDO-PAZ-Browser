"""`dialogtext.dbss`: named pools of NPC lines for `{GetRandomText(<name>)}`.

`dialogtextoffset.dbss` is a bare u32 count and 12-byte rows (`u32 key`,
`u32 offset`, `u32 size`), with no magic and no trailer. In the data file every
record is preceded by a copy of its key, and walks as:

    u32 key | utf16 name | u32 n + n x (u16 text_id, utf16 text) | u32 0

Strings are a u64 UTF-16 code-unit count plus UTF-16LE text. The lines are
localized in LOC type 36, keyed `(key, text_id, 0, 0)`. Full layout in
docs/file-formats/dbss/dialogtext_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader

_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")


@dataclass(frozen=True)
class DialogTextLine:
    text_id: int
    text: str


@dataclass(frozen=True)
class DialogTextPool:
    key: int
    name: str
    lines: tuple[DialogTextLine, ...]


def parse_dialogtext_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row in file order; `entry_id` is the pool key."""
    return parse_bare_u32_offset_rows(data)


def _read_line(reader: RecordReader) -> DialogTextLine:
    (text_id,) = reader.unpack(_U16)
    return DialogTextLine(text_id, reader.text(wide=True))


def parse_dialogtext_record(data: bytes, row: PabrOffsetRow) -> DialogTextPool:
    """Walk one record. Raises ValueError when it does not end at its index size."""
    label = f"dialog text 0x{row.entry_id:08X}"
    reader = RecordReader(data, row.offset, row.offset + row.size, label)
    (key,) = reader.unpack(_U32)
    if key != row.entry_id:
        raise ValueError(f"record at 0x{row.offset:X} holds key 0x{key:08X}, index says 0x{row.entry_id:08X}")

    name = reader.text(wide=True)
    (line_count,) = reader.unpack(_U32)
    lines = tuple(_read_line(reader) for _ in range(line_count))
    reader.skip(_U32.size)  # always 0
    if not reader.at_end():
        raise ValueError(f"{label} ends {reader.remaining()} bytes before its index size")
    return DialogTextPool(key=key, name=name, lines=lines)


def parse_dialogtext_records(data: bytes, offset_data: bytes) -> list[DialogTextPool]:
    """One pool per index row, in index order.

    Raises ValueError on the first record that does not end exactly at its
    index size: the layout has changed and later fields would be misread.
    """
    return [parse_dialogtext_record(data, row) for row in parse_dialogtext_offset_rows(offset_data)]
