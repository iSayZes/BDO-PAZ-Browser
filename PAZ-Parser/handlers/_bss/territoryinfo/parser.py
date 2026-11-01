"""`territoryinfo.bss`: the world's territories, one row per LOC type 12 ID.

    PABR | u32 count | count x row | string table | u32 string_table_start | u32 0
    row: u16 territory_key | u8 is_king_territory_only | u8 is_lord_territory_only
         | f32[3] x positions | u32 national_key | 4 x u32 string ref
         | counted lists (booty items, territory trade keys, territory supply keys)
         | u32 unknown_tail

Rows are byte-packed and grow with their lists, so they are walked in order
and must end exactly where the string table (or, before PABR, the file)
ends. The layouts differ in the position count, the list count width, which
lists a row holds, the supply key width, the tail and, before PABR, inline
UTF-16LE strings in place of string table refs. A file is read with the first
layout of its kind (PABR or not, newest first) whose rows tile it exactly.
Layouts 1 to 9 in docs/file-formats/bss/territoryinfo_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.client_versions import ClientRange, client_order
from _common.pabr_offset import PABR_MAGIC
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader
from _common.ui_texture import ui_texture_path


FILE_NAME = "territoryinfo.bss"

# u16 territory_key | u8 is_king_territory_only | u8 is_lord_territory_only
_HEAD = struct.Struct("<HBB")
_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
# nation_ref | name_ref | icon_large_ref | icon_small_ref
_REFS = struct.Struct("<4I")
_INLINE_STRINGS = 4
_INLINE_COUNT_SIZE = 4

_AXES = 3
# Every stored vec3 value in file order (Territory_Table column names); a
# layout stores the first 1, 3 or 5.
POSITION_FIELDS = (
    "occupying_tent_position",
    "volunteer_attack_position",
    "volunteer_defense_position",
    "plunder_attack_position",
    "plunder_defense_position",
)


@dataclass(frozen=True)
class RowLayout:
    """One documented Territory Row shape; `number` is its Layout N in the doc."""

    number: int
    is_pabr: bool
    list_count: struct.Struct
    position_count: int
    has_trade_keys: bool
    supply_key_format: str
    has_tail: bool
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


# Newest first. Layouts 1 to 4 have no PABR header and store their strings inline.
LAYOUTS = (
    RowLayout(9, True, _U64, 3, False, "I", True, clients=(ClientRange(2726),)),
    RowLayout(8, True, _U64, 3, False, "H", True, clients=(ClientRange(2575, 2717),)),
    RowLayout(7, True, _U64, 3, True, "H", True, clients=(ClientRange(2474, 2567),)),
    RowLayout(6, True, _U64, 5, True, "H", True, clients=(ClientRange(1276, 2468),)),
    RowLayout(5, True, _U64, 5, True, "H", False, clients=(ClientRange(805, 1267),)),
    RowLayout(4, False, _U64, 5, True, "H", False, clients=(ClientRange(723, 794),)),
    RowLayout(3, False, _U64, 3, True, "H", False, clients=(ClientRange(526, 711),)),
    RowLayout(2, False, _U32, 3, True, "H", False, clients=(ClientRange(472, 521),)),
    RowLayout(1, False, _U32, 1, True, "H", False, clients=(ClientRange(435, 466),)),
)


def _positions(coords: tuple[float, ...]) -> dict[str, list[float]]:
    """Each stored vec3 value as `[x, y, z]` under its field name."""
    return {
        field: list(coords[i * _AXES : (i + 1) * _AXES])
        for i, field in enumerate(POSITION_FIELDS[: len(coords) // _AXES])
    }


def _key_list(reader: RecordReader, layout: RowLayout, value_format: str) -> list[int]:
    """A count of the layout's width, then that many values."""
    (count,) = reader.unpack(layout.list_count)
    value_size = struct.calcsize(f"<{value_format}")
    if count * value_size > reader.remaining():
        raise ValueError(f"{FILE_NAME} list of {count} runs past its row at 0x{reader.pos:X}")
    return list(reader.unpack(struct.Struct(f"<{count}{value_format}")))


def _row_strings(reader: RecordReader, layout: RowLayout, strings: list[str]) -> list[str]:
    """Nation name, territory name, large and small icon path."""
    if layout.is_pabr:
        return [string_at(strings, ref) for ref in reader.unpack(_REFS)]
    return [reader.text(wide=True) for _ in range(_INLINE_STRINGS)]


def _read_row(reader: RecordReader, layout: RowLayout, strings: list[str]) -> dict:
    key, is_king_territory_only, is_lord_territory_only = reader.unpack(_HEAD)
    coords = reader.unpack(struct.Struct(f"<{layout.position_count * _AXES}f"))
    (national_key,) = reader.unpack(_U32)
    nation, name, icon_large, icon_small = _row_strings(reader, layout, strings)
    record = {
        "territory_key": key,
        # Korean, but English in the `gamecommondata/binary/en/` copy that
        # older clients ship.
        "nation_kr": nation,
        "name_kr": name,
        "is_king_territory_only": bool(is_king_territory_only),
        "is_lord_territory_only": bool(is_lord_territory_only),
        **_positions(coords),
        "national_key": national_key,
        "icon_large_path": ui_texture_path(icon_large),
        "icon_small_path": ui_texture_path(icon_small),
        "booty_item_ids": _key_list(reader, layout, "I"),
    }
    if layout.has_trade_keys:
        record["territory_trade_keys"] = _key_list(reader, layout, "H")
    record["territory_supply_keys"] = _key_list(reader, layout, layout.supply_key_format)
    if layout.has_tail:
        (record["unknown_tail"],) = reader.unpack(_U32)
    return record


def _read_rows(data: bytes, layout: RowLayout) -> list[dict]:
    """Every row read with `layout`. Raises ValueError when they do not tile the file."""
    if layout.is_pabr:
        start, end, strings = HEADER_SIZE, checked_string_table_start(data, FILE_NAME), read_string_table(data)
        count = u32(data, 4)
    else:
        start, end, strings = _INLINE_COUNT_SIZE, len(data), []
        count = u32(data, 0)
    reader = RecordReader(data, start, end, f"{FILE_NAME} rows")
    records = [_read_row(reader, layout, strings) for _ in range(count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} rows end at 0x{reader.pos:X} but the rows region ends at 0x{end:X}")
    return records


def parse_territoryinfo_records(data: bytes) -> list[dict]:
    """Every territory row in file order, with its strings resolved.

    Raises ValueError when no layout's rows end exactly where the string table
    (or the file) starts: then the row layout has changed and every field is
    suspect.
    """
    if len(data) < _INLINE_COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")
    is_pabr = data[: len(PABR_MAGIC)] == PABR_MAGIC
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        if layout.is_pabr != is_pabr:
            continue
        try:
            return _read_rows(data, layout)
        except ValueError as exc:
            breaks.append(f"Layout {layout.number}: {exc}")
    raise ValueError(f"{FILE_NAME} fits no known layout ({'; '.join(breaks)})")
