"""`guildhonorsystem.bss`: the Guild Fame change reasons, benefits and daily pay steps.

    u64 unknown_00 | i64 unknown_08 | i64 unknown_10 | u64 unknown_18..unknown_38 (5)
    u32 count | count x (u32 key | str16 description_kr | i64 point | u64 reason_param
                         | u32 key_dup | u32 reason_type)
    u32 count | count x (u32 key | str16 description_kr | i64 point | u64 param_1
                         | u64 param_2 | u32 key_dup | u8 benefit_type)
    u32 count | count x (i64 point | u32 bonus_percent)

No PABR magic and no string table; the lists end at the last byte. Layout 1
in docs/file-formats/guildhonorsystem_bss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Callable
from dataclasses import dataclass

from _common.counted_rows import read_counted_structs
from _common.record_reader import RecordReader


FILE_NAME = "guildhonorsystem.bss"

HEAD_FIELDS = (
    "unknown_00",
    "unknown_08",
    "unknown_10",
    "unknown_18",
    "unknown_20",
    "unknown_28",
    "unknown_30",
    "unknown_38",
)
_HEAD = struct.Struct("<Qqq5Q")
_U32 = struct.Struct("<I")
_REASON_TAIL = struct.Struct("<qQII")
_BENEFIT_TAIL = struct.Struct("<qQQIB")
_DAILY_INCENTIVE = struct.Struct("<qI")
_DAILY_INCENTIVE_FIELDS = ("point", "bonus_percent")


@dataclass(frozen=True)
class GuildHonorSystem:
    """The head values and the three lists, each list in file order."""

    head: dict[str, int]
    change_reasons: list[dict]
    benefits: list[dict]
    daily_incentives: list[dict]


def _read_change_reason(reader: RecordReader) -> dict:
    (key,) = reader.unpack(_U32)
    description_kr = reader.text(wide=True)
    point, reason_param, key_dup, reason_type = reader.unpack(_REASON_TAIL)
    return {
        "key": key,
        "description_kr": description_kr,
        "point": point,
        "reason_param": reason_param,
        "key_dup": key_dup,
        "reason_type": reason_type,
    }


def _read_benefit(reader: RecordReader) -> dict:
    (key,) = reader.unpack(_U32)
    description_kr = reader.text(wide=True)
    point, param_1, param_2, key_dup, benefit_type = reader.unpack(_BENEFIT_TAIL)
    return {
        "key": key,
        "description_kr": description_kr,
        "point": point,
        "param_1": param_1,
        "param_2": param_2,
        "key_dup": key_dup,
        "benefit_type": benefit_type,
    }


def _read_list(reader: RecordReader, read_row: Callable[[RecordReader], dict]) -> list[dict]:
    (count,) = reader.unpack(_U32)
    return [read_row(reader) for _ in range(count)]


def parse_guildhonorsystem(data: bytes) -> GuildHonorSystem:
    """The whole file. Raises ValueError when a list runs past the file or ends before it."""
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    head: dict[str, int] = dict(zip(HEAD_FIELDS, reader.unpack(_HEAD), strict=True))
    change_reasons = _read_list(reader, _read_change_reason)
    benefits = _read_list(reader, _read_benefit)
    daily_incentives = read_counted_structs(reader, _DAILY_INCENTIVE, _DAILY_INCENTIVE_FIELDS, "daily incentive")
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} lists end at 0x{reader.pos:X}, the file at 0x{len(data):X}")
    return GuildHonorSystem(head, change_reasons, benefits, daily_incentives)
