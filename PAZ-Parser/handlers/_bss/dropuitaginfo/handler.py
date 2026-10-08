from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, icon_cell, sort_keys, table, text_list_cell
from _common.hunting_ground import hunting_ground_name
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_fields, pa_line_cell
from _bss.dropuihuntinggroundinfo.parser import parse_hunting_ground_records
from .parser import TagColors, parse_tag_records
from .tag_chips import tag_chip
from .text import tag_description_tagged, tag_name


_LANG_DIR = Path(__file__).parent / "lang"
_HUNTING_GROUND_FILE = "dropuihuntinggroundinfo.bss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8


def _argb_text(argb: int) -> str:
    """`0xFFE1BA65`, as the format doc writes a colour."""
    return f"0x{argb:08X}"


def _hunting_grounds_by_tag(data: bytes) -> dict[int, list[str]]:
    """Tag key -> the names of the hunting grounds that carry it, in file order."""
    grounds: dict[int, list[str]] = defaultdict(list)
    for ground in parse_hunting_ground_records(data):
        name = hunting_ground_name(ground["key"]) or ground["name_kr"].strip()
        for tag_key in ground["tag_keys"]:
            grounds[tag_key].append(name)
    return grounds


class DropUiTagInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["guideImage"], sort_key="guide_texture"),
            Column(cols["colors"], sort_key="texture_color"),
            Column(cols["description"], sort_key="description"),
            # A list column: it would only sort by its string form.
            Column(cols["huntingGrounds"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_HUNTING_GROUND_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        ground_data = companions.get(_HUNTING_GROUND_FILE)
        # Without the hunting ground table the Hunting Grounds column is a dash.
        grounds = _hunting_grounds_by_tag(ground_data) if ground_data else {}

        records: list[dict] = []
        for record in parse_tag_records(data):
            key = record["key"]
            records.append({
                **record,
                "name": tag_name(key) or record["name_kr"].strip(),
                **pa_fields("description", tag_description_tagged(key) or record["description_kr"]),
                "colors": f'{_argb_text(record["texture_color"])} / {_argb_text(record["font_color"])}',
                "hunting_grounds": grounds.get(key, []),
            })
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
        rows = [
            [
                e(r["key"]),
                # The tag as the drop item window draws it.
                tag_chip(r["name"], TagColors(r["texture_color"], r["font_color"])) if r["name"] else _EMPTY,
                icon_cell(r["guide_image_path"]) if r["guide_image_path"] else _EMPTY,
                e(r["colors"]),
                pa_line_cell(r, "description"),
                text_list_cell(r["hunting_grounds"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
