from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.buff import buff_loc_description
from _common.duration import format_duration
from _common.html import Column, e, icon_cell, sort_keys, table, truncate
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.lookup_index import IndexKind, index_entries, lookup
from _common.pa_text import pa_cell, pa_fields, pa_html, pa_key
from _common.pabr_offset import parse_pabr_u32_offset_rows
from _common.offset_table import (
    OffsetColumn,
    OffsetTableHandler,
    offset_column,
    offset_records,
    size_column,
)
from .effect import EffectInput, effect_text, param_labels
from .parser import PARAM_COUNT, parse_buff_records
from .title import extract_title_pa, title_leaders


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "buffoffset.dbss"

_EMPTY = "-"
_SHOWN_PARAMS = 3
_LIST_PREVIEW_ITEMS = 3
# Longer Param labels (character and quest names) are cut, in full on hover.
_PARAM_LABEL_CHARS = 24


def _raw_description(buff_id: int, description_kr: str) -> str:
    """English description from LOC with PA tags intact, else the inline Korean."""
    return buff_loc_description(buff_id) or description_kr


def _applying_items(buff_id: int) -> list[int]:
    """Base items whose skills apply the buff, from the BUFF_ITEMS lookup index."""
    item_ids = lookup(IndexKind.BUFF_ITEMS, buff_id)
    return list(item_ids) if isinstance(item_ids, tuple) else []


def _skill_buff_lists() -> list[tuple[int, ...]]:
    """The buffs each skill applies together, from the SKILL_BUFFS lookup index."""
    return [buff_ids for buff_ids in index_entries(IndexKind.SKILL_BUFFS).values() if isinstance(buff_ids, tuple)]


def _effect_input(record: dict) -> EffectInput:
    """The fields the effect of a buff record reads."""
    return EffectInput(
        record["effect_type"],
        [record[f"param_{index}"] for index in range(1, PARAM_COUNT + 1)],
        tick_ms=record["tick_ms"],
        condition_type=record["condition_type"],
        # get_records turns a zero duration into None for sorting.
        duration_ms=record["duration_ms"] or 0,
        icon_path=record["icon_path"],
    )


def _param_cell(value: int, label: str | None) -> str:
    """`25000 (2.5%)`: the stored value, then what it means for the effect type."""
    if not label:
        return e(value)
    short = truncate(label, _PARAM_LABEL_CHARS)
    text = e(f"{value} ({short})")
    return text if short == label else f'<span title="{e(label)}">{text}</span>'


def _title_cell(record: dict) -> str:
    """The title in its game colour; one taken from the headline buff it is
    applied with is dimmed."""
    if not record["title"]:
        return _EMPTY
    title = pa_html(record[pa_key("title")])
    if record["title_buff_id"] == record["buff_id"]:
        return title
    tooltip = f"Title of buff {record['title_buff_id']}"
    return f'<span class="inherited-cell" title="{e(tooltip)}">{title}</span>'


def buff_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("buff_id", "buffId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_pabr_u32_offset_rows, "buff_id"),
    )


def _add_inherited_titles(records: list[dict]) -> None:
    """Give untitled buffs the title of the headline buff they are applied with.

    `title_buff_id` names the buff whose description holds the title: the
    buff itself, the headline buff, or None without a title.
    """
    titled = {r["buff_id"]: r for r in records if r["title"]}
    leaders = title_leaders(_skill_buff_lists(), {buff_id: r["title"] for buff_id, r in titled.items()})
    for record in records:
        buff_id = record["buff_id"]
        title_buff_id = buff_id if buff_id in titled else leaders.get(buff_id)
        record["title_buff_id"] = title_buff_id
        if title_buff_id is not None:
            leader = titled[title_buff_id]
            record["title"] = leader["title"]
            record[pa_key("title")] = leader[pa_key("title")]


def _buff_row(r: dict) -> list[str]:
    labels = param_labels(_effect_input(r))
    return [
        e(r["buff_id"]),
        icon_cell(r["icon_path"]) if r["icon_path"] else _EMPTY,
        _title_cell(r),
        e(r["name"]),
        pa_cell(r, "description"),
        e(r["effect"]) if r["effect"] else _EMPTY,
        item_key_list_cell(r["applied_by_item_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
        e(r["level"]),
        e(r["effect_type"]),
        e(r["duration"]) if r["duration"] else _EMPTY,
        *(_param_cell(r[f"param_{index}"], labels.get(index)) for index in range(1, _SHOWN_PARAMS + 1)),
    ]


class BuffHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["buffId"], "num", sort_key="buff_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["title"], sort_key="title"),
            Column(cols["name"], sort_key="name"),
            Column(cols["description"], sort_key="description"),
            Column(cols["effect"], sort_key="effect"),
            Column(cols["appliedBy"], sort_key="applied_by_count"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["effectType"], "num", sort_key="effect_type"),
            Column(cols["duration"], "num", sort_key="duration_ms"),
            *(
                Column(cols.get(f"param{index}", f"Param {index}"), "num", sort_key=f"param_{index}")
                for index in range(1, _SHOWN_PARAMS + 1)
            ),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_data = companions.get(_OFFSET_FILE)
        if not offset_data:
            raise ValueError(f"{_OFFSET_FILE} companion not found")

        records = parse_buff_records(data, parse_pabr_u32_offset_rows(offset_data))
        for record in records:
            raw = _raw_description(record["buff_id"], record["description_kr"])
            record.update(pa_fields("title", extract_title_pa(raw)))
            record.update(pa_fields("description", raw))
            record["effect"] = effect_text(_effect_input(record))
            record["duration"] = format_duration(record["duration_ms"])
            # 0 means no duration. None renders a dash and sorts last.
            record["duration_ms"] = record["duration_ms"] or None
            item_ids = _applying_items(record["buff_id"])
            record["applied_by_item_ids"] = item_ids
            record["applied_by"] = [item_key_text(item_id) for item_id in item_ids]
            record["applied_by_count"] = len(item_ids) or None
        _add_inherited_titles(records)
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), [_buff_row(r) for r in slice_])
