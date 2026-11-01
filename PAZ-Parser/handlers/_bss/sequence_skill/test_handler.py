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
from _bss.sequencetriggerdata.parser import FILE_NAME as SEQUENCE_TRIGGER_DATA
from _bss.tutorial_equipment.parser import CUTSCENE_FILE_NAME as CUTSCENE_EQUIPMENT
from .handler import file_name_hash_text
from .parser import CUTSCENE_FILE_NAME, SEQUENCE_FILE_NAME


_PABR_COUNT_OFFSET = 4
_ROW_HEAD = struct.Struct("<II")
_CLASS_HEAD = struct.Struct("<BQ")
_SKILL_NO_SIZE = 2
_WARRIOR = 0
# Rows keyed by these hashes: a sequencetriggerdata.bss sequence and a
# cutscenetutorial_equipment.bss cutscene.
_ILLEZRA_SEQUENCE = 0xDEFE7AE1
_ILLEZRA_CUTSCENE = 0xB5DDE516
_SCHEMA = SchemaTest(required_keys=[
    "file_name_hash", "file_name", "class_type", "class_name", "skill_count", "skill_nos", "skill_names",
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


def _case(file_name: str, name_source: str, file_hash: int, row_name: str) -> HandlerCase:
    return HandlerCase(
        handler_name=file_name,
        data_file=file_name,
        companion_files={name_source: name_source},
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
                expected={"file_name": row_name, "class_type": _WARRIOR, "class_name": "Warrior"},
            ),
            UserLanguageTest(fields=["class_name"]),
        ],
    )


SEQUENCE_CASE = _case(SEQUENCE_FILE_NAME, SEQUENCE_TRIGGER_DATA, _ILLEZRA_SEQUENCE, "IllezraTutorial/CS_Tutorial_Illezra_00")
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
    """A sequence path hashes by its file part, as sequencetriggerdata.bss stores it."""
    for r in _result(case).records:
        if r["file_name"]:
            stem = r["file_name"].rsplit("/", 1)[-1]
            assert cutscene_file_hash(stem) == r["file_name_hash"], r["file_name"]


def test_every_sequence_row_is_a_trigger_sequence() -> None:
    """Every sequence_skill.bss row keys a sequencetriggerdata.bss sequence, so no row shows without a name."""
    for r in _result(SEQUENCE_CASE).records:
        assert r["file_name"], file_name_hash_text(r["file_name_hash"])
