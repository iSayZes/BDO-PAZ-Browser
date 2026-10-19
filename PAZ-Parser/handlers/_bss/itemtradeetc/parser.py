"""`itemtradeetc.bss`: the desert trade buff per pair of trade group types.

    PABR | u32 group_count | group_count x group
    | u32 row_count | row_count x 12-byte row
    | string table (count 0) | u32 table_start | u32 0
    group: u8 from_group | u32 pair_count | pair_count x 10-byte pair
    pair:  u8 from_group | u8 to_group | f32 distance | u32 add_rate
    row:   i64 accumulated_advantage | u32 discount_rate

The trade group types are the codes of `itemtradegrouptonpc.dbss`
`trade_group_type`. Full layout in docs/file-formats/itemtradeetc_bss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start, read_string_table
from _common.record_reader import RecordReader


FILE_NAME = "itemtradeetc.bss"

GROUP_HEADER = struct.Struct("<BI")
PAIR = struct.Struct("<BBfI")
COUNT = struct.Struct("<I")
ROW = struct.Struct("<qI")


class ItemTradeEtc(NamedTuple):
    pairs: list[dict]
    rows: list[dict]


def parse_itemtradeetc(data: bytes) -> ItemTradeEtc:
    """The group pairs in file order, then the unknown 12-byte rows.

    Raises ValueError on a bad magic, a pair whose from group differs from its
    group's, a group or row running past the string table, rows that do not
    end where the string table starts, or a string table that is broken or
    holds strings (no field points into it, so strings mean a changed layout).
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    if strings:
        raise ValueError(f"{FILE_NAME} string table holds {len(strings)} strings, expected none")
    reader = RecordReader(data, HEADER_SIZE, table_start, FILE_NAME)
    pairs: list[dict] = []
    for _ in range(u32(data, 4)):
        from_group, pair_count = reader.unpack(GROUP_HEADER)
        pairs.extend(_read_pair(reader, from_group) for _ in range(pair_count))

    (row_count,) = reader.unpack(COUNT)
    rows = [_read_row(reader) for _ in range(row_count)]
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return ItemTradeEtc(pairs, rows)


def _read_pair(reader: RecordReader, group_from: int) -> dict:
    from_group, to_group, distance, add_rate = reader.unpack(PAIR)
    if from_group != group_from:
        raise ValueError(f"{FILE_NAME} pair {from_group} -> {to_group} sits in group {group_from}")
    return {
        "from_group": from_group,
        "to_group": to_group,
        "distance": distance,
        "add_rate": add_rate,
    }


def _read_row(reader: RecordReader) -> dict:
    accumulated_advantage, discount_rate = reader.unpack(ROW)
    return {"accumulated_advantage": accumulated_advantage, "discount_rate": discount_rate}
