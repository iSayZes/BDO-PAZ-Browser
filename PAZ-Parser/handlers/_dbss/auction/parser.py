"""`auction.dbss`: the static auctions and the goods each one starts with.

    u32 count | count x Row
    Row:   u16 auction_no | u64 start_tick_count | u64 interval_tick_count
           | str16 desc_kr | u8 auction_type | u32 unknown_desc_kr_01
           | u32 house_count | house_count x (u16 character_key | i64 lower_price)
           | u32 item_count | item_count x Item | u32 unknown_items_00
    Item:  u32 item_key | i64 price | str16 exhibitor_kr | str16 description_kr
           | u32 unknown_description_kr_00

The rows follow each other with no gap, so the walk from the start needs no
index; `auctionoffset.dbss` points at each row's `auction_no`. Layout 2 in
docs/file-formats/auction_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "auction.dbss"
OFFSET_FILE = "auctionoffset.dbss"

_COUNT_SIZE = 4
# auction_no, start_tick_count, interval_tick_count
_HEAD = struct.Struct("<HQQ")
# auction_type, unknown_desc_kr_01, house_count
_TYPE = struct.Struct("<BII")
# character_key, lower_price
_HOUSE = struct.Struct("<Hq")
# item_key, price
_ITEM_HEAD = struct.Struct("<Iq")
_U32 = struct.Struct("<I")


def parse_auction_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when a row runs past the file or the rows do not end
    exactly at the end of the file.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    reader = RecordReader(data, _COUNT_SIZE, len(data), FILE_NAME)
    records = [_read_row(reader) for _ in range(u32(data, 0))]
    if not reader.at_end():
        raise ValueError(f"{len(records):,} rows end at 0x{reader.pos:X}, the file is {len(data):,} bytes")
    return records


def _read_row(reader: RecordReader) -> dict:
    auction_no, start_tick_count, interval_tick_count = reader.unpack(_HEAD)
    desc_kr = reader.text(wide=True)
    auction_type, unknown_desc_kr_01, house_count = reader.unpack(_TYPE)
    houses = [_read_house(reader) for _ in range(house_count)]
    (item_count,) = reader.unpack(_U32)
    items = [_read_item(reader) for _ in range(item_count)]
    (unknown_items_00,) = reader.unpack(_U32)
    return {
        "auction_no": auction_no,
        "auction_type": auction_type,
        "start_tick_count": start_tick_count,
        "interval_tick_count": interval_tick_count,
        "desc_kr": desc_kr,
        "unknown_desc_kr_01": unknown_desc_kr_01,
        "houses": houses,
        "items": items,
        "unknown_items_00": unknown_items_00,
    }


def _read_house(reader: RecordReader) -> dict:
    character_key, lower_price = reader.unpack(_HOUSE)
    return {"character_key": character_key, "lower_price": lower_price}


def _read_item(reader: RecordReader) -> dict:
    item_key, price = reader.unpack(_ITEM_HEAD)
    exhibitor_kr = reader.text(wide=True)
    description_kr = reader.text(wide=True)
    (unknown_description_kr_00,) = reader.unpack(_U32)
    return {
        "item_key": item_key,
        "price": price,
        "exhibitor_kr": exhibitor_kr,
        "description_kr": description_kr,
        "unknown_description_kr_00": unknown_description_kr_00,
    }
