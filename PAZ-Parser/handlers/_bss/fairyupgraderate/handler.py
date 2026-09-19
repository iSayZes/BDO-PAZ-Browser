from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.fairy import upgrade_step_label
from _common.html import e, icon_cell, table
from _common.icon_index import IconKind, icon_path
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_fairyupgraderate_records


_LANG_DIR = Path(__file__).parent / "lang"

# Item display names live in LOC type 0, keyed by item ID.
_LOC_TYPE_ITEM = 0

_CHANCE_DECIMALS = 4


def _item_name(item_id: int) -> str:
    if not is_loc_loaded():
        return ""

    return strip_pa_tags(loc_lookup(_LOC_TYPE_ITEM, item_id, 0, 0, 0)).strip()


class FairyUpgradeRateBssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []

        for record in parse_fairyupgraderate_records(data):
            row = dict(record)
            item_id = row["item_id"]
            row["upgrade"] = upgrade_step_label(row["step"])
            row["item_name"] = _item_name(item_id)
            row["icon_path"] = icon_path(IconKind.ITEM, item_id)
            records.append(row)

        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        steps = len({record["step"] for record in records})
        meta = f"{len(records):,} Sprouting rates across {steps} upgrade steps"

        localized = sum(1 for record in records if record.get("item_name"))
        if localized:
            meta += f" · {localized:,} LOC names"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("step", "Step"), "num", ""),
            (cols.get("upgrade", "Upgrade"), "", ""),
            (cols.get("icon", "Icon"), "", ""),
            (cols.get("item", "Item"), "", ""),
            (cols.get("itemId", "Item ID"), "num", ""),
            (cols.get("chancePerItem", "Chance / Item"), "num", ""),
            (cols.get("ratePpm", "Rate (ppm)"), "num", ""),
            (cols.get("itemsForMax", "Items for Max"), "num", ""),
        ]

        rows = [
            [
                e(record["step"]),
                e(record["upgrade"] or record["step"]),
                icon_cell(record["icon_path"]),
                e(record["item_name"] or record["item_id"]),
                e(record["item_id"]),
                e(f"{round(record['chance_pct'], _CHANCE_DECIMALS):g}%"),
                e(f"{record['rate_ppm']:,}"),
                e(f"{record['items_for_max']:,}"),
            ]
            for record in slice_
        ]

        return table(meta, headers, rows)
