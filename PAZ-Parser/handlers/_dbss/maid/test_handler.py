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
    case_id,
    header_count,
    run_case,
)

from _bss.pcroommaid.parser import parse_pcroommaid
from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from _common.pabr_offset import parse_bare_offset_rows
from .parser import CHIEF_FIELDS, FILE_NAME, FLAG_FIELDS, OFFSET_FILE, parse_maid_records


_COUNT_SIZE = 4
_KEY_PREFIX_SIZE = 2


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=[
            "character_key", "max_action_index", "cool_time", *FLAG_FIELDS, "skill_0", "skill_1", "forms",
            *CHIEF_FIELDS, "name", "has_character_row",
        ]),
        DeclaredCountTest(declared=header_count(offset=0)),
        *(RangeTest(col=field, min_val=0, max_val=1) for field in (*FLAG_FIELDS, *CHIEF_FIELDS)),
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
        SchemaTest(required_keys=["character_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
    ],
)


@pytest.fixture(scope="module")
def maid_result(request: Any) -> HandlerResult:
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
def test_maid_dbss(spec: Any, maid_result: HandlerResult) -> None:
    maid_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_maidoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_character_keys_are_unique(maid_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in maid_result.records]
    assert len(keys) == len(set(keys))


def test_offset_rows_point_at_each_row() -> None:
    """The index lists the rows in file order; each points past its key prefix and spans up to the next prefix."""
    data = load_binary_fixture(FILE_NAME)
    records = parse_maid_records(data)
    rows = parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE))
    assert [row.entry_id for row in rows] == [r["character_key"] for r in records]

    record_start = _COUNT_SIZE
    for row in rows:
        assert row.offset == record_start + _KEY_PREFIX_SIZE, row.entry_id
        assert struct.unpack_from("<H", data, record_start)[0] == row.entry_id
        record_start = row.offset + row.size
    assert record_start == len(data)


def test_pc_room_rows_are_the_pcroommaid_keys() -> None:
    """pcroommaid.bss lists the keys whose pc_room_type is set, in maid.dbss row order."""
    records = parse_maid_records(load_binary_fixture(FILE_NAME))
    pc_room_keys = [r["character_key"] for r in records if r["pc_room_type"]]
    assert [r["character_key"] for r in parse_pcroommaid(load_binary_fixture("pcroommaid.bss"))] == pc_room_keys


def test_form_icons_are_dds_paths(maid_result: HandlerResult) -> None:
    for record in maid_result.records:
        for form in record["forms"]:
            assert form["icon_path"].lower().endswith(".dds"), record["character_key"]


def _row(key: int, forms: list[tuple[int, str]]) -> bytes:
    head = struct.pack("<HIq6BIII", key, 0, 1_200_000, 1, 1, 0, 0, 0, 0, 0, 0, len(forms))
    body = b"".join(
        struct.pack("<iQ", action_index, len(path)) + path.encode("utf-16-le") for action_index, path in forms
    )
    return head + body + bytes((1, 0))


def test_parser_reads_rows_with_and_without_forms() -> None:
    data = (
        struct.pack("<I", 2)
        + struct.pack("<H", 18951) + _row(18951, [(0, "a.dds")])
        + struct.pack("<H", 18960) + _row(18960, [])
    )
    first, second = parse_maid_records(data)
    assert first["character_key"] == 18951
    assert first["cool_time"] == 1_200_000
    assert (first["is_able_in_warehouse"], first["is_able_submit_market"]) == (1, 0)
    assert first["forms"] == [{"action_index": 0, "icon_path": "a.dds"}]
    assert (first["is_maid_chief"], first["is_maid_chief_market"]) == (1, 0)
    assert second["character_key"] == 18960
    assert second["forms"] == []


def test_parser_rejects_extra_bytes_and_a_wrong_key_prefix() -> None:
    row = _row(18951, [])
    with pytest.raises(ValueError):
        parse_maid_records(struct.pack("<IH", 1, 18951) + row + b"\x00")
    with pytest.raises(ValueError):
        parse_maid_records(struct.pack("<IH", 1, 18951) + row[:-1])
    with pytest.raises(ValueError):
        parse_maid_records(struct.pack("<IH", 1, 18952) + row)
