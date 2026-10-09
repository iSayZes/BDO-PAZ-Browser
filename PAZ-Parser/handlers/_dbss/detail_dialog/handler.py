from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.enum_name import enum_name
from _common.html import Column, e, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup
from _common.pa_text import pa_fields, pa_key, pa_line_cell, pa_list_cell, pa_list_fields, strip_pa_tags
from _common.lease import lease_text_tagged
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.pabr_offset import PabrOffsetRow
from .parser import (
    CONTENTS_TYPE_NAMES,
    DIALOG_BUTTON_TYPE_NAMES,
    DialogRecord,
    parse_detail_dialog_offset_rows,
    parse_detail_dialog_records,
    split_key,
)


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "detail_dialogoffset.dbss"
# Keyed (dialog key, text_id, 0, field); see the fields below.
_LOC_DIALOG = 39
_FIELD_GREETING = 0
_FIELD_OPTION_TITLE = 2
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 3


def _dialog_text(record: DialogRecord, text_id: int, field: int, has_loc: bool) -> str:
    """The user-language text of one dialog string with its PA tags, or "" without LOC."""
    if not has_loc:
        return ""
    text = loc_lookup(_LOC_DIALOG, record.key, text_id, 0, field).strip()
    return text if strip_pa_tags(text).strip() else ""


def _distinct_names(names: tuple[str, ...], values: list[int]) -> list[str]:
    """Enum names of `values` in first-seen order, each once."""
    return list(dict.fromkeys(enum_name(names, value) for value in values))


def _record_dict(record: DialogRecord, has_loc: bool) -> dict:
    leases = [option.lease for option in record.options]
    found = [lease for lease in leases if lease is not None]
    option_titles = [
        _dialog_text(record, option.text_id, _FIELD_OPTION_TITLE, has_loc) or option.title
        for option in record.options
    ]
    return {
        "key": record.key,
        "character_id": record.character_id,
        "dialog_index": record.dialog_index,
        # LOC first; the internal name stands in without it.
        "character": character_name(record.character_id) or record.internal_name,
        "internal_name": record.internal_name,
        # User language first, the Korean source as fallback.
        **pa_fields("greeting", _dialog_text(record, record.text_id, _FIELD_GREETING, has_loc) or record.greeting),
        "contents_types": _distinct_names(CONTENTS_TYPE_NAMES, [line.contents_type for line in record.lines]),
        "option_count": len(record.options),
        "dialog_button_types": _distinct_names(
            DIALOG_BUTTON_TYPE_NAMES, [option.dialog_button_type for option in record.options]
        ),
        **pa_list_fields("option_titles", option_titles),
        **pa_list_fields("leases", [lease_text_tagged(lease, has_loc) for lease in found]),
        "lease_item_ids": [lease.item_id for lease in found],
    }


def _dialog_offset_record(row: PabrOffsetRow) -> dict:
    character_id, dialog_index = split_key(row.entry_id)
    return {
        "key": row.entry_id,
        "character_id": character_id,
        "dialog_index": dialog_index,
        "dbss_offset": row.offset,
        "size": row.size,
    }


def _read_dialog_offsets(data: bytes) -> list[dict]:
    return [_dialog_offset_record(row) for row in parse_detail_dialog_offset_rows(data)]


def detail_dialog_offset_handler() -> OffsetTableHandler:
    """`detail_dialogoffset.dbss`, and `base_dialogoffset.dbss` with the same layout and keys."""
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_id", "characterId"),
            OffsetColumn("dialog_index", "dialog"),
            offset_column("dbss_offset", "dbssOffset"),
            size_column("size", "size"),
        ],
        _read_dialog_offsets,
    )


class DetailDialogHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["dialog"], "num", sort_key="dialog_index"),
            Column(cols["character"], sort_key="character"),
            Column(cols["greeting"], sort_key="greeting"),
            Column(cols["contentsTypes"]),
            Column(cols["options"], "num", sort_key="option_count"),
            Column(cols["dialogButtonTypes"]),
            Column(cols["optionTitles"]),
            Column(cols["leases"]),
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
        return [_record_dict(record, has_loc) for record in parse_detail_dialog_records(data, offset_raw)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        options = sum(r["option_count"] for r in records)
        characters = len({r["character_id"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), characters=characters, options=options)
        rows = [
            [
                e(r["character_id"]),
                e(r["dialog_index"]),
                e(r["character"] or _EMPTY),
                pa_line_cell(r, "greeting"),
                text_list_cell(r["contents_types"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                e(r["option_count"]),
                text_list_cell(r["dialog_button_types"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                pa_list_cell(r[pa_key("option_titles")], _LIST_PREVIEW_ITEMS),
                pa_list_cell(r[pa_key("leases")], _LIST_PREVIEW_ITEMS),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
