"""Length-prefixed strings embedded in variable-length DBSS blocks.

Several large tables store text inline with an 8-byte prefix: a u32 length
followed by a u32 zero, then the text itself with no terminator. UTF-16 strings
count characters, ASCII strings count bytes.

The strings sit at no fixed offset inside a block, so ASCII text is located by
scanning printable runs and confirming the length that precedes each candidate.
"""

from __future__ import annotations

import re

from _common.binary import u32


STRING_PREFIX_SIZE = 8

_MIN_LENGTH = 3
_MAX_LENGTH = 200

_PRINTABLE_RUN = re.compile(rb"[ -~]{3,200}")


def read_prefixed_utf16(data: bytes, prefix_at: int) -> str:
    """Read a UTF-16LE string whose 8-byte prefix starts at `prefix_at`.

    The stored length counts characters, not bytes. Returns an empty string when
    the prefix is not a plausible header or the text runs past the buffer.
    """
    length = u32(data, prefix_at)
    if not _MIN_LENGTH <= length <= _MAX_LENGTH:
        return ""
    if u32(data, prefix_at + 4) != 0:
        return ""

    start = prefix_at + STRING_PREFIX_SIZE
    end = start + length * 2
    if end > len(data):
        return ""

    return data[start:end].decode("utf-16-le", errors="replace")


def find_prefixed_ascii(data: bytes, start: int, end: int) -> list[str]:
    """Return every length-prefixed ASCII string inside `[start, end)`.

    Candidates come from printable runs and are confirmed against the u32 length
    stored 8 bytes before the text.
    """
    found: list[str] = []

    for match in _PRINTABLE_RUN.finditer(data, start, end):
        text_start = match.start()
        prefix_at = text_start - STRING_PREFIX_SIZE
        if prefix_at < start:
            continue

        length = u32(data, prefix_at)
        if not _MIN_LENGTH <= length <= _MAX_LENGTH:
            continue
        if u32(data, prefix_at + 4) != 0:
            continue
        if length > match.end() - text_start or text_start + length > end:
            continue

        found.append(data[text_start:text_start + length].decode("ascii"))

    return found
