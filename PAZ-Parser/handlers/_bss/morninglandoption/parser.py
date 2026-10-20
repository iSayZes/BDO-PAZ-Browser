"""Reads `morninglandoption.bss`: two u64 values and one u8, no PABR magic.

The file is the values alone, 17 bytes, with no string table or trailer.
Field names follow `docs/file-formats/morninglandoption_bss.md`.
"""

from __future__ import annotations

import struct

from ..pabr_values.tables import ValueField, ValueTable


FILE_NAME = "morninglandoption.bss"

MORNING_LAND_OPTION = ValueTable(
    FILE_NAME,
    (
        ValueField("stat_reset_cost", "Q", "statResetCost"),
        ValueField("light_orb_reset_cost", "Q", "lightOrbResetCost"),
        ValueField("unknown_10", "B"),
    ),
)

_VALUES = struct.Struct("<" + "".join(field.fmt for field in MORNING_LAND_OPTION.fields))


def parse_morning_land_option(data: bytes) -> dict:
    """The one record of the file.

    Raises ValueError when the file is not exactly the size of the values.
    """
    if len(data) != _VALUES.size:
        raise ValueError(f"{FILE_NAME} expected {_VALUES.size} bytes, got {len(data)}")
    values = _VALUES.unpack(data)
    return {field.name: value for field, value in zip(MORNING_LAND_OPTION.fields, values, strict=True)}
