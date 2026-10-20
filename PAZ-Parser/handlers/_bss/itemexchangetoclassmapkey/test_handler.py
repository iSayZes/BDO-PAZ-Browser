from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _dbss.itemexchangetoclass.parser import FILE_NAME as GROUP_FILE, parse_itemexchangetoclass_records
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    UserLanguageTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, parse_itemexchangetoclassmapkey_records


# PABR magic, then the u32 count.
_COUNT_OFFSET = 4
# Tuvala Longsword, in the Tuvala main weapon group.
_TUVALA_LONGSWORD = 695113
_TUVALA_MAIN_WEAPON = 165

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["item_key", "key", "item_name"]),
        DeclaredCountTest(declared=header_count(offset=_COUNT_OFFSET)),
        TargetTest(
            col="item_key",
            value=_TUVALA_LONGSWORD,
            expected={"key": _TUVALA_MAIN_WEAPON, "item_name": "Tuvala Longsword"},
        ),
        UserLanguageTest(fields=["item_name"]),
    ],
)


@pytest.fixture(scope="module")
def mapkey_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemexchangetoclassmapkey_bss(spec: Any, mapkey_result: HandlerResult) -> None:
    mapkey_result.check(spec)


def test_item_keys_are_unique(mapkey_result: HandlerResult) -> None:
    item_keys = [r["item_key"] for r in mapkey_result.records]
    assert len(item_keys) == len(set(item_keys)), "an item key has two entries"


def test_entries_invert_the_group_table(mapkey_result: HandlerResult) -> None:
    """Every item itemexchangetoclass.dbss lists has one entry, naming a group that lists it."""
    groups_of_item: dict[int, set[int]] = {}
    for row in parse_itemexchangetoclass_records(load_binary_fixture(GROUP_FILE)):
        for item_key in row["item_keys"]:
            if item_key:
                groups_of_item.setdefault(item_key, set()).add(row["key"])
    actual = {r["item_key"]: r["key"] for r in mapkey_result.records}
    assert set(actual) == set(groups_of_item)
    assert all(key in groups_of_item[item_key] for item_key, key in actual.items())


def _file(entries: list[tuple[int, int]]) -> bytes:
    """A PABR file of `entries` and an empty string table."""
    body = b"".join(struct.pack("<Ii", *entry) for entry in entries)
    rows_end = 8 + len(body)
    return b"PABR" + struct.pack("<I", len(entries)) + body + struct.pack("<III", 0, rows_end, 0)


def test_parser_reads_entries() -> None:
    records = parse_itemexchangetoclassmapkey_records(_file([(_TUVALA_LONGSWORD, _TUVALA_MAIN_WEAPON), (10001, 1)]))
    assert records == [
        {"item_key": _TUVALA_LONGSWORD, "key": _TUVALA_MAIN_WEAPON},
        {"item_key": 10001, "key": 1},
    ]


def test_parser_rejects_a_count_past_the_string_table() -> None:
    data = bytearray(_file([(_TUVALA_LONGSWORD, _TUVALA_MAIN_WEAPON)]))
    struct.pack_into("<I", data, _COUNT_OFFSET, 2)
    with pytest.raises(ValueError):
        parse_itemexchangetoclassmapkey_records(bytes(data))
