"""`cashitemmarketsetting.dbss`: the Central Market price settings of Pearl Shop items.

A `PABR` table of 46-byte rows with an empty string table:

    u32 item_id | u64 base_price_for_item_market | u64 its copy
    | u32 maxest_percent_for_item_market | u32 its copy
    | u32 minest_percent_for_item_market | u32 its copy
    | u16 max_register_count_for_item_market | u16 its copy | bytes[6] unknown_28

`cashitemmarketsettingoffset.dbss` (the `PABR` u32 index of `skilloffset.dbss`)
points 4 bytes into each row, past its `item_id`, and stores size `0`; reading
the rows in order needs no index. Layout in
docs/file-formats/cashitemmarketsetting_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "cashitemmarketsetting.dbss"
OFFSET_FILE = "cashitemmarketsettingoffset.dbss"
KEY_FIELD = "item_id"

_ROW = struct.Struct("<IQQIIIIHH6s")
ROW_SIZE = _ROW.size

_FIELDS = (
    KEY_FIELD,
    "base_price_for_item_market",
    "base_price_for_item_market_dup",
    "maxest_percent_for_item_market",
    "maxest_percent_for_item_market_dup",
    "minest_percent_for_item_market",
    "minest_percent_for_item_market_dup",
    "max_register_count_for_item_market",
    "max_register_count_for_item_market_dup",
)


def _record(values: tuple) -> dict:
    *numbers, unknown_28 = values
    return {**dict(zip(_FIELDS, numbers, strict=True)), "unknown_28": unknown_28.hex()}


def parse_cashitemmarketsetting_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    return [_record(_ROW.unpack_from(data, start)) for start in fixed_row_offsets(data, ROW_SIZE, FILE_NAME)]


def parse_cashitemmarketsettingoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: item ID, the offset just past the row's `item_id`, and size `0`.

    Raises ValueError on a missing magic or a count the file cannot hold.
    """
    return parse_pabr_u32_offset_rows(data)
