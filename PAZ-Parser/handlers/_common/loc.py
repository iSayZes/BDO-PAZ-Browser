from __future__ import annotations

import re
import zlib

from _dbss.common.binary import u32

_PA_TAG_RE = re.compile(r"<PA[^>]+>")


def strip_pa_tags(text: str) -> str:
    return _PA_TAG_RE.sub("", text)


def decompress_loc(raw: bytes) -> bytes | None:
    try:
        return zlib.decompress(raw[4:])
    except Exception:
        return None


def parse_loc_entries(raw: bytes) -> list[str]:
    data = decompress_loc(raw)

    if data is None:
        return []

    entries: list[str] = []
    pos = 0

    while pos + 20 <= len(data):
        str_len = u32(data, pos)
        text_start = pos + 16
        text_end = text_start + str_len * 2

        if text_end + 4 > len(data):
            break

        text = data[text_start:text_end].decode("utf-16-le", errors="ignore")

        if text and text != "<null>":
            entries.append(text)

        pos = text_end + 4

    return entries


def parse_loc_titles(raw: bytes) -> dict[int, tuple[str, str]]:
    """Return {str_id1: (name, requirement)} for str_type=1 entries."""
    data = decompress_loc(raw)

    if data is None:
        return {}

    buckets: dict[int, list[str]] = {}
    pos = 0

    while pos + 16 <= len(data):
        str_size = u32(data, pos)
        str_type = u32(data, pos + 4)
        str_id1 = u32(data, pos + 8)

        text_start = pos + 16
        text_end = text_start + str_size * 2

        if text_end + 4 > len(data):
            break

        if str_type == 1:
            text = data[text_start:text_end].decode("utf-16-le", errors="replace")
            buckets.setdefault(str_id1, []).append(text)

        pos = text_end + 4

    return {
        str_id: (
            texts[0],
            strip_pa_tags(texts[1]) if len(texts) > 1 else "",
        )
        for str_id, texts in buckets.items()
    }
