"""`elementalstat.bss`: one row per Black Shrine aura (Sun, Moon, Earth).

No PABR magic, no trailer:

    u32 count | count x (u8 element_type | u32 ap_per_orb | u32 dp_per_orb
    | u32 stat_points_per_orb | u8 element_type_dup)

Layout in docs/file-formats/elementalstat_bss.md.
"""

from __future__ import annotations

import struct


FILE_NAME = "elementalstat.bss"

_COUNT = struct.Struct("<I")
# The u8 map key, three u32 values, then the row's own copy of the key.
_ROW = struct.Struct("<BIIIB")

# The client Lua's __eElementalStat_* names in value order, without the prefix.
ELEMENT_TYPE_NAMES: tuple[str, ...] = ("Sun", "Moon", "Land")


def parse_elementalstat(data: bytes) -> list[dict]:
    """One record per row, in file order.

    Raises ValueError when the file is too short for its count, or when the
    rows do not end exactly at the end of the file.
    """
    if len(data) < _COUNT.size:
        raise ValueError(f"{FILE_NAME} is too short for its count")
    (count,) = _COUNT.unpack_from(data, 0)
    end = _COUNT.size + count * _ROW.size
    if end != len(data):
        raise ValueError(f"{FILE_NAME} declares {count} rows ({end} bytes) but holds {len(data)} bytes")
    return [
        {
            "element_type": element_type,
            "ap_per_orb": ap_per_orb,
            "dp_per_orb": dp_per_orb,
            "stat_points_per_orb": stat_points_per_orb,
            "element_type_dup": element_type_dup,
        }
        for element_type, ap_per_orb, dp_per_orb, stat_points_per_orb, element_type_dup in _ROW.iter_unpack(
            data[_COUNT.size :]
        )
    ]
