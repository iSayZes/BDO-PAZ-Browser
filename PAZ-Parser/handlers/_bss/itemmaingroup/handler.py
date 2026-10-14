"""itemmaingroup.bss preview handler: each group's subgroups and the items they list."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, html_list_cell, record_link, sort_keys, table
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.lookup_builders import ITEMSUBGROUP
from _dbss.itemsubgroup.parser import ItemSubgroup, parse_itemsubgroup_records
from .parser import ItemMainGroup, group_item_keys, parse_itemmaingroup_records

_LANG_DIR = Path(__file__).parent / "lang"
_SUBGROUP_FILE = "itemsubgroup.dbss"
_SUBGROUP_OFFSET_FILE = "itemsubgroupoffset.dbss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8
_SUBGROUP_SEPARATOR = "<br>"


class ItemMainGroupBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["groupId"], "num", sort_key="group_id"),
            Column(cols["subgroups"], sort_key="subgroups_text"),
            Column(cols["itemCount"], "num", sort_key="item_count"),
            # A list column: it would only sort by its string form.
            Column(cols["items"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_SUBGROUP_FILE}", f"{folder}/{_SUBGROUP_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        subgroup_raw = companions.get(_SUBGROUP_FILE)
        offset_raw = companions.get(_SUBGROUP_OFFSET_FILE)
        if subgroup_raw is None or offset_raw is None:
            return [{"_error": f"{_SUBGROUP_FILE} and {_SUBGROUP_OFFSET_FILE} are required"}]

        try:
            groups = parse_itemmaingroup_records(data)
            subgroups = {
                subgroup.subgroup_key: subgroup
                for subgroup in parse_itemsubgroup_records(subgroup_raw, offset_raw)
            }
        except ValueError as ex:
            return [{"_error": f"itemmaingroup.bss could not be parsed: {ex}"}]

        return [_record_fields(group, subgroups) for group in groups]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        entries = sum(len(record["subgroup_keys"]) for record in records)
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), entries=entries)
        rows = [
            [
                e(record["group_id"]),
                _subgroups_cell(record["subgroup_keys"], record["conditions"]),
                e(record["item_count"]),
                item_key_list_cell(record["item_keys"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)


def _record_fields(group: ItemMainGroup, subgroups: dict[int, ItemSubgroup]) -> dict:
    item_keys = group_item_keys(group, subgroups)
    conditions = [entry.condition for entry in group.entries]
    return {
        "group_id": group.group_id,
        "subgroup_keys": list(group.subgroup_keys),
        "conditions": conditions,
        # Subgroups and conditions as text, so tab search, sorting and CSV export see them.
        "subgroups_text": "; ".join(
            _subgroup_text(key, condition) for key, condition in zip(group.subgroup_keys, conditions)
        ),
        "item_count": len(item_keys),
        "item_keys": item_keys,
        "items": [item_key_text(key) for key in item_keys],
    }


def _subgroup_text(subgroup_key: int, condition: str) -> str:
    return f"{subgroup_key}: {condition}" if condition else str(subgroup_key)


def _subgroups_cell(subgroup_keys: list[int], conditions: list[str]) -> str:
    """Each subgroup as a link to its `itemsubgroup.dbss` row, followed by its condition."""
    entries = [
        record_link(str(key), ITEMSUBGROUP, "subgroup_key", key, "record-link")
        + (f": {e(condition)}" if condition else "")
        for key, condition in zip(subgroup_keys, conditions)
    ]
    return html_list_cell(entries, separator=_SUBGROUP_SEPARATOR) or _EMPTY

