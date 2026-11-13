"""`commandtooltip.dbss`: the key combination text of each skill tooltip, for keyboard and for console pad.

    u32 count | count x (u32 key_hash | str16 pc_command_kr | str16 console_command_kr | u32)

`key_hash` is `key_hash()` (`_common/string_hash.py`) of the row's string key
(`WARRIOR_01`, a `skilltype.dbss` `pattern_control`); the key itself is not
stored. `commandtooltipoffset.dbss` is a `PABR` index (u32 key hash, offset
and size per row) that points at the row start. That is Layout 2 in
docs/file-formats/dbss/commandtooltip_dbss.md; Layout 1 (clients 1239 to
1524) has no `console_command_kr`, which is then None. Nothing in the file
names its layout, so it is read with the first layout, in client order, whose
rows end at the end of the file.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.client_versions import ClientRange, client_order
from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "commandtooltip.dbss"
OFFSET_FILE = "commandtooltipoffset.dbss"
KEY_FIELD = "key_hash"

_U32 = struct.Struct("<I")


@dataclass(frozen=True)
class RowLayout:
    """One documented Row shape; `number` is its Layout N in the doc."""

    number: int
    has_console_command: bool
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


# Newest first.
LAYOUTS = (
    RowLayout(2, has_console_command=True, clients=(ClientRange(1529),)),
    RowLayout(1, has_console_command=False, clients=(ClientRange(1239, 1524),)),
)


def _read_row(reader: RecordReader, layout: RowLayout) -> dict:
    (key,) = reader.unpack(_U32)
    pc_command_kr = reader.text(wide=True)
    console_command_kr = reader.text(wide=True) if layout.has_console_command else None
    (unknown_tail,) = reader.unpack(_U32)
    return {
        KEY_FIELD: key,
        "pc_command_kr": pc_command_kr,
        "console_command_kr": console_command_kr,
        "unknown_console_command_kr_00": unknown_tail,
    }


def parse_commandtooltip_records(data: bytes) -> list[dict]:
    """Every row in file order, read with the first layout that fits.

    Raises ValueError, naming where each layout broke, when in every layout a
    row runs past the file or the rows do not end at its last byte.
    """
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        try:
            return read_counted_records(data, lambda reader: _read_row(reader, layout), FILE_NAME)
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"{FILE_NAME} fits no known layout ({'; '.join(breaks)})")
