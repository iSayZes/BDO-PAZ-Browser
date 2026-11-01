"""`quest.dbss` Layout 1 (clients 1717 to 2000): every record read field by field.

Records sit back to back from `+0x04` in `allquestlist.bss` order, as in
Layout 2, but nothing needs a scan:

    u32 accept_dialog_key | u32 complete_dialog_key | str16 | u32
    | condition_script | action_script | objective_text_kr | str16 | u8
    | base_rewards | select_rewards | unknown_rewards (188-byte entries) | 25 bytes
    | str16 title | str16 description | u32 count, 16-byte entries
    | str8 icon_path | str8 | u32 count, links | 4 x str16 dialog
    | u32 | u8 block_kind | u8 | u32 | u32 quest_category | u32
    | u32 packed_quest_id | 5 bytes | u32 count, u32[] | 14 bytes

Full layout in docs/file-formats/dbss/quest_dbss.md "Layout 1".
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.inline_text import decode_inline_text
from _common.quest.reward_entry import REWARD_ENTRY_LAYOUT_1, read_reward_list
from _common.record_reader import RecordReader
from .family_stat import family_stats
from .model import QuestRecord


_HEADER_SIZE = 4

_DIALOG_KEYS = struct.Struct("<II")
_U8 = struct.Struct("<B")
_U32 = struct.Struct("<I")
# unknown_rewards_00 to unknown_rewards_18.
_AFTER_REWARDS_SIZE = 25
_POSITION_SIZE = 16
# unknown_old_dialogs_00, block_kind, unknown_old_dialogs_05,
# unknown_old_dialogs_06, quest_category, unknown_old_dialogs_0e
_BEFORE_QUEST_ID = struct.Struct("<IBBIII")
# unknown_old_quest_04 to unknown_old_quest_08
_AFTER_QUEST_ID_SIZE = 5
_TRAILER_SIZE = 14
# Text, icon and dialog strings between the reward lists and the quest ID.
_TITLE_TEXTS = 2
_DIALOG_TEXTS = 4


@dataclass(frozen=True)
class QuestIndexLayout1:
    """Where each record starts; built once per file by one walk."""

    packed_quest_ids: list[int]
    record_starts: list[int]

    def __len__(self) -> int:
        return len(self.record_starts)


def _skip_texts(reader: RecordReader, count: int, *, wide: bool) -> None:
    for _ in range(count):
        reader.text(wide=wide)


def _skip_counted(reader: RecordReader, entry_size: int) -> None:
    (count,) = reader.unpack(_U32)
    reader.skip(count * entry_size)


def _skip_links(reader: RecordReader) -> None:
    """u32 count of (u8 key, u32 count of (str8, str16)) groups."""
    (groups,) = reader.unpack(_U32)
    for _ in range(groups):
        reader.unpack(_U8)
        (pairs,) = reader.unpack(_U32)
        for _ in range(pairs):
            reader.text(wide=False)
            reader.text(wide=True)


def _read_record(data: bytes, start: int, row: int) -> QuestRecord:
    """Record `row` at `start`; raises ValueError when a field runs past the file."""
    reader = RecordReader(data, start, len(data), f"quest.dbss record {row} at 0x{start:X}")
    accept_dialog_key, complete_dialog_key = reader.unpack(_DIALOG_KEYS)
    reader.text(wide=True)
    reader.unpack(_U32)
    condition_script = reader.text(wide=True)
    action_script = reader.text(wide=True)
    objective_text_kr = reader.text(wide=True)
    reader.text(wide=True)
    reader.unpack(_U8)
    base_rewards = read_reward_list(reader, REWARD_ENTRY_LAYOUT_1)
    select_rewards = read_reward_list(reader, REWARD_ENTRY_LAYOUT_1)
    read_reward_list(reader, REWARD_ENTRY_LAYOUT_1)
    reader.skip(_AFTER_REWARDS_SIZE)
    _skip_texts(reader, _TITLE_TEXTS, wide=True)
    _skip_counted(reader, _POSITION_SIZE)
    icon_path = reader.text(wide=False)
    reader.text(wide=False)
    _skip_links(reader)
    _skip_texts(reader, _DIALOG_TEXTS, wide=True)
    _repeat, block_kind, _flag, _value_06, quest_category, _value_0e = reader.unpack(_BEFORE_QUEST_ID)
    (packed_quest_id,) = reader.unpack(_U32)
    reader.skip(_AFTER_QUEST_ID_SIZE)
    _skip_counted(reader, _U32.size)
    reader.skip(_TRAILER_SIZE)

    return QuestRecord(
        row=row,
        offset=start,
        size=reader.pos - start,
        packed_quest_id=packed_quest_id,
        accept_dialog_key=accept_dialog_key,
        complete_dialog_key=complete_dialog_key,
        quest_chain_id=packed_quest_id & 0xFFFF,
        quest_id=packed_quest_id >> 16,
        quest_category=quest_category,
        block_kind=block_kind,
        condition_script=condition_script,
        action_script=action_script,
        objective_text_kr=decode_inline_text(objective_text_kr),
        icon_path=icon_path,
        base_rewards=base_rewards,
        select_rewards=select_rewards,
        family_stats=family_stats(base_rewards),
        loc_texts_en=[],
    )


def build_quest_index_layout1(data: bytes, allquestlist_ids: list[int]) -> QuestIndexLayout1:
    """Read every record in `allquestlist.bss` order.

    Raises ValueError when the counts disagree, a record's `packed_quest_id`
    is not its `allquestlist` ID, or the last record does not end the file.
    """
    if len(data) < _HEADER_SIZE:
        raise ValueError("quest.dbss is too small for its header")
    (count,) = _U32.unpack_from(data)
    if count != len(allquestlist_ids):
        raise ValueError(
            f"quest.dbss holds {count:,} records but allquestlist.bss lists {len(allquestlist_ids):,}"
        )

    starts: list[int] = []
    start = _HEADER_SIZE
    for row, expected_id in enumerate(allquestlist_ids):
        record = _read_record(data, start, row)
        if record["packed_quest_id"] != expected_id:
            raise ValueError(
                f"quest.dbss record {row} at 0x{start:X} holds ID {record['packed_quest_id']}, "
                f"allquestlist.bss lists {expected_id}"
            )
        starts.append(start)
        start += record["size"]
    if start != len(data):
        raise ValueError(f"quest.dbss records end at 0x{start:X}, the file at 0x{len(data):X}")
    return QuestIndexLayout1(list(allquestlist_ids), starts)


def parse_quest_record_layout1(data: bytes, index: QuestIndexLayout1, row: int) -> QuestRecord:
    return _read_record(data, index.record_starts[row], row)
