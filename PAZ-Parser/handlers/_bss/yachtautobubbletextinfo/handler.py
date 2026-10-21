"""yachtautobubbletextinfo.bss preview handler: what the player and each Yar! opponent say during a match."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.yachthandrank.parser import FILE_NAME as HAND_RANK_FILE
from _bss.yachthandrank.text import hand_rank_name, korean_hand_rank_names
from _common.character import character_name
from _common.html import Column, e, error, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_text
from .parser import FILE_NAME, PC_GROUP, TEXT_SLOTS, parse_yachtautobubbletextinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# LOC type 112 holds each line under the row key, `str_id4` = slot.
_LOC_BUBBLE_TEXT = 112
_LINE_SEPARATOR = "<br>"


def _lines(record: dict) -> list[str]:
    """The row's lines in slot order: each slot's LOC text, else its Korean text; empty slots left out."""
    return [
        loc_text(_LOC_BUBBLE_TEXT, record["bubble_text_key"], slot) or text_kr
        for slot, text_kr in enumerate(record["texts_kr"])
        if text_kr
    ]


class YachtAutoBubbleTextInfoHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="bubble_text_key"),
            Column(cols["npcKey"], "num", sort_key="npc_key"),
            Column(cols["speaker"], sort_key="speaker"),
            Column(cols["condition"], sort_key="condition_name"),
            Column(cols["handRankKey"], "num", sort_key="hand_rank_key_shown"),
            Column(cols["handRank"], sort_key="hand_rank_name"),
            # A list column: it would only sort by its string form.
            Column(cols["lines"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{HAND_RANK_FILE}"]

    @staticmethod
    def _condition_name(condition: int, names: dict[str, str]) -> str | None:
        """The trigger's name, the bare value for one without a name, or None for `0` (a hand rank row)."""
        if not condition:
            return None
        return names.get(str(condition), str(condition))

    def _display_record(self, record: dict, korean_names: dict[int, str]) -> dict:
        strings = load_handler_strings(self.lang, _LANG_DIR)
        hand_rank_key = record["hand_rank_key"] or None
        is_player = record["group"] == PC_GROUP
        return {
            **record,
            "npc_key": None if is_player else record["character_key"],
            "speaker": strings["player"] if is_player else character_name(record["character_key"]),
            "condition_name": self._condition_name(record["condition"], strings["conditions"]),
            "hand_rank_key_shown": hand_rank_key,
            "hand_rank_name": (
                hand_rank_name(hand_rank_key, korean_names.get(hand_rank_key, "")) if hand_rank_key else None
            ),
            "lines": _lines(record),
        }

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_yachtautobubbletextinfo_records(data)
            korean_names = korean_hand_rank_names(companions.get(HAND_RANK_FILE))
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [self._display_record(record, korean_names) for record in records]

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
                e(r["bubble_text_key"]),
                e(_EMPTY if r["npc_key"] is None else r["npc_key"]),
                e(r["speaker"] or _EMPTY),
                e(r["condition_name"] or _EMPTY),
                e(_EMPTY if r["hand_rank_key_shown"] is None else r["hand_rank_key_shown"]),
                e(r["hand_rank_name"] or _EMPTY),
                text_list_cell(r["lines"], TEXT_SLOTS, _LINE_SEPARATOR) or _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
