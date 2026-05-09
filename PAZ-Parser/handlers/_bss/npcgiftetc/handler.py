from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.binary import u16, u32
from _common.html import e, table
from _common.lang import load_handler_strings


_SIZE = 32
_MAGIC = b"PABR"
_LANG_DIR = Path(__file__).parent / "lang"

_FIELDS = [
    ("config_a", 0x04, "u16", "Global gift-system value"),
    ("config_b", 0x06, "u16", "Global gift-system value"),
    ("config_c", 0x08, "u32", "Global gift-system value"),
    ("config_d", 0x0C, "u32", "Global gift-system value"),
    ("reserved0", 0x10, "u32", "Observed zero"),
    ("reserved1", 0x14, "u32", "Observed zero"),
    ("config_e", 0x18, "u32", "Global gift-system value"),
    ("reserved2", 0x1C, "u32", "Observed zero"),
]

def _parse_value(data: bytes, offset: int, type_name: str) -> int:
    if type_name == "u16":
        return u16(data, offset)
    return u32(data, offset)


class NpcGiftEtcBssHandler(PreviewHandler):
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
        strings = load_handler_strings(self.lang, _LANG_DIR)
        cols = strings.get("columns", {})
        notes = strings.get("notes", {})
        headers = [
            (cols.get("field", "Field"), "", ""),
            (cols.get("value", "Value"), "num", ""),
            (cols.get("notes", "Notes"), "", ""),
        ]
        rows = [
            [e(r["field"]), e(r["value"]), e(notes.get(r["notes"], r["notes"]))]
            for r in slice_
        ]
        return table(f"{len(records):,} config fields", headers, rows)
