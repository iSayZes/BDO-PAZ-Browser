"""The documented characterstatic.dbss record layouts, and which one a file has.

The layouts differ only in where the read fields sit: the size of the
Character Fields block and the offsets inside it, and the fixed runs of the
part after `voice_bank`. The parser reads every record with the layout picked
here. The pick tries the layouts in client order (`client_versions.py`) on the
first records and keeps the first that reads all of them; a record fits only
when it repeats its own ID and ends exactly at its index size. Layouts 1 to 3
in docs/file-formats/dbss/characterstatic_dbss.md.
"""

from __future__ import annotations

from dataclasses import dataclass

from _common.client_versions import ClientRange
from _common.vehicle_type import NO_VEHICLE_TYPE, NO_VEHICLE_TYPE_OLD


@dataclass(frozen=True)
class RecordLayout:
    """One documented Payload shape; `number` is its Layout N in the doc."""

    number: int
    # Bytes of the Character Fields block, from the end of condition_script.
    character_fields_size: int
    # Offsets inside Character Fields.
    character_id: int
    character_group: int
    npc_kind: int
    grade: int
    tendency_on_dead: int
    ocean_tendency: int
    max_hp: int
    vehicle_type: int
    tribe_type: int
    level: int
    body_size: int
    # From the end of voice_bank, then from the end of holdable_item_keys.
    holdable_item_count: int
    contents_group_count: int
    # Bytes from the end of contents_group_hashes to the end of the payload.
    tail_size: int
    # vehicle_type on every row that is not a vehicle (`_common/vehicle_type.py`).
    no_vehicle_type: int
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


LAYOUT_3 = RecordLayout(
    3,
    character_fields_size=0x11F,
    character_id=0x01, character_group=0x03, npc_kind=0x05, grade=0x06,
    tendency_on_dead=0x07, ocean_tendency=0x0B, max_hp=0x21, vehicle_type=0xA6, tribe_type=0xB3,
    level=0xC3, body_size=0xDB,
    holdable_item_count=0x0E, contents_group_count=0x18, tail_size=0x18,
    no_vehicle_type=NO_VEHICLE_TYPE,
    clients=(ClientRange(3464),),
)
# Layout 3 without unknown_c7 after level and without the last tail byte.
LAYOUT_2 = RecordLayout(
    2,
    character_fields_size=0x117,
    character_id=0x01, character_group=0x03, npc_kind=0x05, grade=0x06,
    tendency_on_dead=0x07, ocean_tendency=0x0B, max_hp=0x21, vehicle_type=0xA6, tribe_type=0xB3,
    level=0xC3, body_size=0xD3,
    holdable_item_count=0x0E, contents_group_count=0x18, tail_size=0x17,
    no_vehicle_type=NO_VEHICLE_TYPE,
    clients=(ClientRange(3335, 3458),),
)
LAYOUT_1 = RecordLayout(
    1,
    character_fields_size=0x12A,
    character_id=0x02, character_group=0x04, npc_kind=0x06, grade=0x07,
    tendency_on_dead=0x08, ocean_tendency=0x0C, max_hp=0x22, vehicle_type=0xB9, tribe_type=0xC6,
    level=0xD5, body_size=0xE5,
    holdable_item_count=0x1E, contents_group_count=0x28, tail_size=0x13,
    no_vehicle_type=NO_VEHICLE_TYPE_OLD,
    clients=(ClientRange(1685, 2011),),
)
# Newest first.
LAYOUTS = (LAYOUT_3, LAYOUT_2, LAYOUT_1)
