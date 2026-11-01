"""`pcactionpackagename.bss` of clients 435 to 829: one array per place a package sits, then the same arrays of hashes.

    weapon names    [32][equip_type_count] name
    vehicle names   [32][vehicle_type_count] name
    32 x (u32 count | count x (u8 vehicle_type, u8 equip_type, name))           vehicle with a weapon
    weapon hashes   [32][equip_type_count] u32
    vehicle hashes  [32][vehicle_type_count] u32
    32 x (u32 count | count x (u8 vehicle_type, u8 equip_type, u32 hash))

A name is a `str8` (u64 length, then ASCII) on clients 435 to 794, which have no
PABR magic and no string table, and a u32 index into the PABR string table on
clients 805 to 829. 32 is the class count of every such client. Neither inner
count is stored: their sum is the one whose hashes match every name and whose
arrays end the file (or reach the string table), and the vehicle array starts
at the first `pc/vehicle/` path. The position in a vehicle row is the
`CppEnums.VehicleType` value, the position in a weapon row the equip type.
"""

from __future__ import annotations

import struct
from collections.abc import Callable

from _common.record_reader import RecordReader
from _common.vehicle_type import VEHICLE_TYPE_NAMES
from .packages import (
    FILE_NAME,
    SECTION_VEHICLE,
    SECTION_VEHICLE_WEAPON,
    SECTION_WEAPON,
    PackageStrings,
    package_hash,
    package_record,
)


CLASS_TYPE_COUNT = 32
VEHICLE_FOLDER = "pc/vehicle/"
# `equip_type` and `vehicle_type` are u8 values, so a class row holds at most 256 of each.
MAX_NAMES_PER_CLASS = 512

_MAGIC_SIZE = 4
_U32 = struct.Struct("<I")
_KEY = struct.Struct("<BB")
_HASH_ROW = struct.Struct("<BBI")

# A package path and its string table index (None where the path is inline).
Name = tuple[str, int | None]
# vehicle_type, equip_type, package
_MapRow = tuple[int, int, Name]


class _InlineNames:
    """Clients 435 to 794: every name is a `str8` in place, from the first byte on."""

    # The u64 length of an empty name.
    name_size = 8

    def __init__(self, data: bytes) -> None:
        self._texts: list[str] = []
        self._ends = [0]
        reader = RecordReader(data, 0, len(data), FILE_NAME)
        # The names run on into the maps; read as far as bytes still read as str8.
        while not reader.at_end():
            try:
                self._texts.append(reader.text(wide=False))
            except ValueError:
                break
            self._ends.append(reader.pos)

    def names_end(self, count: int) -> int | None:
        return self._ends[count] if count < len(self._ends) else None

    def names(self, count: int) -> list[Name]:
        return [(text, None) for text in self._texts[:count]]

    def read(self, reader: RecordReader) -> Name:
        return reader.text(wide=False), None


class _IndexedNames:
    """Clients 805 to 829: every name is a u32 index into the PABR string table, after the magic."""

    name_size = _U32.size

    def __init__(self, data: bytes, end: int, strings: PackageStrings) -> None:
        self._data, self._end, self._strings = data, end, strings

    def names_end(self, count: int) -> int | None:
        stop = _MAGIC_SIZE + count * _U32.size
        return stop if stop <= self._end else None

    def names(self, count: int) -> list[Name]:
        indices = struct.unpack_from(f"<{count}I", self._data, _MAGIC_SIZE)
        return [(self._strings.at(index, "a package array"), index) for index in indices]

    def read(self, reader: RecordReader) -> Name:
        (index,) = reader.unpack(_U32)
        return self._strings.at(index, "a vehicle with weapon map"), index


_Names = _InlineNames | _IndexedNames


def parse_inline_arrays(data: bytes) -> list[dict]:
    """Clients 435 to 794. Raises ValueError when no name count per class walks the file."""
    return _parse(data, _InlineNames(data), len(data), "no PABR magic and fits no array layout of inline names")


def parse_indexed_arrays(data: bytes, end: int, strings: PackageStrings) -> list[dict]:
    """Clients 805 to 829, whose arrays end at `end`, the string table. Raises ValueError like `parse_inline_arrays`."""
    return _parse(data, _IndexedNames(data, end, strings), end, "fits no array layout of string indices")


def _parse(data: bytes, names: _Names, end: int, failure: str) -> list[dict]:
    for names_per_class in range(1, MAX_NAMES_PER_CLASS + 1):
        cell_count = CLASS_TYPE_COUNT * names_per_class
        names_end = names.names_end(cell_count)
        if names_end is None:
            break
        try:
            cells, maps = _walk(data, names, cell_count, names_end, end)
        except ValueError:
            continue
        return _records(cells, maps, names_per_class)
    raise ValueError(f"{FILE_NAME} has {failure}")


