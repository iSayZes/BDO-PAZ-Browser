"""Cell text of the guild tables in `guild_tables.py`."""

from __future__ import annotations

from _common.item_key import item_count_text


_LIST_SEPARATOR = ", "


def grade_text(flags: list[int]) -> str:
    """The member grades whose flag is set: `[1, 1, 0, 0, 0, 0, 1]` -> `0, 1, 6`."""
    return _LIST_SEPARATOR.join(str(grade) for grade, flag in enumerate(flags) if flag)


def reward_item_text(entry: list[int]) -> str:
    """An `[item_key, item_count]` entry as `Gold Bar 1,000G x2`."""
    item_key, item_count = entry
    return item_count_text(item_key, item_count)


def number_list_text(values: list[int]) -> str:
    """`421740, 421740, ...`: every value of a list, in list order."""
    return _LIST_SEPARATOR.join(str(value) for value in values)
