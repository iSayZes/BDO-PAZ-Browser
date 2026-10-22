from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from _bss.edaniaregioninfo.parser import EDANIA_REGION_NAMES
from .parser import parse_etc_option_records


_U32 = struct.Struct("<I")
_ROWS_AT = 4
# The row fields up to the item count, and the settings after the rows.
_ROW_HEAD_SIZE = 0x43
_SETTINGS_SIZE = 22
_TRAILER_SIZE = 8
_AETHERION = 0
# Aetherion's contents group and boss clear item (edaniaetcoptionstaticstatus_bss.md, Castles).
_AETHERION_CONTENTS_GROUP = 2177
_AZUREACH_CHEST = 890056


def _declared_rows(source: CaseInput) -> int:
    """The rows from +0x04 up to the settings, walked by each row's item count."""
    data = source.data
    (table_start,) = _U32.unpack_from(data, len(data) - _TRAILER_SIZE)
    offset = _ROWS_AT
    rows = 0
    while offset < table_start - _SETTINGS_SIZE:
        (count,) = _U32.unpack_from(data, offset + _ROW_HEAD_SIZE)
        offset += _ROW_HEAD_SIZE + _U32.size + count * _U32.size
        rows += 1
    return rows


CASE = HandlerCase(
    handler_name="edaniaetcoptionstaticstatus.bss",
    data_file="edaniaetcoptionstaticstatus.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["castle_name", "throne_quest_title", "boss_clear_item_name"],
    internal_path="gamecommondata/binary/edaniaetcoptionstaticstatus.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "edania_region",
                "castle_name",
                "contents_group_hash",
                "contents_group",
                "throne_quest",
                "throne_quest_title",
                "boss_clear_item_key",
                "boss_clear_item_name",
                "min_ap_1",
                "min_dp_1",
                "min_item_grade_1",
                "tax_rate",
                "tax_base_amount",
                "unknown_item_ids",
                "drop_buff_count",
                "drop_buff_rate",
                "drop_buff_minutes",
                "unknown_rows_00",
                "unknown_rows_12",
            ],
        ),
        DeclaredCountTest(declared=_declared_rows),
        TargetTest(
            col="edania_region",
            value=_AETHERION,
            expected={
                "castle_name": "Aetherion Castle",
                "contents_group": _AETHERION_CONTENTS_GROUP,
                "throne_quest_title": "[Weekly] For the Throne: Aetherion",
                "boss_clear_item_key": _AZUREACH_CHEST,
                "boss_clear_item_name": "Edania: Azureach Chest",
            },
        ),
    ],
)


@pytest.fixture(scope="module")
def etc_option_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_edaniaetcoptionstaticstatus_bss(spec: Any, etc_option_result: HandlerResult) -> None:
    etc_option_result.check(spec)


def test_one_row_per_castle(etc_option_result: HandlerResult) -> None:
    assert [r["edania_region"] for r in etc_option_result.records] == list(range(len(EDANIA_REGION_NAMES)))


def test_every_row_opens_by_a_contents_group(etc_option_result: HandlerResult) -> None:
    for record in etc_option_result.records:
        assert record["contents_group"] is not None, record


def test_every_throne_quest_names_its_castle(etc_option_result: HandlerResult) -> None:
    for record in etc_option_result.records:
        assert record["throne_quest_title"].startswith("[Weekly] For the Throne: "), record


def _pabr(values: bytes) -> bytes:
    table_start = _ROWS_AT + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


_SETTINGS = struct.pack("<BB5I", 7, 3, 5, 10, 1_000_000, 60, 0)


def test_a_row_reads_its_items_and_the_settings() -> None:
    head = struct.pack("<I4fBIBIIB3sI3fQIB", 0, 1, 2, 1, 2, 4, 13, 4, 13, 4000, 0, b"\x71\x0b\x00", 0x12394, 0, 0, 0, 5, 890056, 0)
    (record,) = parse_etc_option_records(_pabr(head + _U32.pack(1) + _U32.pack(15282) + _SETTINGS))
    assert record["edania_region"] == 0
    assert record["throne_quest"] == 0x12394
    assert record["unknown_23"] == "71 0b 00"
    assert record["unknown_item_ids"] == [15282]
    assert record["tax_rate"] == 4000
    assert record["drop_buff_rate"] == 1_000_000


def test_a_row_that_runs_into_the_settings_raises() -> None:
    with pytest.raises(ValueError, match="runs past its record"):
        parse_etc_option_records(_pabr(b"\x00" * 10 + _SETTINGS))
