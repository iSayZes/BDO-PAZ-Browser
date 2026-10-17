from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)
from .parser import parse_petskill_records


# Every pet skill has ten levels; the parser yields one record per level.
_LEVEL_ROWS = 10


def _level_rows() -> DeclaredCount:
    """Level rows: the record count in the data file header, ten rows each."""
    records = header_count()

    def read(source: CaseInput) -> int:
        return records(source) * _LEVEL_ROWS

    return read


PETSKILL_CASE = HandlerCase(
    handler_name="petskill.dbss",
    data_file="petskill.dbss",
    companion_files={"petskilloffset.dbss": "petskilloffset.dbss", "stringtable.bss": "stringtable.bss"},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["skill_type_name"],
    internal_path="gamecommondata/binary/petskill.dbss",
    tests=[
        SchemaTest(
            required_keys=[
                "pet_skill_id",
                "skill_type",
                "skill_type_name",
                "level",
                "param_0",
                "param_1",
                "unknown_list",
                "pet_skill_id_match",
                "skill_type_match",
            ]
        ),
        DeclaredCountTest(declared=_level_rows()),
        # The key prefix, the payload key and the offset row key agree.
        RangeTest(col="pet_skill_id_match", min_val=True, max_val=True),
        # Each level entry repeats the payload's skill type.
        RangeTest(col="skill_type_match", min_val=True, max_val=True),
        RangeTest(col="level", min_val=1, max_val=_LEVEL_ROWS),
        # The two payload sizes: an empty trailing list, or one with a single byte.
        RangeTest(col="data_size", min_val=189, max_val=190),
        TargetTest(
            col="pet_skill_id",
            value=47,
            expected=[{"level": level} for level in range(1, _LEVEL_ROWS + 1)],
        ),
        TargetTest(col="pet_skill_id", value=1, expected={"level": 1}),
        # Type 1 is looting; the pet window fills the pickup time in, the browser shows "?".
        TargetTest(col="pet_skill_id", value=1, expected={"skill_type": 1, "skill_type_name": "Loot (every ? sec)"}),
        TargetTest(col="pet_skill_id", value=21, expected={"skill_type": 2, "skill_type_name": "Finds Resources"}),
    ],
)

PETSKILL_OFFSET_CASE = HandlerCase(
    handler_name="petskilloffset.dbss",
    data_file="petskilloffset.dbss",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/petskilloffset.dbss",
    tests=[
        SchemaTest(required_keys=["pet_skill_id", "data_offset", "data_size", "record_start"]),
        DeclaredCountTest(declared=header_count()),
        RangeTest(col="data_size", min_val=189, max_val=190),
        RangeTest(col="unknown_08", min_val=0, max_val=0),
    ],
)


@pytest.fixture(scope="module")
def petskill_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PETSKILL_RESULT", None)
    if result is None:
        result = run_case(replace(PETSKILL_CASE, tests=[]))
        request.module._PETSKILL_RESULT = result
    return result


@pytest.fixture(scope="module")
def petskill_offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_PETSKILL_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(PETSKILL_OFFSET_CASE, tests=[]))
        request.module._PETSKILL_OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", PETSKILL_CASE.tests, ids=case_id)
def test_petskill_dbss(spec: Any, petskill_result: HandlerResult) -> None:
    petskill_result.check(spec)


@pytest.mark.parametrize("spec", PETSKILL_OFFSET_CASE.tests, ids=case_id)
def test_petskilloffset_dbss(spec: Any, petskill_offset_result: HandlerResult) -> None:
    petskill_offset_result.check(spec)


def _payload(pet_skill_id: int, levels: int, tail: bytes) -> bytes:
    head = struct.pack("<HBiII", pet_skill_id, 1, 1, levels, levels)
    rows = b"".join(struct.pack("<iBiii", level, 1, level, 5000, 0) for level in range(1, levels + 1))
    return head + rows + tail


def _files(payload: bytes, pet_skill_id: int) -> tuple[bytes, bytes]:
    data = struct.pack("<IH", 1, pet_skill_id) + payload
    offsets = struct.pack("<IHIHH", 1, pet_skill_id, 6, len(payload), 0)
    return data, offsets


def test_payload_without_trailing_list_parses() -> None:
    # Older clients (1784) end the payload after the last level entry.
    data, offsets = _files(_payload(7, 3, b""), 7)
    records = parse_petskill_records(data, offsets)
    assert [r["level"] for r in records] == [1, 2, 3]
    assert all(r["unknown_list"] == () for r in records)


def test_payload_with_trailing_list_parses() -> None:
    data, offsets = _files(_payload(7, 2, struct.pack("<IB", 1, 9)), 7)
    assert [r["unknown_list"] for r in parse_petskill_records(data, offsets)] == [(9,), (9,)]


def test_payload_with_leftover_bytes_is_rejected() -> None:
    data, offsets = _files(_payload(7, 2, struct.pack("<IBB", 1, 9, 0)), 7)
    with pytest.raises(ValueError, match="after its levels"):
        parse_petskill_records(data, offsets)
