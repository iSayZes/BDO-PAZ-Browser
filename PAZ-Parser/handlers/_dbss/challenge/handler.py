"""challenge.dbss preview handler: the challenges with their condition, reset and rewards."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, flag_cell
from _common.lang import load_handler_strings
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_cell, pa_fields, pa_line_cell
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_challenge_records, parse_challengeoffset_rows
from .text import (
    challenge_reward_texts,
    challenge_rewards_cell,
    challenge_type_name,
    complete_condition_type_name,
    description_tagged,
    reset_type_name,
    title_tagged,
)


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def challenge_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_challengeoffset_rows, KEY_FIELD, "challengeKey")


class ChallengeHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["challengeKey"], "num", sort_key=KEY_FIELD),
            Column(labels["title"], sort_key="title"),
            Column(labels["type"], sort_key="challenge_type_name"),
            Column(labels["completeCondition"], sort_key="complete_condition_type_name"),
            Column(labels["conditionParam1"], "num", sort_key="condition_param1"),
            Column(labels["conditionParam2"], "num", sort_key="condition_param2"),
            Column(labels["rewardCondition"], sort_key="reward_condition"),
            Column(labels["resetType"], sort_key="reset_type_name"),
            Column(labels["resetValue"], "num", sort_key="reset_value"),
            # List columns: they would only sort by their string form.
            Column(labels["rewards"]),
            Column(labels["selectRewards"]),
            Column(labels["optionalType"], "num", sort_key="optional_type"),
            Column(labels["isRewardOverlapable"], sort_key="is_reward_overlapable"),
            Column(labels["isShowIcon"], sort_key="is_show_icon"),
            Column(labels["description"], sort_key="description"),
        ]

    def _coupon_label(self) -> str:
        """`Coupon {number}`, filled with a coupon reward's number."""
        return load_handler_strings(self.lang, _LANG_DIR)["text"]["coupon"]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        coupon_label = self._coupon_label()
        return [self._record_fields(record, coupon_label) for record in parse_challenge_records(data)]

    @staticmethod
    def _record_fields(record: dict, coupon_label: str) -> dict:
        challenge_key = record[KEY_FIELD]
        return {
            **record,
            **pa_fields("title", title_tagged(challenge_key, record["title_kr"])),
            **pa_fields("description", description_tagged(challenge_key, record["description_kr"])),
            "challenge_type_name": challenge_type_name(record["challenge_type"]),
            "complete_condition_type_name": complete_condition_type_name(record["complete_condition_type"]),
            "reset_type_name": reset_type_name(record["reset_type"]),
            # Text forms, so tab search and CSV export see them.
            "base_reward_texts": challenge_reward_texts(record["base_rewards"], coupon_label),
            "select_reward_texts": challenge_reward_texts(record["select_rewards"], coupon_label),
        }

    def cells(self, record: dict) -> list[str]:
        coupon_label = self._coupon_label()
        return [
            e(record[KEY_FIELD]),
            pa_cell(record, "title"),
            e(record["challenge_type_name"]),
            e(record["complete_condition_type_name"]),
            e(f"{record['condition_param1']:,}"),
            e(f"{record['condition_param2']:,}"),
            e(record["reward_condition"]) or _EMPTY,
            e(record["reset_type_name"]),
            e(f"{record['reset_value']:,}"),
            challenge_rewards_cell(record["base_rewards"], coupon_label) or _EMPTY,
            challenge_rewards_cell(record["select_rewards"], coupon_label) or _EMPTY,
            e(f"{record['optional_type']:,}"),
            flag_cell(bool(record["is_reward_overlapable"])),
            flag_cell(bool(record["is_show_icon"])),
            pa_line_cell(record, "description"),
        ]
