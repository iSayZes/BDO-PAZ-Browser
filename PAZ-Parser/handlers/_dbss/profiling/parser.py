"""`profiling.dbss`: the information messages a dialog hands out, per profiling key.

    u32 count | count x row
    row: u16 profiling_key | u32 info_count | info_count x info
         | u32 unknown_infos_00
    info: str16 profile_message_kr | str16 execute

`execute` is the reward script (`pushitem(34023,0,1);`), empty on most infos.
`profilingoffset.dbss` (u32 count, then u16 key, u32 offset and u32 size per
row, no PABR magic) points at the row start. Layout 1 in
docs/file-formats/profiling_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "profiling.dbss"
OFFSET_FILE = "profilingoffset.dbss"
KEY_FIELD = "profiling_key"

_HEAD = struct.Struct("<HI")
_U32 = struct.Struct("<I")
# A u64 length per string: the least an info can take.
_MIN_INFO_SIZE = 16


def _read_info(reader: RecordReader) -> dict:
    return {
        "profile_message_kr": reader.text(wide=True),
        "execute": reader.text(wide=True),
    }


def _read_row(reader: RecordReader) -> dict:
    profiling_key, info_count = reader.unpack(_HEAD)
    if info_count * _MIN_INFO_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME} key {profiling_key} info count {info_count:,} runs past the file")
    infos = [_read_info(reader) for _ in range(info_count)]
    (unknown_infos_00,) = reader.unpack(_U32)
    return {KEY_FIELD: profiling_key, "infos": infos, "unknown_infos_00": unknown_infos_00}


def parse_profiling_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_profilingoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: profiling key, row offset and row size. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
