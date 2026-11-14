"""Walk the head of an action chart, from `uses_shared_tables` to the condition records.

Each function reads one structure of docs/file-formats/other/actionchart_paac.md
and keeps nothing but the counts the handler shows; the handler lists actions.
"""

from __future__ import annotations

from dataclasses import dataclass

from .events import skip_condition_set, skip_effect_data
from .layouts import ChartLayout
from .reader import ChartReader

_SKELETON_ROW_SIZE = 54
_ATTACHMENT_SIZE = 56
_KEYED_DATA_SIZE = 22
_UNKNOWN_ROW_SIZE = 20
_SLOT_HEAD_SIZE = 32 + 4
_SLOT_ARRAYS = 2
_NO_KEY = -1


@dataclass(frozen=True)
class ChartHead:
    uses_shared_tables: int
    animation_count: int
    effect_count: int
    condition_count: int


def _skip_animation(reader: ChartReader, layout: ChartLayout) -> None:
    # name_hash, the group string (Layout 2), name_ref, clip_ref
    reader.raw(12 + (4 if layout.group_strings else 0))
    if reader.u16():
        reader.raw(24)
    if reader.u8():
        reader.raw(4 * reader.count())
    if reader.u8():
        reader.raw(8 * reader.count())
    reader.raw(layout.animation_event_size * reader.short_count())


def _skip_list_block(reader: ChartReader) -> None:
    reader.raw(8 * reader.short_count())
    reader.raw(8 * reader.short_count())
    for _ in range(reader.short_count()):
        reader.raw(4)
        reader.raw(12 * reader.short_count())
        reader.raw(8 * reader.short_count())


def _skip_skeleton(reader: ChartReader, layout: ChartLayout) -> None:
    reader.raw(4 + (4 if layout.group_strings else 0) + 8)
    reader.raw(_SKELETON_ROW_SIZE * reader.count())
    reader.block()


def _skip_mesh_group(reader: ChartReader, layout: ChartLayout) -> None:
    reader.raw(4 + (4 if layout.group_strings else 0))
    for _ in range(reader.count()):
        reader.raw(8)
        reader.block()
    reader.block()


def _skip_keyed_entry(reader: ChartReader) -> None:
    if reader.i32() != _NO_KEY:
        reader.raw(_KEYED_DATA_SIZE)


def _skip_hit_parts(reader: ChartReader, layout: ChartLayout) -> None:
    for _ in range(reader.count()):
        reader.raw(8)
        reader.raw(layout.hit_part_size * reader.count())
    reader.raw(4 * reader.count())


def skip_condition_record(reader: ChartReader) -> None:
    if reader.u8():
        for _ in range(2):
            if reader.u32():
                reader.raw(reader.count())
    for _ in range(reader.u8()):
        skip_condition_set(reader)
    reader.raw(8)
    if reader.u8():
        reader.raw(12)
    reader.block()


def read_head(reader: ChartReader, layout: ChartLayout) -> ChartHead:
    """Read from `uses_shared_tables` through the condition records."""
    uses_shared_tables = reader.u8()
    animation_count = reader.count()
    for _ in range(animation_count):
        _skip_animation(reader, layout)
    _skip_list_block(reader)
    for _ in range(reader.count()):
        _skip_skeleton(reader, layout)
    reader.raw(12 * reader.count())
    for _ in range(reader.count()):
        _skip_mesh_group(reader, layout)
    effect_count = reader.count()
    for _ in range(effect_count):
        reader.raw(4)
        skip_effect_data(reader)
    for _ in range(reader.count()):
        _skip_keyed_entry(reader)
    reader.raw(_UNKNOWN_ROW_SIZE * reader.count())
    reader.raw(8)
    reader.raw(4 * reader.u8())
    reader.raw(4)
    for _ in range(layout.slot_count):
        if reader.u8():
            reader.raw(_SLOT_HEAD_SIZE + _SLOT_ARRAYS * layout.slot_count)
    if reader.u8():
        _skip_hit_parts(reader, layout)
    condition_count = reader.count()
    for _ in range(condition_count):
        skip_condition_record(reader)
    return ChartHead(uses_shared_tables, animation_count, effect_count, condition_count)
