"""`vehicleskill.dbss`: mount and ship skills, one variable-size record per skill key.

    u8 unknown_00 | u32 count | count x Record, back to back up to EOF

Each record holds the Korean name, EXP and price values, the icon, three
key-command and description texts, the training servants, the contents group
hashes, a condition script and the ship skill order. Layout in
docs/file-formats/vehicleskill_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader


FILE_NAME = "vehicleskill.dbss"

_HEADER = struct.Struct("<BI")
_KEY = struct.Struct("<B")
# u32 max_exp | u32 add_exp_for_check | u64 base_price | u32 add_mating_rate | u8 is_learn_from_item
_STATS = struct.Struct("<IIQIB")
# u8 is_market_filter | u32 contents_group_count
_GROUPS_HEAD = struct.Struct("<BI")
_GROUPS_TAIL_SIZE = 8
# u8 vehicle_skill_lock | u32 unknown_condition_desc_01 | u32 skill_order | u32 need_life_level_for_auto_skill
_TAIL = struct.Struct("<BIII")


def _parse_record(reader: RecordReader) -> dict:
    (key,) = reader.unpack(_KEY)
    name_kr = reader.text(wide=True)
    max_exp, add_exp_for_check, base_price, add_mating_rate, is_learn_from_item = reader.unpack(_STATS)
    icon_path = reader.text(wide=True)
    desc_kr = reader.text(wide=True)
    desc2_kr = reader.text(wide=True)
    console_desc_kr = reader.text(wide=True)
    training_skill_characters = reader.text(wide=True)
    is_market_filter, group_count = reader.unpack(_GROUPS_HEAD)
    group_hashes = list(reader.unpack(struct.Struct(f"<{group_count}I")))
    unknown_groups_00 = reader.unpack(struct.Struct(f"<{_GROUPS_TAIL_SIZE}s"))[0]
    condition_desc = reader.text(wide=True)
    vehicle_skill_lock, unknown_condition_desc_01, skill_order, need_life_level = reader.unpack(_TAIL)
    return {
        "key": key,
        "name_kr": name_kr,
        "max_exp": max_exp,
        "add_exp_for_check": add_exp_for_check,
        "base_price": base_price,
        "add_mating_rate": add_mating_rate,
        "is_learn_from_item": is_learn_from_item,
        "icon_path": icon_path,
        "desc_kr": desc_kr,
        "desc2_kr": desc2_kr,
        "console_desc_kr": console_desc_kr,
        "training_skill_characters": training_skill_characters,
        "is_market_filter": is_market_filter,
        "contents_group_key_hashes": group_hashes,
        "unknown_contents_group_key_hashes_00": unknown_groups_00.hex(),
        "condition_desc": condition_desc,
        "vehicle_skill_lock": vehicle_skill_lock,
        "unknown_condition_desc_01": unknown_condition_desc_01,
        "skill_order": skill_order,
        "need_life_level_for_auto_skill": need_life_level,
    }


def parse_vehicleskill_records(data: bytes) -> list[dict]:
    """Every skill in file order (key order).

    Raises ValueError when a record runs past the file or bytes follow the
    last declared record.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    _unknown_00, count = reader.unpack(_HEADER)
    records = [_parse_record(reader) for _ in range(count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME}: {reader.remaining():,} bytes follow record {count}")
    return records


def vehicle_skill_names_kr(data: bytes | None) -> dict[int, str]:
    """Skill key -> Korean name, or an empty map without the file."""
    if data is None:
        return {}
    return {record["key"]: record["name_kr"] for record in parse_vehicleskill_records(data)}
