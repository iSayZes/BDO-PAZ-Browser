"""What every `pcactionpackagename.bss` layout shares: the section names, the package hash and the record of a package."""

from __future__ import annotations

from _common.pabr_strings import read_string_table
from _common.string_hash import ascii_key_hash


FILE_NAME = "pcactionpackagename.bss"

# `section` values, one per place a package sits in the file.
SECTION_WEAPON = "weapon"
SECTION_VEHICLE = "vehicle"
SECTION_VEHICLE_WEAPON = "vehicle_weapon"
SECTION_CUTSCENE = "cutscene"
SECTION_CLASS_PACKAGE = "class_package"
SECTIONS = (SECTION_WEAPON, SECTION_VEHICLE, SECTION_VEHICLE_WEAPON, SECTION_CUTSCENE, SECTION_CLASS_PACKAGE)

_EMPTY_HASH = 0
_NO_HASH = -1


def package_hash(text: str) -> int:
    """The hash a cell stores for `text`; `0` for the empty string, `-1` for a path that is not ASCII."""
    if not text:
        return _EMPTY_HASH
    return ascii_key_hash(text) if text.isascii() else _NO_HASH


class PackageStrings:
    """The PABR string table, with a bounds check that names the bad index."""

    def __init__(self, data: bytes) -> None:
        self._strings = read_string_table(data)
        self._hashes: dict[int, int] = {}

    def at(self, index: int, where: str) -> str:
        if not self.has(index):
            raise ValueError(f"{where} points at string {index:,}, past the {len(self._strings):,} strings")
        return self._strings[index]

    def has(self, index: int) -> bool:
        return 0 <= index < len(self._strings)

    def is_package(self, index: int, stored_hash: int) -> bool:
        """True when `index` is in the table and `stored_hash` is the hash of its string."""
        if not self.has(index):
            return False
        if index not in self._hashes:
            self._hashes[index] = package_hash(self._strings[index])
        return self._hashes[index] == stored_hash


def package_record(
    class_type: int,
    section: str,
    package: str,
    package_index: int | None,
    stored_hash: int,
    *,
    equip_type: int | None = None,
    vehicle_name: str | None = None,
    vehicle_name_index: int | None = None,
) -> dict:
    """One package. `package_index` is None where the layout stores the path inline."""
    return {
        "class_type": class_type,
        "section": section,
        "equip_type": equip_type,
        "vehicle_name": vehicle_name,
        "vehicle_name_index": vehicle_name_index,
        "package": package,
        "package_index": package_index,
        "package_hash": stored_hash,
    }
