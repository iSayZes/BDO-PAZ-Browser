from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.class_type import ALL_CLASSES_MASK, class_types_in_mask
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

_OFFSET_FILE = "skillsimplyoffset.dbss"
# Warrior's Grave Digging I to IV: one rank chain that also needs the Awakening skill.
_GRAVE_DIGGING_I = 1759 << 16 | 1
_GRAVE_DIGGING_III = 1761 << 16 | 1
_AWAKENING_GOYENS_GREATSWORD = 1712
_WARRIOR = 0
# Checked in game: Teleport III has the Quick Slot line in its tooltip, Ultimate: Teleport does not.
_TELEPORT_III = 911 << 16 | 1
_ULTIMATE_TELEPORT = 2208 << 16 | 1
# Checked in game: a staff skill, a dagger (sub-weapon) skill and a sphera (Awakening) skill.
_FIREBALL_IV = 821 << 16 | 1
_ABSOLUTE_DAGGER_STAB = 3144 << 16 | 1
_WATER_SPHERE_III = 2238 << 16 | 1
# Looks like a sentinel, but is the ordinary skill 57005.
_DEAD_KEY = 0xDEAD0001
# 2016 gc::SkillTypeStaticStatus::SkillOwnerType: 0 actor, 1 guild.
_ACTOR_OWNER = 0
_GUILD_OWNER = 1
_AMPLE_STORAGE_LV_26 = 65229 << 16 | 1
# buff.dbss effect_type of the Elvia weapon blessings, the buff an "Elvia:" skill needs.
_ELVIA_BLESSING_EFFECT_TYPE = 179

