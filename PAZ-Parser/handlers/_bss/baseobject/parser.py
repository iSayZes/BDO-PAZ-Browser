"""`baseobject.bss`: the numeric part of each placeable object, by character ID.

    PABR | u32 row_count | row_count x Row | String Table (empty)
    | u32 string_table_start | u32 0
    Row: u16 character_id | u8 armor_material | u8 object_kind | u8 installation_type
    | f32[4][4] unknown_05 | f32[4][4] unknown_45 | i32 unknown_85
    | u8 is_collision | u8 is_siege_tent | u8 unknown_8b
    | u32 layer_count | u32 unknown_90 | layer_count x Hull Layer
    | u16 unknown_layers_00 | u8 x6 place flags
    Hull Layer: u32 hull_count | hull_count x (u32 face_count | face_count x 140-byte face)

The faces (3.9 MB of the 4.7 MB on client 3483) are skipped by their counts;
a record keeps the hull and face totals. Layout 2 in
docs/file-formats/baseobject_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start


FILE_NAME = "baseobject.bss"
KEY_FIELD = "character_id"
PLACE_FLAG_FIELDS = (
    "is_inside",
    "is_outside",
    "is_floor",
    "is_wall",
    "is_on_the_table",
    "is_carpet",
)

_COUNT_OFFSET = 4
_FACE_SIZE = 140
_MATRIX_SIZE = 16
_MATRIX_ROWS = 4
_HEAD = struct.Struct("<HBBB16f16fiBBBII")
_TAIL = struct.Struct("<H6B")
_U32 = struct.Struct("<I")


def _matrix(values: tuple[float, ...]) -> list[list[float]]:
    """Sixteen floats as four rows of four."""
    return [list(values[row * _MATRIX_ROWS : (row + 1) * _MATRIX_ROWS]) for row in range(_MATRIX_ROWS)]


class _Cursor:
    """Reads one row after another and fails before it reads past `end`."""

    def __init__(self, data: bytes, pos: int, end: int) -> None:
        self.data, self.pos, self.end = data, pos, end

    def take(self, fmt: struct.Struct, label: str) -> tuple:
        self.skip(fmt.size, label)
        return fmt.unpack_from(self.data, self.pos - fmt.size)

    def skip(self, size: int, label: str) -> None:
        if self.pos + size > self.end:
            raise ValueError(f"{label} runs past the rows at 0x{self.pos:X}")
        self.pos += size


def _skip_layers(cursor: _Cursor, layer_count: int, label: str) -> tuple[int, int]:
    """Walk the hull layers; returns (hull total, face total)."""
    hulls = faces = 0
    for _ in range(layer_count):
        (hull_count,) = cursor.take(_U32, label)
        hulls += hull_count
        for _ in range(hull_count):
            (face_count,) = cursor.take(_U32, label)
            cursor.skip(face_count * _FACE_SIZE, label)
            faces += face_count
    return hulls, faces


def _read_row(cursor: _Cursor, index: int) -> dict:
    label = f"{FILE_NAME} row {index}"
    head = cursor.take(_HEAD, label)
    character_id, armor_material, object_kind, installation_type = head[:4]
    matrices = head[4 : 4 + 2 * _MATRIX_SIZE]
    unknown_85, is_collision, is_siege_tent, unknown_8b, layer_count, unknown_90 = head[4 + 2 * _MATRIX_SIZE :]
    hull_count, face_count = _skip_layers(cursor, layer_count, label)
    unknown_layers_00, *place_flags = cursor.take(_TAIL, label)
    return {
        KEY_FIELD: character_id,
        "armor_material": armor_material,
        "object_kind": object_kind,
        "installation_type": installation_type,
        "unknown_05": _matrix(matrices[:_MATRIX_SIZE]),
        "unknown_45": _matrix(matrices[_MATRIX_SIZE:]),
        "unknown_85": unknown_85,
        "is_collision": is_collision,
        "is_siege_tent": is_siege_tent,
        "unknown_8b": unknown_8b,
        "layer_count": layer_count,
        "unknown_90": unknown_90,
        "hull_count": hull_count,
        "face_count": face_count,
        "unknown_layers_00": unknown_layers_00,
        **dict(zip(PLACE_FLAG_FIELDS, place_flags, strict=True)),
    }


def parse_baseobject_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic or trailer, a row that runs past the
    string table, or rows that end before it.
    """
    end = checked_string_table_start(data, FILE_NAME)
    (row_count,) = _U32.unpack_from(data, _COUNT_OFFSET)
    cursor = _Cursor(data, HEADER_SIZE, end)
    records = [_read_row(cursor, index) for index in range(row_count)]
    check_rows_end(data, cursor.pos, f"{FILE_NAME} rows")
    return records
