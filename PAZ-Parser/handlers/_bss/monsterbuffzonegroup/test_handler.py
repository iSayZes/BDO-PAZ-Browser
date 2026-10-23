from __future__ import annotations

from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, parse_monsterbuffzonegroup_records


# Olun's Valley and its Olun's Golem (monsterbuffzonegroup_bss.md).
_OLUNS_VALLEY = 1058
_OLUNS_GOLEM = 21249

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["region_name", "structures"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "region_key", "unknown_02", "unknown_06", "entry_count", "entries",
            "region_name", "structures", "listed_characters",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        UserLanguageTest(fields=["region_name", "structures"]),
        TargetTest(col="region_key", value=_OLUNS_VALLEY, expected={
            "region_name": "Olun's Valley",
            "structures": [f"Olun's Golem ({_OLUNS_GOLEM})"],
        }),
    ],
)


@pytest.fixture(scope="module")
def group_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_monsterbuffzonegroup_bss(spec: Any, group_result: HandlerResult) -> None:
    group_result.check(spec)


def test_region_keys_are_unique(group_result: HandlerResult) -> None:
    keys = [record["region_key"] for record in group_result.records]
    assert len(keys) == len(set(keys))


def test_entries_repeat_their_keys(group_result: HandlerResult) -> None:
    # Checks the entry layout: the character key twice, then the row's region key.
    for record in group_result.records:
        assert len(record["entries"]) == record["entry_count"]
        for entry in record["entries"]:
            assert entry["character_key_dup"] == entry["character_key"]
            assert entry["unknown_05"] == record["region_key"]
            assert len(entry["character_keys"]) == entry["character_count"]


def test_short_file_raises() -> None:
    with pytest.raises(ValueError):
        parse_monsterbuffzonegroup_records((1).to_bytes(4, "little"))
