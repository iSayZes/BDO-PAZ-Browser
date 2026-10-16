"""textbind.dbss: the Korean text of every TextBind name, four variants each.

Records follow the u32 count back to back in file order: a u32 key (the
`key_hash()` of the TextBind name, LOC type 59 `str_id1`), variants 0 to 2 as
u64-prefixed UTF-16LE strings, a u32 that is 0 on every record, then
variant 3 (docs/file-formats/textbind_dbss.md).
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader

VARIANT_COUNT = 4
# Variant 0 is the PC text (docs/file-formats/textbind_dbss.md, Variants).
PC_VARIANT = 0
_COUNT_SIZE = 4
_U32 = struct.Struct("<I")
# The always-0 u32 sits before this variant.
_UNKNOWN_BEFORE_VARIANT = 3


@dataclass(frozen=True)
class TextBindRecord:
    key: int
    variants: tuple[str, ...]
    unknown_pre_variant_3: int


def parse_textbind_records(data: bytes) -> list[TextBindRecord]:
    """Every record in file order. Raises ValueError when a record runs past the file."""
    count = u32(data, 0)
    reader = RecordReader(data, _COUNT_SIZE, len(data), "textbind.dbss")
    return [_read_record(reader) for _ in range(count)]


def _read_record(reader: RecordReader) -> TextBindRecord:
    (key,) = reader.unpack(_U32)
    variants: list[str] = []
    unknown = 0
    for variant in range(VARIANT_COUNT):
        if variant == _UNKNOWN_BEFORE_VARIANT:
            (unknown,) = reader.unpack(_U32)
        variants.append(reader.text(wide=True))
    return TextBindRecord(key, tuple(variants), unknown)


def parse_textbind_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    """textbindoffset.dbss: a bare u32 count, then u32 key, offset and size rows."""
    return parse_bare_u32_offset_rows(data)


def build_text_bind_kr_index(data: bytes) -> dict[int, str]:
    """Korean PC text by key hash, for `IndexKind.TEXT_BIND_KR`.

    `resolve_text_binds()` falls back to it when LOC type 59 has no text.
    """
    return {record.key: record.variants[PC_VARIANT] for record in parse_textbind_records(data)}
