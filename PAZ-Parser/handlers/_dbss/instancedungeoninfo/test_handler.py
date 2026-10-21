from __future__ import annotations

import math
import struct
from dataclasses import replace
from typing import Any

import pytest

from bdo_models import PazEntry
from tests.fixtures import load_binary_fixture
from tests.framework import (
    DeclaredCountTest,
    HandlerCase,
    HandlerResult,
    SchemaTest,
    TargetTest,
    case_id,
    fixed_rows,
    header_count,
    run_case,
)

from _common.lookup_index import IndexKind
from _dbss.instancedungeoninfo.handler import InstanceDungeonInfoHandler
from _dbss.instancedungeoninfo.parser import (
    COUNT_SIZE,
    FILE_NAME,
    OFFSET_FILE,
    ROW_SIZE,
    parse_instancedungeoninfo_records,
)

_ENTRY = PazEntry("", f"gamecommondata/binary/{FILE_NAME}", 0, 0, 0, 0, 0)
_KZARKA_FIELD = "칼페온 크자카 인던"


def _case(
    name: str,
    required_keys: list[str],
    extra_tests: list[Any],
    lookup_indexes: dict[IndexKind, dict[int, str]] | None = None,
) -> HandlerCase:
    return HandlerCase(
        handler_name=name,
        data_file=name,
        companion_files={},
        loc_file=None,
        uses_loc=False,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{name}",
        lookup_indexes=lookup_indexes or {},
        tests=[
            SchemaTest(required_keys=required_keys),
            DeclaredCountTest(declared=header_count(offset=0)),
            *extra_tests,
        ],
    )


CASES = {
    FILE_NAME: _case(
        FILE_NAME,
        ["key", "field_no", "field_name", "enter_x", "enter_y", "enter_z", "enter_rotation"],
        # Key 2 enters field 700, the Calpheon Kzarka instance dungeon of
        # fieldinfo.bss and of the client 1784 `Field_Table` sheet.
        [
            DeclaredCountTest(declared=fixed_rows(ROW_SIZE, header_size=COUNT_SIZE)),
            TargetTest(col="key", value=2, expected={"field_no": 700, "field_name": _KZARKA_FIELD}),
        ],
        {IndexKind.FIELD_NAME: {700: _KZARKA_FIELD}},
    ),
    OFFSET_FILE: _case(
        OFFSET_FILE,
        ["key", "offset", "size"],
        [TargetTest(col="key", value=2, expected={"size": ROW_SIZE})],
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
def test_instancedungeoninfo_dbss(name: str, spec: Any) -> None:
    _result(name).check(spec)


def test_keys_are_unique() -> None:
    keys = [r["key"] for r in _result(FILE_NAME).records]
    assert len(keys) == len(set(keys))


def test_offset_rows_point_at_each_row() -> None:
    """Each index row starts at the row with its key and covers the whole row."""
    records = parse_instancedungeoninfo_records(load_binary_fixture(FILE_NAME))
    expected = {record["key"]: (COUNT_SIZE + pos * ROW_SIZE, ROW_SIZE) for pos, record in enumerate(records)}
    actual = {r["key"]: (r["offset"], r["size"]) for r in _result(OFFSET_FILE).records}
    assert actual == expected


def test_rotation_renders_as_degrees() -> None:
    handler = InstanceDungeonInfoHandler()
    handler.lang = "en"
    records = handler.get_records(_table(_row(1, 1239, (0.0, 0.0, 0.0), math.pi / 2)), _ENTRY, {})
    assert "90°" in handler.render_records_page(records, 0, 50)


def _row(key: int, field_no: int, position: tuple[float, float, float], rotation: float) -> bytes:
    return struct.pack("<IH4f", key, field_no, *position, rotation)


def _table(*rows: bytes) -> bytes:
    return struct.pack("<I", len(rows)) + b"".join(rows)


def test_rows_read_back() -> None:
    data = _table(_row(1, 1239, (768000.0, 11542.0, 102400.0), math.pi / 2))
    (record,) = parse_instancedungeoninfo_records(data)
    assert record["key"] == 1
    assert record["field_no"] == 1239
    assert (record["enter_x"], record["enter_y"], record["enter_z"]) == (768000.0, 11542.0, 102400.0)
    assert record["enter_rotation"] == pytest.approx(math.pi / 2)


@pytest.mark.parametrize(
    "data",
    [
        b"",
        _table(_row(0, 700, (0.0, 0.0, 0.0), 0.0))[:-1],
        _table(_row(0, 700, (0.0, 0.0, 0.0), 0.0)) + b"\x00",
        struct.pack("<I", 1),
    ],
    ids=["no_count", "short_row", "trailing_bytes", "missing_row"],
)
def test_a_broken_table_raises(data: bytes) -> None:
    with pytest.raises(ValueError):
        parse_instancedungeoninfo_records(data)
