from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.lookup_index import IndexKind
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

# A fence placed by exactly one item, the link the CHARACTER_ITEM index keeps.
_FENCE_CHARACTER = 2053
_FENCE_ITEM = 58011

OBJECT_CASE = HandlerCase(
    handler_name="characterobject.dbss",
    data_file="characterobject.dbss",
    companion_files={"characterobjectoffset.dbss": "characterobjectoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name"],
    internal_path="gamecommondata/binary/characterobject.dbss",
    lookup_indexes={IndexKind.CHARACTER_ITEM: {_FENCE_CHARACTER: _FENCE_ITEM}},
    tests=[
        SchemaTest(
            required_keys=[
                "character_id", "icon_path", "name", "item_id", "item_name",
                "object_kind", "model_path",
            ]
        ),
        # The data file's own count; the parser walks the offset table's rows.
        DeclaredCountTest(declared=header_count()),
        TargetTest(
            col="character_id",
            value=16111,
            expected={
                "name": "Golden Hand Vase",
                "object_kind": 2,
                "model_path": "00_Common/Pot/Pot_Base_48.pam",
                # Not in the installed index, so no item and a dash.
                "item_id": None,
                "item_name": "",
            },
        ),
        TargetTest(
            col="character_id",
            value=_FENCE_CHARACTER,
            expected={"item_id": _FENCE_ITEM, "item_name": "[Event] Fence"},
        ),
        TargetTest(
            col="character_id",
            value=16640,
            expected={"object_kind": 2, "model_path": "Weed_Sunflower_01.srt"},
        ),
        TargetTest(
            col="character_id",
            value=1001,
            expected={
                "name": "Metal Processing Tool",
                "object_kind": 2,
                "model_path": "00_Common/Crafting/Crafting_Smithing_01.pam",
            },
        ),
        TargetTest(
            col="character_id",
            value=2101,
            expected={
                "object_kind": 5,
                "object_kind_name": "InnRoom",
                "model_path": "02_balenos/velia/balenos_velia_str_house_05.pam",
            },
        ),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="characterobjectoffset.dbss",
    data_file="characterobjectoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/characterobjectoffset.dbss",
    tests=[
        SchemaTest(required_keys=["character_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        # The first record follows the data file's u32 count; offsets point at the record's own ID.
        TargetTest(col="offset", value=4, expected={}),
    ],
)


@pytest.fixture(scope="module")
def object_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OBJECT_RESULT", None)
    if result is None:
        result = run_case(replace(OBJECT_CASE, tests=[]))
        request.module._OBJECT_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", OBJECT_CASE.tests, ids=case_id)
def test_characterobject(spec: Any, object_result: HandlerResult) -> None:
    object_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_characterobjectoffset(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)
