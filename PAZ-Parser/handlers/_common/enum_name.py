"""Display names of client `CppEnums` values.

Tables that store an enum value keep the member names in order from `0`,
without the member prefix, as listed in `global_define_cpp_enum.luac`.
"""

from __future__ import annotations


def enum_name(names: tuple[str, ...], value: int) -> str:
    """The member name of `value`, or the bare value outside the enum."""
    return names[value] if 0 <= value < len(names) else str(value)
