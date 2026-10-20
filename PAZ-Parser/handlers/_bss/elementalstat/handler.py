from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.enum_name import enum_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.string_hash import key_hash
from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from .parser import ELEMENT_TYPE_NAMES, parse_elementalstat


_LANG_DIR = Path(__file__).parent / "lang"
# The Black Shrine window (panel_window_morningland_boss_all.luac,
# _attributeDesc) names each aura with these GAME sheet keys, by element_type.
_AURA_NAME_KEYS: tuple[str, ...] = (
    "LUA_MORNING_ATTRBOSS_SUN",
    "LUA_MORNING_ATTRBOSS_MOON",
    "LUA_MORNING_ATTRBOSS_SOIL",
)


def aura_name(element_type: int) -> str:
    """The aura name the Black Shrine window shows, else the enum name."""
    if 0 <= element_type < len(_AURA_NAME_KEYS):
        text = ui_hash_text(GAME_SHEET, key_hash(_AURA_NAME_KEYS[element_type]))
        if text:
            return text
    return enum_name(ELEMENT_TYPE_NAMES, element_type)


class ElementalStatBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["elementType"], "num", sort_key="element_type"),
            Column(cols["aura"], sort_key="aura"),
            Column(cols["apPerOrb"], "num", sort_key="ap_per_orb"),
            Column(cols["dpPerOrb"], "num", sort_key="dp_per_orb"),
            Column(cols["statPointsPerOrb"], "num", sort_key="stat_points_per_orb"),
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
            {**record, "aura": aura_name(record["element_type"])}
            for record in parse_elementalstat(data)
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
                e(r["element_type"]),
                e(r["aura"]),
                e(r["ap_per_orb"]),
                e(r["dp_per_orb"]),
                e(r["stat_points_per_orb"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
