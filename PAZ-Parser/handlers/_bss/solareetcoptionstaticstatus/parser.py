"""`solareetcoptionstaticstatus.bss`: five Arena of Solare f32 options.

Five little-endian f32 values and nothing else: no magic, no count, no
string table. No source names them yet, so every field is `unknown_<offset>`.
Layout in docs/file-formats/solareetcoptionstaticstatus_bss.md (Layout 2).
"""

from __future__ import annotations

import struct

from ..pabr_values.handler import VALUE_BYTES_FIELD
from ..pabr_values.tables import ValueField, ValueTable


FILE_NAME = "solareetcoptionstaticstatus.bss"

SOLARE_ETC_OPTION = ValueTable(
    FILE_NAME,
    tuple(ValueField(name, "f") for name in ("unknown_00", "unknown_04", "unknown_08", "unknown_0c", "unknown_10")),
)
FIELDS = tuple(field.name for field in SOLARE_ETC_OPTION.fields)

_VALUES = struct.Struct("<" + "".join(field.fmt for field in SOLARE_ETC_OPTION.fields))
FILE_SIZE = _VALUES.size


def parse_solare_etc_option(data: bytes) -> dict:
    """The one record of the file: each f32 under its doc name, plus the raw bytes as hex.

    Raises ValueError when the file is not the 20 bytes of the current layout.
    """
    if len(data) != FILE_SIZE:
        raise ValueError(f"{FILE_NAME} holds {len(data):,} bytes, not the {FILE_SIZE} of five f32 values")
    values = dict(zip(FIELDS, _VALUES.unpack(data), strict=True))
    return {**values, VALUE_BYTES_FIELD: data.hex(" ")}
