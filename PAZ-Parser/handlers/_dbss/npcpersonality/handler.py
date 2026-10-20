from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import loc_lookup
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, picked_records
from .parser import parse_npcpersonality_records, parse_npcpersonalityoffset_records

_LANG_DIR = Path(__file__).parent / "lang"


def _decode_personality_type(code: int) -> str:
    major = code // 100
    name = loc_lookup(7, major)
    return name if name else f"?{major}"


def _group_str(group_id: int) -> str:
    return "-" if group_id == 0 else str(group_id)


def npc_personality_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("personality_id", "personalityId"),
            offset_column("data_offset", "dataOffset"),
        ],
        picked_records(parse_npcpersonalityoffset_records, ("personality_id", "data_offset")),
    )


class NpcPersonalityHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["id"], "num", sort_key="personality_id"),
            Column(cols["row"], "num", sort_key="row"),
            Column(cols["groupA"], "num", sort_key="group_a_id"),
            Column(cols["needA"], "num", sort_key="group_a_need_count"),
            Column(cols["groupB"], "num", sort_key="group_b_id"),
            Column(cols["needB"], "num", sort_key="group_b_need_count"),
            Column(cols["groupC"], "num", sort_key="group_c_id"),
            Column(cols["needC"], "num", sort_key="group_c_need_count"),
            Column(cols["intMin"], "num", sort_key="interest_min"),
            Column(cols["intMax"], "num", sort_key="interest_max"),
            Column(cols["favMin"], "num", sort_key="favor_min"),
            Column(cols["favMax"], "num", sort_key="favor_max"),
            Column(cols["horoscope"], sort_key="personality_type"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [dict(rec) for rec in parse_npcpersonality_records(data)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["personality_id"]),
                e(r["row"]),
                e(_group_str(r["group_a_id"])),
                e(r["group_a_need_count"]),
                e(_group_str(r["group_b_id"])),
                e(r["group_b_need_count"]),
                e(_group_str(r["group_c_id"])),
                e(r["group_c_need_count"]),
                e(int(r["interest_min"])),
                e(int(r["interest_max"])),
                e(int(r["favor_min"])),
                e(int(r["favor_max"])),
                e(_decode_personality_type(r["personality_type"])),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
