"""Records of the action chart views: one per action, or one per shared element."""

from __future__ import annotations

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


def chart_records(chart: Chart, extra_names: list[str]) -> list[dict]:
    """One record per action; `extra_names` adds strings to resolve action hashes with."""
    names = string_hashes(chart.strings + extra_names)
    records = []
    for package in chart.packages:
        for action in package.actions:
            element = action.get("element")
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
