"""gameoption.bss preview handler: one row per named head field, then one per string."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.binary import whole_float
from _common.html import Column, e, error, sort_keys, table
from _common.item_key import item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.pabr_strings import string_at
from .parser import FILE_NAME, FieldValue, GameOption, parse_gameoption


_LANG_DIR = Path(__file__).parent / "lang"

# Head fields whose value names something: an item key, or a string-table index.
_ITEM_KEY_FIELDS = frozenset({"re_awakening_item_key"})
_STRING_REF_FIELDS = frozenset({"final_level_up_condition_ref"})


def _field_text(item: FieldValue, strings: tuple[str, ...]) -> str | None:
    """The item name or the string a head field points at, or None."""
    name = item.field.name
    if name in _ITEM_KEY_FIELDS and isinstance(item.value, int):
        return item_key_text(item.value)
    if name in _STRING_REF_FIELDS and isinstance(item.value, int):
        return string_at(list(strings), item.value)
    return None


def _records(option: GameOption) -> list[dict]:
    head = [
        {
            "offset": item.offset,
            "field": item.field.name,
            "value": whole_float(item.value) if isinstance(item.value, float) else item.value,
            "text": _field_text(item, option.strings),
        }
        for item in option.head
        if not item.field.is_unknown
    ]
    strings = [
        {"offset": None, "field": f"strings[{index}]", "value": text, "text": None}
        for index, text in enumerate(option.strings)
    ]
    return head + strings


def _offset_text(offset: int | None) -> str:
    return "-" if offset is None else f"0x{offset:04X}"


class GameOptionBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["offset"], "num", sort_key="offset"),
            Column(cols["field"], sort_key="field"),
            Column(cols["value"], sort_key="value"),
            Column(cols["text"], sort_key="text"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order: the head fields by offset, then the string table.
        return None

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            option = parse_gameoption(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        records = _records(option)
        if records:
            records[0] = {**records[0], "_body_size": option.body_size}
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                e(_offset_text(r["offset"])),
                e(r["field"]),
                e(r["value"]),
                e(r["text"] or "-"),
            ]
            for r in records[start : start + page_size]
        ]
        string_count = sum(1 for r in records if r["offset"] is None)
        body_size = next((r["_body_size"] for r in records if "_body_size" in r), 0)
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            fields=len(records) - string_count,
            strings=string_count,
            body=f"{body_size:,}",
        )
        return table(meta, self._columns(), rows)
