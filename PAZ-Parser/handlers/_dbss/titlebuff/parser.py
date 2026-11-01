"""Parser for `titlebufflist.dbss`, the Title Effects tiers.

One block per tier, found through `titlebufflistoffset.dbss`:

    u32 tier_id | u32 required_titles | u8 unknown_08 | u8 unknown_09
    | u16 unknown_0a | u64 n + utf16 label_kr | u64 n + utf16 effect_kr
    | u32 reserved

`label_kr` reads "칭호 50개 습득 : " and `effect_kr` holds the bonuses with
their values in PA colour tags. Full layout in
docs/file-formats/dbss/titlebufflist_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader
from .model import TitleBuffRecord

_HEAD = struct.Struct("<IIBBH")
_RESERVED_SIZE = 4


def _parse_tier(data: bytes, offset: int, size: int, tier_id: int) -> TitleBuffRecord:
    reader = RecordReader(data, offset, offset + size, f"title effect tier {tier_id}")
    _, required_titles, unknown_08, unknown_09, unknown_0a = reader.unpack(_HEAD)
    label_kr = reader.text(wide=True)
    effect_kr = reader.text(wide=True)
    reader.skip(_RESERVED_SIZE)
    if not reader.at_end():
        raise ValueError(f"title effect tier {tier_id} has {reader.remaining()} unread bytes")
    return TitleBuffRecord(
        tier_id=tier_id,
        offset=offset,
        required_titles=required_titles,
        unknown_08=unknown_08,
        unknown_09=unknown_09,
        unknown_0a=unknown_0a,
        label_kr=label_kr,
        effect_kr=effect_kr,
    )


def parse_titlebuff_records(
    data: bytes,
    offset_map: dict[int, tuple[int, int]],
) -> list[TitleBuffRecord]:
    """Every tier in tier order."""
    return [
        _parse_tier(data, offset, size, tier_id)
        for tier_id, (offset, size) in sorted(offset_map.items())
    ]
