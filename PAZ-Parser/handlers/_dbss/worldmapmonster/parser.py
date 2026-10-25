"""`worldmapmonster.dbss`: the monster markers of the world map.

    worldmapmonsteroffset.dbss: u32 count | count x (u16 key, u32 offset, u32 size)
    worldmapmonster.dbss:       u32 count | (u16 key copy | record) ...

Each record holds two Korean label lines and a name, the world position, the
marker illustration and an optional condition script. Full layout in
docs/file-formats/dbss/worldmapmonster_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader
from _common.ui_texture import ui_texture_path


_KEY = struct.Struct("<H")
_POSITION = struct.Struct("<3f")
# i32 unknown_ref | u8 unknown_kind | u8 unknown_flag | u8 reserved
_TAIL = struct.Struct("<iBBx")


def parse_worldmapmonster_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    return parse_bare_offset_rows(data)


def _parse_record(data: bytes, row: PabrOffsetRow) -> dict:
    reader = RecordReader(data, row.offset, row.offset + row.size, f"marker {row.entry_id}")
    (key,) = reader.unpack(_KEY)
    if key != row.entry_id:
        raise ValueError(f"marker {row.entry_id} stores key {key}")

    line1_kr = reader.text(wide=True)
    line2_kr = reader.text(wide=True)
    name_kr = reader.text(wide=True)
    pos_x, pos_y, pos_z = reader.unpack(_POSITION)
    icon = reader.text(wide=False)
    condition = reader.text(wide=True)
    unknown_str = reader.text(wide=True)
    unknown_ref, unknown_kind, unknown_flag = reader.unpack(_TAIL)
    if not reader.at_end():
        raise ValueError(f"marker {key} has {reader.remaining()} bytes past its last field")

    return {
        "key": key,
        "line1_kr": line1_kr,
        "line2_kr": line2_kr,
        "name_kr": name_kr,
        "pos_x": pos_x,
        "pos_y": pos_y,
        "pos_z": pos_z,
        "icon_path": ui_texture_path(icon),
        "condition": condition,
        "unknown_str": unknown_str,
        "unknown_ref": unknown_ref,
        "unknown_kind": unknown_kind,
        "unknown_flag": unknown_flag,
    }


def parse_worldmapmonster_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every marker in offset-table order.

    Raises ValueError when a record runs past its size, ends early, or stores a
    key other than its offset row's: then the layout has changed.
    """
    return [_parse_record(data, row) for row in parse_worldmapmonster_offset_rows(offset_data)]


def build_worldmap_marker_icon_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Marker illustration by key, for `IndexKind.WORLDMAP_MARKER_ICON`.

    The Abyssal Wells store no icon and are left out.
    """
    return {
        record["key"]: record["icon_path"]
        for record in parse_worldmapmonster_records(data, offset_data)
        if record["icon_path"]
    }
