"""`skillcommand.dbss`: the key commands the Skill Guide widget shows for each skill.

    u32 count | count x row
    row: u16 skill_no | u16 skill_no_dup | str16 command_kr | str16 name_kr
         | str16 icon_path | u32 pc_level_for_learning | u8 show_check
         | u8 awaken_command | u8 extra_param | u32 unknown_icon_path_07
         | str16 console_command_kr

A str16 is a u64 count of UTF-16LE code units, then the text.
`skillcommandoffset.dbss` (u32 count, then u16 skill number, offset and size
per row) points 2 bytes into a row, at `skill_no_dup`. Layout 4 in
docs/file-formats/dbss/skillcommand_dbss.md; the older Layouts 1 to 3 lack
`extra_param`, then `console_command_kr`, then `skill_no_dup`, and this
parser does not read them.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "skillcommand.dbss"
OFFSET_FILE = "skillcommandoffset.dbss"
KEY_FIELD = "skill_no"

_KEYS = struct.Struct("<HH")
_TAIL = struct.Struct("<IBBBI")
_TAIL_FIELDS = ("pc_level_for_learning", "show_check", "awaken_command", "extra_param", "unknown_icon_path_07")


def _read_row(reader: RecordReader) -> dict:
    skill_no, skill_no_dup = reader.unpack(_KEYS)
    command_kr = reader.text(wide=True)
    name_kr = reader.text(wide=True)
    icon_path = reader.text(wide=True)
    tail = dict(zip(_TAIL_FIELDS, reader.unpack(_TAIL), strict=True))
    return {
        KEY_FIELD: skill_no,
        "skill_no_dup": skill_no_dup,
        "command_kr": command_kr,
        "name_kr": name_kr,
        "icon_path": icon_path,
        **tail,
        "console_command_kr": reader.text(wide=True),
    }


def parse_skillcommand_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_skillcommandoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
