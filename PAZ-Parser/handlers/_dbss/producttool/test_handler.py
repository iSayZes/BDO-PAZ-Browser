from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any

import pytest

from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    RangeTest,
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _dbss.producttool.parser import (
    COUNT_SIZE,
    FILE_NAME,
    OFFSET_FILE,
    RECORD,
    parse_producttool_records,
)

_TRIPLE_FLOAT_FISHING_ROD = 16153
# Cedar Float has one record per enhancement level, so its key carries the level.
_CEDAR_FLOAT = 16169
_CEDAR_FLOAT_LEVEL_3 = 3 << 24 | _CEDAR_FLOAT
_MAX_ENCHANT_LEVEL = 0xFF

_RECORD_KEYS = [
    "item_key",
    "item_key_dup",
    "item_id",
    "enchant_level",
    "item_name",
    "icon_path",
    "unknown_08",
    "unknown_0c",
    "unknown_10",
    "unknown_14",
    "autofishing_time_percents",
]
_OFFSET_KEYS = ["item_key", "item_id", "enchant_level", "data_offset", "data_size"]


def _case(name: str, tests: list[Any], uses_loc: bool) -> HandlerCase:
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file="languagedata_en.loc" if uses_loc else None,
        uses_loc=uses_loc,
        loc_fields=["item_name"] if uses_loc else [],
        internal_path=f"gamecommondata/binary/{name}",
        tests=tests,
    )


CASES = {
    FILE_NAME: _case(
        FILE_NAME,
        [
            SchemaTest(required_keys=_RECORD_KEYS),
            # The u32 record count at +0x00.
            DeclaredCountTest(declared=header_count(offset=0)),
            RangeTest(col="enchant_level", min_val=0, max_val=_MAX_ENCHANT_LEVEL),
            TargetTest(
                col="item_key",
                value=_TRIPLE_FLOAT_FISHING_ROD,
                expected={
                    "item_id": _TRIPLE_FLOAT_FISHING_ROD,
                    "enchant_level": 0,
                    "item_name": "Triple-Float Fishing Rod",
                },
            ),
            TargetTest(
                col="item_key",
                value=_CEDAR_FLOAT_LEVEL_3,
                expected={"item_id": _CEDAR_FLOAT, "enchant_level": 3, "item_name": "Cedar Float"},
            ),
        ],
        uses_loc=True,
    ),
    OFFSET_FILE: _case(
        OFFSET_FILE,
        [
            SchemaTest(required_keys=_OFFSET_KEYS),
            DeclaredCountTest(declared=header_count(offset=0)),
            TargetTest(
                col="item_key",
                value=_CEDAR_FLOAT_LEVEL_3,
                expected={"item_id": _CEDAR_FLOAT, "enchant_level": 3, "data_size": RECORD.size - 4},
            ),
        ],
        uses_loc=False,
    ),
}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in CASES.items() for spec in case.tests],
)
def test_producttool_dbss(name: str, spec: Any) -> None:
    _result(name).check(spec)


def test_each_item_key_appears_once() -> None:
    keys = [record["item_key"] for record in _result(FILE_NAME).records]
    assert len(keys) == len(set(keys))


def test_every_index_row_points_at_its_record_key_copy() -> None:
    # The offset is 4 bytes into the record, at item_key_dup (producttool_dbss.md).
    record_starts = {
        record["item_key"]: COUNT_SIZE + index * RECORD.size
        for index, record in enumerate(_result(FILE_NAME).records)
    }
    rows = _result(OFFSET_FILE).records
    assert {row["item_key"] for row in rows} == set(record_starts)
    for row in rows:
        assert row["data_offset"] == record_starts[row["item_key"]] + 4


def _table(*records: tuple[int, ...]) -> bytes:
    return struct.pack("<I", len(records)) + b"".join(RECORD.pack(*record) for record in records)


def test_records_split_the_item_key_into_item_and_level() -> None:
    key = 10 << 24 | _CEDAR_FLOAT
    records = parse_producttool_records(_table((key, key, 0, 0, 0, 0, 1_000_000), (17591, 17591, 0, 0, 0, 0, 500_000)))
    assert [(r["item_id"], r["enchant_level"], r["autofishing_time_percents"]) for r in records] == [
        (_CEDAR_FLOAT, 10, 1_000_000),
        (17591, 0, 500_000),
    ]


@pytest.mark.parametrize(
    "data",
    [
        b"",
        _table((1, 1, 0, 0, 0, 0, 0))[:-1],
        _table((1, 1, 0, 0, 0, 0, 0)) + b"\x00",
        struct.pack("<I", 1),
        _table((1, 2, 0, 0, 0, 0, 0)),
    ],
    ids=["no_count", "short_record", "trailing_bytes", "missing_record", "keys_differ"],
)
def test_a_file_that_does_not_fit_the_layout_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_producttool_records(data)
