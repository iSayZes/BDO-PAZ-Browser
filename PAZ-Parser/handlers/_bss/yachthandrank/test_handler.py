from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
# Hand rank 12 is Yar!, five equal cards (the HandRanking sheet of client 1784).
_YAR = 12
_FIVE_OF_A_KIND = 5
_TEXTURE_PREFIX = "Combine_Etc_Minigame_Yatzee_Icon_"
_MAX_EYE = 6

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "desc"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "hand_rank_key", "unknown_04", "unknown_0d", "unknown_11", "target_eye", "target_count",
            "straight_count", "is_full_house", "is_two_pair", "made_point", "is_sum_point",
            "icon_texture_index", "icon_texture", "name_kr_index", "name_kr", "desc_kr_index", "desc_kr",
            "name", "desc",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="target_eye", min_val=0, max_val=_MAX_EYE),
        RangeTest(col="is_full_house", min_val=0, max_val=1),
        RangeTest(col="is_two_pair", min_val=0, max_val=1),
        RangeTest(col="is_sum_point", min_val=0, max_val=1),
        TargetTest(col="hand_rank_key", value=_YAR, expected={"target_count": _FIVE_OF_A_KIND, "name": "Yar!"}),
        UserLanguageTest(fields=["name", "desc"]),
    ],
)


@pytest.fixture(scope="module")
def yachthandrank_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_yachthandrank_bss(spec: Any, yachthandrank_result: HandlerResult) -> None:
    yachthandrank_result.check(spec)


def test_hand_rank_keys_are_unique(yachthandrank_result: HandlerResult) -> None:
    keys = [r["hand_rank_key"] for r in yachthandrank_result.records]
    assert len(keys) == len(set(keys)), "a key has two rows"


def test_every_row_has_its_strings(yachthandrank_result: HandlerResult) -> None:
    for r in yachthandrank_result.records:
        assert r["icon_texture"].startswith(_TEXTURE_PREFIX), r["hand_rank_key"]
        assert r["name_kr"] and r["desc_kr"], r["hand_rank_key"]
