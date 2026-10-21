"""yachtgameboardinfo.bss preview handler: the game boards (modes) of a Yar! match between two players."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.yachthandrank.parser import FILE_NAME as HAND_RANK_FILE
from _bss.yachthandrank.text import HAND_RANKS_SHOWN, hand_rank_names, korean_hand_rank_names
from _common.html import Column, e, error, flag_cell, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_text
from .parser import FILE_NAME, parse_yachtgameboardinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# LOC type 109 holds each board's description under its key.
_LOC_GAME_BOARD_DESC = 109


class YachtGameBoardInfoHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="game_board_key"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["description"], sort_key="desc"),
            Column(cols["handRankCount"], "num", sort_key="hand_rank_count"),
            # A list column: it would only sort by its string form.
            Column(cols["handRanks"]),
            Column(cols["rollCountMax"], "num", sort_key="roll_count_max"),
            Column(cols["matchmaking"], sort_key="is_use_matching"),
            Column(cols["iconTexture"], sort_key="icon_texture"),
            Column(cols["bigTexture"], sort_key="big_texture"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{HAND_RANK_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_yachtgameboardinfo_records(data)
            korean_names = korean_hand_rank_names(companions.get(HAND_RANK_FILE))
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "desc": loc_text(_LOC_GAME_BOARD_DESC, record["game_board_key"]) or record["desc_kr"],
                "hand_rank_names": hand_rank_names(record["hand_rank_keys"], korean_names),
            }
            for record in records
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
        rows = [
            [
                e(r["game_board_key"]),
                e(r["level"]),
                e(r["desc"] or _EMPTY),
                e(r["hand_rank_count"]),
                text_list_cell(r["hand_rank_names"], HAND_RANKS_SHOWN) or _EMPTY,
                e(r["roll_count_max"]),
                flag_cell(bool(r["is_use_matching"])),
                e(r["icon_texture"] or _EMPTY),
                e(r["big_texture"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
