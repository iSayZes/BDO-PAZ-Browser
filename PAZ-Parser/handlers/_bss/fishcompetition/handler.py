"""fishcompetition.bss preview handler: each contest fish with its grade, rank rewards and title item."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from _common.html import Column, e, html_list_cell
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_fishcompetition


_LANG_DIR = Path(__file__).parent / "lang"


class FishCompetitionBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["fishKey"], "num", sort_key=KEY_FIELD),
            Column(labels["fish"], sort_key="fish_name"),
            Column(labels["grade"], "num", sort_key="grade"),
            Column(labels["rewards"], sort_key="reward_text"),
            Column(labels["titleItem"], sort_key="title_item_name"),
        ]

    def _tier_texts(self, rank_tiers: Sequence[int]) -> list[str]:
        """`Rank 1`, ..., `Rank 4-30`: the ranks each tier covers, from the last rank of each."""
        texts = []
        previous = 0
        for last in rank_tiers:
            first = previous + 1
            if first == last:
                texts.append(handler_text(self.lang, _LANG_DIR, "text.rank", rank=last))
            else:
                texts.append(handler_text(self.lang, _LANG_DIR, "text.rankRange", first=first, last=last))
            previous = last
        return texts

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        competition = parse_fishcompetition(data)
        tier_texts = self._tier_texts(competition.rank_tiers)
        records = []
        for row in competition.rows:
            rewards = [
                f"{tier}: {item_key_text(key)}"
                for tier, key in zip(tier_texts, row["rank_reward_item_keys"], strict=True)
            ]
            records.append(
                {
                    **row,
                    "fish_name": item_key_text(row[KEY_FIELD]),
                    "rank_tiers": competition.rank_tiers,
                    "rank_tier_texts": tier_texts,
                    "rewards": rewards,
                    "reward_text": ", ".join(rewards),
                    "title_item_name": item_key_text(row["title_item_key"]),
                }
            )
        return records

    def cells(self, record: dict) -> list[str]:
        rewards = [
            f"{e(tier)}: {item_key_list_cell([key], 1)}"
            for tier, key in zip(record["rank_tier_texts"], record["rank_reward_item_keys"], strict=True)
        ]
        return [
            e(record[KEY_FIELD]),
            item_key_list_cell([record[KEY_FIELD]], 1),
            e(record["grade"]),
            html_list_cell(rewards, separator="<br>"),
            item_key_list_cell([record["title_item_key"]], 1),
        ]
