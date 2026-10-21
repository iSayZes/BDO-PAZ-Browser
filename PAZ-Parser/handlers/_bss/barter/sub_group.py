"""Sub group references: which `bartersubgroup.bss` group a barter row names.

Both lists of `bartersubgroup.bss` number their groups from 1, so a key alone
is ambiguous; `sub_group_ref()` adds the list. `bartersubgroup.bss` records
carry it as `sub_group_ref`, and `barter_normal.bss` links each entry to the
first record of its group by that field.
"""

from __future__ import annotations

from _common.html import record_link

SUB_GROUP_FILE = "bartersubgroup.bss"
SUB_GROUP_PATH = f"gamecommondata/binary/{SUB_GROUP_FILE}"
SUB_GROUP_REF_FIELD = "sub_group_ref"
_LINK_CLASS = "record-link"


def sub_group_ref(is_material: bool, barter_sub_group: int) -> str:
    """`trade:12` or `material:3`: the list and the key of one sub group."""
    return f"{'material' if is_material else 'trade'}:{barter_sub_group}"


def sub_group_link(is_material: bool, barter_sub_group: int) -> str:
    """A button showing the key that opens `bartersubgroup.bss` on the group's first entry."""
    ref = sub_group_ref(is_material, barter_sub_group)
    return record_link(str(barter_sub_group), SUB_GROUP_PATH, SUB_GROUP_REF_FIELD, ref, _LINK_CLASS)