def _walk(
    data: bytes, names: _Names, cell_count: int, names_end: int, end: int
) -> tuple[list[Name], list[list[_MapRow]]]:
    """The names and maps when the arrays end at `end` and every hash matches its name; ValueError otherwise."""
    reader = RecordReader(data, names_end, end, FILE_NAME)
    map_row_size = _KEY.size + names.name_size
    maps = [
        _read_map(reader, map_row_size, lambda: (*reader.unpack(_KEY), names.read(reader)))
        for _ in range(CLASS_TYPE_COUNT)
    ]
    hashes = reader.unpack(struct.Struct(f"<{cell_count}I"))
    hash_maps = [
        _read_map(reader, _HASH_ROW.size, lambda: reader.unpack(_HASH_ROW)) for _ in range(CLASS_TYPE_COUNT)
    ]
    if not reader.at_end():
        raise ValueError(f"the arrays end at 0x{reader.pos:X}, not 0x{end:X}")
    cells = names.names(cell_count)
    if any(package_hash(text) != stored for (text, _), stored in zip(cells, hashes)):
        raise ValueError("a package hash does not match its path")
    for rows, hash_rows in zip(maps, hash_maps):
        if len(rows) != len(hash_rows):
            raise ValueError("a hash map holds another row count than its map")
        for (vehicle_type, equip_type, (text, _)), hash_row in zip(rows, hash_rows):
            if hash_row != (vehicle_type, equip_type, package_hash(text)):
                raise ValueError("a hash map row does not match its map row")
    return cells, maps


def _read_map(reader: RecordReader, min_row_size: int, read_row: Callable[[], tuple]) -> list[tuple]:
    (count,) = reader.unpack(_U32)
    if count * min_row_size > reader.remaining():
        raise ValueError(f"a map count of {count:,} runs past the arrays")
    return [read_row() for _ in range(count)]


def _equip_type_count(cells: list[Name]) -> int:
    """The weapon array ends at the first `pc/vehicle/` path, which starts a class row."""
    first = next((pos for pos, (text, _) in enumerate(cells) if text.startswith(VEHICLE_FOLDER)), None)
    if first is None or first % CLASS_TYPE_COUNT:
        raise ValueError(f"{FILE_NAME} has no `{VEHICLE_FOLDER}` path at the start of a class row")
    if any(text and not text.startswith(VEHICLE_FOLDER) for text, _ in cells[first:]):
        raise ValueError(f"{FILE_NAME} holds a path outside `{VEHICLE_FOLDER}` after its first vehicle package")
    return first // CLASS_TYPE_COUNT


def _records(cells: list[Name], maps: list[list[_MapRow]], names_per_class: int) -> list[dict]:
    """Every non-empty package, class by class: weapons, vehicles, then vehicles with a weapon."""
    equip_type_count = _equip_type_count(cells)
    vehicle_type_count = names_per_class - equip_type_count
    vehicle_start = CLASS_TYPE_COUNT * equip_type_count
    records: list[dict] = []
    for class_type in range(CLASS_TYPE_COUNT):
        weapon_start = class_type * equip_type_count
        for equip_type, name in enumerate(cells[weapon_start:weapon_start + equip_type_count]):
            records.extend(_record(class_type, SECTION_WEAPON, name, equip_type=equip_type))
        vehicle_row_start = vehicle_start + class_type * vehicle_type_count
        for vehicle_type, name in enumerate(cells[vehicle_row_start:vehicle_row_start + vehicle_type_count]):
            records.extend(_record(class_type, SECTION_VEHICLE, name, vehicle_type=vehicle_type))
        for vehicle_type, equip_type, name in maps[class_type]:
            records.extend(
                _record(class_type, SECTION_VEHICLE_WEAPON, name, equip_type=equip_type, vehicle_type=vehicle_type)
            )
    return records


def _record(
    class_type: int,
    section: str,
    name: Name,
    *,
    equip_type: int | None = None,
    vehicle_type: int | None = None,
) -> list[dict]:
    """The package as a one-record list, or no record for an empty cell."""
    text, index = name
    if not text:
        return []
    vehicle_name = None if vehicle_type is None else VEHICLE_TYPE_NAMES.get(vehicle_type, str(vehicle_type))
    return [
        package_record(
            class_type, section, text, index, package_hash(text), equip_type=equip_type, vehicle_name=vehicle_name
        )
    ]
