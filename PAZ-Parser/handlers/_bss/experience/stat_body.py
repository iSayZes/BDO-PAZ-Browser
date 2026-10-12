"""The 200-byte stat body of `experience.bss` level records.

`hardcorecharacterstatstaticstatus.bss` rows hold the same body after a u8
class type, and `servantexperience.dbss` records hold it with the mount
values that name `max_hp` and `max_mp`. The `unknown_*` names use offsets
from the start of the body, so every file names a field alike. Layout in
docs/file-formats/experience_bss.md, Stat Body.
"""

from __future__ import annotations

import struct

from _common.binary import whole_float


# max_hp, max_mp, unknown_20, unknown_3c[3], unknown_50, unknown_64[3],
# unknown_70, ap_bonus, dp_bonus. Every skipped byte is 0 on client 3464.
STAT_BODY = struct.Struct("<4xfI20xf24x3I8xf16x3Ifff76x")
STAT_BODY_SIZE = 200
assert STAT_BODY.size == STAT_BODY_SIZE

STAT_FIELDS = (
    "ap_bonus",
    "dp_bonus",
    "max_hp",
    "max_mp",
    "unknown_20",
    "unknown_3c",
    "unknown_50",
    "unknown_64",
    "unknown_70",
)


def stat_fields(values: tuple) -> dict:
    """The record fields of one unpacked `STAT_BODY`."""
    (
        max_hp, max_mp, unknown_20, a3c, b3c, c3c, unknown_50,
        a64, b64, c64, unknown_70, ap_bonus, dp_bonus,
    ) = values
    return {
        "ap_bonus": whole_float(ap_bonus),
        "dp_bonus": whole_float(dp_bonus),
        "max_hp": whole_float(max_hp),
        "max_mp": max_mp,
        "unknown_20": whole_float(unknown_20),
        "unknown_3c": [a3c, b3c, c3c],
        "unknown_50": whole_float(unknown_50),
        "unknown_64": [a64, b64, c64],
        "unknown_70": whole_float(unknown_70),
    }
