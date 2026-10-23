"""`olviaacademypassstaticstatusmanager.bss`: the steps of each Olvia Academy Pass tab.

    PABR | Pass[..table_start] passes | u32 string_count | strings | u32 table_start | u32 0
    Pass: u32 pass_size | pass_size x (u32 base_quest | u32 pass_quest)

One pass per `__eOlviaAcademyPassType_*` value, in the order the pass window
walks them (`PASS_TYPE_NAMES`). The passes have no count: they run up to the
string table, which holds no strings.

Layout 1 in docs/file-formats/olviaacademypassstaticstatusmanager_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_structs
from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "olviaacademypassstaticstatusmanager.bss"
# The pass types in value order from __eOlviaAcademyPassType_Collect up to _Count,
# without the prefix (panel_window_olviaacademy_pass_all.luac).
PASS_TYPE_NAMES: tuple[str, ...] = ("Collect", "Fish", "Hunt", "Cook", "Alchemy", "Work", "Train", "Farm", "Ship")

# The passes follow the PABR magic.
_PASSES_START = 4
_STEP = struct.Struct("<II")
_STEP_FIELDS = ("base_quest", "pass_quest")


def _read_pass(reader: RecordReader, pass_type: int) -> list[dict]:
    steps = read_counted_structs(reader, _STEP, _STEP_FIELDS, f"{FILE_NAME} pass {pass_type} step")
    return [
        {"pass_type": pass_type, "pass_size": len(steps), "quest_index": quest_index, **step}
        for quest_index, step in enumerate(steps)
    ]


def parse_pass_records(data: bytes) -> list[dict]:
    """One record per step (`ToClient_GetOlviaAcademyQuest(passType, questIndex, ...)`), pass by pass.

    `pass_type` is the pass's position in the file. Raises ValueError on a bad
    PABR magic or trailer, or when a step count runs past the string table.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, _PASSES_START, table_start, FILE_NAME)
    records: list[dict] = []
    pass_type = 0
    while not reader.at_end():
        records += _read_pass(reader, pass_type)
        pass_type += 1
    return records
