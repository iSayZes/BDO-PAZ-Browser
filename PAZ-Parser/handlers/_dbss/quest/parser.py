from __future__ import annotations

import re
from dataclasses import dataclass

from _common.binary import u32 as _u32
from .model import QuestRecord


_MAX_SCRIPT_CHARS = 20_000
_MAX_OBJECTIVE_SCAN = 1024
_ICON_RE = re.compile(rb"Icon/[A-Za-z0-9_./ \-]+\.dds", re.IGNORECASE)

# Magic marker that precedes [link_type u32][canonical_quest_id u32] in every
# quest payload.  link_type values 0–31 are valid; larger values are noise.
_CANONICAL_MAGIC = b"\x30\xae\x3b\x00"
_MAX_LINK_TYPE = 31


@dataclass(frozen=True)
class QuestIndex:
    declared_count: int
    starts: list[int]
    record_starts: list[int | None]
    record_ends: list[int]
    icon_paths: list[str]
    canonical_quest_ids: list[int]


def _canonical_quest_id(data: bytes, start: int, end: int) -> int:
    """Return the canonical display quest ID embedded in the record payload.

    Each record contains a sub-record at the position of _CANONICAL_MAGIC with
    layout [magic 4B][link_type u32][canonical_packed_quest_id u32].
    link_type values <= _MAX_LINK_TYPE are real; larger values are noise from
    the magic bytes appearing by coincidence in compressed/Korean text data.
    Returns 0 when not found.
    """
    chunk = data[start:min(end, len(data))]
    p = 0
    while True:
        p = chunk.find(_CANONICAL_MAGIC, p)
        if p == -1:
            return 0
        if p + 12 <= len(chunk):
            link_type = _u32(chunk, p + 4)
            cid = _u32(chunk, p + 8)
            if link_type <= _MAX_LINK_TYPE and cid != 0:
                return cid
        p += 1


def _is_text_clean(text: str) -> bool:
    return "\ufffd" not in text and all(ch >= " " or ch in "\n\r\t" for ch in text)


def _read_utf16_field(
    data: bytes,
    offset: int,
    max_chars: int = _MAX_SCRIPT_CHARS,
) -> tuple[str, int] | None:
    if offset + 8 > len(data):
        return None

    char_count = _u32(data, offset)
    zero = _u32(data, offset + 4)
    byte_count = char_count * 2
    text_start = offset + 8
    text_end = text_start + byte_count

    if zero != 0 or char_count > max_chars or text_end > len(data):
        return None

    text = data[text_start:text_end].decode("utf-16-le", errors="replace")
    if not _is_text_clean(text):
        return None

    return text, text_end


def _find_objective_field(data: bytes, offset: int) -> tuple[str, int] | None:
    scan_end = min(len(data) - 8, offset + _MAX_OBJECTIVE_SCAN)

    for candidate in range(offset, scan_end + 1):
        if any(data[offset:candidate]):
            break
        parsed = _read_utf16_field(data, candidate, max_chars=5000)
        if parsed is None:
            continue
        text, end = parsed
        if text:
            return text, end

    return None


def _parse_fixed_strings(data: bytes, offset: int) -> tuple[str, str, str, int] | None:
    condition = _read_utf16_field(data, offset + 12)
    if condition is None:
        return None

    condition_script, pos = condition
    action = _read_utf16_field(data, pos)
    if action is None:
        return None

    action_script, pos = action
    objective = _find_objective_field(data, pos)
    if objective is None:
        return condition_script, action_script, "", pos

    objective_text_kr, pos = objective
    return condition_script, action_script, objective_text_kr, pos


def _looks_like_relaxed_quest_start(data: bytes, offset: int) -> bool:
    if offset + 24 > len(data):
        return False

    quest_id_a = _u32(data, offset)
    quest_id_b = _u32(data, offset + 4)
    if quest_id_a == 0 or quest_id_b == 0 or _u32(data, offset + 8) != 0:
        return False

    parsed = _parse_fixed_strings(data, offset)
    if parsed is None:
        return False

    condition_script, action_script, _objective_text_kr, _pos = parsed
    return bool(condition_script or action_script)


def _find_record_start_before_icon(data: bytes, start: int, end: int) -> int | None:
    offset = start + (start & 1)
    while offset + 24 <= end:
        if _looks_like_relaxed_quest_start(data, offset):
            return offset
        offset += 2
    return None


def build_quest_index(data: bytes) -> QuestIndex:
    if len(data) < 4:
        return QuestIndex(0, [], [], [], [], [])

    declared_count = _u32(data, 0)
    icons = list(_ICON_RE.finditer(data))

    if not icons:
        return QuestIndex(declared_count, [], [], [], [], [])

    record_starts: list[int | None] = []
    icon_paths: list[str] = []
    canonical_quest_ids: list[int] = []

    for index, icon in enumerate(icons):
        window_start = 4 if index == 0 else icons[index - 1].end() + 1
        record_starts.append(_find_record_start_before_icon(data, window_start, icon.start()))
        icon_paths.append(icon.group(0).decode("ascii", errors="replace"))
        canonical_quest_ids.append(_canonical_quest_id(data, window_start, icon.start()))

    record_ends: list[int] = []
    for index, start in enumerate(record_starts):
        next_start = next((value for value in record_starts[index + 1:] if value is not None), len(data))
        record_ends.append(next_start if start is None or next_start > start else len(data))

    starts = [start for start in record_starts if start is not None]
    return QuestIndex(declared_count, starts, record_starts, record_ends, icon_paths, canonical_quest_ids)


def _icon_path(data: bytes, start: int, end: int) -> str:
    match = None
    for match in _ICON_RE.finditer(data, start, end):
        pass

    if match is None:
        return ""

    return match.group(0).decode("ascii", errors="replace")


def parse_quest_record(
    data: bytes,
    row: int,
    start: int,
    end: int,
    canonical_id: int = 0,
    loc_texts: list[str] | None = None,
) -> QuestRecord | None:
    parsed = _parse_fixed_strings(data, start)
    if parsed is None:
        return None

    condition_script, action_script, objective_text_kr, _pos = parsed
    packed_quest_id = canonical_id or _u32(data, start)

    return QuestRecord(
        row=row,
        offset=start,
        size=max(0, end - start),
        packed_quest_id=packed_quest_id,
        quest_chain_id=packed_quest_id & 0xFFFF,
        quest_id=packed_quest_id >> 16,
        condition_script=condition_script,
        action_script=action_script,
        objective_text_kr=objective_text_kr,
        icon_path=_icon_path(data, start, end),
        loc_texts_en=loc_texts or [],
    )


def parse_quest_records(data: bytes) -> list[QuestRecord]:
    index = build_quest_index(data)
    records: list[QuestRecord] = []

    for row, start in enumerate(index.record_starts):
        if start is None:
            continue
        end = index.record_ends[row]
        record = parse_quest_record(data, row, start, end)
        if record is not None:
            records.append(record)

    return records
