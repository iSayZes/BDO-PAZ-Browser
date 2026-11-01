"""`regioninfo_linkandcheckvalid2.bss`: the region link lists.

    PABR | u32 count | count x (u16 region_key | u32 link_count | u32 unknown_06
    | u16[link_count] pc_delivery_region_keys) | empty string table
    | u32 string_table_start | u32 0

One record per `regioninfo.bss` region, in hash order rather than key order.
Each list matches that region's `pc_delivery_region_keys` in `regioninfo.bss`. Full
layout in docs/file-formats/bss/regioninfo_linkandcheckvalid2_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import checked_string_table_start, string_table_start
from _common.record_reader import RecordReader


_HEADER_SIZE = 8
_FILE = "regioninfo_linkandcheckvalid2.bss"

# u16 region_key | u32 link_count | u32 unknown_06
_HEAD = struct.Struct("<HII")


def _records_end(data: bytes) -> int:
    """Where the records stop. Raises ValueError on a bad magic or trailer."""
    return checked_string_table_start(data, _FILE)


def _read_record(reader: RecordReader) -> dict:
    region_key, link_count, unknown_06 = reader.unpack(_HEAD)
    keys = reader.unpack(struct.Struct(f"<{link_count}H"))
    return {
        "region_key": region_key,
        "pc_delivery_region_keys": list(keys),
        "unknown_06": unknown_06,
    }


def parse_region_link_records(data: bytes) -> list[dict]:
    """Every record in file order.

    Raises ValueError when a record runs past the string table or the walk
    does not end where it starts: then the layout has changed.
    """
    end = _records_end(data)
    reader = RecordReader(data, _HEADER_SIZE, end, _FILE)
    records = [_read_record(reader) for _ in range(u32(data, 4))]
    if not reader.at_end():
        raise ValueError(f"{_FILE} records do not end where its string table starts")
    return records
