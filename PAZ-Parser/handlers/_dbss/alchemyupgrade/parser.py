"""`alchemyupgrade.dbss`: the materials that polish each alchemy stone type.

The file and its `alchemyupgradeoffset.dbss` index use the grouped walk in
`_dbss/alchemystone/grouped.py`. A main row is
`(stone_type, item_id, experience)`.
Layout in docs/file-formats/alchemyupgrade_dbss.md.
"""

from __future__ import annotations

from _dbss.alchemystone.grouped import parse_grouped_rows, parse_stone_offset_records

FILE_NAME = "alchemyupgrade.dbss"
OFFSET_FILE = "alchemyupgradeoffset.dbss"
# `experience` and the stone's own EXP are percent x 10,000; the alchemy stone
# window divides `getExperience()` by this (panel_window_alchemystone_all).
EXPERIENCE_PER_PERCENT = 10_000


def parse_alchemyupgrade_records(data: bytes) -> list[dict]:
    """Every material row, in file order."""
    return [
        {"stone_type": stone_type, "item_id": item_id, "experience": experience}
        for _group, (stone_type, item_id, experience) in parse_grouped_rows(data, FILE_NAME)
    ]


def parse_alchemyupgradeoffset_records(data: bytes) -> list[dict]:
    """Every index row, in file order; `stone_type` is the group index."""
    return parse_stone_offset_records(data, OFFSET_FILE)
