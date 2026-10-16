"""The full record grammar of docs/file-formats/characterobject_dbss.md, walked on the installed client.

The handler reads only the record prefix and the icon index scans for the icon
path, so nothing in production walks a whole record. These tests keep the
documented body layout honest: every record must end exactly at its
`data_size`, and the walked icon path must agree with the scan.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import pytest

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow, parse_pabr_offset_rows
from _common.prefixed_string import read_prefixed_at
from _dbss.characterobject.parser import build_character_icon_index
from tests.fixtures import load_binary_fixture

_FURNITURE = 2
_MODEL_PATH = 0x06

_FURNITURE_BLOCK = 556
_ACTION_HASH = 4
_FURNITURE_TAIL = 48

_FACE = 140
_PROPERTIES = 333
_AFTER_MATERIAL = 16
_SUFFIX = 234
_AFTER_DESCRIPTION_KR = 162
_HOUSE_IMAGE_SLOTS = 4
_AFTER_PATH_4 = 24
_HOUSE_HULL_NAME = "HH_"

_ICON_FILE = re.compile(r"(?i)(?:new_)?icon/[ -~]+\.(?:dds|png)")


@dataclass
class _Cursor:
    data: bytes
    at: int
    end: int

    def ascii(self) -> str:
        text, self.at = read_prefixed_at(self.data, self.at, self.end, wide=False)
        return text

    def wide(self) -> str:
        text, self.at = read_prefixed_at(self.data, self.at, self.end, wide=True)
        return text

    def count(self) -> int:
        value = u32(self.data, self.at)
        self.at += 4
        return value

    def skip(self, size: int) -> None:
        self.at += size


@dataclass(frozen=True)
class _Walked:
    end: int
    icon_path: str
    name_kr: str = ""


def _walk(data: bytes, row: PabrOffsetRow) -> _Walked:
    cursor = _Cursor(data, row.offset + _MODEL_PATH, row.offset + row.size)
    cursor.ascii()  # model_path
    if data[row.offset + 2] == _FURNITURE:
        return _walk_furniture(cursor)
    return _walk_structure(cursor)


def _walk_furniture(cursor: _Cursor) -> _Walked:
    cursor.skip(_FURNITURE_BLOCK)
    cursor.ascii()  # action_name
    cursor.skip(_ACTION_HASH)
    icon_path = cursor.ascii()
    cursor.skip(_FURNITURE_TAIL)
    return _Walked(cursor.at, icon_path)


def _walk_structure(cursor: _Cursor) -> _Walked:
    cursor.ascii()  # hull_model_path
    hull_name = cursor.ascii()
    cursor.skip(1)  # unknown_flag
    layer_count = cursor.count()
    assert cursor.count() == layer_count  # unknown_b
    for _ in range(layer_count):
        for _ in range(cursor.count()):  # hull_count
            cursor.skip(cursor.count() * _FACE)  # face_count faces
    cursor.skip(_PROPERTIES)
    cursor.ascii()  # material_path
    cursor.skip(_AFTER_MATERIAL)
    cursor.ascii()  # unknown_digits
    if not hull_name.startswith(_HOUSE_HULL_NAME):
        cursor.skip(_SUFFIX)
        return _Walked(cursor.at, "")

    name_kr = cursor.wide()
    cursor.wide()  # description_kr
    cursor.skip(_AFTER_DESCRIPTION_KR)  # unknown_description_kr_00
    images = [cursor.ascii() for _ in range(_HOUSE_IMAGE_SLOTS)]
    cursor.skip(_AFTER_PATH_4)  # unknown_unknown_path_4_00
    return _Walked(cursor.at, images[0], name_kr)


@pytest.fixture(scope="module")
def tables() -> tuple[bytes, bytes]:
    return (
        load_binary_fixture("characterobject.dbss"),
        load_binary_fixture("characterobjectoffset.dbss"),
    )


@pytest.fixture(scope="module")
def walked(tables: tuple[bytes, bytes]) -> dict[int, tuple[PabrOffsetRow, _Walked]]:
    data, offset = tables
    return {row.entry_id: (row, _walk(data, row)) for row in parse_pabr_offset_rows(offset)}


def test_every_record_walks_to_its_data_size(
    walked: dict[int, tuple[PabrOffsetRow, _Walked]],
) -> None:
    short = [
        character_id
        for character_id, (row, record) in walked.items()
        if record.end != row.offset + row.size
    ]

    assert not short, f"records that do not end at data_size: {short[:5]}"


def test_house_branch_holds_the_house_icon(
    walked: dict[int, tuple[PabrOffsetRow, _Walked]],
) -> None:
    # Velia 4: image slot 1 is the icon the house list shows.
    _, house = walked[2101]

    assert house.icon_path == "Icon/New_Icon/03_ETC/06_Housing/2101-1.dds"
    assert house.name_kr


def test_icon_scan_agrees_with_the_walked_icon_path(
    tables: tuple[bytes, bytes],
    walked: dict[int, tuple[PabrOffsetRow, _Walked]],
) -> None:
    """The scan keeps every well-formed walked icon, and finds none where the walk has none."""
    index = build_character_icon_index(*tables)

    for character_id, (_, record) in walked.items():
        scanned = index.get(character_id)
        if not record.icon_path:
            assert scanned is None, character_id
        elif _ICON_FILE.fullmatch(record.icon_path):
            assert scanned is not None and scanned.endswith(record.icon_path.lower()), character_id
