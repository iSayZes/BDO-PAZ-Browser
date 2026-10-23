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

from _common.contents_group import contents_group_key
from _common.texture_string import TEXTURE_STRING_COMBINE
from .parser import FILE_NAME, parse_contentsschedulerss_records


_STRINGTABLE_FILE = "stringtable.bss"
# The War of the Roses row (contentsschedulerss_bss.md).
_ROSE_WAR = 3

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={
        _STRINGTABLE_FILE: _STRINGTABLE_FILE,
        TEXTURE_STRING_COMBINE: TEXTURE_STRING_COMBINE,
    },
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["title_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "content_type", "title", "icon_texture", "contents_group_count", "contents_group_hashes",
            "title_text", "contents_groups", "icon_path", "icon_region",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        UserLanguageTest(fields=["title_text"]),
        TargetTest(col="content_type", value=_ROSE_WAR, expected={
            "title": "PANEL_ROSEWAR_TITLE",
            "icon_texture": "Combine_TitleIcon_RoseWar",
            "title_text": "War of the Roses",
        }),
    ],
)


@pytest.fixture(scope="module")
def scheduler_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_contentsschedulerss_bss(spec: Any, scheduler_result: HandlerResult) -> None:
    scheduler_result.check(spec)


def test_content_types_are_unique(scheduler_result: HandlerResult) -> None:
    types = [record["content_type"] for record in scheduler_result.records]
    assert len(types) == len(set(types))


def test_every_hash_is_a_contents_group_key(scheduler_result: HandlerResult) -> None:
    # Checks the hash reading: each value is the string hash of a decimal group key.
    for record in scheduler_result.records:
        assert len(record["contents_group_hashes"]) == record["contents_group_count"]
        assert all(contents_group_key(value) is not None for value in record["contents_group_hashes"]), record


def test_every_icon_key_resolves(scheduler_result: HandlerResult) -> None:
    assert all(record["icon_path"] for record in scheduler_result.records)


def test_short_file_raises() -> None:
    with pytest.raises(ValueError):
        parse_contentsschedulerss_records((1).to_bytes(4, "little"))
