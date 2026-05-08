from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from .parser import parse_mentaltheme_records, parse_mentalthemeoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


def _reward(amount: int, need_count: int) -> str:
    if amount == 0 and need_count == 0:
        return "—"
    return f"+{amount} at {need_count} entries"


def _reward_2(
    amount_1: int,
    need_count_1: int,
    amount_2: int,
    need_count_2: int,
) -> str:
    if amount_1 == amount_2 and need_count_1 == need_count_2:
        return "—"
    return _reward(amount_2, need_count_2)


class MentalThemeOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_mentalthemeoffset_records(data)
        return [
            {
                "theme_id": record["theme_id"],
                "payload_offset": record["payload_offset"],
                "payload_size": record["payload_size"],
            }
            for record in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} offset records"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("themeId", "Theme ID"), "num", ""),
            (cols.get("payloadOffset", "Payload Offset"), "num", ""),
            (cols.get("payloadSize", "Payload Size"), "num", ""),
        ]
        rows = [
            [
                e(r["theme_id"]),
                e(f"0x{r['payload_offset']:08X}"),
                e(r["payload_size"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)


class MentalThemeHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/mentalthemeoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("mentalthemeoffset.dbss")
        if offset_raw is None:
            raise ValueError("mentalthemeoffset.dbss companion not found.")

        records = parse_mentaltheme_records(data, offset_raw)
        return [
            {
                "theme_id": record["theme_id"],
                "name": record["name"],
                "parent_id": record["parent_id"] or "",
                "parent_name": record["parent_name"],
                "energy_reward_1": _reward(record["increase_wp"], record["need_count"]),
                "energy_reward_2": _reward_2(
                    record["increase_wp"],
                    record["need_count"],
                    record["increase_wp_2"],
                    record["need_count_2"],
                ),
                "energy_reward_1_amount": record["increase_wp"],
                "energy_reward_1_entries": record["need_count"],
                "energy_reward_2_amount": record["increase_wp_2"],
                "energy_reward_2_entries": record["need_count_2"],
                "entry_count": record["entry_count"],
                "child_count": record["child_count"],
                "name_ko": record["name_ko"],
                "entry_ids": record["entry_ids"],
                "entry_names": record["entry_names"],
                "child_ids": record["child_ids"],
                "payload_offset": record["payload_offset"],
                "payload_size": record["payload_size"],
                "unknown_flag": record["unknown_flag"],
                "unknown_value": record["unknown_value"],
                "terminator": record["terminator"],
            }
            for record in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]

        with_theme_name = sum(1 for r in records if r["name"])
        with_parent_name = sum(1 for r in records if r["parent_name"])
        meta = (
            f"{len(records):,} mentaltheme records"
            f" · {with_theme_name:,} theme names · {with_parent_name:,} parent names"
        )
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("themeId", "Theme ID"), "num", ""),
            (cols.get("name", "Name"), "", ""),
            (cols.get("parentId", "Parent ID"), "num", ""),
            (cols.get("parentName", "Parent Name"), "", ""),
            (cols.get("energyReward1", "Energy Reward 1"), "", ""),
            (cols.get("energyReward2", "Energy Reward 2"), "", ""),
            (cols.get("entries", "Entries"), "num", ""),
            (cols.get("childrenGroups", "Children Groups"), "num", ""),
        ]

        rows = [
            [
                e(r["theme_id"]),
                e(r["name"] or "—"),
                e(r["parent_id"] or "—"),
                e(r["parent_name"] or "—"),
                e(r["energy_reward_1"]),
                e(r["energy_reward_2"]),
                e(r["entry_count"]),
                e(r["child_count"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
