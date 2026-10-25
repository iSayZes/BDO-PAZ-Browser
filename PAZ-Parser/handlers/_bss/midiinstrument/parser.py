"""`midiinstrument.bss`: the instruments of the music composer.

    PABR | u32 row_count | row_count x row | u32 action_hash_count
    | action_hash_count x u32 | String Table | u32 string_table_start | u32 0
    row: u8 index | u32 bank_name | u32 event_name | u32 ingame_name
         | u64 articulation_count | articulation_count x u8 articulations
         | u32 start_action_hash | u32 end_action_hash | u8 advanced_type
         | u32 instrument_name_type | u8 is_opened | u32 ing_action_count
         | ing_action_count x u32 ing_action_hashes | u8 is_provided
         | u8 unknown_ing_action_hashes_01 | u8 unknown_ing_action_hashes_02
         | u8 unknown_ing_action_hashes_03

`bank_name`, `event_name`, `ingame_name` and `instrument_name_type` index
the string table; the record carries their text as `<field>_text`. The
action hashes are `ascii_key_hash` of action names. Layout 4 in
docs/file-formats/bss/midiinstrument_bss.md. Layouts 1 to 3 (client 1838 and older,
without the three trailing bytes) are not read.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.counted_rows import read_counted_u32s
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "midiinstrument.bss"
KEY_FIELD = "index"
STRING_FIELDS = ("bank_name", "event_name", "ingame_name", "instrument_name_type")

_COUNT_OFFSET = 4
_HEAD = struct.Struct("<BIIIQ")
_ACTIONS = struct.Struct("<IIBIBI")
_TAIL = struct.Struct("<4B")


def _read_row(reader: RecordReader, strings: list[str]) -> dict:
    index, bank_name, event_name, ingame_name, articulation_count = reader.unpack(_HEAD)
    articulations = list(reader.unpack(struct.Struct(f"<{articulation_count}B")))
    start_hash, end_hash, advanced_type, instrument_name_type, is_opened, ing_count = reader.unpack(_ACTIONS)
    ing_hashes = list(reader.unpack(struct.Struct(f"<{ing_count}I")))
    is_provided, unknown_01, unknown_02, unknown_03 = reader.unpack(_TAIL)
    record = {
        KEY_FIELD: index,
        "bank_name": bank_name,
        "event_name": event_name,
        "ingame_name": ingame_name,
        "articulation_count": articulation_count,
        "articulations": articulations,
        "start_action_hash": start_hash,
        "end_action_hash": end_hash,
        "advanced_type": advanced_type,
        "instrument_name_type": instrument_name_type,
        "is_opened": is_opened,
        "ing_action_count": ing_count,
        "ing_action_hashes": ing_hashes,
        "is_provided": is_provided,
        "unknown_ing_action_hashes_01": unknown_01,
        "unknown_ing_action_hashes_02": unknown_02,
        "unknown_ing_action_hashes_03": unknown_03,
    }
    return {**record, **{f"{field}_text": string_at(strings, record[field]) for field in STRING_FIELDS}}


def parse_midiinstrument(data: bytes) -> tuple[list[dict], list[int]]:
    """Every instrument in file order, with the text of its string indexes, and the action hash list.

    Raises ValueError on a missing magic, a row that runs into the string
    table, or an action hash list that does not end where the string table
    starts.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, table_start, FILE_NAME)
    records = [_read_row(reader, strings) for _ in range(u32(data, _COUNT_OFFSET))]
    hashes = read_counted_u32s(reader, f"{FILE_NAME} action hashes")
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} action hashes end at 0x{reader.pos:X}, the string table starts at 0x{table_start:X}")
    return records, hashes


def parse_midiinstrument_records(data: bytes) -> list[dict]:
    """The instruments of `parse_midiinstrument()`."""
    return parse_midiinstrument(data)[0]
