"""Records of the action chart views: one per action, or one per shared element."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from _common.html import e
from _common.string_hash import KEY_HASH_SEED, hashlittle
from .parser import Chart, SharedTables

_EMPTY = "-"


def string_hashes(strings: list[str]) -> dict[int, str]:
    """Hash -> text over a file's string table: the action keys are the hashes of action names."""
    names: dict[int, str] = {}
    for text in strings:
        if text and text.isascii():
            # hashlittle, not the cached ascii_key_hash: thousands of strings would flush its cache.
            names.setdefault(hashlittle(text.encode("ascii"), KEY_HASH_SEED), text)
    return names


def _names_action(element: dict, action_hash: int) -> bool:
    name = element["action_name"]
    return name.isascii() and hashlittle(name.encode("ascii"), KEY_HASH_SEED) == action_hash


def _linked_element(action: dict, element_groups: Mapping[int, Sequence[dict]]) -> dict | None:
    """A class chart action's element in the shared tables file, by its Element Link.

    The link is used only when the element is named after the action, so a
    chart built against another shared tables file gets no wrong element.
    """
    elements = element_groups.get(action.get("element_group_key", -1), ())
    index = action.get("element_index", -1)
    if not 0 <= index < len(elements):
        return None
    element = elements[index]
    return element if _names_action(element, action["action_hash"]) else None


def chart_records(
    chart: Chart, extra_names: list[str], element_groups: Mapping[int, Sequence[dict]] | None = None
) -> list[dict]:
    """One record per action.

    `extra_names` adds strings to resolve action hashes with; `element_groups`
    (Element Group key -> elements of the shared tables file) gives an action
    without an element of its own the one its Element Link points at.
    """
    names = string_hashes(chart.strings + extra_names)
    groups = element_groups or {}
    records = []
    for package in chart.packages:
        for action in package.actions:
            element = action.get("element") or _linked_element(action, groups)
            record = {
                "action_hash": action["action_hash"],
                "action_name": element["action_name"] if element else names.get(action["action_hash"], ""),
                "package_hash": package.package_hash,
                "package_path": package.package_path,
                "animation": element["animation"] if element else "",
                **{key: value for key, value in action.items() if key not in ("action_hash", "element")},
            }
            if element:
                record.update({key: value for key, value in element.items() if key not in ("action_name", "animation")})
            records.append(record)
    return records


def shared_element_records(tables: SharedTables) -> list[dict]:
    return [
        {"key": group.key, **element}
        for group in tables.groups
        for element in group.elements
    ]


def hash_cell(value: int) -> str:
    """A u32 hash as the docs write it, `0x95E46D94`."""
    return f"0x{value:08X}"


def text_cell(value: str) -> str:
    return e(value) if value else _EMPTY
