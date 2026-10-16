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

from .display import effect_sort_values, format_effect, format_effect_type


_ICON_FOLDER = "/New_UI_Common_forLua/Skill/WorkerSkill/"


CASE = HandlerCase(
    handler_name="plantworkerpassiveskill.bss",
    data_file="plantworkerpassiveskill.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Description"],
    internal_path="gamecommondata/binary/plantworkerpassiveskill.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "slot",
                "skill_id",
                "duplicate_skill_id",
                "inline_name",
                "display_name",
                "icon_path",
                "inline_description",
                "display_description",
                "acquisition_weight",
                "effect_type",
                "apply_mode",
                "apply_scope",
                "effect_type_copy",
                "effect_target",
                "effect_value_a",
                "effect_value_b",
                "extra_effect_value_a",
                "extra_effect_value_b",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        # Zero words inside each 0x38-byte record; a stride slip lands data on them.
        RangeTest(col="unknown_14", min_val=0, max_val=0),
        RangeTest(col="unknown_34", min_val=0, max_val=0),
        TargetTest(
            col="skill_id",
            value=1603,
            expected={
                "duplicate_skill_id": 1603,
                "display_name": "Wings C",
                "icon_path": f"{_ICON_FOLDER}1303.dds",
                "effect_type": 0,
            },
        ),
        TargetTest(
            col="skill_id",
            value=1923,
            expected={
                "display_name": "Adv. Siege Weapon Production",
                "icon_path": f"{_ICON_FOLDER}1923.dds",
                "effect_type": 6,
                "effect_type_copy": 6,
                # Siege weapon production category.
                "effect_target": 5004,
            },
        ),
        TargetTest(
            col="skill_id",
            value=1203,
            expected={"display_name": "Thrifty C", "effect_type": 1},
        ),
        # The only record with the extra 16-byte block; its zero words frame it.
        TargetTest(
            col="skill_id",
            value=1012,
            expected={
                "display_name": "Adept Worker",
                "icon_path": f"{_ICON_FOLDER}1012_N.dds",
                "effect_type": 0,
                "unknown_38": 0,
                "unknown_44": 0,
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def plantworkerpassiveskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_plantworkerpassiveskill_bss(
    spec: Any,
    plantworkerpassiveskill_result: HandlerResult,
) -> None:
    plantworkerpassiveskill_result.check(spec)


# (effect_type, effect_target, effect_value_a, effect_value_b) -> (Target, Effect A, Effect B)
# as shown; the values match the skills' English descriptions.
@pytest.mark.parametrize(
    ("params", "shown"),
    [
        ((0, 0, 2_000_000, 1), ("Work Speed", "+2", "-")),  # 1006 Masterly
        ((0, 0, 70_000, 0), ("Move Speed", "+7%", "-")),  # 1302
        ((0, 0, 7_000, 2), ("Luck", "+0.7", "-")),  # 1502
        ((0, 9, 5_000_000, 1), ("Cannon/Siege Weapon Work Speed", "+5", "-")),  # 1009 Siege Knowledge
        ((1, 7_000, 1_000_000, 1_000_000), ("-", "0.7%", "100%")),  # 1203 Thrifty C
        ((2, 1, 200_000, 0), ("Work Speed", "+0.2", "-")),  # 1902 Craftsmanship
        ((2, 0, 5_000, 0), ("Move Speed", "+0.5%", "-")),  # 1901 Leg Work
        ((6, 5004, 3, 0), ("Siege Weapons", "+3", "-")),  # 1923
        ((6, 9999, 3, 0), ("9999", "+3", "-")),  # a category not seen yet
    ],
)
def test_effect_cells_show_in_game_units(
    params: tuple[int, int, int, int], shown: tuple[str, str, str]
) -> None:
    assert tuple(format_effect(*params)) == shown


# Each column sorts by the raw number its cell shows; a dash cell sorts by None.
@pytest.mark.parametrize(
    ("params", "sorted_by"),
    [
        ((0, 9, 5_000_000, 1), (9, 5_000_000, None)),  # 1009 Siege Knowledge
        ((1, 7_000, 1_000_000, 1_000_000), (None, 7_000, 1_000_000)),  # 1203 Thrifty C
        ((2, 1, 200_000, 0), (1, 200_000, None)),  # 1902 Craftsmanship
        ((6, 5004, 3, 0), (5004, 3, None)),  # 1923
        ((9, 4, 5, 6), (4, 5, 6)),  # a type not seen yet shows every raw value
    ],
)
def test_effect_sort_values_match_cells(
    params: tuple[int, int, int, int], sorted_by: tuple[int | None, int, int | None]
) -> None:
    assert tuple(effect_sort_values(*params)) == sorted_by


@pytest.mark.parametrize(
    ("effect_type", "label"),
    [(0, "Flat Stats"), (1, "Full Refund"), (2, "Stats per Level Up"), (6, "Extra Work"), (9, "9")],
)
def test_effect_type_names(effect_type: int, label: str) -> None:
    assert format_effect_type(effect_type) == label
