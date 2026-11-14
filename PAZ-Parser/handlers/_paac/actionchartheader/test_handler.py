from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _common.string_hash import ascii_key_hash
from _paac.actionchartheader.parser import parse_actionchartheader
from tests.framework import (
    DeclaredCountTest, HandlerCase, HandlerResult, SchemaTest, TargetTest, case_id, header_count, run_case,
)

CASE = HandlerCase(
    handler_name="actionchartheader.paach",
    data_file="actionchartheader.paach",
    companion_files={},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path="character/binaryactionchart/actionchartheader.paach",
    tests=[
        SchemaTest(required_keys=["chart_hash", "flag_count", "unknown_flags"]),
        DeclaredCountTest(declared=header_count(offset=8, fmt="<H")),
        # The key is the hash of the chart path below character/binaryactionchart/.
        TargetTest(col="chart_hash", value=ascii_key_hash("pc/3_pew/elfaction_noweapon"), expected={}),
    ],
)


@pytest.fixture(scope="module")
def header_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_actionchartheader_paach(spec: Any, header_result: HandlerResult) -> None:
    header_result.check(spec)


def test_flag_count_is_the_number_of_flag_bytes(header_result: HandlerResult) -> None:
    assert all(len(r["unknown_flags"]) == r["flag_count"] for r in header_result.records)


def _header(entries: list[tuple[int, bytes]], extra: bytes = b"") -> bytes:
    body = b"PABR" + struct.pack("<IH", 1, len(entries))
    body += b"".join(struct.pack("<IH", key, len(flags)) + flags for key, flags in entries) + extra
    body += struct.pack("<I", 1)
    return body + struct.pack("<I", 0) + struct.pack("<II", len(body), 0)


def test_entries_are_read_in_file_order() -> None:
    records = parse_actionchartheader(_header([(7, b"\x10"), (3, b"\xff\x01")]))
    assert [(r["chart_hash"], r["unknown_flags"]) for r in records] == [(7, [0x10]), (3, [0xFF, 0x01])]


def test_bytes_left_after_the_entries_raise() -> None:
    with pytest.raises(ValueError, match="trailing version"):
        parse_actionchartheader(_header([(7, b"\x10")], extra=b"\x00"))
