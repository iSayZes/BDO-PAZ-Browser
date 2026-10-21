"""floatfishing.dbss preview handler: each fishing group with its drop slots and the points that use it."""
from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.html import Column, e, html_list_cell, record_link
from _common.lang import load_handler_strings
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.rate import rate_percent
from _common.row_table import RowTableHandler
from _dbss.floatfishingpoint.parser import FILE_NAME as POINT_FILE, parse_floatfishingpoint_records
from .parser import FILE_NAME, KEY_FIELD, parse_floatfishing_records, parse_floatfishingoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
POINT_PATH = f"gamecommondata/binary/{POINT_FILE}"
# Lang keys of the five drop slots, in row order.
_SLOT_KEYS = ("treasure", "rare", "large", "general", "junk")


def float_fishing_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_floatfishingoffset_rows, KEY_FIELD, "groupKey")


def _point_keys_by_group(point_data: bytes | None) -> dict[int, list[int]] | None:
    """`fishing_group_key` -> the point keys that use it, or None without the companion."""
    if point_data is None:
        return None
    groups: dict[int, list[int]] = defaultdict(list)
    for point in parse_floatfishingpoint_records(point_data):
        groups[point["fishing_group_key"]].append(point["point_key"])
    return groups


class FloatFishingHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["groupKey"], "num", sort_key=KEY_FIELD),
            Column(labels["drops"], sort_key="drop_text"),
            Column(labels["points"], "num", sort_key="point_count"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{POINT_FILE}"]

    def _drop_lines(self, record: dict) -> list[str]:
        """`Rare: 10944 (100%)` per filled slot."""
        slots = load_handler_strings(self.lang, _LANG_DIR)["slots"]
        return [
            f"{slots[slot]}: {drop_id} ({rate_percent(rate)})"
            for slot, drop_id, rate in zip(_SLOT_KEYS, record["drop_ids"], record["drop_rates"], strict=True)
            if drop_id
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        point_keys = _point_keys_by_group(companions.get(POINT_FILE))
        records = []
        for record in parse_floatfishing_records(data):
            drops = self._drop_lines(record)
            keys = None if point_keys is None else point_keys.get(record[KEY_FIELD], [])
            records.append(
                {
                    **record,
                    "drops": drops,
                    "drop_text": ", ".join(drops),
                    "point_keys": keys,
                    # None with no point, so the empty cell sorts last.
                    "point_count": len(keys) if keys else None,
                }
            )
        return records

    def cells(self, record: dict) -> list[str]:
        keys = record["point_keys"]
        if keys is None:
            points = "-"
        else:
            points = html_list_cell(
                [record_link(str(key), POINT_PATH, "point_key", key, "record-link") for key in keys]
            ) or "-"
        return [
            e(record[KEY_FIELD]),
            "<br>".join(e(line) for line in record["drops"]) or "-",
            points,
        ]
