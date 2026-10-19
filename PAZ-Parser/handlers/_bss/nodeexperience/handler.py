from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_nodeexperience_records


_LANG_DIR = Path(__file__).parent / "lang"

# The server turns invested Energy into node EXP at this rate; no client file
# holds it. Measured in game on levels 1 to 4, and the client 1784 server
# dump sets the manager's `_increasePerWP` to it (nodeexperience_bss.md Notes).
EXP_PER_ENERGY = 100

# Level 0 is a node with no investment; its 1 EXP is no Energy cost.
NOT_INVESTED_LEVEL = 0


def energy_to_next_level(record: dict) -> int | None:
    """Energy to the next level, or None on the not-invested row."""
    if record["level"] == NOT_INVESTED_LEVEL:
        return None
    return record["exp"] // EXP_PER_ENERGY


class NodeExperienceBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["exp"], "num", sort_key="exp"),
            Column(cols["energy"], "num", sort_key="energy"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {**record, "energy": energy_to_next_level(record)}
            for record in parse_nodeexperience_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [e(r["level"]), e(f"{r['exp']:,}"), e("-" if r["energy"] is None else f"{r['energy']:,}")]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
