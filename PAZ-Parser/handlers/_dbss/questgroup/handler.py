from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from _common.quest.quest import quest_title
from .parser import parse_questgroup_records


_LANG_DIR = Path(__file__).parent / "lang"


def _join_limited(values: list[str], max_items: int = 8) -> str:
    if len(values) <= max_items:
        return ", ".join(values)
    return ", ".join(values[:max_items]) + f", ... (+{len(values) - max_items})"


def _group_name_en(group_id: int) -> str:
    return strip_pa_tags(loc_lookup(25, group_id)).strip()


class QuestGroupDbssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        has_loc = is_loc_loaded()

        for record in parse_questgroup_records(data):
            name_en = _group_name_en(record["group_id"]) if has_loc else ""
            quest_titles: list[str] = []
            for quest in record["quests"]:
                title = quest_title(quest["group_id"], quest["quest_no"]) if has_loc else ""
                quest_titles.append(title or f"{quest['group_id']}:{quest['quest_no']}")

            records.append({
                "row": record["row"],
                "offset": record["offset"],
                "size": record["size"],
                "group_id": record["group_id"],
                "name_kr": record["name_kr"],
                "name_en": name_en,
                "name": name_en or record["name_kr"],
                "quest_count": record["quest_count"],
                "quest_titles": quest_titles,
                "quest_titles_text": ", ".join(quest_titles),
            })

        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start:start + page_size]
        total_links = sum(r["quest_count"] for r in records)
        meta = f"{len(records):,} quest groups · {total_links:,} quest links"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("groupId", "Group ID"), "num", ""),
            (cols.get("name", "Name"), "", ""),
            (cols.get("quests", "Quests"), "num", ""),
            (cols.get("questTitles", "Quest Titles"), "", ""),
        ]
        rows = [
            [
                e(r["group_id"]),
                e(r["name"]),
                e(r["quest_count"]),
                e(_join_limited(r["quest_titles"])),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
