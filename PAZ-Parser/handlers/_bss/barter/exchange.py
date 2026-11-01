"""The 56-byte Exchange every barter row holds.

    u32 from_item_key | u64 from_min_count | u64 from_max_count
    | u32 to_item_key | u64 to_min_count | u64 to_max_count
    | u32 barter_need_point | u32 exchange_max_count | u32 exchange_min | u32 exchange_max

The item keys pack `enchant_level << 24 | item_id`. `barter_special.bss`
holds it at row +0x06, `bartersubgroup.bss` at entry +0x0C, and
`barter_normal.bss` entries have the same row as `barter_special.bss`. Layout in
docs/file-formats/bss/bartersubgroup_bss.md, "Exchange (56 bytes)".
"""

from __future__ import annotations

import struct

EXCHANGE = struct.Struct("<IQQIQQIIII")

EXCHANGE_FIELDS = (
    "from_item_key",
    "from_min_count",
    "from_max_count",
    "to_item_key",
    "to_min_count",
    "to_max_count",
    "barter_need_point",
    "exchange_max_count",
    "exchange_min",
    "exchange_max",
)


def read_exchange(data: bytes, offset: int) -> dict:
    """The Exchange at `offset` as a dict of its doc field names."""
    return dict(zip(EXCHANGE_FIELDS, EXCHANGE.unpack_from(data, offset)))
