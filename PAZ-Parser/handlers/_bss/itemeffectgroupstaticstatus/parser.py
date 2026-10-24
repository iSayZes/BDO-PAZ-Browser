"""`itemeffectgroupstaticstatus.bss`: the glow effects of each item group type.

    u32 group_count | group_count x Group
    Group: u32 item_group_type | u32 effect_count | effect_count x Effect
    Effect: u32 effect_index | u8 unknown_04 | str8 color | bytes[3] color_rgb
    | u32 name | u32 dye_item_id

No PABR magic and no string table. `item_group_type` is an
`itemgroupingstaticstatus.bss` group type, `color` hex text (`1D3F48`),
`color_rgb` the same colour as three bytes (`00 00 00` where the text is set)
and `name` the `RESOURCE` sheet string hash of the effect name. Layout 4 in
docs/file-formats/itemeffectgroupstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "itemeffectgroupstaticstatus.bss"
KEY_FIELD = "item_group_type"

_U32 = struct.Struct("<I")
_HEAD = struct.Struct("<IB")
_COLOR_RGB = struct.Struct("<3s")
_TAIL = struct.Struct("<II")


def _read_effect(reader: RecordReader) -> dict:
    effect_index, unknown_04 = reader.unpack(_HEAD)
    color = reader.text(wide=False)
    (color_rgb,) = reader.unpack(_COLOR_RGB)
    name, dye_item_id = reader.unpack(_TAIL)
    return {
        "effect_index": effect_index,
        "unknown_04": unknown_04,
        "color": color,
        # RRGGBB, the form of `color`.
        "color_rgb": color_rgb.hex().upper(),
        "name": name,
        "dye_item_id": dye_item_id,
    }


def _read_group(reader: RecordReader) -> dict:
    (item_group_type,) = reader.unpack(_U32)
    (effect_count,) = reader.unpack(_U32)
    return {KEY_FIELD: item_group_type, "effects": [_read_effect(reader) for _ in range(effect_count)]}


def parse_itemeffectgroup_effects(data: bytes) -> list[dict]:
    """Every effect of every group in file order, each with its group's `item_group_type`.

    Raises ValueError when an effect runs past the file or the groups end before it.
    """
    groups = read_counted_records(data, _read_group, FILE_NAME)
    return [{KEY_FIELD: group[KEY_FIELD], **effect} for group in groups for effect in group["effects"]]
