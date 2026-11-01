"""`quest.dbss` Layout 2 (live client): records walked by scanning for their IDs.

There is no offset table. Records sit back to back from `+0x04`, and record
`i` belongs to packed quest ID `allquestlist[i]`:

    u32 accept_dialog_key | u32 complete_dialog_key | u32 unknown_08 | condition_script | action_script
    | objective_gap | objective_text_kr | u32 quest_category
    Q: u32 packed_quest_id | u32 | u32 list_count | u16 list[] | u32 | u32 | u8 block_kind
    | u32 base_reward_count | 178-byte reward entries | u32 select_reward_count | reward entries
    | ... | icon_path | u8[16 or 8] | u32 packed_quest_id_echo | u8[13] trailer

Strings are a u64 count plus text with no terminator: UTF-16LE for the scripts
and objective, ASCII for the icon. The walk finds `Q` as the record's own
packed ID after the scripts, and the echo as its next occurrence. The objective
is the string that ends at the category right before `Q`. The reward entries
are read by `_common/quest/reward_entry.py`. Full layout in
docs/file-formats/dbss/quest_dbss.md "Layout 2".
"""

from __future__ import annotations

import re
import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.inline_text import decode_inline_text
from _common.prefixed_string import prefixes_ending_at
from _common.quest.reward_entry import RewardEntry, read_reward_list
from _common.record_reader import RecordReader
from .family_stat import family_stats
from .model import QuestRecord


_HEADER_SIZE = 4
_LEAD_SIZE = 12
_COMPLETE_DIALOG_KEY = 4
_STRING_PREFIX_SIZE = 8
_CATEGORY_SIZE = 4
_TRAILER_SIZE = 13
# Bytes from the echo's start to the next record's start.
_ECHO_TO_NEXT = 4 + _TRAILER_SIZE

# The block after Q: unknown_q04, then the counted u16 unknown_list at Q+0x08.
_LIST_COUNT = 0x08
# unknown_list_00, unknown_list_04, block_kind
_AFTER_LIST = struct.Struct("<IIB")

# Bytes between the icon path and the echo.
_POST_ICON_SIZES = (16, 8)
_MAX_ICON_LENGTH = 260

_U32 = struct.Struct("<I")
_STRING_PREFIX = struct.Struct("<II")
_NON_ZERO_BYTE = re.compile(rb"[^\x00]")


@dataclass(frozen=True)
class QuestIndexLayout2:
    """Where each record's parts sit; built once per file by one walk."""

    packed_quest_ids: list[int]
    record_starts: list[int]
    quest_offsets: list[int]
    echo_offsets: list[int]

    def __len__(self) -> int:
        return len(self.record_starts)


def _utf16_end(data: bytes, pos: int) -> int | None:
    """End of the u64-prefixed UTF-16LE string at `pos`, or None when implausible."""
    if pos + _STRING_PREFIX_SIZE > len(data) or u32(data, pos + 4) != 0:
        return None
    end = pos + _STRING_PREFIX_SIZE + 2 * u32(data, pos)
    return end if end <= len(data) else None


def _scripts_end(data: bytes, start: int) -> int | None:
    """End of the action script of a record starting at `start`."""
    condition_end = _utf16_end(data, start + _LEAD_SIZE)
    return None if condition_end is None else _utf16_end(data, condition_end)


def _objective_start(data: bytes, gap_start: int, quest_offset: int) -> int | None:
    """Prefix of the objective string that ends right before the category.

    Returns the lowest prefix position whose UTF-16 text ends exactly there.
    Two shortcuts keep the scan to a few tries: the text is whole UTF-16
    units, so the prefix sits an even distance before the end; and only an
    empty objective has a zero length, so the zero run that opens most gaps
    is skipped up to its first non-zero byte.
    """
    end = quest_offset - _CATEGORY_SIZE
    last = end - _STRING_PREFIX_SIZE
    if last < gap_start:
        return None

    # A length at `pos` covers `pos..pos+3`; below the first non-zero byte it
    # can only be zero, which fits the empty objective at `last` alone.
    first_set = _NON_ZERO_BYTE.search(data, gap_start, last + 4)
    pos = last if first_set is None else max(gap_start, first_set.start() - 3)
    pos += (end - pos) & 1
    for pos in range(pos, last + 1, 2):
        length, high_word = _STRING_PREFIX.unpack_from(data, pos)
        if high_word == 0 and pos + _STRING_PREFIX_SIZE + 2 * length == end:
            return pos
    return None


def _find_quest_offset(data: bytes, start: int, packed_quest_id: int) -> int | None:
    """Position of `packed_quest_id` after the scripts, with a valid objective before it."""
    scripts_end = _scripts_end(data, start)
    if scripts_end is None:
        return None

    key = _U32.pack(packed_quest_id)
    pos = data.find(key, scripts_end)
    while pos >= 0:
        if _objective_start(data, scripts_end, pos) is not None:
            return pos
        pos = data.find(key, pos + 1)
    return None


def _find_echo(data: bytes, quest_offset: int, next_quest_id: int | None) -> int | None:
    """Echo of the packed ID; the next record must parse right after its trailer."""
    key = data[quest_offset:quest_offset + 4]
    pos = data.find(key, quest_offset + 4)
    while pos >= 0:
        next_start = pos + _ECHO_TO_NEXT
        if next_quest_id is None:
            if next_start == len(data):
                return pos
        elif _find_quest_offset(data, next_start, next_quest_id) is not None:
            return pos
        pos = data.find(key, pos + 1)
    return None


