from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from _bss.stringtable.parser import GAME_SHEET, parse_key_hashes
from _common.class_type import PLAYABLE_CLASSES_MASK
from _dbss.pcgrowth import combat_types
from _dbss.pcgrowth.combat_types import COMBAT_TYPE_LABELS, combat_type_label, combat_type_text
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)
from tests.runner import load_case


_DATA_FILE = "pcgrowth.dbss"
_OFFSET_FILE = "pcgrowthoffset.dbss"
_SIMPLY_FILE = "pcgrowthsimply.bss"
# Class types are a u8 key; character keys a u16.
_MAX_CLASS_TYPE = 0xFF

CASE = HandlerCase(
    handler_name=_DATA_FILE,
    data_file=_DATA_FILE,
    companion_files={_OFFSET_FILE: _OFFSET_FILE, _SIMPLY_FILE: _SIMPLY_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class_name", "combat_type_name", "description"],
    internal_path=f"gamecommondata/binary/{_DATA_FILE}",
    tests=[
        SchemaTest(
            required_keys=[
                "class_type",
                "character_key",
                "starter_weapons",
                "name_kr",
                "description_kr",
                "select_movie",
                "gender",
                "is_playable",
                "consume_actions",
                "combat_type",
                "class_weapons",
                "weapon_models",
                "class_name",
                "combat_type_name",
                "description",
            ]
        ),
        # The main file and its offset table both open with the row count.
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=header_count(offset=0, companion=_OFFSET_FILE)),
        RangeTest(col="class_type", min_val=0, max_val=_MAX_CLASS_TYPE),
        RangeTest(col="gender", min_val=0, max_val=1),
        RangeTest(col="combat_type", min_val=min(COMBAT_TYPE_LABELS), max_val=max(COMBAT_TYPE_LABELS)),
        # Class type and character key differ: Ranger is class 4, character 2.
        TargetTest(
            col="class_type",
            value=0,
            expected={"character_key": 1, "gender": 0, "name_kr": "워리어", "combat_type_name": "Melee"},
        ),
        TargetTest(col="class_type", value=4, expected={"character_key": 2, "gender": 1, "combat_type_name": "Ranged"}),
        TargetTest(col="class_type", value=25, expected={"character_key": 26, "class_name": "Kunoichi"}),
        # The character info tooltip lists Hashashin under Magic, not melee.
        TargetTest(col="class_type", value=1, expected={"combat_type_name": "Magic"}),
        UserLanguageTest(fields=["class_name", "combat_type_name", "description"]),
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
        SchemaTest(required_keys=["class_type", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        RangeTest(col="class_type", min_val=0, max_val=_MAX_CLASS_TYPE),
    ],
)


@pytest.fixture(scope="module")
def pcgrowth_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PCGROWTH_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._PCGROWTH_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_pcgrowth_dbss(spec: Any, pcgrowth_result: HandlerResult) -> None:
    pcgrowth_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_pcgrowthoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_playable_follows_the_playable_class_mask(pcgrowth_result: HandlerResult) -> None:
    wrong = [
        r["class_type"]
        for r in pcgrowth_result.records
        if r["is_playable"] != bool(PLAYABLE_CLASSES_MASK >> r["class_type"] & 1)
    ]
    assert not wrong, f"class types whose Playable flag disagrees with PLAYABLE_CLASSES_MASK: {wrong}"


def test_playable_is_none_without_pcgrowthsimply() -> None:
    result = run_case(replace(CASE, companion_files={_OFFSET_FILE: _OFFSET_FILE}, tests=[]))
    assert result.records
    assert all(r["is_playable"] is None for r in result.records)


def test_combat_type_hashes_match_stringtable() -> None:
    hashes = parse_key_hashes(load_binary_fixture("stringtable.bss"), GAME_SHEET)
    wrong = {
        label.key: (label.key_hash, hashes.get(label.key))
        for label in COMBAT_TYPE_LABELS.values()
        if hashes.get(label.key) != label.key_hash
    }
    assert not wrong, f"combat type hashes differ from stringtable.bss (stored, file): {wrong}"


def test_combat_types_have_english_text() -> None:
    load_case(CASE)
    missing = [label.enum_name for value, label in COMBAT_TYPE_LABELS.items() if not combat_type_label(value)]
    assert not missing, f"combat types without LOC text: {missing}"


def test_combat_type_without_label_shows_enum_name(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(combat_types, "combat_type_label", lambda combat_type: "")
    assert combat_type_text(1) == "Range"


def test_combat_type_outside_the_enum_is_the_value() -> None:
    assert combat_type_text(max(COMBAT_TYPE_LABELS) + 1) == str(max(COMBAT_TYPE_LABELS) + 1)
