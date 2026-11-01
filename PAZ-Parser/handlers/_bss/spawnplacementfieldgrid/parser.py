"""`mapdata_*/spawnplacementfieldgrid/<field_no>/7/`: the NPC and monster spawns by field grid square.

    x_y.bss            PABR | squares up to table_start | string table | u32 table_start | u32 0
                       square: u16 grid_x | u16 grid_z | u32 spawn_count | spawn_count x spawn
    fieldgridinfo.bss  PABR | (u16 grid_x | u16 grid_z) up to table_start | string table | trailer
    fileinfo.bss       PABR | (u16 cell_x | u16 cell_z) up to table_start | string table | trailer

The string table is empty in every file of client 3482. A spawn is a
variable-size record: a character key only when `has_character` is 1, then
counted waypoint, index position and spawn condition lists. Layouts in
docs/file-formats/bss/x_y_bss.md, fieldgridinfo_bss.md and fileinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PABR_MAGIC
from _common.pabr_strings import TRAILER_SIZE, U32_SIZE, read_string_table, string_table_start
from _common.record_reader import RecordReader

# The registry key every `<x>_<y>.bss` cell reads under: `bdo_preview.GRID_CELL_KEY`,
# written out so a handler pack still imports on an exe older than that name.
CELL_FILE_KEY = "x_y.bss"
FIELDGRIDINFO_FILE = "fieldgridinfo.bss"
FILEINFO_FILE = "fileinfo.bss"
# The folder that holds the grid of each field, under `mapdata_*/`.
GRID_FOLDER = "spawnplacementfieldgrid"
# World units per field grid square side; `instancefield.dbss` multiplies
# `field_grid_sector_count` by the same number.
GRID_SQUARE_SIZE = 3700

_MAGIC_SIZE = 4
_PAIR = struct.Struct("<HH")
_SQUARE_HEAD = struct.Struct("<HHI")
_U8 = struct.Struct("<B")
_U16 = struct.Struct("<H")

# (record key, struct code) runs of the spawn record, split where a variable part follows.
_KEY_TO_CHARACTER_FLAG = (
    ("is_spawnable", "B"),
    ("key_index", "H"),
    ("key_sector_z", "h"),
    ("key_sector_x", "h"),
    ("key_type", "B"),
    ("unknown_08", "B"),
    ("position_x", "f"),
    ("position_y", "f"),
    ("position_z", "f"),
    ("spawn_range", "H"),
    ("direction", "f"),
    ("unknown_1b", "H"),
    ("has_character", "B"),
)
_SCENE_TO_HOUSE = (
    ("scene_sector_x", "i"),
    ("scene_sector_y", "i"),
    ("scene_sector_z", "i"),
    ("scene_type", "H"),
    ("scene_index", "H"),
    ("unknown_character_key_10", "I"),
    ("unknown_character_key_14", "I"),
    ("unknown_character_key_18", "I"),
    ("unknown_character_key_1c", "B"),
    ("spawn_delay_time", "I"),
    ("spawn_delay_variable_time", "I"),
    ("unknown_character_key_25", "B"),
    ("unknown_character_key_26", "3s"),
    ("respawn_number", "I"),
    ("unknown_character_key_2d", "B"),
    ("event_object_key", "I"),
    ("unknown_character_key_32", "I"),
    ("live_world_event_key", "I"),
    ("territory", "h"),
    ("action_index", "I"),
    ("dialog_index", "H"),
    ("dialog_update_time", "I"),
    ("unknown_character_key_46", "4s"),
    ("team_no", "i"),
    ("unknown_character_key_4e", "i"),
    ("house_x", "f"),
    ("house_y", "f"),
    ("house_z", "f"),
    ("waypoint_count", "I"),
)
_WAYPOINTS_TAIL = (
    ("go_home_type", "B"),
    ("unknown_waypoints_01", "B"),
    ("index_position_count", "I"),
)
_WAYPOINT = (("using_type", "B"), ("waypoint_key", "i"))
_INDEX_POSITION = (
    ("unknown_00", "H"),
    ("x", "f"),
    ("y", "f"),
    ("z", "f"),
    ("direction", "f"),
)
_CONDITION = (
    ("unknown_00", "B"),
    ("spawn_start_hour", "h"),
    ("spawn_end_hour", "h"),
)


def _run(fields: tuple[tuple[str, str], ...]) -> tuple[struct.Struct, tuple[str, ...]]:
    return struct.Struct("<" + "".join(code for _, code in fields)), tuple(key for key, _ in fields)


_HEAD_RUN = _run(_KEY_TO_CHARACTER_FLAG)
_BODY_RUN = _run(_SCENE_TO_HOUSE)
_TAIL_RUN = _run(_WAYPOINTS_TAIL)
_WAYPOINT_RUN = _run(_WAYPOINT)
_INDEX_POSITION_RUN = _run(_INDEX_POSITION)
_CONDITION_RUN = _run(_CONDITION)


def _read(reader: RecordReader, run: tuple[struct.Struct, tuple[str, ...]]) -> dict:
    layout, keys = run
    values = (value.hex() if isinstance(value, bytes) else value for value in reader.unpack(layout))
    return dict(zip(keys, values))


def _read_list(reader: RecordReader, count: int, run: tuple[struct.Struct, tuple[str, ...]]) -> list[dict]:
    return [_read(reader, run) for _ in range(count)]


def _read_spawn(reader: RecordReader) -> dict:
    spawn = _read(reader, _HEAD_RUN)
    spawn["character_key"] = reader.unpack(_U16)[0] if spawn["has_character"] == 1 else None
    spawn.update(_read(reader, _BODY_RUN))
    spawn["waypoints"] = _read_list(reader, spawn["waypoint_count"], _WAYPOINT_RUN)
    spawn.update(_read(reader, _TAIL_RUN))
    spawn["index_positions"] = _read_list(reader, spawn["index_position_count"], _INDEX_POSITION_RUN)
    (spawn["condition_count"],) = reader.unpack(_U8)
    spawn["conditions"] = _read_list(reader, spawn["condition_count"], _CONDITION_RUN)
    return spawn


def _rows_end(data: bytes, file_name: str) -> int:
    """Where the rows stop, from the trailer; the files have no row count after the magic.

    Raises ValueError on a bad magic, a trailer outside the file, or a string
    table with text in it: no field of these files reads one.
    """
    if len(data) < _MAGIC_SIZE + U32_SIZE + TRAILER_SIZE or data[:_MAGIC_SIZE] != PABR_MAGIC:
        raise ValueError(f"{file_name} has invalid magic.")
    end = string_table_start(data)
    if not _MAGIC_SIZE <= end <= len(data) - TRAILER_SIZE - U32_SIZE:
        raise ValueError(f"{file_name} string table offset 0x{end:X} is outside the file")
    if read_string_table(data):
        raise ValueError(f"{file_name} has strings in its string table; the layout has changed")
    return end


def parse_cell_spawns(data: bytes, file_name: str) -> list[dict]:
    """Every spawn of a cell file in file order, with the grid square it is listed under.

    Raises ValueError on a bad magic or trailer, a spawn that runs past the
    string table, or a non-empty string table.
    """
    rows_end = _rows_end(data, file_name)
    spawns: list[dict] = []
    pos = _MAGIC_SIZE
    while pos < rows_end:
        reader = RecordReader(data, pos, rows_end, f"{file_name} square at 0x{pos:X}")
        grid_x, grid_z, spawn_count = reader.unpack(_SQUARE_HEAD)
        for _ in range(spawn_count):
            spawn = _read_spawn(reader)
            spawns.append({"grid_x": grid_x, "grid_z": grid_z, **spawn})
        pos = reader.pos
    return spawns


def parse_grid_pairs(data: bytes, file_name: str) -> list[tuple[int, int]]:
    """The (x, z) pairs of `fieldgridinfo.bss` or `fileinfo.bss`, in file order.

    Raises ValueError on a bad magic or trailer, pairs that do not fill the
    space before the string table, or a non-empty string table.
    """
    rows_end = _rows_end(data, file_name)
    rows_size = rows_end - _MAGIC_SIZE
    if rows_size % _PAIR.size:
        raise ValueError(f"{file_name} pairs take {rows_size} bytes, not a multiple of {_PAIR.size}")
    return [_PAIR.unpack_from(data, pos) for pos in range(_MAGIC_SIZE, rows_end, _PAIR.size)]


def grid_field_no(internal_path: str) -> int | None:
    """The `fieldinfo.bss` field number of a grid file, from its `<field_no>/<n>/` folder; None when the path has none."""
    parts = internal_path.replace("\\", "/").lower().split("/")
    if GRID_FOLDER not in parts:
        return None
    folder = parts[parts.index(GRID_FOLDER) + 1 :]
    return int(folder[0]) if len(folder) >= 2 and folder[0].isdigit() else None
