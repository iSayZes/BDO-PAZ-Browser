from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _bss.jewelgroupstaticstatus.names import jewel_group_name
from _bss.jewelgroupstaticstatus.parser import FILE_NAME as GROUP_FILE
from _bss.jewelgroupstaticstatus.parser import parse_jewel_group_records
from .parser import parse_special_slot_records
from .slots import special_slot_label


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8


def _group_names(group_data: bytes | None) -> dict[int, str]:
    """Group number -> its name; empty without `jewelgroupstaticstatus.bss`."""
    if group_data is None:
        return {}
    return {
        group["group"]: jewel_group_name(group["group"], group["max_count"], group["name_kr"])
        for group in parse_jewel_group_records(group_data)
    }


def _group_label(group: int, names: dict[int, str]) -> str:
    """`103 Dawn`, or the number alone when the group has no name."""
    name = names.get(group, "")
    return f"{group} {name}" if name else str(group)


class JewelSpecialSlotsGroupStaticStatusBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["slot"], "num", sort_key="slot"),
            Column(cols["equipment"], sort_key="equipment"),
            # A list column: it would only sort by its string form.
            Column(cols["groups"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{GROUP_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        # Without the group table the groups show as numbers.
        names = _group_names(companions.get(GROUP_FILE))
        return [
            {
                **row,
                "equipment": special_slot_label(row["slot"]),
                "group_labels": [_group_label(group, names) for group in row["groups"]],
            }
            for row in parse_special_slot_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        rows = [
            [
                e(r["slot"]),
                e(r["equipment"] or _EMPTY),
                text_list_cell(r["group_labels"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
