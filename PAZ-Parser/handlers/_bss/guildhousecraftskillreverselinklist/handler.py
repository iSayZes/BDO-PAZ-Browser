"""guildhousecraftskillreverselinklist.bss preview handler: the house uses that grant each guild skill."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, html_list_cell, icon_label_cell, record_link, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.lookup_builders import SKILL
from _common.skill import skill_name
from _dbss.guildhousecraftskill.labels import GUILD_HOUSE_CRAFT_SKILL, house_use_label
from .parser import FILE_NAME, parse_reverse_link_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINK_CLASS = "record-link"


def _with_display_fields(record: dict) -> dict:
    """The record with its skill name and its house uses as text."""
    house_uses = [house_use_label(link["receipe_key"]) for link in record["links"]]
    return {
        **record,
        "skill_name": skill_name(record["skill_no"]) or None,
        "house_uses": house_uses,
        "house_uses_text": ", ".join(house_uses) or None,
    }


def _house_uses_cell(record: dict) -> str:
    """Each house use, linked to its `guildhousecraftskill.dbss` row."""
    links = [
        record_link(label, GUILD_HOUSE_CRAFT_SKILL, "receipe_key", link["receipe_key"], _LINK_CLASS)
        for label, link in zip(record["house_uses"], record["links"])
    ]
    return html_list_cell(links) or _EMPTY


def _slots_cell(record: dict) -> str:
    return e(", ".join(str(link["slot"]) for link in record["links"])) or _EMPTY


class GuildHouseCraftSkillReverseLinkListBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["skill"], sort_key="skill_name"),
            Column(cols["linkCount"], "num", sort_key="link_count"),
            Column(cols["houseUses"], sort_key="house_uses_text"),
            # A list column: it would only sort by its string form.
            Column(cols["slots"]),
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
            records = parse_reverse_link_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [_with_display_fields(record) for record in records]

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
                record_link(str(r["skill_no"]), SKILL, "skill_no", r["skill_no"], _LINK_CLASS),
                icon_label_cell(icon_path(IconKind.SKILL, r["skill_no"]), r["skill_name"] or _EMPTY),
                e(r["link_count"]),
                _house_uses_cell(r),
                _slots_cell(r),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            links=sum(r["link_count"] for r in records),
        )
        return table(meta, self._columns(), rows)
