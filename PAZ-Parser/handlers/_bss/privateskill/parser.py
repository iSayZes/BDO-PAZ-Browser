"""`privateskill.bss`: the active and passive skills and the classes that learn them.

    PABR | u32 active_count | active_count x Row | u32 passive_count
    | passive_count x Row | string table | u32 table_start | u32 0
    Row (Layout 2, client 1267 on): u32 skill_key | u64 class_mask
    Row (Layout 1, clients 1194 to 1261): u32 skill_key | u8[32] class flags

Layout 2 sets bit `n` of `class_mask` for class type `n`; Layout 1 stores one
byte per class type, read here into the same bit mask. Layout 2 files up to
client 2243 hold a 32-bit mask with its bit 31 copied into the high half;
such a file is read with 32 class slots like Layout 1. Nothing in the file
names its layout, so it is read with the first layout (newest first) whose
rows end where the string table starts. Layouts 1 and 2 in
docs/file-formats/privateskill_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.counted_rows import read_counted_structs
from _common.pabr_offset import PABR_MAGIC
from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "privateskill.bss"
# The skillsimply.dbss `kind` of every key in each list, in file order.
ACTIVE_KIND = 1
PASSIVE_KIND = 2
LIST_KINDS = {"active": ACTIVE_KIND, "passive": PASSIVE_KIND}

_ROW_FIELDS = ("skill_key", "class_mask")
_LAYOUT_1_CLASS_SLOTS = 32
_LAYOUT_2_CLASS_SLOTS = 64
_LOW_HALF = (1 << _LAYOUT_1_CLASS_SLOTS) - 1
_SIGN_BIT = _LAYOUT_1_CLASS_SLOTS - 1


def class_flags_mask(flags: bytes) -> int:
    """The bit mask of a one-byte-per-class set: bit `n` set when byte `n` is not `0`."""
    return sum(1 << class_type for class_type, flag in enumerate(flags) if flag)


def _class_mask(stored: int | bytes) -> int:
    """A stored class set as a bit mask: Layout 2 stores the mask, Layout 1 one byte per class."""
    return class_flags_mask(stored) if isinstance(stored, bytes) else stored


@dataclass(frozen=True)
class RowLayout:
    """One documented Row shape; `number` is its Layout N in the doc.

    `class_slots` is how many class types the row's class set can hold.
    """

    number: int
    row: struct.Struct
    class_slots: int


# Newest first.
LAYOUTS = (
    RowLayout(2, struct.Struct("<IQ"), _LAYOUT_2_CLASS_SLOTS),
    RowLayout(1, struct.Struct(f"<I{_LAYOUT_1_CLASS_SLOTS}s"), _LAYOUT_1_CLASS_SLOTS),
)


@dataclass(frozen=True)
class PrivateSkillTable:
    """The layout the file fits and its rows, the active list then the passive list.

    `class_slots` is how many class types the file's class sets hold: the
    layout's, or 32 for a Layout 2 file of sign-widened 32-bit masks.
    """

    layout: RowLayout
    records: list[dict]
    class_slots: int


def _read_rows(data: bytes, end: int, layout: RowLayout) -> list[dict]:
    """Both lists read with `layout`; raises ValueError when they do not end at `end`."""
    reader = RecordReader(data, len(PABR_MAGIC), end, FILE_NAME)
    records = [
        {**row, "class_mask": _class_mask(row["class_mask"]), "kind": kind}
        for list_name, kind in LIST_KINDS.items()
        for row in read_counted_structs(reader, layout.row, _ROW_FIELDS, f"{FILE_NAME} {list_name}_count")
    ]
    if not reader.at_end():
        raise ValueError(f"rows end at 0x{reader.pos:X}, the string table starts at 0x{end:X}")
    return records


def _is_sign_widened(mask: int) -> bool:
    """True when the high half of `mask` is its bit 31 copied: all set with bit 31, else `0`."""
    high = mask >> _LAYOUT_1_CLASS_SLOTS
    return high == (_LOW_HALF if mask >> _SIGN_BIT & 1 else 0)


def _table(layout: RowLayout, records: list[dict]) -> PrivateSkillTable:
    """`records` as read with `layout`; a file of sign-widened 32-bit masks keeps their low half."""
    if layout.class_slots <= _LAYOUT_1_CLASS_SLOTS or not all(_is_sign_widened(row["class_mask"]) for row in records):
        return PrivateSkillTable(layout, records, layout.class_slots)
    narrowed = [{**row, "class_mask": row["class_mask"] & _LOW_HALF} for row in records]
    return PrivateSkillTable(layout, narrowed, _LAYOUT_1_CLASS_SLOTS)


def parse_privateskill(data: bytes) -> PrivateSkillTable:
    """The first layout, newest first, whose rows fill the file up to the string table.

    Raises ValueError on a bad PABR magic or trailer, or when no layout's rows
    end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    breaks: list[str] = []
    for layout in LAYOUTS:
        try:
            return _table(layout, _read_rows(data, end, layout))
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"{FILE_NAME} fits no known layout ({'; '.join(breaks)})")


def parse_privateskill_records(data: bytes) -> list[dict]:
    """Every row, the active list then the passive list, each with the list's `kind`.

    Raises ValueError like `parse_privateskill()`.
    """
    return parse_privateskill(data).records
