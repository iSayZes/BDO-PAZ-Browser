from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.client_versions import covering
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, KeyHashes, ui_key_hashes
from .names import value_name
from .parser import parse_quest_counts
from .tables import QuestCountTable


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _naming_table(quest_table: QuestCountTable, value_count: int) -> QuestCountTable | None:
    """The table that names the values, or None.

    An older enum names the file on the clients in its range. Otherwise the
    live enum names it when the file holds the whole enum; a shorter file
    comes from a client whose enum order is not confirmed.
    """
    older = covering(quest_table.older, lambda table: table.clients)
    if older is not None:
        return older
    return quest_table if value_count >= len(quest_table.enum_names) else None


def quest_count_records(quest_table: QuestCountTable, data: bytes, hashes: KeyHashes) -> list[dict]:
    """One record per value, with the name the client's quest window shows, else ''."""
    counts = parse_quest_counts(data, quest_table.file_name)
    naming = _naming_table(quest_table, len(counts))
    return [
        {
            quest_table.key_field: value,
            quest_table.name_field: "" if naming is None else value_name(naming, hashes, value),
            "quest_count": count,
        }
        for value, count in enumerate(counts)
    ]


class TotalQuestCountBssHandler(PreviewHandler):
    """Quests per region or per quest type; one instance per file."""

    def __init__(self, quest_table: QuestCountTable) -> None:
        self._table = quest_table

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols[self._table.key_column], "num", sort_key=self._table.key_field),
            Column(cols[self._table.name_column], sort_key=self._table.name_field),
            Column(cols["questCount"], "num", sort_key="quest_count"),
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
        return quest_count_records(self._table, data, hashes)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, f"meta.{self._table.count_meta}", count=len(records))
        rows = [
            [
                e(r[self._table.key_field]),
                e(r[self._table.name_field] or _EMPTY),
                e(r["quest_count"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
