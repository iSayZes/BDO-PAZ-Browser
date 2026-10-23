from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    run_case,
)

from _bss.sequence_scripts.reader import cutscene_file_hash
from _bss.tutorial_equipment.parser import CUTSCENE_FILE_NAME as CUTSCENE_EQUIPMENT
from _bss.tutorial_equipment.parser import SEQUENCE_FILE_NAME as SEQUENCE_EQUIPMENT
from .parser import CUTSCENE_FILE_NAME, SEQUENCE_FILE_NAME


_PABR_COUNT_OFFSET = 4
_ROW_HEAD = struct.Struct("<II")
_CLASS_HEAD = struct.Struct("<BQ")
_SKILL_NO_SIZE = 2
_WARRIOR = 0
# Rows keyed by these hashes; both names are in the equipment table of the same kind.
_ILLEZRA_SEQUENCE = 0xDEFE7AE1
_ILLEZRA_CUTSCENE = 0xB5DDE516
_SCHEMA = SchemaTest(required_keys=[
    "file_name_hash", "cutscene_file_name", "class_type", "class_name", "skill_count", "skill_nos", "skill_names",
])


def _class_entries(source: CaseInput) -> int:
    """The class counts of every row added up, walked from the row heads and skill counts."""
    data = source.data
    pos, total = struct.calcsize("<4sI"), 0
    for _ in range(struct.unpack_from("<I", data, _PABR_COUNT_OFFSET)[0]):
        _, class_count = _ROW_HEAD.unpack_from(data, pos)
        pos += _ROW_HEAD.size
        total += class_count
        for _ in range(class_count):
            _, skill_count = _CLASS_HEAD.unpack_from(data, pos)
            pos += _CLASS_HEAD.size + skill_count * _SKILL_NO_SIZE
    return total


def _case(file_name: str, equipment: str, file_hash: int, cutscene_file_name: str) -> HandlerCase:
    return HandlerCase(
        handler_name=file_name,
        data_file=file_name,
        companion_files={equipment: equipment},
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=["class_name", "skill_names"],
        internal_path=f"gamecommondata/binary/{file_name}",
        tests=[
            _SCHEMA,
            DeclaredCountTest(declared=_class_entries),
            TargetTest(
                col="file_name_hash",
                value=file_hash,
                expected={"cutscene_file_name": cutscene_file_name, "class_type": _WARRIOR, "class_name": "Warrior"},
            ),
            UserLanguageTest(fields=["class_name"]),
        ],
    )


SEQUENCE_CASE = _case(SEQUENCE_FILE_NAME, SEQUENCE_EQUIPMENT, _ILLEZRA_SEQUENCE, "CS_Tutorial_Illezra_00.pas")
CUTSCENE_CASE = _case(CUTSCENE_FILE_NAME, CUTSCENE_EQUIPMENT, _ILLEZRA_CUTSCENE, "CS_Tutorial_00_Illezra_0008.pas")
CASES = [SEQUENCE_CASE, CUTSCENE_CASE]
_RESULTS: dict[str, HandlerResult] = {}
_SPECS = [(case, spec) for case in CASES for spec in case.tests]


def _result(case: HandlerCase) -> HandlerResult:
    result = _RESULTS.get(case.handler_name)
    if result is None:
        result = run_case(replace(case, tests=[]))
        _RESULTS[case.handler_name] = result
    return result


@pytest.mark.parametrize(("case", "spec"), _SPECS, ids=[f"{case.handler_name}-{case_id(spec)}" for case, spec in _SPECS])
def test_skill_table(case: HandlerCase, spec: Any) -> None:
    _result(case).check(spec)


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_skill_count_is_the_list_length(case: HandlerCase) -> None:
    for r in _result(case).records:
        assert r["skill_count"] == len(r["skill_nos"]), (r["file_name_hash"], r["class_type"])


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_class_types_repeat_once_per_row(case: HandlerCase) -> None:
    keys = [(r["file_name_hash"], r["class_type"]) for r in _result(case).records]
    assert len(keys) == len(set(keys))


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_resolved_names_hash_to_the_row(case: HandlerCase) -> None:
    for r in _result(case).records:
        if r["cutscene_file_name"]:
            assert cutscene_file_hash(r["cutscene_file_name"]) == r["file_name_hash"], r["cutscene_file_name"]
