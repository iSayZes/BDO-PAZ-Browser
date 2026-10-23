"""eventmanagement.bss preview handler: the scheduled world events, then the event contents they set.

An event row shows its condition script, the period it names and the
contents rows it sets; a contents row shows its function and parameters and
the events that set it. Each linked key opens the other row of this file.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import TableSort

from _common.character import character_name
from _common.html import Column, e, hidden_slice, html_list_cell, record_link, text_list_cell, truncate
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_eventmanagement
from .records import CONTENTS_SECTION, EVENT_SECTION, ROW_REF_FIELD, eventmanagement_records, row_ref


_LANG_DIR = Path(__file__).parent / "lang"
_PATH = f"gamecommondata/binary/{FILE_NAME}"
_EMPTY = "-"
_LINK_CLASS = "record-link"
_MAX_LINKS = 6
_MAX_CHARACTERS = 4
_DETAILS_CHARS = 160
# What the linked keys of each section point at.
_LINKED_SECTION = {EVENT_SECTION: CONTENTS_SECTION, CONTENTS_SECTION: EVENT_SECTION}


def _character_label(character_key: int) -> str:
    """`Dastard Bheg (28922)`, or the bare key without a name."""
    name = character_name(character_key)
    return f"{name} ({character_key})" if name else str(character_key)


def _linked_cell(record: dict) -> str:
    """The linked keys, each a button that opens its row in this file."""
    keys = record["linked_keys"]
    section = _LINKED_SECTION[record["section"]]
    links = [
        record_link(str(key), _PATH, ROW_REF_FIELD, row_ref(section, key), _LINK_CLASS)
        for key in keys[:_MAX_LINKS]
    ]
    hidden = [str(key) for key in hidden_slice(keys, _MAX_LINKS)]
    return html_list_cell(links, len(keys) - _MAX_LINKS, hidden)


class EventManagementHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["key"], "num", sort_key="key"),
            Column(labels["section"], sort_key="section"),
            Column(labels["name"], sort_key="name"),
            Column(labels["details"], sort_key="details"),
            Column(labels["periodStart"], sort_key="period_start"),
            Column(labels["periodEnd"], sort_key="period_end"),
            # List columns would only sort by their string form.
            Column(labels["characters"]),
            Column(labels["linked"]),
        ]

    def default_sort(self) -> TableSort | None:
        # File view order: the events by key, then the contents rows by key; two fields give it.
        return None

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return eventmanagement_records(parse_eventmanagement(data), _character_label)

    def cells(self, record: dict) -> list[str]:
        sections = load_handler_strings(self.lang, _LANG_DIR)["sections"]
        return [
            e(record["key"]),
            e(sections[record["section"]]),
            e(record["name"]) or _EMPTY,
            e(truncate(record["details"], _DETAILS_CHARS)) or _EMPTY,
            e(record["period_start"] or _EMPTY),
            e(record["period_end"] or _EMPTY),
            text_list_cell(record["character_names"], _MAX_CHARACTERS) or _EMPTY,
            _linked_cell(record) or _EMPTY,
        ]
