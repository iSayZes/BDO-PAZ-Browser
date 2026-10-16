"""bossinfostaicstatusmanager.bss preview handler: the Boss Info window's bosses in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, KeyHashes, ui_key_hashes, ui_key_text
from _common.character import character_name
from _common.html import Column, e, error, sort_keys, sprite_icon_cell, table
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.texture_string import (
    TEXTURE_STRING_COMBINE,
    TEXTURE_STRING_COMBINE_PATH,
    TextureRegion,
    icon_fields,
    parse_texture_regions,
)
from .parser import FILE_NAME, parse_bossinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_TAB_KEY = "LUA_WORLDMAP_BOSSLIST_TOOLTIP_{}"
_REWARD_PREVIEW_ITEMS = 3
# spawn_times group 0; which group the client uses is an open question.
_FIRST_GROUP = 0


def _tab_name(hashes: KeyHashes, boss_info_type: int) -> str:
    """The window tab's name in the loaded language, else the raw type."""
    return ui_key_text(hashes, GAME_SHEET, _TAB_KEY.format(boss_info_type)) or str(boss_info_type)


def _spawn_count(spawn_times: list[dict]) -> int | None:
    """How many times group 0 holds, or None for a "Random Spawn" boss."""
    for group in spawn_times:
        if group["group"] == _FIRST_GROUP:
            return len(group["values"])
    return None


def _display_fields(record: dict, hashes: KeyHashes, textures: dict[str, TextureRegion]) -> dict:
    reinforced_id = record["reinforced_character_id"]
    return {
        "name": character_name(record["character_id"]),
        "tab": _tab_name(hashes, record["boss_info_type"]),
        "reinforced_name": character_name(reinforced_id) if reinforced_id is not None else "",
        "reward_count": len(record["reward_items"]),
        "reward_names": [item_key_text(item_id) for item_id in record["reward_items"]],
        "spawn_count": _spawn_count(record["spawn_times"]),
        "position": f"{record['x']:,.0f}, {record['y']:,.0f}, {record['z']:,.0f}",
        **icon_fields(textures, record["list_texture"]),
    }


class BossInfoStaicStatusManagerBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["name"], sort_key="name"),
            Column(cols["tab"], sort_key="boss_info_type"),
            Column(cols["reinforcedId"], "num", sort_key="reinforced_character_id"),
            Column(cols["reinforcedName"], sort_key="reinforced_name"),
            Column(cols["rewards"], sort_key="reward_count"),
            Column(cols["spawnTimes"], "num", sort_key="spawn_count"),
            Column(cols["position"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{STRINGTABLE_FILE}", TEXTURE_STRING_COMBINE_PATH]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_bossinfo_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        hashes = ui_key_hashes(companions.get(STRINGTABLE_FILE), [GAME_SHEET])
        textures = parse_texture_regions(
            companions.get(TEXTURE_STRING_COMBINE),
            (r["list_texture"] for r in records),
        )
        return [{**record, **_display_fields(record, hashes, textures)} for record in records]

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
                e(r["character_id"]),
                sprite_icon_cell(r["icon_path"], r["icon_region"]),
                e(r["name"] or _EMPTY),
                e(r["tab"]),
                e(r["reinforced_character_id"] if r["reinforced_character_id"] is not None else _EMPTY),
                e(r["reinforced_name"] or _EMPTY),
                item_key_list_cell(r["reward_items"], _REWARD_PREVIEW_ITEMS) if r["reward_items"] else _EMPTY,
                e(r["spawn_count"] if r["spawn_count"] is not None else _EMPTY),
                e(r["position"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
