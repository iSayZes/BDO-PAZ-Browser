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
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, parse_instancefieldcommon_records


# PABR magic, then the u32 record count.
_COUNT_OFFSET = 4
# The `InstanceCommonOption` row of the character awakening quest (instancefieldcommon_bss.md).
_AWAKENING_INSTANCE_TYPE = 4

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["quest_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "instance_mode", "instance_type", "limited_character_level", "limited_quest_group",
            "limited_quest_id", "limited_quest_string", "unknown_10", "unknown_14",
            "limited_quest_text_kr", "quest", "quest_name",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="instance_type", value=_AWAKENING_INSTANCE_TYPE, expected={
            "instance_mode": 0,
            "limited_quest_group": 804,
            "limited_quest_id": 1,
            "quest_name": "[Awakening] The Black Spirit's Strange Power",
        }),
    ],
)


@pytest.fixture(scope="module")
def common_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_instancefieldcommon_bss(spec: Any, common_result: HandlerResult) -> None:
    common_result.check(spec)


def test_list_length_follows_its_count(common_result: HandlerResult) -> None:
    for record in common_result.records:
        assert len(record["unknown_14"]) == record["unknown_10"]


def test_every_message_index_names_a_string(common_result: HandlerResult) -> None:
    assert all(record["limited_quest_text_kr"] for record in common_result.records)


def test_message_line_breaks_are_decoded(common_result: HandlerResult) -> None:
    # The stored text writes a line break as backslash and n.
    assert all("\\n" not in record["limited_quest_text_kr"] for record in common_result.records)


def test_bad_magic_raises() -> None:
    with pytest.raises(ValueError):
        parse_instancefieldcommon_records(b"XXXX" + bytes(16))
