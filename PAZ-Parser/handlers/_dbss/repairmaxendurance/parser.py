"""`repairmaxendurance.dbss`: the materials that restore each item's max durability.

A u32 row count, then variable rows: the u32 item key, the same key again,
the i64 silver-only cost, the i16 silver-only repair count, a u32 material
count and that many 14-byte materials (u32 item key, i16 repair count, i64
silver). `repairmaxenduranceoffset.dbss` points 4 bytes into a row, at the
second key, so the walk from the start needs no index. Layout 1 in
docs/file-formats/repairmaxendurance_dbss.md.
"""

from __future__ import annotations

import struct


FILE_NAME = "repairmaxendurance.dbss"
OFFSET_FILE = "repairmaxenduranceoffset.dbss"

_COUNT = struct.Struct("<I")
# item_key, item_key_dup, only_need_money, only_money_repair_count, material_count
_ROW_HEAD = struct.Struct("<IIqhI")
# item_key, repair_count, need_money
_MATERIAL = struct.Struct("<Ihq")
ROW_HEAD_SIZE = _ROW_HEAD.size
MATERIAL_SIZE = _MATERIAL.size


def _parse_row(data: bytes, offset: int) -> tuple[dict, int]:
    """The row at `offset` and the offset after it."""
    if offset + ROW_HEAD_SIZE > len(data):
        raise ValueError(f"the row at 0x{offset:X} runs past the end of the file")
    item_key, item_key_dup, only_need_money, only_money_repair_count, material_count = _ROW_HEAD.unpack_from(
        data, offset
    )
    materials_start = offset + ROW_HEAD_SIZE
    end = materials_start + material_count * MATERIAL_SIZE
    if end > len(data):
        raise ValueError(f"the {material_count:,} materials of the row at 0x{offset:X} run past the end of the file")
    materials = [_MATERIAL.unpack_from(data, materials_start + i * MATERIAL_SIZE) for i in range(material_count)]
    record = {
        "item_key": item_key,
        "item_key_dup": item_key_dup,
        "only_need_money": only_need_money,
        "only_money_repair_count": only_money_repair_count,
        "material_count": material_count,
        "material_item_keys": [key for key, _, _ in materials],
        "material_repair_counts": [count for _, count, _ in materials],
        "material_need_money": [money for _, _, money in materials],
    }
    return record, end


def parse_repairmaxendurance_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT.size:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    (count,) = _COUNT.unpack_from(data, 0)
    records: list[dict] = []
    offset = _COUNT.size
    for _ in range(count):
        record, offset = _parse_row(data, offset)
        records.append(record)
    if offset != len(data):
        raise ValueError(f"{len(data) - offset:,} bytes follow the last of {count:,} rows")
    return records
