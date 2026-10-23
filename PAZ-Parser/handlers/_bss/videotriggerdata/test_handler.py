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
    case_id,
    header_count,
    run_case,
)

from _bss.sequence_scripts.reader import SCRIPT_FIELDS
from _common.string_hash import ascii_key_hash
from .parser import FILE_NAME


_PABR_COUNT_OFFSET = 4
# The video of `ui_movie/pc/intro/intro.bk2`.
_INTRO = "Intro"

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "video_name_hash", "video_name", *SCRIPT_FIELDS, "position", "video_name_hash_dup",
            "radius", "contents_group_open", "unknown_2c",
        ]),
        DeclaredCountTest(declared=header_count(offset=_PABR_COUNT_OFFSET)),
        TargetTest(col="video_name", value=_INTRO, expected={"video_name_hash": ascii_key_hash(_INTRO)}),
        RangeTest(col="unknown_2c", min_val=0, max_val=1),
    ],
)


@pytest.fixture(scope="module")
def video_trigger_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_videotriggerdata_bss(spec: Any, video_trigger_result: HandlerResult) -> None:
    video_trigger_result.check(spec)


def test_both_hashes_are_the_name_hash(video_trigger_result: HandlerResult) -> None:
    """`video_name_hash` and its copy are the ASCII key hash of `video_name`."""
    for r in video_trigger_result.records:
        assert r["video_name_hash"] == ascii_key_hash(r["video_name"]), r["video_name"]
        assert r["video_name_hash_dup"] == r["video_name_hash"], r["video_name"]


def test_contents_groups_are_decimal_keys(video_trigger_result: HandlerResult) -> None:
    for r in video_trigger_result.records:
        assert r["contents_group_open"] == "" or r["contents_group_open"].isdigit(), r["video_name"]
