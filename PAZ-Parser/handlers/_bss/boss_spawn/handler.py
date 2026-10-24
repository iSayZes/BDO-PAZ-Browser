"""boss_spawn.bss preview handler: Guild Boss Summon spawn points in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.boss_spawnlevel.parser import FILE_NAME as LEVEL_FILE, optional_boss_characters
from _common.character import character_name
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_boss_spawn_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_AXES = ("x", "y", "z")


class BossSpawnBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["boss"], sort_key="boss_name"),
            Column(cols["levels"], "num", sort_key="max_level"),
            *(Column(cols[axis], "num", sort_key=axis) for axis in _AXES),
            Column(cols["range"], "num", sort_key="range"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{LEVEL_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_boss_spawn_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        characters = optional_boss_characters(companions.get(LEVEL_FILE))
        return [
            {
                **record,
                "character_id": characters.get(record["key"]),
                "boss_name": character_name(characters[record["key"]]) if record["key"] in characters else "",
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
                e(r["key"]),
                e(r["boss_name"] or _EMPTY),
                e(r["max_level"]),
                *(e(f"{r[axis]:,.0f}") for axis in _AXES),
                e(f"{r['range']:,}"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
