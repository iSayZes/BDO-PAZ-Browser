"""`nakmessagerenewelss.bss`: the look of every screen-wide message (NAK) of `Panel_NakMessage_Renewel`.

    u32 count | count x row
    row: u8[7] is_exist flags | u32 nak_message_type | u16 | f32 ani_time
         | u8[5] | u32 | u32 contents_group_hash
         | background main_bg | background sub_bg
         | text main_text | text sub_text | text sub_text2 | text sub_text3
         | u32 count x effect | u32 count x sound | icon tail (28 bytes)
    background: str8 texture_id | u8 use_grid | f32[4] x 4 grid | f32 span_y | f32[2] size
    text: str16 text_kr | str8 font | str8 color | u8 send_chat | f32 span_x | f32 span_y
    effect: str8 effect_name | u8 loop | i16 pos_x | i16 pos_y
    sound: u16 audio_index | u16 audio_index_b | u8 console_play

Layout 1 in docs/file-formats/bss/nakmessagerenewelss_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records, read_counted_structs
from _common.record_reader import RecordReader


FILE_NAME = "nakmessagerenewelss.bss"

# The seven presence flags at the row start, in file order.
EXIST_FIELDS = (
    "is_exist_sub_bg",
    "is_exist_sub_text",
    "is_exist_sub_text2",
    "is_exist_sub_text3",
    "is_exist_effect_bg",
    "is_exist_sound_list",
    "is_exist_icon",
)
TEXT_FIELDS = ("main_text", "sub_text", "sub_text2", "sub_text3")
_HEAD_FIELDS = (
    *EXIST_FIELDS,
    "nak_message_type",
    "unknown_0b",
    "ani_time",
    "unknown_11",
    "unknown_12",
    "unknown_13",
    "unknown_14",
    "unknown_15",
    "unknown_16",
    "contents_group_hash",
)
_HEAD = struct.Struct("<7BIHf5BII")
_GRID = struct.Struct("<4f")
_BG_TAIL = struct.Struct("<f2f")
_U8 = struct.Struct("<B")
_U32 = struct.Struct("<I")
_TEXT_TAIL = struct.Struct("<Bff")
_EFFECT_TAIL = struct.Struct("<Bhh")
_SOUND = struct.Struct("<HHB")
_SOUND_FIELDS = ("audio_index", "audio_index_b", "console_play")
_ICON_TAIL = struct.Struct("<f8s2f2f")


def _read_background(reader: RecordReader) -> dict:
    texture_id = reader.text(wide=False)
    (use_grid,) = reader.unpack(_U8)
    grids = [list(reader.unpack(_GRID)) for _ in range(4)]
    span_y, size_x, size_y = reader.unpack(_BG_TAIL)
    return {
        "texture_id": texture_id,
        "use_grid": bool(use_grid),
        "grid_pos_x": grids[0],
        "grid_pos_y": grids[1],
        "grid_uv_x": grids[2],
        "grid_uv_y": grids[3],
        "span_y": span_y,
        "size": [size_x, size_y],
    }


def _read_text(reader: RecordReader) -> dict:
    text_kr = reader.text(wide=True)
    font = reader.text(wide=False)
    color = reader.text(wide=False)
    send_chat, span_x, span_y = reader.unpack(_TEXT_TAIL)
    return {
        "text_kr": text_kr,
        "font": font,
        "color": color,
        "send_chat": bool(send_chat),
        "span_x": span_x,
        "span_y": span_y,
    }


def _read_effects(reader: RecordReader) -> list[dict]:
    (count,) = reader.unpack(_U32)
    effects = []
    for _ in range(count):
        effect_name = reader.text(wide=False)
        loop, pos_x, pos_y = reader.unpack(_EFFECT_TAIL)
        effects.append({"effect_name": effect_name, "loop": bool(loop), "pos_x": pos_x, "pos_y": pos_y})
    return effects


def _read_row(reader: RecordReader) -> dict:
    head = dict(zip(_HEAD_FIELDS, reader.unpack(_HEAD), strict=True))
    record: dict = {
        **{field: bool(head[field]) for field in EXIST_FIELDS},
        **{field: head[field] for field in _HEAD_FIELDS if field not in EXIST_FIELDS},
        "main_bg": _read_background(reader),
        "sub_bg": _read_background(reader),
    }
    for field in TEXT_FIELDS:
        record[field] = _read_text(reader)
    record["effects"] = _read_effects(reader)
    record["sounds"] = [
        {**sound, "console_play": bool(sound["console_play"])}
        for sound in read_counted_structs(reader, _SOUND, _SOUND_FIELDS, "sound list")
    ]
    icon_span_y, unknown_sounds_04, *sizes = reader.unpack(_ICON_TAIL)
    record["icon_span_y"] = icon_span_y
    record["unknown_sounds_04"] = unknown_sounds_04.hex()
    record["unknown_sounds_0c"] = sizes[0:2]
    record["unknown_sounds_14"] = sizes[2:4]
    return record


def parse_nakmessagerenewelss_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)
