"""`marblegamediceitemgroup.dbss`: the Black Spirit's Adventure dice drop groups.

    u32 count | count x row
    row: u32 dice_drop_group_key | u32 entry_count | entry_count x (u32 dice_item_key | u32 rate)

`marblegamediceitemgroupoffset.dbss` (u32 count, then u32 key, offset and
size per row) points at the row start. Layout 1 in
docs/file-formats/dbss/marblegamediceitemgroup_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "marblegamediceitemgroup.dbss"
OFFSET_FILE = "marblegamediceitemgroupoffset.dbss"
KEY_FIELD = "dice_drop_group_key"

_HEAD = struct.Struct("<II")
# dice_item_key, rate
_ENTRY = struct.Struct("<II")


def _read_row(reader: RecordReader) -> dict:
    group_key, entry_count = reader.unpack(_HEAD)
    if entry_count * _ENTRY.size > reader.remaining():
        raise ValueError(f"{FILE_NAME}: group {group_key} lists {entry_count:,} dice, more than the file holds")
    entries = [reader.unpack(_ENTRY) for _ in range(entry_count)]
    return {
        KEY_FIELD: group_key,
        "entries": [{"dice_item_key": dice_item_key, "rate": rate} for dice_item_key, rate in entries],
    }


def parse_marblegamediceitemgroup_records(data: bytes) -> list[dict]:
    """Every group in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_marblegamediceitemgroupoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)


def groups_by_dice_item(data: bytes | None) -> dict[int, list[int]]:
    """The group keys that list each dice item key, ascending; empty when the file is missing.

    Raises ValueError when the file does not parse.
    """
    if data is None:
        return {}
    groups: dict[int, list[int]] = {}
    for record in parse_marblegamediceitemgroup_records(data):
        for entry in record["entries"]:
            groups.setdefault(entry["dice_item_key"], []).append(record[KEY_FIELD])
    return {dice_item_key: sorted(keys) for dice_item_key, keys in groups.items()}
