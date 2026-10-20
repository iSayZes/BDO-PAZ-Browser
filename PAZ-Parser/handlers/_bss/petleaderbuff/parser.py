"""`petleaderbuff.bss`: the alpha pet loot cooldown cut per pet tier.

No PABR magic and no trailer: a u32 entry count, then 6-byte entries of
u8 `pet_tier`, u8 `unknown_01` and u32 `leader_buff_rate` (1,000,000 = 100%).
Full layout in docs/file-formats/petleaderbuff_bss.md.
"""

from __future__ import annotations

import struct


_COUNT = struct.Struct("<I")
_ENTRY = struct.Struct("<BBI")


def parse_petleaderbuff_records(data: bytes) -> list[dict]:
    """One record per entry. Raises ValueError when the entries do not fill the file."""
    if len(data) < _COUNT.size:
        raise ValueError(f"petleaderbuff.bss: {len(data)} bytes, too short for the entry count")
    (count,) = _COUNT.unpack_from(data, 0)
    expected = _COUNT.size + count * _ENTRY.size
    if len(data) != expected:
        raise ValueError(
            f"petleaderbuff.bss: {count} entries need {expected} bytes, the file has {len(data)}"
        )
    return [
        {"pet_tier": pet_tier, "unknown_01": unknown_01, "leader_buff_rate": leader_buff_rate}
        for pet_tier, unknown_01, leader_buff_rate in _ENTRY.iter_unpack(data[_COUNT.size :])
    ]
