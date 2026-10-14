from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _common.pabr_offset import parse_pabr_offset_rows
from _dbss.characterstatic.parser import build_knowledge_character_index, parse_characterstatic_records
from _dbss.itemenchant.parser import build_character_item_index
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)


STATIC_CASE = HandlerCase(
    handler_name="characterstatic.dbss",
    data_file="characterstatic.dbss",
    companion_files={"characterstaticoffset.dbss": "characterstaticoffset.dbss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name"],
    internal_path="gamecommondata/binary/characterstatic.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "character_id", "name", "title", "label_kr", "action_script", "condition_script",
                "knowledge_id", "npc_kind", "grade", "tendency_on_dead", "ocean_tendency",
                "vehicle_type", "vehicle_type_name", "class_type", "ai_script", "model_path",
                "source_item_id", "source_item_name", "payload_size",
            ]
        ),
        # The data file's own count; the parser walks the offset table's rows.
        DeclaredCountTest(declared=header_count()),
        TargetTest(
            col="character_id",
            value=16640,
            expected={
                "name": "Dev Plant210",
                "action_script": "",
                "knowledge_id": None,
                "npc_kind": 8,
                # The stem of character/aiscript/9999.ai.
                "ai_script": "9999",
                "model_path": "monster/dummy_normal",
            },
        ),
        # A condition script used to be misread into the action script and
        # shifted every field after it.
        TargetTest(
            col="character_id",
            value=47332,
            expected={
                "action_script": "getknowledge(2095);",
                "condition_script": "getOceanTendency()>-1;",
                "knowledge_id": 2095,
                "npc_kind": 2,
            },
        ),
        # The LOC title in the user's language; the internal label exists only in Korean.
        TargetTest(
            col="character_id",
            value=47791,
            expected={"title": "<Node Manager>", "label_kr": "에다니아2_아우리스 해안_거점관리인_idx53"},
        ),
        # Without a LOC title the Korean one stands in.
        TargetTest(col="character_id", value=47481, expected={"title": "<여관 관리인>"}),
        # The getknowledge match ignores case.
        TargetTest(col="character_id", value=50613, expected={"knowledge_id": 933}),
        # class_type differs from character_id: Warrior is 1 / 0, Ranger 2 / 4.
        TargetTest(
            col="character_id",
            value=1,
            # Player characters store their model path first and name no script.
            expected={"class_type": 0, "ai_script": "", "model_path": "pc/1_phm/fighteraction_noweapon"},
        ),
        TargetTest(col="character_id", value=2, expected={"class_type": 4}),
        # Grade 4 is CppEnums.CharacterGradeType_Boss, the grade the Lua boss gauge checks.
        TargetTest(col="character_id", value=29929, expected={"name": "Garmoth", "grade": 4, "vehicle_type": None}),
        # Vehicle type 0 is Type_Horse, a value and not the "no vehicle" dash.
        TargetTest(col="character_id", value=9001, expected={"vehicle_type": 0, "vehicle_type_name": "Horse"}),
        # The item that places the character, as itemenchant.dbss links it.
        TargetTest(col="character_id", value=2053, expected={"source_item_id": 58011}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name="characterstaticoffset.dbss",
    data_file="characterstaticoffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/characterstaticoffset.dbss",
    tests=[
        SchemaTest(required_keys=["character_id", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        # The first payload follows the data file's u32 count and its inline u16 ID.
        TargetTest(col="offset", value=6, expected={}),
    ],
)


@pytest.fixture(scope="module")
def static_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_STATIC_RESULT", None)
    if result is None:
        result = run_case(replace(STATIC_CASE, tests=[]))
        request.module._STATIC_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", STATIC_CASE.tests, ids=case_id)
def test_characterstatic_dbss(spec: Any, static_result: HandlerResult) -> None:
    static_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_characterstaticoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_knowledge_index_holds_every_granting_character(static_result: HandlerResult) -> None:
    """The index is the preview's knowledge links, grouped by knowledge ID."""
    source = static_result.source
    index = build_knowledge_character_index(source.data, source.file("characterstaticoffset.dbss"))

    expected: dict[int, list[int]] = {}
    for record in static_result.records:
        if record["knowledge_id"] is not None:
            expected.setdefault(record["knowledge_id"], []).append(record["character_id"])

    assert index == {knowledge_id: tuple(sorted(ids)) for knowledge_id, ids in expected.items()}


def test_source_item_matches_the_itemenchant_link(static_result: HandlerResult) -> None:
    """A stored source item is the item whose itemenchant.dbss record names the character."""
    links = build_character_item_index(
        load_binary_fixture("itemenchant.dbss"),
        load_binary_fixture("itemenchantoffset.dbss"),
    )
    stored = {
        record["character_id"]: record["source_item_id"]
        for record in static_result.records
        if record["source_item_id"] is not None
    }

    assert stored
    assert {character_id: links.get(character_id) for character_id in stored} == stored


def test_korean_strings_follow_the_model_path(static_result: HandlerResult) -> None:
    """The UTF-16 strings after the model path: Korean name, internal label, title."""
    source = static_result.source
    records = parse_characterstatic_records(
        source.data, parse_pabr_offset_rows(source.file("characterstaticoffset.dbss"))
    )
    by_id = {record["character_id"]: record for record in records}

    assert by_id[29929]["name_kr"] == "가모스"
    assert by_id[1]["name_kr"] == "워리어"
    assert by_id[47791]["title_kr"] == "<거점 관리인>"
    assert all(record["name_kr"] and record["label_kr"] for record in records)
