"""Checks of the item tables in `item_tables.py` that the shared cases in test_handler.py do not cover."""

from __future__ import annotations

from tests.fixtures import load_binary_fixture

from _bss.buffitemautousestaticstatus.parser import parse_buffitemautouse_records
from _bss.territoryinfo.parser import parse_territoryinfo_records
from .item_names import auto_use_category_name, item_classify_text, item_type_text, move_filter_loc_key, move_filter_name
from .item_tables import ITEM_TABLES
from .layout import ValueTable
from .parser import PABR_VALUES_START, parse_value_rows, parse_value_table


_TABLES = {value_table.file_name: value_table for value_table in ITEM_TABLES}
_SORT_PRIORITY = _TABLES["itemsortprioritytype.bss"]
_MOVE_DATA = _TABLES["itemmovedata.bss"]
_AUTO_USE_CATEGORY = _TABLES["autousebuffitemcategoryinfo.bss"]
_BOOTY = _TABLES["bootyitemlist.bss"]
_NOTIFY = _TABLES["notifyexpirationperioditem.bss"]
# The 4 bytes after the u8 index of an itemmovedata.bss row: contents event, classify, type.
_MOVE_KEY_AT = 1
_MOVE_KEY_SIZE = 4
_U32_SIZE = 4
# LOC types 101 and 118 have no entry 0, so a zero row falls back to its Korean name.
_UNNAMED_KEY = 0


def _records(value_table: ValueTable) -> list[dict]:
    return parse_value_table(load_binary_fixture(value_table.file_name), value_table)


def test_the_sort_priority_rows_hold_each_value_once() -> None:
    records = _records(_SORT_PRIORITY)
    positions = [record["unknown_00"] for record in records]
    assert positions == list(range(len(records)))
    assert sorted(record["unknown_01"] for record in records) == positions


def test_the_move_filter_loc_key_is_the_four_bytes_after_the_index() -> None:
    for record, row_hex in parse_value_rows(load_binary_fixture(_MOVE_DATA.file_name), _MOVE_DATA):
        stored = int.from_bytes(bytes.fromhex(row_hex)[_MOVE_KEY_AT : _MOVE_KEY_AT + _MOVE_KEY_SIZE], "little")
        assert move_filter_loc_key(record["item_type"], record["item_classify"], record["contents_event_type"]) == stored


def test_the_move_filter_indexes_are_unique() -> None:
    indexes = [record["index"] for record in _records(_MOVE_DATA)]
    assert indexes and len(indexes) == len(set(indexes))


def test_a_name_without_a_loc_entry_falls_back_to_the_korean_name() -> None:
    move_record = {"item_type": 0, "item_classify": 0, "contents_event_type": _UNNAMED_KEY, "exception_filter_name_tag_kr": "요리류 제외"}
    assert move_filter_name(move_record) == "요리류 제외"
    category_record = {"category_key": _UNNAMED_KEY, "category_name_kr": "기타"}
    assert auto_use_category_name(category_record) == "기타"


def test_the_item_enum_cells_name_the_member() -> None:
    assert item_type_text(10) == "10 ContentsEvent"
    assert item_classify_text(8) == "8 Cook"
    assert item_classify_text(99) == "99"


def test_every_auto_use_item_has_its_category() -> None:
    keys = {record["category_key"] for record in _records(_AUTO_USE_CATEGORY)}
    items = parse_buffitemautouse_records(load_binary_fixture("buffitemautousestaticstatus.bss"))
    assert keys and {item["category_key"] for item in items} <= keys


def test_every_booty_list_is_a_territory() -> None:
    territories = {row["territory_key"] for row in parse_territoryinfo_records(load_binary_fixture("territoryinfo.bss"))}
    keys = [record["territory_key"] for record in _records(_BOOTY)]
    assert keys and set(keys) <= territories and len(keys) == len(set(keys))


def test_each_booty_list_holds_its_count() -> None:
    data = load_binary_fixture(_BOOTY.file_name)
    offset = PABR_VALUES_START + _U32_SIZE
    for record in _records(_BOOTY):
        count = int.from_bytes(data[offset + _U32_SIZE : offset + 2 * _U32_SIZE], "little")
        assert len(record["booty_item_ids"]) == count, record
        offset += 3 * _U32_SIZE + count * _U32_SIZE


def test_the_notified_items_are_unique() -> None:
    keys = [record["item_key"] for record in _records(_NOTIFY)]
    assert keys and len(keys) == len(set(keys))

