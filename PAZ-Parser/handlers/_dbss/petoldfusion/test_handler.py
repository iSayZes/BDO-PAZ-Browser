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
    fixed_rows,
    header_count,
    run_case,
)

from _dbss.pet.joins import PET_FILE, PET_OFFSET_FILE, fusion_key, pet_fusion_key
from _dbss.pet.parser import parse_pet_records
from .parser import (
    FILE_NAME,
    KEY_PREFIX_SIZE,
    OFFSET_FILE,
    ROW_SIZE,
    SELECT_FIELDS,
    parse_petoldfusion_records,
    parse_petoldfusionoffset_records,
)


_COUNT_SIZE = 4
_OFFSET_ROW_SIZE = 12
# Rates are on the 1,000,000 = 100% scale.
_FULL_RATE = 1_000_000
_SELECT_KEYS = [field for select in SELECT_FIELDS for field in select]

CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={PET_FILE: PET_FILE, PET_OFFSET_FILE: PET_OFFSET_FILE},
    loc_file=None,
    uses_loc=False,
    loc_fields=[],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["key_prefix", "variant", "species", "unknown_06", "tier", *_SELECT_KEYS, "pet_names"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(ROW_SIZE, header_size=_COUNT_SIZE)),
        *(RangeTest(col=rate, min_val=0, max_val=_FULL_RATE) for _tier, _padding, rate in SELECT_FIELDS),
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
        SchemaTest(required_keys=["fusion_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        DeclaredCountTest(declared=fixed_rows(_OFFSET_ROW_SIZE, header_size=_COUNT_SIZE)),
        RangeTest(col="size", min_val=ROW_SIZE - KEY_PREFIX_SIZE, max_val=ROW_SIZE - KEY_PREFIX_SIZE),
    ],
)

_CASES = {case.handler_name: case for case in (CASE, OFFSET_CASE)}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(_CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in _CASES.items() for spec in case.tests],
)
def test_pet_old_fusion_tables(name: str, spec: Any) -> None:
    _result(name).check(spec)


def _records() -> list[dict]:
    return parse_petoldfusion_records(load_binary_fixture(FILE_NAME))


def test_key_prefix_is_the_four_key_bytes() -> None:
    for record in _records():
        key = fusion_key(record["variant"], record["species"], record["unknown_06"], record["tier"])
        assert record["key_prefix"] == key, record


def test_offset_rows_point_past_each_key_prefix() -> None:
    """Each index row starts at its row's `variant` and covers the row without its key prefix."""
    expected = {
        r["key_prefix"]: (_COUNT_SIZE + index * ROW_SIZE + KEY_PREFIX_SIZE, ROW_SIZE - KEY_PREFIX_SIZE)
        for index, r in enumerate(_records())
    }
    rows = parse_petoldfusionoffset_records(load_binary_fixture(OFFSET_FILE))
    assert {row["fusion_key"]: (row["offset"], row["size"]) for row in rows} == expected


def test_most_fusion_keys_have_a_pet() -> None:
    """Most rows key the fusion key of a pet.dbss pet; a few species have rows but no pet left."""
    pets = parse_pet_records(load_binary_fixture(PET_FILE), load_binary_fixture(PET_OFFSET_FILE))
    pet_keys = {pet_fusion_key(pet) for pet in pets}
    row_keys = {r["key_prefix"] for r in _records()}
    assert len(row_keys & pet_keys) > len(row_keys) // 2


def test_the_first_result_never_lowers_the_main_pet_tier() -> None:
    for record in _records():
        assert record["select_tier_0"] >= record["tier"], record


def test_parser_reads_a_row_and_rejects_extra_or_missing_bytes() -> None:
    selects = struct.pack("<B3sI", 2, b"\x7f\x00\x00", 500_000) + struct.pack("<B3sI", 1, b"\x7f\x00\x00", _FULL_RATE)
    selects += struct.pack("<B3sI", 0, b"\x00\x00\x00", 0) * 2
    data = struct.pack("<II4B", 1, 0x00002801, 1, 40, 0, 0) + selects
    record = parse_petoldfusion_records(data)[0]
    assert record["key_prefix"] == 0x00002801
    assert (record["variant"], record["species"], record["tier"]) == (1, 40, 0)
    assert (record["select_tier_0"], record["select_rate_0"], record["padding_09"]) == (2, 500_000, "7f 00 00")
    assert (record["select_tier_1"], record["select_rate_1"]) == (1, _FULL_RATE)
    with pytest.raises(ValueError):
        parse_petoldfusion_records(data + b"\x00")
    with pytest.raises(ValueError):
        parse_petoldfusion_records(data[:-1])
