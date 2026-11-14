"""Packages, actions and elements of an action chart, as record dicts.

Field names are the doc's (docs/file-formats/other/actionchart_paac.md):
Package, Action, Element and Element Record. Blocks are kept as hex text so
the records stay JSON-serializable.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from .events import skip_condition_set
from .layouts import ChartLayout
from .reader import ChartReader

_STRINGS_AFTER_ANIMATION = 11
_ELEMENT_ITEM_SIZE = 17
_ELEMENT_BYTES_38 = 12
_PACKAGE_TAIL = 60
_PACKAGE_NAMES = 10


@dataclass(frozen=True)
class Package:
    package_hash: int
    package_path: str
    actions: list[dict]


def _rows(reader: ChartReader, fmt: str) -> list[list[int]]:
    """A u64 count, then that many rows of `fmt` reads (`H` u16, `I` u32, `i` i32)."""
    readers = {"H": reader.u16, "I": reader.u32, "i": reader.i32}
    return [[readers[kind]() for kind in fmt] for _ in range(reader.count())]


def _values(reader: ChartReader, kind: str) -> list[int]:
    """A u64 count, then that many values of one `struct` kind (`H`, `I` or `i`)."""
    count = reader.count()
    return list(struct.unpack(f"<{count}{kind}", reader.raw(struct.calcsize(kind) * count)))


def _element_record(reader: ChartReader) -> dict:
    record: dict = {"unknown_str_ref_00": reader.string(), "unknown_str_ref_04": reader.string()}
    skip_condition_set(reader)
    record["unknown_set_00"] = reader.u32()
    record["values"] = list(reader.raw(reader.u8()))
    return record


def read_element(reader: ChartReader, layout: ChartLayout) -> dict:
    element: dict = {
        "action_name": reader.string(),
        "animation": reader.string(),
        "unknown_str_refs_08": [reader.string() for _ in range(_STRINGS_AFTER_ANIMATION)],
    }
    if layout.loader_element:
        element["unknown_34"] = reader.u32()
        element["unknown_str_refs_38"] = [reader.string(), reader.string()]
        element["records"] = [_element_record(reader) for _ in range(reader.count())]
    else:
        element["unknown_34"] = reader.string()
        element["unknown_38"] = reader.raw(_ELEMENT_BYTES_38).hex()
        element["unknown_items"] = [reader.raw(_ELEMENT_ITEM_SIZE).hex() for _ in range(reader.short_count())]
        element["unknown_items_00"] = reader.u32()
        element["unknown_items_04"] = reader.u64()
        element["unknown_items_0c"] = reader.u8()
    element["unknown_parameters"] = reader.block().hex()
    return element


def _read_action(reader: ChartReader) -> dict:
    action: dict = {"action_hash": reader.u32()}
    action["unknown_first_values"] = _values(reader, "i")
    action["unknown_second_values"] = _values(reader, "I")
    action["unknown_third_values"] = _values(reader, "H")
    action["unknown_fourth_rows"] = _rows(reader, "HHI")
    action["unknown_fifth_rows"] = _rows(reader, "HH")
    action["unknown_sixth_rows"] = _rows(reader, "iHHIIHHH")
    action["unknown_sixth_rows_00"] = reader.u32()
    action["unknown_sixth_rows_04"] = reader.u32()
    action["unknown_first_data"] = reader.block().hex()
    action["unknown_first_data_00"] = reader.u16()
    action["unknown_second_data"] = reader.block().hex()
    return action


def _skip_package_tables(reader: ChartReader) -> None:
    for _ in range(reader.count()):
        reader.raw(4)
        reader.raw(16 * reader.count())
    reader.raw(8 * reader.count())
    for _ in range(reader.count()):
        reader.raw(4 * reader.count())
        reader.raw(10 * reader.count())
        reader.raw(4)


def read_package(reader: ChartReader, layout: ChartLayout) -> Package:
    package_hash = reader.u32()
    flag_a, flag_b = reader.u8(), reader.u8()
    package_path = reader.string()
    reader.raw(4 * _PACKAGE_NAMES)
    reader.raw(2 + layout.package_header_u8_count + 4)
    _skip_package_tables(reader)
    with_element = not (flag_a and flag_b)
    actions = []
    for _ in range(reader.count()):
        action = _read_action(reader)
        if with_element:
            action["element"] = read_element(reader, layout)
        actions.append(action)
    reader.raw(_PACKAGE_TAIL)
    return Package(package_hash, package_path, actions)
