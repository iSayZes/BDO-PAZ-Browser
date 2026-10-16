"""`skillsimply.dbss`: the learning rules of every skill rank.

`skillsimplyoffset.dbss` (bare u32 rows, no magic) maps each skill key to its
record. A record, in order:

    u32 skill_key | u32 level_1_key | u32 kind | u8 branch | u8
    | u32 n + n x u32 unknown_hashes
    | u8 | u32 need_level | u16 previous_rank_no
    | u32 n + n x u32 next_rank_keys
    | u8 weapon_type | u8 uses_main_weapon | u8 uses_sub_weapon | u8[15]
    | u32 first_rank_key | u8 is_fusion | u8[2] | u8 can_quick_slot | u8[2]
    | u64 class_mask
    | u16 + u16 need_skill_no_1 | u16 + u16 need_skill_no_2 | u8[8]
    | u16 need_skill_point | u8[4]
    | u64 n + n x u16 exclusive_skill_nos
    | u8[10] | u32 n + n x u32 base_skill_keys | u8

Full layout in docs/file-formats/skillsimply_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader
from _common.skill import split_skill_key

_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
# skill_key, level_1_key, kind, branch, then unknown_0d.
_HEAD = struct.Struct("<IIIBx")
# unknown_h00, need_level, previous_rank_no.
_RANK = struct.Struct("<BIH")
# weapon_type, uses_main_weapon, uses_sub_weapon, then 15 bytes up to first_rank_key.
_WEAPON = struct.Struct("<BBB15x")
# first_rank_key, is_fusion, two unknown bytes, can_quick_slot, two unknown bytes, class_mask.
_CLASS = struct.Struct("<IB2xB2xQ")
# Two (has_need_skill, need_skill_no) pairs, eight zero bytes, need_skill_point, four zero bytes.
_NEEDS = struct.Struct("<2xH2xH8xH4x")
_BEFORE_BASE_SKILLS_SIZE = 10
_END_MARKER_SIZE = 1


@dataclass(frozen=True)
class SkillSimplyRecord:
    skill_key: int
    kind: int
    branch: int
    need_level: int
    previous_rank_no: int
    next_rank_keys: tuple[int, ...]
    weapon_type: int
    uses_main_weapon: bool
    uses_sub_weapon: bool
    first_rank_key: int
    is_fusion: bool
    can_quick_slot: bool
    class_mask: int
    need_skill_nos: tuple[int, ...]
    need_skill_point: int
    exclusive_skill_nos: tuple[int, ...]
    base_skill_keys: tuple[int, ...]

    @property
    def skill_no(self) -> int:
        return split_skill_key(self.skill_key)[0]

    @property
    def level(self) -> int:
        return split_skill_key(self.skill_key)[1]


def _list(reader: RecordReader, count_fmt: struct.Struct, item_code: str) -> tuple[int, ...]:
    (count,) = reader.unpack(count_fmt)
    return reader.unpack(struct.Struct(f"<{count}{item_code}"))


def parse_skillsimply_record(data: bytes, row: PabrOffsetRow) -> SkillSimplyRecord:
    """Walk one record. Raises ValueError when it does not end at its index size."""
    label = f"skill simply 0x{row.entry_id:08X}"
    reader = RecordReader(data, row.offset, row.offset + row.size, label)
    key, _level_1_key, kind, branch = reader.unpack(_HEAD)
    if key != row.entry_id:
        raise ValueError(f"record at 0x{row.offset:X} holds key 0x{key:08X}, index says 0x{row.entry_id:08X}")

    _list(reader, _U32, "I")  # unknown_hashes
    _unknown_h00, need_level, previous_rank_no = reader.unpack(_RANK)
    next_rank_keys = _list(reader, _U32, "I")
    weapon_type, uses_main_weapon, uses_sub_weapon = reader.unpack(_WEAPON)
    first_rank_key, is_fusion, can_quick_slot, class_mask = reader.unpack(_CLASS)
    need_skill_no_1, need_skill_no_2, need_skill_point = reader.unpack(_NEEDS)
    exclusive_skill_nos = _list(reader, _U64, "H")
    reader.skip(_BEFORE_BASE_SKILLS_SIZE)
    base_skill_keys = _list(reader, _U32, "I")
    reader.skip(_END_MARKER_SIZE)
    if not reader.at_end():
        raise ValueError(f"{label} ends {reader.remaining()} bytes before its index size")

    return SkillSimplyRecord(
        skill_key=key,
        kind=kind,
        branch=branch,
        need_level=need_level,
        previous_rank_no=previous_rank_no,
        next_rank_keys=next_rank_keys,
        weapon_type=weapon_type,
        uses_main_weapon=bool(uses_main_weapon),
        uses_sub_weapon=bool(uses_sub_weapon),
        first_rank_key=first_rank_key,
        is_fusion=bool(is_fusion),
        can_quick_slot=bool(can_quick_slot),
        class_mask=class_mask,
        # Zero means no required skill.
        need_skill_nos=tuple(no for no in (need_skill_no_1, need_skill_no_2) if no),
        need_skill_point=need_skill_point,
        exclusive_skill_nos=exclusive_skill_nos,
        base_skill_keys=base_skill_keys,
    )


def parse_skillsimply_offset_rows(offset_data: bytes) -> list[PabrOffsetRow]:
    """`skillsimplyoffset.dbss`: a u32 count, then u32 key, offset and size rows."""
    return parse_bare_u32_offset_rows(offset_data)


def parse_skillsimply_records(data: bytes, offset_data: bytes) -> list[SkillSimplyRecord]:
    """One record per index row, in index order.

    Raises ValueError on the first record that does not end exactly at its
    index size: the layout has changed and later fields would be misread.
    """
    return [parse_skillsimply_record(data, row) for row in parse_skillsimply_offset_rows(offset_data)]
