"""`olviaacademycurriculumss.bss`: the curricula and family rewards of the Olvia Academy main window.

    u32 curriculum_count | Curriculum[curriculum_count]
    | u32 reward_count | Reward[reward_count]
    Curriculum: str16 curriculum_title | str8 curriculum_icon | u32 subject_count | Subject[subject_count]
    Subject: u32 preview_text_count | str16[preview_text_count] preview_texts
             | (str16 preview_title | str16 preview_desc | str8 preview_texture_id, only after a text)
             | u32 start_quest | str16 subject_title | str16 subject_desc
             | u32 quest_count | quest_count x (u32 quest | str8 quest_texture_id)
    Reward: str16 reward_title | str16 reward_sub_title | str16 reward_desc | str8 reward_icon
            | u32 reward_group_count | reward_group_count x (str16 reward_group_title | u32 quest_count | u32[quest_count] quests)

str16 is a u64 count and UTF-16LE text, str8 a u64 count and ASCII text.
Every title, description and preview text is a RESOURCE sheet key; every
quest a packed quest ID. No PABR magic, no string table.

Layout 1 in docs/file-formats/olviaacademycurriculumss_bss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Callable

from _common.counted_rows import read_counted_u32s
from _common.record_reader import RecordReader


FILE_NAME = "olviaacademycurriculumss.bss"
CURRICULUM_SECTION = "curriculum"
REWARD_SECTION = "reward"

_U32 = struct.Struct("<I")
# The fewest bytes one entry of each list takes (its fixed part in the doc); a
# count whose entries cannot fit in the rest of the file raises before the read.
_STRING_HEAD = 8
_SUBJECT_QUEST_MIN = 12
_SUBJECT_MIN = 28
_CURRICULUM_MIN = 20
_REWARD_MIN = 36
_REWARD_GROUP_MIN = 12


def row_ref(section: str, parent_index: int, index: int) -> str:
    """The key of one record, `curriculum:1:0` or `reward:1:3`: section, then the two Lua indexes from 0."""
    return f"{section}:{parent_index}:{index}"


def _count(reader: RecordReader, what: str, min_size: int) -> int:
    """A u32 count of items at least `min_size` bytes each; raises when they cannot fit."""
    (count,) = reader.unpack(_U32)
    if count * min_size > reader.remaining():
        raise ValueError(f"{FILE_NAME} {what} count {count:,} at 0x{reader.pos - _U32.size:X} runs past the file")
    return count


def _wide(reader: RecordReader) -> str:
    return reader.text(wide=True)


def _ascii(reader: RecordReader) -> str:
    return reader.text(wide=False)


def _read_preview(reader: RecordReader) -> dict:
    """The preview page of a subject: its texts, then title, description and texture after the first text."""
    texts = [_wide(reader) for _ in range(_count(reader, "preview text", _STRING_HEAD))]
    if not texts:
        return {"preview_texts": [], "preview_title": "", "preview_desc": "", "preview_texture_id": ""}
    return {
        "preview_texts": texts,
        "preview_title": _wide(reader),
        "preview_desc": _wide(reader),
        "preview_texture_id": _ascii(reader),
    }


def _read_subject_quests(reader: RecordReader) -> list[dict]:
    quests: list[dict] = []
    for _ in range(_count(reader, "subject quest", _SUBJECT_QUEST_MIN)):
        (quest,) = reader.unpack(_U32)
        quests.append({"quest": quest, "quest_texture_id": _ascii(reader)})
    return quests


def _read_subject(reader: RecordReader, head: dict, index: int) -> dict:
    preview = _read_preview(reader)
    (start_quest,) = reader.unpack(_U32)
    subject_title = _wide(reader)
    subject_desc = _wide(reader)
    quests = _read_subject_quests(reader)
    return {
        "section": CURRICULUM_SECTION,
        "row_ref": row_ref(CURRICULUM_SECTION, head["curriculum_index"], index),
        **head,
        "subject_index": index,
        **preview,
        "start_quest": start_quest,
        "subject_title": subject_title,
        "subject_desc": subject_desc,
        "quests": [quest["quest"] for quest in quests],
        "quest_texture_ids": [quest["quest_texture_id"] for quest in quests],
    }


def _read_curriculum(reader: RecordReader, index: int) -> list[dict]:
    head = {
        "curriculum_index": index,
        "curriculum_title": _wide(reader),
        "curriculum_icon": _ascii(reader),
    }
    return [_read_subject(reader, head, subject) for subject in range(_count(reader, "subject", _SUBJECT_MIN))]


def _read_reward(reader: RecordReader, index: int) -> list[dict]:
    head = {
        "reward_index": index,
        "reward_title": _wide(reader),
        "reward_sub_title": _wide(reader),
        "reward_desc": _wide(reader),
        "reward_icon": _ascii(reader),
    }
    groups: list[dict] = []
    for group in range(_count(reader, "reward group", _REWARD_GROUP_MIN)):
        reward_group_title = _wide(reader)
        quests = read_counted_u32s(reader, f"{FILE_NAME} reward {index} group {group} quest")
        groups.append({
            "section": REWARD_SECTION,
            "row_ref": row_ref(REWARD_SECTION, index, group),
            **head,
            "reward_group_index": group,
            "reward_group_title": reward_group_title,
            "quests": quests,
        })
    return groups


def _read_section(reader: RecordReader, what: str, min_size: int, read: Callable[[RecordReader, int], list[dict]]) -> list[dict]:
    return [record for index in range(_count(reader, what, min_size)) for record in read(reader, index)]


def parse_curriculum_records(data: bytes) -> list[dict]:
    """One record per subject (`section` curriculum), then one per reward group (`section` reward).

    Each record carries its curriculum's or reward's fields. Raises ValueError
    when a count or string runs past the file or the rewards end before it.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    records = _read_section(reader, "curriculum", _CURRICULUM_MIN, _read_curriculum)
    records += _read_section(reader, "reward", _REWARD_MIN, _read_reward)
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} rewards end at 0x{reader.pos:X}, the file at 0x{len(data):X}")
    return records
