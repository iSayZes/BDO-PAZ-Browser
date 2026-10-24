"""The uses of a house: (receipe key, level) entries named and linked to their `houseinforeceipe.dbss` row.

`houseinfo.bss` and `guildhouseinfo.dbss` both store a house's uses as
`(u32 receipe_key, u32 level)` pairs. The name is the LOC type 16 house use
name, else the Korean `houseinforeceipe.dbss` name, else the bare key.
"""

from __future__ import annotations

from _common.html import html_list_cell, record_link
from _dbss.guildhousecraftskill.labels import house_use_name
from .parser import FILE_NAME as RECEIPE_FILE, parse_houseinforeceipe_records


RECEIPE_PATH = f"gamecommondata/binary/{RECEIPE_FILE}"
_LINK_CLASS = "record-link"
_EMPTY = "-"


def receipe_companion(internal_path: str) -> str:
    """The `houseinforeceipe.dbss` path next to a file in the same folder."""
    folder = internal_path.rsplit("/", 1)[0]
    return f"{folder}/{RECEIPE_FILE}"


def receipe_names_kr(companions: dict[str, bytes]) -> dict[int, str]:
    """Korean name of each `houseinforeceipe.dbss` receipe; empty without the companion."""
    receipe_data = companions.get(RECEIPE_FILE)
    if receipe_data is None:
        return {}
    return {r["receipe_key"]: r["name_kr"] for r in parse_houseinforeceipe_records(receipe_data)}


def labelled_crafts(crafts: list[dict], names_kr: dict[int, str], level_format: str) -> list[dict]:
    """Each craft with a `label`: `level_format` filled with the use name and the level."""
    return [
        {
            **craft,
            "label": level_format.format(
                name=house_use_name(craft["receipe_key"]) or names_kr.get(craft["receipe_key"]) or craft["receipe_key"],
                level=craft["level"],
            ),
        }
        for craft in crafts
    ]


def uses_cell(crafts: list[dict]) -> str:
    """One line per labelled craft, linked to its `houseinforeceipe.dbss` row."""
    if not crafts:
        return _EMPTY
    lines = [
        record_link(craft["label"], RECEIPE_PATH, "receipe_key", craft["receipe_key"], _LINK_CLASS)
        for craft in crafts
    ]
    return html_list_cell(lines, separator="<br>")
