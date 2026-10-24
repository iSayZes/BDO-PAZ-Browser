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

from _bss.sequence_scripts.reader import CUTSCENE_FILE_SUFFIX, SCRIPT_FIELDS, cutscene_file_hash
from .parser import FILE_NAME


_PABR_COUNT_OFFSET = 4
# The first Duvencrune tutorial cutscene, the row the 2022 sheet also holds.
_FIRST_TUTORIAL = "CS_Tutorial_01_EternalWinter_0000.pas"
_DUVENCRUNE_MOUNTAIN = 890

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["region_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "region_key", "file_name_hash", "cutscene_file_name", *SCRIPT_FIELDS,
            "unknown_16", "unknown_1a", "region_name",
        ]),
        DeclaredCountTest(declared=header_count(offset=_PABR_COUNT_OFFSET)),
        TargetTest(col="cutscene_file_name", value=_FIRST_TUTORIAL, expected={"region_key": _DUVENCRUNE_MOUNTAIN}),
        RangeTest(col="unknown_1a", min_val=0, max_val=1),
        UserLanguageTest(fields=["region_name"]),
    ],
)


@pytest.fixture(scope="module")
def sequence_data_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_sequencedatatable_bss(spec: Any, sequence_data_result: HandlerResult) -> None:
    sequence_data_result.check(spec)


def test_file_name_hash_is_the_name_hash(sequence_data_result: HandlerResult) -> None:
    """`file_name_hash` is the ASCII key hash of `cutscene_file_name` without `.pas`."""
    for r in sequence_data_result.records:
        assert r["cutscene_file_name"].endswith(CUTSCENE_FILE_SUFFIX), r["cutscene_file_name"]
        assert r["file_name_hash"] == cutscene_file_hash(r["cutscene_file_name"]), r["cutscene_file_name"]


def test_file_names_and_unknown_16_are_unique(sequence_data_result: HandlerResult) -> None:
    for field in ("cutscene_file_name", "unknown_16"):
        values = [r[field] for r in sequence_data_result.records]
        assert len(values) == len(set(values)), field
