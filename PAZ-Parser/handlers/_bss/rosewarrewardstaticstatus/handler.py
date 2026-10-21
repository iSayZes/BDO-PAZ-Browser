from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, flag_cell, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields
from .parser import parse_reward_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# The lang `results` key of each named reward list; the fourth list has none.
_RESULT_KEYS = {"win_rewards": "win", "lose_rewards": "lose", "draw_rewards": "draw"}


class RoseWarRewardStaticStatusBssHandler(PreviewHandler):
    """One row per reward item: guild or not, the war result it is for, the item and its count."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["count"], "num", sort_key="count"),
            Column(cols["result"], sort_key="result"),
            Column(cols["guild"], sort_key="is_guild"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def _result(self, reward_list: str) -> str | None:
        key = _RESULT_KEYS.get(reward_list)
        return None if key is None else load_handler_strings(self.lang, _LANG_DIR)["results"][key]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {
                **record,
                "result": self._result(record["reward_list"]),
                "icon_path": icon_path(IconKind.ITEM, record["item_id"]),
                **pa_fields("item_name", item_name_tagged(record["item_id"])),
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
                e(r["result"] or _EMPTY),
                flag_cell(bool(r["is_guild"])),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
