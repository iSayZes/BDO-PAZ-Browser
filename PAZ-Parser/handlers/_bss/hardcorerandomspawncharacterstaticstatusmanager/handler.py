from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.string_hash import key_hash
from _bss.stringtable.parser import RESOURCE_SHEET
from _bss.stringtable.text import ui_hash_text
from .parser import RandomSpawnFile, parse_random_spawn_file


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Which list after the rows holds a row's random_spawn_key; the lang `spawnLists` labels.
BOSS_LIST = "boss"
NPC_LIST = "npc"


def _notice_text(key: str) -> str:
    """LOC text of a RESOURCE sheet notice key (`PANEL_BIGNAK_HARDCOREMESSAGE_4`), else the key."""
    if not key:
        return ""
    return ui_hash_text(RESOURCE_SHEET, key_hash(key)) or key


def _spawn_list(parsed: RandomSpawnFile, random_spawn_key: int) -> str:
    if random_spawn_key in parsed.boss_keys:
        return BOSS_LIST
    return NPC_LIST if random_spawn_key in parsed.npc_keys else ""


def _text_cell(value: str) -> str:
    return e(value) if value else _EMPTY


class HardcoreRandomSpawnCharacterStaticStatusManagerBssHandler(PreviewHandler):
    """One row per random spawn: its character, the list it is on, its icons and notices."""

    def _strings(self) -> dict:
        return load_handler_strings(self.lang, _LANG_DIR)

    def _columns(self) -> list[Column]:
        cols = self._strings()["columns"]
        return [
            Column(cols["randomSpawnKey"], "num", sort_key="random_spawn_key"),
            Column(cols["characterId"], "num", sort_key="character_key"),
            Column(cols["character"], sort_key="character_name"),
            Column(cols["spawnList"], sort_key="spawn_list"),
            Column(cols["worldMapIcon"], sort_key="world_map_icon"),
            Column(cols["bossIcon"], sort_key="boss_icon"),
            Column(cols["noticeBackground"], sort_key="notice_background"),
            Column(cols["notice"], sort_key="notice"),
            Column(cols["revealNotice"], sort_key="reveal_notice"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        parsed = parse_random_spawn_file(data)
        return [
            {
                **row,
                "character_name": character_name(row["character_key"]),
                "spawn_list": _spawn_list(parsed, row["random_spawn_key"]),
                "notice": _notice_text(row["notice_key"]),
                "reveal_notice": _notice_text(row["reveal_notice_key"]),
            }
            for row in parsed.rows
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        strings = self._strings()
        lists = strings["spawnLists"]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["random_spawn_key"]),
                e(r["character_key"]),
                _text_cell(r["character_name"]),
                _text_cell(lists.get(r["spawn_list"], "")),
                _text_cell(r["world_map_icon"]),
                _text_cell(r["boss_icon"]),
                _text_cell(r["notice_background"]),
                _text_cell(r["notice"]),
                _text_cell(r["reveal_notice"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
