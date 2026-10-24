"""`houseworking.dbss`: the work a worker can do at a house installation (a crafting tool).

    u32 count | count x row
    row: u32 work_count | work_count x (u32 exchange_key, u32 unit_production)
         | u16 install_object_key

The row key sits after the work list. `houseworkingoffset.dbss` (u32
count, then u16 key, offset and size per row) points at the row start.
Layout 2 in docs/file-formats/houseworking_dbss.md; clients before it
store the exchange key as a u16 (Layout 1), which this parser does not read.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "houseworking.dbss"
OFFSET_FILE = "houseworkingoffset.dbss"
KEY_FIELD = "install_object_key"

_U32 = struct.Struct("<I")
_WORK = struct.Struct("<II")
_KEY = struct.Struct("<H")


def _read_row(reader: RecordReader) -> dict:
    (work_count,) = reader.unpack(_U32)
    works = [dict(zip(("exchange_key", "unit_production"), reader.unpack(_WORK))) for _ in range(work_count)]
    (install_object_key,) = reader.unpack(_KEY)
    return {KEY_FIELD: install_object_key, "works": works}


def parse_houseworking_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_houseworkingoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
