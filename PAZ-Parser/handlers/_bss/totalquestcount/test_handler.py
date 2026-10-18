from __future__ import annotations

import struct
from collections import Counter
from dataclasses import replace
from typing import Any

import pytest

from tests.fixtures import load_binary_fixture
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

from _bss.allquestlist.parser import parse_allquestlist_records
from _dbss.quest.parser import build_quest_index, parse_quest_record
from .handler import quest_count_records
from .parser import FIRST_VALUE, parse_quest_counts
from .tables import QUEST_COUNT_TABLES, QUEST_REGION_TABLE, QUEST_TYPE_TABLE, QuestCountTable


_U32 = struct.Struct("<I")
_TABLE_START_AT = -8


def _array_length(source: CaseInput) -> int:
    """The u32 count between the magic and the trailer's `table_start`."""
    (table_start,) = _U32.unpack_from(source.file(None), _TABLE_START_AT)
    return (table_start - FIRST_VALUE) // _U32.size


# Names the quest window shows (GAME sheet keys of panel_window_quest_all.luac).
_NAMES: dict[str, list[tuple[int, str]]] = {
    QUEST_REGION_TABLE.file_name: [(2, "Serendia"), (13, "Abyss One"), (17, "Inner Edania")],
    QUEST_TYPE_TABLE.file_name: [(0, "Black Spirit"), (9, "Event"), (12, "Region Bonus")],
}


def _case(quest_table: QuestCountTable) -> HandlerCase:
    key, name = quest_table.key_field, quest_table.name_field
    return HandlerCase(
        handler_name=quest_table.file_name,
        data_file=quest_table.file_name,
        companion_files={"stringtable.bss": "stringtable.bss"},
        loc_file="languagedata_en.loc",
        uses_loc=True,
        loc_fields=[],
        internal_path=f"gamecommondata/binary/{quest_table.file_name}",
        tests=[
            SchemaTest(required_keys=[key, name, "quest_count"]),
            DeclaredCountTest(declared=_array_length),
            RangeTest(col=key, min_val=0, max_val=len(quest_table.enum_names) - 1),
            *(
                TargetTest(col=key, value=value, expected={name: text})
                for value, text in _NAMES[quest_table.file_name]
            ),
        ],
    )


CASES = {quest_table.file_name: _case(quest_table) for quest_table in QUEST_COUNT_TABLES}
_RESULTS: dict[str, HandlerResult] = {}


def _result(name: str) -> HandlerResult:
    if name not in _RESULTS:
        _RESULTS[name] = run_case(replace(CASES[name], tests=[]))
    return _RESULTS[name]


@pytest.mark.parametrize(
    ("name", "spec"),
    [pytest.param(name, spec, id=f"{name}-{case_id(spec)}") for name, case in CASES.items() for spec in case.tests],
)
def test_totalquestcount_bss(name: str, spec: Any) -> None:
    _result(name).check(spec)


@pytest.fixture(scope="module")
def quest_categories() -> Counter[int]:
    """How many `quest.dbss` records hold each `quest_category`."""
    data = load_binary_fixture("quest.dbss")
    ids = [r["packed_quest_id"] for r in parse_allquestlist_records(load_binary_fixture("allquestlist.bss"))]
    index = build_quest_index(data, ids)
    return Counter(parse_quest_record(data, index, row)["quest_category"] for row in range(len(ids)))


def test_type_counts_are_the_quest_categories_of_quest_dbss(quest_categories: Counter[int]) -> None:
    counts = parse_quest_counts(load_binary_fixture(QUEST_TYPE_TABLE.file_name), QUEST_TYPE_TABLE.file_name)
    assert set(quest_categories) <= set(range(len(counts)))
    assert counts == [quest_categories[quest_type] for quest_type in range(len(counts))]


def test_region_counts_do_not_exceed_the_quest_records(quest_categories: Counter[int]) -> None:
    counts = parse_quest_counts(load_binary_fixture(QUEST_REGION_TABLE.file_name), QUEST_REGION_TABLE.file_name)
    assert sum(counts) <= sum(quest_categories.values())


def _counts_file(value_count: int) -> bytes:
    """A PABR quest count file with `value_count` values and an empty string table."""
    table_start = FIRST_VALUE + value_count * _U32.size
    return b"PABR" + bytes(value_count * _U32.size) + _U32.pack(0) + _U32.pack(table_start) + _U32.pack(0)


@pytest.mark.parametrize("quest_table", QUEST_COUNT_TABLES, ids=lambda t: t.file_name)
def test_a_file_shorter_than_the_enum_gets_no_names(quest_table: QuestCountTable) -> None:
    records = quest_count_records(quest_table, _counts_file(len(quest_table.enum_names) - 1), {})
    assert [r[quest_table.name_field] for r in records] == [""] * (len(quest_table.enum_names) - 1)


@pytest.mark.parametrize("quest_table", QUEST_COUNT_TABLES, ids=lambda t: t.file_name)
def test_a_file_with_the_whole_enum_gets_names(quest_table: QuestCountTable) -> None:
    records = quest_count_records(quest_table, _counts_file(len(quest_table.enum_names) + 1), {})
    assert [r[quest_table.name_field] for r in records] == [*quest_table.enum_names, ""]


def test_an_array_end_inside_a_value_raises() -> None:
    data = b"PABR" + bytes(6) + _U32.pack(0) + _U32.pack(10) + _U32.pack(0)
    with pytest.raises(ValueError, match="whole u32"):
        parse_quest_counts(data, "x.bss")


def test_a_missing_magic_raises() -> None:
    with pytest.raises(ValueError, match="invalid magic"):
        parse_quest_counts(bytes(24), "x.bss")
