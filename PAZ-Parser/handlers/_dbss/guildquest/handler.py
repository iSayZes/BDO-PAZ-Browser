"""guildquest.dbss preview handler: the guild missions with their objective, fee and rewards."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.contents_group import contents_groups_text
from _common.html import Column, e, error, flag_cell, html_list_cell, icon_cell, icon_html_label_cell, sort_keys, table
from _common.item_key import item_key_icon_path, item_key_text, item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields, pa_html, pa_line_cell
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import FILE_NAME, parse_guildquest_records
from .text import LOC_DESCRIPTION, LOC_OBJECTIVE, LOC_TITLE, guild_quest_tagged, guild_quest_type_name


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# gc::RewardType eRewardItem: the only reward type the guild missions use.
_REWARD_ITEM = 3


def guild_quest_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("quest_no", "questNo"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "quest_no", "data_offset", "data_size"),
    )


class GuildQuestHandler(PreviewHandler):
    def _strings(self) -> dict:
        return load_handler_strings(self.lang, _LANG_DIR)

    def _columns(self) -> list[Column]:
        cols = self._strings()["columns"]
        return [
            Column(cols["questNo"], "num", sort_key="quest_no"),
            Column(cols["title"], sort_key="title"),
            Column(cols["type"], sort_key="guild_quest_type_name"),
            Column(cols["objective"], sort_key="objective"),
            Column(cols["condition"], sort_key="complete_condition"),
            Column(cols["questLevel"], "num", sort_key="quest_level"),
            Column(cols["description"], sort_key="description"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["limitMinute"], "num", sort_key="limit_minute"),
            Column(cols["needItem"], sort_key="need_item_count"),
            Column(cols["isPreoccupancy"], sort_key="is_preoccupancy"),
            # A list column: it would only sort by its string form.
            Column(cols["rewards"]),
            Column(cols["contentsGroups"], sort_key="contents_groups"),
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
            records = parse_guildquest_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [self._record_fields(record) for record in records]

    def _reward_text(self, reward: dict) -> str:
        """`Silver x220,000,000`, or the reward type for a reward that is no item."""
        if reward["reward_type"] != _REWARD_ITEM:
            return handler_text(self.lang, _LANG_DIR, "reward.type", type=reward["reward_type"])
        return f"{item_key_text(reward['item_key'])} x{reward['item_count']:,}"

    def _record_fields(self, record: dict) -> dict:
        quest_no = record["quest_no"]
        return {
            **record,
            **pa_fields("title", guild_quest_tagged(quest_no, LOC_TITLE, record["title_kr"])),
            **pa_fields("objective", guild_quest_tagged(quest_no, LOC_OBJECTIVE, record["complete_condition_text_kr"])),
            **pa_fields("description", guild_quest_tagged(quest_no, LOC_DESCRIPTION, record["description_kr"])),
            "guild_quest_type_name": guild_quest_type_name(record["guild_quest_type"]),
            "need_item": f"{item_key_text(record['need_item_key'])} x{record['need_item_count']:,}",
            # Text forms, so tab search and CSV export see them.
            "rewards": [self._reward_text(reward) for reward in record["base_rewards"]],
            "contents_groups": contents_groups_text(record["contents_group_hashes"]),
        }

    def _reward_cell(self, reward: dict, text: str) -> str:
        """An item reward with its icon and grade colour, then its count."""
        if reward["reward_type"] != _REWARD_ITEM:
            return e(text)
        label = f"{pa_html(item_key_text_tagged(reward['item_key']))} x{reward['item_count']:,}"
        return icon_html_label_cell(item_key_icon_path(reward["item_key"]), label)

    def _rewards_cell(self, record: dict) -> str:
        cells = [self._reward_cell(reward, text) for reward, text in zip(record["base_rewards"], record["rewards"])]
        return html_list_cell(cells) or _EMPTY

    def _row(self, r: dict) -> list[str]:
        need_item = f"{pa_html(item_key_text_tagged(r['need_item_key']))} x{r['need_item_count']:,}"
        return [
            e(r["quest_no"]),
            pa_cell(r, "title"),
            e(r["guild_quest_type_name"]),
            pa_cell(r, "objective"),
            e(r["complete_condition"]) or _EMPTY,
            e(r["quest_level"]),
            pa_line_cell(r, "description"),
            icon_cell(r["icon_path"]),
            e(f"{r['limit_minute']:,}"),
            icon_html_label_cell(item_key_icon_path(r["need_item_key"]), need_item),
            flag_cell(bool(r["is_preoccupancy"])),
            self._rewards_cell(r),
            e(r["contents_groups"]) or _EMPTY,
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
        rows = [self._row(r) for r in records[start : start + page_size]]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
