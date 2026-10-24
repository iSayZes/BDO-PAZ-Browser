"""`cutscene.dbss`: the name and place of every `.pas` cutscene, keyed by file name hash.

    u32 count | count x (u32 key_prefix | row)
    row: u32 cutscene_key | str16 file_name | str16 cutscene_name_kr
         | str16 description_kr | u32 unknown_description_00

`cutscene_key` is `key_hash()` of `file_name`, and `key_prefix` repeats it.
`cutsceneoffset.dbss` (u32 count, then u32 key, u32 offset and u32 size per
row, no PABR magic) points past the key prefix. Layout 1 in
docs/file-formats/cutscene_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "cutscene.dbss"
OFFSET_FILE = "cutsceneoffset.dbss"
KEY_FIELD = "cutscene_key"

_HEAD = struct.Struct("<II")
_U32 = struct.Struct("<I")


def _read_row(reader: RecordReader) -> dict:
    key_prefix, cutscene_key = reader.unpack(_HEAD)
    if key_prefix != cutscene_key:
        raise ValueError(f"{FILE_NAME} row 0x{cutscene_key:08X} follows the key prefix 0x{key_prefix:08X}")
    file_name = reader.text(wide=True)
    cutscene_name_kr = reader.text(wide=True)
    description_kr = reader.text(wide=True)
    (unknown_description_00,) = reader.unpack(_U32)
    return {
        KEY_FIELD: cutscene_key,
        "file_name": file_name,
        "cutscene_name_kr": cutscene_name_kr,
        "description_kr": description_kr,
        "unknown_description_00": unknown_description_00,
    }


def parse_cutscene_records(data: bytes) -> list[dict]:
    """Every cutscene in file order.

    Raises ValueError when a row runs past the file, its key prefix differs
    from its key, or the rows end before the last byte.
    """
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_cutsceneoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: cutscene key, row offset and row size. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)
