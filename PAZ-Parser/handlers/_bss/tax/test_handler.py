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
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    run_case,
)

from .handler import TAX_TYPE_NAMES, tax_type_text
from .parser import TAX_TYPE_COUNT, parse_tax_records


_U32 = struct.Struct("<I")
_ROW_COUNT_AT = 4
_ROWS_AT = 8
# territoryinfo.bss keys: Balenos and Calpheon.
_BALENOS = 0
_CALPHEON = 2


def _declared_records(source: CaseInput) -> int:
    """Eight tax types for each row the file declares."""
    (row_count,) = _U32.unpack_from(source.data, _ROW_COUNT_AT)
    return row_count * TAX_TYPE_COUNT


CASE = HandlerCase(
    handler_name="tax.bss",
    data_file="tax.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["territory_name"],
    internal_path="gamecommondata/binary/tax.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "territory_key",
                "territory_key_dup",
                "territory_name",
                "tax_type",
                "min_percent_or_price",
                "max_percent_or_price",
                "system_percent",
            ],
        ),
        DeclaredCountTest(declared=_declared_records),
        RangeTest(col="tax_type", min_val=0, max_val=TAX_TYPE_COUNT - 1),
        TargetTest(col="territory_key", value=_BALENOS, expected={"territory_name": "Balenos"}),
        TargetTest(col="territory_key", value=_CALPHEON, expected={"territory_name": "Calpheon"}),
    ],
)


@pytest.fixture(scope="module")
def tax_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_tax_bss(spec: Any, tax_result: HandlerResult) -> None:
    tax_result.check(spec)


def test_each_row_repeats_its_territory_key(tax_result: HandlerResult) -> None:
    for record in tax_result.records:
        assert record["territory_key_dup"] == record["territory_key"], record


def test_each_territory_has_every_tax_type_once(tax_result: HandlerResult) -> None:
    types_by_territory: dict[int, list[int]] = {}
    for record in tax_result.records:
        types_by_territory.setdefault(record["territory_key"], []).append(record["tax_type"])
    assert types_by_territory
    assert all(types == list(range(TAX_TYPE_COUNT)) for types in types_by_territory.values())


def test_the_maximum_is_not_below_the_minimum(tax_result: HandlerResult) -> None:
    for record in tax_result.records:
        assert record["min_percent_or_price"] <= record["max_percent_or_price"], record


def test_tax_types_read_as_enum_names() -> None:
    assert len(TAX_TYPE_NAMES) == TAX_TYPE_COUNT
    assert tax_type_text(4) == "4 DeliverItemByPublicWagon"
    assert tax_type_text(TAX_TYPE_COUNT) == str(TAX_TYPE_COUNT)


def _pabr(values: bytes) -> bytes:
    table_start = _ROWS_AT - _U32.size + len(values)
    return b"PABR" + values + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


def test_a_row_reads_eight_tax_types() -> None:
    taxes = b"".join(struct.pack("<3i", 0, 100 + tax_type, tax_type) for tax_type in range(TAX_TYPE_COUNT))
    row = struct.pack("<hh", _CALPHEON, _CALPHEON) + taxes
    records = parse_tax_records(_pabr(_U32.pack(1) + row))
    assert [record["tax_type"] for record in records] == list(range(TAX_TYPE_COUNT))
    assert records[3] == {
        "territory_key": _CALPHEON,
        "territory_key_dup": _CALPHEON,
        "tax_type": 3,
        "min_percent_or_price": 0,
        "max_percent_or_price": 103,
        "system_percent": 3,
    }


def test_rows_that_stop_short_of_the_string_table_raise() -> None:
    row = struct.pack("<hh", _BALENOS, _BALENOS) + bytes(TAX_TYPE_COUNT * 12) + b"\x00"
    with pytest.raises(ValueError, match="string table starts"):
        parse_tax_records(_pabr(_U32.pack(1) + row))
