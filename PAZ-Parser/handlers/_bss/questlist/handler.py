from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, icon_cell, sort_keys, table, truncate
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, loc_tagged
from _common.pa_text import LINE_PREVIEW_CHARS, pa_cell, pa_fields
from _common.quest.quest import quest_title_tagged
from .parser import parse_quest_list_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Each quest list has its own LOC type with the group names, keyed
# (group_key, 0, 0, 0), and each quest's condition line, keyed
# (packed_quest_id, group_key, 0, 1).
QUEST_LIST_LOC_TYPES: dict[str, int] = {
    "newquest.bss": 58,
    "mainquest.bss": 43,
    "recommendationquest.bss": 28,
    "repetitionquest.bss": 42,
}
# Only the event list stores an event period per group; the others leave it blank.
EVENT_PERIOD_LISTS = frozenset({"newquest.bss"})
_FIELD_GROUP_NAME = 0
_FIELD_CONDITION = 1


def _script_cell(script: str) -> str:
    """A condition script on one line, cut like other long text, or a dash."""
    return e(truncate(" ".join(script.split()), LINE_PREVIEW_CHARS)) if script else _EMPTY


class QuestListBssHandler(PreviewHandler):
    def __init__(self, loc_type: int, has_event_period: bool = False) -> None:
        self._loc_type = loc_type
        self._has_event_period = has_event_period

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        event_columns = [
            Column(cols["eventStart"], sort_key="event_start"),
            Column(cols["eventEnd"], sort_key="event_end"),
        ] if self._has_event_period else []
        return [
            Column(cols["mainId"], "num", sort_key="quest_chain_id"),
            Column(cols["subId"], "num", sort_key="quest_id"),
            Column(cols["groupKey"], "num", sort_key="group_key"),
            Column(cols["groupName"], sort_key="group_name"),
            *event_columns,
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["title"], sort_key="title"),
            Column(cols["condition"], sort_key="condition"),
            # The quest window lists a quest while its visible conditions hold
            # and its hide conditions do not.
            Column(cols["shownWhen"], sort_key="visible_conditions"),
            Column(cols["hiddenWhen"], sort_key="hide_conditions"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        has_loc = is_loc_loaded()

        for record in parse_quest_list_records(data):
            row = dict(record)
            title = quest_title_tagged(record["quest_chain_id"], record["quest_id"]) if has_loc else ""
            group_name = loc_tagged(self._loc_type, record["group_key"], _FIELD_GROUP_NAME)
            condition = loc_lookup(
                self._loc_type, record["packed_quest_id"], record["group_key"], 0, _FIELD_CONDITION,
            ).strip()
            row.update(pa_fields("title", title))
            row.update(pa_fields("group_name", group_name or record["group_name_kr"]))
            row.update(pa_fields("condition", condition or record["condition_kr"].strip()))
            row["icon_path"] = icon_path(IconKind.QUEST, record["packed_quest_id"])
            records.append(row)

        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        with_titles = sum(1 for record in records if record.get("title"))
        group_count = len({record["group"] for record in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), group_count=group_count)
        if with_titles:
            meta += handler_text(self.lang, _LANG_DIR, "meta.withTitles", with_titles=with_titles)

        rows = [self._row_cells(record) for record in slice_]
        return table(meta, self._columns(), rows)

    def _row_cells(self, record: dict) -> list[str]:
        event_cells = [
            e(record["event_start"] or _EMPTY),
            e(record["event_end"] or _EMPTY),
        ] if self._has_event_period else []
        return [
            e(record["quest_chain_id"]),
            e(record["quest_id"]),
            e(record["group_key"]),
            pa_cell(record, "group_name"),
            *event_cells,
            icon_cell(record["icon_path"]) if record["icon_path"] else _EMPTY,
            pa_cell(record, "title"),
            pa_cell(record, "condition"),
            _script_cell(record["visible_conditions"]),
            _script_cell(record["hide_conditions"]),
        ]
