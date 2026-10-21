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
    case_id,
    run_case,
)

from .parser import parse_guild_right_records


_U32 = struct.Struct("<I")
_GROUP_COUNT_AT = 4
# u8 group_no, u8 unknown_01, u32 group_name_ref, then the u32 right_count.
_RIGHT_COUNT_IN_GROUP = 6
_GROUP_HEAD_SIZE = 10
_RIGHT_SIZE = 12
# __eGuildRightNew_* rights the Lua checks; right 29 is the Guild League sign-up (길드 리그 신청).
_GUILD_LEAGUE_RIGHT = 29


def _declared_rights(source: CaseInput) -> int:
    """The right counts of every group, summed."""
    data = source.data
    (group_count,) = _U32.unpack_from(data, _GROUP_COUNT_AT)
    offset = _GROUP_COUNT_AT + _U32.size
    total = 0
    for _ in range(group_count):
        (right_count,) = _U32.unpack_from(data, offset + _RIGHT_COUNT_IN_GROUP)
        total += right_count
        offset += _GROUP_HEAD_SIZE + right_count * _RIGHT_SIZE
    return total


CASE = HandlerCase(
    handler_name="guildrightnewstaticstatus.bss",
    data_file="guildrightnewstaticstatus.bss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/guildrightnewstaticstatus.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "right_no",
                "group_no",
                "unknown_01",
                "group_name_ref",
                "group_name_kr",
                "name_ref",
                "name_kr",
                "description_ref",
                "description_kr",
            ]
        ),
        DeclaredCountTest(declared=_declared_rights),
        TargetTest(col="right_no", value=_GUILD_LEAGUE_RIGHT, expected={"name_kr": "길드 리그 신청"}),
    ],
)


@pytest.fixture(scope="module")
def rights_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_guildrightnewstaticstatus_bss(spec: Any, rights_result: HandlerResult) -> None:
    rights_result.check(spec)


def test_right_numbers_are_unique_and_named(rights_result: HandlerResult) -> None:
    numbers = [record["right_no"] for record in rights_result.records]
    assert len(numbers) == len(set(numbers))
    assert all(record["name_kr"] and record["group_name_kr"] for record in rights_result.records)


def _pabr(values: bytes, strings: list[str]) -> bytes:
    table_start = _GROUP_COUNT_AT + len(values)
    table = _U32.pack(len(strings))
    for text in strings:
        raw = text.encode("utf-16-le")
        table += struct.pack("<BI", 1, len(raw)) + raw
    return b"PABR" + values + table + _U32.pack(table_start) + _U32.pack(0)


def test_each_right_carries_its_group() -> None:
    group = struct.pack("<BBII", 2, 2, 0, 1) + struct.pack("<III", 11, 1, 2)
    records = parse_guild_right_records(_pabr(_U32.pack(1) + group, ["활동", "수락", "설명"]))
    assert records == [
        {
            "right_no": 11,
            "group_no": 2,
            "unknown_01": 2,
            "group_name_ref": 0,
            "group_name_kr": "활동",
            "name_ref": 1,
            "name_kr": "수락",
            "description_ref": 2,
            "description_kr": "설명",
        }
    ]


def test_a_right_count_past_the_string_table_raises() -> None:
    group = struct.pack("<BBII", 1, 1, 0, 9) + bytes(_RIGHT_SIZE)
    with pytest.raises(ValueError, match="runs past the string table"):
        parse_guild_right_records(_pabr(_U32.pack(1) + group, []))
