from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from _bss.itemmaingroup.parser import MainGroupEntry, parse_itemmaingroup_records
from _common.pabr_offset import parse_pabr_offset_rows
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

_SUBGROUP_FILE = "itemsubgroup.dbss"
_SUBGROUP_OFFSET_FILE = "itemsubgroupoffset.dbss"
# The list of items general store NPCs buy: one subgroup of the same key, no condition.
_SHOP_SELL_GROUP = 52001

CASE = HandlerCase(
    handler_name="itemmaingroup.bss",
    data_file="itemmaingroup.bss",
    companion_files={name: name for name in (_SUBGROUP_FILE, _SUBGROUP_OFFSET_FILE)},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["Item Names"],
    internal_path="gamecommondata/binary/itemmaingroup.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "group_id", "subgroup_keys", "conditions", "subgroups_text",
                "item_count", "item_keys", "items",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=4)),
        TargetTest(
            col="group_id",
            value=_SHOP_SELL_GROUP,
            expected={"subgroup_keys": [_SHOP_SELL_GROUP], "conditions": [""]},
        ),
    ],
)


@pytest.fixture(scope="module")
def itemmaingroup_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemmaingroup_bss(spec: Any, itemmaingroup_result: HandlerResult) -> None:
    itemmaingroup_result.check(spec)


def test_every_subgroup_is_in_itemsubgroup(itemmaingroup_result: HandlerResult) -> None:
    source = itemmaingroup_result.source
    known = {row.entry_id for row in parse_pabr_offset_rows(source.file(_SUBGROUP_OFFSET_FILE))}

    missing = [
        (record["group_id"], key)
        for record in itemmaingroup_result.records
        for key in record["subgroup_keys"]
        if key not in known
    ]

    assert not missing


def test_group_ids_are_unique(itemmaingroup_result: HandlerResult) -> None:
    ids = [record["group_id"] for record in itemmaingroup_result.records]
    assert len(ids) == len(set(ids))


def _wide(text: str) -> bytes:
    payload = text.encode("utf-16-le")
    return struct.pack("<BI", 1, len(payload)) + payload


def _group(group_id: int, entries: list[tuple[int, int]]) -> bytes:
    head = struct.pack("<IB8xi8xI", group_id, 1, -1, len(entries))
    return head + b"".join(struct.pack("<IIH", 0, ref, key) for ref, key in entries)


def _file(groups: list[bytes], strings: list[str]) -> bytes:
    body = b"PABR" + struct.pack("<I", len(groups)) + b"".join(groups)
    table = struct.pack("<I", len(strings)) + b"".join(_wide(text) for text in strings)
    return body + table + struct.pack("<II", len(body), 0)


def test_parser_reads_entries_and_conditions() -> None:
    data = _file([_group(7, [(0, 40189), (1, 54001)]), _group(8, [])], ["", "checkexplore(103, 1)"])

    groups = parse_itemmaingroup_records(data)

    assert [group.group_id for group in groups] == [7, 8]
    assert groups[0].entries == (MainGroupEntry(40189, ""), MainGroupEntry(54001, "checkexplore(103, 1)"))
    assert groups[1].entries == ()


def test_parser_rejects_a_condition_past_the_table() -> None:
    with pytest.raises(ValueError):
        parse_itemmaingroup_records(_file([_group(7, [(5, 1)])], [""]))


def test_parser_rejects_groups_that_miss_the_string_table() -> None:
    data = bytearray(_file([_group(7, [(0, 1)])], [""]))
    # Claim one group fewer: the walk stops before the string table.
    struct.pack_into("<I", data, 4, 0)
    with pytest.raises(ValueError):
        parse_itemmaingroup_records(bytes(data))
