from __future__ import annotations

import struct
from collections.abc import Callable
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _common.string_hash import ascii_key_hash
from .array_layout import CLASS_TYPE_COUNT
from .equip_types import equip_type_name
from .packages import (
    FILE_NAME,
    SECTION_CLASS_PACKAGE,
    SECTION_CUTSCENE,
    SECTION_VEHICLE,
    SECTION_VEHICLE_WEAPON,
    SECTION_WEAPON,
    SECTIONS,
)
from .parser import MAX_CLASS_TYPE_COUNT, MAX_EQUIP_TYPE_COUNT, parse_pcactionpackagename

# Warrior (class type 0) with a Longsword (equip type 1), and the Warrior's cutscene package.
_WARRIOR = 0
_LONGSWORD = 1
_WARRIOR_LONGSWORD = "pc/1_phm/fighteraction_onehandsword"
_WARRIOR_CUTSCENE = "pc/cutscene/fighteraction_cutscene"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "class_type", "class_name", "section", "section_name", "equip_type", "equip_type_name",
                "vehicle_name", "vehicle_name_index", "package", "package_index", "package_hash",
            ]
        ),
        RangeTest(col="class_type", min_val=0, max_val=MAX_CLASS_TYPE_COUNT - 1),
        RangeTest(col="equip_type", min_val=0, max_val=MAX_EQUIP_TYPE_COUNT - 1),
        TargetTest(
            col="package",
            value=_WARRIOR_LONGSWORD,
            expected={
                "class_type": _WARRIOR,
                "class_name": "Warrior",
                "section": SECTION_WEAPON,
                "equip_type": _LONGSWORD,
                "equip_type_name": "LongSword",
            },
        ),
        TargetTest(
            col="package",
            value=_WARRIOR_CUTSCENE,
            expected={"class_type": _WARRIOR, "section": SECTION_CUTSCENE, "equip_type": None, "vehicle_name": None},
        ),
    ],
)


@pytest.fixture(scope="module")
def pcaction_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_pcactionpackagename_bss(spec: Any, pcaction_result: HandlerResult) -> None:
    pcaction_result.check(spec)


@pytest.fixture(scope="module")
def records() -> list[dict]:
    return parse_pcactionpackagename(load_binary_fixture(FILE_NAME))


def test_every_hash_is_the_ascii_key_hash_of_its_package(records: list[dict]) -> None:
    wrong = [r["package"] for r in records if r["package_hash"] != ascii_key_hash(r["package"])]
    assert not wrong, wrong[:5]


def test_every_section_is_present(records: list[dict]) -> None:
    assert {r["section"] for r in records} == set(SECTIONS)


def test_equip_type_and_vehicle_follow_the_section(records: list[dict]) -> None:
    has_equip = {SECTION_WEAPON, SECTION_VEHICLE_WEAPON}
    has_vehicle = {SECTION_VEHICLE, SECTION_VEHICLE_WEAPON}
    for record in records:
        assert (record["equip_type"] is not None) == (record["section"] in has_equip), record
        assert bool(record["vehicle_name"]) == (record["section"] in has_vehicle), record


def test_class_packages_sit_in_the_folder_of_their_class(records: list[dict]) -> None:
    folders: dict[int, set[str]] = {}
    for record in records:
        if record["section"] == SECTION_WEAPON:
            folders.setdefault(record["class_type"], set()).add(_folder(record["package"]))
    for record in records:
        if record["section"] == SECTION_CLASS_PACKAGE:
            assert _folder(record["package"]) in folders.get(record["class_type"], set()), record


def _folder(package: str) -> str:
    return package.split("/", 2)[1]


def test_equip_type_names_come_from_the_enum_and_the_sheet() -> None:
    assert equip_type_name(_LONGSWORD) == "LongSword"
    assert equip_type_name(53) == "HuntRifle"
    assert equip_type_name(63) == "Kriegsmesser"
    assert equip_type_name(MAX_EQUIP_TYPE_COUNT - 1) == ""
    assert equip_type_name(None) == ""


_U32 = struct.Struct("<I")
_CELL = struct.Struct("<II")
_VEHICLE_ROW = struct.Struct("<III")
_CLASS_PACKAGE_ROW = struct.Struct("<BII")
_STRINGS = ["", "pc/1_phm/test_package", "Horse", "pc/1_phm/test_horse", "pc/cutscene/test_cutscene"]
_EMPTY_STRING, _PACKAGE_STRING, _HORSE_STRING, _HORSE_PACKAGE_STRING, _CUTSCENE_STRING = range(len(_STRINGS))
_LIST_CLASS = 2


