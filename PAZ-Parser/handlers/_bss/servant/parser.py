"""`servant.bss`: base data of every servant, one variable-size record per character.

    u32 count | count x Row, back to back up to EOF

A row holds the Korean dev name, servant kind, tier, grade, coat colors,
breeding count, lifespan, prices, flags and two u8 lists of
`vehicleskill.dbss` keys (the skills the servant starts with, and the
stallion skills). Layout 2 in docs/file-formats/bss/servant_bss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader


FILE_NAME = "servant.bss"

_COUNT = struct.Struct("<I")
_IDS = struct.Struct("<HH")
# u8 servant_kind | u8 servant_kind_sub | u16 tier | u16 grade | u16 color1..3
# | u8 mating_count | u32 lifespan | i64 base_price | i64 price_per_level
# | u8 is_male | u8 is_display_gender | u8 servant_main_model
# | u8 is_mating_result | u8 is_trade | u8 link_count
# | i32 experience_per_one | u16 form_index | u8 basic_learn_skill_max_count
# | u32 basic_learn_skill_count
_BODY = struct.Struct("<BBHHHHHBIqqBBBBBBiHBI")
_BODY_FIELDS = (
    "servant_kind",
    "servant_kind_sub",
    "tier",
    "grade",
    "color1",
    "color2",
    "color3",
    "mating_count",
    "lifespan",
    "base_price",
    "price_per_level",
    "is_male",
    "is_display_gender",
    "servant_main_model",
    "is_mating_result",
    "is_trade",
    "link_count",
    "experience_per_one",
    "form_index",
    "basic_learn_skill_max_count",
    "basic_learn_skill_count",
)
assert len(_BODY_FIELDS) == len(_BODY.format) - 1
# bytes[5] unknown | u32 reward_money_percent | u8 is_only_pcroom | u32 stallion_skill_count
_MIDDLE = struct.Struct("<5sIBI")
# u8 can_mix | u8 can_mating | bytes[2] unknown
_TAIL = struct.Struct("<BB2s")


def _skill_keys(reader: RecordReader, count: int) -> list[int]:
    return list(reader.unpack(struct.Struct(f"<{count}B")))


def _parse_row(reader: RecordReader, index: int) -> dict:
    character_id, character_id_dup = reader.unpack(_IDS)
    if character_id_dup != character_id:
        raise ValueError(
            f"{FILE_NAME} row {index} at 0x{reader.pos - _IDS.size:X} repeats "
            f"character {character_id_dup}, expected {character_id}"
        )
    name_kr = reader.text(wide=True)
    body = dict(zip(_BODY_FIELDS, reader.unpack(_BODY), strict=True))
    basic_keys = _skill_keys(reader, body["basic_learn_skill_count"])
    unknown_basic_00, reward_money_percent, is_only_pcroom, stallion_count = reader.unpack(_MIDDLE)
    stallion_keys = _skill_keys(reader, stallion_count)
    can_mix, can_mating, unknown_stallion_02 = reader.unpack(_TAIL)
    return {
        "character_id": character_id,
        "name_kr": name_kr,
        **body,
        "basic_learn_skill_keys": basic_keys,
        "unknown_basic_learn_skill_keys_00": unknown_basic_00.hex(),
        "reward_money_percent": reward_money_percent,
        "is_only_pcroom": is_only_pcroom,
        "stallion_skill_count": stallion_count,
        "stallion_skill_keys": stallion_keys,
        "can_mix": can_mix,
        "can_mating": can_mating,
        "unknown_stallion_skill_keys_02": unknown_stallion_02.hex(),
    }


def parse_servant_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when a row runs past the file, a row's
    `character_id_dup` differs from its `character_id`, or bytes follow the
    last declared row.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    (count,) = reader.unpack(_COUNT)
    records = [_parse_row(reader, index) for index in range(count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME}: {reader.remaining():,} bytes follow row {count}")
    return records
