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
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _common.character_link import CHARACTERSTATIC_OFFSET_FILE
from _common.pabr_offset import parse_bare_offset_rows
from _common.pabr_strings import HEADER_SIZE, string_table_start
from .parser import COUNT_OFFSET, FILE_NAME, OFFSET_FILE, parse_buildingupgrade_records


# The loader reads SourceItemKey00 to SourceItemKey04.
_MAX_SOURCE_ITEMS = 5
_HWACHA = 12834
_BIG_HWACHA = 12836
_SAVAGE_BARRICADE = 2056
_SAVAGE_IRON_BARRICADE = 2061
_IRON_INGOT = 4052


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={CHARACTERSTATIC_OFFSET_FILE: CHARACTERSTATIC_OFFSET_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["name", "target_name"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(
            required_keys=[
                "character_key", "upgrade_time", "upgrade_level", "target_character_key", "item_count",
                "items", "name", "has_character_row", "target_name", "has_target_row", "source_items",
            ]
        ),
        DeclaredCountTest(declared=header_count(offset=COUNT_OFFSET)),
        RangeTest(col="item_count", min_val=0, max_val=_MAX_SOURCE_ITEMS),
        TargetTest(
            col="character_key",
            value=_HWACHA,
            expected={"name": "Hwacha", "target_character_key": _BIG_HWACHA, "target_name": "Big Hwacha"},
        ),
        TargetTest(
            col="character_key",
            value=_SAVAGE_BARRICADE,
            expected={"name": "Savage Barricade", "target_character_key": _SAVAGE_IRON_BARRICADE},
        ),
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
        SchemaTest(required_keys=["character_key", "offset", "size"]),
        DeclaredCountTest(declared=header_count(offset=0)),
        TargetTest(col="character_key", value=_HWACHA, expected={"character_key": _HWACHA}),
    ],
)


def _row(key: int, target: int, items: list[tuple[int, int]]) -> bytes:
    head = struct.pack("<HIiHI", key, 90000, 1, target, len(items))
    return head + b"".join(struct.pack("<Iq", item_key, count) for item_key, count in items)


def _table(rows: list[bytes], extra: bytes = b"") -> bytes:
    body = b"PABR" + struct.pack("<I", len(rows)) + b"".join(rows) + extra
    return body + struct.pack("<III", 0, len(body), 0)


@pytest.fixture(scope="module")
def upgrade_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.fixture(scope="module")
def offset_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_OFFSET_RESULT", None)
    if result is None:
        result = run_case(replace(OFFSET_CASE, tests=[]))
        request.module._OFFSET_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_buildingupgrade_dbss(spec: Any, upgrade_result: HandlerResult) -> None:
    upgrade_result.check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_buildingupgradeoffset_dbss(spec: Any, offset_result: HandlerResult) -> None:
    offset_result.check(spec)


def test_keys_are_unique(upgrade_result: HandlerResult) -> None:
    keys = [r["character_key"] for r in upgrade_result.records]
    assert len(keys) == len(set(keys))


def test_offset_rows_tile_the_main_rows() -> None:
    """Each index row starts at its main row's key, and the rows run back to
    back from the end of the header to the string table."""
    main = load_binary_fixture(FILE_NAME)
    rows = sorted(parse_bare_offset_rows(load_binary_fixture(OFFSET_FILE)), key=lambda row: row.offset)
    for row in rows:
        assert struct.unpack_from("<H", main, row.offset)[0] == row.entry_id
    assert rows[0].offset == HEADER_SIZE
    ends = [row.offset + row.size for row in rows]
    assert ends[:-1] == [row.offset for row in rows[1:]]
    assert ends[-1] == string_table_start(main)


def test_a_small_table_reads_back() -> None:
    data = _table([_row(_HWACHA, _BIG_HWACHA, [(_IRON_INGOT, 10), (4057, 5)]), _row(7, 8, [])])
    records = parse_buildingupgrade_records(data)
    assert [r["character_key"] for r in records] == [_HWACHA, 7]
    assert records[0]["target_character_key"] == _BIG_HWACHA
    assert records[0]["items"] == [{"item_key": _IRON_INGOT, "count": 10}, {"item_key": 4057, "count": 5}]
    assert records[1]["item_count"] == 0


def test_a_cut_row_raises() -> None:
    row = _row(_HWACHA, _BIG_HWACHA, [(_IRON_INGOT, 10)])
    with pytest.raises(ValueError):
        parse_buildingupgrade_records(_table([row[:-1]]))


def test_bytes_before_the_string_table_raise() -> None:
    with pytest.raises(ValueError):
        parse_buildingupgrade_records(_table([_row(7, 8, [])], extra=b"\x00"))


def test_an_item_count_past_the_rows_raises() -> None:
    bad = struct.pack("<HIiHI", 7, 0, 1, 8, 0xFFFFFFFF)
    with pytest.raises(ValueError):
        parse_buildingupgrade_records(_table([bad]))