def _cell(index: int) -> bytes:
    text = _STRINGS[index]
    return _CELL.pack(index, ascii_key_hash(text) if text else 0)


def _class_block(class_type: int, equip_type_count: int, has_cutscene: bool) -> bytes:
    """Block 0 holds a Longsword cell, a horse row and a cutscene package; every other block is empty."""
    is_filled = class_type == _WARRIOR
    cells = b"".join(
        _cell(_PACKAGE_STRING if is_filled and equip_type == _LONGSWORD else _EMPTY_STRING)
        for equip_type in range(equip_type_count)
    )
    horse = _VEHICLE_ROW.pack(_HORSE_STRING, _HORSE_PACKAGE_STRING, ascii_key_hash(_STRINGS[_HORSE_PACKAGE_STRING]))
    vehicles = _U32.pack(1) + horse if is_filled else _U32.pack(0)
    vehicle_weapons = _U32.pack(0) * equip_type_count
    cutscene = _cell(_CUTSCENE_STRING if is_filled else _EMPTY_STRING) if has_cutscene else b""
    return cells + vehicles + vehicle_weapons + cutscene


def _file(
    *,
    class_type_count: int = 3,
    equip_type_count: int = 5,
    class_package_count: int | None = 1,
    has_cutscene: bool = True,
    magic: bytes = b"PABR",
) -> bytes:
    """The class blocks, then a class package list of one row unless `class_package_count` is None.

    A `class_package_count` other than 1 makes the stored count disagree with the one row.
    """
    blocks = b"".join(
        _class_block(class_type, equip_type_count, has_cutscene) for class_type in range(class_type_count)
    )
    body = magic + blocks
    if class_package_count is not None:
        row = _CLASS_PACKAGE_ROW.pack(_LIST_CLASS, _PACKAGE_STRING, ascii_key_hash(_STRINGS[_PACKAGE_STRING]))
        body += _U32.pack(class_package_count) + row
    return body + _string_table(_STRINGS) + _U32.pack(len(body)) + bytes(4)


def _string_table(strings: list[str]) -> bytes:
    entries = b"".join(bytes([0]) + _U32.pack(len(text)) + text.encode("ascii") for text in strings)
    return _U32.pack(len(strings)) + entries


def _summary(parsed: list[dict]) -> list[tuple]:
    return [(r["class_type"], r["section"], r["equip_type"], r["vehicle_name"], r["package"]) for r in parsed]


@pytest.mark.parametrize("equip_type_count", [2, 5, 9])
def test_the_equip_type_count_comes_from_the_file(equip_type_count: int) -> None:
    parsed = parse_pcactionpackagename(_file(equip_type_count=equip_type_count))
    assert _summary(parsed) == [
        (_WARRIOR, SECTION_WEAPON, _LONGSWORD, None, _STRINGS[_PACKAGE_STRING]),
        (_WARRIOR, SECTION_VEHICLE, None, "Horse", _STRINGS[_HORSE_PACKAGE_STRING]),
        (_WARRIOR, SECTION_CUTSCENE, None, None, _STRINGS[_CUTSCENE_STRING]),
        (_LIST_CLASS, SECTION_CLASS_PACKAGE, None, None, _STRINGS[_PACKAGE_STRING]),
    ]


def test_a_file_without_the_class_package_list_reads() -> None:
    parsed = parse_pcactionpackagename(_file(class_package_count=None))
    assert SECTION_CLASS_PACKAGE not in {r["section"] for r in parsed}
    assert len(parsed) == 3


def test_an_empty_class_package_list_reads() -> None:
    blocks = _file(class_package_count=None)
    # Same file with a u32 list count of 0 in front of the string table.
    end = _U32.unpack_from(blocks, len(blocks) - 8)[0]
    data = blocks[:end] + _U32.pack(0) + blocks[end:-8] + _U32.pack(end + _U32.size) + bytes(4)
    assert len(parse_pcactionpackagename(data)) == 3


def test_a_list_count_that_disagrees_with_its_rows_is_rejected() -> None:
    with pytest.raises(ValueError, match="fits no class block"):
        parse_pcactionpackagename(_file(class_package_count=2))


def test_a_file_without_magic_that_is_no_array_layout_is_rejected() -> None:
    with pytest.raises(ValueError, match="no PABR magic"):
        parse_pcactionpackagename(_file(magic=b"XXXX"))


