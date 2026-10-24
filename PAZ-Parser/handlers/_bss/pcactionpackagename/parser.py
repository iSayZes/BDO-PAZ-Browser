"""`pcactionpackagename.bss`: the action chart package of each class per weapon, vehicle and cutscene.

    PABR | 97 x class block | u32 n | n x (u8 class_type, u32 package_index, u32 package_hash)
    | string table | u32 string_table_start | u32 0

    class block: 119 x cell                       one per equip type
                 u32 vehicle_count | vehicle_count x vehicle row
                 119 x (u32 count | count x vehicle row)   vehicle with a weapon, per equip type
                 cell                             cutscene package
    cell:        u32 package_index | u32 package_hash
    vehicle row: u32 vehicle_name_index | u32 package_index | u32 package_hash

Both block counts are fixed by the client, not stored. Every index points into
the PABR string table; an empty cell points at the empty string with hash `0`.
Layout 2 in docs/file-formats/pcactionpackagename_bss.md; the 82 x 92 blocks of
Layout 1 (client 1784) are not read.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import check_rows_end, checked_string_table_start, read_string_table
from _common.record_reader import RecordReader


FILE_NAME = "pcactionpackagename.bss"
CLASS_TYPE_COUNT = 97
EQUIP_TYPE_COUNT = 119

# `section` values, one per place a package sits in the file.
SECTION_WEAPON = "weapon"
SECTION_VEHICLE = "vehicle"
SECTION_VEHICLE_WEAPON = "vehicle_weapon"
SECTION_CUTSCENE = "cutscene"
SECTION_CLASS_PACKAGE = "class_package"
SECTIONS = (SECTION_WEAPON, SECTION_VEHICLE, SECTION_VEHICLE_WEAPON, SECTION_CUTSCENE, SECTION_CLASS_PACKAGE)

_MAGIC_SIZE = 4
_U32 = struct.Struct("<I")
_CELL = struct.Struct("<II")
_VEHICLE_ROW = struct.Struct("<III")
_CLASS_PACKAGE_ROW = struct.Struct("<BII")


class _Strings:
    """The string table, with a bounds check that names the bad index."""

    def __init__(self, data: bytes) -> None:
        self._strings = read_string_table(data)

    def at(self, index: int, where: str) -> str:
        if not 0 <= index < len(self._strings):
            raise ValueError(f"{where} points at string {index:,}, past the {len(self._strings):,} strings")
        return self._strings[index]


def parse_pcactionpackagename(data: bytes) -> list[dict]:
    """Every non-empty package, in file order.

    Each record holds `class_type`, `section` (one of `SECTIONS`),
    `equip_type` and `vehicle_name` (None where the section has none),
    `vehicle_name_index`, `package`, `package_index` and `package_hash`.
    Raises ValueError on a bad PABR magic, an index past the string table or
    when the walk does not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = _Strings(data)
    reader = RecordReader(data, _MAGIC_SIZE, end, FILE_NAME)
    records: list[dict] = []
    for class_type in range(CLASS_TYPE_COUNT):
        records.extend(_read_class_block(reader, strings, class_type))
    records.extend(_read_class_packages(reader, strings))
    check_rows_end(data, reader.pos, f"{FILE_NAME} class blocks")
    return records


def _read_class_block(reader: RecordReader, strings: _Strings, class_type: int) -> list[dict]:
    where = f"class block {class_type}"
    weapons = [
        _package(strings, where, class_type, SECTION_WEAPON, *reader.unpack(_CELL), equip_type=equip_type)
        for equip_type in range(EQUIP_TYPE_COUNT)
    ]
    records = [record for record in weapons if record["package"]]
    records.extend(_read_vehicle_rows(reader, strings, where, class_type, SECTION_VEHICLE, None))
    for equip_type in range(EQUIP_TYPE_COUNT):
        records.extend(_read_vehicle_rows(reader, strings, where, class_type, SECTION_VEHICLE_WEAPON, equip_type))
    cutscene = _package(strings, where, class_type, SECTION_CUTSCENE, *reader.unpack(_CELL))
    if cutscene["package"]:
        records.append(cutscene)
    return records


def _read_vehicle_rows(
    reader: RecordReader,
    strings: _Strings,
    where: str,
    class_type: int,
    section: str,
    equip_type: int | None,
) -> list[dict]:
    (count,) = reader.unpack(_U32)
    records: list[dict] = []
    for _ in range(count):
        name_index, index, package_hash = reader.unpack(_VEHICLE_ROW)
        records.append(
            _package(
                strings, where, class_type, section, index, package_hash,
                equip_type=equip_type, vehicle_name_index=name_index,
            )
        )
    return records


def _read_class_packages(reader: RecordReader, strings: _Strings) -> list[dict]:
    (count,) = reader.unpack(_U32)
    records: list[dict] = []
    for _ in range(count):
        class_type, index, package_hash = reader.unpack(_CLASS_PACKAGE_ROW)
        records.append(_package(strings, "class package list", class_type, SECTION_CLASS_PACKAGE, index, package_hash))
    return records


def _package(
    strings: _Strings,
    where: str,
    class_type: int,
    section: str,
    package_index: int,
    package_hash: int,
    *,
    equip_type: int | None = None,
    vehicle_name_index: int | None = None,
) -> dict:
    vehicle_name = None if vehicle_name_index is None else strings.at(vehicle_name_index, where)
    return {
        "class_type": class_type,
        "section": section,
        "equip_type": equip_type,
        "vehicle_name": vehicle_name,
        "vehicle_name_index": vehicle_name_index,
        "package": strings.at(package_index, where),
        "package_index": package_index,
        "package_hash": package_hash,
    }
