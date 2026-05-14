from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


PETACTION_CASE = HandlerCase(
    handler_name="petaction.dbss",
    data_file="petaction.dbss",
    companion_files={"petactionoffset.dbss": "petactionoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["action_name"],
    internal_path="gamecommondata/binary/petaction.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "action_id",
                "action_name",
                "icon_action_name",
                "action_group",
                "icon_path",
                "icon_hashes",
                "record_offset",
                "record_size",
                "trailing_zeroes",
                "action_id_match",
            ]
        ),
        CountTest(expected=10),
        PosTest(
            pos=0,
            expected={
                "action_id": 0,
                "action_name": "Joy",
                "icon_action_name": "Like",
                "action_group": 2,
                "icon_path": "New_Icon/08_Servant_Skill/02_Pet/Action_0_Like.dds",
                "icon_hashes_hex": "0xC068AE30",
                "trailing_zeroes": True,
                "action_id_match": True,
            },
        ),
        TargetTest(
            col="action_id",
            value=7,
            expected={
                "action_name": "Crouch",
                "icon_action_name": "Play2",
                "action_group": 4,
                "icon_path": "New_Icon/08_Servant_Skill/02_Pet/Action_7_Play2.dds",
                "icon_hashes_hex": "0xD06CC6C5, 0xAE30B9AC",
            },
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="petactionoffset.dbss",
    data_file="petactionoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petactionoffset.dbss",
    tests=[
        SchemaTest(required_keys=["action_id", "record_offset", "record_size"]),
        CountTest(expected=10),
        PosTest(pos=0, expected={"action_id": 0, "record_offset": 0}),
        PosTest(pos=-1, expected={"action_id": 9}),
    ],
)


@pytest.fixture(scope="module")
def petaction_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PETACTION_RESULT", None)
    if result is None:
        result = run_case(replace(PETACTION_CASE, tests=[]))
        request.module._PETACTION_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", PETACTION_CASE.tests, ids=case_id)
def test_petaction_dbss(spec: Any, petaction_result: HandlerResult) -> None:
    spec.check(petaction_result.records)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_petactionoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    spec.check(offset_result.records)
