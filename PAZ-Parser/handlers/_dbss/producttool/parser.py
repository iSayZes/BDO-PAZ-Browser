"""`producttool.dbss`: the AutofishingTimePercents value of fishing rods and floats.

    u32 count | count x 28-byte record
    record = u32 item_key | u32 item_key_dup | 4 x u32 unknown | u32 autofishing_time_percents

`item_key` packs `enchant_level << 24 | item_id` (`_common/item_key.py`).
`producttooloffset.dbss` holds bare u32-keyed index rows that point at
`item_key_dup`, just past each record's first key. The records fill the file,
so the parser reads them in order without the index. Layout in
docs/file-formats/dbss/producttool_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.item_key import split_item_key
from _common.pabr_offset import parse_bare_u32_offset_rows


FILE_NAME = "producttool.dbss"
OFFSET_FILE = "producttooloffset.dbss"

COUNT_SIZE = 4
# u32 item_key | u32 item_key_dup | u32 unknown_08 | u32 unknown_0c | u32 unknown_10
# | u32 unknown_14 | u32 autofishing_time_percents
RECORD = struct.Struct("<7I")
_FIELDS = (
    "item_key",
    "item_key_dup",
    "unknown_08",
    "unknown_0c",
    "unknown_10",
    "unknown_14",
    "autofishing_time_percents",
)


def parse_producttool_records(data: bytes) -> list[dict]:
    """Every record in file order, with its item key split into item and level.

    Raises ValueError when the file is not exactly its count and that many
    records, or when a record's two keys differ: then the record size has
    changed and every field is suspect.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its record count")
    count = u32(data, 0)
    expected = COUNT_SIZE + count * RECORD.size
    if len(data) != expected:
        raise ValueError(f"{FILE_NAME} declares {count:,} records ({expected:,} bytes) but holds {len(data):,} bytes")
    return [_record(index, values) for index, values in enumerate(RECORD.iter_unpack(data[COUNT_SIZE:]))]


def _record(index: int, values: tuple[int, ...]) -> dict:
    record = dict(zip(_FIELDS, values))
    if record["item_key"] != record["item_key_dup"]:
        raise ValueError(
            f"{FILE_NAME} record {index}: item_key {record['item_key']} "
            f"differs from item_key_dup {record['item_key_dup']}"
        )
    item_id, enchant_level = split_item_key(record["item_key"])
    return {**record, "item_id": item_id, "enchant_level": enchant_level}


def parse_producttooloffset_records(data: bytes) -> list[dict]:
    """Every index row in file order, its key split into item and level.

    Raises ValueError on a count the file cannot hold.
    """
    return [_offset_record(row.entry_id, row.offset, row.size) for row in parse_bare_u32_offset_rows(data)]


def _offset_record(item_key: int, data_offset: int, data_size: int) -> dict:
    item_id, enchant_level = split_item_key(item_key)
    return {
        "item_key": item_key,
        "item_id": item_id,
        "enchant_level": enchant_level,
        "data_offset": data_offset,
        "data_size": data_size,
    }
