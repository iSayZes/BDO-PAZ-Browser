"""`tax.bss`: the tax bounds of each territory, per tax type.

    PABR | u32 row_count | row_count x Row | string table
    | u32 table_start | u32 0
    Row (100 bytes): i16 territory_key | i16 territory_key_dup | 8 x Tax
    Tax (12 bytes): i32 min_percent_or_price | i32 max_percent_or_price
    | i32 system_percent

Full layout in docs/file-formats/bss/tax_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "tax.bss"

_KEYS = struct.Struct("<hh")
_TAX = struct.Struct("<3i")
# pa::Array<gc::TaxStaticStatus::value, 8> in the 2016 gc::TaxStaticStatus.
TAX_TYPE_COUNT = 8
ROW_SIZE = _KEYS.size + TAX_TYPE_COUNT * _TAX.size


def _row_records(data: bytes, start: int) -> list[dict]:
    """One record per tax type of the row at `start`."""
    territory_key, territory_key_dup = _KEYS.unpack_from(data, start)
    records: list[dict] = []
    for tax_type in range(TAX_TYPE_COUNT):
        minimum, maximum, system = _TAX.unpack_from(data, start + _KEYS.size + tax_type * _TAX.size)
        records.append(
            {
                "territory_key": territory_key,
                "territory_key_dup": territory_key_dup,
                "tax_type": tax_type,
                "min_percent_or_price": minimum,
                "max_percent_or_price": maximum,
                "system_percent": system,
            }
        )
    return records


def parse_tax_records(data: bytes) -> list[dict]:
    """One record per territory and tax type, in file order.

    `tax_type` is the index of the entry in the row's `taxes` array. Raises
    ValueError on a bad magic or when the rows do not end where the string
    table starts.
    """
    return [record for start in fixed_row_offsets(data, ROW_SIZE, FILE_NAME) for record in _row_records(data, start)]
