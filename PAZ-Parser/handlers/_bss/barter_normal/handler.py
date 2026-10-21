"""barter_normal.bss preview handler: one row per barter slot of each region, both lists."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.barter.category import category_names
from _bss.barter.display import exchange_cells, exchange_columns, exchange_text_fields
from _bss.barter.sub_group import sub_group_link
from _bss.barter_npclist.parser import parse_barter_npclist_records
from _common.character import character_name
from _common.html import Column, e, error, flag_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.town import town_name
from .parser import FILE_NAME, parse_barter_normal_records


_LANG_DIR = Path(__file__).parent / "lang"
_NPCLIST_FILE = "barter_npclist.bss"
_EMPTY = "-"


def _region_npcs(npclist_data: bytes | None) -> dict[int, int]:
    """Barter region key -> NPC character from the optional `barter_npclist.bss`;
    empty when it is missing or unreadable, since the NPC is only a convenience here."""
    if npclist_data is None:
        return {}
    try:
        records = parse_barter_npclist_records(npclist_data)
    except ValueError:
        return {}
    return {record["barter_region_key"]: record["character_id"] for record in records}


def _region_fields(region_keys: set[int], npcs: dict[int, int]) -> dict[int, dict]:
    """The region name and NPC of each region key, looked up once per region."""
    fields: dict[int, dict] = {}
    for key in region_keys:
        character_id = npcs.get(key)
        fields[key] = {
            # LOC type 17 names regions; the barter regions are regions.
            "region_name": town_name(key) or None,
            "character_id": character_id,
            "npc_name": (character_name(character_id) or None) if character_id is not None else None,
        }
    return fields


class BarterNormalBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["regionKey"], "num", sort_key="region_key"),
            Column(cols["region"], sort_key="region_name"),
            Column(cols["npc"], sort_key="npc_name"),
            Column(cols["material"], sort_key="is_material"),
            Column(cols["slot"], "num", sort_key="slot"),
            Column(cols["selectRate"], "num", sort_key="select_rate"),
            *exchange_columns(self.lang),
            Column(cols["subGroup"], "num", sort_key="sub_group"),
            Column(cols["category"], sort_key="category_names"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_NPCLIST_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_barter_normal_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        regions = _region_fields(
            {record["region_key"] for record in records},
            _region_npcs(companions.get(_NPCLIST_FILE)),
        )
        return [
            {
                **record,
                **regions[record["region_key"]],
                **exchange_text_fields(record),
                # 0 is "no sub group"; None sorts its dashed cell last.
                "sub_group": record["barter_sub_group"] or None,
                "category_names": category_names(record["barter_category"]),
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
                e(r["region_key"]),
                e(r["region_name"] or _EMPTY),
                e(r["npc_name"] or _EMPTY),
                flag_cell(r["is_material"]),
                e(r["slot"]),
                e(f"{r['select_rate']:,}"),
                *exchange_cells(r),
                sub_group_link(r["is_material"], r["sub_group"]) if r["sub_group"] else _EMPTY,
                e(r["category_names"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            regions=len({r["region_key"] for r in records}),
        )
        return table(meta, self._columns(), rows)
