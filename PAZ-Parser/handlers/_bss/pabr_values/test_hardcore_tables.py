"""Checks of the Hardcore channel tables in `hardcore_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

import re
import struct

import pytest

from tests.fixtures import load_binary_fixture

from _common.class_type import PLAYABLE_CLASSES_MASK, class_types_in_mask
from .hardcore_names import grade_name
from .hardcore_tables import HARDCORE_TABLES
from .handler import PabrValuesBssHandler
from .layout import RowCount, ValueField, ValueTable
from .names import map_color_text
from .parser import parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in HARDCORE_TABLES}
_CHANNEL_INFO = "hardcorechannelinfo.bss"
_ETC_OPTION = "hardcorechanneletcoptionstaticstatus.bss"
_TITLES = "hardcorechanneltitlestaticstatusmanager.bss"
_GRADES = "hardcorechanneltotalrankgradestaticstatusmanager.bss"
# The ranking window's _totalGradeCount and _topRankerCount (panel_widget_ranking_hardcore.luac).
_GRADE_COUNT = 10
_TOP_RANKER_COUNT = 3
# The kill count in a title's condition text: "<난폭한> 사막 나가 100마리 처치".
_CONDITION_COUNT = re.compile(r"(\d+)마리 처치")
_U32 = struct.Struct("<I")


def _records(name: str) -> list[dict]:
    return parse_value_table(load_binary_fixture(name), _TABLES[name])


def test_every_map_color_is_unique() -> None:
    colors = [record["map_color"] for record in _records(_CHANNEL_INFO)]
    assert colors and len(colors) == len(set(colors))


def test_each_map_color_is_stored_twice() -> None:
    for record in _records(_CHANNEL_INFO):
        assert record["unknown_04"] == record["map_color"], record


def test_a_map_color_reads_blue_green_red() -> None:
    assert map_color_text("e8 1b 18") == "181be8"


def test_no_possible_class_is_an_unused_class_type() -> None:
    (record,) = _records(_ETC_OPTION)
    classes = record["possible_class_types"]
    playable = set(class_types_in_mask(PLAYABLE_CLASSES_MASK))
    unused = set(range(PLAYABLE_CLASSES_MASK.bit_length())) - playable
    assert classes and len(classes) == len(set(classes))
    assert not set(classes) & unused


def test_title_keys_are_unique() -> None:
    keys = [record["title_key"] for record in _records(_TITLES)]
    assert keys and len(keys) == len(set(keys))


def test_every_title_has_a_name_description_and_condition() -> None:
    for record in _records(_TITLES):
        assert record["name_kr"] and record["description_kr"] and record["condition_kr"], record


def test_the_kill_count_is_the_count_in_the_condition() -> None:
    for record in _records(_TITLES):
        match = _CONDITION_COUNT.search(record["condition_kr"])
        assert match is not None, record
        assert int(match.group(1)) == record["kill_count"], record


def test_every_grade_key_is_a_ranking_window_grade() -> None:
    keys = [record["grade_key"] for record in _records(_GRADES)]
    assert keys and len(keys) == len(set(keys))
    assert set(keys) <= set(range(_GRADE_COUNT))


def test_the_top_grades_hold_one_rank_each() -> None:
    by_key = {record["grade_key"]: record for record in _records(_GRADES)}
    for rank in range(1, _TOP_RANKER_COUNT + 1):
        assert by_key[rank]["rank"] == rank


def test_the_percent_grades_widen_with_the_key() -> None:
    percents = [record["percent"] for record in sorted(_records(_GRADES), key=lambda r: r["grade_key"]) if record["percent"]]
    assert percents == sorted(percents)


def test_every_grade_row_holds_the_head_values() -> None:
    data = load_binary_fixture(_GRADES)
    (threshold,) = _U32.unpack_from(data, 4)
    assert all(record["rank_threshold"] == threshold for record in _records(_GRADES))


def test_a_grade_outside_the_window_has_no_name() -> None:
    assert grade_name(_GRADE_COUNT) == ""


def test_head_fields_need_a_counted_table() -> None:
    with pytest.raises(ValueError, match="head fields"):
        ValueTable("test.bss", (ValueField("a", "B"),), head=(ValueField("b", "I"),))


def test_head_columns_follow_the_row_columns() -> None:
    value_table = ValueTable(
        "test.bss",
        (ValueField("grade_key", "H", "gradeKey"),),
        RowCount.COUNTED,
        head=(ValueField("rank_threshold", "I", "rankThreshold"),),
    )
    data = b"PABR" + _U32.pack(100) + _U32.pack(1) + struct.pack("<H", 4) + _U32.pack(0) + _U32.pack(14) + _U32.pack(0)
    (record,) = parse_value_table(data, value_table)
    assert record == {"grade_key": 4, "rank_threshold": 100}
    handler = PabrValuesBssHandler(value_table)
    handler.lang = "en"
    html = handler.render_records_page([record], 0, 1)
    assert html.index("Grade Key") < html.index("Ranked Players")


def test_a_byte_run_display_draws_its_cell() -> None:
    value_table = _TABLES[_CHANNEL_INFO]
    handler = PabrValuesBssHandler(value_table)
    handler.lang = "en"
    record = {"map_color": "ff 14 64", "unknown_03": 0, "unknown_04": "ff 14 64", "unknown_07": 0, "unknown_08": 3}
    assert '<td class="num">6414ff</td>' in handler.render_records_page([record], 0, 1)