CASE = HandlerCase(
    handler_name="skillsimply.dbss",
    data_file="skillsimply.dbss",
    companion_files={_OFFSET_FILE: _OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Classes", "Required Skills", "Previous Rank", "Exclusive Skills"],
    internal_path="gamecommondata/binary/skillsimply.dbss",
    tests=[
        SchemaTest(required_keys=[
            "skill_key", "skill_no", "level", "max_level", "icon_path", "name", "class_mask", "classes",
            "kind", "kind_label", "branch", "require_equip_type", "require_equip_slot", "weapon",
            "skill_owner_type", "is_fusion", "can_quick_slot", "condition", "is_except_cool_time",
            "need_buff_module_type", "contents_group_keys",
            "need_level", "need_skill_point", "need_skill_nos", "need_skills", "previous_rank_no",
            "previous_rank", "next_rank_keys", "first_rank_key", "exclusive_skill_nos", "related_cool_time_skill_keys",
        ]),
        DeclaredCountTest(declared=header_count(offset=4)),
        DeclaredCountTest(declared=header_count(offset=0, companion=_OFFSET_FILE)),
        RangeTest(col="kind", min_val=0, max_val=2),
        RangeTest(col="level", min_val=1, max_val=0xFFFF),
        TargetTest(
            col="skill_key",
            value=_GRAVE_DIGGING_III,
            expected={
                "skill_no": 1761,
                "name": "Grave Digging III",
                "classes": "Warrior",
                "previous_rank_no": 1760,
                "first_rank_key": _GRAVE_DIGGING_I,
            },
        ),
        TargetTest(col="skill_key", value=_DEAD_KEY, expected={"skill_no": 57005, "level": 1}),
        TargetTest(col="skill_key", value=_TELEPORT_III, expected={"can_quick_slot": True}),
        TargetTest(col="skill_key", value=_ULTIMATE_TELEPORT, expected={"can_quick_slot": False}),
        TargetTest(col="skill_key", value=_FIREBALL_IV, expected={"weapon": "Main"}),
        TargetTest(col="skill_key", value=_ABSOLUTE_DAGGER_STAB, expected={"weapon": "Sub"}),
        TargetTest(col="skill_key", value=_WATER_SPHERE_III, expected={"weapon": "Awakening"}),
        TargetTest(col="skill_key", value=_AMPLE_STORAGE_LV_26, expected={"skill_owner_type": _GUILD_OWNER}),
        TargetTest(col="skill_key", value=_FIREBALL_IV, expected={"skill_owner_type": _ACTOR_OWNER}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=_OFFSET_FILE,
    data_file=_OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{_OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["skill_key", "skill_no", "level", "dbss_offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="skill_key", value=_GRAVE_DIGGING_III, expected={"skill_no": 1761, "level": 1}),
    ],
)


@pytest.fixture(scope="module")
def skillsimply_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


def _by_key(result: HandlerResult) -> dict[int, dict]:
    return {r["skill_key"]: r for r in result.records}


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_skillsimply_dbss(spec: Any, skillsimply_result: HandlerResult) -> None:
    skillsimply_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_skillsimplyoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_grave_digging_needs_its_previous_rank_and_the_awakening(skillsimply_result: HandlerResult) -> None:
    record = _by_key(skillsimply_result)[_GRAVE_DIGGING_III]
    assert set(record["need_skill_nos"]) == {1760, _AWAKENING_GOYENS_GREATSWORD}
    assert class_types_in_mask(record["class_mask"]) == (_WARRIOR,)


def test_next_ranks_are_the_skills_naming_this_one_as_previous(skillsimply_result: HandlerResult) -> None:
    by_key = _by_key(skillsimply_result)
    for record in skillsimply_result.records:
        for next_key in record["next_rank_keys"]:
            assert by_key[next_key]["previous_rank_no"] == record["skill_no"], record["skill_key"]


def test_first_rank_is_a_level_1_skill_of_its_own_chain(skillsimply_result: HandlerResult) -> None:
    by_key = _by_key(skillsimply_result)
    for record in skillsimply_result.records:
        first = by_key[record["first_rank_key"]]
        assert first["level"] == 1
        assert first["first_rank_key"] == first["skill_key"], record["skill_key"]


def test_every_linked_skill_is_in_the_table(skillsimply_result: HandlerResult) -> None:
    keys = {r["skill_key"] for r in skillsimply_result.records}
    skill_nos = {r["skill_no"] for r in skillsimply_result.records}
    for record in skillsimply_result.records:
        assert set(record["next_rank_keys"] + record["related_cool_time_skill_keys"]) <= keys, record["skill_key"]
        linked_nos = record["need_skill_nos"] + record["exclusive_skill_nos"]
        if record["previous_rank_no"]:
            linked_nos = linked_nos + [record["previous_rank_no"]]
        assert set(linked_nos) <= skill_nos, record["skill_key"]


def test_all_class_skills_show_one_label(skillsimply_result: HandlerResult) -> None:
    all_class = [r for r in skillsimply_result.records if r["class_mask"] == ALL_CLASSES_MASK]
    assert all_class
    assert {r["classes"] for r in all_class} == {"All"}


def test_max_level_is_the_highest_level_of_its_skill_number(skillsimply_result: HandlerResult) -> None:
    top_levels: dict[int, int] = {}
    for record in skillsimply_result.records:
        top_levels[record["skill_no"]] = max(top_levels.get(record["skill_no"], 0), record["level"])
    for record in skillsimply_result.records:
        assert record["max_level"] == top_levels[record["skill_no"]], record["skill_key"]


def test_every_contents_group_hash_decodes_to_a_key(skillsimply_result: HandlerResult) -> None:
    for record in skillsimply_result.records:
        assert record["contents_group_keys"], record["skill_key"]
        assert None not in record["contents_group_keys"], record["skill_key"]


def test_only_elvia_skills_need_the_elvia_blessing(skillsimply_result: HandlerResult) -> None:
    elvia = [r for r in skillsimply_result.records if r["name"].startswith("Elvia:")]
    assert elvia
    for record in skillsimply_result.records:
        needs_blessing = record["need_buff_module_type"] == _ELVIA_BLESSING_EFFECT_TYPE
        assert needs_blessing == record["name"].startswith("Elvia:"), record["skill_key"]


def test_cooldown_exempt_skills_are_black_spirit_skills(skillsimply_result: HandlerResult) -> None:
    exempt = [r for r in skillsimply_result.records if r["is_except_cool_time"]]
    assert exempt
    for record in exempt:
        assert record["name"].startswith("Black Spirit:"), record["skill_key"]


def test_records_open_in_skill_key_order(skillsimply_result: HandlerResult) -> None:
    keys = [r["skill_key"] for r in skillsimply_result.records]
    assert keys == sorted(keys)


@pytest.mark.parametrize(
    ("class_mask", "class_types"),
    [(0, ()), (0x1, (0,)), (0x100, (8,)), (0x90000000, (28, 31))],
)
def test_class_types_in_mask(class_mask: int, class_types: tuple[int, ...]) -> None:
    assert class_types_in_mask(class_mask) == class_types
