from __future__ import annotations

import codecs
import struct
import zlib
from collections.abc import Mapping
from types import MappingProxyType

from _common.data_deps import LOC, note_read
# Re-exported: handlers import strip_pa_tags from here.
from _common.pa_text import strip_pa_tags as strip_pa_tags
from _common.string_hash import key_hash
from _common.text_bind import LOC_TEXT_BIND, MARKER, TEXT_BIND_VARIANT, fill_text_binds, korean_text_bind

# Some LOC keys store this literal instead of a text.
LOC_NULL = "<null>"

# Record header: text length in UTF-16 units, str_type, str_id1 to str_id4.
_RECORD_HEADER = struct.Struct("<IIIHBB")
# A u32 terminator, always 0, follows every text.
_RECORD_TRAILER_SIZE = 4
# The file starts with the exact size of the decompressed record stream.
_FILE_HEADER = struct.Struct("<I")
# LOC text compresses about 6x; a header claiming more than this is not
# trusted as the buffer size (zlib still grows the buffer when it needs to).
_MAX_COMPRESSION_RATIO = 32
# Compressed bytes inflated per step while indexing, about 24 MB of records:
# 1 MB pieces were 3% slower than one whole decompress, 4 MB about 2%, at the
# same peak memory.
_STREAM_CHUNK_BYTES = 4 * 1024 * 1024

LocKey = tuple[int, int, int, int, int]
LocIndex = dict[LocKey, str]
LocPrefix = dict[tuple[int, int], list[str]]


def decompress_loc(raw: bytes) -> bytes | None:
    """The record stream of a LOC file, or None when it does not decompress.

    zlib gets the output size from the header up front: without it, it grows
    its buffer as it goes and peaks at over twice the output (516 MB for the
    228 MB English stream, against 228 MB). The view avoids copying the input.
    """
    if len(raw) < _FILE_HEADER.size:
        return None
    (size,) = _FILE_HEADER.unpack_from(raw)
    bufsize = max(1, min(size, len(raw) * _MAX_COMPRESSION_RATIO))
    try:
        return zlib.decompress(memoryview(raw)[_FILE_HEADER.size :], bufsize=bufsize)
    except zlib.error:
        return None


# ── Module-level indices (populated by init_loc) ─────────────────────────────

# (str_type, str_id1, str_id2, str_id3, str_id4) → text
_LOC_INDEX: LocIndex | None = None
# (str_type, str_id1) -> text values in file order
_LOC_PREFIX: LocPrefix | None = None
# str_type -> its keys and texts, built on the first `loc_type_entries()` call
# for the `_LOC_INDEX` held in `_LOC_BY_TYPE_SOURCE`
_LOC_BY_TYPE: dict[int, Mapping[tuple[int, int, int, int, int], str]] = {}
_LOC_BY_TYPE_SOURCE: object | None = None


def init_loc(raw: bytes | None) -> None:
    """Parse a languagedata_*.loc file. Pass None to clear all LOC data."""
    global _LOC_INDEX, _LOC_PREFIX, _LOC_BY_TYPE_SOURCE

    # Let go of the old index's per-type copies now, not on the next lookup.
    _LOC_BY_TYPE.clear()
    _LOC_BY_TYPE_SOURCE = None
    if raw is None:
        _LOC_INDEX = None
        _LOC_PREFIX = None
        return

    indexed = _index_stream(raw)
    if indexed is None:
        return

    _LOC_INDEX, _LOC_PREFIX = indexed


def _index_stream(raw: bytes) -> tuple[LocIndex, LocPrefix] | None:
    """The key index and prefix lists of a LOC file, or None when it does not decompress.

    The record stream is inflated a piece at a time and indexed as it
    arrives, so the whole stream (228 MB in English) never sits in memory next
    to the index built from it. A truncated zlib stream is refused, as
    `decompress_loc()` refuses it.
    """
    if len(raw) < _FILE_HEADER.size:
        return None
    index: LocIndex = {}
    prefix: LocPrefix = {}
    decompressor = zlib.decompressobj()
    compressed = memoryview(raw)[_FILE_HEADER.size :]
    pending = b""
    try:
        for start in range(0, len(compressed), _STREAM_CHUNK_BYTES):
            pending += decompressor.decompress(compressed[start : start + _STREAM_CHUNK_BYTES])
            pending = pending[_index_records(pending, index, prefix) :]
        pending += decompressor.flush()
    except zlib.error:
        return None
    if not decompressor.eof:
        return None
    _index_records(pending, index, prefix)
    return index, prefix


