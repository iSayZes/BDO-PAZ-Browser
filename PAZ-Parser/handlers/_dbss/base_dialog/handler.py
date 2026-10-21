from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_loc_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup
from _common.pa_text import pa_key, pa_list_cell, strip_pa_tags
from .parser import BaseDialogRecord, parse_base_dialog_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "base_dialogoffset.dbss"
# Keyed (character_id, dialog_index, 0, n): n = 0 the dialog name, 1.. its lines.
_LOC_BASE_DIALOG = 38
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 3


def _dialog_text(record: BaseDialogRecord, field: int) -> str:
    """One LOC string of the dialog with its PA tags, or "" when it has no text."""
    text = loc_lookup(_LOC_BASE_DIALOG, record.character_id, record.dialog_index, 0, field).strip()
    return text if strip_pa_tags(text).strip() else ""


def _record_dict(record: BaseDialogRecord, has_loc: bool) -> dict:
    # English first; the character's LOC name, then the Korean source, stand in.
    name = strip_pa_tags(
        ((_dialog_text(record, 0) or character_loc_name(record.character_id)) if has_loc else "") or record.name_kr
    ).strip()
    lines = [
        (_dialog_text(record, number) if has_loc else "") or line
        for number, line in enumerate(record.lines, start=1)
    ]
    return {
        "key": record.key,
        "character_id": record.character_id,
        "dialog_index": record.dialog_index,
        "character": name,
        "name_kr": record.name_kr,
        "lines": [strip_pa_tags(line).strip() for line in lines],
        pa_key("lines"): lines,
        "lines_kr": list(record.lines),
        # Empty sorts last.
        "line_count": len(record.lines) or None,
    }


class BaseDialogHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["dialog"], "num", sort_key="dialog_index"),
            Column(cols["character"], sort_key="character"),
            Column(cols["lines"], sort_key="line_count"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        has_loc = is_loc_loaded()
        return [_record_dict(record, has_loc) for record in parse_base_dialog_records(data, offset_raw)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        with_lines = sum(1 for r in records if r["lines"])
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), with_lines=with_lines)
        rows = [
            [
                e(r["character_id"]),
                e(r["dialog_index"]),
                e(r["character"] or _EMPTY),
                pa_list_cell(r[pa_key("lines")], _LIST_PREVIEW_ITEMS),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
