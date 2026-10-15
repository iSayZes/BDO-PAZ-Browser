from __future__ import annotations

import struct

from _common.pabr_offset import parse_bare_offset_rows, parse_bare_u32_offset_rows


_PET_HEADER_SIZE = 32
_PET_FOOTER_SIZE = 94
_PETGRADE_HEADER_SIZE = 4
_PETGRADE_RECORD_SIZE = 12
# Each petgrade.dbss offset points past the record's 4-byte key prefix.
_PETGRADE_KEY_PREFIX_SIZE = 4


def parse_petoffset_records(data: bytes) -> list[dict]:
    """The offset rows; the u16 size and the zero u16 after it read as one u32."""
    return [
        {"pet_id": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_offset_rows(data)
    ]


def parse_petgrade_records(data: bytes) -> list[dict]:
    if len(data) < _PETGRADE_HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    records: list[dict] = []

    for index in range(count):
        pos = _PETGRADE_HEADER_SIZE + index * _PETGRADE_RECORD_SIZE
        if pos + _PETGRADE_RECORD_SIZE > len(data):
            break

        key, padding, key_dup, padding_dup, grade = struct.unpack_from("<HHHHI", data, pos)
        variant = key & 0xFF
        species = key >> 8
        records.append({
            "key": key,
            "variant": variant,
            "species": species,
            "key_dup": key_dup,
            "grade": grade,
            "padding": padding,
            "padding_dup": padding_dup,
        })

    return records


def parse_petgradeoffset_records(data: bytes) -> list[dict]:
    """The offset rows; the u16 key and the zero u16 after it read as one u32."""
    return [
        {
            "key": row.entry_id,
            "variant": row.entry_id & 0xFF,
            "species": row.entry_id >> 8,
            "data_offset": row.offset,
            "data_size": row.size,
            "record_start": row.offset - _PETGRADE_KEY_PREFIX_SIZE,
        }
        for row in parse_bare_u32_offset_rows(data)
    ]


def parse_petgrade_records_with_offsets(data: bytes, offset_data: bytes) -> list[dict]:
    records: list[dict] = []
    offsets = parse_petgradeoffset_records(offset_data)

    for row, offset_record in enumerate(offsets):
        record_start = offset_record["record_start"]
        data_offset = offset_record["data_offset"]
        data_size = offset_record["data_size"]
        if record_start < _PETGRADE_HEADER_SIZE or data_offset + data_size > len(data):
            raise ValueError(f"pet grade record {row} exceeds file size")

        key, padding, key_dup, padding_dup, grade = struct.unpack_from("<HHHHI", data, record_start)
        variant = key & 0xFF
        species = key >> 8
        records.append({
            "key": key,
            "variant": variant,
            "species": species,
            "key_dup": key_dup,
            "grade": grade,
            "data_offset": data_offset,
            "data_size": data_size,
            "record_start": record_start,
            "offset_key": offset_record["key"],
            "key_match": key == key_dup == offset_record["key"],
            "padding": padding,
            "padding_dup": padding_dup,
        })

    return records


def build_petgrade_map(data: bytes | None) -> dict[tuple[int, int], int]:
    if data is None:
        return {}

    return {
        (record["species"], record["variant"]): record["grade"]
        for record in parse_petgrade_records(data)
    }


def _read_icon_path(block: bytes, icon_len: int) -> str:
    start = _PET_HEADER_SIZE
    end = start + icon_len
    if end > len(block):
        raise ValueError("pet record icon path exceeds record size")
    return block[start:end].decode("ascii", errors="replace")


def _parse_pet_header(block: bytes) -> dict:
    """The 32 bytes before the icon path; names follow the Pet_Table sheet (see the doc)."""
    pet_id, variant, species, reserved_04, tier, reserved_06 = struct.unpack_from("<HBBBBB", block, 0)
    max_level, max_hunger, exp_key, is_indexed, default_action_index, change_look_key, icon_path_len = (
        struct.unpack_from("<iiHBIHQ", block, 0x07)
    )
    return {
        "pet_id": pet_id,
        "pet_id_hex": f"0x{pet_id:04X}",
        "variant": variant,
        "species": species,
        "tier": tier,
        "max_level": max_level,
        "max_hunger": max_hunger,
        "exp_key": exp_key,
        "is_indexed": bool(is_indexed),
        "default_action_index": default_action_index,
        "change_look_key": change_look_key,
        "icon_path_len": icon_path_len,
        "reserved_04": reserved_04,
        "reserved_06": reserved_06,
    }


def _parse_pet_footer(footer: bytes) -> dict:
    """The 94 bytes after the icon path; names follow the Pet_Table sheet (see the doc)."""
    base_price, min_price, max_price, minest_percent, maxest_percent, skill_max_count = (
        struct.unpack_from("<qqqiiI", footer, 0x00)
    )
    acquire_type_id, base_skill_id = struct.unpack_from("<HH", footer, 0x24)
    pet_type, loot_skill_id, race_skill_id, unknown_57, is_joker_pet_use, pc_room_type = (
        struct.unpack_from("<BHHBBB", footer, 0x52)
    )
    return {
        "base_price_for_pet_market": base_price,
        "min_price_for_pet_market": min_price,
        "max_price_for_pet_market": max_price,
        "minest_percent_for_pet_market": minest_percent,
        "maxest_percent_for_pet_market": maxest_percent,
        "skill_max_count": skill_max_count,
        "acquire_type_id": acquire_type_id,
        "base_skill_id": base_skill_id,
        "action_rates": list(struct.unpack_from("<10i", footer, 0x2A)),
        "pet_type": pet_type,
        "loot_skill_id": loot_skill_id,
        "race_skill_id": race_skill_id,
        "unknown_57": unknown_57,
        "is_joker_pet_use": bool(is_joker_pet_use),
        "pc_room_type": pc_room_type,
    }


def _parse_pet_payload(row: int, offset_record: dict, block: bytes, grade_map: dict[tuple[int, int], int]) -> dict:
    if len(block) < _PET_HEADER_SIZE + _PET_FOOTER_SIZE:
        raise ValueError(f"pet record {row} is too small")

    header = _parse_pet_header(block)
    icon_path_len = header["icon_path_len"]
    icon_path = _read_icon_path(block, icon_path_len)
    footer_start = _PET_HEADER_SIZE + icon_path_len
    footer_end = footer_start + _PET_FOOTER_SIZE
    if footer_end > len(block):
        raise ValueError(f"pet record {row} footer exceeds record size")

    return {
        "row": row,
        **header,
        "icon_path": icon_path,
        **_parse_pet_footer(block[footer_start:footer_end]),
        "grade": grade_map.get((header["species"], header["variant"])),
        "offset": offset_record["data_offset"],
        "size": offset_record["data_size"],
    }


def parse_pet_records(data: bytes, offset_data: bytes, grade_data: bytes | None = None) -> list[dict]:
    records: list[dict] = []
    offsets = parse_petoffset_records(offset_data)
    grade_map = build_petgrade_map(grade_data)

    for row, offset_record in enumerate(offsets):
        data_offset = offset_record["data_offset"]
        data_size = offset_record["data_size"]
        prefix_offset = data_offset - 2
        if prefix_offset < 0 or data_offset + data_size > len(data):
            raise ValueError(f"pet record {row} exceeds file size")

        prefix_pet_id = struct.unpack_from("<H", data, prefix_offset)[0]
        block = data[data_offset:data_offset + data_size]
        record = _parse_pet_payload(row, offset_record, block, grade_map)
        record["prefix_pet_id"] = prefix_pet_id
        record["pet_id_match"] = prefix_pet_id == record["pet_id"] == offset_record["pet_id"]
        records.append(record)

    return sorted(records, key=lambda record: record["pet_id"])
