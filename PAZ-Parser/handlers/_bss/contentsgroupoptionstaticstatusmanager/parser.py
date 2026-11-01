"""`contentsgroupoptionstaticstatusmanager.bss`: the contents groups open on the client's service.

    u32 open_count | u32 open_key_hashes x open_count (ascending)
    | u32 group_count | group_count x (u32 key_hash, str16 contents_group_key)

Layout in docs/file-formats/bss/contentsgroupoptionstaticstatusmanager_bss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader


FILE_NAME = "contentsgroupoptionstaticstatusmanager.bss"

_U32 = struct.Struct("<I")


def parse_contentsgroupoption_records(data: bytes) -> list[dict]:
    """Every group in file order, with whether its hash is in the open list.

    Raises ValueError when a count runs past the file, bytes follow the last
    group, or an open hash names no group.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    (open_count,) = reader.unpack(_U32)
    open_hashes = set(reader.unpack(struct.Struct(f"<{open_count}I")))
    (group_count,) = reader.unpack(_U32)
    records = []
    for _ in range(group_count):
        (key_hash,) = reader.unpack(_U32)
        key = reader.text(wide=True)
        records.append(
            {
                "key_hash": key_hash,
                "contents_group_key": key,
                "is_open": key_hash in open_hashes,
            }
        )
    if not reader.at_end():
        raise ValueError(f"{reader.remaining():,} bytes follow the last group")
    open_groups = sum(1 for r in records if r["is_open"])
    if open_groups != len(open_hashes):
        raise ValueError(f"{len(open_hashes) - open_groups} open hashes name no group")
    return records
