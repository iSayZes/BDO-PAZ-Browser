"""`skillgroup.bss`: the rank chains of player skills.

No magic and no trailer: a u32 group count, then groups back to back to the
end of the file:

    u16 group_no | u32 rank_count | rank_count x u32 skill_key

Rank 0 is always `0` (not learned); the rest are `skill.dbss` keys in rank
order. Full layout in docs/file-formats/bss/skillgroup_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

_U32 = struct.Struct("<I")
_GROUP_HEADER = struct.Struct("<HI")
_KEY_SIZE = 4


@dataclass(frozen=True)
class SkillGroup:
    group_no: int
    # Rank 1 onward; the unlearned rank-0 entry is dropped.
    skill_keys: tuple[int, ...]


def parse_skillgroup_records(data: bytes) -> list[SkillGroup]:
    """Every group in file order.

    Raises ValueError when a group runs past the file or the walk does not end
    exactly at end of file, since the layout would then have changed.
    """
    (count,) = _U32.unpack_from(data, 0)
    pos = _U32.size
    groups: list[SkillGroup] = []
    for _ in range(count):
        if pos + _GROUP_HEADER.size > len(data):
            raise ValueError(f"skill group header at 0x{pos:X} runs past the file")
        group_no, rank_count = _GROUP_HEADER.unpack_from(data, pos)
        pos += _GROUP_HEADER.size
        end = pos + rank_count * _KEY_SIZE
        if end > len(data):
            raise ValueError(f"skill group {group_no} runs past the file")
        keys = struct.unpack_from(f"<{rank_count}I", data, pos)
        groups.append(SkillGroup(group_no=group_no, skill_keys=keys[1:]))
        pos = end
    if pos != len(data):
        raise ValueError(f"skill groups end at 0x{pos:X}, {len(data) - pos} bytes before end of file")
    return groups


def skill_keys_by_group(data: bytes) -> dict[int, tuple[int, ...]]:
    """Rank keys (rank 1 onward) by group number."""
    return {group.group_no: group.skill_keys for group in parse_skillgroup_records(data)}
