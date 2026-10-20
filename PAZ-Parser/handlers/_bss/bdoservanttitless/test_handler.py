from __future__ import annotations

import re
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

from _bss.bdoservanttitless.parser import parse_bdoservanttitless_records


# PABR magic, then the u32 record count.
_COUNT_OFFSET = 4
_NUMBER = re.compile(r"\d+")

CASE = HandlerCase(
    handler_name="bdoservanttitless.bss",
    data_file="bdoservanttitless.bss",
    companion_files={"characterstaticoffset.dbss": "characterstaticoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "title"],
    internal_path="gamecommondata/binary/bdoservanttitless.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "character_id",
                "name",
                "title_name",
                "title_kr",
                "title",
                "contents_option",
                "has_character_row",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        UserLanguageTest(fields=["title"]),
        # The horses checked in game by their Base Coat line (bdoservanttitless_bss.md).
        TargetTest(col="character_id", value=9953, expected={"title_kr": "품종 11번", "title": "Breed 11"}),
        TargetTest(col="character_id", value=31619, expected={"title_kr": "품종 13번", "title": "Breed 13"}),
    ],
)


@pytest.fixture(scope="module")
def titles_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_bdoservanttitless_bss(spec: Any, titles_result: HandlerResult) -> None:
    titles_result.check(spec)


def test_every_title_index_names_a_string(titles_result: HandlerResult) -> None:
    # Checks title_name: an index into the string table, never past it.
    assert all(r["title_kr"] for r in titles_result.records)


def test_loc_title_has_the_breed_number_of_the_string(titles_result: HandlerResult) -> None:
    # Checks the LOC type 111 join: "Breed N" for the row whose string is 품종 N번.
    for r in titles_result.records:
        assert _NUMBER.findall(r["title"]) == _NUMBER.findall(r["title_kr"]), r


def test_character_ids_are_unique(titles_result: HandlerResult) -> None:
    ids = [r["character_id"] for r in titles_result.records]
    assert len(ids) == len(set(ids))


def test_bad_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_bdoservanttitless_records(b"XXXX" + bytes(16))
