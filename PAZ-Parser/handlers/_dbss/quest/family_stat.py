"""Permanent Family stats of a quest's base rewards, from each entry's Family Stat Union.

The union is `family_stat` of a Reward Entry: a u32 `family_stat_type`, then
the byte-packed field of every type. "Family Stat Union" in
docs/file-formats/dbss/quest_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.quest.reward_entry import RewardEntry
from .model import FamilyStat


_I32 = struct.Struct("<i")
_F32 = struct.Struct("<f")

_NO_FAMILY_STAT = 16
# Weight is stored in 1/10,000 LT.
_WEIGHT_TYPE = 5
_WEIGHT_PER_LT = 10_000

# family_stat_type -> (label, union offset, reader). Types 12 and 13 only occur
# in test quests and their field widths are unconfirmed, so they stay unnamed.
_FAMILY_STAT_FIELDS: dict[int, tuple[str, int, struct.Struct | None]] = {
    0: ("AP", 0x04, _F32),
    1: ("DP", 0x08, _F32),
    2: ("HP", 0x0C, _F32),
    3: ("MP", 0x10, _F32),
    4: ("Stamina", 0x14, _I32),
    5: ("Weight", 0x18, _I32),
    6: ("Inventory", 0x1C, None),
    7: ("Accuracy", 0x1D, _F32),
    8: ("Evasion", 0x21, _F32),
    9: ("Enhancement Chance", 0x25, _I32),
    10: ("Valks Limit", 0x29, _I32),
    11: ("Stack Limit", 0x2D, _I32),
}


def _family_stat_value(union: bytes, stat_type: int) -> float | None:
    field = _FAMILY_STAT_FIELDS.get(stat_type)
    if field is None:
        return None
    _label, offset, reader = field
    if reader is None:
        return union[offset]
    value = reader.unpack_from(union, offset)[0]
    return value / _WEIGHT_PER_LT if stat_type == _WEIGHT_TYPE else value


def family_stats(base_rewards: list[RewardEntry]) -> list[FamilyStat]:
    """Family stats granted by the base reward entries (type 16 is none)."""
    stats: list[FamilyStat] = []
    for entry, reward in enumerate(base_rewards):
        union = bytes.fromhex(reward["family_stat"])
        stat_type = u32(union, 0)
        if stat_type == _NO_FAMILY_STAT:
            continue
        label = _FAMILY_STAT_FIELDS.get(stat_type, (f"Type {stat_type}", 0, None))[0]
        stats.append({
            "entry": entry,
            "type": stat_type,
            "label": label,
            "value": _family_stat_value(union, stat_type),
        })
    return stats
