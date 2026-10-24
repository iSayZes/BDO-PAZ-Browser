"""`intimacyinfo.bss`: what an NPC offers at an amity level (the dialog's amity list).

    PABR | u32 row_count | row_count x row | u32 string_count (0)
    | u32 table_start | u32 0
    row: u16 character_key | u32 info_count | info_count x info
    info (26 bytes): u16 character_key | i32 intimacy | u32 type_index
         | u32 operator_type | u32 knowledge_key
         | u16 quest_group (type 0) or dialog_index (other types) | u16 quest_id
         | u32 unknown_quest_id_02

Layout 1 in docs/file-formats/intimacyinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "intimacyinfo.bss"
KEY_FIELD = "character_key"
# eIntimacyInformationTypeInfo_Quest: the u16 at +0x12 is the quest group;
# on the other types it is the NPC's dialog index.
QUEST_TYPE = 0

_ROW_HEAD = struct.Struct("<HI")
_INFO = struct.Struct("<HiIIIHHI")


def _info(values: tuple) -> dict:
    character_key, intimacy, type_index, operator_type, knowledge_key, group_or_dialog, quest_id, unknown = values
    info = {
        "character_key": character_key,
        "intimacy": intimacy,
        "type_index": type_index,
        "operator_type": operator_type,
        "knowledge_key": knowledge_key,
    }
    if type_index == QUEST_TYPE:
        info["quest_group"] = group_or_dialog
    else:
        info["dialog_index"] = group_or_dialog
    return {**info, "quest_id": quest_id, "unknown_quest_id_02": unknown}


def parse_intimacyinfo_records(data: bytes) -> list[dict]:
    """One record per NPC, with its amity entries in file order.

    Raises ValueError on a bad magic, a row that runs into the string table,
    or rows that do not end where it starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE, end, FILE_NAME)
    records = []
    for _ in range(struct.unpack_from("<I", data, 4)[0]):
        character_key, info_count = reader.unpack(_ROW_HEAD)
        infos = [_info(reader.unpack(_INFO)) for _ in range(info_count)]
        records.append({KEY_FIELD: character_key, "infos": infos})
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records
