"""boss_spawnlevel.bss preview handler: Guild Boss Summon levels in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, error, icon_cell, sort_keys, table
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_boss_spawnlevel_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_ONE_ITEM = 1


class BossSpawnLevelBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["bossKey"], "num", sort_key="boss_key"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["image"], sort_key="image_path"),
            Column(cols["boss"], sort_key="boss_name"),
            Column(cols["reward"], sort_key="reward_name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_boss_spawnlevel_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "boss_name": character_name(record["character_id"]),
                "reward_name": item_key_text(record["reward_item_id"]),
            }
            for record in records
        ]

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
                e(r["boss_key"]),
                e(r["level"]),
                icon_cell(r["image_path"]),
                e(r["boss_name"] or r["character_id"]),
                item_key_list_cell([r["reward_item_id"]], _ONE_ITEM) if r["reward_item_id"] else _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            bosses=len({r["boss_key"] for r in records}),
        )
        return table(meta, self._columns(), rows)
