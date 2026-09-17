"""Shared parsing for the pet/fairy equip-skill roll tables.

`petequipskillaquire.dbss` and `fairyequipskillaquire.dbss` share one layout: a
keyed record holding a flat array of roll weights, indexed by the
`equip_skill_id` of the matching equip-skill catalog. A weight of `0` means that
skill cannot be rolled by that acquire type.
"""

from __future__ import annotations

import struct


HEADER_SIZE = 4
OFFSET_RECORD_SIZE = 10
KEY_PREFIX_SIZE = 2
RECORD_SIZE = 176
DATA_SIZE = RECORD_SIZE - KEY_PREFIX_SIZE

# 4-byte packed key followed by 43 u32 weights fills the 176-byte record.
WEIGHT_TABLE_OFFSET = 4
WEIGHT_COUNT = 43

# Fairy tables normalise to this total; pet tables do not (see format docs).
PPM_SCALE = 1_000_000

# Catalog records are 12 bytes from +0x04: [u32 id][u32 type][u8 tier][u8 pad][u16 loc_id].
_CATALOG_START = 4
_CATALOG_RECORD_SIZE = 12
_CATALOG_NULL_ID = 200


def parse_roll_offset_records(data: bytes, label: str) -> list[dict]:
    """Parse an `*aquireoffset.dbss` index."""
    if len(data) < HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    records: list[dict] = []

    for index in range(count):
        pos = HEADER_SIZE + index * OFFSET_RECORD_SIZE
        if pos + OFFSET_RECORD_SIZE > len(data):
            break

        acquire_type_id, data_offset, data_size, padding = struct.unpack_from(
            "<HIHH", data, pos
        )
        records.append({
            "source_index": index,
            "acquire_type_id": acquire_type_id,
            "data_offset": data_offset,
            "data_size": data_size,
            "record_start": data_offset - KEY_PREFIX_SIZE,
            "padding": padding,
        })

    return records


def parse_roll_records(data: bytes, offset_data: bytes, label: str) -> list[dict]:
    """Parse an `*aquire.dbss` weight table, using its offset companion for seeks."""
    if len(data) < HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    offsets = parse_roll_offset_records(offset_data, label)
    if len(offsets) != count:
        raise ValueError(
            f"{label} count mismatch: main has {count}, offset has {len(offsets)}"
        )

    records: list[dict] = []
    for offset_record in offsets:
        source_index = offset_record["source_index"]
        data_offset = offset_record["data_offset"]
        data_size = offset_record["data_size"]
        record_start = offset_record["record_start"]

        if data_size != DATA_SIZE:
            raise ValueError(
                f"{label} record {source_index} has unexpected size {data_size}"
            )
        if record_start < HEADER_SIZE or data_offset + data_size > len(data):
            raise ValueError(f"{label} record {source_index} exceeds file size")

        weights = list(
            struct.unpack_from(
                f"<{WEIGHT_COUNT}I", data, record_start + WEIGHT_TABLE_OFFSET
            )
        )
        total_weight = sum(weights)

        records.append({
            "source_index": source_index,
            "acquire_type_id": offset_record["acquire_type_id"],
            "packed_key": struct.unpack_from("<I", data, record_start)[0],
            "weights": weights,
            "total_weight": total_weight,
            "rollable_count": sum(1 for weight in weights if weight),
            "is_normalized": total_weight == PPM_SCALE,
            "data_offset": data_offset,
            "data_size": data_size,
            "record_start": record_start,
        })

    return records


def read_skill_loc_ids(catalog_data: bytes, max_records: int = WEIGHT_COUNT) -> dict[int, int]:
    """Map `equip_skill_id -> loc_id` from an equip-skill catalog (`*equipskill.bss`).

    Reads the leading fixed-stride section only, which is the portion the roll
    weights index. Stops early at the catalog's null sentinel.
    """
    loc_ids: dict[int, int] = {}

    for index in range(max_records):
        pos = _CATALOG_START + index * _CATALOG_RECORD_SIZE
        if pos + _CATALOG_RECORD_SIZE > len(catalog_data):
            break

        skill_id = struct.unpack_from("<I", catalog_data, pos)[0]
        if skill_id == _CATALOG_NULL_ID:
            break

        loc_ids[skill_id] = struct.unpack_from("<H", catalog_data, pos + 0x0A)[0]

    return loc_ids


def flatten_roll_rows(
    records: list[dict],
    loc_ids: dict[int, int],
    skill_name: "callable[[int], str]",
) -> list[dict]:
    """Expand weight arrays into one row per (acquire type, rollable skill)."""
    rows: list[dict] = []

    for record in records:
        total = record["total_weight"]
        for skill_id, weight in enumerate(record["weights"]):
            if not weight:
                continue

            loc_id = loc_ids.get(skill_id, 0)
            rows.append({
                "acquire_type_id": record["acquire_type_id"],
                "equip_skill_id": skill_id,
                "loc_id": loc_id,
                "skill_name": skill_name(loc_id) if loc_id else "",
                "weight": weight,
                "chance_pct": round(weight * 100 / total, 4) if total else 0.0,
                "total_weight": total,
            })

    return rows
