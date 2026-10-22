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
from _common.territory import territory_name
from .parser import BOOTY_LIST, parse_reward_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# The lang `rewards` key of each reward list, row item and the booty lists.
_REWARD_KEYS: dict[str, str] = {
    "win_rewards": "win",
    "lose_rewards": "lose",
    "release_win_rewards": "scoreRank1",
    **{f"release_rewards_{index}": f"scoreRank{index + 2}" for index in range(5)},
    "release_rewards": "liberation",
    "plus_medal_rewards": "plusMedal",
    "plus_item_rewards": "plusItem",
    "item_id_1": "item1",
    "item_id_2": "item2",
    "item_id_3": "item3",
    BOOTY_LIST: "booty",
}


def _count_cell(count: int | None) -> str:
    return _EMPTY if count is None else e(f"{count:,}")


class MajorSiegeRewardBssHandler(PreviewHandler):
    """One row per item: each row's reward lists and three item IDs, then the booty lists."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["count"], "num", sort_key="count"),
            Column(cols["reward"], sort_key="reward"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order: each row's lists in turn, then the booty lists.
        return None

    def _reward(self, record: dict, territory: str) -> str:
        """The list's label; a booty list's names its territory, or the key without a LOC name."""
        label = load_handler_strings(self.lang, _LANG_DIR)["rewards"][_REWARD_KEYS[record["reward_list"]]]
        if record["territory_key"] is None:
            return label
        return label.format(territory=territory or record["territory_key"])

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        for record in parse_reward_records(data):
            key = record["territory_key"]
            territory = "" if key is None else territory_name(key)
            records.append(
                {
                    **record,
                    "territory_name": territory,
                    "reward": self._reward(record, territory),
                    "icon_path": icon_path(IconKind.ITEM, record["item_id"]),
                    **pa_fields("item_name", item_name_tagged(record["item_id"])),
                }
            )
        return records

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
                _count_cell(r["count"]),
                e(r["reward"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
