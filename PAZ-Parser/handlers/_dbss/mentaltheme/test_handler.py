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


CASE = HandlerCase(
    handler_name="mentaltheme.dbss",
    data_file="mentaltheme.dbss",
    companion_files={"mentalthemeoffset.dbss": "mentalthemeoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Parent Name"],
    internal_path="gamecommondata/binary/mentaltheme.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "theme_id", "name", "parent_id", "parent_name", "entry_count", "child_count", "bookshelf_item",
                "bookshelf", "is_copy_right_able",
            ],
        ),
        DeclaredCountTest(declared=header_count()),
        RangeTest(col="is_copy_right_able", min_val=0, max_val=1),
        TargetTest(
            col="theme_id",
            value=20120,
            expected={
                "name": "Morning Light - Hwanghae Logs I",
                "parent_id": 20119,
                "parent_name": "Morning Light Logs - Hwanghae Province",
            },
        ),
        TargetTest(
            col="theme_id",
            value=10319,
            expected={
                "name": "Refugee Camp",
                "bookshelf_item": 2532,
                "bookshelf": "Bookshelf with Knowledge on Monsters of the Refugee Camp",
            },
        ),
        TargetTest(
            col="theme_id",
            value=20304,
            expected={
                "name": "Calpheon City Adventure Log I",
                "parent_id": 20030,
                "parent_name": "Calpheon Logs",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def mentaltheme_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_mentaltheme_dbss(spec: Any, mentaltheme_result: HandlerResult) -> None:
    mentaltheme_result.check(spec)


def test_bookshelf_items_are_named_items(mentaltheme_result: HandlerResult) -> None:
    """Every bookshelf item resolves to a LOC type 0 item name, not the ID fallback."""
    shelves = [r for r in mentaltheme_result.records if r["bookshelf_item"] is not None]
    assert shelves
    for record in shelves:
        name = record["bookshelf"]
        assert name and name != str(record["bookshelf_item"]), record["theme_id"]
        assert name.lower().startswith("bookshelf"), (record["theme_id"], name)


def test_no_bookshelf_is_blank(mentaltheme_result: HandlerResult) -> None:
    """A theme without a bookshelf item stores None and no name, so its cell shows a dash."""
    blank = [r for r in mentaltheme_result.records if r["bookshelf_item"] is None]
    assert blank
    assert all(r["bookshelf"] == "" for r in blank)
