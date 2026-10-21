"""`elementalmonsterstat.bss`: the Black Shrine bosses and the monsters of their fights.

    u32 count | count x row
    row: u16 character_key | u16 character_key_dup | u16 unlock_character_key
         | u32 unlock_mental_card_key | f32 offence_stat | f32 defence_stat
         | u8 element_type | u8 level | u8 group | u8 is_boss | u8 monster_part
         | u32 show_reward_count | show_reward_count x reward item
         | f32 position_x | f32 position_y | f32 position_z | f32 min_ap
    reward item: u32 item_key | 4 bytes padding | i64 count

No PABR magic. Full layout in docs/file-formats/elementalmonsterstat_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import whole_float
from _common.record_reader import RecordReader


FILE_NAME = "elementalmonsterstat.bss"

_COUNT = struct.Struct("<I")
_ROW_HEAD = struct.Struct("<HHHIffBBBBBI")
_ROW_TAIL = struct.Struct("<ffff")
_REWARD_ITEM = struct.Struct("<I4sq")


def read_reward_items(reader: RecordReader, count: int) -> list[dict]:
    """`count` Reward Items as `{item_key, count}`; the padding is left out.

    Shared with `elementalmonsterreward.bss`, which stores the same 16-byte item.
    """
    items: list[dict] = []
    for _ in range(count):
        item_key, _padding, item_count = reader.unpack(_REWARD_ITEM)
        items.append({"item_key": item_key, "count": item_count})
    return items


def _read_row(reader: RecordReader) -> dict:
    (
        character_key, character_key_dup, unlock_character_key, unlock_mental_card_key,
        offence_stat, defence_stat, element_type, level, group, is_boss, monster_part,
        show_reward_count,
    ) = reader.unpack(_ROW_HEAD)
    show_rewards = read_reward_items(reader, show_reward_count)
    position_x, position_y, position_z, min_ap = reader.unpack(_ROW_TAIL)
    return {
        "character_key": character_key,
        "character_key_dup": character_key_dup,
        "unlock_character_key": unlock_character_key,
        "unlock_mental_card_key": unlock_mental_card_key,
        "offence_stat": whole_float(offence_stat),
        "defence_stat": whole_float(defence_stat),
        "element_type": element_type,
        "level": level,
        "group": group,
        "is_boss": bool(is_boss),
        "monster_part": monster_part,
        "show_reward_count": show_reward_count,
        "show_rewards": show_rewards,
        "position_x": position_x,
        "position_y": position_y,
        "position_z": position_z,
        "min_ap": whole_float(min_ap),
    }


def parse_elementalmonsterstat_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when a row runs past the file or the rows do not end
    at the end of the file.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    (count,) = reader.unpack(_COUNT)
    records = [_read_row(reader) for _ in range(count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME}: {reader.remaining():,} bytes left after {count:,} rows")
    return records


def boss_difficulties(data: bytes) -> dict[int, tuple[int, int]]:
    """Boss character key -> (monster_part, level), for the tables keyed by boss.

    Raises ValueError as `parse_elementalmonsterstat_records` does.
    """
    return {
        r["character_key"]: (r["monster_part"], r["level"])
        for r in parse_elementalmonsterstat_records(data)
        if r["is_boss"]
    }