def test_class_blocks_without_the_cutscene_cell_read() -> None:
    parsed = parse_pcactionpackagename(_file(class_package_count=None, has_cutscene=False))
    assert _summary(parsed) == [
        (_WARRIOR, SECTION_WEAPON, _LONGSWORD, None, _STRINGS[_PACKAGE_STRING]),
        (_WARRIOR, SECTION_VEHICLE, None, "Horse", _STRINGS[_HORSE_PACKAGE_STRING]),
    ]


def test_a_hash_that_does_not_match_its_path_is_rejected() -> None:
    data = bytearray(_file())
    # The first cell of class block 1 points at the empty string, whose stored hash is 0.
    block_size = len(_class_block(_WARRIOR, 5, True))
    _U32.pack_into(data, len(b"PABR") + block_size + _U32.size, 1)
    with pytest.raises(ValueError, match="not the hash of its path"):
        parse_pcactionpackagename(bytes(data))


# Clients 435 to 829 store arrays: [class][equip type] and [class][vehicle type] names, one
# map per class, then the same arrays of hashes.
_ARRAY_STRINGS = ["", "pc/1_phm/test_package", "pc/vehicle/ridinghorse/test_horse", "pc/vehicle/horse/test_weapon"]
_ARRAY_EMPTY, _ARRAY_WEAPON, _ARRAY_VEHICLE, _ARRAY_VEHICLE_WEAPON = range(len(_ARRAY_STRINGS))
_HORSE = 0
_ARRAY_EQUIP_TYPES = 3
_ARRAY_VEHICLE_TYPES = 2


def _hash(text: str) -> int:
    return ascii_key_hash(text) if text else 0


def _array_map(row_tail: bytes) -> bytes:
    """A map of one horse with Longsword row, `row_tail` after its key."""
    return _U32.pack(1) + bytes([_HORSE, _LONGSWORD]) + row_tail


def _array_body(name: Callable[[int], bytes]) -> bytes:
    """The Warrior holds a Longsword package, a horse package and a horse with Longsword package."""
    weapons = [_ARRAY_EMPTY] * (CLASS_TYPE_COUNT * _ARRAY_EQUIP_TYPES)
    weapons[_WARRIOR * _ARRAY_EQUIP_TYPES + _LONGSWORD] = _ARRAY_WEAPON
    vehicles = [_ARRAY_EMPTY] * (CLASS_TYPE_COUNT * _ARRAY_VEHICLE_TYPES)
    vehicles[_WARRIOR * _ARRAY_VEHICLE_TYPES + _HORSE] = _ARRAY_VEHICLE
    cells = weapons + vehicles
    empty_maps = _U32.pack(0) * (CLASS_TYPE_COUNT - 1)
    maps = _array_map(name(_ARRAY_VEHICLE_WEAPON)) + empty_maps
    hash_maps = _array_map(_U32.pack(_hash(_ARRAY_STRINGS[_ARRAY_VEHICLE_WEAPON]))) + empty_maps
    hashes = b"".join(_U32.pack(_hash(_ARRAY_STRINGS[index])) for index in cells)
    return b"".join(name(index) for index in cells) + maps + hashes + hash_maps


def _str8(index: int) -> bytes:
    text = _ARRAY_STRINGS[index].encode("ascii")
    return struct.pack("<Q", len(text)) + text


def _indexed_array_file() -> bytes:
    body = b"PABR" + _array_body(_U32.pack)
    return body + _string_table(_ARRAY_STRINGS) + _U32.pack(len(body)) + bytes(4)


_ARRAY_SUMMARY = [
    (_WARRIOR, SECTION_WEAPON, _LONGSWORD, None, _ARRAY_STRINGS[_ARRAY_WEAPON]),
    (_WARRIOR, SECTION_VEHICLE, None, "Horse", _ARRAY_STRINGS[_ARRAY_VEHICLE]),
    (_WARRIOR, SECTION_VEHICLE_WEAPON, _LONGSWORD, "Horse", _ARRAY_STRINGS[_ARRAY_VEHICLE_WEAPON]),
]


def test_arrays_of_inline_names_read() -> None:
    parsed = parse_pcactionpackagename(_array_body(_str8))
    assert _summary(parsed) == _ARRAY_SUMMARY
    assert {r["package_index"] for r in parsed} == {None}


def test_arrays_of_string_indices_read() -> None:
    parsed = parse_pcactionpackagename(_indexed_array_file())
    assert _summary(parsed) == _ARRAY_SUMMARY
    assert [r["package_index"] for r in parsed] == [_ARRAY_WEAPON, _ARRAY_VEHICLE, _ARRAY_VEHICLE_WEAPON]
