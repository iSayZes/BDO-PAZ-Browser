from __future__ import annotations

from _common.binary import u16, u32


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_RECORD_START = 8
_RECORD_SIZE = 0x38
_EXTRA_SIZE = 0x10
_TRAILER_SIZE = 8


def _read_utf16le_string_table(data: bytes, offset: int) -> list[str]:
    if offset + 4 > len(data):
        return []

    count = u32(data, offset)
    pos = offset + 4
    strings: list[str] = []

    for _ in range(count):
        if pos + 5 > len(data):
            break

        present = data[pos]
        size = u32(data, pos + 1)
        pos += 5
        end = pos + size
        if end > len(data):
            break

        raw = data[pos:end]
        pos = end
        if not present:
            strings.append("")
            continue

        strings.append(raw.decode("utf-16-le", errors="replace").rstrip("\x00"))

    return strings


def _string_at(strings: list[str], index: int) -> str:
    if 0 <= index < len(strings):
        return strings[index]
    return ""


def parse_plantworkerpassiveskill_records(data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE + _TRAILER_SIZE:
        return []

    if data[:4] != _MAGIC:
        raise ValueError("plantworkerpassiveskill.bss has invalid magic.")

    count = u32(data, 4)
    string_table_start = u32(data, len(data) - _TRAILER_SIZE)
    if (
        string_table_start < _RECORD_START
        or string_table_start > len(data) - _TRAILER_SIZE
    ):
        string_table_start = len(data) - _TRAILER_SIZE

    strings = _read_utf16le_string_table(data, string_table_start)

    records: list[dict] = []
    pos = _RECORD_START
    for slot in range(count):
        if pos + _RECORD_SIZE > string_table_start:
            break

        skill_id = u16(data, pos)
        name_index = u32(data, pos + 0x04)
        icon_index = u32(data, pos + 0x08)
        description_index = u32(data, pos + 0x0C)

        record = {
            "slot": slot,
            "skill_id": skill_id,
            "duplicate_skill_id": u16(data, pos + 0x02),
            "name_index": name_index,
            "icon_index": icon_index,
            "description_index": description_index,
            "inline_name": _string_at(strings, name_index),
            "icon_path": _string_at(strings, icon_index),
            "inline_description": _string_at(strings, description_index),
            "acquisition_weight": u32(data, pos + 0x10),
            "zero_a": u32(data, pos + 0x14),
            "effect_type": u32(data, pos + 0x18),
            "apply_mode": u32(data, pos + 0x1C),
            "apply_scope": u32(data, pos + 0x20),
            "effect_type_copy": u32(data, pos + 0x24),
            "effect_target": u32(data, pos + 0x28),
            "effect_value_a": u32(data, pos + 0x2C),
            "effect_value_b": u32(data, pos + 0x30),
            "zero_b": u32(data, pos + 0x34),
            "extra_zero_a": None,
            "extra_effect_value_a": None,
            "extra_effect_value_b": None,
            "extra_zero_b": None,
        }

        pos += _RECORD_SIZE

        remaining_records = count - slot - 1
        expected_remaining = remaining_records * _RECORD_SIZE
        extra_remaining = string_table_start - pos - expected_remaining
        if (
            skill_id == 1012
            and extra_remaining >= _EXTRA_SIZE
            and pos + _EXTRA_SIZE <= string_table_start
        ):
            record["extra_zero_a"] = u32(data, pos)
            record["extra_effect_value_a"] = u32(data, pos + 0x04)
            record["extra_effect_value_b"] = u32(data, pos + 0x08)
            record["extra_zero_b"] = u32(data, pos + 0x0C)
            pos += _EXTRA_SIZE

        records.append(record)

    return records
