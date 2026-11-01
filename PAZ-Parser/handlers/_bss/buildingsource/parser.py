"""`buildingsource.bss`: build time and repair materials of the guild building kits.

    PABR | u32 count | count x row | u32 unknown_after_rows | u32 0 | u32 table_start | u32 0

A row is the kit's u32 item key twice, a u16 `unknown_08`, a u32 build time,
a u8 work animation, three u64-counted lists (u32 repair item keys, i64
repair item counts, then after a u64 repair time the u32 repair percents)
and a u32 `unknown_repair_percents_00`. `unknown_after_rows` is `0` on
clients 1784 and 3474; the parser rejects any other value, since what would
follow it is unknown. Layout in docs/file-formats/bss/buildingsource_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start
from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "buildingsource.bss"
COUNT_OFFSET = 4

# item_key, item_key_dup, unknown_08, build_time, work_ani_type
_HEAD = struct.Struct("<IIHIB")
_COUNT = struct.Struct("<Q")
_U32 = struct.Struct("<I")
_I64 = struct.Struct("<q")
_REPAIR_TIME = struct.Struct("<Q")
_TAIL = struct.Struct("<I")


def parse_buildingsource_records(data: bytes) -> list[dict]:
    """Every building kit row, in file order.

    Raises ValueError on a bad magic or trailer, a row or list that runs past
    the string table, a non-zero `unknown_after_rows`, or rows that end
    before the string table.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    count = u32(data, COUNT_OFFSET)
    reader = RecordReader(data, HEADER_SIZE, rows_end, FILE_NAME)
    records = [_read_row(reader) for _ in range(count)]
    (after_rows,) = reader.unpack(_TAIL)
    if after_rows:
        raise ValueError(f"{FILE_NAME} has {after_rows:,} in unknown_after_rows; only 0 is known")
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records


def _read_list(reader: RecordReader, item: struct.Struct, what: str) -> list[int]:
    (count,) = reader.unpack(_COUNT)
    if count * item.size > reader.remaining():
        raise ValueError(f"list of {count:,} {what} runs past the rows of {FILE_NAME}")
    return [reader.unpack(item)[0] for _ in range(count)]


def _read_row(reader: RecordReader) -> dict:
    item_key, item_key_dup, unknown_08, build_time, work_ani_type = reader.unpack(_HEAD)
    repair_item_keys = _read_list(reader, _U32, "repair item keys")
    repair_item_counts = _read_list(reader, _I64, "repair item counts")
    (repair_time,) = reader.unpack(_REPAIR_TIME)
    repair_percents = _read_list(reader, _U32, "repair percents")
    (unknown_repair_percents_00,) = reader.unpack(_TAIL)
    return {
        "item_key": item_key,
        "item_key_dup": item_key_dup,
        "unknown_08": unknown_08,
        "build_time": build_time,
        "work_ani_type": work_ani_type,
        "repair_item_keys_count": len(repair_item_keys),
        "repair_item_keys": repair_item_keys,
        "repair_item_counts_count": len(repair_item_counts),
        "repair_item_counts": repair_item_counts,
        "repair_time": repair_time,
        "repair_percents_count": len(repair_percents),
        "repair_percents": repair_percents,
        "unknown_repair_percents_00": unknown_repair_percents_00,
    }
