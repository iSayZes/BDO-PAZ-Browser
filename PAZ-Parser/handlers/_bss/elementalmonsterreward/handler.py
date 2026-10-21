"""elementalmonsterreward.bss preview handler: one row per rank tier and base reward row of each boss."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.elementalmonsterstat.parser import FILE_NAME as STAT_FILE, boss_difficulties
from _bss.elementalmonsterstat.text import difficulty_label, part_label
from _common.character import character_name
from _common.html import Column, e, error, flag_cell, record_link, sort_keys, table
from _common.item_key import item_count_list_cell, item_count_text
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_elementalmonsterreward
from .text import base_reward_label, rank_label


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = ", "
_STAT_PATH = f"gamecommondata/binary/{STAT_FILE}"
_LINK_CLASS = "record-link"


def _boss_key_cell(character_key: int, has_stat_row: bool) -> str:
    """The key as a link to its `elementalmonsterstat.bss` row, or plain text without one."""
    if not has_stat_row:
        return e(character_key)
    return record_link(str(character_key), _STAT_PATH, "character_key", character_key, _LINK_CLASS)


def _reward_items(rewards: list[dict]) -> list[tuple[int, int]]:
    return [(item["item_key"], item["count"]) for item in rewards]


class ElementalMonsterRewardBssHandler(PreviewHandler):
    def _strings(self) -> dict:
        return load_handler_strings(self.lang, _LANG_DIR)

    def _columns(self) -> list[Column]:
        cols = self._strings()["columns"]
        return [
            Column(cols["bossKey"], "num", sort_key="character_key"),
            Column(cols["boss"], sort_key="name"),
            Column(cols["part"], sort_key="part"),
            Column(cols["difficulty"], sort_key="level"),
            Column(cols["partyRanking"], sort_key="is_part2"),
            Column(cols["rank"], sort_key="rank"),
            Column(cols["rewards"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{STAT_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            tables = parse_elementalmonsterreward(data)
            stat_raw = companions.get(STAT_FILE)
            difficulties = boss_difficulties(stat_raw) if stat_raw is not None else None
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        rows: list[dict] = []
        for is_part2, records in ((False, tables.records), (True, tables.part2_records)):
            for record in records:
                rows.extend(self._tier_rows(record, is_part2, difficulties))
        return rows

    def _tier_rows(
        self,
        record: dict,
        is_part2: bool,
        difficulties: dict[int, tuple[int, int]] | None,
    ) -> list[dict]:
        """The rank tiers of one boss, then its base rewards when it has any."""
        key = record["character_key"]
        boss = self._boss_fields(key, is_part2, difficulties)
        rank_format = self._strings()["ranks"]["rank"]
        rows: list[dict] = []
        previous_rank: int | None = None
        for tier in record["rank_tiers"]:
            rows.append(self._row_record(
                boss, tier["rank"], rank_label(tier["rank"], previous_rank, rank_format), tier["rewards"],
            ))
            previous_rank = tier["rank"]
        if record["base_rewards"] or not record["rank_tiers"]:
            label = base_reward_label() or self._strings()["ranks"]["base"]
            rows.append(self._row_record(boss, None, label, record["base_rewards"]))
        return rows

    def _boss_fields(
        self,
        key: int,
        is_part2: bool,
        difficulties: dict[int, tuple[int, int]] | None,
    ) -> dict:
        difficulty = difficulties.get(key) if difficulties is not None else None
        return {
            "character_key": key,
            "name": character_name(key),
            "is_part2": is_part2,
            "has_stat_row": difficulties is None or difficulty is not None,
            "part": part_label(self.lang, difficulty[0]) if difficulty else None,
            "level": difficulty[1] if difficulty else None,
            "difficulty": difficulty_label(self.lang, *difficulty) if difficulty else None,
        }

    @staticmethod
    def _row_record(boss: dict, rank: int | None, label: str, rewards: list[dict]) -> dict:
        return {
            **boss,
            "rank": rank,
            "rank_label": label,
            "rewards": rewards,
            "rewards_text": _LIST_SEPARATOR.join(
                item_count_text(key, count) for key, count in _reward_items(rewards)
            ),
        }

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
                _boss_key_cell(r["character_key"], r["has_stat_row"]),
                e(r["name"] or _EMPTY),
                e(r["part"] or _EMPTY),
                e(r["difficulty"] or _EMPTY),
                flag_cell(r["is_part2"]),
                e(r["rank_label"]),
                item_count_list_cell(_reward_items(r["rewards"])) if r["rewards"] else _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            bosses=len({r["character_key"] for r in records}),
        )
        return table(meta, self._columns(), rows)
