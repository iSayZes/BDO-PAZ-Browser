from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.loc import strip_pa_tags
from tests.framework import CountTest, HandlerCase, HandlerResult, PosTest, RangeTest, SchemaTest, TargetTest, case_id, run_case

from .handler import _category_label


def _title_record(record: dict) -> dict:
    title_color = record["title_color_argb"]
    title_color_hex = f"#{title_color[4:]}" if title_color.startswith("0xFF") else "-"
    requirement = strip_pa_tags(record.get("en_req") or record["requirement_text_ko"])

    return {
        "TitleId": record["title_id"],
        "Category": _category_label(record["category_id"]),
        "Title": strip_pa_tags(record.get("en_name") or record["title_text_ko"]),
        "TitleColor": title_color_hex,
        "TitleRequirements": " ".join(requirement.split()),
        "Special": bool(title_color or record["header_field_meaning"] != "style"),
        "Effect": record["title_effect_name"] or "-",
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
        SchemaTest(required_keys=["TitleId", "Category", "Title", "TitleColor", "TitleRequirements", "Special", "Effect"]),
        RangeTest(col="TitleId", min_val=1, max_val=9999),
        CountTest(expected=3048),
        TargetTest(
            col="TitleId",
            value=3,
            expected={
                "TitleId": 3,
                "Category": "Combat",
                "Title": "Parasitic Bee Curious",
                "TitleColor": "-",
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
                    "TitleColor": "-",
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
                    "TitleColor": "-",
                    "TitleRequirements": (
                        "Title Requirement: Defeat Grass Beetle "
                        "I felt threatened by its wings! I can withstand it, though."
                    ),
                    "Special": False,
                    "Effect": "-",
                },
            ],
        ),
        PosTest(
            pos=0,
            expected={
                "TitleId": 1,
                "Category": "Combat",
                "Title": "Battle Ready",
                "TitleColor": "-",
                "TitleRequirements": (
                    "Title Requirement: Defeat Parasitic Bees "
                    "Enough fundamentals. Parasitic Bees are nothing."
                ),
                "Special": False,
                "Effect": "-",
            },
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
    spec.check(title_result.records)
