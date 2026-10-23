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
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from _bss.sequence_scripts.reader import cutscene_file_hash
from .parser import FILE_NAME, FLAG_FIELDS, TEXT_FIELDS


_PABR_COUNT_OFFSET = 4
_SEQUENCE_PATH = "Sadang/CS_SadangSeoul_06_02_Pyeseja"
_GEUNJEONGJEON_HALL = 1496

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["region_names_text"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "file_name_hash", *TEXT_FIELDS, "position", "resurrect_position", "region_count", "region_keys",
            "file_name_hash_dup", "radius", *FLAG_FIELDS, "sequence_path", "options",
        ]),
        DeclaredCountTest(declared=header_count(offset=_PABR_COUNT_OFFSET)),
        TargetTest(
            col="sequence_path",
            value=_SEQUENCE_PATH,
            expected={"folder": "Sadang", "region_keys": [_GEUNJEONGJEON_HALL]},
        ),
        *(RangeTest(col=field, min_val=0, max_val=1) for field in FLAG_FIELDS),
        UserLanguageTest(fields=["region_names_text"]),
    ],
)


@pytest.fixture(scope="module")
def sequence_trigger_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_sequencetriggerdata_bss(spec: Any, sequence_trigger_result: HandlerResult) -> None:
    sequence_trigger_result.check(spec)


def test_both_hashes_are_the_file_name_hash(sequence_trigger_result: HandlerResult) -> None:
    """`file_name_hash` and its copy are the ASCII key hash of `file_name`, as for the cutscene tables."""
    for r in sequence_trigger_result.records:
        assert r["file_name_hash"] == cutscene_file_hash(r["file_name"]), r["sequence_path"]
        assert r["file_name_hash_dup"] == r["file_name_hash"], r["sequence_path"]


def test_every_row_has_a_region_and_a_unique_path(sequence_trigger_result: HandlerResult) -> None:
    paths = [r["sequence_path"] for r in sequence_trigger_result.records]
    assert len(paths) == len(set(paths))
    for r in sequence_trigger_result.records:
        assert r["region_keys"], r["sequence_path"]
