from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    case_id,
    header_count,
    run_case,
)

from .parser import FILE_NAME, TYPE_COUNT, parse_selectbox_boxes


# PABR magic, then the u32 box count.
_BOX_COUNT_AT = 4
_U32 = struct.Struct("<I")
_ENTRY = struct.Struct("<IBIQI")
_STRING_HEADER = struct.Struct("<BI")

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["type0_items"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "key",
                "type_lists",
                "tabs",
                *(f"type{index}_items" for index in range(TYPE_COUNT)),
                *(f"type{index}_count" for index in range(TYPE_COUNT)),
            ],
        ),
        DeclaredCountTest(declared=header_count(offset=_BOX_COUNT_AT)),
    ],
)


@pytest.fixture(scope="module")
def selectbox_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_selectbox_bss(spec: Any, selectbox_result: HandlerResult) -> None:
    selectbox_result.check(spec)


def test_every_box_has_a_key_its_entries_share(selectbox_result: HandlerResult) -> None:
    keys = []
    for record in selectbox_result.records:
        assert record["key"] is not None, record
        assert all(entry["key"] == record["key"] for entries in record["type_lists"] for entry in entries), record
        keys.append(record["key"])
    assert len(keys) == len(set(keys))


def test_each_entry_sits_in_the_list_of_its_type(selectbox_result: HandlerResult) -> None:
    for record in selectbox_result.records:
        assert len(record["type_lists"]) == TYPE_COUNT
        for type_index, entries in enumerate(record["type_lists"]):
            assert all(entry["type"] == type_index for entry in entries), record["key"]


def test_every_tab_texture_names_a_string(selectbox_result: HandlerResult) -> None:
    entries = [entry for record in selectbox_result.records for items in record["type_lists"] for entry in items]
    # An index past the string table reads as ''.
    assert all(entry["texture_name_text"] for entry in entries)


def _pabr(body: bytes, strings: list[str]) -> bytes:
    table = _U32.pack(len(strings)) + b"".join(
        _STRING_HEADER.pack(0, len(text)) + text.encode("utf-8") for text in strings
    )
    table_start = 4 + len(body)
    return b"PABR" + body + table + _U32.pack(table_start) + _U32.pack(0)


def test_a_box_reads_five_type_lists() -> None:
    empty_list = _U32.pack(0)
    body = (
        _U32.pack(1)
        + _U32.pack(2) + _ENTRY.pack(65, 0, 17839, 2, 1) + _ENTRY.pack(65, 0, 17849, 1, 1)
        + _U32.pack(1) + _ENTRY.pack(65, 1, 3 << 24 | 752193, 1, 0)
        + empty_list * (TYPE_COUNT - 2)
    )
    boxes = parse_selectbox_boxes(_pabr(body, ["Combine_Tab_Icon_Dark", "Combine_Tab_Icon_Daily"]))
    assert [box["key"] for box in boxes] == [65]
    type_lists = boxes[0]["type_lists"]
    assert [len(entries) for entries in type_lists] == [2, 1, 0, 0, 0]
    assert type_lists[0][1] == {
        "key": 65, "type": 0, "item_key": 17849, "item_count": 1,
        "texture_name": 1, "texture_name_text": "Combine_Tab_Icon_Daily",
    }
    assert type_lists[1][0]["item_key"] >> 24 == 3


def test_boxes_that_stop_short_of_the_string_table_raise() -> None:
    body = _U32.pack(1) + _U32.pack(0) * TYPE_COUNT + bytes(4)
    with pytest.raises(ValueError, match="string table starts"):
        parse_selectbox_boxes(_pabr(body, []))
