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
    SchemaTest,
    TargetTest,
    case_id,
    header_count,
    run_case,
)

from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import (
    FILE_NAME,
    KEY_SIZE,
    OFFSET_FILE,
    SOURCE_FILE,
    SOURCE_OFFSET_FILE,
    parse_itemimprovement_records,
    parse_itemimprovementsource_records,
)


# Kharazad Necklace reforms into Dawnbound Kharazad Necklace with Cup of
# Destined Dawn (itemimprovement_dbss.md).
_KHARAZAD_REFORM_KEY = 4233
_KHARAZAD_NECKLACE = 11697
_DAWNBOUND_KHARAZAD_NECKLACE = 11698
_CUP_OF_DESTINED_DAWN = 820974
_ACCESSORY_STONES = 3


def _offset_case(file_name: str, key_field: str) -> HandlerCase:
    return HandlerCase(
        handler_name=file_name,
        data_file=file_name,
        companion_files={},
        loc_file=None,
        uses_loc=False,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{file_name}",
        tests=[
            SchemaTest(required_keys=[key_field, "offset", "size"]),
            DeclaredCountTest(declared=header_count()),
        ],
    )


CASE = HandlerCase(
    handler_name=FILE_NAME,
    data_file=FILE_NAME,
    companion_files={SOURCE_FILE: SOURCE_FILE},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["result", "input", "stones"],
    internal_path=f"gamecommondata/binary/{FILE_NAME}",
    tests=[
        SchemaTest(required_keys=["key", "result_id", "input_id", "group", "result", "input", "stone_ids", "stones"]),
        DeclaredCountTest(declared=header_count()),
        TargetTest(
            col="key",
            value=_KHARAZAD_REFORM_KEY,
            expected={"result_id": _DAWNBOUND_KHARAZAD_NECKLACE, "input_id": _KHARAZAD_NECKLACE},
        ),
    ],
)

SOURCE_CASE = HandlerCase(
    handler_name=SOURCE_FILE,
    data_file=SOURCE_FILE,
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["item_name"],
    internal_path=f"gamecommondata/binary/{SOURCE_FILE}",
    tests=[
        SchemaTest(required_keys=["item_id", "item_name", "icon_path", "category", "group", "is_default_display"]),
        DeclaredCountTest(declared=header_count()),
        TargetTest(col="item_id", value=_CUP_OF_DESTINED_DAWN, expected={"category": _ACCESSORY_STONES}),
    ],
)

OFFSET_CASE = _offset_case(OFFSET_FILE, "key")
SOURCE_OFFSET_CASE = _offset_case(SOURCE_OFFSET_FILE, "item_id")
_CASES = {"gear": CASE, "source": SOURCE_CASE, "offset": OFFSET_CASE, "source_offset": SOURCE_OFFSET_CASE}


@pytest.fixture(scope="module")
def results(request: Any) -> dict[str, HandlerResult]:
    cached = getattr(request.module, "_HANDLER_RESULTS", None)
    if cached is None:
        cached = {name: run_case(replace(case, tests=[])) for name, case in _CASES.items()}
        request.module._HANDLER_RESULTS = cached
    return cached


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_itemimprovement_dbss(spec: Any, results: dict[str, HandlerResult]) -> None:
    results["gear"].check(spec)


@pytest.mark.parametrize("spec", SOURCE_CASE.tests, ids=case_id)
def test_itemimprovementsource_dbss(spec: Any, results: dict[str, HandlerResult]) -> None:
    results["source"].check(spec)


@pytest.mark.parametrize("spec", OFFSET_CASE.tests, ids=case_id)
def test_itemimprovementoffset_dbss(spec: Any, results: dict[str, HandlerResult]) -> None:
    results["offset"].check(spec)


@pytest.mark.parametrize("spec", SOURCE_OFFSET_CASE.tests, ids=case_id)
def test_itemimprovementsourceoffset_dbss(spec: Any, results: dict[str, HandlerResult]) -> None:
    results["source_offset"].check(spec)


def _walked_rows(starts_by_key: dict[int, int], file_size: int) -> dict[int, tuple[int, int]]:
    """`key -> (offset past the key, size without it)` of records walked in file order."""
    ordered = sorted(starts_by_key.items(), key=lambda item: item[1])
    ends = [start for _, start in ordered[1:]] + [file_size]
    return {key: (start + KEY_SIZE, end - start - KEY_SIZE) for (key, start), end in zip(ordered, ends)}


@pytest.mark.parametrize(
    ("file_name", "offset_file", "parse", "key_field"),
    [
        (FILE_NAME, OFFSET_FILE, parse_itemimprovement_records, "key"),
        (SOURCE_FILE, SOURCE_OFFSET_FILE, parse_itemimprovementsource_records, "item_id"),
    ],
)
def test_every_offset_row_points_past_its_records_key(file_name: str, offset_file: str, parse: Any, key_field: str) -> None:
    data = load_binary_fixture(file_name)
    walked = _walked_rows({r[key_field]: r["offset"] for r in parse(data)}, len(data))
    rows = parse_bare_u32_offset_rows(load_binary_fixture(offset_file))
    assert {row.entry_id: (row.offset, row.size) for row in rows} == walked


def test_every_reform_group_has_a_stone(results: dict[str, HandlerResult]) -> None:
    stone_groups = {r["group"] for r in results["source"].records}
    assert {r["group"] for r in results["gear"].records} <= stone_groups


def test_the_dawnbound_reform_lists_its_cup(results: dict[str, HandlerResult]) -> None:
    (record,) = [r for r in results["gear"].records if r["key"] == _KHARAZAD_REFORM_KEY]
    assert _CUP_OF_DESTINED_DAWN in record["stone_ids"]


def _gear(key: int, ids: list[int], group: int) -> bytes:
    return struct.pack(f"<IQ{len(ids)}I", key, len(ids), *ids) + struct.pack("<BB11s", 0, group, bytes(11))


def _file(*records: bytes) -> bytes:
    return struct.pack("<I", len(records)) + b"".join(records)


def test_a_small_gear_file_reads_back() -> None:
    records = parse_itemimprovement_records(_file(_gear(7, [20, 10, 10, 10, 10], 3), _gear(8, [30], 4)))
    assert [(r["key"], r["result_id"], r["input_id"], r["group"]) for r in records] == [(7, 20, 10, 3), (8, None, 30, 4)]


def test_differing_inputs_raise() -> None:
    with pytest.raises(ValueError, match="differing inputs"):
        parse_itemimprovement_records(_file(_gear(7, [20, 10, 10, 11, 10], 3)))


def test_an_unexpected_item_count_raises() -> None:
    with pytest.raises(ValueError, match="holds 2 items"):
        parse_itemimprovement_records(_file(_gear(7, [20, 10], 3)))


def test_bytes_after_the_last_record_raise() -> None:
    with pytest.raises(ValueError, match="bytes after its 1 records"):
        parse_itemimprovement_records(_file(_gear(7, [30], 3)) + bytes(2))
