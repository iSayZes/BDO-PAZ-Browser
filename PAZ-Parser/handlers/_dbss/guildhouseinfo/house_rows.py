"""The table row of a house key: `houseinfo.bss` for node houses, `guildhouseinfo.dbss` for guild houses.

Tables that list house characters (`houseinfoviewposition.dbss`,
`innstaticstatus.dbss`) link each key to the row that describes the house
and show its town. Both tables are optional companions; a key neither holds
(the villas `3371` to `3387` on client 3482) stays plain text.
"""

from __future__ import annotations

from typing import NamedTuple

from _common.html import e, record_link
from _common.town import town_name
from _bss.houseinfo.parser import FILE_NAME as HOUSEINFO_FILE, parse_houseinfo
from .parser import FILE_NAME as GUILDHOUSEINFO_FILE, KEY_FIELD, parse_guildhouseinfo_records


HOUSEINFO_PATH = f"gamecommondata/binary/{HOUSEINFO_FILE}"
GUILDHOUSEINFO_PATH = f"gamecommondata/binary/{GUILDHOUSEINFO_FILE}"
_LINK_CLASS = "record-link"


class HouseRow(NamedTuple):
    """Where a house key has its row, and the town that row names."""

    path: str
    affiliated_town: int


def house_row_companions(internal_path: str) -> list[str]:
    """The `houseinfo.bss` and `guildhouseinfo.dbss` paths next to a file in the same folder."""
    folder = internal_path.rsplit("/", 1)[0]
    return [f"{folder}/{HOUSEINFO_FILE}", f"{folder}/{GUILDHOUSEINFO_FILE}"]


def house_rows(companions: dict[str, bytes]) -> dict[int, HouseRow]:
    """House key -> its row, from whichever companions are loaded.

    Raises ValueError, naming the companion, when its rows do not parse.
    """
    rows: dict[int, HouseRow] = {}
    houseinfo = companions.get(HOUSEINFO_FILE)
    if houseinfo is not None:
        try:
            houses = parse_houseinfo(houseinfo).houses
        except ValueError as ex:
            raise ValueError(f"{HOUSEINFO_FILE}: {ex}") from ex
        rows.update((h["character_key"], HouseRow(HOUSEINFO_PATH, h["affiliated_town"])) for h in houses)
    guildhouseinfo = companions.get(GUILDHOUSEINFO_FILE)
    if guildhouseinfo is not None:
        try:
            guild_houses = parse_guildhouseinfo_records(guildhouseinfo)
        except ValueError as ex:
            raise ValueError(f"{GUILDHOUSEINFO_FILE}: {ex}") from ex
        rows.update((h[KEY_FIELD], HouseRow(GUILDHOUSEINFO_PATH, h["affiliated_town"])) for h in guild_houses)
    return rows


def house_fields(house_row: HouseRow | None) -> dict:
    """The record fields a house key's row gives: `house_path` and the `town` name, both None without a row."""
    if house_row is None:
        return {"house_path": None, "town": None}
    town = town_name(house_row.affiliated_town) or str(house_row.affiliated_town)
    return {"house_path": house_row.path, "town": town}


def house_cell(label: str, character_key: int, house_path: str | None) -> str:
    """`label` as a link to the house's row in `house_path`, or plain text without one."""
    if house_path is None:
        return e(label)
    return record_link(label, house_path, KEY_FIELD, character_key, _LINK_CLASS)
