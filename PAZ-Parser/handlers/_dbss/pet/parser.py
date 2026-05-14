from __future__ import annotations

import struct


_OFFSET_HEADER_SIZE = 4
_PET_OFFSET_RECORD_SIZE = 10
_PET_HEADER_SIZE = 32
_PET_FOOTER_SIZE = 94
_PETGRADE_HEADER_SIZE = 4
_PETGRADE_RECORD_SIZE = 12
_PETGRADE_OFFSET_RECORD_SIZE = 12


def parse_petoffset_records(data: bytes) -> list[dict]:
    if len(data) < _OFFSET_HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    records: list[dict] = []

    for index in range(count):
        pos = _OFFSET_HEADER_SIZE + index * _PET_OFFSET_RECORD_SIZE
        if pos + _PET_OFFSET_RECORD_SIZE > len(data):
            break

        pet_id, data_offset, data_size, padding = struct.unpack_from("<HIHH", data, pos)
        records.append({
            "pet_id": pet_id,
            "data_offset": data_offset,
            "data_size": data_size,
            "padding": padding,
        })

    return records


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
    if len(data) < _PETGRADE_HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    records: list[dict] = []

    for index in range(count):
        pos = _PETGRADE_HEADER_SIZE + index * _PETGRADE_OFFSET_RECORD_SIZE
        if pos + _PETGRADE_OFFSET_RECORD_SIZE > len(data):
            break

        key, padding, data_offset, data_size = struct.unpack_from("<HHII", data, pos)
        variant = key & 0xFF
        species = key >> 8
        records.append({
            "key": key,
            "variant": variant,
            "species": species,
            "data_offset": data_offset,
            "data_size": data_size,
            "record_start": data_offset - 4,
            "padding": padding,
        })

    return records


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


def _parse_pet_payload(row: int, offset_record: dict, block: bytes, grade_map: dict[tuple[int, int], int]) -> dict:
    if len(block) < _PET_HEADER_SIZE + _PET_FOOTER_SIZE:
        raise ValueError(f"pet record {row} is too small")

    pet_id, variant, species, reserved_04, tier, reserved_06, max_level = struct.unpack_from("<HBBBBBB", block, 0)
    const_90000000 = struct.unpack_from("<I", block, 0x08)[0]
    reserved_0c = block[0x0C]
    reserved_0d = struct.unpack_from("<H", block, 0x0D)[0]
    equip_skill_slots = block[0x0F]
    reserved_10 = struct.unpack_from("<H", block, 0x10)[0]
    unknown_12 = block[0x12]
    reserved_13 = block[0x13]
    type_param = struct.unpack_from("<I", block, 0x14)[0]
    icon_path_len = struct.unpack_from("<I", block, 0x18)[0]
    reserved_1c = struct.unpack_from("<I", block, 0x1C)[0]

    icon_path = _read_icon_path(block, icon_path_len)
    footer_start = _PET_HEADER_SIZE + icon_path_len
    footer_end = footer_start + _PET_FOOTER_SIZE
    if footer_end > len(block):
        raise ValueError(f"pet record {row} footer exceeds record size")

    footer = block[footer_start:footer_end]
    constants = struct.unpack_from("<IIIIIIIII", footer, 0)
    acquire_type_id = struct.unpack_from("<H", footer, 0x24)[0]
    equip_skill_id = struct.unpack_from("<H", footer, 0x26)[0]
    upgrade_table = list(struct.unpack_from("<10I", footer, 0x2A))
    grade_score = footer[0x53]

    return {
        "row": row,
        "pet_id": pet_id,
        "pet_id_hex": f"0x{pet_id:04X}",
        "variant": variant,
        "species": species,
        "tier": tier,
        "max_level": max_level,
        "equip_skill_slots": equip_skill_slots,
        "type_param": type_param,
        "icon_path_len": icon_path_len,
        "icon_path": icon_path,
        "acquire_type_id": acquire_type_id,
        "equip_skill_id": equip_skill_id,
        "grade_score": grade_score,
        "grade": grade_map.get((species, variant)),
        "offset": offset_record["data_offset"],
        "size": offset_record["data_size"],
        "unknown_12": unknown_12,
        "upgrade_table": upgrade_table,
        "constants": constants,
        "reserved_04": reserved_04,
        "reserved_06": reserved_06,
        "reserved_0c": reserved_0c,
        "reserved_0d": reserved_0d,
        "reserved_10": reserved_10,
        "reserved_13": reserved_13,
        "reserved_1c": reserved_1c,
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
