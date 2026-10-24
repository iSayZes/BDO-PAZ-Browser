from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.contents_group import contents_group_key
from _common.html import Column, e, sort_keys, table
from _common.item_key import item_name
from _common.lang import handler_text, load_handler_strings
from _common.quest.quest import quest_title, split_packed_quest_id
from _common.rate import rate_percent
from _bss.edaniaregioninfo.castle import castle_name
from .parser import parse_etc_option_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# The AP, DP and item grade minimums, shown in this order after the contents group.
_LIMIT_FIELDS = ("min_ap_1", "min_dp_1", "min_ap_2", "min_dp_2", "min_item_grade_1", "min_item_grade_2")


def _derived_fields(record: dict) -> dict:
    """The castle, the contents group key, the quest title and the item name of one row."""
    return {
        "castle_name": castle_name(record["edania_region"]),
        "contents_group": contents_group_key(record["contents_group_hash"]),
        "throne_quest_title": quest_title(*split_packed_quest_id(record["throne_quest"])),
        "boss_clear_item_name": item_name(record["boss_clear_item_key"]),
    }


class EdaniaEtcOptionBssHandler(PreviewHandler):
    """One row per Edania castle: contents group, AP, DP and grade minimums, tax, throne quest and boss clear item."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["edaniaRegion"], "num", sort_key="edania_region"),
            Column(cols["castle"], sort_key="castle_name"),
            Column(cols["contentsGroup"], "num", sort_key="contents_group"),
            Column(cols["minAp1"], "num", sort_key="min_ap_1"),
            Column(cols["minDp1"], "num", sort_key="min_dp_1"),
            Column(cols["minAp2"], "num", sort_key="min_ap_2"),
            Column(cols["minDp2"], "num", sort_key="min_dp_2"),
            Column(cols["minItemGrade1"], "num", sort_key="min_item_grade_1"),
            Column(cols["minItemGrade2"], "num", sort_key="min_item_grade_2"),
            Column(cols["taxRate"], "num", sort_key="tax_rate"),
            Column(cols["throneQuest"], sort_key="throne_quest_title"),
            Column(cols["taxBaseAmount"], "num", sort_key="tax_base_amount"),
            Column(cols["bossClearItemKey"], "num", sort_key="boss_clear_item_key"),
            Column(cols["bossClearItem"], sort_key="boss_clear_item_name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [{**record, **_derived_fields(record)} for record in parse_etc_option_records(data)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        if records:
            # The drop buff settings are stored once and repeat on every record.
            first = records[0]
            meta += handler_text(
                self.lang,
                _LANG_DIR,
                "meta.dropBuff",
                rate=rate_percent(first["drop_buff_rate"]),
                minutes=first["drop_buff_minutes"],
                uses=first["drop_buff_count"],
            )
        rows = [
            [
                e(r["edania_region"]),
                e(r["castle_name"] or _EMPTY),
                e(_EMPTY if r["contents_group"] is None else r["contents_group"]),
                *(e(r[name]) for name in _LIMIT_FIELDS),
                e(rate_percent(r["tax_rate"])),
                e(r["throne_quest_title"] or _EMPTY),
                e(f"{r['tax_base_amount']:,}"),
                e(r["boss_clear_item_key"]),
                e(r["boss_clear_item_name"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
