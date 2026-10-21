from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _bss.enchantfailcountexpstaticstatus.parser import parse_enchantfailcountexp_rows
from tests.framework import (
    CaseInput,
    DeclaredCount,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    case_id,
    run_case,
)


_HEADER_SIZE = 8
_STACK_SIZE = 8
_PEN = 20


def _entry_rows() -> DeclaredCount:
    """Entry rows: the sum of every declared group's entry_count, walked with
    struct apart from the parser."""

    def read(source: CaseInput) -> int:
        raw = source.file(None)
        (count,) = struct.unpack_from("<I", raw, 4)
        pos, total = _HEADER_SIZE, 0
        for _ in range(count):
            (group_count,) = struct.unpack_from("<I", raw, pos)
            pos += 4
            for _ in range(group_count):
                entry_count = struct.unpack_from("<I", raw, pos + 2)[0]
                pos += 6 + entry_count * 5
                total += entry_count
            pos += _STACK_SIZE
        return total

    return read


CASE = HandlerCase(
    handler_name="enchantfailcountexpstaticstatus.bss",
    data_file="enchantfailcountexpstaticstatus.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path="gamecommondata/binary/enchantfailcountexpstaticstatus.bss",
    tests=[
        SchemaTest(required_keys=["stack", "fairy_feed_key", "enchant_level", "unknown_01"]),
        DeclaredCountTest(declared=_entry_rows()),
        RangeTest(col="enchant_level", min_val=0, max_val=_PEN),
    ],
)


@pytest.fixture(scope="module")
def enchantfailcountexp_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_enchantfailcountexpstaticstatus_bss(
    spec: Any,
    enchantfailcountexp_result: HandlerResult,
) -> None:
    enchantfailcountexp_result.check(spec)


def test_every_declared_record_has_its_own_stack(enchantfailcountexp_result: HandlerResult) -> None:
    (count,) = struct.unpack_from("<I", enchantfailcountexp_result.source.file(None), 4)
    stacks = {record["stack"] for record in enchantfailcountexp_result.records}
    assert len(stacks) == count


def test_every_stack_holds_the_same_entries(enchantfailcountexp_result: HandlerResult) -> None:
    pairs_by_stack: dict[int, list[tuple[int, int]]] = {}
    for record in enchantfailcountexp_result.records:
        pairs_by_stack.setdefault(record["stack"], []).append(
            (record["fairy_feed_key"], record["enchant_level"])
        )
    assert len({tuple(pairs) for pairs in pairs_by_stack.values()}) == 1


def _record(stack: int, groups: list[tuple[int, list[tuple[int, int]]]]) -> bytes:
    body = struct.pack("<I", len(groups))
    for key, entries in groups:
        body += struct.pack("<HI", key, len(entries))
        body += b"".join(struct.pack("<BI", level, value) for level, value in entries)
    return body + struct.pack("<Q", stack)


def _file(records: list[bytes]) -> bytes:
    body = b"".join(records)
    end_of_records = _HEADER_SIZE + len(body)
    head = b"PABR" + struct.pack("<I", len(records))
    return head + body + struct.pack("<III", 0, end_of_records, 0)


def test_a_synthetic_file_reads_the_stack_after_the_groups() -> None:
    data = _file([
        _record(7, [(1, [(19, 55), (20, 75)]), (3, [(0, 6)])]),
        _record(2, [(1, [(19, 0), (20, 1)]), (3, [(0, 0)])]),
    ])
    rows = parse_enchantfailcountexp_rows(data)
    assert rows == [
        {"stack": 7, "fairy_feed_key": 1, "enchant_level": 19, "unknown_01": 55},
        {"stack": 7, "fairy_feed_key": 1, "enchant_level": 20, "unknown_01": 75},
        {"stack": 7, "fairy_feed_key": 3, "enchant_level": 0, "unknown_01": 6},
        {"stack": 2, "fairy_feed_key": 1, "enchant_level": 19, "unknown_01": 0},
        {"stack": 2, "fairy_feed_key": 1, "enchant_level": 20, "unknown_01": 1},
        {"stack": 2, "fairy_feed_key": 3, "enchant_level": 0, "unknown_01": 0},
    ]


def test_an_entry_count_past_the_string_table_raises() -> None:
    data = bytearray(_file([_record(0, [(1, [(19, 55)])])]))
    # entry_count of the only group: header, group_count, then the u16 key.
    struct.pack_into("<I", data, _HEADER_SIZE + 4 + 2, 9)
    with pytest.raises(ValueError):
        parse_enchantfailcountexp_rows(bytes(data))


def test_a_short_walk_raises() -> None:
    data = bytearray(_file([_record(0, [(1, [(19, 55)])])]))
    # Points end_of_records 4 bytes past where the records stop.
    end_offset = len(data) - 8
    struct.pack_into("<I", data, end_offset, struct.unpack_from("<I", data, end_offset)[0] + 4)
    with pytest.raises(ValueError):
        parse_enchantfailcountexp_rows(bytes(data))
