from __future__ import annotations

from _common.binary import u32
from _common.prefixed_string import find_prefixed_ascii, read_prefixed_utf16


# The offset companion has no PABR magic and no trailer, a u32 count then rows.
_OFFSET_HEADER_SIZE = 4
_OFFSET_ROW_SIZE = 12

_BLOCK_HEADER_SIZE = 4
_NAME_PREFIX_OFFSET = 0x04

# A u32 item ID follows the icon string, this many bytes past its end.
_ITEM_ID_GAP = 16
_MAX_ITEM_ID = 0x00FFFFFF

# Stored icon paths already start at "Icon/", so they hang off ui_texture.
ICON_ROOT = "ui_texture/"


def parse_cashproductoffset_records(data: bytes) -> list[dict]:
    """Parse the product-ID index into plain dicts."""
    if len(data) < _OFFSET_HEADER_SIZE:
        raise ValueError("cashproductoffset.dbss is too small to hold a count.")

    count = u32(data, 0)
    end = _OFFSET_HEADER_SIZE + count * _OFFSET_ROW_SIZE
    if end > len(data):
        raise ValueError(
            f"cashproductoffset.dbss declares {count:,} rows but is only "
            f"{len(data):,} bytes."
        )

    records: list[dict] = []
    for index in range(count):
        pos = _OFFSET_HEADER_SIZE + index * _OFFSET_ROW_SIZE
        records.append({
            "product_id": u32(data, pos),
            "data_offset": u32(data, pos + 0x04),
            "data_size": u32(data, pos + 0x08),
        })

    return records


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
            "product_icon_path": f"{ICON_ROOT}{icon.lower()}" if icon else "",
            "item_id": _linked_item_id(data, icon_end, end) if icon else 0,
            "block_size": row["data_size"],
        })

    return records
