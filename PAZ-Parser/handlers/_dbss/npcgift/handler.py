from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import is_loc_loaded
from _common.html import e, table
from .parser import (
    parse_gift_offset_records,
    parse_npcgift_records,
    parse_npcgiftdata_records,
)


_OFFSET_HEADERS: list[tuple[str, str, str]] = [
    ("NPC ID",      "num", ""),
    ("Data Offset", "num", ""),
    ("Data Size",   "num", ""),
]

_GIFT_HEADERS: list[tuple[str, str, str]] = [
    ("NPC ID",    "num", ""),
    ("NPC Name",  "",    ""),
    ("Item ID",   "num", ""),
    ("Item Name", "",    ""),
    ("Amity",     "num", ""),
]

_DATA_HEADERS: list[tuple[str, str, str]] = [
    ("NPC ID",        "num", ""),
    ("NPC Name",      "",    ""),
    ("Unknown Param", "num", ""),
    ("Dialogue",      "",    ""),
]


class _NpcGiftOffsetHandler(PreviewHandler):
    """Shared handler for npcgiftoffset.dbss and npcgiftdataoffset.dbss — identical layout."""

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [dict(r) for r in parse_gift_offset_records(data)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} offset records"
        rows = [
            [
                e(r["npc_id"]),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
            ]
            for r in slice_
        ]
        return table(meta, _OFFSET_HEADERS, rows)


class NpcGiftOffsetHandler(_NpcGiftOffsetHandler):
    pass


class NpcGiftDataOffsetHandler(_NpcGiftOffsetHandler):
    pass


class NpcGiftHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [dict(r) for r in parse_npcgift_records(data)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        loc = is_loc_loaded()

        with_npc_name  = sum(1 for r in records if r["npc_name"])
        with_item_name = sum(1 for r in records if r["item_name"])
        meta = f"{len(records):,} gift rows"
        if loc:
            meta += f" · {with_npc_name:,} NPC names · {with_item_name:,} item names"

        rows = [
            [
                e(r["npc_id"]),
                e(r["npc_name"] or "—"),
                e(r["item_id"]),
                e(r["item_name"] or "—"),
                e(r["amity"]),
            ]
            for r in slice_
        ]
        return table(meta, _GIFT_HEADERS, rows)


class NpcGiftDataHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [dict(r) for r in parse_npcgiftdata_records(data)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        loc = is_loc_loaded()

        with_loc = sum(1 for r in records if r["dialogue_source"] == "loc")
        meta = f"{len(records):,} NPC dialogue records"
        if loc:
            meta += f" · {with_loc:,} with LOC type 54 text"

        rows = [
            [
                e(r["npc_id"]),
                e(r["npc_name"] or "—"),
                e(r["unknown_param"]),
                e(r["dialogue"]),
            ]
            for r in slice_
        ]
        return table(meta, _DATA_HEADERS, rows)
