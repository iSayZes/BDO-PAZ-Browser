"""`pcactionpackagename.bss`: the action chart package of each class per weapon, vehicle and cutscene.

    PABR | class_type_count x class block | [u32 n | n x (u8 class_type, u32 package_index, u32 package_hash)]
    | string table | u32 string_table_start | u32 0

    class block: equip_type_count x cell          one per equip type
                 u32 vehicle_count | vehicle_count x vehicle row
                 equip_type_count x (u32 count | count x vehicle row)   vehicle with a weapon, per equip type
                 cell                             cutscene package
    cell:        u32 package_index | u32 package_hash
    vehicle row: u32 vehicle_name_index | u32 package_index | u32 package_hash

Neither count is stored and both grow with the client (82 x 91 on client 1743,
97 x 119 on client 3483), so the parser finds them in the file: the equip type
count is the one whose first class block holds a valid package hash in every
cell and row, and the class blocks go on until the rest of the file is empty
(clients 1743 to 2098) or exactly one class package list (client 2107 on).
Every index points into the PABR string table; an empty cell points at the
empty string with hash `0`. docs/file-formats/pcactionpackagename_bss.md has a
layout per count pair.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import check_rows_end, checked_string_table_start, read_string_table
from _common.record_reader import RecordReader
from _common.string_hash import ascii_key_hash


FILE_NAME = "pcactionpackagename.bss"
# `equip_type` and the list's `class_type` are u8 values, so neither count can pass 256.
MAX_EQUIP_TYPE_COUNT = 256
MAX_CLASS_TYPE_COUNT = 256

# `section` values, one per place a package sits in the file.
SECTION_WEAPON = "weapon"
SECTION_VEHICLE = "vehicle"
SECTION_VEHICLE_WEAPON = "vehicle_weapon"
SECTION_CUTSCENE = "cutscene"
SECTION_CLASS_PACKAGE = "class_package"
SECTIONS = (SECTION_WEAPON, SECTION_VEHICLE, SECTION_VEHICLE_WEAPON, SECTION_CUTSCENE, SECTION_CLASS_PACKAGE)

_MAGIC_SIZE = 4
_EMPTY_HASH = 0
_NO_HASH = -1
_U32 = struct.Struct("<I")
_CELL = struct.Struct("<II")
_VEHICLE_ROW = struct.Struct("<III")
_CLASS_PACKAGE_ROW = struct.Struct("<BII")


class _Strings:
    """The string table, with a bounds check that names the bad index."""

    def __init__(self, data: bytes) -> None:
        self._strings = read_string_table(data)
        self._hashes: dict[int, int] = {}

    def at(self, index: int, where: str) -> str:
        if not self.has(index):
            raise ValueError(f"{where} points at string {index:,}, past the {len(self._strings):,} strings")
        return self._strings[index]

    def has(self, index: int) -> bool:
        return 0 <= index < len(self._strings)

    def is_package(self, index: int, package_hash: int) -> bool:
        """True when `index` is in the table and `package_hash` is its hash (`0` for the empty string)."""
        if not self.has(index):
            return False
        if index not in self._hashes:
            self._hashes[index] = _package_hash(self._strings[index])
        return self._hashes[index] == package_hash


def _package_hash(text: str) -> int:
    """The hash a cell stores for `text`; `_NO_HASH` for a path that is not ASCII, which no cell can store."""
    if not text:
        return _EMPTY_HASH
    return ascii_key_hash(text) if text.isascii() else _NO_HASH


def parse_pcactionpackagename(data: bytes) -> list[dict]:
    """Every non-empty package, in file order.

    Each record holds `class_type`, `section` (one of `SECTIONS`),
    `equip_type` and `vehicle_name` (None where the section has none),
    `vehicle_name_index`, `package`, `package_index` and `package_hash`.
    Raises ValueError on a bad PABR magic, an index past the string table or
    when no equip type count reads the class blocks up to the string table.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = _Strings(data)
    errors: list[str] = []
    for equip_type_count in range(1, MAX_EQUIP_TYPE_COUNT + 1):
        if not _first_block_fits(data, end, strings, equip_type_count):
            continue
        try:
            return _read_file(data, end, strings, equip_type_count)
        except ValueError as error:
            errors.append(f"{equip_type_count}: {error}")
    reasons = f" ({'; '.join(errors)})" if errors else ""
    raise ValueError(f"{FILE_NAME} fits no class block of 1 to {MAX_EQUIP_TYPE_COUNT} equip types{reasons}")


def _first_block_fits(data: bytes, end: int, strings: _Strings, equip_type_count: int) -> bool:
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
        index, package_hash = reader.unpack(_CELL)
    except ValueError:
        return False
    return strings.is_package(index, package_hash)


def _vehicle_rows_fit(reader: RecordReader, strings: _Strings) -> bool:
    (count,) = reader.unpack(_U32)
    if count * _VEHICLE_ROW.size > reader.remaining():
        return False
    for _ in range(count):
        name_index, index, package_hash = reader.unpack(_VEHICLE_ROW)
        # A vehicle type name has no hash; only its index must be in the table.
        if not strings.has(name_index) or package_hash == _EMPTY_HASH or not strings.is_package(index, package_hash):
            return False
    return True


def _read_file(data: bytes, end: int, strings: _Strings, equip_type_count: int) -> list[dict]:
    reader = RecordReader(data, _MAGIC_SIZE, end, FILE_NAME)
    records: list[dict] = []
    class_type = 0
    while not reader.at_end() and not _is_class_package_list(data, reader.pos, end):
        if class_type == MAX_CLASS_TYPE_COUNT:
            raise ValueError(f"more than {MAX_CLASS_TYPE_COUNT} class blocks")
        records.extend(_read_class_block(reader, strings, class_type, equip_type_count))
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


def _read_class_block(reader: RecordReader, strings: _Strings, class_type: int, equip_type_count: int) -> list[dict]:
    where = f"class block {class_type}"
    weapons = [
        _package(strings, where, class_type, SECTION_WEAPON, *reader.unpack(_CELL), equip_type=equip_type)
        for equip_type in range(equip_type_count)
    ]
    records = [record for record in weapons if record["package"]]
    records.extend(_read_vehicle_rows(reader, strings, where, class_type, SECTION_VEHICLE, None))
    for equip_type in range(equip_type_count):
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
