"""Player class types and their LOC type 21 names.

A class type is the number `getClassType()` returns: `0` Warrior, `4` Ranger,
`8` Sorceress, `32` Seraph. Skill tables store sets of them as a bit mask
where bit `n` is class type `n`. See docs/file-formats/skillsimply_dbss.md.
"""

from __future__ import annotations

from _common.loc import loc_text

LOC_CLASS = 21
# Every bit a class can use; skills open to all classes store this mask.
ALL_CLASSES_MASK = 0x7FFF_FFFF_FFFF
# Every playable class on client 3458 (types 0 to 35 without the unused 13,
# 14, 18 and 22); equipment for all classes stores this mask. A new class adds
# its bit to such items, so test for a superset, not equality.
PLAYABLE_CLASSES_MASK = 0xF_FFBB_9FFF


def class_name(class_type: int) -> str:
    """LOC type 21 name of a class type, else the number."""
    return loc_text(LOC_CLASS, class_type) or str(class_type)


def class_types_in_mask(class_mask: int) -> tuple[int, ...]:
    """The class types whose bits are set, lowest first."""
    return tuple(bit for bit in range(class_mask.bit_length()) if class_mask >> bit & 1)


def is_all_classes(class_mask: int) -> bool:
    """Whether the mask allows every playable class."""
    return class_mask & PLAYABLE_CLASSES_MASK == PLAYABLE_CLASSES_MASK


def class_names(class_mask: int) -> list[str]:
    """LOC names of the playable classes in the mask, lowest type first."""
    return [class_name(class_type) for class_type in class_types_in_mask(class_mask & PLAYABLE_CLASSES_MASK)]


def classes_label(class_mask: int, all_label: str) -> str:
    """`all_label` when every playable class may use it, else the class names; '' for none."""
    return all_label if is_all_classes(class_mask) else ", ".join(class_names(class_mask))
