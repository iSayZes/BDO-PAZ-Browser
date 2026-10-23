from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
from _dbss.itemeffectchange.parser import FILE_NAME as EFFECT_CHANGE_FILE
from _dbss.itemeffectchange.parser import parse_itemeffectchange_records
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

from .parser import FILE_NAME, KEY_FIELD, parse_itemmesh_records


_COUNT_OFFSET = 0
_TAIL = struct.Struct("<QI5B")
# Highest `Adult` value the developer comment on the Item_Mesh_Table sheet names (15 and over).
_ADULT_MAX = 3
# The one-handed sword mesh of itemeffectchange.dbss (21 levels), worn by
# Blackstar Longsword as a Warrior (itemenchant.dbss class entry).
_SWORD_MESH = 336000
_SWORD_MODEL = "1_pc/1_phm/weapon/1_onehandsword/phm_01_ohs_0017_r.pac"
_BLACKSTAR_LONGSWORD = 715001
_BLACKSTAR_LONGSWORD_NAME = "Blackstar Longsword"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    lookup_indexes={IndexKind.MESH_KEY_ITEMS: {_SWORD_MESH: (_BLACKSTAR_LONGSWORD,)}},
    tests=[
        SchemaTest(
            required_keys=[
                "mesh_file",
                "effect_file",
                "unknown_effect_file_00",
                KEY_FIELD,
                "weapon_material",
                "unknown_effect_file_0d",
                "armor_material",
                "adult",
                "effects_change_type",
                "item_ids",
                "item_names",
                "item_count",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="adult", min_val=0, max_val=_ADULT_MAX),
        RangeTest(col="effects_change_type", min_val=0, max_val=1),
        TargetTest(
            col=KEY_FIELD,
            value=_SWORD_MESH,
            expected={
                "mesh_file": _SWORD_MODEL,
                "effects_change_type": 1,
                "item_ids": [_BLACKSTAR_LONGSWORD],
                "item_names": [_BLACKSTAR_LONGSWORD_NAME],
                "item_count": 1,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def itemmesh_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemmeshstaticstatus_bss(spec: Any, itemmesh_result: HandlerResult) -> None:
    itemmesh_result.check(spec)


def test_mesh_keys_are_unique(itemmesh_result: HandlerResult) -> None:
    keys = [record[KEY_FIELD] for record in itemmesh_result.records]
    assert len(keys) == len(set(keys))


def test_every_mesh_file_is_a_pac(itemmesh_result: HandlerResult) -> None:
    wrong = [record[KEY_FIELD] for record in itemmesh_result.records if not record["mesh_file"].endswith(".pac")]
    assert not wrong, wrong[:5]


def test_every_level_model_mesh_has_effects_change_type_set(itemmesh_result: HandlerResult) -> None:
    flags = {record[KEY_FIELD]: record["effects_change_type"] for record in itemmesh_result.records}
    level_meshes = {entry["mesh_key"] for entry in parse_itemeffectchange_records(load_binary_fixture(EFFECT_CHANGE_FILE))}
    wrong = sorted(key for key in level_meshes if flags.get(key) != 1)
    assert not wrong, wrong[:5]


def _row(mesh_file: bytes, effect_file: bytes, key: int, numbers: tuple[int, int, int, int, int]) -> bytes:
    return (
        struct.pack("<Q", len(mesh_file)) + mesh_file
        + struct.pack("<Q", len(effect_file)) + effect_file
        + _TAIL.pack(0, key, *numbers)
    )


def test_a_small_table_reads_back() -> None:
    data = struct.pack("<I", 2) + _row(b"a.pac", b"", 7, (3, 0, 0, 0, 1)) + _row(b"b.pac", b"0", 8, (0, 1, 2, 1, 0))

    first, second = parse_itemmesh_records(data)

    assert first == {
        "mesh_file": "a.pac",
        "effect_file": "",
        "unknown_effect_file_00": 0,
        KEY_FIELD: 7,
        "weapon_material": 3,
        "unknown_effect_file_0d": 0,
        "armor_material": 0,
        "adult": 0,
        "effects_change_type": 1,
    }
    assert (second[KEY_FIELD], second["effect_file"], second["armor_material"], second["adult"]) == (8, "0", 2, 1)


def test_rows_that_stop_before_the_end_fail() -> None:
    data = struct.pack("<I", 1) + _row(b"a.pac", b"", 7, (0, 0, 0, 0, 0))
    with pytest.raises(ValueError):
        parse_itemmesh_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_itemmesh_records(data[:-1])
