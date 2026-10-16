"""Parse enchantstaticstatus.dbss: one block per (enchant key, level).

The enchant key is the u32 that `itemenchant.dbss` stores just before an
item's Korean name; many items share one key. Block `level` holds the stats of
the item at that level and what the attempt to reach it costs. Layout and
evidence are in docs/file-formats/enchantstaticstatus_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_offset import parse_pabr_u32_offset_rows
from _common.record_reader import RecordReader

# key = level << 24 | enchant_key
_LEVEL_SHIFT = 24
_ENCHANT_KEY_MASK = 0x00FFFFFF

# +0x00 to +0x42: key, level, material and count, perfect enhancement count,
# black_count_for_item_market, 8 zero bytes, success rate, downgrade rate,
# 4 zero bytes, durability, durability lost on failure,
# recover_max_endurance, unknown_3b, durability lost by a perfect
# enhancement, max HP.
_HEADER = struct.Struct("<IBIQQQ8xII4xHHHBHf")
# +0x42 to +0xA7: max MP, HP and MP regen, 72 zero bytes, weight, 8 zero
# bytes, socket count. The names follow the Enchant_* sheet columns.
_VARIED = struct.Struct("<ifi72xq8xB")
_U32 = struct.Struct("<I")
_F32 = struct.Struct("<f")
# Seven stats, three f32 each (melee, ranged, magic): added damage, one
# unknown, AP min, AP max, AP display, damage reduction, evasion.
_LANE_STATS = struct.Struct("<21f")
_ADDED_DAMAGE, _AP_MIN, _AP_MAX, _EVASION = 0, 2, 3, 6
_LANES = 3
# +0xFB: skill_key, `skill_no << 16 | level` as in skill.dbss; the SkillNo
# column is the high half.
_SKILL_NO_SHIFT = 16
# After the effect script, 13 bytes: is_notify_world, what a failed attempt
# does (the EnchantType column), item_market_added_price, an unknown u32,
# the two market filters and a zero byte.
_AFTER_SCRIPT = struct.Struct("<BBII2Bx")
# Fail results: the client's danger types (Safe, Broken, Gradedown); 0 is
# stored on attempts that cannot fail.
FAIL_CANNOT_FAIL, FAIL_SAFE, FAIL_DESTROYED, FAIL_DOWNGRADE = 0, 1, 2, 3
# Per lane: evasion, hidden evasion, damage reduction, hidden damage reduction.
_DEFENSE = struct.Struct("<4f")
_HIDDEN_EVASION, _DAMAGE_REDUCTION, _HIDDEN_DAMAGE_REDUCTION = 1, 2, 3
# unknown_dice_accuracy_30 (three i32, always -1), then 65 bytes: life main and sub type, life stat,
# group level, the new perfect enhancement item, count and durability loss,
# prevent cron count, three adjust values, max food, four cannon values.
_UNKNOWN_DICE_ACCURACY_30 = b"\xff" * 12
_UNKNOWN_DICE_ACCURACY_30_FIELD = struct.Struct(f"{len(_UNKNOWN_DICE_ACCURACY_30)}s")
_LATE_FIELDS = struct.Struct("<BBfBIqHq3fq4i")
# cronable, guild_rental, need_perfect_enchant_stack, 2 zero bytes.
_FOOTER = struct.Struct("<BBH2x")

# Rates are stored in millionths; shown as a percentage.
_RATE_PER_PERCENT = 10_000


@dataclass(frozen=True)
class _Header:
    material_item_id: int
    material_count: int
    perfect_count: int
    success_rate: int
    downgrade_rate: int
    max_durability: int
    fail_durability_loss: int
    perfect_durability_loss: int
    max_hp: float


def split_enchant_status_key(key: int) -> tuple[int, int]:
    """`(enchant_key, level)` of an offset key."""
    return key & _ENCHANT_KEY_MASK, key >> _LEVEL_SHIFT


def parse_enchantstaticstatusoffset_records(data: bytes) -> list[dict]:
    """The offset rows with the key split into enchant key and level."""
    records = []
    for row in parse_pabr_u32_offset_rows(data):
        enchant_key, level = split_enchant_status_key(row.entry_id)
        records.append({
            "enchant_key": enchant_key,
            "level": level,
            "data_offset": row.offset,
            "data_size": row.size,
        })
    return records


def _read_header(reader: RecordReader, enchant_key: int, level: int) -> tuple[_Header, dict]:
    """The cost and durability fields, and the fields kept as they are stored."""
    (stored_key, stored_level, material, count, perfect_count, black_count_for_item_market,
     rate, downgrade_rate, durability, fail_loss, recover_max_endurance, _unknown_3b,
     perfect_loss, max_hp) = reader.unpack(_HEADER)
    if (stored_key, stored_level) != (enchant_key, level):
        raise ValueError(
            f"enchantstaticstatus block {enchant_key}/{level} stores {stored_key}/{stored_level}"
        )
    max_mp, recov_hp, recov_mp, weight, socket_count = reader.unpack(_VARIED)
    header = _Header(material, count, perfect_count, rate, downgrade_rate, durability, fail_loss, perfect_loss, max_hp)
    return header, {
        "black_count_for_item_market": black_count_for_item_market,
        "recover_max_endurance": recover_max_endurance,
        "varied_max_mp": max_mp,
        "varied_recov_hp": recov_hp,
        "varied_recov_mp": recov_mp,
        "varied_possessable_weight": weight,
        "socket_count": socket_count,
    }


def _lane_max(values: tuple[float, ...], stat: int) -> int:
    """The highest of a stat's three lanes, rounded; hybrids fill two lanes alike."""
    return round(max(values[stat * _LANES:(stat + 1) * _LANES]))


