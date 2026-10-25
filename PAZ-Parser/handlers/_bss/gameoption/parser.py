"""`gameoption.bss`: the game option values in one PABR record.

    PABR | head fields (0xC5 bytes, HEAD_FIELDS) | option runs (BODY_RUNS)
    | rest of the record up to table_start
    | u32 string_count | string_count x pstr | u32 table_start | u32 0

The head is the `BattleOption` loader's first columns. The runs after it
(`ServantOption`, `MovementVerifyOption`, `EtcOption`, `GuildOption`,
`ItemMarket` and the blocks between them) are read up to the end of the
`ItemMarket` run; the rest of the record stays one byte run. Layout in
docs/file-formats/bss/gameoption_bss.md (Layout 6, the live client).
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_strings import checked_string_table_start, read_string_table
from _common.record_reader import RecordReader
from .run_fields import BODY_RUNS
from .runs import RunValue, read_run


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


@dataclass(frozen=True)
class FieldValue:
    """One head field as read: its offset in the file and its value (bytes for a byte run)."""

    offset: int
    field: HeadField
    value: int | float | bytes


@dataclass(frozen=True)
class GameOption:
    """The parsed record.

    `runs` holds every run field up to the end of the `ItemMarket` run; it is
    empty when the bytes after the head do not walk by Layout 6, and
    `body_error` then says where the walk stopped. `undecoded_size` counts the
    bytes of the record that no named field covers.
    """

    head: tuple[FieldValue, ...]
    runs: tuple[RunValue, ...]
    body_error: str
    undecoded_size: int
    strings: tuple[str, ...]


def parse_gameoption(data: bytes) -> GameOption:
    """The head fields, the option runs, the undecoded byte count and the string table.

    Raises ValueError on a bad magic or trailer, or when the head runs past
    the string table. A body that does not walk leaves `runs` empty instead.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEAD_START, table_start, FILE_NAME)
    head = tuple(_read_head(reader))
    runs: tuple[RunValue, ...] = ()
    body_error = ""
    try:
        runs = tuple(value for run in BODY_RUNS for value in read_run(reader, run))
    except ValueError as ex:
        body_error = str(ex)
    named_bytes = sum(struct.calcsize("<" + field.fmt) for field in NAMED_HEAD_FIELDS)
    named_bytes += sum(value.size for value in runs if not value.field.is_unknown)
    return GameOption(
        head=head,
        runs=runs,
        body_error=body_error,
        undecoded_size=table_start - HEAD_START - named_bytes,
        strings=tuple(read_string_table(data)),
    )


def _read_head(reader: RecordReader) -> list[FieldValue]:
    head = []
    for field in HEAD_FIELDS:
        offset = reader.pos
        (value,) = reader.unpack(struct.Struct("<" + field.fmt))
        head.append(FieldValue(offset, field, value))
    return head
