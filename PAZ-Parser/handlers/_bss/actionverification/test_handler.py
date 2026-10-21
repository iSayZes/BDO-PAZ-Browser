from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _common.binary import u32
from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from _common.pabr_offset import PABR_MAGIC
from _common.string_hash import ascii_key_hash
from .action_names import ACTION_NAMES, SHEET_ACTION_NAMES
from .parser import FILE_NAME, parse_actionverification_records


# PABR magic, then the u32 character count.
_COUNT_OFFSET = 4
_WARRIOR = 1
_JORDINE = 65002

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["character_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_key",
                "character_name",
                "has_character_row",
                "action_hash",
                "action_name",
                "able_call_time",
            ]
        ),
        TargetTest(
            col="action_hash",
            value=ascii_key_hash("SHADOW_DASHJUMP_ATTACK"),
            expected={"action_name": "SHADOW_DASHJUMP_ATTACK"},
        ),
        TargetTest(col="character_key", value=_WARRIOR, expected={"character_name": "Warrior"}),
        TargetTest(col="character_key", value=_JORDINE, expected={"character_name": "Jordine"}),
    ],
)


def _file(characters: list[tuple[int, list[tuple[int, int]]]], rows_end_delta: int = 0) -> bytes:
    """PABR, the count, the characters, an empty string table and the trailer pointing at it."""
    body = struct.pack("<I", len(characters))
    for character_key, actions in characters:
        body += struct.pack("<HI", character_key, len(actions))
        body += b"".join(struct.pack("<II", *action) for action in actions)
    rows_end = len(PABR_MAGIC) + len(body) + rows_end_delta
    return PABR_MAGIC + body + struct.pack("<III", 0, rows_end, 0)


@pytest.fixture(scope="module")
def actionverification_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_actionverification_bss(spec: Any, actionverification_result: HandlerResult) -> None:
    actionverification_result.check(spec)


def test_every_declared_character_has_actions(actionverification_result: HandlerResult) -> None:
    keys = {record["character_key"] for record in actionverification_result.records}
    assert len(keys) == u32(actionverification_result.source.data, _COUNT_OFFSET)


def test_actions_are_unique_per_character(actionverification_result: HandlerResult) -> None:
    pairs = [(r["character_key"], r["action_hash"]) for r in actionverification_result.records]
    assert len(pairs) == len(set(pairs))


def test_no_two_sheet_names_share_a_hash() -> None:
    assert len(ACTION_NAMES) == len(set(SHEET_ACTION_NAMES))


def test_a_synthetic_file_reads_every_action_in_order() -> None:
    data = _file([(7, [(11, 100), (12, 200)]), (8, []), (9, [(13, 300)])])
    assert parse_actionverification_records(data) == [
        {"character_key": 7, "action_hash": 11, "able_call_time": 100},
        {"character_key": 7, "action_hash": 12, "able_call_time": 200},
        {"character_key": 9, "action_hash": 13, "able_call_time": 300},
    ]


def test_an_action_count_past_the_characters_raises() -> None:
    data = bytearray(_file([(7, [(11, 100)])]))
    struct.pack_into("<I", data, len(PABR_MAGIC) + 4 + 2, 2)
    with pytest.raises(ValueError, match="past the end of the characters"):
        parse_actionverification_records(bytes(data))


def test_characters_that_stop_short_of_the_string_table_raise() -> None:
    data = _file([(7, [(11, 100)])], rows_end_delta=4)
    with pytest.raises(ValueError):
        parse_actionverification_records(data)


def test_a_missing_magic_raises() -> None:
    data = b"XXXX" + _file([(7, [(11, 100)])])[len(PABR_MAGIC) :]
    with pytest.raises(ValueError, match="invalid magic"):
        parse_actionverification_records(data)
