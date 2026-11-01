"""`attendance.dbss`: the daily login reward (attendance) events.

    u32 count | count x row
    row: u16 attendance_key | str16 title_kr | bytes[8] unknown_title_00
         | str16 start_date | bytes[8] unknown_start_date_00
         | str16 attendance_end_date | bytes[8] unknown_attendance_end_date_00
         | str16 reward_end_date | bytes[8] unknown_reward_end_date_00
         | str16 event_period_kr | str16 event_expired_kr
         | bytes[8] unknown_event_expired_kr_00 | u8 user_connection_type
         | u32 reward_count | reward_count x Reward
         | u32 overlap_count | u32 overlap_waiting_time | u32 unknown_rewards_08
         | u8[7] day_of_week | u32 display_order | bytes[4] unknown_rewards_17
         | u32 guild_level_count | u16[guild_level_count] guild_level
    Reward: u32 day | u32 item_id | u64 item_count | u8 grade_type | str16 desc_kr

`attendanceoffset.dbss` (u32 count, then u16 key, u32 offset and u32 size per
row, no PABR magic) points at the row start. Layout 3 in
docs/file-formats/dbss/attendance_dbss.md; client 1784 to 2107 rows (Layout 2) end before
`guild_level_count`.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "attendance.dbss"
OFFSET_FILE = "attendanceoffset.dbss"
KEY_FIELD = "attendance_key"
DAYS_PER_WEEK = 7

_KEY = struct.Struct("<H")
_GAP = struct.Struct("<8s")
_U8 = struct.Struct("<B")
_U32 = struct.Struct("<I")
_REWARD_HEAD = struct.Struct("<IIQB")
_OVERLAP = struct.Struct("<III")
_DAY_OF_WEEK = struct.Struct(f"<{DAYS_PER_WEEK}B")
_DISPLAY_ORDER = struct.Struct("<I4s")
_GUILD_LEVEL = struct.Struct("<H")


def _gap(reader: RecordReader) -> str:
    (raw,) = reader.unpack(_GAP)
    return raw.hex(" ")


def _read_reward(reader: RecordReader) -> dict:
    day, item_id, item_count, grade_type = reader.unpack(_REWARD_HEAD)
    return {
        "day": day,
        "item_id": item_id,
        "item_count": item_count,
        "grade_type": grade_type,
        "desc_kr": reader.text(wide=True),
    }


def _read_counted(reader: RecordReader, what: str, item_size: int) -> int:
    (count,) = reader.unpack(_U32)
    if count * item_size > reader.remaining():
        raise ValueError(f"{FILE_NAME} {what} count {count:,} at 0x{reader.pos - _U32.size:X} runs past the file")
    return count


def _read_row(reader: RecordReader) -> dict:
    (attendance_key,) = reader.unpack(_KEY)
    title_kr = reader.text(wide=True)
    unknown_title_00 = _gap(reader)
    start_date = reader.text(wide=True)
    unknown_start_date_00 = _gap(reader)
    attendance_end_date = reader.text(wide=True)
    unknown_attendance_end_date_00 = _gap(reader)
    reward_end_date = reader.text(wide=True)
    unknown_reward_end_date_00 = _gap(reader)
    event_period_kr = reader.text(wide=True)
    event_expired_kr = reader.text(wide=True)
    unknown_event_expired_kr_00 = _gap(reader)
    (user_connection_type,) = reader.unpack(_U8)
    reward_count = _read_counted(reader, "reward", _REWARD_HEAD.size)
    rewards = [_read_reward(reader) for _ in range(reward_count)]
    overlap_count, overlap_waiting_time, unknown_rewards_08 = reader.unpack(_OVERLAP)
    day_of_week = list(reader.unpack(_DAY_OF_WEEK))
    display_order, unknown_rewards_17 = reader.unpack(_DISPLAY_ORDER)
    guild_level_count = _read_counted(reader, "guild level", _GUILD_LEVEL.size)
    guild_level = list(reader.unpack(struct.Struct(f"<{guild_level_count}H")))
    return {
        KEY_FIELD: attendance_key,
        "title_kr": title_kr,
        "unknown_title_00": unknown_title_00,
        "start_date": start_date,
        "unknown_start_date_00": unknown_start_date_00,
        "attendance_end_date": attendance_end_date,
        "unknown_attendance_end_date_00": unknown_attendance_end_date_00,
        "reward_end_date": reward_end_date,
        "unknown_reward_end_date_00": unknown_reward_end_date_00,
        "event_period_kr": event_period_kr,
        "event_expired_kr": event_expired_kr,
        "unknown_event_expired_kr_00": unknown_event_expired_kr_00,
        "user_connection_type": user_connection_type,
        "rewards": rewards,
        "overlap_count": overlap_count,
        "overlap_waiting_time": overlap_waiting_time,
        "unknown_rewards_08": unknown_rewards_08,
        "day_of_week": day_of_week,
        "display_order": display_order,
        "unknown_rewards_17": unknown_rewards_17.hex(" "),
        "guild_level": guild_level,
    }


def parse_attendance_records(data: bytes) -> list[dict]:
    """Every attendance event in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_attendanceoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: attendance key, row offset and row size. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
