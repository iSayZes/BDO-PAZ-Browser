"""`edaniaregioninfo.bss`: one row per Edania region (castle domain) and a "none" row.

    PABR | u32 count | count x 9-byte row | u32 0 (empty string table)
    | u32 string_table_start | u32 0

A row is the region map colour and a copy, each 3 bytes and a zero byte, and the
`__eEdaniaRegion` value at +0x08. Full layout in docs/file-formats/bss/edaniaregioninfo_bss.md.
"""

from __future__ import annotations

from _common.binary import u8, u32
from _common.pabr_strings import fixed_row_offsets, string_table_start


ROW_SIZE = 9

# Row field offsets.
_MAP_COLOR = 0x00
_UNKNOWN_04 = 0x04
_EDANIA_REGION = 0x08
_RGB_SIZE = 3

# The __eEdaniaRegion names in value order, without the prefix. The client Lua
# lists them in this order and loops 0..Zephyros for the first Edana group and
# Aphrodon..Count-1 for the second; the value after Voidekaia is _Count, which
# ToClient_GetEdaniaRegion returns for "no Edania region".
EDANIA_REGION_NAMES: tuple[str, ...] = (
    "Aetherion", "Nymphamare", "Orbita", "Tenebraum", "Zephyros",
    "Aphrodon", "Hermesia", "Magaia", "Aresion", "Voidekaia",
)


def _rgb_hex(data: bytes, offset: int) -> str:
    """Three bytes stored blue, green, red as `rrggbb`, the way regioninfo.bss reads its colour."""
    return data[offset : offset + _RGB_SIZE][::-1].hex()


def _parse_row(data: bytes, pos: int) -> dict:
    return {
        "edania_region": u8(data, pos + _EDANIA_REGION),
        "map_color": _rgb_hex(data, pos + _MAP_COLOR),
        "unknown_04": _rgb_hex(data, pos + _UNKNOWN_04),
    }


def parse_edaniaregioninfo_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a missing magic or a row count that does not end
    where the trailer says the string table starts.
    """
    return [_parse_row(data, pos) for pos in fixed_row_offsets(data, ROW_SIZE, "edaniaregioninfo.bss")]
