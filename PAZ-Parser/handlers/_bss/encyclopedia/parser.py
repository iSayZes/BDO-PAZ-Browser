"""`encyclopedia.bss`: the entries of the Fishing Encyclopedia.

    PABR | u32 count | count x 104-byte row | string table
    | u32 string_table_start | u32 0
    row: u16 key | u32 item_id | u32 type | u8 category | u8 rareness
         | f32 base_size | f32 | u64 fish_exp_rate | u32 fish_exp_type
         | u32 desc_ref | u32 image_ref | 5 x (u32 count, u32 sides, i32 bonus)
         | u32

`desc_ref` and `image_ref` index the string table: the Korean description
and the artwork path under `ui_texture/`. The five dice are the server-only
`VarySize_0` to `_4` rolls, `1D1+0` on every client row. Full layout in
docs/file-formats/bss/encyclopedia_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at
from _common.ui_texture import ui_texture_path


FILE_NAME = "encyclopedia.bss"

_HEAD = struct.Struct("<HIIBBffQIII")
_DICE = struct.Struct("<IIi")
_DICE_COUNT = 5
_TAIL = struct.Struct("<I")
_ROW_SIZE = _HEAD.size + _DICE_COUNT * _DICE.size + _TAIL.size


def _read_dice(data: bytes, offset: int) -> list[dict]:
    """The five size rolls from `offset`, as the sheet's count, sides and bonus."""
    return [
        dict(zip(("count", "sides", "bonus"), _DICE.unpack_from(data, offset + i * _DICE.size)))
        for i in range(_DICE_COUNT)
    ]


def _read_row(data: bytes, offset: int, strings: list[str]) -> dict:
    (
        key, item_id, type_, category, rareness, base_size, unknown_10,
        fish_exp_rate, fish_exp_type, desc_ref, image_ref,
    ) = _HEAD.unpack_from(data, offset)
    dice_offset = offset + _HEAD.size
    (unknown_64,) = _TAIL.unpack_from(data, dice_offset + _DICE_COUNT * _DICE.size)
    return {
        "key": key,
        "item_id": item_id,
        "type": type_,
        "category": category,
        "rareness": rareness,
        "base_size": base_size,
        "fish_exp_rate": fish_exp_rate,
        "fish_exp_type": fish_exp_type,
        "description_kr": string_at(strings, desc_ref).strip(),
        "image_path": ui_texture_path(string_at(strings, image_ref)),
        "vary_sizes": _read_dice(data, dice_offset),
        "unknown_10": unknown_10,
        "unknown_64": unknown_64,
    }


def parse_encyclopedia_records(data: bytes) -> list[dict]:
    """Every entry in file order, with its strings resolved.

    Raises ValueError on a bad magic or when the rows do not end where the
    string table starts.
    """
    offsets = fixed_row_offsets(data, _ROW_SIZE, FILE_NAME)
    strings = read_string_table(data)
    return [_read_row(data, offset, strings) for offset in offsets]
