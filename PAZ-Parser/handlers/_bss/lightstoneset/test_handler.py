from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    PaFieldTest,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _bss.lightstoneset.parser import build_lightstone_set_index, parse_lightstone_sets, substitute_ids
from _bss.lightstoneset.text import split_set_text
from _common.lookup_index import IndexKind


_DATA_FILE = "lightstoneset.bss"
# The set count follows the PABR magic.
_COUNT_OFFSET = 4
# Two Artifacts with two Lightstone slots each.
_MAX_MEMBERS = 4
# Set 182 [The Wild: Edania]: three Lightstones of Fire: Twisted and an Iridescent Lightstone.
_EDANIA_SET = 182
_EDANIA_SKILL = 47521
_TWISTED = 758021
_AMPLIFIED_TWISTED = 758221
_IRIDESCENT = 766101
_EDANIA_BUFF = 48555
_SET_SKILL_LEVEL = 1

CASE = HandlerCase(
    handler_name=_DATA_FILE,
    data_file=_DATA_FILE,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "effects", "members"],
    internal_path=f"gamecommondata/binary/{_DATA_FILE}",
    lookup_indexes={IndexKind.SKILL_BUFFS: {_EDANIA_SKILL << 16 | _SET_SKILL_LEVEL: (_EDANIA_BUFF,)}},
    tests=[
        SchemaTest(
            required_keys=[
                "set_id",
                "skill_no",
                "member_ids",
                "text_kr",
                "member_count",
                "name",
                "members",
                "substitute_ids",
                "substitutes",
                "effects",
                "buff_ids",
                "buffs",
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        PaFieldTest(field="name"),
        UserLanguageTest(fields=["name", "effects"]),
        RangeTest(col="member_count", min_val=1, max_val=_MAX_MEMBERS),
        TargetTest(
            col="set_id",
            value=_EDANIA_SET,
            expected={
                "skill_no": _EDANIA_SKILL,
                "member_ids": [_TWISTED, _TWISTED, _TWISTED, _IRIDESCENT],
                "name": "[The Wild: Edania]",
                "members": [
                    "Lightstone of Fire: Twisted",
                    "Lightstone of Fire: Twisted",
                    "Lightstone of Fire: Twisted",
                    "Iridescent Lightstone",
                ],
                "substitute_ids": [_AMPLIFIED_TWISTED],
                "buff_ids": [_EDANIA_BUFF],
            },
        ),
        # Set 1 [Prayer for Victory]: Fire: Predation and the two Wind: Alert stones.
        TargetTest(
            col="set_id",
            value=1,
            expected={"skill_no": 55077, "member_ids": [758003, 762004, 762005], "name": "[Prayer for Victory]"},
        ),
    ],
)


@pytest.fixture(scope="module")
def lightstoneset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_lightstoneset_bss(spec: Any, lightstoneset_result: HandlerResult) -> None:
    lightstoneset_result.check(spec)


def test_keys_are_unique(lightstoneset_result: HandlerResult) -> None:
    records = lightstoneset_result.records
    assert len({r["set_id"] for r in records}) == len(records)
    assert len({r["skill_no"] for r in records}) == len(records)


def test_every_member_counts_as_itself(lightstoneset_result: HandlerResult) -> None:
    """The substitute table maps each set member to itself, and every other item to a member."""
    parsed = parse_lightstone_sets(lightstoneset_result.source.data)
    members = {item_id for record in parsed.sets for item_id in record["member_ids"]}

    assert {item_id for item_id in members if parsed.substitutes.get(item_id) != item_id} == set()
    assert set(parsed.substitutes.values()) <= members


def test_set_index_links_members_and_substitutes(lightstoneset_result: HandlerResult) -> None:
    data = lightstoneset_result.source.data
    parsed = parse_lightstone_sets(data)
    index = build_lightstone_set_index(data)

    assert _EDANIA_SET in index[_TWISTED]
    assert _EDANIA_SET in index[_IRIDESCENT]
    # An Amplified Lightstone counts toward the sets of its base Lightstone.
    assert index[_AMPLIFIED_TWISTED] == index[_TWISTED]
    for record in parsed.sets:
        for item_id in record["member_ids"]:
            assert record["set_id"] in index[item_id]
    assert all(list(set_ids) == sorted(set(set_ids)) for set_ids in index.values())


def test_substitute_ids_skip_the_member_itself() -> None:
    table = {10: 10, 210: 10, 20: 20, 220: 20, 30: 30, 230: 30}

    assert substitute_ids([10, 10, 20], table) == [210, 220]
    assert substitute_ids([40], table) == []


def test_split_set_text() -> None:
    text = split_set_text("<PAColor0xffd2ffad>[Well-prepared]<PAOldColor>\nCombat EXP +50%\n\nSkill EXP +10%\n")

    assert text.name == "<PAColor0xffd2ffad>[Well-prepared]<PAOldColor>"
    assert text.effects == ["Combat EXP +50%", "Skill EXP +10%"]
    assert split_set_text("[Name]").effects == []
