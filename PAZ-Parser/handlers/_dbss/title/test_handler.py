from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.pa_text import pa_cell, strip_pa_tags
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

from .handler import _category_label, _title_cell


def _title_record(record: dict) -> dict:
    requirement = strip_pa_tags(record.get("en_req") or record["requirement_text_kr"])

    return {
        "TitleId": record["title_id"],
        "Category": _category_label(record["category_id"]),
        "Title": strip_pa_tags(record.get("en_name") or record["title_text_kr"]),
        "TitleRequirements": " ".join(requirement.split()),
        "Special": bool(record["title_color_argb"] or record["header_field_meaning"] != "style"),
        "Effect": record["title_effect_name"] or "-",
        "TitleHtml": _title_cell(record),
        "RequirementHtml": pa_cell(record, "requirement"),
    }


CASE = HandlerCase(
    handler_name="title.dbss",
    data_file="title.dbss",
    companion_files={"titleoffset.dbss": "titleoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Title", "TitleRequirements"],
    internal_path="gamecommondata/binary/title.dbss",
    record_mapper=_title_record,
    tests=[
        SchemaTest(required_keys=["TitleId", "Category", "Title", "TitleRequirements", "Special", "Effect"]),
        RangeTest(col="TitleId", min_val=1, max_val=9999),
        DeclaredCountTest(declared=header_count(companion="titleoffset.dbss")),
        TargetTest(
            col="TitleId",
            value=1,
            expected={
                "Category": "Combat",
                "Title": "Battle Ready",
                "TitleRequirements": (
                    "Title Requirement: Defeat Parasitic Bees "
                    "Enough fundamentals. Parasitic Bees are nothing."
                ),
                "Special": False,
                "Effect": "-",
            },
        ),
        TargetTest(
            col="TitleId",
            value=3,
            expected={
                "TitleId": 3,
                "Category": "Combat",
                "Title": "Parasitic Bee Curious",
                "TitleRequirements": (
                    "Title Requirement: Defeat Parasitic Bee "
                    "What are they doing instead of eating honey?"
                ),
                "Special": False,
                "Effect": "-",
            },
        ),
        TargetTest(
            col="TitleId",
            value=(4, 5),
            expected=[
                {
                    "TitleId": 4,
                    "Category": "Combat",
                    "Title": "Parasitic Bee Dominator",
                    "TitleRequirements": (
                        "Title Requirement: Defeat Parasitic Bee "
                        "I'm getting bored. I'd better find another playmate."
                    ),
                    "Special": False,
                    "Effect": "-",
                },
                {
                    "TitleId": 5,
                    "Category": "Combat",
                    "Title": "Grass Beetle Crusher",
                    "TitleRequirements": (
                        "Title Requirement: Defeat Grass Beetle "
                        "I felt threatened by its wings! I can withstand it, though."
                    ),
                    "Special": False,
                    "Effect": "-",
                },
            ],
        ),
    ],
)


@pytest.fixture(scope="module")
def title_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_title_dbss(spec: Any, title_result: HandlerResult) -> None:
    title_result.check(spec)


def _title_html(title_result: HandlerResult, title: str) -> str:
    return next(r["TitleHtml"] for r in title_result.records if r["Title"] == title)


def test_gradient_title_draws_its_tag_colours(title_result: HandlerResult) -> None:
    """MASTER WARRIOR colours each pair of letters with a tag of its own."""
    html = _title_html(title_result, "MASTER WARRIOR")

    assert html.count('class="pa-color"') > 1
    assert "PAColor" not in html


def test_stored_title_colour_wraps_the_title(title_result: HandlerResult) -> None:
    html = _title_html(title_result, "Trooper")

    assert html.startswith('<span class="pa-color" style="color: rgba(')
    assert html.endswith("Trooper</span>")


def test_requirement_label_keeps_its_colour(title_result: HandlerResult) -> None:
    """Requirements open with a coloured "Title Requirement" label."""
    html = next(r["RequirementHtml"] for r in title_result.records if r["Title"] == "Battle Ready")

    assert html.startswith('<span class="pa-color" style="color: rgba(')
    assert "PAColor" not in html
