from __future__ import annotations

from _common.binary import u32
from _common.prefixed_string import find_prefixed_ascii


_MAGIC = b"PABR"
_OFFSET_HEADER_SIZE = 8
_OFFSET_ROW_SIZE = 12
_TRAILER_SIZE = 12

# key = (enchant_level << 24) | item_id
_ITEM_ID_MASK = 0x00FFFFFF
_ENCHANT_LEVEL_SHIFT = 24

# Stored icon paths are relative to this folder.
ICON_ROOT = "ui_texture/icon/"


def parse_itemenchantoffset_records(data: bytes) -> list[dict]:
    """Parse the key/offset index into plain dicts."""
    if len(data) < _OFFSET_HEADER_SIZE or data[:4] != _MAGIC:
        raise ValueError("itemenchantoffset.dbss has invalid magic.")

    count = u32(data, 4)
    end = _OFFSET_HEADER_SIZE + count * _OFFSET_ROW_SIZE
    if end > len(data):
        raise ValueError(
            f"itemenchantoffset.dbss declares {count:,} rows but is only "
            f"{len(data):,} bytes."
        )

    records: list[dict] = []
    for index in range(count):
        pos = _OFFSET_HEADER_SIZE + index * _OFFSET_ROW_SIZE
        key = u32(data, pos)
        records.append({
            "key": key,
            "item_id": key & _ITEM_ID_MASK,
            "enchant_level": key >> _ENCHANT_LEVEL_SHIFT,
            "data_offset": u32(data, pos + 0x04),
            "data_size": u32(data, pos + 0x08),
        })

    return records


def parse_itemenchant_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Parse one row per (item, enchant level), carrying the inline icon path.

    The first string in a block is always the icon path; an optional second
    string is an effect tag such as `ITEM_BIC_HIT_1`.
    """
    records: list[dict] = []

    for row in parse_itemenchantoffset_records(offset_data):
        start = row["data_offset"]
        end = start + row["data_size"]
        if end > len(data):
            raise ValueError(
                f"itemenchant.dbss block for key {row['key']} ends at "
                f"{end:,} but the file is {len(data):,} bytes."
            )

        strings = find_prefixed_ascii(data, start, end)
        icon = strings[0] if strings else ""
        records.append({
            "item_id": row["item_id"],
            "enchant_level": row["enchant_level"],
            "icon_path": f"{ICON_ROOT}{icon.lower()}" if icon else "",
            "effect_tag": strings[1] if len(strings) > 1 else "",
            "block_size": row["data_size"],
        })

    return records


def build_item_icon_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Map item ID to icon path using only the level-0 (base item) records.

    Enchanted variants repeat the base item's icon, so skipping them cuts the
    work to a third without losing an entry.
    """
    index: dict[int, str] = {}

    for row in parse_itemenchantoffset_records(offset_data):
        if row["enchant_level"]:
            continue

        start = row["data_offset"]
        end = start + row["data_size"]
        if end > len(data):
            continue

        strings = find_prefixed_ascii(data, start, end)
        if strings:
            index[row["item_id"]] = f"{ICON_ROOT}{strings[0].lower()}"

    return index
