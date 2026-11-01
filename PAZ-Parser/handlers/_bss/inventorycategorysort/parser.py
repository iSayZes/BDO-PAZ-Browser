"""`inventorycategorysort.bss`: the inventory categories of the category view, with their Korean names.

    u32 row_count | row_count x row
    row: u8 category_key | str16 name_kr | u8 unknown_name_kr_00
    | u8 category_key_dup

No PABR magic and no string table. Layout 1 in
docs/file-formats/bss/inventorycategorysort_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "inventorycategorysort.bss"
KEY_FIELD = "category_key"

_U8 = struct.Struct("<B")
_TAIL = struct.Struct("<BB")


def _read_row(reader: RecordReader) -> dict:
    (category_key,) = reader.unpack(_U8)
    name_kr = reader.text(wide=True)
    unknown_name_kr_00, category_key_dup = reader.unpack(_TAIL)
    return {
        KEY_FIELD: category_key,
        "name_kr": name_kr,
        "unknown_name_kr_00": unknown_name_kr_00,
        "category_key_dup": category_key_dup,
    }


def parse_inventorycategorysort_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when a row runs past the file or the rows end before it.
    """
    return read_counted_records(data, _read_row, FILE_NAME)
