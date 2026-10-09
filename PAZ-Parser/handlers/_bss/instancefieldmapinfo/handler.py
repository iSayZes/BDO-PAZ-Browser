from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, KeyHashes, ui_key_hashes, ui_key_text
from _common.html import Column, e, icon_cell, sort_keys, sprite_icon_cell, table
from _common.instance_field import instance_field_name
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from .parser import parse_instancefieldmapinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_CM_PER_M = 100
# The Crimson field maps store this region for their whole image.
_WHOLE_IMAGE = [0, 0, 1, 1]
_AXES = ("x", "y", "z")


def _ui_text(hashes: KeyHashes, key: str) -> str:
    """The key's GAME sheet text in the loaded language, else ''."""
    return ui_key_text(hashes, GAME_SHEET, key) if key else ""


def _display_fields(record: dict, hashes: KeyHashes) -> dict:
    """Fields the table shows, with None where the file stores no value."""
    has_position = any(record[axis] for axis in _AXES)
    item_id = record["entry_item_id"] or None
    return {
        "field_name": instance_field_name(record["key"]) or None,
        # The key itself when LOC has no text, as menu.bss does.
        "title": _ui_text(hashes, record["title_key"]) or record["title_key"] or None,
        "description": _ui_text(hashes, record["description_key"]) or None,
        **{f"pos_{axis}": record[axis] if has_position else None for axis in _AXES},
        "radius_m": record["radius"] / _CM_PER_M if record["radius"] else None,
        "entry_item_id": item_id,
        "entry_item": item_key_text(item_id) if item_id else None,
        "spawn_count": len(record["spawns"]),
    }


def _image_cell(record: dict) -> str:
    path = record["image_path"]
    if not path:
        return _EMPTY
    region = record["image_region"]
    return icon_cell(path) if region == _WHOLE_IMAGE else sprite_icon_cell(path, region)


def _number_cell(value: float | None, digits: int = 0) -> str:
    return _EMPTY if value is None else e(f"{value:,.{digits}f}")


class InstanceFieldMapInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["field"], sort_key="field_name"),
            Column(cols["title"], sort_key="title"),
            Column(cols["description"], sort_key="description"),
            *(Column(cols[axis], "num", sort_key=f"pos_{axis}") for axis in _AXES),
            Column(cols["radius"], "num", sort_key="radius_m"),
            Column(cols["image"], sort_key="image_path"),
            Column(cols["entryItem"], sort_key="entry_item"),
            Column(cols["spawns"], "num", sort_key="spawn_count"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{STRINGTABLE_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        hashes = ui_key_hashes(companions.get(STRINGTABLE_FILE), [GAME_SHEET])
        return [
            {**record, **_display_fields(record, hashes)}
            for record in parse_instancefieldmapinfo_records(data)
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
                e(r["key"]),
                e(r["field_name"] or _EMPTY),
                e(r["title"] or _EMPTY),
                e(r["description"] or _EMPTY),
                *(_number_cell(r[f"pos_{axis}"]) for axis in _AXES),
                _number_cell(r["radius_m"]),
                _image_cell(r),
                item_key_list_cell([r["entry_item_id"]], 1) if r["entry_item_id"] else _EMPTY,
                e(r["spawn_count"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
