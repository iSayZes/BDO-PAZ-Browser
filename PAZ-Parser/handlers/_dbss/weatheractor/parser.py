"""`weatheractor.dbss`: the characters tied to the weather system.

A u32 row count, then 75-byte rows with no `PABR` magic and no string
table: a u16 key, the character key, the weather type, the radius, rain,
cloud and damage values, a skill key with its apply rate, and a few fields
whose meaning is open. `weatheractoroffset.dbss`
points 2 bytes into each row, past its key. Layout in
docs/file-formats/weatheractor_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


# gc::EWeatherType member names of the 2016 client (eWeatherType_ prefix
# dropped); the file also stores 3 and 4, which came later.
WEATHER_TYPE_NAMES: tuple[str, ...] = ("Cyclone", "DesertWind", "Weather")

FILE_NAME = "weatheractor.dbss"
OFFSET_FILE = "weatheractoroffset.dbss"

_COUNT_SIZE = 4
_ROW = struct.Struct("<HBHB7fIIIf12sHfH4sB")
_FIELDS = (
    "key",
    "unknown_02",
    "character_key",
    "weather_type",
    "radius",
    "rain_amount",
    "cloud_rate",
    "damage_max",
    "damage_radius",
    "damage_radius_rate",
    "push_pull_speed",
    "skill_key",
    "skill_apply_rate",
    "unknown_2a",
    "unknown_2e",
    "unknown_32",
    "unknown_3e",
    "unknown_40",
    "unknown_44",
    "unknown_46",
    "unknown_4a",
)


def parse_weatheractor_records(data: bytes) -> list[dict]:
    """Every row, in file order; byte runs become hex text.

    Raises ValueError when the file is not exactly the count and its rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    expected_size = _COUNT_SIZE + count * _ROW.size
    if len(data) != expected_size:
        raise ValueError(
            f"{FILE_NAME} declares {count:,} rows ({expected_size:,} bytes) but holds {len(data):,} bytes"
        )

    return [
        {field: value.hex() if isinstance(value, bytes) else value for field, value in zip(_FIELDS, row)}
        for row in _ROW.iter_unpack(data[_COUNT_SIZE:])
    ]
