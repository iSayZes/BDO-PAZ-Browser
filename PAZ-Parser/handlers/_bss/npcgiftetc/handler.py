from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.binary import u16, u32, u64
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings


_SIZE = 32
_MAGIC = b"PABR"
_LANG_DIR = Path(__file__).parent / "lang"

# The named fields are the NpcGift_Option sheet columns, in sheet order.
_FIELDS = [
    ("use_gift_wp", 0x04, "u16", "Energy cost of a gift"),
    ("use_propose_wp", 0x06, "u16", "Energy cost of a confession"),
    ("min_propose_intimacy", 0x08, "u32", "Lowest amity for a confession"),
    ("limit_gift_price", 0x0C, "u64", "Highest item price for a gift"),
    ("unknown_14", 0x14, "u32", "Observed zero"),
    ("unknown_18", 0x18, "u32", "Global gift-system value"),
    ("unknown_1c", 0x1C, "u32", "Observed zero"),
]

_READERS = {"u16": u16, "u32": u32, "u64": u64}


def _parse_value(data: bytes, offset: int, type_name: str) -> int:
    return _READERS[type_name](data, offset)


class NpcGiftEtcBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["field"], sort_key="field"),
            Column(cols["value"], "num", sort_key="value"),
            Column(cols["notes"], sort_key="notes"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        if len(data) != _SIZE:
            raise ValueError(f"npcgiftetc.bss expected {_SIZE} bytes, got {len(data)}.")
        if data[:4] != _MAGIC:
            magic = data[:4].decode("ascii", errors="replace")
            raise ValueError(f"npcgiftetc.bss expected PABR magic, got {magic!r}.")

        return [
            {
                "field": name,
                "value": _parse_value(data, offset, type_name),
                "notes": notes,
            }
            for name, offset, type_name, notes in _FIELDS
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        notes = load_handler_strings(self.lang, _LANG_DIR)["notes"]
        rows = [
            [e(r["field"]), e(r["value"]), e(notes.get(r["notes"], r["notes"]))]
            for r in slice_
        ]
        return table(handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records)), self._columns(), rows)
