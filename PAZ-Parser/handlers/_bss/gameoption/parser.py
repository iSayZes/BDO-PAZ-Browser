"""`gameoption.bss`: the game option values in one PABR record.

    PABR | head fields (0xC5 bytes, HEAD_FIELDS) | unknown_c5 up to table_start
    | u32 string_count | string_count x pstr | u32 table_start | u32 0

Only the head is decoded; the rest of the record stays one byte run. Layout
in docs/file-formats/bss/gameoption_bss.md (Layout 2, the live client).
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_strings import checked_string_table_start, read_string_table
from _common.record_reader import RecordReader


FILE_NAME = "gameoption.bss"

# Where the head starts: right after the PABR magic.
HEAD_START = 4


@dataclass(frozen=True)
class HeadField:
    """One head field: doc field name and `struct` format. An `s` format is a byte run nobody understands."""

    name: str
    fmt: str

    @property
    def is_unknown(self) -> bool:
        return self.name.startswith("unknown_")


HEAD_FIELDS: tuple[HeadField, ...] = (
    HeadField("unknown_04", "36s"),
    HeadField("inn_rental_time", "q"),
    HeadField("inn_room_service_time", "h"),
    HeadField("unknown_32", "10s"),
    HeadField("summon_monster_count_limit", "I"),
    HeadField("max_decreasable_hp_by_damage_rate_module", "f"),
    HeadField("max_decreasable_mp_by_damage_rate_module", "i"),
    HeadField("unknown_48", "13s"),
    HeadField("saving_buff_time", "Q"),
    HeadField("saving_cool_time", "Q"),
    HeadField("unknown_65", "24s"),
    HeadField("authentic_password_limit", "B"),
    HeadField("password_length_min", "B"),
    HeadField("password_length_max", "B"),
    HeadField("revival_product_no", "I"),
    HeadField("rescue_cool_time", "Q"),
    HeadField("final_level_up_condition_ref", "I"),
    HeadField("mail_remain_time", "Q"),
    HeadField("unknown_98", "Q"),
    HeadField("reset_awakening_need_exp", "q"),
    HeadField("expired_tent_check_day", "B"),
    HeadField("unknown_a9", "20s"),
    HeadField("attack_to_servant_rate", "i"),
    HeadField("re_awakening_item_key", "I"),
)

NAMED_HEAD_FIELDS: tuple[HeadField, ...] = tuple(f for f in HEAD_FIELDS if not f.is_unknown)

# The record past the head, up to the string table.
BODY_FIELD = "unknown_c5"


@dataclass(frozen=True)
class FieldValue:
    """One head field as read: its offset in the file and its value (bytes for a byte run)."""

    offset: int
    field: HeadField
    value: int | float | bytes


@dataclass(frozen=True)
class GameOption:
    head: tuple[FieldValue, ...]
    body_offset: int
    body_size: int
    strings: tuple[str, ...]


def parse_gameoption(data: bytes) -> GameOption:
    """The head fields, the size of the byte run after them and the string table.

    Raises ValueError on a bad magic or trailer, or when the head runs past
    the string table.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEAD_START, table_start, FILE_NAME)
    head = []
    for field in HEAD_FIELDS:
        offset = reader.pos
        (value,) = reader.unpack(struct.Struct("<" + field.fmt))
        head.append(FieldValue(offset, field, value))
    return GameOption(
        head=tuple(head),
        body_offset=reader.pos,
        body_size=reader.remaining(),
        strings=tuple(read_string_table(data)),
    )
