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
from .parser import (
    CLASS_TYPE_COUNT,
    EQUIP_TYPE_COUNT,
    FILE_NAME,
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
                "class_type", "class_name", "section", "section_name", "equip_type",
                "vehicle_name", "vehicle_name_index", "package", "package_index", "package_hash",
            ]
        ),
        RangeTest(col="class_type", min_val=0, max_val=CLASS_TYPE_COUNT - 1),
        RangeTest(col="equip_type", min_val=0, max_val=EQUIP_TYPE_COUNT - 1),
        TargetTest(
            col="package",
            value=_WARRIOR_LONGSWORD,
            expected={"class_type": _WARRIOR, "class_name": "Warrior", "section": SECTION_WEAPON, "equip_type": _LONGSWORD},
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


_U32 = struct.Struct("<I")
_CELL = struct.Struct("<II")
_CLASS_PACKAGE_ROW = struct.Struct("<BII")
_EMPTY_STRING = 0
_PACKAGE_STRING = 1
_PACKAGE = "pc/1_phm/test_package"


def _string_table(strings: list[str]) -> bytes:
    entries = b"".join(bytes([0]) + _U32.pack(len(text)) + text.encode("ascii") for text in strings)
    return _U32.pack(len(strings)) + entries


def _file(*, magic: bytes = b"PABR", class_package_count: int = 0) -> bytes:
    """Every class block empty but Warrior's Longsword cell, then the class package list."""
    blocks = bytearray()
    for class_type in range(CLASS_TYPE_COUNT):
        for equip_type in range(EQUIP_TYPE_COUNT):
            if (class_type, equip_type) == (_WARRIOR, _LONGSWORD):
                blocks += _CELL.pack(_PACKAGE_STRING, ascii_key_hash(_PACKAGE))
            else:
                blocks += _CELL.pack(_EMPTY_STRING, 0)
        blocks += _U32.pack(0)
        blocks += _U32.pack(0) * EQUIP_TYPE_COUNT
        blocks += _CELL.pack(_EMPTY_STRING, 0)
    rows = _CLASS_PACKAGE_ROW.pack(6, _PACKAGE_STRING, ascii_key_hash(_PACKAGE))
    body = magic + bytes(blocks) + _U32.pack(class_package_count) + rows
    return body + _string_table(["", _PACKAGE]) + _U32.pack(len(body)) + bytes(4)


def test_empty_cells_get_no_record() -> None:
    parsed = parse_pcactionpackagename(_file(class_package_count=1))
    assert [(r["class_type"], r["section"], r["equip_type"], r["package"]) for r in parsed] == [
        (_WARRIOR, SECTION_WEAPON, _LONGSWORD, _PACKAGE),
        (6, SECTION_CLASS_PACKAGE, None, _PACKAGE),
    ]


def test_blocks_short_of_the_string_table_are_rejected() -> None:
    with pytest.raises(ValueError, match="string table starts"):
        parse_pcactionpackagename(_file(class_package_count=0))


def test_a_list_past_the_string_table_is_rejected() -> None:
    with pytest.raises(ValueError, match="runs past"):
        parse_pcactionpackagename(_file(class_package_count=2))


def test_a_bad_magic_is_rejected() -> None:
    with pytest.raises(ValueError, match="invalid magic"):
        parse_pcactionpackagename(_file(magic=b"XXXX", class_package_count=1))
