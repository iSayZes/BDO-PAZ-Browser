"""`tradeexperiencess.bss`: the base Trading EXP of one sold trade item, per Trading level.

    u32 count | count x u64 trade_exp

Row r holds the value for Trading level r + 1. Layout 1 in
docs/file-formats/bss/tradeexperiencess_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import counted_row_values


FILE_NAME = "tradeexperiencess.bss"

_ROW = struct.Struct("<Q")


def parse_tradeexperiencess_records(data: bytes) -> list[dict]:
    """One record per row, with the Trading level it belongs to.

    Raises ValueError when the rows do not end at the last byte of the file.
    """
    return [
        {"trading_level": row + 1, "trade_exp": trade_exp}
        for row, (trade_exp,) in enumerate(counted_row_values(data, _ROW, FILE_NAME))
    ]
