"""gameoption.bss preview handler: one row per named head and run field, then one per string."""
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
from .runs import RunValue


_LANG_DIR = Path(__file__).parent / "lang"

# The head is the first columns of this sheet's loader.
HEAD_SHEET = "BattleOption"

# Head fields whose value names something: an item key, or a string-table index.
_HEAD_KINDS = {"re_awakening_item_key": "item", "final_level_up_condition_ref": "string"}

# A cheer buff is stored as `buff_key << 16 | 1`.
_BUFF_KEY_SHIFT = 16

_Value = int | float | bytes | tuple


def _value_text(kind: str, value: _Value, strings: tuple[str, ...]) -> str | None:
    """The item names, string or buff keys a field's value points at, or None."""
    if kind == "item" and isinstance(value, int):
        return item_key_text(value)
    if kind == "items" and isinstance(value, tuple):
        return ", ".join(item_key_text(key) for key in value) or None
    if kind == "string" and isinstance(value, int):
        return string_at(list(strings), value)
    if kind == "buffs" and isinstance(value, tuple):
        return ", ".join(str(packed >> _BUFF_KEY_SHIFT) for packed in value)
    return None


def _shown_value(value: _Value) -> int | float | str:
    """A number as read, a whole float as an int, an array as comma-joined numbers."""
    if isinstance(value, float):
        return whole_float(value)
    if isinstance(value, tuple):
        return ", ".join(str(_shown_value(v)) for v in value)
    if isinstance(value, bytes):
        return value.hex(" ")
    return value


def _head_record(item: FieldValue, strings: tuple[str, ...]) -> dict:
    return {
        "offset": item.offset,
        "sheet": HEAD_SHEET,
        "field": item.field.name,
        "value": _shown_value(item.value),
        "text": _value_text(_HEAD_KINDS.get(item.field.name, ""), item.value, strings),
    }


def _run_record(item: RunValue, strings: tuple[str, ...]) -> dict:
    return {
        "offset": item.offset,
        "sheet": item.sheet,
        "field": item.field.name,
        "value": _shown_value(item.value),
        "text": _value_text(item.field.kind, item.value, strings),
    }


def _records(option: GameOption) -> list[dict]:
    head = [_head_record(item, option.strings) for item in option.head if not item.field.is_unknown]
    runs = [_run_record(item, option.strings) for item in option.runs if item.field.is_shown]
    strings = [
        {"offset": None, "sheet": None, "field": f"strings[{index}]", "value": text, "text": None}
        for index, text in enumerate(option.strings)
    ]
    return head + runs + strings


def _offset_text(offset: int | None) -> str:
    return "-" if offset is None else f"0x{offset:04X}"


class GameOptionBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["offset"], "num", sort_key="offset"),
            Column(cols["sheet"], sort_key="sheet"),
            Column(cols["field"], sort_key="field"),
            Column(cols["value"], sort_key="value"),
            Column(cols["text"], sort_key="text"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # File order: the head and run fields by offset, then the string table.
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
            records[0] = {
                **records[0],
                "_undecoded_size": option.undecoded_size,
                "_body_error": option.body_error,
            }
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
                e(r["sheet"] or "-"),
                e(r["field"]),
                e(r["value"]),
                e(r["text"] or "-"),
            ]
            for r in records[start : start + page_size]
        ]
        return table(self._meta(records), self._columns(), rows)

    def _meta(self, records: list[dict]) -> str:
        string_count = sum(1 for r in records if r["offset"] is None)
        first = records[0] if records else {}
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            fields=len(records) - string_count,
            strings=string_count,
            body=first.get("_undecoded_size", 0),
        )
        if first.get("_body_error"):
            meta += " " + handler_text(self.lang, _LANG_DIR, "meta.body_error", reason=first["_body_error"])
        return meta
