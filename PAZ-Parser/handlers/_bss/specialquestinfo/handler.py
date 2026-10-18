"""specialquestinfo.bss preview handler: each special quest group's quests."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.quest.quest import quest_title, split_packed_quest_id
from .parser import FILE_NAME, parse_specialquestinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_QUESTS = 8


def _quest_text(packed_quest_id: int) -> str:
    """`chain/quest title`, or `chain/quest` without a title.

    The steps of one chain often share a title, so the IDs tell them apart.
    """
    chain, quest = split_packed_quest_id(packed_quest_id)
    title = quest_title(chain, quest)
    return f"{chain}/{quest} {title}" if title else f"{chain}/{quest}"


class SpecialQuestInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["groupKey"], "num", sort_key="group_key"),
            Column(cols["questCount"], "num", sort_key="quest_count"),
            # A list column: it would only sort by its string form.
            Column(cols["quests"]),
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
            groups = parse_specialquestinfo_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        # Quest titles as text, so tab search and CSV export see them.
        return [
            {**group, "quests": [_quest_text(packed) for packed in group["packed_quest_ids"]]}
            for group in groups
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            quests=sum(record["quest_count"] for record in records),
        )
        rows = [
            [
                e(record["group_key"]),
                e(record["quest_count"]),
                text_list_cell(record["quests"], _LIST_PREVIEW_QUESTS) or _EMPTY,
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
