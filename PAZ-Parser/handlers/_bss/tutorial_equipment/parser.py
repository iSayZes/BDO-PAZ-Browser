"""`sequencetutorial_equipment.bss` and `cutscenetutorial_equipment.bss`: the
costume items each class wears in a tutorial sequence or cutscene.

    PABR | u32 row_count | row_count x row | String Table
    | u32 string_table_start | u32 0
    row: u32 file_name_hash | u32 cutscene_file_name | u32 class_count
         | class_count x 25-byte class
    class: u8 class_type | u32 item IDs of the main weapon, sub-weapon,
           helmet, armor, gloves and shoes (0 for none)

Layout 1 in docs/file-formats/tutorial_equipment_bss.md; the row head is
read by `_bss/sequence_scripts/reader.py`.
"""

from __future__ import annotations

import struct

from _bss.sequence_scripts.reader import check_rows_end, open_table, read_class_entries, read_string_refs
from _common.record_reader import RecordReader


SEQUENCE_FILE_NAME = "sequencetutorial_equipment.bss"
CUTSCENE_FILE_NAME = "cutscenetutorial_equipment.bss"
# The six item fields of a class entry, in file order.
SLOT_FIELDS = (
    "main_weapon_item_id",
    "sub_weapon_item_id",
    "helmet_item_id",
    "armor_item_id",
    "gloves_item_id",
    "shoes_item_id",
)

_HASH = struct.Struct("<I")
_CLASS = struct.Struct(f"<B{len(SLOT_FIELDS)}I")


def _read_class(reader: RecordReader) -> dict:
    class_type, *item_ids = reader.unpack(_CLASS)
    return {"class_type": class_type, **dict(zip(SLOT_FIELDS, item_ids))}


def parse_tutorial_equipment_rows(data: bytes, file_name: str) -> list[dict]:
    """Every row in file order: its file name and hash and its class entries.

    Raises ValueError on a bad magic, a string index past the table, or rows
    that do not end where the string table starts.
    """
    table = open_table(data, file_name)
    rows: list[dict] = []
    for index in range(table.row_count):
        (file_name_hash,) = table.reader.unpack(_HASH)
        texts = read_string_refs(table, ("cutscene_file_name",), f"{file_name} row {index}")
        rows.append({
            "file_name_hash": file_name_hash,
            **texts,
            "classes": read_class_entries(table.reader, _read_class),
        })
    check_rows_end(table, file_name)
    return rows


def file_names_by_hash(data: bytes, file_name: str) -> dict[int, str]:
    """Each row's file name by its hash, for `cutscene_skill.bss`, which stores the hash alone."""
    return {row["file_name_hash"]: row["cutscene_file_name"] for row in parse_tutorial_equipment_rows(data, file_name)}
