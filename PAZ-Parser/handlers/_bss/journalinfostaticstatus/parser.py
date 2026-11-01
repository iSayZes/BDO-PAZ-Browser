"""`journalinfostaticstatus.bss`: the main quest boards of Morning Land and Edania.

    PABR | u32 journal_list_count | journal_list_count x journal list
    | u32 texture_info_count | texture_info_count x u32[21] texture info
    | string table | u32 table_start | u32 0
    journal list: u32 journal_count | journal_count x journal
    journal: u16 chapter_index | u16 ui_type | u16 ui_type_index
             | u16 journal_index | u16 quest_group_no | u16 unknown_0a
             | u32 chapter_string_ref | u32 scenario_desc_ref
             | u32 title_string_ref | u16 unknown_18 | u32 texture_normal_ref
             | u32 texture_over_ref | u32 unknown_22
             | u32[3] detail_btn_texture_id_refs | u32 detail_btn_string_ref
             | u16 unknown_36
             | u32 book_quest_count | book_quest_count x (u32 condition_ref
                   | u16 book_quest_group | u16 book_quest_id | u16 unknown_08)
             | u32 ed_texture_count | ed_texture_count x
                   (u32 texture_normal_ref | u32 texture_over_ref | u16 unknown_08)

The `*_ref` fields and `unknown_22` index the string table; the records
hold their text under the name without `_ref`. Texture info entry `n` is
`ToClient_getJournalTextureInfo(list, n)`. Layout 4 in
docs/file-formats/bss/journalinfostaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "journalinfostaticstatus.bss"
# ToClient_getJournalTextureInfo(list, 0) to (list, 20).
TEXTURE_INFO_SLOTS = 21

_LIST_COUNT_AT = 4
_U32 = struct.Struct("<I")
_HEAD = struct.Struct("<6H3IH")
_TEXTURES = struct.Struct("<7IH")
_BOOK_QUEST = struct.Struct("<IHHH")
_ED_TEXTURE = struct.Struct("<IIH")
_TEXTURE_INFO = struct.Struct(f"<{TEXTURE_INFO_SLOTS}I")


def _read_list(reader: RecordReader, item: struct.Struct, what: str) -> list[tuple]:
    (count,) = reader.unpack(_U32)
    if count * item.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} {what} count {count:,} at 0x{reader.pos - 4:X} runs past the rows")
    return [reader.unpack(item) for _ in range(count)]


def _read_journal(reader: RecordReader, list_index: int, strings: list[str]) -> dict:
    (
        chapter_index, ui_type, ui_type_index, journal_index, quest_group_no, unknown_0a,
        chapter_string, scenario_desc, title_string, unknown_18,
    ) = reader.unpack(_HEAD)
    texture_normal, texture_over, unknown_22, btn_0, btn_1, btn_2, detail_btn_string, unknown_36 = reader.unpack(
        _TEXTURES
    )
    book_quests = [
        {
            "condition": string_at(strings, condition),
            "book_quest_group": group,
            "book_quest_id": quest,
            "unknown_08": unknown_08,
        }
        for condition, group, quest, unknown_08 in _read_list(reader, _BOOK_QUEST, "book quest")
    ]
    ed_textures = [
        {
            "texture_normal": string_at(strings, normal),
            "texture_over": string_at(strings, over),
            "unknown_08": unknown_08,
        }
        for normal, over, unknown_08 in _read_list(reader, _ED_TEXTURE, "ed texture")
    ]
    return {
        "journal_list_index": list_index,
        "chapter_index": chapter_index,
        "ui_type": ui_type,
        "ui_type_index": ui_type_index,
        "journal_index": journal_index,
        "quest_group_no": quest_group_no,
        "unknown_0a": unknown_0a,
        "chapter_string": string_at(strings, chapter_string),
        "scenario_desc": string_at(strings, scenario_desc),
        "title_string": string_at(strings, title_string),
        "unknown_18": unknown_18,
        "texture_normal": string_at(strings, texture_normal),
        "texture_over": string_at(strings, texture_over),
        "unknown_22": string_at(strings, unknown_22),
        "detail_btn_texture_ids": [string_at(strings, index) for index in (btn_0, btn_1, btn_2)],
        "detail_btn_string": string_at(strings, detail_btn_string),
        "unknown_36": unknown_36,
        "book_quests": book_quests,
        "ed_textures": ed_textures,
    }


def parse_journalinfostaticstatus(data: bytes) -> tuple[list[dict], list[list[str]]]:
    """Every journal in file order, and each journal list's 21 texture info strings.

    Raises ValueError on a bad magic, or when a list runs past or ends before
    the string table.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, rows_end, FILE_NAME)
    journals: list[dict] = []
    for list_index in range(u32(data, _LIST_COUNT_AT)):
        (journal_count,) = reader.unpack(_U32)
        journals.extend(_read_journal(reader, list_index, strings) for _ in range(journal_count))
    texture_infos = [
        [string_at(strings, index) for index in entry]
        for entry in _read_list(reader, _TEXTURE_INFO, "texture info")
    ]
    check_rows_end(data, reader.pos, f"{FILE_NAME} lists")
    return journals, texture_infos
