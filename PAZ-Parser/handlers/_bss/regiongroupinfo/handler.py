from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, flag_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.node import full_node_name
from .parser import parse_regiongroupinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _number_cell(value: float | int | None) -> str:
    """A whole number with thousands separators, or a dash for None."""
    return _EMPTY if value is None else e(f"{value:,.0f}")


class RegionGroupInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["regionGroupKey"], "num", sort_key="region_group_key"),
            Column(cols["nodeKey"], "num", sort_key="node_key"),
            Column(cols["nodeName"], sort_key="node_name"),
            Column(cols["concurrentUsers"], "num", sort_key="concurrent_playable_user_count"),
            Column(cols["corpProductivity"], sort_key="enable_corp_productivity"),
            Column(cols["fishingProductivity"], sort_key="enable_fishing_productivity"),
            Column(cols["loyalty"], sort_key="enable_loyalty"),
            Column(cols["x"], "num", sort_key="pos_x"),
            Column(cols["y"], "num", sort_key="pos_y"),
            Column(cols["z"], "num", sort_key="pos_z"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {
                **record,
                "node_name": full_node_name(record["node_key"]) if record["node_key"] else "",
            }
            for record in parse_regiongroupinfo_records(data)
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
                e(r["region_group_key"]),
                _EMPTY if r["node_key"] is None else e(r["node_key"]),
                e(r["node_name"] or _EMPTY),
                _number_cell(r["concurrent_playable_user_count"]),
                flag_cell(r["enable_corp_productivity"]),
                flag_cell(r["enable_fishing_productivity"]),
                flag_cell(r["enable_loyalty"]),
                _number_cell(r["pos_x"]),
                _number_cell(r["pos_y"]),
                _number_cell(r["pos_z"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
