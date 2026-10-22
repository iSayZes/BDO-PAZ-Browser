from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields
from _common.skill import skill_name
from .parser import SET_REWARD_LISTS, parse_reward_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _list_number(reward_list: str) -> int | None:
    """The 1-based position of a Reward Set list, None for the list after the sets."""
    return SET_REWARD_LISTS.index(reward_list) + 1 if reward_list in SET_REWARD_LISTS else None


def _number_cell(value: int | None) -> str:
    return _EMPTY if value is None else e(value)


def _text_cell(text: str) -> str:
    return e(text) if text else _EMPTY


class OceanSiegeRewardBssHandler(PreviewHandler):
    """One row per reward item: the item and its count, its set and list, and the row's two skills."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["count"], "num", sort_key="count"),
            Column(cols["rewardSet"], "num", sort_key="reward_set"),
            Column(cols["rewardList"], "num", sort_key="reward_list_number"),
            Column(cols["skill1Id"], "num", sort_key="skill_key_1"),
            Column(cols["skill1"], sort_key="skill_name_1"),
            Column(cols["skill2Id"], "num", sort_key="skill_key_2"),
            Column(cols["skill2"], sort_key="skill_name_2"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order: the five sets with their four lists each, then the last list.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {
                **record,
                "reward_list_number": _list_number(record["reward_list"]),
                "icon_path": icon_path(IconKind.ITEM, record["item_id"]),
                **pa_fields("item_name", item_name_tagged(record["item_id"])),
                "skill_name_1": skill_name(record["skill_key_1"]),
                "skill_name_2": skill_name(record["skill_key_2"]),
            }
            for record in parse_reward_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["item_id"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "item_name"),
                e(f"{r['count']:,}"),
                _number_cell(r["reward_set"]),
                _number_cell(r["reward_list_number"]),
                e(r["skill_key_1"]),
                _text_cell(r["skill_name_1"]),
                e(r["skill_key_2"]),
                _text_cell(r["skill_name_2"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
