"""yachtnpcdiceinfo.bss preview handler: the NPCs a player can challenge to Yar!."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, error, sort_keys, table
from _common.knowledge import knowledge_name
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_yachtnpcdiceinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class YachtNpcDiceInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="npc_dice_info_key"),
            Column(cols["npcKey"], "num", sort_key="npc_key"),
            Column(cols["npc"], sort_key="npc_name"),
            Column(cols["dicePreset"], "num", sort_key="dice_preset_key"),
            # A list column: it would only sort by its string form.
            Column(cols["handRanks"]),
            Column(cols["knowledgeKey"], "num", sort_key="knowledge_key"),
            Column(cols["knowledge"], sort_key="knowledge_name"),
            Column(cols["deckLimit"], "num", sort_key="deck_limit"),
            Column(cols["rollCountMax"], "num", sort_key="roll_count_max"),
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
            rows = parse_yachtnpcdiceinfo_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **row,
                "npc_name": character_name(row["npc_key"]),
                "knowledge_name": knowledge_name(row["knowledge_key"]),
            }
            for row in rows
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
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["npc_dice_info_key"]),
                e(r["npc_key"]),
                e(r["npc_name"] or _EMPTY),
                e(r["dice_preset_key"]),
                e(", ".join(str(key) for key in r["hand_rank_keys"]) or _EMPTY),
                e(r["knowledge_key"]),
                e(r["knowledge_name"] or _EMPTY),
                e(r["deck_limit"]),
                e(r["roll_count_max"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
