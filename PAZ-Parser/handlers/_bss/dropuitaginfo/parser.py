"""`dropuitaginfo.bss`: the tags of the drop item window hunting grounds.

    PABR | u32 count | count x 32-byte row | string table
    | u32 string_table_start | u32 0

Each row holds the tag key, its Korean name and tooltip, the Dehkia's Lantern
guide image name and the tag's background and text colours (as hex text and
as ARGB u32s). `dropuihuntinggroundinfo.bss` lists the tag keys of each zone.
Full layout in docs/file-formats/dropuitaginfo_bss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.inline_text import decode_inline_text
from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


_FILE_NAME = "dropuitaginfo.bss"

# u32 key | u32 name_ref | u32 guide_texture_ref | u32 desc_ref
# | u32 texture_color_ref | u32 font_color_ref | u32 texture_color | u32 font_color
_TAG = struct.Struct("<8I")

# A guide image name (`Combine_Etc_DekiaLanterns_GroundTooltip_01`) is a whole
# texture of that name in the folder its first two parts name.
_TEXTURE_ROOT = "ui_texture"
_TEXTURE_FOLDER_PARTS = 2
_TEXTURE_EXTENSION = ".dds"


class TagColors(NamedTuple):
    """The ARGB colours a tag is drawn in: its background tint and its text."""

    texture: int
    font: int


def guide_image_path(texture: str) -> str:
    """PAZ path of a guide image name, or '' when the row has none."""
    if not texture:
        return ""
    folder = "/".join(texture.split("_")[:_TEXTURE_FOLDER_PARTS])
    return f"{_TEXTURE_ROOT}/{folder}/{texture}{_TEXTURE_EXTENSION}".lower()


def parse_tag_records(data: bytes) -> list[dict]:
    """Every tag row in file order, with its strings resolved.

    The hex colour strings are left out: they always equal the two u32s.
    Raises ValueError on a bad magic or when the rows do not end where the
    string table starts.
    """
    offsets = fixed_row_offsets(data, _TAG.size, _FILE_NAME)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        (
            key, name_ref, guide_texture_ref, desc_ref,
            _texture_color_ref, _font_color_ref, texture_color, font_color,
        ) = _TAG.unpack_from(data, offset)
        guide_texture = string_at(strings, guide_texture_ref)
        records.append({
            "key": key,
            "name_kr": string_at(strings, name_ref),
            "description_kr": decode_inline_text(string_at(strings, desc_ref)),
            "guide_texture": guide_texture,
            "guide_image_path": guide_image_path(guide_texture),
            "texture_color": texture_color,
            "font_color": font_color,
        })
    return records


def parse_tag_colors(data: bytes) -> dict[int, TagColors]:
    """Tag key -> its colours. Raises ValueError like `parse_tag_records`."""
    return {
        record["key"]: TagColors(record["texture_color"], record["font_color"])
        for record in parse_tag_records(data)
    }
