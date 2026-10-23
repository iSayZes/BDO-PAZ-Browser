from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import DeclaredCountTest, HandlerCase, HandlerResult, SchemaTest, TargetTest, case_id, run_case

from .handler import command_text
from .parser import ACTION_INPUT_TYPES, FILE_NAME, parse_classinput_records


_U32 = struct.Struct("<I")
_INDEX_HEAD = struct.Struct("<II")
_CLASS_HEAD = struct.Struct("<BQ")
_COUNT_AT = 4
# ActionInputType_WeaponInOut, the sheet's TAB on index 1 (classinputdata_bss.md, Commands).
_WEAPON_IN_OUT = ACTION_INPUT_TYPES.index("WeaponInOut")


def _declared_entries(source: CaseInput) -> int:
    """The class entries the index rows declare."""
    data = source.data
    (index_count,) = _U32.unpack_from(data, _COUNT_AT)
    pos, entries = _COUNT_AT + _U32.size, 0
    for _ in range(index_count):
        _index, class_count = _INDEX_HEAD.unpack_from(data, pos)
        pos += _INDEX_HEAD.size
        for _ in range(class_count):
            _class_no, command_count = _CLASS_HEAD.unpack_from(data, pos)
            pos += _CLASS_HEAD.size + command_count * _U32.size
        entries += class_count
    return entries


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["index", "class_no", "commands", "command_text"]),
        DeclaredCountTest(declared=_declared_entries),
        TargetTest(col="command_text", value="WeaponInOut", expected={"index": 1, "commands": [_WEAPON_IN_OUT]}),
        TargetTest(col="command_text", value="Dash + MoveBack", expected={"index": 2}),
    ],
)


@pytest.fixture(scope="module")
def classinput_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_classinputdata(spec: Any, classinput_result: HandlerResult) -> None:
    classinput_result.check(spec)


def test_every_command_is_an_action_input_type(classinput_result: HandlerResult) -> None:
    for record in classinput_result.records:
        assert record["commands"], record
        assert all(0 <= command < len(ACTION_INPUT_TYPES) for command in record["commands"]), record


def test_each_index_holds_each_class_no_once(classinput_result: HandlerResult) -> None:
    keys = [(record["index"], record["class_no"]) for record in classinput_result.records]
    assert len(keys) == len(set(keys))


def test_a_command_outside_the_enum_shows_its_value() -> None:
    assert command_text([6, 1]) == "Dash + MoveBack"
    assert command_text([len(ACTION_INPUT_TYPES)]) == str(len(ACTION_INPUT_TYPES))


def _pabr(values: bytes) -> bytes:
    table_start = _COUNT_AT + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def _entry(class_no: int, *commands: int) -> bytes:
    return _CLASS_HEAD.pack(class_no, len(commands)) + struct.pack(f"<{len(commands)}I", *commands)


def test_entries_of_one_index_share_its_index() -> None:
    data = _pabr(_U32.pack(1) + _INDEX_HEAD.pack(7, 2) + _entry(0, 4) + _entry(1, 1, 4, 5))
    assert parse_classinput_records(data) == [
        {"index": 7, "class_no": 0, "commands": [4]},
        {"index": 7, "class_no": 1, "commands": [1, 4, 5]},
    ]


def test_a_command_count_past_the_string_table_raises() -> None:
    data = _pabr(_U32.pack(1) + _INDEX_HEAD.pack(1, 1) + _CLASS_HEAD.pack(0, 3) + _U32.pack(10))
    with pytest.raises(ValueError, match="runs past"):
        parse_classinput_records(data)


def test_rows_that_stop_short_of_the_string_table_raise() -> None:
    data = _pabr(_U32.pack(1) + _INDEX_HEAD.pack(1, 1) + _entry(0, 10) + _U32.pack(0))
    with pytest.raises(ValueError, match="rows end"):
        parse_classinput_records(data)
