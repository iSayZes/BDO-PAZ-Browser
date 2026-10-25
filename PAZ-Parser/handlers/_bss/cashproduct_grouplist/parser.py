"""`cashproduct_grouplist.bss`: the Pearl Shop products of each offer group.

    PABR | u32 row_count | row_count x row | string table | u32 table_start | u32 0
    row: u32 product_count | u32 offer_group | product_count x u32 product_nos

`offer_group` is the `OfferGroup` the products share; `product_nos` are
`cashproduct.dbss` product IDs. Layout 1 in
docs/file-formats/bss/cashproduct_grouplist_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "cashproduct_grouplist.bss"
KEY_FIELD = "offer_group"

_HEAD = struct.Struct("<II")
_U32_SIZE = 4


def _read_row(reader: RecordReader) -> dict:
    product_count, offer_group = reader.unpack(_HEAD)
    if product_count * _U32_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME} group {offer_group} declares {product_count:,} products past the rows")
    product_nos = list(reader.unpack(struct.Struct(f"<{product_count}I")))
    return {"product_count": product_count, KEY_FIELD: offer_group, "product_nos": product_nos}


def parse_cashproduct_grouplist_records(data: bytes) -> list[dict]:
    """Every offer group in file order.

    Raises ValueError on a bad PABR magic or trailer, or when the rows do not
    end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE, end, FILE_NAME)
    records = [_read_row(reader) for _ in range(u32(data, HEADER_SIZE - _U32_SIZE))]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} rows end at 0x{reader.pos:X}, the string table starts at 0x{end:X}")
    return records
