from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _bss.worldmapdecostaticstatusmanager.parser import FILE_NAME, KEY_FIELD, parse_worldmapdeco_records


# Index 1 is the Velia model in the client 1784 WorlmapDeco_Table sheet and on client 3482.
_VELIA = 1
_VELIA_MODEL = "WofldMap_Velia_etc_all.pam"
_MODEL_SUFFIX = ".pam"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "deco_index",
                "world_map_object_file",
                "location_x",
                "location_y",
                "location_z",
                "scale",
                "rotation",
                "unknown_world_map_object_file_14",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col=KEY_FIELD, value=_VELIA, expected={"world_map_object_file": _VELIA_MODEL}),
    ],
)


@pytest.fixture(scope="module")
def deco_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_worldmapdecostaticstatusmanager_bss(spec: Any, deco_result: HandlerResult) -> None:
    deco_result.check(spec)


def test_keys_are_unique(deco_result: HandlerResult) -> None:
    keys = [r[KEY_FIELD] for r in deco_result.records]
    assert len(keys) == len(set(keys))


def test_every_model_is_a_pam_file(deco_result: HandlerResult) -> None:
    wrong = [r[KEY_FIELD] for r in deco_result.records if not r["world_map_object_file"].lower().endswith(_MODEL_SUFFIX)]
    assert not wrong, wrong


def _row(key: int, model: str, placement: tuple[float, float, float, float, float], tail: int) -> bytes:
    raw = model.encode("ascii")
    return struct.pack("<HQ", key, len(raw)) + raw + struct.pack("<5fH", *placement, tail)


def test_parse_reads_scale_before_rotation() -> None:
    data = struct.pack("<I", 1) + _row(2049, "A.pam", (1.0, 2.0, 3.0, 100.0, 90.0), 1)

    (record,) = parse_worldmapdeco_records(data)

    assert record == {
        "deco_index": 2049,
        "world_map_object_file": "A.pam",
        "location_x": 1.0,
        "location_y": 2.0,
        "location_z": 3.0,
        "scale": 100.0,
        "rotation": 90.0,
        "unknown_world_map_object_file_14": 1,
    }


def test_parse_rejects_a_short_last_row() -> None:
    data = struct.pack("<I", 1) + _row(1, "A.pam", (0.0, 0.0, 0.0, 100.0, 0.0), 1)[:-1]
    with pytest.raises(ValueError):
        parse_worldmapdeco_records(data)
