"""`commandtooltip.dbss`: the key combination text of each skill tooltip, for keyboard and for console pad.

    u32 count | count x (u32 key_hash | str16 pc_command_kr | str16 console_command_kr | u32)

`key_hash` is `key_hash()` (`_common/string_hash.py`) of the row's string key
(`WARRIOR_01`); the key itself is not stored. `commandtooltipoffset.dbss` is a
`PABR` index (u32 key hash, offset and size per row) that points at the row
start. Layout 1 in docs/file-formats/commandtooltip_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "commandtooltip.dbss"
OFFSET_FILE = "commandtooltipoffset.dbss"
KEY_FIELD = "key_hash"

_U32 = struct.Struct("<I")


def _read_row(reader: RecordReader) -> dict:
    (key,) = reader.unpack(_U32)
    pc_command_kr = reader.text(wide=True)
    console_command_kr = reader.text(wide=True)
    (unknown_tail,) = reader.unpack(_U32)
    return {
        KEY_FIELD: key,
        "pc_command_kr": pc_command_kr,
        "console_command_kr": console_command_kr,
        "unknown_console_command_kr_00": unknown_tail,
    }


def parse_commandtooltip_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when a row runs past the file or the rows do not end at
    its last byte.
    """
    return read_counted_records(data, _read_row, FILE_NAME)
