"""journalinfostaticstatus.bss preview handler: each main quest board card with its quest chain and texts."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry
from table_sort import TableSort

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, KeyHashes, ui_key_hashes, ui_key_text
from _common.html import Column, e, sprite_icon_cell, text_list_cell, truncate
from _common.quest.quest import quest_title
from _common.row_table import RowTableHandler
from _common.texture_string import TEXTURE_STRING_COMBINE, TEXTURE_STRING_COMBINE_PATH, icon_fields, parse_texture_regions
from .parser import FILE_NAME, parse_journalinfostaticstatus


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MAX_BOOK_QUESTS = 2
_STORY_PREVIEW_CHARS = 120


def _key_text(hashes: KeyHashes, key: str) -> str:
    """LOC text of a `GAME` sheet key, the key itself without one, '' for no key."""
    if not key:
        return ""
    return ui_key_text(hashes, GAME_SHEET, key) or key


def _book_quest_text(book_quest: dict) -> str:
    """`8700-1 Title`, or the bare quest number without a LOC title."""
    group, quest = book_quest["book_quest_group"], book_quest["book_quest_id"]
    return f"{group}-{quest} {quest_title(group, quest)}".strip()


def _card_order(record: dict) -> tuple[int, ...]:
    return (
        record["journal_list_index"], record["chapter_index"], record["ui_type_index"], record["journal_index"],
    )


class JournalInfoHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["journalList"], "num", sort_key="journal_list_index"),
            Column(labels["chapter"], "num", sort_key="chapter_index"),
            Column(labels["page"], "num", sort_key="ui_type_index"),
            Column(labels["card"], "num", sort_key="journal_index"),
            Column(labels["texture"], sort_key="texture_normal"),
            Column(labels["questChain"], "num", sort_key="quest_group_no"),
            Column(labels["chapterName"], sort_key="chapter_text"),
            Column(labels["title"], sort_key="title_text"),
            Column(labels["story"], sort_key="scenario_text"),
            Column(labels["bookQuests"], sort_key="book_quests_text"),
        ]

    def default_sort(self) -> TableSort | None:
        # read_records() orders by list, chapter, page and card; no one column gives that.
        return None

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{STRINGTABLE_FILE}", TEXTURE_STRING_COMBINE_PATH]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        journals, _ = parse_journalinfostaticstatus(data)
        hashes = ui_key_hashes(companions.get(STRINGTABLE_FILE), [GAME_SHEET])
        textures = parse_texture_regions(companions.get(TEXTURE_STRING_COMBINE), (j["texture_normal"] for j in journals))
        records = []
        for journal in journals:
            book_quests = [_book_quest_text(book_quest) for book_quest in journal["book_quests"]]
            records.append(
                {
                    **journal,
                    "chapter_text": _key_text(hashes, journal["chapter_string"]),
                    "title_text": _key_text(hashes, journal["title_string"]),
                    "scenario_text": " ".join(_key_text(hashes, journal["scenario_desc"]).split()),
                    "book_quest_texts": book_quests,
                    "book_quests_text": ", ".join(book_quests),
                    **icon_fields(textures, journal["texture_normal"]),
                }
            )
        return sorted(records, key=_card_order)

    def cells(self, record: dict) -> list[str]:
        texture = (
            sprite_icon_cell(record["icon_path"], record["icon_region"]) if record["icon_path"] else e(record["texture_normal"])
        )
        return [
            e(record["journal_list_index"]),
            e(record["chapter_index"]),
            e(record["ui_type_index"]),
            e(record["journal_index"]),
            texture or _EMPTY,
            e(record["quest_group_no"]),
            e(record["chapter_text"]) or _EMPTY,
            e(record["title_text"]) or _EMPTY,
            e(truncate(record["scenario_text"], _STORY_PREVIEW_CHARS)) or _EMPTY,
            text_list_cell(record["book_quest_texts"], _MAX_BOOK_QUESTS) or _EMPTY,
        ]
