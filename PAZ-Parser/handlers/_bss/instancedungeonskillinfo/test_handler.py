from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import HandlerCase, HandlerResult, RangeTest, SchemaTest, case_id, run_case

from _common.skill import skill_key
from .parser import CLASS_ROW_COUNT, FILE_NAME, LIST_COUNT, SkillEntry, SkillList, parse_instancedungeonskillinfo


_ERROR_FIELD = "_error"
_TAMER = 16
_LEVEL = 1

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["class", "skill"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["class_type", "class", "list_index", "skill_key", "skill_no", "skill", "unknown_02", "unknown_08"]),
        RangeTest(col="list_index", min_val=0, max_val=LIST_COUNT - 1),
    ],
)


@pytest.fixture(scope="module")
def skill_info_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_instancedungeonskillinfo_bss(spec: Any, skill_info_result: HandlerResult) -> None:
    skill_info_result.check(spec)


def test_live_file_parses(skill_info_result: HandlerResult) -> None:
    errors = [r[_ERROR_FIELD] for r in skill_info_result.records if _ERROR_FIELD in r]
    assert not errors, errors


def _pabr_file(lists: dict[tuple[int, int], list[int]], entries: list[tuple[int, int, bytes]]) -> bytes:
    """A file of the newest layout with the given filled lists and skill entries."""
    body = bytearray(b"PABR")
    for class_type in range(CLASS_ROW_COUNT):
        for list_index in range(LIST_COUNT):
            keys = lists.get((class_type, list_index), [])
            body += struct.pack(f"<Q{len(keys)}I", len(keys), *keys)
    body += struct.pack("<I", len(entries))
    for skill_no, unknown_02, values in entries:
        body += struct.pack("<HHI", skill_no, unknown_02, len(values)) + values
    table_start = len(body)
    return bytes(body + struct.pack("<3I", 0, table_start, 0))


def test_lists_and_entries_read_in_file_order() -> None:
    keys = [skill_key(17055, _LEVEL), skill_key(17501, _LEVEL)]
    data = _pabr_file({(_TAMER, 0): keys}, [(17055, _LEVEL, bytes([2])), (17054, _LEVEL, bytes([1, 2]))])
    parsed = parse_instancedungeonskillinfo(data)
    assert parsed.lists == (SkillList(_TAMER, 0, tuple(keys)),)
    assert parsed.entries == (SkillEntry(17055, _LEVEL, (2,)), SkillEntry(17054, _LEVEL, (1, 2)))


def test_a_short_class_row_count_fails() -> None:
    data = _pabr_file({}, [])
    truncated = data[: 4 + 8] + data[-12:-8] + struct.pack("<I", 4 + 8) + data[-4:]
    with pytest.raises(ValueError):
        parse_instancedungeonskillinfo(truncated)
