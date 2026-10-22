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
from .parser import parse_reward_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _slot_key(slot: str) -> str:
    """The lang `slots` key of a slot: `major_release_0` -> `majorRelease0`."""
    head, *rest = slot.split("_")
    return head + "".join(part.capitalize() for part in rest)


def _number_cell(value: int | None) -> str:
    return _EMPTY if value is None else e(f"{value:,}")


class SiegeRewardDataBssHandler(PreviewHandler):
    """One row per reward slot: the item and its count, the reward it is, its tier, tier grid and block."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["count"], "num", sort_key="count"),
            Column(cols["reward"], sort_key="reward"),
            Column(cols["tier"], "num", sort_key="tier"),
            Column(cols["tierGrid"], "num", sort_key="tier_grid"),
            Column(cols["block"], "num", sort_key="block"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order: the Grid Block, then the Tier Block, each ending with its Conquest War slots.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        slots = load_handler_strings(self.lang, _LANG_DIR)["slots"]
        return [
            {
                **record,
                "reward": slots[_slot_key(record["slot"])],
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
                _number_cell(r["count"]),
                e(r["reward"]),
                _number_cell(r["tier"]),
                _number_cell(r["tier_grid"]),
                e(r["block"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
