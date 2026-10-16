from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)


_HEADER_SIZE = 4
_RECORD_SIZE = 12
_RESERVED_SLOTS = 200
_RESERVED_SLOT = struct.pack("<4I", 200, 0, 0, 0)


def _catalog_rows() -> DeclaredCount:
    """Skill rows: the bytes between the magic and the 200 null reserved slots
    that end at the trailer's data_end, in 12-byte records."""

    def read(source: CaseInput) -> int:
        raw = source.file(None)
        data_end = struct.unpack_from("<I", raw, len(raw) - 8)[0]
        reserved_start = data_end - _RESERVED_SLOTS * len(_RESERVED_SLOT)
        catalog_size = reserved_start - _HEADER_SIZE
        if data_end != len(raw) - 12 or catalog_size < 0 or catalog_size % _RECORD_SIZE:
            raise AssertionError(f"data_end 0x{data_end:X} does not leave whole records in {len(raw)} bytes")
        if raw[reserved_start:data_end] != _RESERVED_SLOT * _RESERVED_SLOTS:
            raise AssertionError(f"the {_RESERVED_SLOTS} slots before 0x{data_end:X} are not all null")
        return catalog_size // _RECORD_SIZE

    return read


_ICON_DIR = "ui_texture/icon/new_icon/08_servant_skill/02_pet"

CASE = HandlerCase(
    handler_name="fairyequipskill.bss",
    data_file="fairyequipskill.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Skill Name", "Description"],
    internal_path="gamecommondata/binary/fairyequipskill.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "equip_skill_id",
                "skill_type",
                "unknown_08",
                "unknown_09",
                "loc_id",
                "skill_name",
                "skill_description",
                "icon_path",
            ],
        ),
        # The 200 null reserved slots must be skipped.
        DeclaredCountTest(declared=_catalog_rows()),
        RangeTest(col="unknown_09", min_val=0, max_val=0),
        TargetTest(
            col="equip_skill_id",
            value=0,
            expected={
                "skill_type": 1,
                "loc_id": 49096,
                "skill_name": "Tingling Breath I",
                "icon_path": f"{_ICON_DIR}/equipskill_fairy_00049096.dds",
            },
        ),
        # Fairy's Tear is the one group whose loc_ids descend as ids ascend.
        TargetTest(
            col="equip_skill_id",
            value=10,
            expected={
                "skill_type": 3,
                "loc_id": 49114,
                "skill_name": "Fairy's Tear I",
            },
        ),
        TargetTest(
            col="equip_skill_id",
            value=13,
            expected={
                "skill_type": 3,
                "loc_id": 49111,
                "skill_name": "Fairy's Tear IV",
            },
        ),
        # Single-record skill groups.
        TargetTest(
            col="loc_id",
            value=49120,
            expected={
                "equip_skill_id": 19,
                "skill_type": 5,
                "skill_name": "Morning Star",
            },
        ),
        TargetTest(
            col="equip_skill_id",
            value=29,
            expected={
                "skill_type": 7,
                "loc_id": 49130,
                "skill_name": "Gift",
            },
        ),
        # Legacy and current naming coexist inside skill type 6.
        TargetTest(
            col="loc_id",
            value=49121,
            expected={
                "equip_skill_id": 20,
                "skill_type": 6,
                "skill_name": "Miraculous Cheer 10 Seconds",
            },
        ),
        TargetTest(
            col="loc_id",
            value=49129,
            expected={
                "equip_skill_id": 28,
                "skill_type": 6,
                "skill_name": "Miraculous Cheer V",
            },
        ),
        TargetTest(
            col="equip_skill_id",
            value=34,
            expected={
                "skill_type": 8,
                "loc_id": 49181,
                "skill_name": "Continuous Care V",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def fairyequipskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_fairyequipskill_bss(
    spec: Any,
    fairyequipskill_result: HandlerResult,
) -> None:
    fairyequipskill_result.check(spec)
