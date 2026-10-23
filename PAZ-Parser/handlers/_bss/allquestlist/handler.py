from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.lang import handler_text, load_handler_strings
from _common.html import Column, e, icon_cell, record_link, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.loc import is_loc_loaded
from _common.pa_text import pa_cell, pa_fields
from _common.quest.quest import quest_title_tagged
from .olvia_academy import QuestPlace, QuestPlaces
from .parser import parse_allquestlist_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINK_CLASS = "record-link"
# A quest's place in the `QuestPlaces` table, and the target row's link value.
PLACE_FIELD = "place"
PLACE_REF_FIELD = "place_ref"


class AllQuestListBssHandler(PreviewHandler):
    """A list of packed quest IDs; with `places`, each quest's place in another table follows its title."""

    def __init__(self, places: QuestPlaces | None = None) -> None:
        self._places = places

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        columns = [
            Column(cols["mainId"], "num", sort_key="quest_chain_id"),
            Column(cols["subId"], "num", sort_key="quest_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["title"], sort_key="title"),
        ]
        if self._places is not None:
            columns.append(Column(cols[self._places.column], sort_key=PLACE_FIELD))
        return columns

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        if self._places is None:
            return []
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{self._places.file_name}"]

    def _read_places(self, companions: dict[str, bytes]) -> dict[int, QuestPlace]:
        """Each quest's place; none when the table is missing or does not parse, so the list still shows."""
        if self._places is None:
            return {}
        raw = companions.get(self._places.file_name)
        if raw is None:
            return {}
        try:
            return dict(self._places.read(raw))
        except ValueError:
            return {}

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        has_loc = is_loc_loaded()
        places = self._read_places(companions)

        for record in parse_allquestlist_records(data):
            row = dict(record)
            title = quest_title_tagged(record["quest_chain_id"], record["quest_id"]) if has_loc else ""
            row.update(pa_fields("title", title))
            row["icon_path"] = icon_path(IconKind.QUEST, record["packed_quest_id"])
            if self._places is not None:
                place = places.get(record["packed_quest_id"])
                row[PLACE_FIELD] = place.text if place else None
                row[PLACE_REF_FIELD] = place.ref if place else None
            records.append(row)

        return records

    def _place_cell(self, record: dict, places: QuestPlaces) -> str:
        if record.get(PLACE_FIELD) is None:
            return _EMPTY
        return record_link(record[PLACE_FIELD], places.path, places.target_field, record[PLACE_REF_FIELD], _LINK_CLASS)

    def _cells(self, record: dict) -> list[str]:
        cells = [
            e(record["quest_chain_id"]),
            e(record["quest_id"]),
            icon_cell(record["icon_path"]) if record["icon_path"] else _EMPTY,
            pa_cell(record, "title"),
        ]
        if self._places is not None:
            cells.append(self._place_cell(record, self._places))
        return cells

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        with_titles = sum(1 for record in records if record.get("title"))
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        if with_titles:
            meta += handler_text(self.lang, _LANG_DIR, "meta.withTitles", with_titles=with_titles)

        return table(meta, self._columns(), [self._cells(record) for record in slice_])
