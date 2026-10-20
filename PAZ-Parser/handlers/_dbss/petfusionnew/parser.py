"""The pet exchange tables: result tiers with their base chance, and the add rates.

`petfusionnew.dbss`, one row per main pet tier, no count:

    Row[..end] (u8 tier | u8 select_tier_0 | bytes[3] padding_02 | u32 select_rate_0
                | u8 select_tier_1 | bytes[3] padding_0a | u32 select_rate_1)

`petfusionnewoffset.dbss` is a bare u8-keyed offset table into it (u32 count,
then u8 tier, u32 offset, u32 size per row).

`petfusionnewaddrateinfo.dbss`, the values alone:

    u32[4][4] add rates by main pet tier, then sub pet tier | u32[4] gosphy_add_rate

Every rate is on the 1,000,000 = 100% scale and every tier is stored from 0
(Tier 1). Layout 1 in docs/file-formats/petfusionnew_dbss.md and
docs/file-formats/petfusionnewaddrateinfo_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import parse_bare_u8_offset_rows


FILE_NAME = "petfusionnew.dbss"
OFFSET_FILE = "petfusionnewoffset.dbss"
ADD_RATE_FILE = "petfusionnewaddrateinfo.dbss"

# The two results of a row, the next tier up first: (select_tier, padding, select_rate)
# with the padding named by its offset in the row.
SELECT_FIELDS = (
    ("select_tier_0", "padding_02", "select_rate_0"),
    ("select_tier_1", "padding_0a", "select_rate_1"),
)
# tier, then per select: select_tier, the 3 padding bytes, select_rate
_ROW = struct.Struct("<B" + "B3sI" * len(SELECT_FIELDS))

# Main and sub pet tiers the add rate rows cover: Tier 1 to Tier 4.
ADD_RATE_TIERS = 4
ADD_RATE_FIELDS = tuple(f"add_rate_tier_{sub_tier}" for sub_tier in range(ADD_RATE_TIERS))
# The add rate of a Wizard Gosphy (race 99) as the other pet, by main pet tier.
GOSPHY_FIELD = "gosphy_add_rate"
_ADD_RATE_ROW = struct.Struct(f"<{ADD_RATE_TIERS}I")
_ADD_RATE_SIZE = (ADD_RATE_TIERS + 1) * _ADD_RATE_ROW.size


def _select_values(values: tuple) -> dict[str, object]:
    """The select fields of one row, with each padding run as hex text."""
    record: dict[str, object] = {}
    for index, (tier_field, padding_field, rate_field) in enumerate(SELECT_FIELDS):
        tier, padding, rate = values[index * 3 : index * 3 + 3]
        record |= {tier_field: tier, padding_field: padding.hex(" "), rate_field: rate}
    return record


def parse_petfusionnew_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not whole rows.
    """
    if len(data) % _ROW.size:
        raise ValueError(f"{FILE_NAME} is {len(data):,} bytes, not whole {_ROW.size}-byte rows")
    return [{"tier": tier, **_select_values(tuple(rest))} for tier, *rest in _ROW.iter_unpack(data)]


def parse_petfusionnewoffset_records(data: bytes) -> list[dict]:
    """Every index row: the tier, where its row starts and its size.

    Raises ValueError on a count the file cannot hold.
    """
    return [{"tier": row.entry_id, "offset": row.offset, "size": row.size} for row in parse_bare_u8_offset_rows(data)]


def parse_add_rate_records(data: bytes) -> list[dict]:
    """One record per main pet tier: its add rate per sub pet tier and the Wizard Gosphy add rate.

    Raises ValueError when the file is not the 80 bytes of the two arrays.
    """
    if len(data) != _ADD_RATE_SIZE:
        raise ValueError(f"{ADD_RATE_FILE} is {len(data):,} bytes, expected {_ADD_RATE_SIZE}")
    rows = list(_ADD_RATE_ROW.iter_unpack(data))
    gosphy_rates = rows[ADD_RATE_TIERS]
    return [
        {"main_tier": main_tier, **dict(zip(ADD_RATE_FIELDS, rates)), GOSPHY_FIELD: gosphy_rates[main_tier]}
        for main_tier, rates in enumerate(rows[:ADD_RATE_TIERS])
    ]
