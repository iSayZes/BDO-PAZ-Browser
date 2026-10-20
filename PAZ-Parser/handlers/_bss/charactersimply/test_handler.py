from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _bss.charactersimply.parser import parse_charactersimply_records
from _common.pabr_offset import parse_pabr_offset_rows
from _dbss.characterstatic.parser import parse_characterstatic_records
from tests.fixtures import load_binary_fixture
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

# Fields both files store, by the same name, with the same meaning.
_SHARED_FIELDS = (
    "npc_kind", "grade", "level", "character_group", "class_type", "body_size",
    "vehicle_type", "model_path", "name_kr", "title_kr", "action_script", "condition_script",
)

CASE = HandlerCase(
    handler_name="charactersimply.bss",
    data_file="charactersimply.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Name", "Title"],
    internal_path="gamecommondata/binary/charactersimply.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "character_id", "name", "title", "name_kr", "title_kr", "npc_kind", "npc_kind_name",
                "grade", "level", "character_group", "class_type", "vehicle_type", "vehicle_type_name",
                "body_size", "body_height", "max_hp", "model_path", "model_path_hash", "voice_bank",
                "action_script", "knowledge_id", "condition_script", "attribute_type_mask",
                "is_live_collect", "fusion_group_key", "unknown_0a", "unknown_76",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        RangeTest(col="is_hidden_name", min_val=0, max_val=1),
        RangeTest(col="unknown_5c", min_val=0x15, max_val=0x15),
        RangeTest(col="unknown_43", min_val=1, max_val=1),
        # A node manager: LOC name and title, Korean strings from the string table.
        TargetTest(
            col="character_id",
            value=47791,
            expected={
                "name": "Ehren",
                "name_kr": "에론",
                "title_kr": "<거점 관리인>",
                "npc_kind": 2,
                "npc_kind_name": "Npc",
                "action_script": "getknowledge(15936);",
                "knowledge_id": 15936,
                "model_path": "npc/pedu2/npc_pedu2_named",
            },
        ),
        # Warrior: character 1, a player character (kind 0) of class 0.
        TargetTest(
            col="character_id",
            value=1,
            expected={"name_kr": "워리어", "npc_kind": 0, "class_type": 0},
        ),
        # The one row the sheet gives a FusionGroupKey.
        TargetTest(col="character_id", value=530, expected={"name": "Aal's Breath", "fusion_group_key": 1}),
    ],
)


@pytest.fixture(scope="module")
def charactersimply_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_charactersimply_bss(spec: Any, charactersimply_result: HandlerResult) -> None:
    charactersimply_result.check(spec)


def test_rows_repeat_the_characterstatic_fields() -> None:
    """Both files hold the same characters, and every shared field the same value."""
    simple = {r["character_id"]: r for r in parse_charactersimply_records(load_binary_fixture("charactersimply.bss"))}
    static = {
        r["character_id"]: r
        for r in parse_characterstatic_records(
            load_binary_fixture("characterstatic.dbss"),
            parse_pabr_offset_rows(load_binary_fixture("characterstaticoffset.dbss")),
        )
    }

    assert simple.keys() == static.keys()
    mismatched = sorted(
        (field, character_id)
        for character_id, record in simple.items()
        for field in _SHARED_FIELDS
        if record[field] != static[character_id][field]
    )
    assert not mismatched, f"fields that differ from characterstatic.dbss: {mismatched[:5]}"
