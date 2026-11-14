"""Named fields of the Layout 1 (client 1784) action data and element parameters.

Offsets are the doc's Action Data, Element Link and Element Parameters
(docs/file-formats/other/actionchart_paac.md, Layout 1). Layout 2 keeps these
blocks as hex: their fields are not checked on client 3483 yet.
"""

from __future__ import annotations

import struct

ACTION_DATA_SIZE = 16
ELEMENT_LINK_SIZE = 19
ELEMENT_PARAMETERS_SIZE = 337

# move_speed, move_speed_dup, frame_count, unknown_0c
_ACTION_DATA = struct.Struct("<fffI")
# element_index, unknown_04, weapon_type, element_group_key
_ELEMENT_LINK = struct.Struct("<IIII")

# (field, struct format, offset) of the named Element Parameters.
_ELEMENT_PARAMETERS: tuple[tuple[str, str, int], ...] = (
    ("start_frame", "f", 0x08),
    ("end_frame", "f", 0x0C),
    ("animation_speed", "f", 0x10),
    ("rotation", "f", 0x1C),
    ("skill_no", "i", 0xE8),
    ("apply_sp", "i", 0xF4),
    ("action_type", "B", 0x114),
    ("move_direction", "B", 0x115),
    ("sp_use_type", "B", 0x116),
    ("apply_speed_buff_type", "B", 0x11D),
    ("navigation_type", "B", 0x135),
    ("item_access_level", "B", 0x141),
)


def action_data_fields(first_data: bytes, second_data: bytes) -> dict:
    """The Action's `first_data` and `second_data` fields; empty for a block of another size."""
    fields: dict = {}
    if len(first_data) == ACTION_DATA_SIZE:
        move_speed, _, frame_count, _ = _ACTION_DATA.unpack(first_data)
        fields.update(move_speed=move_speed, frame_count=frame_count)
    if len(second_data) == ELEMENT_LINK_SIZE:
        element_index, _, weapon_type, element_group_key = _ELEMENT_LINK.unpack_from(second_data)
        fields.update(element_index=element_index, weapon_type=weapon_type, element_group_key=element_group_key)
    return fields


def element_parameter_fields(parameters: bytes) -> dict:
    """The named Element Parameters; empty for a block of another size."""
    if len(parameters) != ELEMENT_PARAMETERS_SIZE:
        return {}
    return {name: struct.unpack_from(f"<{kind}", parameters, offset)[0] for name, kind, offset in _ELEMENT_PARAMETERS}
