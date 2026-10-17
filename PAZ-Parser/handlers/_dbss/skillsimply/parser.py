"""`skillsimply.dbss`: the learning rules of every skill rank.

`skillsimplyoffset.dbss` (bare u32 rows, no magic) maps each skill key to its
record. A record, in order:

    u32 skill_key | u32 level_1_key | u32 kind | u8 branch | u8
    | u32 n + n x u32 contents_group_hashes
    | u8 | u32 need_level | u16 previous_rank_no
    | u32 n + n x u32 next_rank_keys
    | u8 require_equip_type | u8 uses_main_weapon | u8 uses_sub_weapon | u8[4]
    | u8 require_equip_slot | u8 | u8[4] | u32 skill_owner_type | u8
    | u32 first_rank_key | u8 is_fusion | u8 condition | u8 | u8 can_quick_slot
    | u16 max_level | u64 class_mask
    | u16 need_skill_level_1 + u16 need_skill_no_1 | u16 + u16 need_skill_no_2 | u8[8]
    | u16 need_skill_point | u8[4]
    | u64 n + n x u16 exclusive_skill_nos
    | u8[9] | u8 is_except_cool_time | u32 n + n x u32 base_skill_keys | u8 need_buff_module_type

Full layout and the sheet columns behind the names in
docs/file-formats/skillsimply_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from functools import cache

from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader
from _common.skill import split_skill_key
from _common.string_hash import key_hash

_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
# skill_key, level_1_key, kind, branch, then unknown_0d.
_HEAD = struct.Struct("<IIIBx")
# unknown_h00, need_level, previous_rank_no.
_RANK = struct.Struct("<BIH")
# A copy of the 9-byte item equip type (require_equip_type, its weapon and
# sub-weapon flags, four unknown bytes, require_equip_slot, one unknown byte),
# then four zero bytes, skill_owner_type and unknown_n11.
_EQUIP = struct.Struct("<BBB4xBx4xIx")
# first_rank_key, is_fusion, condition, a zero byte, can_quick_slot, max_level, class_mask.
_CLASS = struct.Struct("<IBBxBHQ")
# Two (need_skill_level, need_skill_no) pairs, eight zero bytes, need_skill_point, four zero bytes.
_NEEDS = struct.Struct("<2xH2xH8xH4x")
# Eight zero bytes and unknown_e08, then is_except_cool_time.
_COOL_TIME = struct.Struct("<9xB")
_NEED_BUFF_MODULE = struct.Struct("<B")

# Contents group keys are 16-bit (2016 `KeyType<short>`); the record stores
# key_hash() of each key's decimal text.
_CONTENTS_GROUP_KEY_COUNT = 0x8000


@cache
def _contents_group_keys_by_hash() -> dict[int, int]:
    return {key_hash(str(key)): key for key in range(_CONTENTS_GROUP_KEY_COUNT)}


def contents_group_key(stored_hash: int) -> int | None:
    """The contents group key whose decimal text hashes to `stored_hash`, or None."""
    return _contents_group_keys_by_hash().get(stored_hash)


@dataclass(frozen=True)
class SkillSimplyRecord:
    skill_key: int
    kind: int
    branch: int
    contents_group_hashes: tuple[int, ...]
    need_level: int
    previous_rank_no: int
    next_rank_keys: tuple[int, ...]
    require_equip_type: int
    uses_main_weapon: bool
    uses_sub_weapon: bool
    require_equip_slot: int
    skill_owner_type: int
    first_rank_key: int
    is_fusion: bool
    condition: bool
    can_quick_slot: bool
    max_level: int
    class_mask: int
    need_skill_nos: tuple[int, ...]
    need_skill_point: int
    exclusive_skill_nos: tuple[int, ...]
    is_except_cool_time: bool
    base_skill_keys: tuple[int, ...]
    need_buff_module_type: int

    @property
    def skill_no(self) -> int:
        return split_skill_key(self.skill_key)[0]

    @property
    def level(self) -> int:
        return split_skill_key(self.skill_key)[1]

    @property
    def contents_group_keys(self) -> tuple[int | None, ...]:
        """The decoded `contents_group_hashes`; None for a hash no 16-bit key gives."""
        return tuple(contents_group_key(stored_hash) for stored_hash in self.contents_group_hashes)


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

    contents_group_hashes = _list(reader, _U32, "I")
    _unknown_h00, need_level, previous_rank_no = reader.unpack(_RANK)
    next_rank_keys = _list(reader, _U32, "I")
    require_equip_type, uses_main_weapon, uses_sub_weapon, require_equip_slot, skill_owner_type = reader.unpack(_EQUIP)
    first_rank_key, is_fusion, condition, can_quick_slot, max_level, class_mask = reader.unpack(_CLASS)
    need_skill_no_1, need_skill_no_2, need_skill_point = reader.unpack(_NEEDS)
    exclusive_skill_nos = _list(reader, _U64, "H")
    (is_except_cool_time,) = reader.unpack(_COOL_TIME)
    base_skill_keys = _list(reader, _U32, "I")
    (need_buff_module_type,) = reader.unpack(_NEED_BUFF_MODULE)
    if not reader.at_end():
        raise ValueError(f"{label} ends {reader.remaining()} bytes before its index size")

    return SkillSimplyRecord(
        skill_key=key,
        kind=kind,
        branch=branch,
        contents_group_hashes=contents_group_hashes,
        need_level=need_level,
        previous_rank_no=previous_rank_no,
        next_rank_keys=next_rank_keys,
        require_equip_type=require_equip_type,
        uses_main_weapon=bool(uses_main_weapon),
        uses_sub_weapon=bool(uses_sub_weapon),
        require_equip_slot=require_equip_slot,
        skill_owner_type=skill_owner_type,
        first_rank_key=first_rank_key,
        is_fusion=bool(is_fusion),
        condition=bool(condition),
        can_quick_slot=bool(can_quick_slot),
        max_level=max_level,
        class_mask=class_mask,
        # Zero means no required skill.
        need_skill_nos=tuple(no for no in (need_skill_no_1, need_skill_no_2) if no),
        need_skill_point=need_skill_point,
        exclusive_skill_nos=exclusive_skill_nos,
        is_except_cool_time=bool(is_except_cool_time),
        base_skill_keys=base_skill_keys,
        need_buff_module_type=need_buff_module_type,
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