def _index_records(data: bytes, index: LocIndex, prefix: LocPrefix) -> int:
    """Add every whole record of `data` to `index` and `prefix`; the bytes used.

    A record cut off at the end of `data` is left for the next piece. Runs
    once per text, 1.4 million times on an English client, so the header is
    one precompiled unpack (the loop condition already checks its bounds),
    the decoder is called without the codec lookup `bytes.decode` does, and a
    prefix list is only built for a new key.
    """
    unpack_header = _RECORD_HEADER.unpack_from
    header_size = _RECORD_HEADER.size
    decode = codecs.utf_16_le_decode
    data_size = len(data)

    pos = 0
    while pos + header_size <= data_size:
        str_size, str_type, str_id1, str_id2, str_id3, str_id4 = unpack_header(data, pos)
        text_start = pos + header_size
        text_end = text_start + str_size * 2
        if text_end + _RECORD_TRAILER_SIZE > data_size:
            break

        text = decode(data[text_start:text_end], "replace")[0]
        pos = text_end + _RECORD_TRAILER_SIZE

        index[(str_type, str_id1, str_id2, str_id3, str_id4)] = text
        texts = prefix.get((str_type, str_id1))
        if texts is None:
            prefix[(str_type, str_id1)] = [text]
        else:
            texts.append(text)

    return pos


# ── Public API ────────────────────────────────────────────────────────────────

def is_loc_loaded() -> bool:
    note_read(LOC)
    return _LOC_INDEX is not None


def loc_lookup(
    str_type: int,
    str_id1: int,
    str_id2: int = 0,
    str_id3: int = 0,
    str_id4: int = 0,
) -> str:
    """Return matching string or '' on miss / not loaded, TextBinds filled."""
    note_read(LOC)
    if _LOC_INDEX is None:
        return ""
    return _filled(_LOC_INDEX.get((str_type, str_id1, str_id2, str_id3, str_id4), ""))


def text_bind_tagged(name: str) -> str:
    """Text of one TextBind name with its PA tags: LOC type 59, else the Korean
    `textbind.dbss` text, else ''. Placeholders inside it are filled too."""
    return resolve_text_binds(_text_bind_raw(name))


def resolve_text_binds(text: str) -> str:
    """`text` with every TextBind placeholder that has a text replaced by it.

    LOC reads are filled already; this is for inline (Korean) text.
    """
    return fill_text_binds(text, _text_bind_raw)


def _text_bind_raw(name: str) -> str:
    """One TextBind text as stored, its own placeholders not filled yet."""
    if _LOC_INDEX is not None:
        note_read(LOC)
        text = _LOC_INDEX.get((LOC_TEXT_BIND, key_hash(name), 0, 0, TEXT_BIND_VARIANT), "").strip()
        if text:
            return text
    return korean_text_bind(name).strip()


def _filled(text: str) -> str:
    return fill_text_binds(text, _text_bind_raw) if MARKER in text else text


def loc_tagged(str_type: int, str_id1: int, str_id4: int = 0) -> str:
    """Text for a LOC key with its PA tags kept, for `pa_fields`, or '' on miss / not loaded."""
    return loc_lookup(str_type, str_id1, 0, 0, str_id4).strip()


def loc_text(str_type: int, str_id1: int, str_id4: int = 0) -> str:
    """Display text for a LOC key with PA tags removed, or '' on miss / not loaded."""
    return strip_pa_tags(loc_tagged(str_type, str_id1, str_id4)).strip()


def loc_lookup_prefix(str_type: int, str_id1: int) -> list[str]:
    """Return all strings matching a type/id1 pair in LOC index order."""
    note_read(LOC)
    if _LOC_PREFIX is None:
        return []

    return [_filled(text) for text in _LOC_PREFIX.get((str_type, str_id1), [])]


def loc_type_entries(str_type: int) -> Mapping[tuple[int, int, int, int, int], str]:
    """Every key of one type with its text, read-only, or empty when not loaded.

    For types whose keys hold a part no caller knows up front, such as the
    service code in `str_id3` of type 50. The first call per type walks the
    whole index once. Texts have their TextBinds filled, like `loc_lookup()`.
    """
    global _LOC_BY_TYPE_SOURCE

    note_read(LOC)
    if _LOC_INDEX is None:
        return MappingProxyType({})
    if _LOC_BY_TYPE_SOURCE is not _LOC_INDEX:
        _LOC_BY_TYPE.clear()
        _LOC_BY_TYPE_SOURCE = _LOC_INDEX
    entries = _LOC_BY_TYPE.get(str_type)
    if entries is None:
        entries = MappingProxyType({key: _filled(text) for key, text in _LOC_INDEX.items() if key[0] == str_type})
        _LOC_BY_TYPE[str_type] = entries
    return entries
