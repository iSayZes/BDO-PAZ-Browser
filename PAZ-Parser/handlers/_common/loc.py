from __future__ import annotations

import re
import struct
import zlib

from _common.binary import u32

_PA_TAG_RE = re.compile(r"<PA[^>]+>")


def strip_pa_tags(text: str) -> str:
    return _PA_TAG_RE.sub("", text)


def decompress_loc(raw: bytes) -> bytes | None:
    try:
        return zlib.decompress(raw[4:])
    except Exception:
        return None


# ── Module-level indices (populated by init_loc) ─────────────────────────────

# (str_type, str_id1, str_id2, str_id3, str_id4) → text
_LOC_INDEX: dict[tuple[int, int, int, int, int], str] | None = None
# (str_type, str_id1) -> text values in file order
_LOC_PREFIX: dict[tuple[int, int], list[str]] | None = None
# all text values in file order
_LOC_ALL:   list[str] | None = None


def init_loc(raw: bytes) -> None:
    """Parse languagedata_en.loc once at startup. Safe to call again on reload."""
    global _LOC_INDEX, _LOC_PREFIX, _LOC_ALL

    data = decompress_loc(raw)
    if data is None:
        return

    index:     dict[tuple[int, int, int, int, int], str] = {}
    prefix:    dict[tuple[int, int], list[str]] = {}
    all_texts: list[str] = []

    pos = 0
    while pos + 16 <= len(data):
        str_size = u32(data, pos)
        str_type = u32(data, pos + 4)
        str_id1  = u32(data, pos + 8)
        str_id2  = struct.unpack_from("<H", data, pos + 12)[0]
        str_id3  = data[pos + 14]
        str_id4  = data[pos + 15]
        text_end = pos + 16 + str_size * 2

        if text_end + 4 > len(data):
            break

        text = data[pos + 16:text_end].decode("utf-16-le", errors="replace")
        pos = text_end + 4

        index[(str_type, str_id1, str_id2, str_id3, str_id4)] = text
        prefix.setdefault((str_type, str_id1), []).append(text)
        all_texts.append(text)

    _LOC_INDEX  = index
    _LOC_PREFIX = prefix
    _LOC_ALL    = all_texts


# ── Public API ────────────────────────────────────────────────────────────────

def is_loc_loaded() -> bool:
    return _LOC_INDEX is not None


def loc_lookup(
    str_type: int,
    str_id1: int,
    str_id2: int = 0,
    str_id3: int = 0,
    str_id4: int = 0,
) -> str:
    """Return matching string or '' on miss / not loaded."""
    if _LOC_INDEX is None:
        return ""
    return _LOC_INDEX.get((str_type, str_id1, str_id2, str_id3, str_id4), "")


def loc_lookup_prefix(str_type: int, str_id1: int) -> list[str]:
    """Return all strings matching a type/id1 pair in LOC index order."""
    if _LOC_PREFIX is None:
        return []

    return list(_LOC_PREFIX.get((str_type, str_id1), []))


def loc_all_texts() -> list[str]:
    """All text values in file order — for content-based scanning."""
    if _LOC_ALL is None:
        return []
    return _LOC_ALL
