from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

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

from .parser import FILE_NAME, QUEST_TYPE, parse_intimacyinfo_records


# CppEnums.IntimacyInformationTypeInfo has six values, DlgCommonConditionOperatorType three.
_TYPE_COUNT = 6
_OPERATOR_COUNT = 3
_KNOWLEDGE_TYPE = 3
# Islin Bartali, the Velia innkeeper.
_ISLIN_BARTALI = 40001

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["character_key", "infos", "name", "entry_count", "entries_text"]),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(col="character_key", value=_ISLIN_BARTALI, expected={"name": "Islin Bartali"}),
    ],
)


@pytest.fixture(scope="module")
def intimacy_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_intimacyinfo_bss(spec: Any, intimacy_result: HandlerResult) -> None:
    intimacy_result.check(spec)


def test_every_entry_belongs_to_its_npc() -> None:
    for record in parse_intimacyinfo_records(load_binary_fixture(FILE_NAME)):
        assert record["infos"], record["character_key"]
        for info in record["infos"]:
            assert info["character_key"] == record["character_key"]
            assert 0 <= info["type_index"] < _TYPE_COUNT
            assert 0 <= info["operator_type"] < _OPERATOR_COUNT


def test_only_quests_carry_a_quest_and_only_knowledge_a_knowledge_key() -> None:
    for record in parse_intimacyinfo_records(load_binary_fixture(FILE_NAME)):
        for info in record["infos"]:
            is_quest = info["type_index"] == QUEST_TYPE
            assert ("quest_group" in info) == is_quest
            assert ("dialog_index" in info) != is_quest
            if not is_quest:
                assert info["quest_id"] == 0
            assert (info["knowledge_key"] != 0) == (info["type_index"] == _KNOWLEDGE_TYPE)


def test_entries_name_their_target(intimacy_result: HandlerResult) -> None:
    lines = [line for record in intimacy_result.records for line in record["_entries"]]
    assert any(line.startswith("Quest: ") for line in lines)
    assert any(line.startswith("Knowledge: ") for line in lines)


def test_parse_reads_a_quest_and_a_talk_entry() -> None:
    quest = struct.pack("<HiIIIHHI", 507, 100, QUEST_TYPE, 1, 0, 2023, 4, 0)
    talk = struct.pack("<HiIIIHHI", 507, 50, 4, 2, 0, 7, 0, 3)
    rows = struct.pack("<HI", 507, 2) + quest + talk
    table_start = 8 + len(rows)
    data = b"PABR" + struct.pack("<I", 1) + rows + struct.pack("<I", 0) + struct.pack("<II", table_start, 0)

    (record,) = parse_intimacyinfo_records(data)

    first, second = record["infos"]
    assert (first["quest_group"], first["quest_id"]) == (2023, 4)
    assert (second["dialog_index"], second["unknown_quest_id_02"]) == (7, 3)


def test_parse_rejects_rows_that_miss_the_string_table() -> None:
    rows = struct.pack("<HI", 507, 0)
    data = b"PABR" + struct.pack("<I", 1) + rows + struct.pack("<I", 0) + struct.pack("<II", 8 + len(rows) + 2, 0)
    with pytest.raises(ValueError):
        parse_intimacyinfo_records(data)
