from __future__ import annotations

import struct
from collections import defaultdict
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

from _common.rate import RATE_PER_PERCENT
from .handler import PalaceManagementBssHandler
from .parser import MANUFACTURE, PRODUCTION, parse_palace_records


_U32 = struct.Struct("<I")
_BOARD_GROUPS_AT = 4
# u16 key, three u32 string indexes, u8 type, u16 NPC, u16 dialog index, then the u32 board count.
_GROUP_HEAD_SIZE = 19
_BOARD_REF_SIZE = 3
# u16 key, u32 name index, then the u32 item count.
_BOARD_HEAD_SIZE = 6
_PRODUCTION_ITEM_SIZE = 10
_MANUFACTURE_ITEM_SIZE = 6
_FULL_CHANCE = 100 * RATE_PER_PERCENT
# Board group 1 and its NPC (palacemanagementstaticstatus_bss.md, Board Groups).
_YEONGMAN = 62114


def _skip_groups(data: bytes) -> int:
    (count,) = _U32.unpack_from(data, _BOARD_GROUPS_AT)
    offset = _BOARD_GROUPS_AT + _U32.size
    for _ in range(count):
        (board_count,) = _U32.unpack_from(data, offset + _GROUP_HEAD_SIZE)
        offset += _GROUP_HEAD_SIZE + _U32.size + board_count * _BOARD_REF_SIZE
    return offset


def _board_items(data: bytes, offset: int, item_size: int) -> tuple[int, int]:
    """The item count of every board of one list, and the offset after the list."""
    (count,) = _U32.unpack_from(data, offset)
    offset += _U32.size
    total = 0
    for _ in range(count):
        (item_count,) = _U32.unpack_from(data, offset + _BOARD_HEAD_SIZE)
        offset += _BOARD_HEAD_SIZE + _U32.size + item_count * item_size
        total += item_count
    return total, offset


def _declared_items(source: CaseInput) -> int:
    """The items of every production and processing board; each group lists each board once."""
    production, offset = _board_items(source.data, _skip_groups(source.data), _PRODUCTION_ITEM_SIZE)
    manufacture, _ = _board_items(source.data, offset, _MANUFACTURE_ITEM_SIZE)
    return production + manufacture


CASE = HandlerCase(
    handler_name="palacemanagementstaticstatus.bss",
    data_file="palacemanagementstaticstatus.bss",
    companion_files={},
    loc_file="languagedata_en.loc",
    uses_loc=True,
    loc_fields=["npc_name"],
    internal_path="gamecommondata/binary/palacemanagementstaticstatus.bss",
    tests=[
        SchemaTest(
            required_keys=[
                "board_group_key",
                "board_group_name_kr",
                "texture",
                "board_group_type",
                "npc_character_key",
                "npc_name",
                "board_key",
                "board_name_kr",
                "item_index",
                "probability",
                "exchange_key",
                "nations",
            ],
        ),
        DeclaredCountTest(declared=_declared_items),
        RangeTest(col="board_group_type", min_val=PRODUCTION, max_val=MANUFACTURE),
        RangeTest(col="probability", min_val=0, max_val=_FULL_CHANCE),
        TargetTest(
            col="board_group_key",
            value=1,
            expected={"board_group_type": PRODUCTION, "npc_character_key": _YEONGMAN, "npc_name": "Yeongman"},
        ),
    ],
)


@pytest.fixture(scope="module")
def palace_result(request: Any) -> HandlerResult:
    result = getattr(request.module, "_HANDLER_RESULT", None)
    if result is None:
        result = run_case(replace(CASE, tests=[]))
        request.module._HANDLER_RESULT = result
    return result


@pytest.mark.parametrize("spec", CASE.tests, ids=case_id)
def test_palacemanagementstaticstatus_bss(spec: Any, palace_result: HandlerResult) -> None:
    palace_result.check(spec)


def test_each_production_board_sums_to_a_whole_chance(palace_result: HandlerResult) -> None:
    sums: dict[tuple[int, int], int] = defaultdict(int)
    for record in palace_result.records:
        if record["board_group_type"] == PRODUCTION:
            sums[(record["board_group_key"], record["board_key"])] += record["probability"]
    assert sums and set(sums.values()) == {_FULL_CHANCE}


def test_only_production_items_have_a_chance(palace_result: HandlerResult) -> None:
    for record in palace_result.records:
        assert (record["probability"] is None) == (record["board_group_type"] == MANUFACTURE), record


def test_every_group_has_a_name_and_a_texture(palace_result: HandlerResult) -> None:
    for record in palace_result.records:
        assert record["board_group_name_kr"] and record["texture"], record


def _pabr(values: bytes, strings: list[str]) -> bytes:
    table = _U32.pack(len(strings))
    for text in strings:
        raw = text.encode("utf-16-le")
        table += struct.pack("<BI", 1, len(raw)) + raw
    table_start = _BOARD_GROUPS_AT + len(values)
    return b"PABR" + values + table + _U32.pack(table_start) + _U32.pack(0)


def _group(board_key: int, group_type: int = PRODUCTION) -> bytes:
    head = struct.pack("<HIIIBHHI", 1, 0, 1, 2, group_type, _YEONGMAN, 1, 1)
    return _U32.pack(1) + head + struct.pack("<HB", board_key, 1)


_SETTINGS = struct.pack("<6H", 0, 1, 1, 10, 1420, 1419)
_NATIONS = _U32.pack(1) + struct.pack("<IH", 4, 50)
_STRINGS = ["경회루", "Combine_Etc_PalaceManagement_NodePopUpImg_22", "", "자시문", "NA"]


def test_a_group_reads_its_board_items_and_the_tail() -> None:
    production = _U32.pack(1) + struct.pack("<HII", 1, 3, 1) + struct.pack("<HII", 0, _FULL_CHANCE, 44894)
    manufacture = _U32.pack(0)
    data = _pabr(_group(1) + production + manufacture + _SETTINGS + _NATIONS, _STRINGS)
    (record,) = parse_palace_records(data)
    assert record["board_group_name_kr"] == "경회루"
    assert record["board_name_kr"] == "자시문"
    assert (record["board_key"], record["unknown_02"], record["probability"], record["exchange_key"]) == (1, 1, _FULL_CHANCE, 44894)
    assert record["unknown_manufacture_boards_08"] == 1420
    assert record["nations"] == [["NA", 50]]


def test_a_group_that_lists_a_missing_board_raises() -> None:
    data = _pabr(_group(7) + _U32.pack(0) + _U32.pack(0) + _SETTINGS + _NATIONS, _STRINGS)
    with pytest.raises(ValueError, match="lists missing board 7"):
        parse_palace_records(data)


def test_the_cells_show_the_type_and_the_chance() -> None:
    handler = PalaceManagementBssHandler()
    handler.lang = "en"
    production = _U32.pack(1) + struct.pack("<HII", 1, 3, 1) + struct.pack("<HII", 0, 170_000, 44894)
    data = _pabr(_group(1) + production + _U32.pack(0) + _SETTINGS + _NATIONS, _STRINGS)
    records = [{**record, "npc_name": "Yeongman"} for record in parse_palace_records(data)]
    html = handler.render_records_page(records, 0, 1)
    assert "Production" in html and "17%" in html