def _read_accuracy(reader: RecordReader) -> int:
    """Three (AP dice text, accuracy) pairs; the highest accuracy, rounded."""
    accuracy = 0.0
    for _ in range(_LANES):
        reader.text(wide=True)
        (value,) = reader.unpack(_F32)
        accuracy = max(accuracy, value)
    return round(accuracy)


def _defense_max(defense: list[tuple[float, ...]], stat: int) -> int:
    """The highest lane of one tail defense value, rounded."""
    return round(max(lane[stat] for lane in defense))


def _read_late_fields(reader: RecordReader, label: str) -> dict:
    """The 65 bytes after unknown_dice_accuracy_30, the aid items and the footer."""
    if reader.unpack(_UNKNOWN_DICE_ACCURACY_30_FIELD)[0] != _UNKNOWN_DICE_ACCURACY_30:
        raise ValueError(f"{label}: unknown_dice_accuracy_30 is not three -1 values")
    (life_main_type, life_sub_type, life_stat, group_level, new_perfect_item, new_perfect_count,
     new_perfect_loss, prevent_cron_count, adjust_strength, adjust_speed, adjust_health,
     max_food, cannon_cool_time, _cannon_accuracy, _cannon_max_length, _cannon_max_angle,
     ) = reader.unpack(_LATE_FIELDS)
    (count,) = reader.unpack(_U32)
    aids = list(reader.unpack(struct.Struct(f"<{count}I")))
    cronable, guild_rental, need_perfect_enchant_stack = reader.unpack(_FOOTER)
    if not reader.at_end():
        raise ValueError(f"{label}: {reader.remaining()} bytes left after the footer")
    return {
        "aid_item_ids": aids,
        "life_main_type": life_main_type,
        "life_sub_type": life_sub_type,
        "life_stat": life_stat,
        "group_level": group_level,
        "new_perfect_enchant_item_id": new_perfect_item,
        "new_perfect_enchant_item_count": new_perfect_count,
        "new_perfect_enchant_durability_loss": new_perfect_loss,
        "prevent_cron_count": prevent_cron_count,
        "adjust_strength": adjust_strength,
        "adjust_speed": adjust_speed,
        "adjust_health": adjust_health,
        "varied_max_food": max_food,
        "varied_cannon_cool_time": cannon_cool_time,
        "is_cronable": bool(cronable),
        "is_guild_rental": bool(guild_rental),
        "need_perfect_enchant_stack": need_perfect_enchant_stack,
    }


