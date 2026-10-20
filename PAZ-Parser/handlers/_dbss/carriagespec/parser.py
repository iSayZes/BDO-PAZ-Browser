"""`carriagespec.dbss`: one row per transport carriage type.

    u32 count | count x (u8 carriage_key | i32 distance_per_minute | i32 loadage
                         | i32 transport_max_weight | i32 camasilb_add_transport_max_weight
                         | i64 base_fee | i32 overload_weight | i64 fee_per_weight
                         | u8 non_stack_trade | u8 stack_trade | u8 expiration_period_trade)

`carriagespecoffset.dbss` points at each row's `carriage_key`, so the walk
from the start needs no index. Layout 1 in docs/file-formats/carriagespec_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "carriagespec.dbss"
OFFSET_FILE = "carriagespecoffset.dbss"

_COUNT_SIZE = 4
_FIELDS = (
    "carriage_key",
    "distance_per_minute",
    "loadage",
    "transport_max_weight",
    "camasilb_add_transport_max_weight",
    "base_fee",
    "overload_weight",
    "fee_per_weight",
    "non_stack_trade",
    "stack_trade",
    "expiration_period_trade",
)
_ROW = struct.Struct("<BiiiiqiqBBB")
ROW_SIZE = _ROW.size


def parse_carriagespec_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    end = _COUNT_SIZE + count * _ROW.size
    if end != len(data):
        raise ValueError(f"{count:,} rows of {_ROW.size} bytes end at 0x{end:X}, the file is {len(data):,} bytes")

    return [dict(zip(_FIELDS, values)) for values in _ROW.iter_unpack(data[_COUNT_SIZE:end])]
