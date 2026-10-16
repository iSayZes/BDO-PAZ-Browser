"""The Field column rules of docs/format-docs.md."""
from __future__ import annotations

import re

from .model import Field

UNKNOWN_PREFIX = "unknown_"
# The offset-file row fields that place and size a structure sized by that file.
OFFSET_FIELD = re.compile(r"^(?:[a-z0-9_]+_)?offset$")
SIZE_FIELD = re.compile(r"^(?:[a-z0-9_]+_)?size$")
PABR_TRAILER_ZERO = "zero"
_SNAKE = re.compile(r"^[a-z][a-z0-9_]*$")
_PADDING = re.compile(r"^padding_[0-9a-f]{2,}$")
_PADDING_PROOF = re.compile(r"pdb|align", re.IGNORECASE)
# Names that state a value or a guess in place of a meaning.
_VALUE_NAMES = (
    (re.compile(r"^(reserved|pad|padding)(\d|_|$)"), "a `padding_<hex>` with its proof, or `unknown_<hex>`"),
    (re.compile(r"^const(\d|_|$)"), "`unknown_<hex>`; the value goes in Notes"),
    (re.compile(r"(^|_)zero(_|$)"), "`unknown_<hex>`; the value goes in Notes"),
    (re.compile(r"^flag_[0-9a-f]+$"), "`unknown_<hex>` until the flag's meaning is known"),
)


def name_problems(field: Field, names: frozenset[str], is_top_level: bool) -> tuple[str, ...]:
    """What is wrong with `field.name`; `names` holds every name of its structure."""
    name = field.name.strip("`")
    if not _SNAKE.match(name):
        return (f"`{name}` is not one snake_case name",)
    if name == "unknown":
        return ("a bare `unknown`; add the offset, `unknown_<hex>`",)
    if name.endswith("_ko"):
        return (f"`{name}`: Korean text ends in `_kr`",)
    if _PADDING.match(name):
        return () if _PADDING_PROOF.search(field.notes) else (f"`{name}` needs its proof (PDB or alignment) in Notes",)
    if name == PABR_TRAILER_ZERO:
        return () if is_top_level else ("`zero` is only the PABR string-table trailer u32",)
    for pattern, advice in _VALUE_NAMES:
        if pattern.search(name):
            return (f"`{name}` states a value, not a meaning; use {advice}",)
    return _reference_problems(name, names)


def _reference_problems(name: str, names: frozenset[str]) -> tuple[str, ...]:
    """A `_dup` or `unknown_after_` name must point at a field of the same structure."""
    dup = re.match(r"^(?P<base>.+)_dup\d*$", name)
    if dup and dup.group("base") not in names:
        return (f"`{name}` copies `{dup.group('base')}`, which is not in this structure",)
    after = re.match(r"^unknown_after_(?P<base>.+)$", name)
    if after and after.group("base") not in names:
        return (f"`{name}` follows `{after.group('base')}`, which is not in this structure",)
    return ()
