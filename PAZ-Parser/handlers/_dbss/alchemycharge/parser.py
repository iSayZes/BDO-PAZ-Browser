"""`alchemycharge.dbss`: the materials that recharge each alchemy stone type.

The file and its `alchemychargeoffset.dbss` index use the grouped walk in
`_common/grouped_rows.py`. A main row is
`(stone_type, item_id, charge_point)`.
Layout in docs/file-formats/dbss/alchemycharge_dbss.md.
"""

from __future__ import annotations

from _dbss.alchemystone.grouped import parse_stone_offset_records, parse_stone_rows

FILE_NAME = "alchemycharge.dbss"
OFFSET_FILE = "alchemychargeoffset.dbss"


def parse_alchemycharge_records(data: bytes) -> list[dict]:
    """Every material row, in file order."""
    return [
        {"stone_type": stone_type, "item_id": item_id, "charge_point": charge_point}
        for _group, (stone_type, item_id, charge_point) in parse_stone_rows(data, FILE_NAME)
    ]


def parse_alchemychargeoffset_records(data: bytes) -> list[dict]:
    """Every index row, in file order; `stone_type` is the group index."""
    return parse_stone_offset_records(data, OFFSET_FILE)
