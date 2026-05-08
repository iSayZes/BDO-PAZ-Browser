from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import is_loc_loaded
from _common.html import e, table
from _common.lang import load_handler_strings
from .parser import (
    parse_gift_offset_records,
    parse_npcgift_records,
    parse_npcgiftdata_records,
)


_LANG_DIR = Path(__file__).parent / "lang"


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
        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("npcId", "NPC ID"), "num", ""),
            (cols.get("dataOffset", "Data Offset"), "num", ""),
            (cols.get("dataSize", "Data Size"), "num", ""),
        ]
        rows = [
            [
                e(r["npc_id"]),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)


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
        cols = load_handler_strings(self.lang, _LANG_DIR).get("giftColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("npcId", "NPC ID"), "num", ""),
            (cols.get("npcName", "NPC Name"), "", ""),
            (cols.get("itemId", "Item ID"), "num", ""),
            (cols.get("itemName", "Item Name"), "", ""),
            (cols.get("amity", "Amity"), "num", ""),
        ]

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
        return table(meta, headers, rows)


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
        cols = load_handler_strings(self.lang, _LANG_DIR).get("dataColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("npcId", "NPC ID"), "num", ""),
            (cols.get("npcName", "NPC Name"), "", ""),
            (cols.get("unknownParam", "Unknown Param"), "num", ""),
            (cols.get("dialogue", "Dialogue"), "", ""),
        ]

        rows = [
            [
                e(r["npc_id"]),
                e(r["npc_name"] or "—"),
                e(r["unknown_param"]),
                e(r["dialogue"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
