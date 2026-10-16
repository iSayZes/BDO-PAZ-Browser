from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup
from _common.pa_text import argb_css, pa_cell, pa_fields, pa_html, pa_key

from _common.binary import parse_offset_table
from _common.html import Column, e, sort_keys, table
from .parser import extract_title_records


_LANG_DIR = Path(__file__).parent / "lang"

_CATEGORY_NAMES: dict[int, str] = {
    0: "World",
    1: "Combat",
    2: "Life Skill",
    3: "Fishing",
}


def _category_label(category_id: int) -> str:
    return _CATEGORY_NAMES.get(category_id, str(category_id))


def _title_cell(record: dict) -> str:
    """The title in its stored colour, with the colours of its own tags on top.

    362 titles store one colour in the record (`title_color_argb`); about 30
    names colour themselves with tags instead, such as the MASTER WARRIOR
    gradients.
    """
    title = pa_html(record[pa_key("title")])
    stored = record["title_color_argb"]
    if not stored:
        return title
    return f'<span class="pa-color" style="color: {argb_css(int(stored, 16))}">{title}</span>'


class TitleDbssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["titleId"], "num", sort_key="title_id"),
            Column(cols["category"], sort_key="category"),
            Column(cols["title"], sort_key="title"),
            Column(cols["titleRequirements"], sort_key="requirement"),
            Column(cols["special"], sort_key="is_special"),
            Column(cols["effect"], sort_key="title_effect_name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/titleoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("titleoffset.dbss")
        if offset_raw is None:
            raise ValueError("titleoffset.dbss companion not found - cannot parse blocks.")

        offset_map = parse_offset_table(offset_raw)
        records = extract_title_records(data, offset_map)

        has_loc = is_loc_loaded()
        result: list[dict] = []
        for rec in records:
            row: dict = dict(rec)
            if has_loc:
                row["en_name"] = loc_lookup(1, rec["title_id"])
                row["en_req"] = loc_lookup(1, rec["title_id"], 0, 0, 1)
            row["category"] = _category_label(rec["category_id"])
            row.update(pa_fields("title", row.get("en_name") or rec["title_text_kr"]))
            row.update(pa_fields("requirement", row.get("en_req") or rec["requirement_text_kr"]))
            row["is_special"] = bool(rec["title_color_argb"] or rec["is_styled_title"])
            result.append(row)

        return result

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]

        rows = [
            [
                e(record["title_id"]),
                e(record["category"]),
                _title_cell(record),
                pa_cell(record, "requirement"),
                e("True" if record["is_special"] else "False"),
                e(record["title_effect_name"] or "-"),
            ]
            for record in slice_
        ]

        return table(handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records)), self._columns(), rows)
