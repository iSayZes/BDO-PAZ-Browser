"""`pcactionpackagename.bss`: the action chart package of each class per weapon, vehicle and cutscene.

Clients 1109 on store one block per class:

    PABR | class_type_count x class block | [u32 n | n x (u8 class_type, u32 package_index, u32 package_hash)]
    | string table | u32 string_table_start | u32 0

    class block: equip_type_count x cell          one per equip type
                 u32 vehicle_count | vehicle_count x vehicle row
                 equip_type_count x (u32 count | count x vehicle row)   vehicle with a weapon, per equip type
                 cell                             cutscene package, from client 1743 on
    cell:        u32 package_index | u32 package_hash
    vehicle row: u32 vehicle_name_index | u32 package_index | u32 package_hash

Neither count is stored and both grow with the client (32 x 84 on client 1109,
97 x 119 on client 3483), so the parser finds them in the file: the equip type
count is the one whose first class block holds a valid package hash in every
cell and row, and the class blocks go on until the rest of the file is empty
(clients 1109 to 2098) or exactly one class package list (client 2107 on).
Every cell and row must hold the hash of the string its index points at; an
empty cell points at the empty string with hash `0`. Clients 435 to 829 store
arrays instead (`array_layout.py`). docs/file-formats/bss/pcactionpackagename_bss.md
has a layout per count pair.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PABR_MAGIC
from _common.pabr_strings import check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader
from .array_layout import parse_indexed_arrays, parse_inline_arrays
from .packages import (
    FILE_NAME,
    SECTION_CLASS_PACKAGE,
    SECTION_CUTSCENE,
    SECTION_VEHICLE,
    SECTION_VEHICLE_WEAPON,
    SECTION_WEAPON,
    PackageStrings,
    package_record,
)


# `equip_type` and the list's `class_type` are u8 values, so neither count can pass 256.
MAX_EQUIP_TYPE_COUNT = 256
MAX_CLASS_TYPE_COUNT = 256

_MAGIC_SIZE = 4
_EMPTY_HASH = 0
_U32 = struct.Struct("<I")
_CELL = struct.Struct("<II")
_VEHICLE_ROW = struct.Struct("<III")
_CLASS_PACKAGE_ROW = struct.Struct("<BII")
# Class blocks end with the cutscene cell from client 1743 on, and without it before.
_CUTSCENE_SHAPES = (True, False)


def parse_pcactionpackagename(data: bytes) -> list[dict]:
    """Every non-empty package, class by class.

    Each record holds `class_type`, `section` (one of `SECTIONS`),
    `equip_type` and `vehicle_name` (None where the section has none),
    `vehicle_name_index`, `package`, `package_index` (None where the path
    is inline) and `package_hash`. Raises ValueError on a bad PABR trailer,
    an index past the string table or a hash that does not match its path,
    and when no layout reads the file.
    """
    if data[:_MAGIC_SIZE] != PABR_MAGIC:
        return parse_inline_arrays(data)
    end = checked_string_table_start(data, FILE_NAME)
    strings = PackageStrings(data)
    errors: list[str] = []
    for has_cutscene in _CUTSCENE_SHAPES:
        for equip_type_count in range(1, MAX_EQUIP_TYPE_COUNT + 1):
            if not _first_block_fits(data, end, strings, equip_type_count, has_cutscene):
                continue
            try:
                return _read_file(data, end, strings, equip_type_count, has_cutscene)
            except ValueError as error:
                errors.append(f"{equip_type_count}: {error}")
    try:
        return parse_indexed_arrays(data, end, strings)
    except ValueError as error:
        reasons = f" ({'; '.join(errors)})" if errors else ""
        raise ValueError(f"{FILE_NAME} fits no class block of 1 to {MAX_EQUIP_TYPE_COUNT} equip types{reasons}; {error}") from None


def _first_block_fits(data: bytes, end: int, strings: PackageStrings, equip_type_count: int, has_cutscene: bool) -> bool:
    """True when class block 0 read with `equip_type_count` cells holds a valid hash in every cell and row."""
    reader = RecordReader(data, _MAGIC_SIZE, end, FILE_NAME)
    try:
        cells = [reader.unpack(_CELL) for _ in range(equip_type_count)]
        if not all(strings.is_package(index, package_hash) for index, package_hash in cells):
            return False
        # The vehicle rows, then one list per equip type.
        for _ in range(1 + equip_type_count):
            if not _vehicle_rows_fit(reader, strings):
                return False
        if not has_cutscene:
            return True
        index, package_hash = reader.unpack(_CELL)
    except ValueError:
        return False
    return strings.is_package(index, package_hash)


def _vehicle_rows_fit(reader: RecordReader, strings: PackageStrings) -> bool:
    (count,) = reader.unpack(_U32)
    if count * _VEHICLE_ROW.size > reader.remaining():
        return False
    for _ in range(count):
        name_index, index, package_hash = reader.unpack(_VEHICLE_ROW)
        # A vehicle type name has no hash; only its index must be in the table.
        if not strings.has(name_index) or package_hash == _EMPTY_HASH or not strings.is_package(index, package_hash):
            return False
    return True


def _read_file(data: bytes, end: int, strings: PackageStrings, equip_type_count: int, has_cutscene: bool) -> list[dict]:
    reader = RecordReader(data, _MAGIC_SIZE, end, FILE_NAME)
    records: list[dict] = []
    class_type = 0
    while not reader.at_end() and not _is_class_package_list(data, reader.pos, end):
        if class_type == MAX_CLASS_TYPE_COUNT:
            raise ValueError(f"more than {MAX_CLASS_TYPE_COUNT} class blocks")
        records.extend(_read_class_block(reader, strings, class_type, equip_type_count, has_cutscene))
        class_type += 1
    if not reader.at_end():
        records.extend(_read_class_packages(reader, strings))
    check_rows_end(data, reader.pos, f"{FILE_NAME} class blocks")
    return records


def _is_class_package_list(data: bytes, pos: int, end: int) -> bool:
    """True when the bytes from `pos` to `end` are exactly one u32 count and that many class package rows."""
    if end - pos < _U32.size:
        return False
    (count,) = _U32.unpack_from(data, pos)
    return _U32.size + count * _CLASS_PACKAGE_ROW.size == end - pos


def _read_class_block(
    reader: RecordReader, strings: PackageStrings, class_type: int, equip_type_count: int, has_cutscene: bool
) -> list[dict]:
    where = f"class block {class_type}"
    weapons = [
        _package(strings, where, class_type, SECTION_WEAPON, *reader.unpack(_CELL), equip_type=equip_type)
        for equip_type in range(equip_type_count)
    ]
    records = [record for record in weapons if record["package"]]
    records.extend(_read_vehicle_rows(reader, strings, where, class_type, SECTION_VEHICLE, None))
    for equip_type in range(equip_type_count):
        records.extend(_read_vehicle_rows(reader, strings, where, class_type, SECTION_VEHICLE_WEAPON, equip_type))
    if has_cutscene:
        cutscene = _package(strings, where, class_type, SECTION_CUTSCENE, *reader.unpack(_CELL))
        if cutscene["package"]:
            records.append(cutscene)
    return records


def _read_vehicle_rows(
    reader: RecordReader,
    strings: PackageStrings,
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


def _read_class_packages(reader: RecordReader, strings: PackageStrings) -> list[dict]:
    (count,) = reader.unpack(_U32)
    records: list[dict] = []
    for _ in range(count):
        class_type, index, package_hash = reader.unpack(_CLASS_PACKAGE_ROW)
        records.append(_package(strings, "class package list", class_type, SECTION_CLASS_PACKAGE, index, package_hash))
    return records


def _package(
    strings: PackageStrings,
    where: str,
    class_type: int,
    section: str,
    package_index: int,
    package_hash: int,
    *,
    equip_type: int | None = None,
    vehicle_name_index: int | None = None,
) -> dict:
    package = strings.at(package_index, where)
    if not strings.is_package(package_index, package_hash):
        raise ValueError(f"{where} stores hash 0x{package_hash:08X} for string {package_index:,}, not the hash of its path")
    vehicle_name = None if vehicle_name_index is None else strings.at(vehicle_name_index, where)
    return package_record(
        class_type, section, package, package_index, package_hash,
        equip_type=equip_type, vehicle_name=vehicle_name, vehicle_name_index=vehicle_name_index,
    )
