"""`skillcommand.dbss`: the key commands the Skill Guide widget shows for each skill.

    u32 count | count x row
    row: u16 skill_no | u16 skill_no_dup | str16 command_kr | str16 name_kr
         | str16 icon_path | u32 pc_level_for_learning | u8 show_check
         | u8 awaken_command | u8 extra_param | u32 unknown_icon_path_07
         | str16 console_command_kr

A str16 is a u64 count of UTF-16LE code units, then the text.
`skillcommandoffset.dbss` (u32 count, then u16 skill number, offset and size
per row) points 2 bytes into a row, at `skill_no_dup`. That is Layout 4 in
docs/file-formats/dbss/skillcommand_dbss.md. Going back, Layout 3 (clients
1559 to 1945) has no `extra_param`, Layout 2 also no `console_command_kr` and
Layout 1 also no `skill_no_dup`. A field the row does not hold is None.
Nothing in the file names its layout, so it is read with the first layout,
in client order, whose rows end at the end of the file.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.client_versions import ClientRange, client_order
from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "skillcommand.dbss"
OFFSET_FILE = "skillcommandoffset.dbss"
KEY_FIELD = "skill_no"

_U8 = struct.Struct("<B")
_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
# pc_level_for_learning, show_check, awaken_command
_LEARNING = struct.Struct("<IBB")


@dataclass(frozen=True)
class RowLayout:
    """One documented Row shape; `number` is its Layout N in the doc."""

    number: int
    has_skill_no_dup: bool
    has_extra_param: bool
    has_console_command: bool
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


# Newest first.
LAYOUTS = (
    RowLayout(4, has_skill_no_dup=True, has_extra_param=True, has_console_command=True, clients=(ClientRange(1950),)),
    RowLayout(
        3, has_skill_no_dup=True, has_extra_param=False, has_console_command=True,
        clients=(ClientRange(1559, 1945),),
    ),
    RowLayout(
        2, has_skill_no_dup=True, has_extra_param=False, has_console_command=False,
        clients=(ClientRange(1346, 1554),),
    ),
    RowLayout(
        1, has_skill_no_dup=False, has_extra_param=False, has_console_command=False,
        clients=(ClientRange(1256, 1341),),
    ),
)


def _read_row(reader: RecordReader, layout: RowLayout) -> dict:
    (skill_no,) = reader.unpack(_U16)
    skill_no_dup = reader.unpack(_U16)[0] if layout.has_skill_no_dup else None
    command_kr = reader.text(wide=True)
    name_kr = reader.text(wide=True)
    icon_path = reader.text(wide=True)
    pc_level_for_learning, show_check, awaken_command = reader.unpack(_LEARNING)
    extra_param = reader.unpack(_U8)[0] if layout.has_extra_param else None
    (unknown_icon_path_07,) = reader.unpack(_U32)
    console_command_kr = reader.text(wide=True) if layout.has_console_command else None
    return {
        KEY_FIELD: skill_no,
        "skill_no_dup": skill_no_dup,
        "command_kr": command_kr,
        "name_kr": name_kr,
        "icon_path": icon_path,
        "pc_level_for_learning": pc_level_for_learning,
        "show_check": show_check,
        "awaken_command": awaken_command,
        "extra_param": extra_param,
        "unknown_icon_path_07": unknown_icon_path_07,
        "console_command_kr": console_command_kr,
    }


def parse_skillcommand_records(data: bytes) -> list[dict]:
    """Every row in file order, read with the first layout that fits.

    Raises ValueError, naming where each layout broke, when in every layout a
    row runs past the file or the rows end before it.
    """
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        try:
            return read_counted_records(data, lambda reader: _read_row(reader, layout), FILE_NAME)
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"{FILE_NAME} fits no known layout ({'; '.join(breaks)})")


def parse_skillcommandoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
