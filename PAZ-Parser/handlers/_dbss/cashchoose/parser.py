"""`cashchoose.dbss`: the Pearl Shop choice packs, the products a buyer picks from.

    u32 count | count x row
    row: u16 choose_key | u32 choose_count | u8 is_choose_duplicate
         | u32[10] include_product_no | u64[10] stack_count
         | str8 display_icon_path | u32 choose_cash_count

`cashchooseoffset.dbss` (u32 count, then u16 key, u32 offset and u32 size per
row, no PABR magic) points at the row start. Layout 3 in
docs/file-formats/cashchoose_dbss.md; older rows have no
`display_icon_path` (Layout 2) and u16 product IDs (Layout 1).
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "cashchoose.dbss"
OFFSET_FILE = "cashchooseoffset.dbss"
KEY_FIELD = "choose_key"
# Product slots per pack: IncludeProductNo0 to IncludeProductNo9.
PRODUCT_SLOTS = 10

_HEAD = struct.Struct("<HIB")
_PRODUCTS = struct.Struct(f"<{PRODUCT_SLOTS}I")
_STACKS = struct.Struct(f"<{PRODUCT_SLOTS}Q")
_U32 = struct.Struct("<I")


def _read_row(reader: RecordReader) -> dict:
    choose_key, choose_count, is_choose_duplicate = reader.unpack(_HEAD)
    include_product_no = list(reader.unpack(_PRODUCTS))
    stack_count = list(reader.unpack(_STACKS))
    display_icon_path = reader.text(wide=False)
    (choose_cash_count,) = reader.unpack(_U32)
    return {
        KEY_FIELD: choose_key,
        "choose_count": choose_count,
        "is_choose_duplicate": is_choose_duplicate,
        "include_product_no": include_product_no,
        "stack_count": stack_count,
        "display_icon_path": display_icon_path,
        "choose_cash_count": choose_cash_count,
    }


def parse_cashchoose_records(data: bytes) -> list[dict]:
    """Every choice pack in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_cashchooseoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: choose key, row offset and row size. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
