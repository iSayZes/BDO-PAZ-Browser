from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
from tests.framework import (
    CaseInput,
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.cashproduct.parser import parse_cashproductoffset_records
from .handler import VALUE_BYTES_FIELD
from .parser import VALUES_START, parse_value_table, row_value_bytes
from .tables import VALUE_TABLES, RowCount, ValueField, ValueTable


_U32 = struct.Struct("<I")
_TABLE_START_AT = -8
_ROW_SIZE_TO_TABLE_START = 4
_TABLES = {value_table.file_name: value_table for value_table in VALUE_TABLES}
_NEWBIE_PRODUCT = "cashproduct_newbieproduct.bss"


def _rows_to_table_start(source: CaseInput) -> int:
    """The 4-byte rows between the magic and the trailer's `table_start`."""
    (table_start,) = _U32.unpack_from(source.data, _TABLE_START_AT)
    return (table_start - VALUES_START) // _ROW_SIZE_TO_TABLE_START


def _lookup_fields(name: str) -> list[str]:
    return [field.lookup.field for field in _TABLES[name].fields if field.lookup is not None]


def _required_keys(value_table: ValueTable) -> list[str]:
    keys = [field.name for field in value_table.fields] + _lookup_fields(value_table.file_name)
    if not value_table.has_named_field:
        keys.append(VALUE_BYTES_FIELD)
    return keys


def _count_tests(value_table: ValueTable) -> list[Any]:
    if value_table.rows is RowCount.COUNTED:
        return [DeclaredCountTest(declared=header_count(offset=VALUES_START))]
    if value_table.rows is RowCount.TO_TABLE_START:
        return [DeclaredCountTest(declared=_rows_to_table_start)]
    return [DeclaredCountTest(declared=lambda _source: 1)]


# Identity anchors: keys and the LOC names they resolve to.
_TARGETS: dict[str, list[TargetTest]] = {
    "interaction.bss": [
        # InteractionType_Awake (CppEnums.InteractionType 61) on both Offin characters.
        TargetTest(col="character_key", value=23751, expected={"interaction_type": 61, "character_name": "Mirumok Watcher Offin"}),
        TargetTest(col="character_key", value=23767, expected={"interaction_type": 61, "character_name": "Mirumok Destroyer Offin"}),
    ],
    "servantchecktitle.bss": [
        TargetTest(
            col="title_id",
            value=2705,
            expected={"title_name": "Captain Epheria", "character_key": 31020, "character_name": "Epheria Galleon"},
        ),
    ],
    "timeattackranking.bss": [
        TargetTest(col="character_key", value=23751, expected={"character_name": "Mirumok Watcher Offin"}),
        TargetTest(col="character_key", value=24385, expected={"character_name": "Transcended Kzarka"}),
    ],
    "vehicletrainingskill.bss": [
        TargetTest(col="skill_key", value=49, expected={"skill_name": "Skill"}),
        TargetTest(col="skill_key", value=50, expected={"skill_name": "Elegance"}),
        TargetTest(col="skill_key", value=51, expected={"skill_name": "Strength"}),
    ],
    "voxelregionskillstaticstatusmanager.bss": [
        # skill_no 42501 and 42502, level 1.
        TargetTest(col="skill_key", value=0xA6050001, expected={"skill_name": "All-Consuming Heat"}),
        TargetTest(col="skill_key", value=0xA6060001, expected={"skill_name": "Dead Soul's Chill"}),
    ],
}


def _case(value_table: ValueTable) -> HandlerCase:
    name = value_table.file_name
    lookup_fields = _lookup_fields(name)
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file="languagedata_en.loc" if lookup_fields else None,
        uses_loc=bool(lookup_fields),
        loc_fields=lookup_fields,
        internal_path=f"gamecommondata/binary/{name}",
        tests=[
            SchemaTest(required_keys=_required_keys(value_table)),
            *_count_tests(value_table),
            *_TARGETS.get(name, []),
        ],
    )


