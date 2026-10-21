"""`monstergroup.dbss`: monster character keys per hunting zone group.

    monstergroupoffset.dbss: u32 count | count x (u16 key, u32 offset, u32 size)
    monstergroup.dbss:       u32 count | (u16 key copy | u16 group_key, u32 member_count,
                                          member_count x (u16 character_key, u32 percent)) ...

Full layout in docs/file-formats/monstergroup_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows


_KEY = struct.Struct("<H")
_HEAD = struct.Struct("<HI")
_MEMBER = struct.Struct("<HI")


def parse_monstergroup_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    return parse_bare_offset_rows(data)


def _parse_group(data: bytes, row: PabrOffsetRow) -> dict:
    end = row.offset + row.size
    if row.offset < _KEY.size or end > len(data):
        raise ValueError(f"group {row.entry_id} lies outside the file")
    (key_prefix,) = _KEY.unpack_from(data, row.offset - _KEY.size)
    group_key, member_count = _HEAD.unpack_from(data, row.offset)
    if key_prefix != row.entry_id or group_key != row.entry_id:
        raise ValueError(f"group {row.entry_id} stores keys {key_prefix} and {group_key}")
    if _HEAD.size + member_count * _MEMBER.size != row.size:
        raise ValueError(f"group {group_key} has {member_count} members in {row.size} bytes")

    members = [
        {"character_key": character_key, "percent": percent}
        for character_key, percent in _MEMBER.iter_unpack(data[row.offset + _HEAD.size : end])
    ]
    return {"group_key": group_key, "member_count": member_count, "members": members}


def parse_monstergroup_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every group in offset-table order.

    Raises ValueError when a group lies outside the file, stores a key other
    than its offset row's, or its member count does not fill its size: then
    the layout has changed.
    """
    return [_parse_group(data, row) for row in parse_monstergroup_offset_rows(offset_data)]
