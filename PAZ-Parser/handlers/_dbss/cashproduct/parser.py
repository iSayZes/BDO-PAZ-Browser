from __future__ import annotations

from _common.binary import u32
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.prefixed_string import find_prefixed_ascii, read_prefixed_utf16
from _common.ui_texture import ui_texture_path


_BLOCK_HEADER_SIZE = 4
_NAME_PREFIX_OFFSET = 0x04

# A u32 item ID follows the icon string, this many bytes past its end.
_ITEM_ID_GAP = 16
_MAX_ITEM_ID = 0x00FFFFFF


def parse_cashproductoffset_records(data: bytes) -> list[dict]:
    """Parse the product-ID index (no PABR magic, no trailer) into plain dicts."""
    return [
        {"product_id": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_u32_offset_rows(data)
    ]


def _linked_item_id(data: bytes, icon_end: int, block_end: int) -> int:
    """Item ID stored a fixed gap after the icon string, or 0 when absent."""
    pos = icon_end + _ITEM_ID_GAP
    if pos + 4 > block_end:
        return 0

    item_id = u32(data, pos)
    return item_id if 1 <= item_id <= _MAX_ITEM_ID else 0


def parse_cashproduct_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Parse one row per cash product, carrying its shop tile and linked item.

    The stored path is the Pearl Shop tile for the product, not the item's own
    icon. 58% of products share a tile with another, so a whole collection can
    point at one promotional image. Use the linked item ID for an item icon.
    """
    records: list[dict] = []

    for row in parse_cashproductoffset_records(offset_data):
        start = row["data_offset"]
        end = start + row["data_size"]
        if end > len(data):
            raise ValueError(
                f"cashproduct.dbss block for product {row['product_id']} ends "
                f"at {end:,} but the file is {len(data):,} bytes."
            )

        strings = find_prefixed_ascii(data, start, end)
        icon = strings[0] if strings else ""
        icon_end = (
            data.find(icon.encode("ascii"), start, end) + len(icon) if icon else start
        )

        records.append({
            "product_id": row["product_id"],
            "product_name": read_prefixed_utf16(data, start + _NAME_PREFIX_OFFSET),
            "product_icon_path": ui_texture_path(icon),
            "item_id": _linked_item_id(data, icon_end, end) if icon else 0,
            "block_size": row["data_size"],
        })

    return records
