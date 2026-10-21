from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME


_WARRIOR = 0
_TEXTURE_PREFIX = "Combine_Etc_Minigame_Icon_Profile_"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["class_type", "class_type_dup", "texture_id", "class_name"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="class_type", value=_WARRIOR, expected={"class_type_dup": _WARRIOR, "class_name": "Warrior"}),
        UserLanguageTest(fields=["class_name"]),
    ],
)


@pytest.fixture(scope="module")
def yachtclasstypetextureinfo_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_yachtclasstypetextureinfo_dbss(spec: Any, yachtclasstypetextureinfo_result: HandlerResult) -> None:
    yachtclasstypetextureinfo_result.check(spec)


def test_keys_repeat_inside_each_row(yachtclasstypetextureinfo_result: HandlerResult) -> None:
    for r in yachtclasstypetextureinfo_result.records:
        assert r["class_type_dup"] == r["class_type"], r["class_type"]


def test_class_types_are_unique(yachtclasstypetextureinfo_result: HandlerResult) -> None:
    keys = [r["class_type"] for r in yachtclasstypetextureinfo_result.records]
    assert len(keys) == len(set(keys)), "a class type has two rows"


def test_every_texture_is_a_profile_icon(yachtclasstypetextureinfo_result: HandlerResult) -> None:
    for r in yachtclasstypetextureinfo_result.records:
        assert r["texture_id"].startswith(_TEXTURE_PREFIX), r["texture_id"]
