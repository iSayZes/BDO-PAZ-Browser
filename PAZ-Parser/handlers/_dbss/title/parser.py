"""`title.dbss` records, located through `titleoffset.dbss`.

Each offset row points at a record's `key_count`; the record reads straight
from its counts:

    u32 key_count | u32[key_count] key_values | u32 title_id
    | str16 title_text_kr | str16 requirement_text_kr
    | u32 | u32 category_id | 20 bytes | u32 unknown_tail_1c | u32
    | u32 unknown_tail_24 | u32 | str8 effect_name | str8 color_argb
    | u32 color_value | 12 bytes

`str16` / `str8` are a u64 count, then UTF-16LE / ASCII text. The count of
`title_text_kr` is the title's length; earlier readings took it for a style
value. Full layout in docs/file-formats/dbss/title_dbss.md.
"""

from __future__ import annotations

from _common.binary import u32
from _common.prefixed_string import read_prefixed_at
from .model import TitleRecord

_KEY_VALUES = 4
_U32_SIZE = 4
# From the end of requirement_text_kr.
_CATEGORY = 0x04
_UNKNOWN_TAIL_1C = 0x1C
_UNKNOWN_TAIL_24 = 0x24
_EFFECT_NAME = 0x2C
# color_value, then 12 bytes that end the record.
_AFTER_COLOR_ARGB = _U32_SIZE + 12
# Styled titles ("MASTER ...") colour their own name with PAColor tags.
_PA_TAG = "<PA"


def _color_fields(color_argb: str) -> tuple[str, str]:
    """`0xAARRGGBB` and `#RRGGBB` for a stored colour, or two empty strings."""
    if not color_argb:
        return "", ""
    argb = color_argb.upper()
    return f"0x{argb}", f"#{argb[2:]}"


def parse_title_record(block: bytes, title_id: int) -> TitleRecord:
    """Read one record; `block` is exactly the bytes the offset row covers.

    Raises ValueError when the record does not repeat `title_id` or its
    fields do not end exactly at the end of the block.
    """
    end = len(block)
    key_count = u32(block, 0)
    title_id_at = _KEY_VALUES + key_count * _U32_SIZE
    if title_id_at + _U32_SIZE > end or u32(block, title_id_at) != title_id:
        raise ValueError(f"title {title_id} record does not repeat its own ID")

    title_text_kr, pos = read_prefixed_at(block, title_id_at + _U32_SIZE, end, wide=True)
    requirement_text_kr, tail = read_prefixed_at(block, pos, end, wide=True)
    if tail + _EFFECT_NAME > end:
        raise ValueError(f"title {title_id} ends inside its tail")
    effect_name, pos = read_prefixed_at(block, tail + _EFFECT_NAME, end, wide=False)
    color_argb, pos = read_prefixed_at(block, pos, end, wide=False)
    if pos + _AFTER_COLOR_ARGB != end:
        raise ValueError(f"title {title_id} record is {end} bytes, its fields end at {pos + _AFTER_COLOR_ARGB}")

    title_color_argb, title_color_css = _color_fields(color_argb)
    return TitleRecord(
        key_count=key_count,
        key_values=[u32(block, _KEY_VALUES + index * _U32_SIZE) for index in range(key_count)],
        title_id=title_id,
        title_text_kr=title_text_kr,
        requirement_text_kr=requirement_text_kr,
        is_styled_title=title_text_kr.startswith(_PA_TAG),
        category_id=u32(block, tail + _CATEGORY),
        unknown_tail_1c=u32(block, tail + _UNKNOWN_TAIL_1C),
        unknown_tail_24=u32(block, tail + _UNKNOWN_TAIL_24),
        title_color_argb=title_color_argb,
        title_color_css=title_color_css,
        title_effect_name=effect_name,
    )


def extract_title_records(
    data: bytes,
    offset_map: dict[int, tuple[int, int]],
) -> list[TitleRecord]:
    """Every record the offset table points at, in title ID order.

    Raises ValueError on a block that runs past the file or does not read
    to its size, since its fields would be misread.
    """
    records: list[TitleRecord] = []
    for title_id, (offset, size) in sorted(offset_map.items()):
        if offset + size > len(data):
            raise ValueError(f"title {title_id} block runs past the end of title.dbss")
        records.append(parse_title_record(data[offset:offset + size], title_id))
    return records
