from __future__ import annotations

import struct

_WORD = struct.Struct("<I")


def parse_itemcouponreward_offset_records(data: bytes) -> list[dict]:
    """Every u32 word of itemcouponrewardoffset.dbss: the count at +0x00, then unknown words.

    The file declares 4 entries but holds 16 bytes after the count, too few for
    key, offset and size rows. The 4 likely counts one block per coupon type,
    each word that block's row count, but no reader confirms it, so the words
    keep `unknown_<offset>` names.
    """
    if len(data) < _WORD.size:
        raise ValueError("itemcouponrewardoffset.dbss is too short to contain a record-count header.")
    if len(data) % _WORD.size:
        raise ValueError(f"itemcouponrewardoffset.dbss is {len(data)} bytes, not a whole number of u32 words.")

    return [
        {
            "offset": offset,
            "field": "count" if offset == 0 else f"unknown_{offset:02x}",
            "value": _WORD.unpack_from(data, offset)[0],
        }
        for offset in range(0, len(data), _WORD.size)
    ]
