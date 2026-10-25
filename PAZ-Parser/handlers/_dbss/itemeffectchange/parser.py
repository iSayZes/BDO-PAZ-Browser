"""`itemeffectchange.dbss`: the model an item mesh uses at each enhancement level.

    u32 group_count | group_count x Group
    Group: u32 entry_count | entry_count x (u32 mesh_key | u8 enchant_level | str8 mesh_file)

`itemeffectchangeoffset.dbss` has the same groups in another order, each a
u32 row count, the u32 mesh key and (u32 enchant_level, offset, size) rows.
Layout 2 in docs/file-formats/dbss/itemeffectchange_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "itemeffectchange.dbss"
OFFSET_FILE = "itemeffectchangeoffset.dbss"

_U32 = struct.Struct("<I")
_ENTRY_HEAD = struct.Struct("<IB")
_INDEX_GROUP_HEAD = struct.Struct("<II")
_INDEX_ROW = struct.Struct("<III")


def _read_group(reader: RecordReader) -> dict:
    (entry_count,) = reader.unpack(_U32)
    entries = []
    for _ in range(entry_count):
        mesh_key, enchant_level = reader.unpack(_ENTRY_HEAD)
        entries.append({
            "mesh_key": mesh_key,
            "enchant_level": enchant_level,
            "entry_count": entry_count,
            "mesh_file": reader.text(wide=False),
        })
    return {"entries": entries}


def _read_index_group(reader: RecordReader) -> dict:
    row_count, mesh_key = reader.unpack(_INDEX_GROUP_HEAD)
    rows = []
    for _ in range(row_count):
        enchant_level, offset, size = reader.unpack(_INDEX_ROW)
        rows.append({"mesh_key": mesh_key, "enchant_level": enchant_level, "offset": offset, "size": size})
    return {"entries": rows}


def parse_itemeffectchange_records(data: bytes) -> list[dict]:
    """Every entry in file order, with its group's `entry_count`.

    Raises ValueError when a group runs past the file or bytes are left after the last one.
    """
    groups = read_counted_records(data, _read_group, FILE_NAME)
    return [entry for group in groups for entry in group["entries"]]


def parse_itemeffectchangeoffset_records(data: bytes) -> list[dict]:
    """Every index row in file order, with its group's `mesh_key`.

    Raises ValueError like `parse_itemeffectchange_records()`.
    """
    groups = read_counted_records(data, _read_index_group, OFFSET_FILE)
    return [row for group in groups for row in group["entries"]]
