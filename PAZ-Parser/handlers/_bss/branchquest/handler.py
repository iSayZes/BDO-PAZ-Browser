"""branchquest.bss preview handler: the crossroad quest groups."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded
from _common.pa_text import pa_cell, pa_fields
from _common.quest.quest import quest_title_tagged
from .parser import FILE_NAME, parse_branchquest_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class BranchQuestBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["groupKey"], "num", sort_key="group_key"),
            Column(cols["mainId"], "num", sort_key="quest_chain_id"),
            Column(cols["subId"], "num", sort_key="quest_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["title"], sort_key="title"),
            Column(cols["role"], sort_key="is_root_quest"),
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
            records = parse_branchquest_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        has_loc = is_loc_loaded()
        # Role labels keyed by `is_root_quest`; a value the lang files lack shows as the number.
        roles: dict[str, str] = load_handler_strings(self.lang, _LANG_DIR)["roles"]
        rows: list[dict] = []
        for record in records:
            title = quest_title_tagged(record["quest_chain_id"], record["quest_id"]) if has_loc else ""
            rows.append({
                **record,
                **pa_fields("title", title),
                "role": roles.get(str(record["is_root_quest"]), str(record["is_root_quest"])),
                "icon_path": icon_path(IconKind.QUEST, record["packed_quest_id"]),
            })
        return rows

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        group_count = len({record["group"] for record in records})
        with_titles = sum(1 for record in records if record["title"])
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), group_count=group_count)
        if with_titles:
            meta += handler_text(self.lang, _LANG_DIR, "meta.withTitles", with_titles=with_titles)

        rows = [
            [
                e(record["group_key"]),
                e(record["quest_chain_id"]),
                e(record["quest_id"]),
                icon_cell(record["icon_path"]) if record["icon_path"] else _EMPTY,
                pa_cell(record, "title"),
                e(record["role"]),
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
