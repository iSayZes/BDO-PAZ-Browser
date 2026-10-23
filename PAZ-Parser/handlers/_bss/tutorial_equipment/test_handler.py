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
from .parser import CUTSCENE_FILE_NAME, SEQUENCE_FILE_NAME, SLOT_FIELDS


_PABR_COUNT_OFFSET = 4
_ROW_HEAD = struct.Struct("<III")
_CLASS_SIZE = 25
_WARRIOR = 0
_ITEM_NAME_FIELDS = [field.replace("_item_id", "_item_name") for field in SLOT_FIELDS]


def _class_entries(source: CaseInput) -> int:
    """The class counts of every row added up; each class entry is 25 bytes."""
    data = source.data
    pos, total = struct.calcsize("<4sI"), 0
    for _ in range(struct.unpack_from("<I", data, _PABR_COUNT_OFFSET)[0]):
        class_count = _ROW_HEAD.unpack_from(data, pos)[2]
        pos += _ROW_HEAD.size + class_count * _CLASS_SIZE
        total += class_count
    return total


def _case(file_name: str, cutscene_file_name: str) -> HandlerCase:
    return HandlerCase(
        handler_name=file_name,
        data_file=file_name,
        companion_files={},
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=["class_name", *_ITEM_NAME_FIELDS],
        internal_path=f"gamecommondata/binary/{file_name}",
        tests=[
            SchemaTest(required_keys=[
                "file_name_hash", "cutscene_file_name", "class_type", "class_name", *SLOT_FIELDS, *_ITEM_NAME_FIELDS,
            ]),
            DeclaredCountTest(declared=_class_entries),
            TargetTest(
                col="cutscene_file_name",
                value=cutscene_file_name,
                expected={"file_name_hash": cutscene_file_hash(cutscene_file_name), "class_type": _WARRIOR},
            ),
            UserLanguageTest(fields=["class_name"]),
        ],
    )


SEQUENCE_CASE = _case(SEQUENCE_FILE_NAME, "CS_Tutorial_Illezra_00.pas")
CUTSCENE_CASE = _case(CUTSCENE_FILE_NAME, "CS_Tutorial_00_Illezra_0000.pas")
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
def test_tutorial_equipment(case: HandlerCase, spec: Any) -> None:
    _result(case).check(spec)


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_file_name_hash_is_the_name_hash(case: HandlerCase) -> None:
    for r in _result(case).records:
        assert r["file_name_hash"] == cutscene_file_hash(r["cutscene_file_name"]), r["cutscene_file_name"]


@pytest.mark.parametrize("case", CASES, ids=lambda case: case.handler_name)
def test_class_types_repeat_once_per_row(case: HandlerCase) -> None:
    keys = [(r["file_name_hash"], r["class_type"]) for r in _result(case).records]
    assert len(keys) == len(set(keys))

