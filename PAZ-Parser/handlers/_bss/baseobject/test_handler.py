from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.pabr_offset import parse_pabr_offset_rows
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from .installation_types import INSTALLATION_TYPE_NAMES
from .parser import FILE_NAME, KEY_FIELD, PLACE_FLAG_FIELDS, parse_baseobject_records


_COUNT_OFFSET = 4
_OBJECT_OFFSET_FILE = "characterobjectoffset.dbss"
_IDENTITY = [[1.0 if row == col else 0.0 for col in range(4)] for row in range(4)]
_NO_HOUSE_NUMBER = -1
# gc::ObjectKind values of the 2016 client.
_KIND_INSTALLATION = 2
_KIND_INN_ROOM = 5
_INSTALLATION_TYPE_MAID = 30
# Morning Light Nampo 1, a house with hull layers; Golden Hand Vase, a vase.
_NAMPO_HOUSE = 3823
_GOLDEN_HAND_VASE = 16111
# [Oasis] Ethan the Butler, a maid doll.
_OASIS_ETHAN = 18977

_FLAG_TESTS = [RangeTest(col=field, min_val=0, max_val=1) for field in ("is_collision", "is_siege_tent", "unknown_8b", *PLACE_FLAG_FIELDS)]

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                KEY_FIELD,
                "armor_material",
                "object_kind",
                "installation_type",
                "unknown_05",
                "unknown_45",
                "unknown_85",
                "is_collision",
                "is_siege_tent",
                "unknown_8b",
                "layer_count",
                "unknown_90",
                "hull_count",
                "face_count",
                "unknown_layers_00",
                *PLACE_FLAG_FIELDS,
                "icon_path",
                "name",
                "object_kind_name",
                "installation_type_name",
                "placement",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="installation_type", min_val=0, max_val=len(INSTALLATION_TYPE_NAMES) - 1),
        *_FLAG_TESTS,
        TargetTest(
            col=KEY_FIELD,
            value=_NAMPO_HOUSE,
            expected={"object_kind": _KIND_INN_ROOM, "object_kind_name": "InnRoom"},
        ),
        TargetTest(
            col=KEY_FIELD,
            value=_GOLDEN_HAND_VASE,
            expected={"object_kind": _KIND_INSTALLATION, "layer_count": 0, "unknown_05": _IDENTITY},
        ),
        TargetTest(
            col=KEY_FIELD,
            value=_OASIS_ETHAN,
            expected={"installation_type": _INSTALLATION_TYPE_MAID, "installation_type_name": "Maid"},
        ),
    ],
)


@pytest.fixture(scope="module")
def baseobject_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_baseobject_bss(spec: Any, baseobject_result: HandlerResult) -> None:
    baseobject_result.check(spec)


def test_keys_are_the_characterobject_keys(baseobject_result: HandlerResult) -> None:
    keys = [record[KEY_FIELD] for record in baseobject_result.records]
    object_keys = {row.entry_id for row in parse_pabr_offset_rows(load_binary_fixture(_OBJECT_OFFSET_FILE))}
    assert len(keys) == len(set(keys))
    assert set(keys) == object_keys


def test_both_layer_counts_agree(baseobject_result: HandlerResult) -> None:
    wrong = [record[KEY_FIELD] for record in baseobject_result.records if record["layer_count"] != record["unknown_90"]]
    assert not wrong, wrong[:5]


def test_only_houses_carry_matrices_and_a_house_number(baseobject_result: HandlerResult) -> None:
    """A row without hull layers keeps both identity matrices and no house number."""
    wrong = [
        record[KEY_FIELD]
        for record in baseobject_result.records
        if record["layer_count"] == 0
        and (record["unknown_05"] != _IDENTITY or record["unknown_45"] != _IDENTITY or record["unknown_85"] != _NO_HOUSE_NUMBER)
    ]
    assert not wrong, wrong[:5]


_HEAD = struct.Struct("<HBBB16f16fiBBBII")
_TAIL = struct.Struct("<H6B")
_FACE_SIZE = 140
_FLAT_IDENTITY = [value for row in _IDENTITY for value in row]


def _pabr(rows: bytes, row_count: int) -> bytes:
    """A PABR file around `rows` with an empty string table."""
    rows_end = 8 + len(rows)
    return b"PABR" + struct.pack("<I", row_count) + rows + struct.pack("<III", 0, rows_end, 0)


def _row(character_id: int, layers: list[list[int]], place_flags: tuple[int, ...]) -> bytes:
    """One row; `layers` lists the face count of each hull per layer."""
    head = _HEAD.pack(character_id, 100, 5, 0, *_FLAT_IDENTITY, *_FLAT_IDENTITY, 7, 1, 0, 0, len(layers), len(layers))
    body = b"".join(
        struct.pack("<I", len(hulls)) + b"".join(struct.pack("<I", faces) + bytes(faces * _FACE_SIZE) for faces in hulls)
        for hulls in layers
    )
    return head + body + _TAIL.pack(0, *place_flags)


def test_a_small_table_reads_back() -> None:
    rows = _row(3823, [[12, 12], [4]], (0, 1, 1, 0, 0, 0)) + _row(16111, [], (1, 0, 1, 0, 1, 0))
    house, vase = parse_baseobject_records(_pabr(rows, 2))

    assert (house[KEY_FIELD], house["object_kind"], house["layer_count"], house["unknown_90"]) == (3823, 5, 2, 2)
    assert (house["hull_count"], house["face_count"], house["unknown_85"]) == (3, 28, 7)
    assert (house["is_outside"], house["is_floor"], house["is_inside"]) == (1, 1, 0)
    assert house["unknown_05"] == _IDENTITY
    assert (vase[KEY_FIELD], vase["layer_count"], vase["face_count"], vase["is_on_the_table"]) == (16111, 0, 0, 1)


def test_rows_that_do_not_end_at_the_string_table_fail() -> None:
    row = _row(1, [[12]], (0,) * 6)
    with pytest.raises(ValueError):
        parse_baseobject_records(_pabr(row + b"\x00", 1))
    with pytest.raises(ValueError):
        parse_baseobject_records(_pabr(row[:-1], 1))
