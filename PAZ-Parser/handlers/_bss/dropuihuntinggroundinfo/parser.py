"""`dropuihuntinggroundinfo.bss`: the hunting grounds of the drop item window.

    PABR | u32 count | count x variable-length row | string table
    | u32 string_table_start | u32 0

Each row lists the zone's region tab, filter categories, monsters, quests,
drop items, tags, regions and titles (each a u32 count and its values), then
its position, recommended and Total Stat AP / DP, node, Max AP Limit and
monster species. `dropuimaincategoryinfo.bss` maps the region tab to a
territory; `_bss/dropuitaginfo/parser.py` reads the tag colours. Full layouts
in docs/file-formats/dropuihuntinggroundinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import check_pabr, fixed_row_offsets, read_string_table, string_at, string_table_start
from _common.record_reader import RecordReader


_HEADER_SIZE = 8

_U32 = struct.Struct("<I")
# u32 key | u32 main_category_key
_HEAD = struct.Struct("<II")
# f32 x 3 position | f32 recommended_ap | f32 recommended_dp | u32 node_key
# | f32 total_ap | f32 total_dp | u32 limited_ap | u32 limited_ap_apply_percent
# | u8 tribe_type
_TAIL = struct.Struct("<3fffIffIIB")

# u32 key | u16 territory_key | u32 icon_ref
_MAIN_CATEGORY = struct.Struct("<IHI")


def _row_count(data: bytes, name: str) -> int:
    """The PABR row count, after checking the magic."""
    check_pabr(data, name)
    return u32(data, 4)


def _list(reader: RecordReader, value_format: str) -> list[int]:
    """A u32 count followed by that many values of `value_format` (`H` or `I`)."""
    (count,) = reader.unpack(_U32)
    return list(reader.unpack(struct.Struct(f"<{count}{value_format}")))


def _parse_row(reader: RecordReader, strings: list[str]) -> dict:
    key, main_category_key = reader.unpack(_HEAD)
    sub_category_keys = _list(reader, "I")
    (name_ref,) = reader.unpack(_U32)
    monster_ids = _list(reader, "H")
    repeat_quest_keys = _list(reader, "I")
    sudden_quest_keys = _list(reader, "I")
    drop_item_ids = _list(reader, "I")
    tag_keys = _list(reader, "I")
    region_keys = _list(reader, "H")
    title_keys = _list(reader, "I")
    (
        pos_x, pos_y, pos_z,
        recommended_ap, recommended_dp, node_key,
        total_ap, total_dp, limited_ap, limited_ap_apply_percent,
        tribe_type,
    ) = reader.unpack(_TAIL)
    return {
        "key": key,
        "main_category_key": main_category_key,
        "sub_category_keys": sub_category_keys,
        "name_kr": string_at(strings, name_ref),
        "monster_ids": monster_ids,
        "repeat_quest_keys": repeat_quest_keys,
        "sudden_quest_keys": sudden_quest_keys,
        "drop_item_ids": drop_item_ids,
        "tag_keys": tag_keys,
        "region_keys": region_keys,
        "title_keys": title_keys,
        "pos_x": pos_x,
        "pos_y": pos_y,
        "pos_z": pos_z,
        "recommended_ap": recommended_ap,
        "recommended_dp": recommended_dp,
        "node_key": node_key,
        "total_ap": total_ap,
        "total_dp": total_dp,
        "limited_ap": limited_ap,
        "limited_ap_apply_percent": limited_ap_apply_percent,
        "tribe_type": tribe_type,
    }


def parse_hunting_ground_records(data: bytes) -> list[dict]:
    """Every hunting ground row in file order, with its Korean name resolved.

    Raises ValueError on a bad magic, when a row runs into the string table, or
    when the rows end anywhere but where the string table starts: then the row
    layout has changed and every later field is suspect.
    """
    count = _row_count(data, "dropuihuntinggroundinfo.bss")
    rows_end = string_table_start(data)
    strings = read_string_table(data)

    records: list[dict] = []
    pos = _HEADER_SIZE
    for index in range(count):
        reader = RecordReader(data, pos, rows_end, f"hunting ground row {index}")
        records.append(_parse_row(reader, strings))
        pos = reader.pos
    if pos != rows_end:
        raise ValueError(
            f"dropuihuntinggroundinfo.bss rows end at 0x{pos:X} but its string "
            f"table starts at 0x{rows_end:X}"
        )
    return records


def parse_territory_keys(data: bytes) -> dict[int, int]:
    """Region tab key -> territory key, from `dropuimaincategoryinfo.bss`.

    Raises ValueError on a bad magic or when the rows do not end where the
    string table starts.
    """
    territories: dict[int, int] = {}
    for offset in fixed_row_offsets(data, _MAIN_CATEGORY.size, "dropuimaincategoryinfo.bss"):
        key, territory_key, _icon_ref = _MAIN_CATEGORY.unpack_from(data, offset)
        territories[key] = territory_key
    return territories
