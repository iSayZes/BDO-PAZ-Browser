from __future__ import annotations

import struct
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
from .equip_types import equip_type_name
from .parser import (
    FILE_NAME,
    MAX_CLASS_TYPE_COUNT,
    MAX_EQUIP_TYPE_COUNT,
    SECTION_CLASS_PACKAGE,
    SECTION_CUTSCENE,
    SECTION_VEHICLE,
    SECTION_VEHICLE_WEAPON,
    SECTION_WEAPON,
    SECTIONS,
    parse_pcactionpackagename,
)

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


def _class_block(class_type: int, equip_type_count: int) -> bytes:
    """Block 0 holds a Longsword cell, a horse row and a cutscene package; every other block is empty."""
    is_filled = class_type == _WARRIOR
    cells = b"".join(
        _cell(_PACKAGE_STRING if is_filled and equip_type == _LONGSWORD else _EMPTY_STRING)
        for equip_type in range(equip_type_count)
    )
    horse = _VEHICLE_ROW.pack(_HORSE_STRING, _HORSE_PACKAGE_STRING, ascii_key_hash(_STRINGS[_HORSE_PACKAGE_STRING]))
    vehicles = _U32.pack(1) + horse if is_filled else _U32.pack(0)
    vehicle_weapons = _U32.pack(0) * equip_type_count
    cutscene = _cell(_CUTSCENE_STRING if is_filled else _EMPTY_STRING)
    return cells + vehicles + vehicle_weapons + cutscene


def _file(
    *,
    class_type_count: int = 3,
    equip_type_count: int = 5,
    class_package_count: int | None = 1,
    magic: bytes = b"PABR",
) -> bytes:
    """The class blocks, then a class package list of one row unless `class_package_count` is None.

    A `class_package_count` other than 1 makes the stored count disagree with the one row.
    """
    blocks = b"".join(_class_block(class_type, equip_type_count) for class_type in range(class_type_count))
    body = magic + blocks
    if class_package_count is not None:
        row = _CLASS_PACKAGE_ROW.pack(_LIST_CLASS, _PACKAGE_STRING, ascii_key_hash(_STRINGS[_PACKAGE_STRING]))
        body += _U32.pack(class_package_count) + row
    entries = b"".join(bytes([0]) + _U32.pack(len(text)) + text.encode("ascii") for text in _STRINGS)
    return body + _U32.pack(len(_STRINGS)) + entries + _U32.pack(len(body)) + bytes(4)


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


def test_a_bad_magic_is_rejected() -> None:
    with pytest.raises(ValueError, match="invalid magic"):
        parse_pcactionpackagename(_file(magic=b"XXXX"))
