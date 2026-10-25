"""`plantzone.dbss`: worker production zones, located through `plantzoneoffset.dbss`.

    u32 record_id | u32 | u32 | u16 | u8 work_ani_type
    | u16 productivity_upgrade_group_index | u16 luck_productivity_upgrade_group_index
    | u32 production_count | (u16 production_key | u16 max_capacity_level)[production_count]
    | u32 species_count | u8[species_count] worker_species

Full layout in docs/file-formats/dbss/plantzone_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import parse_bare_u32_offset_rows

# Record field offsets; the last five are unaligned.
_WORK_ANI_TYPE = 0x0E
_PRODUCTION_COUNT = 0x13
_PRODUCTION_KEY = 0x17
_MAX_CAPACITY_LEVEL = 0x19
_SPECIES_COUNT = 0x1B
_SPECIES = 0x1F

# Every zone on clients 1784 and 3464 lists one production; the fixed offsets
# above assume it.
_PRODUCTIONS_PER_ZONE = 1

# Worker species byte (plantworker.bss +0x38F), named after the workers that
# carry each value; the client enum was not found.
WORKER_SPECIES_NAMES: tuple[str, ...] = (
    "Goblin", "Human", "Giant", "Papu", "Fadus", "Dwarf", "Dokkebi", "Dolswe", "Shellfolk",
)


def parse_offset_records(data: bytes) -> list[dict]:
    """The offset rows; the u16 record ID and the zero u16 after it read as one u32."""
    return [
        {"record_id": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_u32_offset_rows(data)
    ]


def parse_plantzone_records(data: bytes, offset_data: bytes) -> list[dict]:
    """One zone per offset row, in offset-file order.

    Raises ValueError when a row points past the file, lists other than one
    production, or its species list does not end exactly at the row's size:
    every later field would then be misread.
    """
    records: list[dict] = []

    for off in parse_offset_records(offset_data):
        start = off["data_offset"]
        size = off["data_size"]
        record_id = off["record_id"]
        if start + size > len(data) or size < _SPECIES:
            raise ValueError(f"plantzone record {record_id} runs past the end of plantzone.dbss")

        payload = data[start : start + size]
        production_count = struct.unpack_from("<I", payload, _PRODUCTION_COUNT)[0]
        if production_count != _PRODUCTIONS_PER_ZONE:
            raise ValueError(f"plantzone record {record_id} lists {production_count} productions, not 1")

        species_count = struct.unpack_from("<I", payload, _SPECIES_COUNT)[0]
        if _SPECIES + species_count != size:
            raise ValueError(f"plantzone record {record_id} lists {species_count} species in {size} bytes")

        records.append({
            "record_id": struct.unpack_from("<I", payload, 0x00)[0],
            "work_ani_type": payload[_WORK_ANI_TYPE],
            "production_key": struct.unpack_from("<H", payload, _PRODUCTION_KEY)[0],
            "max_capacity_level": struct.unpack_from("<H", payload, _MAX_CAPACITY_LEVEL)[0],
            "worker_species": list(payload[_SPECIES:]),
            "data_size": size,
        })

    return records
