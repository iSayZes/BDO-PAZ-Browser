from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags

from _common.binary import parse_offset_table
from _common.html import color_cell, e, table
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


def _title_cell(title: str, css_color: str) -> str:
    if not css_color:
        return e(title)

    return f'<span style="color:{e(css_color)}">{e(title)}</span>'


class TitleDbssHandler(PreviewHandler):
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

        result: list[dict] = []
        for rec in records:
            row: dict = dict(rec)
            if is_loc_loaded():
                row["en_name"] = loc_lookup(1, rec["title_id"])
                row["en_req"] = strip_pa_tags(loc_lookup(1, rec["title_id"], 0, 0, 1))
            result.append(row)

        return result

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("titleId",           "Title ID"),           "num", ""),
            (cols.get("category",          "Category"),           "",    ""),
            (cols.get("titleColor",        "Title Color"),        "",    ""),
            (cols.get("title",             "Title"),              "",    ""),
            (cols.get("titleRequirements", "Title Requirements"), "",    ""),
            (cols.get("special",           "Special"),            "",    ""),
            (cols.get("effect",            "Effect"),             "",    ""),
        ]

        start = page * page_size
        slice_ = records[start : start + page_size]

        rows: list[list] = []
        for record in slice_:
            title_color = record["title_color_argb"]
            title_color_hex = title_color[4:] if title_color.startswith("0xFF") else ""
            title = strip_pa_tags(record.get("en_name") or record["title_text_ko"])
            requirement = strip_pa_tags(record.get("en_req") or record["requirement_text_ko"])
            is_special = bool(title_color or record["header_field_meaning"] != "style")

            rows.append([
                e(record["title_id"]),
                e(_category_label(record["category_id"])),
                color_cell([title_color_hex]) if title_color_hex else "-",
                _title_cell(title, record["title_color_css"]),
                e(requirement),
                e("True" if is_special else "False"),
                e(record["title_effect_name"] or "-"),
            ])

        return table(f"{len(records):,} titles decoded", headers, rows)
