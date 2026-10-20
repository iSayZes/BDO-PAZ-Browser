from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.case_input import CaseInput
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _common.string_hash import key_hash
from .parser import FILE_NAME, parse_contentsgroupoption_records


_U32 = struct.Struct("<I")
# `_ContentsGroup_DuelCharacter` in global_contentsoptions.luac.
_DUEL_CHARACTER_GROUP = "330"


def _group_count(source: CaseInput) -> int:
    """The u32 `group_count` after the `open_count` hashes."""
    (open_count,) = _U32.unpack_from(source.data, 0)
    (group_count,) = _U32.unpack_from(source.data, _U32.size * (1 + open_count))
    return group_count


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=["key_hash", "contents_group_key", "is_open", "contents_group_number"]
        ),
        DeclaredCountTest(declared=_group_count),
        TargetTest(
            col="contents_group_key",
            value=_DUEL_CHARACTER_GROUP,
            expected={
                "key_hash": key_hash(_DUEL_CHARACTER_GROUP),
                "contents_group_number": int(_DUEL_CHARACTER_GROUP),
            },
        ),
    ],
)


def _file(open_keys: tuple[str, ...], keys: tuple[str, ...], tail: bytes = b"") -> bytes:
    """The open hashes (ascending), then each group as (hash, u64 length, UTF-16LE key)."""
    open_hashes = sorted(key_hash(k) for k in open_keys)
    out = struct.pack(f"<I{len(open_hashes)}I", len(open_hashes), *open_hashes)
    out += _U32.pack(len(keys))
    for key in keys:
        out += struct.pack("<IQ", key_hash(key), len(key)) + key.encode("utf-16-le")
    return out + tail


@pytest.fixture(scope="module")
def contents_group_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_contentsgroupoptionstaticstatusmanager_bss(
    spec: Any, contents_group_result: HandlerResult
) -> None:
    contents_group_result.check(spec)


def test_every_key_hash_is_the_hash_of_its_key(contents_group_result: HandlerResult) -> None:
    mismatches = [
        r["contents_group_key"]
        for r in contents_group_result.records
        if r["key_hash"] != key_hash(r["contents_group_key"])
    ]
    assert not mismatches


def test_keys_are_unique_decimal_numbers(contents_group_result: HandlerResult) -> None:
    keys = [r["contents_group_key"] for r in contents_group_result.records]
    assert len(keys) == len(set(keys))
    assert all(key.isdecimal() for key in keys)


def test_open_groups_match_the_declared_open_count(contents_group_result: HandlerResult) -> None:
    (open_count,) = _U32.unpack_from(contents_group_result.source.data, 0)
    assert sum(1 for r in contents_group_result.records if r["is_open"]) == open_count


def test_groups_read_back_in_file_order() -> None:
    records = parse_contentsgroupoption_records(_file(("7",), ("49", "7", "2295")))
    assert [(r["contents_group_key"], r["is_open"]) for r in records] == [
        ("49", False),
        ("7", True),
        ("2295", False),
    ]


@pytest.mark.parametrize(
    "data",
    [
        _file(("7",), ("49", "7"), tail=b"\0"),
        _file(("8",), ("49", "7")),
        _file((), ("49", "7"))[:-2],
    ],
    ids=["trailing_bytes", "open_hash_without_group", "truncated_key"],
)
def test_a_changed_file_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_contentsgroupoption_records(data)
