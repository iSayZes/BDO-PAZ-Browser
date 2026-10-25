"""`.cl` preview handler: a class combo list as one row per combo.

The Parsed tab, named Combo List, shows a summary and the combos in file
order; the Text tab next to it shows the file's XML. See
docs/file-formats/other/combolist_cl.md.
"""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler, TextHandler, decode_text
from table_sort import TableSort

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .combolist import parse_combo_list
from .records import combo_records
from .render import ComboRenderer

_LANG_DIR = Path(__file__).parent / "lang"
_TEXT_VIEW = TextHandler()


class ComboListHandler(PreviewHandler):
    """Opens in file order, where the section titles read as in the file."""

    def _strings(self) -> dict:
        return load_handler_strings(self.lang, _LANG_DIR)

    def _columns(self) -> list[Column]:
        cols = self._strings()["columns"]
        return [
            Column(cols["combo"], sort_key="combo"),
            Column(cols["weapon"], sort_key="weapon"),
            Column(cols["consoleOnly"], sort_key="console_only"),
            Column(cols["checks"]),
            Column(cols["steps"]),
        ]

    def parsed_label(self) -> str:
        return self._strings()["tab"]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        return None

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        return combo_records(parse_combo_list(decode_text(data)), self._strings())

    def render_text(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        return _TEXT_VIEW.render(data, entry, companions)

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        strings = self._strings()
        renderer = ComboRenderer(records, strings)
        start = page * page_size
        rows = []
        # A section title shows on its first row, and again at the top of a page.
        section = None
        for record in records[start : start + page_size]:
            is_new_section = record["section"] != section
            section = record["section"]
            rows.append([
                renderer.id_cell(record, section if is_new_section else ""),
                renderer.weapon_cell(record),
                renderer.console_only_cell(record),
                renderer.checks_cell(record),
                renderer.steps_cell(record),
            ])
        command_count = records[0]["_file"]["commands"] if records else 0
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return (
            '<div class="ai-combo-list">'
            f'{renderer.summary(command_count)}'
            f'{table(meta, self._columns(), rows)}'
            f'<p class="ai-footnote">{e(strings["footnote"])}</p>'
            '</div>'
        )
