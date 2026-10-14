from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields
from _common.quest.dialog import dialog_cell, dialog_key, dialog_name
from _common.quest.quest import quest_title_tagged
from .parser import QuestNpcRecord, parse_quest_npc_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _display_record(record: QuestNpcRecord) -> dict:
    """The parsed row with its LOC text; no NPC shows as an empty NPC cell.

    Rows without an NPC keep their dialog: key `0` (NPC 0, dialog 0) is the
    Black Spirit's dialog, which LOC names, and key `65536` (dialog 1) is a
    `detail_dialog.dbss` record without a name.
    """
    npc_id = record["npc_id"] or None
    return {
        **record,
        **pa_fields("title", quest_title_tagged(record["quest_chain_id"], record["quest_id"])),
        "npc_id": npc_id,
        "npc_name": character_name(npc_id) if npc_id else "",
        "dialog_name": dialog_name(record["npc_id"], record["dialog_index"]),
        "dialog_key": dialog_key(record["npc_id"], record["dialog_index"]),
    }


class QuestNpcBssHandler(PreviewHandler):
    """One handler for both files; `file_name` only names the file in errors."""

    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["questId"], "num", sort_key="packed_quest_id"),
            Column(cols["mainId"], "num", sort_key="quest_chain_id"),
            Column(cols["subId"], "num", sort_key="quest_id"),
            Column(cols["title"], sort_key="title"),
            Column(cols["npcId"], "num", sort_key="npc_id"),
            Column(cols["npcName"], sort_key="npc_name"),
            Column(cols["dialog"], "num", sort_key="dialog_index"),
            Column(cols["dialogName"], sort_key="dialog_name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [_display_record(record) for record in parse_quest_npc_records(data, self._file_name)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        npc_count = len({r["npc_id"] for r in records if r["npc_id"]})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), npc_count=npc_count)
        rows = [
            [
                e(r["packed_quest_id"]),
                e(r["quest_chain_id"]),
                e(r["quest_id"]),
                pa_cell(r, "title"),
                e(r["npc_id"] or _EMPTY),
                e(r["npc_name"] or _EMPTY),
                dialog_cell(r["dialog_key"], str(r["dialog_index"])),
                e(r["dialog_name"] or _EMPTY),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
