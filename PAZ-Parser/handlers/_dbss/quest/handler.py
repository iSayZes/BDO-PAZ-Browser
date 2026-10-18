from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from record_fields import record_matches
from table_sort import TableSort, sort_order_by_values

from _common.loc import is_loc_loaded, resolve_text_binds
from _common.pa_text import pa_cell, pa_fields, strip_pa_tags

from _common.html import Column, e, icon_cell, sort_keys, table, truncate
from _common.lang import handler_text, load_handler_strings
from _common.quest.dialog import dialog_cell, dialog_speaker
from _common.quest.quest import quest_text_tagged
from _bss.allquestlist.parser import parse_allquestlist_records
from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, KeyHashes, ui_key_hashes
from _bss.totalquestcount.names import value_name
from _bss.totalquestcount.tables import QUEST_TYPE_TABLE
from .model import FamilyStat
from .parser import QuestIndex, build_quest_index, parse_quest_record


_LANG_DIR = Path(__file__).parent / "lang"
_ORDER_FILE = "allquestlist.bss"


_TEXT_PREVIEW_CHARS = 140


def _truncate(text: str) -> str:
    return truncate(text, _TEXT_PREVIEW_CHARS)


def _quest_loc_texts(quest_chain_id: int, quest_id: int) -> list[str]:
    """LOC type 18 texts of a quest with their PA tags and TextBinds filled, each visible text once."""
    if not is_loc_loaded():
        return []

    seen: set[str] = set()
    texts: list[str] = []
    for str_id4 in range(10):
        text = quest_text_tagged(quest_chain_id, quest_id, str_id4)
        clean = strip_pa_tags(text).strip()
        if clean and clean not in seen:
            seen.add(clean)
            texts.append(text)
    return texts


def _title(loc_texts: list[str]) -> str:
    return loc_texts[0] if loc_texts else ""


def _objective(loc_texts: list[str]) -> str:
    return loc_texts[3] if len(loc_texts) > 3 else ""


def _family_stat_text(stats: list[FamilyStat]) -> str:
    """`AP +1, Weight +50 LT`; a stat with an unknown field shows its label alone."""
    parts: list[str] = []
    for stat in stats:
        value = stat["value"]
        if value is None:
            parts.append(stat["label"])
            continue
        unit = " LT" if stat["label"] == "Weight" else ""
        parts.append(f"{stat['label']} {value:+g}{unit}")
    return ", ".join(parts)


