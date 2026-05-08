from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, SchemaTest, TargetTest, case_id, run_case


OFFSET_CASE = HandlerCase(
    handler_name="journalquestoffset.dbss",
    data_file="journalquestoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/journalquestoffset.dbss",
    tests=[
        SchemaTest(required_keys=["group_id", "entry_no", "byte_offset", "byte_size"]),
        CountTest(expected=112),
        PosTest(pos=0, expected={"group_id": 1, "entry_no": 1, "byte_offset": 8, "byte_size": 498}),
        TargetTest(
            col="group_id",
            value=10,
            expected={"entry_no": 1, "byte_offset": 44190, "byte_size": 320},
        ),
    ],
)


CASE = HandlerCase(
    handler_name="journalquest.dbss",
    data_file="journalquest.dbss",
    companion_files={"journalquestoffset.dbss": "journalquestoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["page_titles_text"],
    internal_path="gamecommondata/binary/journalquest.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "group_id",
                "entry_no",
                "journal_cat_id",
                "journal_title",
                "page_vol_title",
                "page_count",
                "combine_model",
                "static_model",
                "page_titles_text",
            ]
        ),
        CountTest(expected=112),
        PosTest(
            pos=0,
            expected={
                "group_id": 1,
                "entry_no": 1,
                "journal_cat_id": 748,
                "journal_title_text": "Igor Bartali's Adventures",
                "subtitle_text": "Logs of Velia's Chief Igor Bartali's youthful past",
                "page_vol_title_text": "Igor Bartali's Adventures - Volume 1",
                "page_count": 3,
                "page_titles_text": (
                    "Hey There Big Fellow!, Irresistible Lure, "
                    "The Divine Entity inside the Cave"
                ),
                "combine_model": "Combine_Etc_Adventure_Bookshelf01\"",
                "static_model": "Adventure_Bookshelf_Static_book_00",
            },
        ),
        TargetTest(
            col="journal_cat_id",
            value=30006,
            expected={
                "group_id": 2,
                "entry_no": 1,
                "page_count": 4,
                "journal_title_text": "Shakatu Merchants' Archive",
                "page_vol_title_text": "Deve's Encyclopedia - Volume 1\nThe Altinovan on all things random!",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def journalquestoffset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def journalquest_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_journalquestoffset_dbss(spec: Any, journalquestoffset_result: HandlerResult) -> None:
    spec.check(journalquestoffset_result.records)


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_journalquest_dbss(spec: Any, journalquest_result: HandlerResult) -> None:
    spec.check(journalquest_result.records)
