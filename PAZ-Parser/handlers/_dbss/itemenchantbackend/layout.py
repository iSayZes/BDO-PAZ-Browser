"""The walk of one itemenchantbackend.dbss block, front to back (itemenchantbackend_dbss.md, Block).

A block holds six counted lists and three strings, so every field after the
first list moves with the counts before it. `read_block` walks them all and
checks that the walk ends at the packed key and crystal group the block ends
with. The offsets below are the ones in a block whose lists are empty.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.prefixed_string import read_prefixed_at


@dataclass(frozen=True)
class BackendBlock:
    """The named fields of a block; the `unknown_*` ones stay in the bytes."""

    item_access_level: int
    repair_time: int
    maxest_percent_for_item_market: int
    minest_percent_for_item_market: int
    base_price_for_item_market: int
    max_register_count_for_item_market: int
    # (item ID, count) pairs.
    jewel_need_items: tuple[tuple[int, int], ...]
    jewel_equip_type: int
    jewel_color_type: int
    jewel_demolition_rate: int
    collect_tool_type: int
    collect_time: int
    need_contribute: int
    target_type: int
    # (item ID, count) pairs.
    popup_result_items: tuple[tuple[int, int], ...]
    enchant_difficulty: int
    expiration_period_type: int
    expiration_period_param1: int
    expiration_period_param2: int
    # An `eConnectUiType` value (connectui.luac); -1 when the item opens no window.
    connect_ui: int
    market_filter_1: int
    market_filter_2: int
    item_properties: int
    fairy_feed_key: int
    use_condition: str
    acquire_action: str
    description_kr: str
    restore_type: int
    key: int
    crystal_group: int


_U8 = struct.Struct("<B").unpack_from
_U32 = struct.Struct("<I").unpack_from
_U64 = struct.Struct("<Q").unpack_from

# `+0x2F` to `+0x9A`: the access level, price fields and three unknown i64.
_HEAD = struct.Struct("<B6iqqqqqiiqH24x")
_HEAD_AT = 0x2F
_COUNT32 = 4
_COUNT64 = 8
_JEWEL_NEED_ITEM = struct.Struct("<I4xq")
# `jewel_equip_type` to `unknown_be`, after the jewel list.
_MIDDLE = struct.Struct("<BBiBq4xhBBB4x4x")
_POPUP_RESULT_ITEM = struct.Struct("<qI")
_UNKNOWN_C6_SIZE = 8
_LIST_VALUE_SIZE = 4
# `unknown_d6` to `unknown_f8`, after the u32 list at `+0xCE`.
_LATE = struct.Struct("<H7xBBiqiBB4xBx")
# `unknown_101` to `fairy_feed_key`, after the u32 list at `+0xF9`.
_FAIRY_FEED_KEY_AT = 0x0C
_AFTER_LIST_43A = 0x0E
_END_VALUE_SIZE = 2
_AFTER_END_LIST = 0x0A
_TAIL = struct.Struct("<IH")


def _counted(data: bytes, pos: int, count_size: int, entry_size: int, end: int) -> tuple[int, int]:
    """The count at `pos` and where its entries start; raises ValueError when they run past `end`."""
    count = (_U32 if count_size == _COUNT32 else _U64)(data, pos)[0]
    start = pos + count_size
    if start + count * entry_size > end:
        raise ValueError(f"the list at 0x{pos:X} ({count:,} entries) runs past the block end")
    return count, start


def read_block(data: bytes, start: int, end: int) -> BackendBlock:
    """Walk the block `[start, end)`.

    Raises ValueError when a count or string runs past the block, or the walk
    does not end 6 bytes before `end`, where the key and crystal group sit.
    """
    try:
        return _read(data, start, end)
    except struct.error as error:
        raise ValueError(f"block at 0x{start:X}: a field runs past the data") from error


def _read(data: bytes, start: int, end: int) -> BackendBlock:
    (access_level, *_rates, repair_time, _p1, _p2, _p3, _p4, maxest, minest, base_price, max_register) = (
        _HEAD.unpack_from(data, start + _HEAD_AT)
    )
    pos = start + _HEAD_AT + _HEAD.size

    count, pos = _counted(data, pos, _COUNT64, _JEWEL_NEED_ITEM.size, end)
    jewel_need_items = tuple(_JEWEL_NEED_ITEM.iter_unpack(data[pos:pos + count * _JEWEL_NEED_ITEM.size]))
    pos += count * _JEWEL_NEED_ITEM.size

    (jewel_equip, jewel_color, demolition, collect_tool, collect_time, need_contribute,
     _b7, _b8, target_type) = _MIDDLE.unpack_from(data, pos)
    pos += _MIDDLE.size

    count, pos = _counted(data, pos, _COUNT32, _POPUP_RESULT_ITEM.size, end)
    entries = _POPUP_RESULT_ITEM.iter_unpack(data[pos:pos + count * _POPUP_RESULT_ITEM.size])
    popup = tuple((item, amount) for amount, item in entries)
    pos += count * _POPUP_RESULT_ITEM.size + _UNKNOWN_C6_SIZE

    count, pos = _counted(data, pos, _COUNT64, _LIST_VALUE_SIZE, end)
    pos += count * _LIST_VALUE_SIZE

    (_d6, difficulty, period_type, period_param1, period_param2, connect_ui, filter_1, filter_2,
     item_properties) = _LATE.unpack_from(data, pos)
    pos += _LATE.size

    count, pos = _counted(data, pos, _COUNT32, _LIST_VALUE_SIZE, end)
    pos += count * _LIST_VALUE_SIZE
    fairy_feed_key = struct.unpack_from("<H", data, pos + _FAIRY_FEED_KEY_AT)[0]
    pos += _AFTER_LIST_43A

    use_condition, pos = read_prefixed_at(data, pos, end, wide=True)
    acquire_action, pos = read_prefixed_at(data, pos, end, wide=False)
    description_kr, pos = read_prefixed_at(data, pos, end, wide=True)

    count, pos = _counted(data, pos, _COUNT32, _LIST_VALUE_SIZE, end)
    pos += count * _LIST_VALUE_SIZE
    restore_type = _U8(data, pos)[0]
    count, pos = _counted(data, pos + 1, _COUNT32, _END_VALUE_SIZE, end)
    pos += count * _END_VALUE_SIZE + _AFTER_END_LIST

    if pos + _TAIL.size != end:
        raise ValueError(f"block at 0x{start:X}: the walk ends {end - pos - _TAIL.size:+,} bytes from the key")
    key, crystal_group = _TAIL.unpack_from(data, pos)

    return BackendBlock(
        item_access_level=access_level,
        repair_time=repair_time,
        maxest_percent_for_item_market=maxest,
        minest_percent_for_item_market=minest,
        base_price_for_item_market=base_price,
        max_register_count_for_item_market=max_register,
        jewel_need_items=jewel_need_items,
        jewel_equip_type=jewel_equip,
        jewel_color_type=jewel_color,
        jewel_demolition_rate=demolition,
        collect_tool_type=collect_tool,
        collect_time=collect_time,
        need_contribute=need_contribute,
        target_type=target_type,
        popup_result_items=popup,
        enchant_difficulty=difficulty,
        expiration_period_type=period_type,
        expiration_period_param1=period_param1,
        expiration_period_param2=period_param2,
        connect_ui=connect_ui,
        market_filter_1=filter_1,
        market_filter_2=filter_2,
        item_properties=item_properties,
        fairy_feed_key=fairy_feed_key,
        use_condition=use_condition,
        acquire_action=acquire_action,
        description_kr=description_kr,
        restore_type=restore_type,
        key=key,
        crystal_group=crystal_group,
    )