class QuestDbssHandler(PreviewHandler):

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["displayId"], "num", sort_key="packed_quest_id"),
            Column(cols["chainId"], "num", sort_key="quest_chain_id"),
            Column(cols["questId"], "num", sort_key="quest_id"),
            Column(cols["category"], "num", sort_key="quest_category"),
            Column(cols["questType"], sort_key="quest_type_name"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["titleName"], sort_key="title"),
            Column(cols["acceptNpc"], sort_key="accept_npc"),
            Column(cols["completeNpc"], sort_key="complete_npc"),
            Column(cols["condition"], sort_key="condition_script"),
            Column(cols["action"], sort_key="action_script"),
            Column(cols["objective"], sort_key="objective"),
            Column(cols["familyStat"], sort_key="family_stat_text"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_ORDER_FILE}", f"{folder}/{STRINGTABLE_FILE}"]

    def _get_index(self, data: bytes, companions: dict[str, bytes]) -> QuestIndex:
        def build() -> QuestIndex:
            order_raw = companions.get(_ORDER_FILE)
            if order_raw is None:
                raise ValueError(f"{_ORDER_FILE} companion not found; it gives the record order.")
            ids = [record["packed_quest_id"] for record in parse_allquestlist_records(order_raw)]
            return build_quest_index(data, ids)

        return self._data_cache(data, "index", build)

    def _key_hashes(self, data: bytes, companions: dict[str, bytes]) -> KeyHashes:
        """GAME sheet key hashes for the quest type names; none without `stringtable.bss`."""
        return self._data_cache(
            data, "key_hashes", lambda: ui_key_hashes(companions.get(STRINGTABLE_FILE), [GAME_SHEET])
        )

    def _record_at(self, data: bytes, index: QuestIndex, hashes: KeyHashes, row: int) -> dict:
        parsed = parse_quest_record(data, index, row)
        loc_texts = _quest_loc_texts(parsed["quest_chain_id"], parsed["quest_id"])
        return {
            **parsed,
            "loc_texts_en": [strip_pa_tags(text).strip() for text in loc_texts],
            **pa_fields("title", _title(loc_texts)),
            **pa_fields("objective", _objective(loc_texts) or resolve_text_binds(parsed["objective_text_kr"])),
            # Empty sorts last and exports as an empty cell.
            "family_stat_text": _family_stat_text(parsed["family_stats"]) or None,
            "accept_npc": dialog_speaker(parsed["accept_dialog_key"]),
            "complete_npc": dialog_speaker(parsed["complete_dialog_key"]),
            # quest_category is the quest type (__eQuestType); see quest_dbss.md.
            "quest_type_name": value_name(QUEST_TYPE_TABLE, hashes, parsed["quest_category"]),
        }

    def _records_at(self, data: bytes, companions: dict[str, bytes], rows: Iterable[int]) -> list[dict]:
        index = self._get_index(data, companions)
        hashes = self._key_hashes(data, companions)
        return [self._record_at(data, index, hashes, row) for row in rows]

    def get_record_count(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> int:
        return len(self._get_index(data, companions))

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return self._records_at(data, companions, range(len(self._get_index(data, companions))))

    def render_data_page(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        page: int,
        page_size: int,
    ) -> str:
        total = len(self._get_index(data, companions))
        start_row = page * page_size
        rows = range(start_row, min(total, start_row + page_size))
        return self._render_table(self._records_at(data, companions, rows), total)

    def _sort_columns(self, data: bytes, companions: dict[str, bytes]) -> dict[str, tuple]:
        """Every sortable field's value per row, built in one pass on the first sort.

        Keeps the sort values (about 4 million characters on client 3474) instead of
        every parsed record through get_records(). One pass costs as much as
        sorting by a single field, so later fields and directions are free.
        """
        def build() -> dict[str, tuple]:
            index = self._get_index(data, companions)
            hashes = self._key_hashes(data, companions)
            fields = self.sortable_fields()
            rows = [
                tuple(record.get(field) for field in fields)
                for record in (self._record_at(data, index, hashes, row) for row in range(len(index)))
            ]
            columns = list(zip(*rows)) if rows else [() for _ in fields]
            return dict(zip(fields, columns))

        return self._data_cache(data, "sort_columns", build)

    def _build_sort_order(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        sort: TableSort,
    ) -> list[int]:
        if sort.field == "packed_quest_id":
            # The default sort: the index already holds the IDs, so the table
            # opens without parsing every quest.
            index = self._get_index(data, companions)
            return sort_order_by_values(index.packed_quest_ids, sort.descending)
        values = self._sort_columns(data, companions)[sort.field]
        return sort_order_by_values(values, sort.descending)

    def render_sorted_page(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        page: int,
        page_size: int,
        sort: TableSort,
    ) -> str:
        order = self.sorted_order(data, entry, companions, sort)
        start = page * page_size
        rows = order[start : start + page_size]
        return self._render_table(self._records_at(data, companions, rows), len(order))

    def search_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        query: str,
    ) -> list[int]:
        q = query.lower()
        if not q:
            return []

        matches: list[int] = []
        index = self._get_index(data, companions)
        hashes = self._key_hashes(data, companions)
        for row in range(len(index)):
            record = self._record_at(data, index, hashes, row)
            if record_matches(record, q):
                matches.append(row)

        return matches

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        return self._render_table(records[page * page_size : page * page_size + page_size], len(records))

    def _render_table(self, records: list[dict], total: int) -> str:
        rows: list[list] = []
        with_loc = 0

        for record in records:
            if record.get("loc_texts_en"):
                with_loc += 1

            rows.append([
                e(record["packed_quest_id"]),
                e(record["quest_chain_id"]),
                e(record["quest_id"]),
                e(record["quest_category"]),
                e(record["quest_type_name"] or "-"),
                icon_cell(record["icon_path"]),
                pa_cell(record, "title", _TEXT_PREVIEW_CHARS),
                dialog_cell(record["accept_dialog_key"], record["accept_npc"] or "-"),
                dialog_cell(record["complete_dialog_key"], record["complete_npc"] or "-"),
                e(_truncate(record["condition_script"])),
                e(_truncate(record["action_script"])),
                pa_cell(record, "objective", _TEXT_PREVIEW_CHARS),
                e(record["family_stat_text"] or "-"),
            ])

        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=total)
        if with_loc:
            meta += handler_text(self.lang, _LANG_DIR, "meta.withLoc", with_loc=with_loc)

        return table(meta, self._columns(), rows)