CASES = {value_table.file_name: _case(value_table) for value_table in VALUE_TABLES}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in CASES.items() for spec in case.tests],
)
def test_pabr_values(name: str, spec: Any) -> None:
    _result(name).check(spec)


@pytest.mark.parametrize("name", [name for name in _TABLES if _lookup_fields(name)])
def test_every_key_has_a_loc_name(name: str) -> None:
    for record in _result(name).records:
        for field in _lookup_fields(name):
            assert record[field], f"{name}: no LOC name for {record}"


def test_the_newbie_product_is_a_cash_product() -> None:
    (record,) = _result(_NEWBIE_PRODUCT).records
    product_ids = {row["product_id"] for row in parse_cashproductoffset_records(load_binary_fixture("cashproductoffset.dbss"))}
    assert record["product_id"] in product_ids


# Synthetic files: PABR, the values, an empty string table and the trailer.
def _pabr(values: bytes) -> bytes:
    table_start = VALUES_START + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


_ONE = ValueTable("one.bss", (ValueField("a", "I", "productId"), ValueField("unknown_04", "2s")))
_COUNTED = ValueTable("counted.bss", (ValueField("key", "B", "skillId"),), RowCount.COUNTED)
_COUNTED_PAIRS = ValueTable("pairs.bss", (ValueField("unknown_00", "B"), ValueField("unknown_01", "B")), RowCount.COUNTED)
_ROWS = ValueTable("rows.bss", (ValueField("a", "H", "regionKey"), ValueField("b", "H")), RowCount.TO_TABLE_START)


def test_one_value_set_reads_one_record_with_hex_bytes() -> None:
    data = _pabr(_U32.pack(7) + b"\x01\x0a")
    assert parse_value_table(data, _ONE) == [{"a": 7, "unknown_04": "01 0a"}]


def test_a_counted_list_reads_one_record_per_entry() -> None:
    data = _pabr(_U32.pack(3) + bytes([49, 50, 51]))
    assert parse_value_table(data, _COUNTED) == [{"key": 49}, {"key": 50}, {"key": 51}]


def test_cultivation_event_types_are_unique() -> None:
    types = [record["cultivation_event_type"] for record in _result("cultivationevent.bss").records]
    assert len(types) == len(set(types))


def test_row_value_bytes_split_a_counted_list_into_rows() -> None:
    data = _pabr(_U32.pack(2) + bytes([1, 2, 3, 4]))
    assert row_value_bytes(data, _COUNTED_PAIRS) == ["01 02", "03 04"]


def test_row_value_bytes_of_one_value_set_hold_every_value_byte() -> None:
    data = _pabr(_U32.pack(7) + bytes([1, 10]))
    assert row_value_bytes(data, _ONE) == ["07 00 00 00 01 0a"]


def test_rows_run_up_to_the_string_table() -> None:
    data = _pabr(struct.pack("<HHHH", 1176, 1, 1484, 2))
    assert parse_value_table(data, _ROWS) == [{"a": 1176, "b": 1}, {"a": 1484, "b": 2}]


def test_a_count_past_the_string_table_raises() -> None:
    data = _pabr(_U32.pack(4) + bytes([49, 50, 51]))
    with pytest.raises(ValueError, match="string table starts"):
        parse_value_table(data, _COUNTED)


def test_values_that_stop_short_of_the_string_table_raise() -> None:
    data = _pabr(_U32.pack(7) + b"\x01\x0a\x00")
    with pytest.raises(ValueError, match="string table starts"):
        parse_value_table(data, _ONE)


def test_rows_that_split_at_the_string_table_raise() -> None:
    data = _pabr(struct.pack("<HHH", 1176, 1, 1484))
    with pytest.raises(ValueError, match="not after whole 4-byte rows"):
        parse_value_table(data, _ROWS)


def test_a_bad_magic_raises() -> None:
    with pytest.raises(ValueError, match="invalid magic"):
        parse_value_table(b"XXXX" + _pabr(_U32.pack(7) + b"\x01\x0a")[4:], _ONE)
