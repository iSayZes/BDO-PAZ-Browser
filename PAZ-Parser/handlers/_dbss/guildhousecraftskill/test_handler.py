from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
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

from .parser import FILE_NAME, OFFSET_FILE, ROW_SIZE, SKILL_SLOT_COUNT, parse_guildhousecraftskill_records


_COUNT_OFFSET = 0
_COUNT_SIZE = 4
# The index points past the row's leading key, at receipe_key_dup.
_INDEXED_KEY_SIZE = 4
_STORAGE = 2
_GUILD_SHIPYARD = 1601


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "receipe_key", "receipe_key_dup", "unknown_08", "skill_nos",
            "name", "skills", "skill_count", "skills_text",
        ]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        RangeTest(col="skill_count", min_val=0, max_val=SKILL_SLOT_COUNT),
        UserLanguageTest(fields=["name"]),
        TargetTest(col="receipe_key", value=_STORAGE, expected={"name": "Storage"}),
        TargetTest(col="receipe_key", value=_GUILD_SHIPYARD, expected={"name": "Guild Shipyard"}),
    ],
)

OFFSET_CASE = HandlerCase(
    handler_name=OFFSET_FILE,
    data_file=OFFSET_FILE,
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{OFFSET_FILE}",
    tests=[
        SchemaTest(required_keys=["receipe_key", "data_offset", "data_size"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(col="receipe_key", value=_GUILD_SHIPYARD, expected={"receipe_key": _GUILD_SHIPYARD}),
    ],
)


@pytest.fixture(scope="module")
def skill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_guildhousecraftskill_dbss(spec: Any, skill_result: HandlerResult) -> None:
    skill_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_guildhousecraftskilloffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_keys_are_unique_and_repeated(skill_result: HandlerResult) -> None:
    keys = [r["receipe_key"] for r in skill_result.records]
    assert len(keys) == len(set(keys))
    assert all(r["receipe_key_dup"] == r["receipe_key"] for r in skill_result.records)


def test_skill_slots_fill_from_the_first(skill_result: HandlerResult) -> None:
    """A row's skills are its first `skill_count` slots; the rest are 0."""
    for r in skill_result.records:
        assert r["skill_nos"] == r["skills"] + [0] * (SKILL_SLOT_COUNT - r["skill_count"])


def test_offset_rows_point_past_each_leading_key(offset_result: HandlerResult) -> None:
    """Each index row starts 4 bytes into the row with its key and runs to its end."""
    records = parse_guildhousecraftskill_records(load_binary_fixture(FILE_NAME))
    expected = {
        r["receipe_key"]: (_COUNT_SIZE + index * ROW_SIZE + _INDEXED_KEY_SIZE, ROW_SIZE - _INDEXED_KEY_SIZE)
        for index, r in enumerate(records)
    }
    actual = {r["receipe_key"]: (r["data_offset"], r["data_size"]) for r in offset_result.records}
    assert actual == expected


def _row(key: int, skills: list[int]) -> bytes:
    slots = skills + [0] * (SKILL_SLOT_COUNT - len(skills))
    return struct.pack(f"<iiH{SKILL_SLOT_COUNT}H", key, key, 0, *slots)


def test_parser_reads_rows_and_rejects_bytes_after_them() -> None:
    data = struct.pack("<I", 2) + _row(_GUILD_SHIPYARD, [65042, 65043]) + _row(_STORAGE, [65062])
    records = parse_guildhousecraftskill_records(data)
    assert [(r["receipe_key"], r["skill_nos"]) for r in records] == [
        (_GUILD_SHIPYARD, [65042, 65043, 0, 0, 0]),
        (_STORAGE, [65062, 0, 0, 0, 0]),
    ]
    with pytest.raises(ValueError):
        parse_guildhousecraftskill_records(data + b"\x00")


def test_parser_rejects_a_row_cut_short() -> None:
    data = struct.pack("<I", 1) + _row(_STORAGE, [65062])[:-1]
    with pytest.raises(ValueError):
        parse_guildhousecraftskill_records(data)
