from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, flag_cell, icon_html_label_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import (
    OffsetColumn,
    OffsetTableHandler,
    offset_column,
    picked_records,
    size_column,
)
from _common.pa_text import pa_fields, pa_html, pa_key
from .model import MentalThemeRecord
from .parser import parse_mentaltheme_records, parse_mentalthemeoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


_EMPTY = "-"


def _reward(amount: int, need_count: int) -> str:
    if amount == 0 and need_count == 0:
        return _EMPTY
    return f"+{amount} at {need_count} entries"


def _reward_2(
    amount_1: int,
    need_count_1: int,
    amount_2: int,
    need_count_2: int,
) -> str:
    if amount_1 == amount_2 and need_count_1 == need_count_2:
        return _EMPTY
    return _reward(amount_2, need_count_2)


def _shown_amount(reward: str, amount: int) -> int | None:
    """The amount a reward column sorts by; None where the cell shows a dash, so it sorts last."""
    return None if reward == _EMPTY else amount


def _bookshelf_fields(item_id: int) -> dict:
    """The theme's bookshelf item: ID (None for none), name in its grade colour and icon path."""
    if not item_id:
        return {"bookshelf_item": None, **pa_fields("bookshelf", ""), "bookshelf_icon_path": ""}
    return {
        "bookshelf_item": item_id,
        **pa_fields("bookshelf", item_key_text_tagged(item_id)),
        "bookshelf_icon_path": icon_path(IconKind.ITEM, item_id),
    }


def _bookshelf_cell(record: dict) -> str:
    """The bookshelf item's icon and name in its grade colour, or a dash."""
    if not record["bookshelf"]:
        return _EMPTY
    return icon_html_label_cell(record["bookshelf_icon_path"], pa_html(record[pa_key("bookshelf")]))


def _theme_record(record: MentalThemeRecord) -> dict:
    reward_1 = _reward(record["increase_wp"], record["need_count"])
    reward_2 = _reward_2(
        record["increase_wp"],
        record["need_count"],
        record["increase_wp_2"],
        record["need_count_2"],
    )
    return {
        "theme_id": record["theme_id"],
        "name": record["name"],
        # 0 marks a root theme. None renders a dash and sorts last.
        "parent_id": record["parent_id"] or None,
        "parent_name": record["parent_name"],
        "energy_reward_1": reward_1,
        "energy_reward_2": reward_2,
        "energy_reward_1_amount": _shown_amount(reward_1, record["increase_wp"]),
        "energy_reward_1_entries": record["need_count"],
        "energy_reward_2_amount": _shown_amount(reward_2, record["increase_wp_2"]),
        "energy_reward_2_entries": record["need_count_2"],
        "entry_count": record["entry_count"],
        "child_count": record["child_count"],
        **_bookshelf_fields(record["bookshelf_item"]),
        "is_copy_right_able": record["is_copy_right_able"],
        "name_kr": record["name_kr"],
        "entry_ids": record["entry_ids"],
        "entry_names": record["entry_names"],
        "child_ids": record["child_ids"],
        "payload_offset": record["payload_offset"],
        "payload_size": record["payload_size"],
        "unknown_after_child_ids": record["unknown_after_child_ids"],
    }


def mental_theme_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("theme_id", "themeId"),
            offset_column("payload_offset", "payloadOffset"),
            size_column("payload_size", "payloadSize"),
        ],
        picked_records(parse_mentalthemeoffset_records, ("theme_id", "payload_offset", "payload_size")),
    )


class MentalThemeHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["themeId"], "num", sort_key="theme_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["parentId"], "num", sort_key="parent_id"),
            Column(cols["parentName"], sort_key="parent_name"),
            Column(cols["energyReward1"], sort_key="energy_reward_1_amount"),
            Column(cols["energyReward2"], sort_key="energy_reward_2_amount"),
            Column(cols["entries"], "num", sort_key="entry_count"),
            Column(cols["childrenGroups"], "num", sort_key="child_count"),
            Column(cols["bookshelf"], sort_key="bookshelf"),
            # is_copy_right_able: the theme gets knowledge grades and can be compiled into a book.
            Column(cols["knowledgeGrade"], sort_key="is_copy_right_able"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/mentalthemeoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("mentalthemeoffset.dbss")
        if offset_raw is None:
            raise ValueError("mentalthemeoffset.dbss companion not found.")

        return [_theme_record(record) for record in parse_mentaltheme_records(data, offset_raw)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]

        with_theme_name = sum(1 for r in records if r["name"])
        with_parent_name = sum(1 for r in records if r["parent_name"])
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            with_theme_name=with_theme_name,
            with_parent_name=with_parent_name,
        )

        rows = [
            [
                e(r["theme_id"]),
                e(r["name"] or _EMPTY),
                e(r["parent_id"] or _EMPTY),
                e(r["parent_name"] or _EMPTY),
                e(r["energy_reward_1"]),
                e(r["energy_reward_2"]),
                e(r["entry_count"]),
                e(r["child_count"]),
                _bookshelf_cell(r),
                flag_cell(r["is_copy_right_able"]),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
