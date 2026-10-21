"""yachtnpcdiceinfo.bss preview handler: the NPCs a player can challenge to Yar!."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.yachthandrank.parser import FILE_NAME as HAND_RANK_FILE
from _bss.yachthandrank.text import HAND_RANKS_SHOWN, hand_rank_names, korean_hand_rank_names
from _common.character import character_name
from _common.html import Column, e, error, sort_keys, table, text_list_cell
from _common.knowledge import knowledge_name
from _common.lang import handler_text, load_handler_strings
from _dbss.yacht_common.text import keys_text
from _dbss.yachtdicepreset.parser import FILE_NAME as DICE_PRESET_FILE, dice_keys_by_preset
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
            # List columns: they would only sort by their string form.
            Column(cols["dice"]),
            Column(cols["handRanks"]),
            Column(cols["knowledgeKey"], "num", sort_key="knowledge_key"),
            Column(cols["knowledge"], sort_key="knowledge_name"),
            Column(cols["deckLimit"], "num", sort_key="deck_limit"),
            Column(cols["rollCountMax"], "num", sort_key="roll_count_max"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{HAND_RANK_FILE}", f"{folder}/{DICE_PRESET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            rows = parse_yachtnpcdiceinfo_records(data)
            korean_names = korean_hand_rank_names(companions.get(HAND_RANK_FILE))
            preset_dice = dice_keys_by_preset(companions.get(DICE_PRESET_FILE))
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **row,
                "npc_name": character_name(row["npc_key"]),
                "dice_text": keys_text(preset_dice.get(row["dice_preset_key"], [])),
                "hand_rank_names": hand_rank_names(row["hand_rank_keys"], korean_names),
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
                e(r["dice_text"] or _EMPTY),
                text_list_cell(r["hand_rank_names"], HAND_RANKS_SHOWN) or _EMPTY,
                e(r["knowledge_key"]),
                e(r["knowledge_name"] or _EMPTY),
                e(r["deck_limit"]),
                e(r["roll_count_max"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
