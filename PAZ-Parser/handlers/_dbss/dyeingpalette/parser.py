"""`dyeingpalette.dbss`: the colours of every dye palette.

    u32 count | count x Row
    Row: u8 palette_type | u8 unknown_01 | u64 color_count | Color[color_count]
    Color (12 bytes): u8 color_b | u8 color_g | u8 color_r | u8 color_a
                      | f32 environment | f32 specular

A colour's position in its row is the `palette_index` that
`itempalette.dbss` stores. `dyeingpaletteoffset.dbss` (u32 count, then u8
palette type, u32 offset, u32 size per row) points 1 byte into a row, at
`unknown_01`. Layout 1 in docs/file-formats/dbss/dyeingpalette_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "dyeingpalette.dbss"
OFFSET_FILE = "dyeingpaletteoffset.dbss"

COUNT_SIZE = 4
# palette_type, unknown_01, color_count
_HEAD = struct.Struct("<BBQ")
_COLOR = struct.Struct("<4Bff")
COLOR_SIZE = _COLOR.size
_COLOR_FIELDS = ("color_b", "color_g", "color_r", "color_a", "environment", "specular")


def _read_row(reader: RecordReader) -> dict:
    palette_type, unknown_01, color_count = reader.unpack(_HEAD)
    colors = [dict(zip(_COLOR_FIELDS, reader.unpack(_COLOR), strict=True)) for _ in range(color_count)]
    return {"palette_type": palette_type, "unknown_01": unknown_01, "color_count": color_count, "colors": colors}


def parse_dyeingpalette_rows(data: bytes) -> list[dict]:
    """Every palette in file order, its colours under `colors`.

    Raises ValueError when a row runs past the file or the rows do not end at
    its last byte.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    reader = RecordReader(data, COUNT_SIZE, len(data), FILE_NAME)
    rows = [_read_row(reader) for _ in range(count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} has {reader.remaining():,} bytes after its {count:,} rows")
    return rows
