"""The Offset column forms of docs/format-docs.md."""
from __future__ import annotations

import re
from dataclasses import dataclass

_FIELD = r"[a-z][a-z0-9_]*"
_OFFSET = re.compile(rf"^`?(?:(?P<anchor>{_FIELD}|end|EOF)(?P<sign>[+-])|\+)0x(?P<value>[0-9A-Fa-f]+)`?$")


@dataclass(frozen=True)
class Offset:
    """`anchor` is None for the structure start, `end` / `EOF` for the end, else a field name."""

    anchor: str | None
    value: int

    @property
    def is_from_end(self) -> bool:
        return self.anchor in ("end", "EOF")


def parse_offset(text: str) -> Offset | str:
    """The parsed Offset cell, or the reason it is not one of the forms."""
    match = _OFFSET.match(text)
    if not match:
        return f"`{text.strip('`')}` is not an offset; use `+0xNN`, `field+0xNN`, `end-0xNN` or `EOF-0xNN`"
    anchor = match.group("anchor")
    sign = match.group("sign")
    if anchor in ("end", "EOF") and sign != "-":
        return f"`{text.strip('`')}` counts back from the end, so it takes `-`"
    if anchor not in (None, "end", "EOF") and sign != "+":
        return f"`{text.strip('`')}` counts on from a field, so it takes `+`"
    return Offset(anchor, int(match.group("value"), 16))
