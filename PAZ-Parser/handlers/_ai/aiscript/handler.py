"""`.ai` preview handler: an NPC or monster AI script as one row per state.

The Parsed tab is the AI Script view (summary, then the states in file
order); the Text tab next to it shows the script's XML. See
docs/file-formats/aiscript_ai.md.
"""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler, TextHandler, decode_text
from table_sort import TableSort

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .records import script_records
from .render import ScriptRenderer
from .script import parse_script

_LANG_DIR = Path(__file__).parent / "lang"
_TEXT_VIEW = TextHandler()


class AiScriptHandler(PreviewHandler):
    """Opens in file order, where the section titles read as in the file. A
    sorted page gets render_records_page() the sorted list, so the state
    links' record indices follow the shown order."""

    def _strings(self) -> dict:
        return load_handler_strings(self.lang, _LANG_DIR)

    def _columns(self) -> list[Column]:
        cols = self._strings()["columns"]
        return [
            Column(cols["state"], sort_key="state"),
            Column(cols["behavior"], sort_key="behavior"),
            Column(cols["cycle"], "num", sort_key="cycle_ms"),
            Column(cols["runs"]),
            Column(cols["transitions"]),
            Column(cols["reachedFrom"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        return None

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        return script_records(parse_script(decode_text(data)), self._strings())

    def render_text(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        return _TEXT_VIEW.render(data, entry, companions)

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        strings = self._strings()
        renderer = ScriptRenderer(records, strings)
        start = page * page_size
        rows = []
        # A section title shows on its first row, and again at the top of a page.
        section = None
        for record in records[start : start + page_size]:
            is_new_section = record["section"] != section
            section = record["section"]
            rows.append([
                renderer.id_cell(record, section if is_new_section else ""),
                renderer.behavior_cell(record),
                '<span class="ai-dim">-</span>' if record["cycle_ms"] is None else e(record["cycle_ms"]),
                renderer.runs_cell(record),
                renderer.transitions_cell(record),
                renderer.reached_from_cell(record),
            ])
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return (
            '<div class="ai-script">'
            f'{renderer.summary()}'
            f'{table(meta, self._columns(), rows)}'
            f'<p class="ai-footnote">{e(strings["footnote"])}</p>'
            '</div>'
        )
