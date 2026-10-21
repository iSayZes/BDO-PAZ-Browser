"""yachthandrank.bss preview handler: the hand ranks (scoring combinations) of Yar!."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, flag_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_yachthandrank_records
from .text import hand_rank_desc, hand_rank_name


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Checks the sheet leaves `<null>` and the file stores as 0.
_CHECK_FIELDS = ("target_eye", "target_count", "straight_count", "made_point")


def _display_record(record: dict) -> dict:
    """The record with its LOC texts, and `None` for each check it does not make."""
    return {
        **record,
        "name": hand_rank_name(record["hand_rank_key"], record["name_kr"]),
        "desc": hand_rank_desc(record["hand_rank_key"], record["desc_kr"]),
        **{f"{field}_shown": record[field] or None for field in _CHECK_FIELDS},
    }


def _number_cell(value: int | None) -> str:
    return e(_EMPTY if value is None else value)


class YachtHandRankHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="hand_rank_key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["description"], sort_key="desc"),
            Column(cols["targetEye"], "num", sort_key="target_eye_shown"),
            Column(cols["targetCount"], "num", sort_key="target_count_shown"),
            Column(cols["straightCount"], "num", sort_key="straight_count_shown"),
            Column(cols["twoPair"], sort_key="is_two_pair"),
            Column(cols["fullHouse"], sort_key="is_full_house"),
            Column(cols["madePoint"], "num", sort_key="made_point_shown"),
            Column(cols["sumPoint"], sort_key="is_sum_point"),
            Column(cols["iconTexture"], sort_key="icon_texture"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_yachthandrank_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [_display_record(record) for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                e(r["hand_rank_key"]),
                e(r["name"] or _EMPTY),
                e(r["desc"] or _EMPTY),
                _number_cell(r["target_eye_shown"]),
                _number_cell(r["target_count_shown"]),
                _number_cell(r["straight_count_shown"]),
                flag_cell(bool(r["is_two_pair"])),
                flag_cell(bool(r["is_full_house"])),
                _number_cell(r["made_point_shown"]),
                flag_cell(bool(r["is_sum_point"])),
                e(r["icon_texture"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
