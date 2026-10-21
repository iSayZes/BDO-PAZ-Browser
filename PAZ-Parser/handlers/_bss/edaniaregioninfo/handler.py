from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, KeyHashes, ui_key_hashes, ui_key_text
from .parser import EDANIA_REGION_NAMES, parse_edaniaregioninfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# The Edania window (panel_window_edania_contents_all.luac) names each region's
# castle with this GAME sheet key; Orbita and Tenebraum swap numbers 3 and 4.
_CASTLE_NAME_KEY = "LUA_EDANIA_SYSTEM_CASTLE_NAME_{}"
_CASTLE_NAME_NUMBERS = (1, 2, 4, 3, 5, 6, 7, 8, 9, 10)


def _castle_name(hashes: KeyHashes, edania_region: int) -> str:
    """The castle name the Edania window shows, else the enum name, else ''."""
    if edania_region >= len(EDANIA_REGION_NAMES):
        return ""
    key = _CASTLE_NAME_KEY.format(_CASTLE_NAME_NUMBERS[edania_region])
    return ui_key_text(hashes, GAME_SHEET, key) or EDANIA_REGION_NAMES[edania_region]


class EdaniaRegionInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["edaniaRegion"], "num", sort_key="edania_region"),
            Column(cols["castle"], sort_key="castle_name"),
            Column(cols["mapColor"], "num", sort_key="map_color"),
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
            {**record, "castle_name": _castle_name(hashes, record["edania_region"])}
            for record in parse_edaniaregioninfo_records(data)
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
                e(r["edania_region"]),
                e(r["castle_name"] or _EMPTY),
                e(r["map_color"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
