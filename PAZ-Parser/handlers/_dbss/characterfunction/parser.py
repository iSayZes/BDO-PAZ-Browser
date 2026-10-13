"""`characterfunction.dbss` records, located through `characterfunctionoffset.dbss`.

The data file opens with a u32 record count. Each offset row points just past a
u16 inline copy of the character ID; the record there is the head, the
function slots of `layout.py` and the tail, read in order:

    u8[4] head | 37 x (name, condition, slot fields) | u8, u8, u32, u8 tail

Every record must end exactly at its row's size, so a changed layout fails
loudly. Full layout in docs/file-formats/characterfunction_dbss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType

from _common.binary import u16
from _common.pabr_offset import PabrOffsetRow
from _common.record_reader import RecordReader
from .layout import HEAD_FIELDS, ITEM_GROUP_FIELDS, SLOTS, TAIL_FIELDS, FieldSpec, SlotSpec

FieldValue = int | tuple[int, ...]

_INLINE_ID_SIZE = 2
_U8 = struct.Struct("<B")
_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
_FIXED = {"u8": _U8, "u16": _U16, "u32": _U32}


@dataclass(frozen=True)
class FunctionSlot:
    key: str
    loc_index: int | None
    name: str
    condition: str
    fields: Mapping[str, FieldValue]


@dataclass(frozen=True)
class CharacterFunctionRecord:
    character_id: int
    head: Mapping[str, FieldValue]
    slots: tuple[FunctionSlot, ...]
    tail: Mapping[str, FieldValue]

    def slot(self, key: str) -> FunctionSlot:
        return next(slot for slot in self.slots if slot.key == key)

    @property
    def managed_node_keys(self) -> tuple[int, ...]:
        """Nodes this character manages (`exploration.bss` manager)."""
        return self._node_keys("managed_node_keys")

    @property
    def town_node_keys(self) -> tuple[int, ...]:
        """Town nodes this character represents (`exploration.bss` representative)."""
        return self._node_keys("town_node_keys")

    @property
    def vehicle_types(self) -> tuple[int, ...]:
        """`CppEnums.VehicleType` values the stable takes, as stored; one can repeat."""
        return self._list_field("stable", "vehicle_types")

    @property
    def item_groups(self) -> dict[str, int]:
        """`itemmaingroup.bss` group IDs by field name, 0 for none, in slot order."""
        return {field: self._int_field(slot, field) for slot, field in ITEM_GROUP_FIELDS}

    def _node_keys(self, field: str) -> tuple[int, ...]:
        return self._list_field("node_management", field)

    def _list_field(self, slot: str, field: str) -> tuple[int, ...]:
        values = self.slot(slot).fields[field]
        return values if isinstance(values, tuple) else ()

    def _int_field(self, slot: str, field: str) -> int:
        value = self.slot(slot).fields[field]
        return value if isinstance(value, int) else 0


def parse_characterfunction_records(
    data: bytes,
    rows: list[PabrOffsetRow],
) -> list[CharacterFunctionRecord]:
    """Parse every record, in offset-table order.

    Raises ValueError when a row's inline ID differs from its key or a record
    does not end exactly at its size.
    """
    return [_parse_record(data, row) for row in rows]


def _parse_record(data: bytes, row: PabrOffsetRow) -> CharacterFunctionRecord:
    label = f"character {row.entry_id}"
    if row.offset < _INLINE_ID_SIZE or row.offset > len(data):
        raise ValueError(f"{label} starts outside characterfunction.dbss")
    inline_id = u16(data, row.offset - _INLINE_ID_SIZE)
    if inline_id != row.entry_id:
        raise ValueError(f"record at 0x{row.offset:X} holds character {inline_id}, not {row.entry_id}")

    reader = RecordReader(data, row.offset, row.offset + row.size, label)
    head = _read_fields(reader, HEAD_FIELDS)
    slots = tuple(_read_slot(reader, spec) for spec in SLOTS)
    tail = _read_fields(reader, TAIL_FIELDS)
    if not reader.at_end():
        raise ValueError(f"{label} has {reader.remaining()} unread bytes")
    return CharacterFunctionRecord(row.entry_id, head, slots, tail)


def _read_slot(reader: RecordReader, spec: SlotSpec) -> FunctionSlot:
    first = reader.text(wide=True)
    second = reader.text(wide=True)
    name, condition = (second, first) if spec.condition_first else (first, second)
    return FunctionSlot(spec.key, spec.loc_index, name, condition, _read_fields(reader, spec.fields))


def _read_fields(reader: RecordReader, specs: tuple[FieldSpec, ...]) -> Mapping[str, FieldValue]:
    """Read `specs` in order; "skip" spans are passed over and left out of the result."""
    values: dict[str, FieldValue] = {}
    for spec in specs:
        if spec.kind == "skip":
            reader.skip(spec.size)
        else:
            values[spec.name] = _read_field(reader, spec)
    return MappingProxyType(values)


def _read_field(reader: RecordReader, spec: FieldSpec) -> FieldValue:
    if spec.kind in _FIXED:
        return reader.unpack(_FIXED[spec.kind])[0]
    item = _U8 if spec.kind == "u8[]" else _U32
    (count,) = reader.unpack(_U32)
    if count * item.size > reader.remaining():
        raise ValueError(f"{spec.name} holds {count:,} items, more than the record has left")
    return tuple(reader.unpack(item)[0] for _ in range(count))
