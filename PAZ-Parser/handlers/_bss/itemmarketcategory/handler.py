"""itemmarketcategory.bss preview handler: the Central Market category tree."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_lookup, strip_pa_tags
from .parser import FILE_NAME, LIST_FIELDS, parse_itemmarketcategory_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 12

# Category names, keyed (main category, sub-category, filter 1, filter 2)
# with 0 for the parts an entry does not have; LIST_FIELDS is in that order.
_LOC_MARKET_CATEGORY = 44


def _category_name(main_no: int, value: dict, list_field: str | None) -> str:
    """The LOC name of a main category (`list_field` None) or a list entry, else its Korean name."""
    parts = [0] * len(LIST_FIELDS)
    if list_field is not None:
        parts[LIST_FIELDS.index(list_field)] = value["category_no"]
    text = strip_pa_tags(loc_lookup(_LOC_MARKET_CATEGORY, main_no, *parts)).strip()
    return text or value["name_kr"]


def _entry_text(value: dict) -> str:
    """`Longsword (1)`: the name and the category number the market sends to the server."""
    return f"{value['name']} ({value['category_no']})"


def _named(main_no: int, values: list[dict], list_field: str) -> list[dict]:
    return [{**value, "name": _category_name(main_no, value, list_field)} for value in values]


class ItemMarketCategoryBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["name"], sort_key="name"),
            # List columns: they would only sort by their string form.
            Column(cols["subCategories"]),
            Column(cols["filter1"]),
            Column(cols["filter2"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_itemmarketcategory_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        named: list[dict] = []
        for record in records:
            main = record["main_category"]
            main_no = main["category_no"]
            named.append({
                **record,
                "name": _category_name(main_no, main, None),
                **{field: _named(main_no, record[field], field) for field in LIST_FIELDS},
            })
        return named

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["key"]),
                e(r["name"]),
                *(
                    text_list_cell([_entry_text(value) for value in r[field]], _LIST_PREVIEW_ITEMS) or _EMPTY
                    for field in LIST_FIELDS
                ),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