def build_quest_index_layout2(data: bytes, allquestlist_ids: list[int]) -> QuestIndexLayout2:
    """Walk every record in `allquestlist.bss` order.

    Raises ValueError when the counts disagree or a record cannot be walked:
    every later record would then start at the wrong byte.
    """
    if len(data) < _HEADER_SIZE:
        raise ValueError("quest.dbss is too small for its header")

    count = u32(data, 0)
    if count != len(allquestlist_ids):
        raise ValueError(
            f"quest.dbss holds {count:,} records but allquestlist.bss lists {len(allquestlist_ids):,}"
        )

    starts: list[int] = []
    quest_offsets: list[int] = []
    echo_offsets: list[int] = []
    start = _HEADER_SIZE
    for row, packed_quest_id in enumerate(allquestlist_ids):
        quest_offset = _find_quest_offset(data, start, packed_quest_id)
        if quest_offset is None:
            raise ValueError(f"quest.dbss record {row} at 0x{start:X} has no ID {packed_quest_id}")

        next_quest_id = allquestlist_ids[row + 1] if row + 1 < count else None
        echo = _find_echo(data, quest_offset, next_quest_id)
        if echo is None:
            raise ValueError(f"quest.dbss record {row} (ID {packed_quest_id}) has no ID echo")

        starts.append(start)
        quest_offsets.append(quest_offset)
        echo_offsets.append(echo)
        start = echo + _ECHO_TO_NEXT

    return QuestIndexLayout2(list(allquestlist_ids), starts, quest_offsets, echo_offsets)


def _read_utf16(data: bytes, pos: int) -> tuple[str, int]:
    end = _utf16_end(data, pos)
    if end is None:
        raise ValueError(f"quest.dbss string at 0x{pos:X} runs past the file")
    return data[pos + _STRING_PREFIX_SIZE:end].decode("utf-16-le", errors="replace"), end


def _icon_path(data: bytes, quest_offset: int, echo: int) -> str:
    """ASCII icon path whose u64 prefix ends 16 or 8 bytes before the echo.

    Returns the highest prefix whose length ends exactly there; path text holds
    no zero bytes, which makes a real icon's prefix the first one tried.
    """
    for post_icon in _POST_ICON_SIZES:
        end = echo - post_icon
        lowest = max(quest_offset, end - _STRING_PREFIX_SIZE - _MAX_ICON_LENGTH)
        for pos in prefixes_ending_at(data, lowest, end, wide=False):
            raw = data[pos + _STRING_PREFIX_SIZE:end]
            if raw.isascii() and raw.lower().endswith(b".dds"):
                return raw.decode("ascii")
    return ""


@dataclass(frozen=True)
class _RewardBlock:
    block_kind: int
    base_rewards: list[RewardEntry]
    select_rewards: list[RewardEntry]


def _reward_block(data: bytes, quest_offset: int, echo: int) -> _RewardBlock:
    """`block_kind` and the two reward lists after `Q`.

    Raises ValueError when a list runs past the echo.
    """
    reader = RecordReader(data, quest_offset + _LIST_COUNT, echo, f"quest.dbss ID at 0x{quest_offset:X}")
    (list_count,) = reader.unpack(_U32)
    reader.skip(2 * list_count)
    _list_00, _list_04, block_kind = reader.unpack(_AFTER_LIST)
    base_rewards = read_reward_list(reader)
    select_rewards = read_reward_list(reader)
    return _RewardBlock(block_kind, base_rewards, select_rewards)


def parse_quest_record_layout2(data: bytes, index: QuestIndexLayout2, row: int) -> QuestRecord:
    start = index.record_starts[row]
    quest_offset = index.quest_offsets[row]
    echo = index.echo_offsets[row]
    packed_quest_id = index.packed_quest_ids[row]

    condition_script, pos = _read_utf16(data, start + _LEAD_SIZE)
    action_script, pos = _read_utf16(data, pos)
    objective_start = _objective_start(data, pos, quest_offset)
    objective_text_kr = "" if objective_start is None else _read_utf16(data, objective_start)[0]
    rewards = _reward_block(data, quest_offset, echo)

    return QuestRecord(
        row=row,
        offset=start,
        size=echo + _ECHO_TO_NEXT - start,
        packed_quest_id=packed_quest_id,
        accept_dialog_key=u32(data, start),
        complete_dialog_key=u32(data, start + _COMPLETE_DIALOG_KEY),
        quest_chain_id=packed_quest_id & 0xFFFF,
        quest_id=packed_quest_id >> 16,
        quest_category=u32(data, quest_offset - _CATEGORY_SIZE),
        block_kind=rewards.block_kind,
        condition_script=condition_script,
        action_script=action_script,
        objective_text_kr=decode_inline_text(objective_text_kr),
        icon_path=_icon_path(data, quest_offset, echo),
        base_rewards=rewards.base_rewards,
        select_rewards=rewards.select_rewards,
        family_stats=family_stats(rewards.base_rewards),
        loc_texts_en=[],
    )


def quest_icon_path_layout2(data: bytes, index: QuestIndexLayout2, row: int) -> str:
    """Icon path of record `row`, found without parsing the rest of the record."""
    return _icon_path(data, index.quest_offsets[row], index.echo_offsets[row])
