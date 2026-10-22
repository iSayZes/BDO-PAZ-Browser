"""attendance.dbss preview handler: each daily login reward event with its day rewards."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.duration import format_duration
from _common.html import Column, e, hidden_slice, icon_html_list_cell
from _common.item_key import item_count_text, item_key_icon_path, item_key_text_tagged
from _common.lang import load_handler_strings
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_cell, pa_fields, pa_html
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_attendance_records, parse_attendanceoffset_rows
from .text import AttendanceText, attendance_texts


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_NO_TEXT = AttendanceText(title="", period="", expired="")
# One week of login days; the rest of a reward list sits behind the "(+N)" marker.
_REWARDS_SHOWN = 7
_MS_PER_SECOND = 1000


def attendance_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_attendanceoffset_rows, KEY_FIELD, "attendanceKey")


def _reward_text(reward: dict) -> str:
    return f"{reward['day']}: {item_count_text(reward['item_id'], reward['item_count'])}"


def _rewards_cell(rewards: list[dict]) -> str:
    """The first week of day rewards, each item with its icon and grade colour, and a count of the rest."""
    shown = rewards[:_REWARDS_SHOWN]
    entries = [
        (
            item_key_icon_path(reward["item_id"]),
            f"{reward['day']}: {pa_html(item_key_text_tagged(reward['item_id']))} x{reward['item_count']:,}",
        )
        for reward in shown
    ]
    hidden = [_reward_text(reward) for reward in hidden_slice(rewards, _REWARDS_SHOWN)]
    return icon_html_list_cell(entries, len(rewards) - len(shown), hidden_names=hidden)


def _weekdays(flags: list[int]) -> list[int]:
    """The weekday numbers whose `day_of_week` flag is set."""
    return [day for day, flag in enumerate(flags) if flag]


class AttendanceHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["attendanceKey"], "num", sort_key=KEY_FIELD),
            Column(labels["name"], sort_key="name"),
            Column(labels["startDate"], sort_key="start_date"),
            Column(labels["attendanceEndDate"], sort_key="attendance_end_date"),
            Column(labels["rewardEndDate"], sort_key="reward_end_date"),
            Column(labels["eventPeriod"], sort_key="event_period"),
            Column(labels["claimPeriod"], sort_key="claim_period"),
            Column(labels["players"], sort_key="players"),
            Column(labels["rewards"], sort_key="rewards_text"),
            Column(labels["overlapCount"], "num", sort_key="overlap_count"),
            Column(labels["overlapWaitingTime"], "num", sort_key="overlap_waiting_time"),
            Column(labels["dayOfWeek"], sort_key="weekdays_text"),
            Column(labels["displayOrder"], "num", sort_key="display_order"),
            Column(labels["guildLevel"], sort_key="guild_level_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        player_types: Mapping[str, str] = load_handler_strings(self.lang, _LANG_DIR)["playerTypes"]
        texts = attendance_texts()
        records = []
        for record in parse_attendance_records(data):
            text = texts.get(record[KEY_FIELD], _NO_TEXT)
            user_type = record["user_connection_type"]
            records.append(
                {
                    **record,
                    **pa_fields("name", text.title or record["title_kr"].strip()),
                    **pa_fields("event_period", text.period or record["event_period_kr"].strip()),
                    **pa_fields("claim_period", text.expired or record["event_expired_kr"].strip()),
                    "players": player_types.get(str(user_type), str(user_type)),
                    "rewards_text": ", ".join(_reward_text(reward) for reward in record["rewards"]),
                    "weekdays_text": ", ".join(str(day) for day in _weekdays(record["day_of_week"])),
                    "guild_level_text": ", ".join(str(level) for level in record["guild_level"]),
                }
            )
        return records

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            pa_cell(record, "name"),
            e(record["start_date"]),
            e(record["attendance_end_date"]),
            e(record["reward_end_date"]),
            pa_cell(record, "event_period"),
            pa_cell(record, "claim_period"),
            e(record["players"]),
            _rewards_cell(record["rewards"]) or _EMPTY,
            e(record["overlap_count"]),
            e(format_duration(record["overlap_waiting_time"] * _MS_PER_SECOND) or _EMPTY),
            e(record["weekdays_text"]) or _EMPTY,
            e(record["display_order"]),
            e(record["guild_level_text"]) or _EMPTY,
        ]