def _enhancement_fields(header: _Header, level: int, fail_result: int) -> dict:
    """What the attempt to reach `level` costs; all None on level 0, the base item."""
    if not level:
        return {
            "material_item_id": None,
            "material_count": None,
            "success_chance": None,
            "fail_result": None,
            "downgrade_chance": None,
            "fail_durability_loss": None,
            "perfect_count": None,
            "perfect_durability_loss": None,
        }
    has_perfect = header.perfect_count > 0
    return {
        "material_item_id": header.material_item_id,
        "material_count": header.material_count,
        "success_chance": header.success_rate / _RATE_PER_PERCENT,
        "fail_result": fail_result,
        # The chance a failure drops a level; 100 on nearly every downgrade attempt.
        "downgrade_chance": header.downgrade_rate / _RATE_PER_PERCENT,
        "fail_durability_loss": header.fail_durability_loss,
        # None sorts last and exports empty: no perfect enhancement.
        "perfect_count": header.perfect_count if has_perfect else None,
        "perfect_durability_loss": header.perfect_durability_loss if has_perfect else None,
    }


def _parse_block(data: bytes, start: int, size: int, enchant_key: int, level: int) -> dict:
    label = f"enchantstaticstatus block {enchant_key}/{level}"
    reader = RecordReader(data, start, start + size, label)
    header, stored = _read_header(reader, enchant_key, level)
    lane_stats = reader.unpack(_LANE_STATS)
    (skill_key,) = reader.unpack(_U32)
    description_kr = reader.text(wide=True)
    effects = reader.text(wide=True)
    (is_notify_world, fail_result, item_market_added_price, _unknown_after_script,
     market_filter_1, market_filter_2) = reader.unpack(_AFTER_SCRIPT)
    accuracy = _read_accuracy(reader)
    defense = [reader.unpack(_DEFENSE) for _ in range(_LANES)]
    late = _read_late_fields(reader, label)
    return {
        # The offset key, which names one level of one enchant key.
        "status_key": level << _LEVEL_SHIFT | enchant_key,
        "enchant_key": enchant_key,
        "level": level,
        **_enhancement_fields(header, level, fail_result),
        "max_durability": header.max_durability,
        "ap_min": _lane_max(lane_stats, _AP_MIN),
        "ap_max": _lane_max(lane_stats, _AP_MAX),
        "accuracy": accuracy,
        "evasion": _lane_max(lane_stats, _EVASION),
        "hidden_evasion": _defense_max(defense, _HIDDEN_EVASION),
        "damage_reduction": _defense_max(defense, _DAMAGE_REDUCTION),
        "hidden_damage_reduction": _defense_max(defense, _HIDDEN_DAMAGE_REDUCTION),
        # Ships and wagons show it as Max Durability, their HP.
        "max_hp": round(header.max_hp),
        "added_damage": _lane_max(lane_stats, _ADDED_DAMAGE),
        "effects": effects,
        "description_kr": description_kr,
        "skill_key": skill_key,
        "skill_no": skill_key >> _SKILL_NO_SHIFT,
        "is_notify_world": bool(is_notify_world),
        "item_market_added_price": item_market_added_price,
        "market_filter_1": market_filter_1,
        "market_filter_2": market_filter_2,
        **stored,
        **late,
    }


def parse_enchantstaticstatus_records(data: bytes, offset_data: bytes) -> list[dict]:
    """One record per block, sorted by enchant key, then level."""
    records = []
    for row in parse_enchantstaticstatusoffset_records(offset_data):
        records.append(_parse_block(
            data, row["data_offset"], row["data_size"], row["enchant_key"], row["level"],
        ))
    records.sort(key=lambda record: (record["enchant_key"], record["level"]))
    return records
