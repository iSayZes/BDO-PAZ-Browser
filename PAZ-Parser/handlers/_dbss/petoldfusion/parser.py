"""`petoldfusion.dbss`: the old pet exchange, result tiers per fusion key.

    u32 count | Row[count]
    Row (40 bytes): u32 key_prefix | u8 variant | u8 species | u8 unknown_06 | u8 tier
                    | 4 x (u8 select_tier | bytes[3] padding | u32 select_rate)

`petoldfusionoffset.dbss` is a bare u32-keyed offset table into it (u32
count, then u32 fusion key, u32 offset, u32 size per row); each offset points
past the row's key prefix. Tiers are stored from 0 (Tier 1), rates on the
1,000,000 = 100% scale. Layout 1 in docs/file-formats/dbss/petoldfusion_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import parse_bare_u32_offset_rows


FILE_NAME = "petoldfusion.dbss"
OFFSET_FILE = "petoldfusionoffset.dbss"

_COUNT_SIZE = 4
KEY_PREFIX_SIZE = 4
# The four results of a row: (select_tier, padding, select_rate), the padding
# named by its offset in the row.
SELECT_FIELDS = (
    ("select_tier_0", "padding_09", "select_rate_0"),
    ("select_tier_1", "padding_11", "select_rate_1"),
    ("select_tier_2", "padding_19", "select_rate_2"),
    ("select_tier_3", "padding_21", "select_rate_3"),
)
# key_prefix, the four fusion key bytes, then per select: tier, 3 padding bytes, rate
_ROW = struct.Struct("<I4B" + "B3sI" * len(SELECT_FIELDS))
ROW_SIZE = _ROW.size


def _select_values(values: tuple) -> dict[str, object]:
    """The select fields of one row, with each padding run as hex text."""
    record: dict[str, object] = {}
    for index, (tier_field, padding_field, rate_field) in enumerate(SELECT_FIELDS):
        tier, padding, rate = values[index * 3 : index * 3 + 3]
        record |= {tier_field: tier, padding_field: padding.hex(" "), rate_field: rate}
    return record


def parse_petoldfusion_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when the file is shorter or longer than its count says.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")
    count = u32(data, 0)
    expected = _COUNT_SIZE + count * ROW_SIZE
    if len(data) != expected:
        raise ValueError(f"{FILE_NAME} is {len(data):,} bytes, {count:,} rows need {expected:,}")

    return [
        {
            "key_prefix": key_prefix,
            "variant": variant,
            "species": species,
            "unknown_06": unknown_06,
            "tier": tier,
            **_select_values(tuple(selects)),
        }
        for key_prefix, variant, species, unknown_06, tier, *selects in _ROW.iter_unpack(data[_COUNT_SIZE:])
    ]


def parse_petoldfusionoffset_records(data: bytes) -> list[dict]:
    """Every index row: the fusion key, where its row starts past the key prefix, and its size.

    Raises ValueError on a count the file cannot hold.
    """
    return [
        {"fusion_key": row.entry_id, "offset": row.offset, "size": row.size}
        for row in parse_bare_u32_offset_rows(data)
    ]
