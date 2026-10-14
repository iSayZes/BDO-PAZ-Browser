"""`quest.dbss`: quest definitions, walked in `allquestlist.bss` order.

There is no offset table. Records sit back to back from `+0x04`, and record
`i` belongs to packed quest ID `allquestlist[i]`:

    u32 accept_dialog_key | u32 complete_dialog_key | u32 unknown_08 | condition_script | action_script
    | objective_gap | objective_text_kr | u32 quest_category
    Q: u32 packed_quest_id | ... | u8 block_kind @ Q+0x14
    | u32 reward_entry_count @ Q+0x15 | 178-byte reward entries | ...
    | icon_path | u8[16 or 8] | u32 packed_quest_id_echo | u8[13] trailer

Strings are a u64 count plus text with no terminator: UTF-16LE for the scripts
and objective, ASCII for the icon. The walk finds `Q` as the record's own
packed ID after the scripts, and the echo as its next occurrence. The objective
is the string that ends at the category right before `Q`. Full layout in
docs/file-formats/quest_dbss.md.
"""

from __future__ import annotations

import re
import struct
from dataclasses import dataclass

from _bss.allquestlist.parser import parse_allquestlist_records
from _common.binary import u32
from _common.inline_text import decode_inline_text
from _common.prefixed_string import prefixes_ending_at
from .model import FamilyStat, QuestRecord


_HEADER_SIZE = 4
_LEAD_SIZE = 12
_COMPLETE_DIALOG_KEY = 4
_STRING_PREFIX_SIZE = 8
_CATEGORY_SIZE = 4
_TRAILER_SIZE = 13
# Bytes from the echo's start to the next record's start.
_ECHO_TO_NEXT = 4 + _TRAILER_SIZE

# Fixed block, relative to Q.
_BLOCK_KIND = 0x14
_REWARD_COUNT = 0x15
_UNION_START = 0x80
_REWARD_ENTRY_SIZE = 178
# block_kind 0 shifts the block; its reward entries are not read.
_SHIFTED_BLOCK_KIND = 0

# Bytes between the icon path and the echo.
_POST_ICON_SIZES = (16, 8)
_MAX_ICON_LENGTH = 260

_U32 = struct.Struct("<I")
_STRING_PREFIX = struct.Struct("<II")
_NON_ZERO_BYTE = re.compile(rb"[^\x00]")
_I32 = struct.Struct("<i")
_F32 = struct.Struct("<f")

_NO_FAMILY_STAT = 16
# Weight is stored in 1/10,000 LT.
_WEIGHT_TYPE = 5
_WEIGHT_PER_LT = 10_000

# family_stat_type -> (label, union offset, reader). Types 12 and 13 only occur
# in test quests and their field widths are unconfirmed, so they stay unnamed.
_FAMILY_STAT_FIELDS: dict[int, tuple[str, int, struct.Struct | None]] = {
    0: ("AP", 0x04, _F32),
    1: ("DP", 0x08, _F32),
    2: ("HP", 0x0C, _F32),
    3: ("MP", 0x10, _F32),
    4: ("Stamina", 0x14, _I32),
    5: ("Weight", 0x18, _I32),
    6: ("Inventory", 0x1C, None),
    7: ("Accuracy", 0x1D, _F32),
    8: ("Evasion", 0x21, _F32),
    9: ("Enhancement Chance", 0x25, _I32),
    10: ("Valks Limit", 0x29, _I32),
    11: ("Stack Limit", 0x2D, _I32),
}


@dataclass(frozen=True)
class QuestIndex:
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


def build_quest_index(data: bytes, allquestlist_ids: list[int]) -> QuestIndex:
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

    return QuestIndex(list(allquestlist_ids), starts, quest_offsets, echo_offsets)


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


def _family_stat_value(data: bytes, union: int, stat_type: int) -> float | None:
    field = _FAMILY_STAT_FIELDS.get(stat_type)
    if field is None:
        return None
    _label, offset, reader = field
    if reader is None:
        return data[union + offset]
    value = reader.unpack_from(data, union + offset)[0]
    return value / _WEIGHT_PER_LT if stat_type == _WEIGHT_TYPE else value


def _family_stats(data: bytes, quest_offset: int, echo: int) -> list[FamilyStat]:
    """Family stats granted by the counted reward entries (type 16 is none)."""
    if data[quest_offset + _BLOCK_KIND] == _SHIFTED_BLOCK_KIND:
        return []

    stats: list[FamilyStat] = []
    for entry in range(u32(data, quest_offset + _REWARD_COUNT)):
        union = quest_offset + _UNION_START + entry * _REWARD_ENTRY_SIZE
        if union + _REWARD_ENTRY_SIZE > echo:
            break
        stat_type = u32(data, union)
        if stat_type == _NO_FAMILY_STAT:
            continue
        label = _FAMILY_STAT_FIELDS.get(stat_type, (f"Type {stat_type}", 0, None))[0]
        stats.append({
            "entry": entry,
            "type": stat_type,
            "label": label,
            "value": _family_stat_value(data, union, stat_type),
        })
    return stats


def parse_quest_record(data: bytes, index: QuestIndex, row: int) -> QuestRecord:
    start = index.record_starts[row]
    quest_offset = index.quest_offsets[row]
    echo = index.echo_offsets[row]
    packed_quest_id = index.packed_quest_ids[row]

    condition_script, pos = _read_utf16(data, start + _LEAD_SIZE)
    action_script, pos = _read_utf16(data, pos)
    objective_start = _objective_start(data, pos, quest_offset)
    objective_text_kr = "" if objective_start is None else _read_utf16(data, objective_start)[0]

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
        block_kind=data[quest_offset + _BLOCK_KIND],
        condition_script=condition_script,
        action_script=action_script,
        objective_text_kr=decode_inline_text(objective_text_kr),
        icon_path=_icon_path(data, quest_offset, echo),
        family_stats=_family_stats(data, quest_offset, echo),
        loc_texts_en=[],
    )


# Stored quest icon paths start at "Icon/", "New_Icon/" or "UI_Artwork/",
# which all hang off ui_texture.
QUEST_ICON_ROOT = "ui_texture/"


def build_quest_icon_index(data: bytes, allquestlist_data: bytes) -> dict[int, str]:
    """Map packed quest ID to icon path.

    `allquestlist.bss` names the record order the walk needs.
    """
    ids = [record["packed_quest_id"] for record in parse_allquestlist_records(allquestlist_data)]
    index = build_quest_index(data, ids)
    icons: dict[int, str] = {}
    for row, packed_quest_id in enumerate(index.packed_quest_ids):
        icon = _icon_path(data, index.quest_offsets[row], index.echo_offsets[row])
        if icon:
            # A few stored paths carry a doubled separator, such as
            # "Icon/Quest//lost_wagon.dds", which can never match a PAZ entry.
            icons[packed_quest_id] = f"{QUEST_ICON_ROOT}{icon.lower().replace('//', '/')}"
    return icons
